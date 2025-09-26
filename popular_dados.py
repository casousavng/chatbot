#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🧻 Script para Popular Bases de Dados - Chatbot PaperCare
Cria dados de exemplo para demonstração do dashboard e funcionalidades
"""

import sqlite3
import json
import random
from datetime import datetime, timedelta
from typing import List, Dict

# Dados de exemplo para popular as bases de dados
NOMES_EXEMPLO = [
    "João Silva", "Maria Santos", "António Costa", "Ana Ferreira", "Carlos Pereira",
    "Sofia Oliveira", "Miguel Rodrigues", "Catarina Alves", "Pedro Gonçalves", "Inês Martins",
    "Ricardo Sousa", "Beatriz Lima", "Tiago Carvalho", "Joana Ribeiro", "Bruno Dias",
    "Marta Fernandes", "André Lopes", "Teresa Mendes", "Hugo Barbosa", "Cristina Rocha"
]

EMPRESAS_EXEMPLO = [
    "Supermercados Continente", "Pingo Doce", "Lidl Portugal", "Auchan",
    "Hotel Vila Galé", "Pestana Hotels", "TAP Air Portugal", "NOS",
    "Vodafone Portugal", "MEO", "Banco Santander", "CGD",
    "Sonae MC", "Jerónimo Martins", "EDP", "Galp Energia",
    "Café Delta", "Compal", "Unicer", "Super Bock Group"
]

DOMINIOS_EMAIL = ["gmail.com", "hotmail.com", "sapo.pt", "outlook.com", "empresa.pt"]

PRODUTOS = ["1 Folha", "2 Folhas", "3 Folhas Premium"]

MERCADOS = ["Retalho", "Hotelaria", "Escritórios", "Restauração", "Saúde"]

ESPECIALISTAS = [
    "ana.silva@papercare.pt", "joao.costa@papercare.pt", "sofia.santos@papercare.pt",
    "miguel.ferreira@papercare.pt", "carla.oliveira@papercare.pt"
]

CATEGORIAS_RECLAMACAO = ["produto", "atendimento", "entrega", "preço", "qualidade"]

MENSAGENS_RECLAMACAO = [
    "O produto chegou danificado e quero uma substituição",
    "O papel é muito fino e rasga facilmente",  
    "A entrega demorou mais do que prometido",
    "O preço aumentou muito desde o mês passado",
    "A qualidade não corresponde ao que foi descrito",
    "Não recebi a encomenda no prazo indicado",
    "O papel não é tão absorvente como esperava",
    "Falta de stock constante nos supermercados",
    "Embalagem não é sustentável como prometido",
    "Atendimento ao cliente pouco profissional"
]

def gerar_telefone() -> str:
    """Gera um número de telefone português realista"""
    prefixos = ["91", "92", "93", "96"]
    prefixo = random.choice(prefixos)
    numero = ''.join([str(random.randint(0, 9)) for _ in range(7)])
    return f"+351 {prefixo} {numero[:3]} {numero[3:]}"

def gerar_email(nome: str) -> str:
    """Gera email baseado no nome"""
    nome_parts = nome.lower().split()
    if len(nome_parts) >= 2:
        email_user = f"{nome_parts[0]}.{nome_parts[1]}"
    else:
        email_user = nome_parts[0]
    
    # Remover acentos
    replacements = {
        'ã': 'a', 'á': 'a', 'à': 'a', 'â': 'a',
        'é': 'e', 'ê': 'e', 'è': 'e',
        'í': 'i', 'î': 'i', 'ì': 'i',
        'ó': 'o', 'ô': 'o', 'õ': 'o', 'ò': 'o',
        'ú': 'u', 'û': 'u', 'ù': 'u',
        'ç': 'c'
    }
    
    for old, new in replacements.items():
        email_user = email_user.replace(old, new)
    
    dominio = random.choice(DOMINIOS_EMAIL)
    return f"{email_user}@{dominio}"

def gerar_timestamp_recente(dias_atras: int = 30) -> str:
    """Gera timestamp recente para simular atividade"""
    agora = datetime.now()
    tempo_aleatorio = agora - timedelta(
        days=random.randint(0, dias_atras),
        hours=random.randint(0, 23),
        minutes=random.randint(0, 59)
    )
    return tempo_aleatorio.isoformat()

def popular_metricas(cursor: sqlite3.Cursor, num_registos: int = 100):
    """Popula tabela de métricas com dados de exemplo"""
    print(f"📊 Criando {num_registos} registos de métricas...")
    
    for i in range(num_registos):
        conversa_id = f"conversa_{i:04d}"
        tempo_resposta = round(random.uniform(0.5, 5.0), 2)  # 0.5 a 5 segundos
        timestamp = gerar_timestamp_recente()
        
        cursor.execute("""
            INSERT INTO metricas (conversa_id, tempo_resposta, timestamp)
            VALUES (?, ?, ?)
        """, (conversa_id, tempo_resposta, timestamp))

def popular_leads(cursor: sqlite3.Cursor, num_registos: int = 50):
    """Popula tabela de leads com dados de exemplo"""
    print(f"👥 Criando {num_registos} registos de leads...")
    
    status_opcoes = ["novo", "contactado", "convertido", "perdido"]
    
    for i in range(num_registos):
        nome = random.choice(NOMES_EXEMPLO)
        email = gerar_email(nome)
        telefone = gerar_telefone()
        empresa = random.choice(EMPRESAS_EXEMPLO)
        produto = random.choice(PRODUTOS)
        mercado = random.choice(MERCADOS)
        especialista = random.choice(ESPECIALISTAS)
        timestamp = gerar_timestamp_recente()
        status = random.choice(status_opcoes)
        
        cursor.execute("""
            INSERT INTO leads (nome, email, telefone, empresa, produto, mercado, especialista, timestamp, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (nome, email, telefone, empresa, produto, mercado, especialista, timestamp, status))

