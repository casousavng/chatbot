# -*- coding: utf-8 -*-
"""
Dashboard Simples de KPIs do Chatbot PaperCare
Compativel com Python 2.7 e 3.x
"""

import sqlite3
from datetime import datetime, timedelta

def conectar_db():
    """Conecta a base de dados"""
    return sqlite3.connect('chatbot_kpis.db')

def dashboard():
    """Mostra dashboard completo"""
    print("🧻 Dashboard KPIs - Chatbot PaperCare")
    print("=" * 40)
    
    try:
        conn = conectar_db()
        cursor = conn.cursor()
        
        # Contar registos
        cursor.execute("SELECT COUNT(*) FROM metricas")
        metricas = cursor.fetchone()[0]
        print("📊 Métricas: %d registos" % metricas)
        
        cursor.execute("SELECT COUNT(*) FROM leads")
        leads = cursor.fetchone()[0]
        print("👥 Leads: %d registos" % leads)
        
        cursor.execute("SELECT COUNT(*) FROM satisfacao")
        satisfacao = cursor.fetchone()[0]
        print("⭐ Satisfação: %d registos" % satisfacao)
        
        cursor.execute("SELECT COUNT(*) FROM reclamacoes")
        reclamacoes = cursor.fetchone()[0]
        print("📝 Reclamações: %d registos" % reclamacoes)
        
        print("=" * 40)
        
        # Estatísticas
        cursor.execute("SELECT AVG(tempo_resposta) FROM metricas")
        tempo_medio = cursor.fetchone()[0]
        if tempo_medio:
            print("⏱️  Tempo médio resposta: %.2f s" % tempo_medio)
        
        cursor.execute("SELECT AVG(avaliacao) FROM satisfacao")
        satisfacao_media = cursor.fetchone()[0]
        if satisfacao_media:
            print("⭐ Satisfação média: %.1f/5.0" % satisfacao_media)
        
        # Leads recentes
        print("\n👥 Últimos 5 Leads:")
        print("-" * 30)
        cursor.execute("""
            SELECT nome, empresa, produto, status 
            FROM leads 
            ORDER BY timestamp DESC 
            LIMIT 5
        """)
        
        for lead in cursor.fetchall():
            nome, empresa, produto, status = lead
            print("• %s (%s) - %s [%s]" % (nome, empresa, produto, status))
        
        # Reclamações
        print("\n📝 Reclamações Recentes:")
        print("-" * 30)
        cursor.execute("""
            SELECT mensagem, categoria, status 
            FROM reclamacoes 
            ORDER BY timestamp DESC 
            LIMIT 3
        """)
        
        for rec in cursor.fetchall():
            mensagem, categoria, status = rec
            msg_curta = mensagem[:35] + "..." if len(mensagem) > 35 else mensagem
            print("• [%s] %s [%s]" % (categoria, msg_curta, status))
        
        conn.close()
        print("\n✅ Dashboard atualizado!")
        
    except Exception as e:
        print("❌ Erro: %s" % str(e))
        print("💡 Execute: python resetar_dados.py")

if __name__ == "__main__":
    dashboard()