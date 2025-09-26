# -*- coding: utf-8 -*-
"""
Dashboard Simples de KPIs do Chatbot PaperCare
"""

import sqlite3
from datetime import datetime, timedelta

def conectar_db():
    """Conecta à base de dados"""
    return sqlite3.connect('chatbot_kpis.db')

def contar_tabelas():
    """Conta registos em todas as tabelas"""
    conn = conectar_db()
    cursor = conn.cursor()
    
    print("🧻 Dashboard KPIs - Chatbot PaperCare")
    print("=" * 40)
    
    # Métricas
    cursor.execute("SELECT COUNT(*) FROM metricas")
    metricas = cursor.fetchone()[0]
    print(f"📊 Métricas: {metricas} registos")
    
    # Leads
    cursor.execute("SELECT COUNT(*) FROM leads")
    leads = cursor.fetchone()[0]
    print(f"👥 Leads: {leads} registos")
    
    # Satisfação
    cursor.execute("SELECT COUNT(*) FROM satisfacao")
    satisfacao = cursor.fetchone()[0]
    print(f"⭐ Satisfação: {satisfacao} registos")
    
    # Reclamações  
    cursor.execute("SELECT COUNT(*) FROM reclamacoes")
    reclamacoes = cursor.fetchone()[0]
    print(f"📝 Reclamações: {reclamacoes} registos")
    
    print("\n" + "=" * 40)
    
    # Estatísticas rápidas
    cursor.execute("SELECT AVG(tempo_resposta) FROM metricas")
    tempo_medio = cursor.fetchone()[0]
    if tempo_medio:
        print(f"⏱️  Tempo médio resposta: {tempo_medio:.2f}s")
    
    cursor.execute("SELECT AVG(avaliacao) FROM satisfacao")
    satisfacao_media = cursor.fetchone()[0]
    if satisfacao_media:
        print(f"⭐ Satisfação média: {satisfacao_media:.1f}/5.0")
    
    cursor.execute("SELECT COUNT(*) FROM leads WHERE status='convertido'")
    convertidos = cursor.fetchone()[0]
    if leads > 0:
        taxa_conversao = (convertidos / leads) * 100
        print(f"💰 Taxa conversão: {taxa_conversao:.1f}%")
    
    conn.close()
    print("\n✅ Dashboard atualizado com sucesso!")
    print("💡 Execute novamente para ver dados atualizados")

def mostrar_leads_recentes():
    """Mostra os últimos leads criados"""
    conn = conectar_db()
    cursor = conn.cursor()
    
    print("\n👥 Últimos 5 Leads:")
    print("-" * 50)
    
    cursor.execute("""
        SELECT nome, empresa, produto, status 
        FROM leads 
        ORDER BY timestamp DESC 
        LIMIT 5
    """)
    
    leads = cursor.fetchall()
    for lead in leads:
        nome, empresa, produto, status = lead
        print(f"• {nome} ({empresa}) - {produto} [{status}]")
    
    conn.close()

def mostrar_reclamacoes():
    """Mostra reclamações recentes"""
    conn = conectar_db()
    cursor = conn.cursor()
    
    print("\n📝 Reclamações Recentes:")
    print("-" * 50)
    
    cursor.execute("""
        SELECT mensagem, categoria, status 
        FROM reclamacoes 
        ORDER BY timestamp DESC 
        LIMIT 3
    """)
    
    reclamacoes = cursor.fetchall()
    for reclamacao in reclamacoes:
        mensagem, categoria, status = reclamacao
        print(f"• [{categoria}] {mensagem[:40]}... [{status}]")
    
    conn.close()

if __name__ == "__main__":
    try:
        contar_tabelas()
        mostrar_leads_recentes()
        mostrar_reclamacoes()
    except Exception as e:
        print(f"❌ Erro: {e}")
        print("💡 Certifique-se que executou: python resetar_dados.py")