def popular_satisfacao(cursor: sqlite3.Cursor, num_registos: int = 80):
    """Popula tabela de satisfação com dados de exemplo"""
    print(f"⭐ Criando {num_registos} registos de satisfação...")
    
    for i in range(num_registos):
        conversa_id = f"conversa_{i:04d}"
        # Gerar avaliações com tendência positiva (mais 4-5 estrelas)
        if random.random() < 0.7:  # 70% chance de avaliação boa
            avaliacao = round(random.uniform(4.0, 5.0), 1)
        else:
            avaliacao = round(random.uniform(1.0, 4.0), 1)
        
        timestamp = gerar_timestamp_recente()
        
        cursor.execute("""
            INSERT INTO satisfacao (conversa_id, avaliacao, timestamp)
            VALUES (?, ?, ?)
        """, (conversa_id, avaliacao, timestamp))

def popular_reclamacoes(cursor: sqlite3.Cursor, num_registos: int = 25):
    """Popula tabela de reclamações com dados de exemplo"""
    print(f"📝 Criando {num_registos} registos de reclamações...")
    
    status_opcoes = ["nova", "em_andamento", "resolvida", "fechada"]
    
    for i in range(num_registos):
        conversa_id = f"conversa_{i:04d}"
        mensagem = random.choice(MENSAGENS_RECLAMACAO)
        categoria = random.choice(CATEGORIAS_RECLAMACAO)
        timestamp = gerar_timestamp_recente()
        status = random.choice(status_opcoes)
        
        cursor.execute("""
            INSERT INTO reclamacoes (conversa_id, mensagem, categoria, timestamp, status)
            VALUES (?, ?, ?, ?, ?)
        """, (conversa_id, mensagem, categoria, timestamp, status))

