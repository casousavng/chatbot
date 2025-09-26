#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🧻 Script para Resetar e Popular Bases de Dados - Chatbot PaperCare
Limpa e recria dados de exemplo para demonstração
"""

import sqlite3
import json
import random
from datetime import datetime, timedelta

def resetar_e_popular():
    """Limpa e popula as bases de dados com dados frescos"""
    print("🧻 Resetando e Populando Bases de Dados do Chatbot PaperCare")
    print("=" * 60)
    
    # Base de dados KPIs
    print("\n🗑️  Limpando dados antigos da base KPIs...")
    conn_kpis = sqlite3.connect('chatbot_kpis.db')
    cursor_kpis = conn_kpis.cursor()
    
    # Limpar tabelas
    cursor_kpis.execute("DELETE FROM metricas")
    cursor_kpis.execute("DELETE FROM leads") 
    cursor_kpis.execute("DELETE FROM satisfacao")
    cursor_kpis.execute("DELETE FROM reclamacoes")
    
    print("✅ Dados antigos removidos!")
    
    # Dados de exemplo
    nomes = ["João Silva", "Maria Santos", "António Costa", "Ana Ferreira", "Carlos Pereira"]
    empresas = ["Continente", "Pingo Doce", "Hotel Vila Galé", "Banco Santander", "EDP"]
    
    # Popular métricas (50 registos)
    print("\n📊 Criando 50 métricas...")
    for i in range(50):
        cursor_kpis.execute("""
            INSERT INTO metricas (conversa_id, tempo_resposta, timestamp)
            VALUES (?, ?, ?)
        """, (f"conv_{i:03d}", round(random.uniform(0.5, 4.0), 2), 
              datetime.now().isoformat()))
    
    # Popular leads (25 registos)
    print("👥 Criando 25 leads...")
    for i in range(25):
        nome = random.choice(nomes)
        cursor_kpis.execute("""
            INSERT INTO leads (nome, email, telefone, empresa, produto, mercado, especialista, timestamp, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (nome, f"{nome.split()[0].lower()}@empresa.pt", "+351 91 123 456",
              random.choice(empresas), "2 Folhas", "Retalho", "ana@papercare.pt",
              datetime.now().isoformat(), "novo"))
    
    # Popular satisfação (40 registos)
    print("⭐ Criando 40 avaliações...")
    for i in range(40):
        cursor_kpis.execute("""
            INSERT INTO satisfacao (conversa_id, avaliacao, timestamp)
            VALUES (?, ?, ?)
        """, (f"conv_{i:03d}", round(random.uniform(3.5, 5.0), 1),
              datetime.now().isoformat()))
    
    # Popular reclamações (15 registos)
    print("📝 Criando 15 reclamações...")
    reclamacoes = [
        "Produto chegou danificado", "Papel muito fino", "Entrega atrasada",
        "Preço muito alto", "Qualidade inferior ao esperado"
    ]
    for i in range(15):
        cursor_kpis.execute("""
            INSERT INTO reclamacoes (conversa_id, mensagem, categoria, timestamp, status)
            VALUES (?, ?, ?, ?, ?)
        """, (f"conv_{i:03d}", random.choice(reclamacoes), "produto",
              datetime.now().isoformat(), "nova"))
    
    conn_kpis.commit()
    conn_kpis.close()
    
    print("\n✅ Base de dados populada com sucesso!")
    print("\n📋 Resumo:")
    print("  📊 50 métricas de resposta")
    print("  👥 25 leads de clientes")
    print("  ⭐ 40 avaliações de satisfação")  
    print("  📝 15 reclamações")
    print("\n🎯 Execute: python kpi_dashboard.py")

if __name__ == "__main__":
    resetar_e_popular()