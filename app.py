# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, jsonify
import requests
import datetime
import sqlite3
import json

app = Flask(__name__)

# URL do teu Rasa server local
RASA_URL = "http://localhost:5005/webhooks/rest/webhook"

def make_request_no_proxy(url, method='GET', **kwargs):
    """Helper function para fazer requests sem proxy"""
    proxies = {'http': '', 'https': ''}
    kwargs['proxies'] = proxies
    if 'timeout' not in kwargs:
        kwargs['timeout'] = 10
    
    if method.upper() == 'POST':
        return requests.post(url, **kwargs)
    else:
        return requests.get(url, **kwargs)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send_message", methods=["POST"])
def send_message():
    user_msg = request.json.get("message")
    sender_id = request.json.get("sender_id", "user")
    
    print("Mensagem recebida do front-end:", user_msg)  # debug
    
    payload = {"sender": sender_id, "message": user_msg}
    
    try:
        # Usar função helper sem proxy
        response = make_request_no_proxy(RASA_URL, method='POST', json=payload)
        print("Resposta Rasa:", response.json())  # debug
        
        if response.status_code == 200:
            rasa_messages = response.json()
            messages = []
            
            for r in rasa_messages:
                if "text" in r:
                    messages.append(r["text"])
                # Suporte para outros tipos de resposta (botões, imagens, etc.)
                elif "buttons" in r:
                    messages.append({"text": r.get("text", ""), "buttons": r["buttons"]})
                elif "image" in r:
                    messages.append({"text": r.get("text", ""), "image": r["image"]})
            
            return jsonify({
                "messages": messages,
                "status": "success"
            })
        else:
            return jsonify({
                "messages": ["Erro na comunicação com o chatbot. Tente novamente."],
                "status": "error"
            })
            
    except Exception as e:
        print("Erro ao comunicar com Rasa: " + str(e))
        return jsonify({
            "messages": ["Serviço temporariamente indisponível. Tente novamente em alguns instantes."],
            "status": "error"
        })

@app.route("/kpis")
def view_kpis():
    """Endpoint para visualizar KPIs do chatbot"""
    try:
        from kpi_dashboard import ChatbotKPIDashboard
        dashboard = ChatbotKPIDashboard()
        relatorio = dashboard.gerar_relatorio_completo(30)
        return jsonify(relatorio)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/admin")
def admin_dashboard():
    """Página de administração com KPIs"""
    return render_template("admin.html")

@app.route("/leads")
def get_leads():
    """Endpoint para obter leads gerados"""
    try:
        conn = sqlite3.connect('chatbot_kpis.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT nome, email, telefone, empresa, produto, mercado, especialista, timestamp, status
            FROM leads
            ORDER BY timestamp DESC
            LIMIT 100
        ''')
        
        leads = []
        for row in cursor.fetchall():
            leads.append({
                'nome': row[0],
                'email': row[1], 
                'telefone': row[2],
                'empresa': row[3],
                'produto': row[4],
                'mercado': row[5],
                'especialista': row[6],
                'timestamp': row[7],
                'status': row[8]
            })
        
        conn.close()
        return jsonify(leads)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/reclamacoes")
def get_reclamacoes():
    """Endpoint para obter reclamações"""
    try:
        conn = sqlite3.connect('chatbot_kpis.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT conversa_id, mensagem, categoria, timestamp, status
            FROM reclamacoes
            ORDER BY timestamp DESC
            LIMIT 50
        ''')
        
        reclamacoes = []
        for row in cursor.fetchall():
            reclamacoes.append({
                'conversa_id': row[0],
                'mensagem': row[1],
                'categoria': row[2],
                'timestamp': row[3],
                'status': row[4]
            })
        
        conn.close()
        return jsonify(reclamacoes)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/health")
def health_check():
    """Health check endpoint"""
    try:
        # Testar conexão com Rasa usando helper function
        response = make_request_no_proxy("http://localhost:5005/", timeout=5)
        rasa_status = "ok" if response.status_code == 200 else "down"
    except:
        rasa_status = "down"
    
    return jsonify({
        "status": "ok",
        "timestamp": datetime.datetime.now().isoformat(),
        "services": {
            "rasa": rasa_status,
            "database": "ok"  # Assume DB always ok for simplicity
        }
    })

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5020)