def popular_conversas_rasa(cursor: sqlite3.Cursor, num_conversas: int = 30):
    """Popula tabela do Rasa tracker com conversas de exemplo"""
    print(f"💬 Criando {num_conversas} conversas de exemplo no Rasa...")
    
    # Verificar o maior ID existente
    cursor.execute("SELECT MAX(id) FROM events")
    max_id = cursor.fetchone()[0]
    event_id = (max_id + 1) if max_id else 1
    
    print(f"   Começando com event_id: {event_id}")
    
    intents_exemplo = [
        "saudacao", "tipos_papel", "precos", "sustentabilidade", 
        "onde_comprar", "horario_atendimento", "qualidade_papel",
        "empresa_desconto", "reclamacao", "garantia", "info_tecnica"
    ]
    
    actions_exemplo = [
        "utter_saudacao", "utter_tipos_papel", "utter_precos", 
        "utter_sustentabilidade", "utter_onde_comprar", "utter_horario_atendimento"
    ]
    
    for i in range(num_conversas):
        sender_id = f"user_{i:04d}"
        
        # Criar eventos de uma conversa típica
        num_eventos = random.randint(3, 8)  # 3 a 8 interações por conversa
        
        for j in range(num_eventos):
            timestamp = datetime.now().timestamp() - random.randint(0, 2592000)  # Últimos 30 dias
            
            if j % 2 == 0:  # Mensagem do usuário
                intent_name = random.choice(intents_exemplo)
                data = json.dumps({
                    "text": f"Mensagem de exemplo {j}",
                    "intent": {"name": intent_name, "confidence": round(random.uniform(0.85, 0.99), 3)},
                    "entities": []
                })
                
                cursor.execute("""
                    INSERT INTO events (id, sender_id, type_name, timestamp, intent_name, data)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (event_id, sender_id, "user", timestamp, intent_name, data))
                
            else:  # Resposta do bot
                action_name = random.choice(actions_exemplo)
                data = json.dumps({
                    "text": f"Resposta automática do bot",
                    "buttons": []
                })
                
                cursor.execute("""
                    INSERT INTO events (id, sender_id, type_name, timestamp, action_name, data)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (event_id, sender_id, "bot", timestamp, action_name, data))
            
            event_id += 1

def main():
    """Função principal para popular todas as bases de dados"""
    print("🧻 Populando Bases de Dados do Chatbot PaperCare")
    print("=" * 50)
    
    # Conectar à base de dados de KPIs
    print("\n📊 Conectando à base de dados de KPIs...")
    conn_kpis = sqlite3.connect('chatbot_kpis.db')
    cursor_kpis = conn_kpis.cursor()
    
    # Popular tabelas de KPIs
    popular_metricas(cursor_kpis, 150)
    popular_leads(cursor_kpis, 75)
    popular_satisfacao(cursor_kpis, 120)
    popular_reclamacoes(cursor_kpis, 35)
    
    conn_kpis.commit()
    conn_kpis.close()
    
    # Conectar à base de dados do Rasa
    print("\n💬 Conectando à base de dados do Rasa...")
    conn_rasa = sqlite3.connect('rasa_tracker.db')
    cursor_rasa = conn_rasa.cursor()
    
    # Popular conversas do Rasa
    popular_conversas_rasa(cursor_rasa, 50)
    
    conn_rasa.commit()
    conn_rasa.close()
    
    print("\n✅ Bases de dados populadas com sucesso!")
    print("\n📋 Resumo dos dados criados:")
    print("  📊 150 métricas de tempo de resposta")
    print("  👥 75 leads de potenciais clientes")
    print("  ⭐ 120 avaliações de satisfação")
    print("  📝 35 reclamações de exemplo")
    print("  💬 50 conversas com histórico no Rasa")
    print("\n🎯 Agora pode:")
    print("  1. Executar o dashboard: python kpi_dashboard.py")
    print("  2. Iniciar o chatbot: python app.py")
    print("  3. Ver dados no frontend: http://localhost:5020")

if __name__ == "__main__":
    main()