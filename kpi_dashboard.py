#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dashboard de KPIs do Chatbot
Monitora métricas de performance, satisfação, conversão e reclamações
"""

import sqlite3
import datetime
import json

class ChatbotKPIDashboard:
    def __init__(self, db_path='chatbot_kpis.db'):
        self.db_path = db_path
        self._init_database()
    
    def _init_database(self):
        """Inicializa as tabelas do banco de dados"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Tabela de métricas
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS metricas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                conversa_id TEXT,
                tempo_resposta REAL,
                timestamp TEXT
            )
        ''')
        
        # Tabela de leads
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS leads (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                email TEXT,
                telefone TEXT,
                empresa TEXT,
                produto TEXT,
                mercado TEXT,
                especialista TEXT,
                timestamp TEXT,
                status TEXT DEFAULT 'novo'
            )
        ''')
        
        # Tabela de satisfação
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS satisfacao (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                conversa_id TEXT,
                avaliacao REAL,
                timestamp TEXT
            )
        ''')
        
        # Tabela de reclamações
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS reclamacoes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                conversa_id TEXT,
                mensagem TEXT,
                categoria TEXT,
                timestamp TEXT,
                status TEXT DEFAULT 'nova'
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def get_tempo_medio_resposta(self, periodo_dias: int = 30) -> float:
        """Calcula o tempo médio de resposta em segundos"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        data_limite = (datetime.datetime.now() - datetime.timedelta(days=periodo_dias)).isoformat()
        
        cursor.execute('''
            SELECT AVG(tempo_resposta) FROM metricas 
            WHERE timestamp >= ?
        ''', (data_limite,))
        
        resultado = cursor.fetchone()[0]
        conn.close()
        
        return resultado or 0.0
    
    def get_taxa_conversao(self, periodo_dias: int = 30) -> float:
        """Calcula a taxa de conversão de vendas"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        data_limite = (datetime.datetime.now() - datetime.timedelta(days=periodo_dias)).isoformat()
        
        # Total de conversas (métricas geradas)
        cursor.execute('''
            SELECT COUNT(DISTINCT conversa_id) FROM metricas 
            WHERE timestamp >= ?
        ''', (data_limite,))
        total_conversas = cursor.fetchone()[0] or 0
        
        # Total de leads gerados
        cursor.execute('''
            SELECT COUNT(*) FROM leads 
            WHERE timestamp >= ?
        ''', (data_limite,))
        total_leads = cursor.fetchone()[0] or 0
        
        conn.close()
        
        if total_conversas == 0:
            return 0.0
        
        return (total_leads / total_conversas) * 100
    
    def get_satisfacao_media(self, periodo_dias: int = 30) -> float:
        """Calcula a satisfação média"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        data_limite = (datetime.datetime.now() - datetime.timedelta(days=periodo_dias)).isoformat()
        
        cursor.execute('''
            SELECT AVG(avaliacao) FROM satisfacao 
            WHERE timestamp >= ?
        ''', (data_limite,))
        
        resultado = cursor.fetchone()[0]
        conn.close()
        
        return resultado or 0.0
    
    def get_total_reclamacoes(self, periodo_dias: int = 30) -> int:
        """Conta o total de reclamações"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        data_limite = (datetime.datetime.now() - datetime.timedelta(days=periodo_dias)).isoformat()
        
        cursor.execute('''
            SELECT COUNT(*) FROM reclamacoes 
            WHERE timestamp >= ?
        ''', (data_limite,))
        
        resultado = cursor.fetchone()[0]
        conn.close()
        
        return resultado or 0
    
    def get_reclamacoes_por_categoria(self, periodo_dias=30):
        """Quebra reclamações por categoria"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        data_limite = (datetime.datetime.now() - datetime.timedelta(days=periodo_dias)).isoformat()
        
        cursor.execute('''
            SELECT categoria, COUNT(*) FROM reclamacoes 
            WHERE timestamp >= ?
            GROUP BY categoria
        ''', (data_limite,))
        
        resultados = cursor.fetchall()
        conn.close()
        
        return {categoria: count for categoria, count in resultados}
    
    def get_leads_por_produto(self, periodo_dias=30):
        """Quebra leads por produto"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        data_limite = (datetime.datetime.now() - datetime.timedelta(days=periodo_dias)).isoformat()
        
        cursor.execute('''
            SELECT produto, COUNT(*) FROM leads 
            WHERE timestamp >= ?
            GROUP BY produto
        ''', (data_limite,))
        
        resultados = cursor.fetchall()
        conn.close()
        
        return {produto: count for produto, count in resultados}
    
    def get_leads_por_mercado(self, periodo_dias=30):
        """Quebra leads por mercado"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        data_limite = (datetime.datetime.now() - datetime.timedelta(days=periodo_dias)).isoformat()
        
        cursor.execute('''
            SELECT mercado, COUNT(*) FROM leads 
            WHERE timestamp >= ?
            GROUP BY mercado
        ''', (data_limite,))
        
        resultados = cursor.fetchall()
        conn.close()
        
        return {mercado: count for mercado, count in resultados}
    
    def gerar_relatorio_completo(self, periodo_dias=30):
        """Gera relatório completo dos KPIs"""
        relatorio = {
            'periodo_dias': periodo_dias,
            'data_geracao': datetime.datetime.now().isoformat(),
            'kpis': {
                'tempo_medio_resposta_segundos': round(self.get_tempo_medio_resposta(periodo_dias), 2),
                'taxa_conversao_vendas_percentual': round(self.get_taxa_conversao(periodo_dias), 2),
                'satisfacao_media_estrelas': round(self.get_satisfacao_media(periodo_dias), 2),
                'total_reclamacoes': self.get_total_reclamacoes(periodo_dias)
            },
            'detalhamento': {
                'reclamacoes_por_categoria': self.get_reclamacoes_por_categoria(periodo_dias),
                'leads_por_produto': self.get_leads_por_produto(periodo_dias),
                'leads_por_mercado': self.get_leads_por_mercado(periodo_dias)
            }
        }
        
        return relatorio
    
    def imprimir_relatorio(self, periodo_dias: int = 30):
        """Imprime relatório formatado no console"""
        relatorio = self.gerar_relatorio_completo(periodo_dias)
        
        print(f"\n{'='*60}")
        print(f"RELATÓRIO DE KPIs DO CHATBOT - {periodo_dias} DIAS")
        print(f"Gerado em: {relatorio['data_geracao']}")
        print(f"{'='*60}")
        
        print(f"\n📊 KPIs PRINCIPAIS:")
        print(f"   • Tempo médio de resposta: {relatorio['kpis']['tempo_medio_resposta_segundos']}s")
        print(f"   • Taxa de conversão: {relatorio['kpis']['taxa_conversao_vendas_percentual']}%")
        print(f"   • Satisfação média: {relatorio['kpis']['satisfacao_media_estrelas']}/5 ⭐")
        print(f"   • Total de reclamações: {relatorio['kpis']['total_reclamacoes']}")
        
        print(f"\n📈 LEADS POR PRODUTO:")
        for produto, count in relatorio['detalhamento']['leads_por_produto'].items():
            print(f"   • {produto}: {count}")
        
        print(f"\n🎯 LEADS POR MERCADO:")
        for mercado, count in relatorio['detalhamento']['leads_por_mercado'].items():
            print(f"   • {mercado}: {count}")
        
        print(f"\n⚠️  RECLAMAÇÕES POR CATEGORIA:")
        for categoria, count in relatorio['detalhamento']['reclamacoes_por_categoria'].items():
            print(f"   • {categoria}: {count}")
        
        print(f"\n{'='*60}")

def main():
    """Função principal para executar o dashboard"""
    dashboard = ChatbotKPIDashboard()
    
    # Gerar relatório para os últimos 30 dias
    dashboard.imprimir_relatorio(30)
    
    # Gerar arquivo JSON com dados completos
    relatorio = dashboard.gerar_relatorio_completo(30)
    with open('kpis_chatbot.json', 'w', encoding='utf-8') as f:
        json.dump(relatorio, f, ensure_ascii=False, indent=2)
    
    print(f"\n💾 Relatório completo salvo em: kpis_chatbot.json")

if __name__ == "__main__":
    main()