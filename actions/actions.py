# Custom actions for intelligent chatbot with multi-language support

import requests
import re
import json
import datetime
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, FollowupAction
from rasa_sdk.types import DomainDict
import sqlite3
from langdetect import detect, DetectorFactory

# Configurar para ter resultados consistentes
DetectorFactory.seed = 0

class ActionDetectarIdioma(Action):
    """Detecta automaticamente o idioma da mensagem do usuário"""
    
    def name(self) -> Text:
        return "action_detectar_idioma"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        user_message = tracker.latest_message.get("text", "")
        
        try:
            # Detectar idioma
            detected_lang = detect(user_message)
            
            # Mapear para idiomas suportados
            language_mapping = {
                'pt': 'pt',
                'es': 'es', 
                'en': 'en',
                'ca': 'es',  # Catalão -> Espanhol
                'gl': 'pt',  # Galego -> Português
            }
            
            final_lang = language_mapping.get(detected_lang, 'pt')  # Default português
            
            # Registrar timestamp de início da conversa se não existir
            tempo_inicio = tracker.get_slot("tempo_inicio_conversa")
            if not tempo_inicio:
                tempo_inicio = datetime.datetime.now().isoformat()
            
            return [
                SlotSet("idioma_detectado", final_lang),
                SlotSet("tempo_inicio_conversa", tempo_inicio)
            ]
            
        except Exception as e:
            # Se falhar detecção, usar português como padrão
            return [
                SlotSet("idioma_detectado", "pt"),
                SlotSet("tempo_inicio_conversa", datetime.datetime.now().isoformat())
            ]

class ActionValidarInformacoesComerciais(Action):
    """Valida as informações comerciais básicas antes do encaminhamento"""
    
    def name(self) -> Text:
        return "action_validar_informacoes_comerciais"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        nome = tracker.get_slot("nome_cliente")
        email = tracker.get_slot("email_cliente")
        telefone = tracker.get_slot("telefone_cliente")
        empresa = tracker.get_slot("empresa_cliente")
        
        # Validações básicas
        is_valid = True
        
        # Validar email
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not email or not re.match(email_pattern, email):
            is_valid = False
        
        # Validar telefone (9-15 dígitos)
        if not telefone or not re.match(r'^\d{9,15}$', telefone.replace(' ', '').replace('-', '')):
            is_valid = False
        
        # Validar nome (mínimo 2 palavras)
        if not nome or len(nome.split()) < 2:
            is_valid = False
        
        # Validar empresa (não vazio)
        if not empresa or len(empresa.strip()) < 2:
            is_valid = False
        
        return [SlotSet("informacoes_validadas", is_valid)]

class ActionEncaminharContato(Action):
    """Encaminha o contato para o especialista adequado baseado em produto/mercado"""
    
    def name(self) -> Text:
        return "action_encaminhar_contato"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        produto = tracker.get_slot("produto_interesse")
        mercado = tracker.get_slot("mercado_alvo")
        nome = tracker.get_slot("nome_cliente")
        email = tracker.get_slot("email_cliente")
        telefone = tracker.get_slot("telefone_cliente")
        empresa = tracker.get_slot("empresa_cliente")
        
        # Lógica de roteamento inteligente
        especialista = self._determinar_especialista(produto, mercado)
        
        # Salvar lead no banco de dados
        self._salvar_lead({
            'nome': nome,
            'email': email,
            'telefone': telefone,
            'empresa': empresa,
            'produto': produto,
            'mercado': mercado,
            'especialista': especialista,
            'timestamp': datetime.datetime.now().isoformat()
        })
        
        return []

    def _determinar_especialista(self, produto: str, mercado: str) -> str:
        """Determina o especialista adequado baseado no produto e mercado"""
        
        # Matriz de roteamento
        roteamento = {
            ('CRM', 'tecnologia'): 'especialista_crm_tech@empresa.com',
            ('CRM', 'retail'): 'especialista_crm_retail@empresa.com',
            ('ERP', 'manufacturing'): 'especialista_erp_manufacturing@empresa.com',
            ('ERP', 'finance'): 'especialista_erp_finance@empresa.com',
            ('Analytics', 'finance'): 'especialista_analytics_finance@empresa.com',
            ('Analytics', 'healthcare'): 'especialista_analytics_health@empresa.com',
        }
        
        # Buscar especialista específico
        especialista = roteamento.get((produto, mercado))
        
        if not especialista:
            # Fallback por produto
            produto_fallback = {
                'CRM': 'vendas_crm@empresa.com',
                'ERP': 'vendas_erp@empresa.com', 
                'Analytics': 'vendas_analytics@empresa.com'
            }
            especialista = produto_fallback.get(produto, 'vendas_geral@empresa.com')
        
        return especialista

    def _salvar_lead(self, lead_data: dict):
        """Salva o lead no banco de dados"""
        try:
            conn = sqlite3.connect('chatbot_kpis.db')
            cursor = conn.cursor()
            
            # Criar tabela se não existir
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
            
            cursor.execute('''
                INSERT INTO leads (nome, email, telefone, empresa, produto, mercado, especialista, timestamp)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                lead_data['nome'],
                lead_data['email'], 
                lead_data['telefone'],
                lead_data['empresa'],
                lead_data['produto'],
                lead_data['mercado'],
                lead_data['especialista'],
                lead_data['timestamp']
            ))
            
            conn.commit()
            conn.close()
            
        except Exception as e:
            print(f"Erro ao salvar lead: {e}")

class ActionCalcularKpis(Action):
    """Calcula e atualiza os KPIs do sistema"""
    
    def name(self) -> Text:
        return "action_calcular_kpis"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        tempo_inicio = tracker.get_slot("tempo_inicio_conversa")
        
        if tempo_inicio:
            # Calcular tempo de resposta
            inicio = datetime.datetime.fromisoformat(tempo_inicio)
            agora = datetime.datetime.now()
            tempo_resposta = (agora - inicio).total_seconds()
            
            # Salvar métricas
            self._salvar_metricas({
                'tempo_resposta': tempo_resposta,
                'timestamp': agora.isoformat(),
                'conversa_id': tracker.sender_id
            })
        
        return []

    def _salvar_metricas(self, metricas: dict):
        """Salva métricas no banco de dados"""
        try:
            conn = sqlite3.connect('chatbot_kpis.db')
            cursor = conn.cursor()
            
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS metricas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    conversa_id TEXT,
                    tempo_resposta REAL,
                    timestamp TEXT
                )
            ''')
            
            cursor.execute('''
                INSERT INTO metricas (conversa_id, tempo_resposta, timestamp)
                VALUES (?, ?, ?)
            ''', (
                metricas['conversa_id'],
                metricas['tempo_resposta'],
                metricas['timestamp']
            ))
            
            conn.commit()
            conn.close()
            
        except Exception as e:
            print(f"Erro ao salvar métricas: {e}")

class ActionRegistrarSatisfacao(Action):
    """Registra a avaliação de satisfação do cliente"""
    
    def name(self) -> Text:
        return "action_registrar_satisfacao"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Extrair avaliação da mensagem
        user_message = tracker.latest_message.get("text", "")
        avaliacao = self._extrair_avaliacao(user_message)
        
        if avaliacao:
            self._salvar_satisfacao({
                'conversa_id': tracker.sender_id,
                'avaliacao': avaliacao,
                'timestamp': datetime.datetime.now().isoformat()
            })
            
            idioma = tracker.get_slot("idioma_detectado") or "pt"
            
            mensagens = {
                "pt": f"Obrigado pela sua avaliação de {avaliacao} estrelas! 🌟",
                "es": f"¡Gracias por su evaluación de {avaliacao} estrellas! 🌟", 
                "en": f"Thank you for your {avaliacao} star rating! 🌟"
            }
            
            dispatcher.utter_message(text=mensagens.get(idioma, mensagens["pt"]))
        
        return [SlotSet("avaliacao_satisfacao", avaliacao)]

    def _extrair_avaliacao(self, texto: str) -> float | None:
        """Extrai a avaliação numérica do texto"""
        # Procurar por números de 1-5
        numeros = re.findall(r'\b[1-5]\b', texto)
        if numeros:
            return float(numeros[0])
        
        # Procurar por palavras-chave
        if any(word in texto.lower() for word in ['excelente', 'excellent', 'excelente']):
            return 5.0
        elif any(word in texto.lower() for word in ['bom', 'good', 'bueno']):
            return 4.0
        elif any(word in texto.lower() for word in ['ok', 'regular', 'normal']):
            return 3.0
        elif any(word in texto.lower() for word in ['mau', 'bad', 'malo']):
            return 2.0
        elif any(word in texto.lower() for word in ['terrível', 'terrible', 'terrible']):
            return 1.0
        
        return None

    def _salvar_satisfacao(self, dados: dict):
        """Salva dados de satisfação no banco"""
        try:
            conn = sqlite3.connect('chatbot_kpis.db')
            cursor = conn.cursor()
            
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS satisfacao (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    conversa_id TEXT,
                    avaliacao REAL,
                    timestamp TEXT
                )
            ''')
            
            cursor.execute('''
                INSERT INTO satisfacao (conversa_id, avaliacao, timestamp)
                VALUES (?, ?, ?)
            ''', (
                dados['conversa_id'],
                dados['avaliacao'],
                dados['timestamp']
            ))
            
            conn.commit()
            conn.close()
            
        except Exception as e:
            print(f"Erro ao salvar satisfação: {e}")

class ActionProcessarReclamacao(Action):
    """Processa reclamações e as categoriza"""
    
    def name(self) -> Text:
        return "action_processar_reclamacao"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        user_message = tracker.latest_message.get("text", "")
        idioma = tracker.get_slot("idioma_detectado") or "pt"
        
        # Categorizar reclamação
        categoria = self._categorizar_reclamacao(user_message)
        
        # Salvar reclamação
        self._salvar_reclamacao({
            'conversa_id': tracker.sender_id,
            'mensagem': user_message,
            'categoria': categoria,
            'timestamp': datetime.datetime.now().isoformat()
        })
        
        # Resposta baseada no idioma
        respostas = {
            "pt": f"Lamento saber da sua experiência negativa. A sua reclamação foi registada como '{categoria}' e será encaminhada para resolução prioritária.",
            "es": f"Lamento saber de su experiencia negativa. Su queja ha sido registrada como '{categoria}' y será dirigida para resolución prioritaria.",
            "en": f"I'm sorry to hear about your negative experience. Your complaint has been registered as '{categoria}' and will be forwarded for priority resolution."
        }
        
        dispatcher.utter_message(text=respostas.get(idioma, respostas["pt"]))
        
        return []

    def _categorizar_reclamacao(self, texto: str) -> str:
        """Categoriza a reclamação baseada em palavras-chave"""
        texto_lower = texto.lower()
        
        categorias = {
            'produto': ['produto', 'funcionalidade', 'bug', 'erro', 'product', 'feature', 'producto'],
            'atendimento': ['atendimento', 'suporte', 'vendas', 'service', 'support', 'sales', 'servicio'],
            'cobranca': ['preço', 'faturação', 'pagamento', 'price', 'billing', 'payment', 'precio', 'facturacion'],
            'entrega': ['entrega', 'prazo', 'delivery', 'deadline', 'entrega'],
            'geral': []
        }
        
        for categoria, palavras in categorias.items():
            if any(palavra in texto_lower for palavra in palavras):
                return categoria
        
        return 'geral'

    def _salvar_reclamacao(self, dados: dict):
        """Salva reclamação no banco"""
        try:
            conn = sqlite3.connect('chatbot_kpis.db')
            cursor = conn.cursor()
            
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
            
            cursor.execute('''
                INSERT INTO reclamacoes (conversa_id, mensagem, categoria, timestamp)
                VALUES (?, ?, ?, ?)
            ''', (
                dados['conversa_id'],
                dados['mensagem'],
                dados['categoria'],
                dados['timestamp']
            ))
            
            conn.commit()
            conn.close()
            
        except Exception as e:
            print(f"Erro ao salvar reclamação: {e}")

class ValidateInformacoesClienteForm(FormValidationAction):
    """Valida formulário de informações do cliente"""
    
    def name(self) -> Text:
        return "validate_informacoes_cliente_form"

    def validate_nome_cliente(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        
        if slot_value and len(slot_value.split()) >= 2:
            return {"nome_cliente": slot_value}
        else:
            idioma = tracker.get_slot("idioma_detectado") or "pt"
            mensagens = {
                "pt": "Por favor, forneça o seu nome completo.",
                "es": "Por favor, proporcione su nombre completo.",
                "en": "Please provide your full name."
            }
            dispatcher.utter_message(text=mensagens.get(idioma, mensagens["pt"]))
            return {"nome_cliente": None}

    def validate_email_cliente(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        if slot_value and re.match(email_pattern, slot_value):
            return {"email_cliente": slot_value}
        else:
            idioma = tracker.get_slot("idioma_detectado") or "pt"
            mensagens = {
                "pt": "Por favor, forneça um email válido.",
                "es": "Por favor, proporcione un correo electrónico válido.",
                "en": "Please provide a valid email address."
            }
            dispatcher.utter_message(text=mensagens.get(idioma, mensagens["pt"]))
            return {"email_cliente": None}

    def validate_telefone_cliente(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        
        if slot_value and re.match(r'^\d{9,15}$', slot_value.replace(' ', '').replace('-', '')):
            return {"telefone_cliente": slot_value}
        else:
            idioma = tracker.get_slot("idioma_detectado") or "pt"
            mensagens = {
                "pt": "Por favor, forneça um número de telefone válido (9-15 dígitos).",
                "es": "Por favor, proporcione un número de teléfono válido (9-15 dígitos).",
                "en": "Please provide a valid phone number (9-15 digits)."
            }
            dispatcher.utter_message(text=mensagens.get(idioma, mensagens["pt"]))
            return {"telefone_cliente": None}

# Manter action original do Ollama
class ActionAskOllama(Action):
    def name(self):
        return "action_ask_ollama"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict):

        user_message = tracker.latest_message.get("text")
        idioma = tracker.get_slot("idioma_detectado") or "pt"

        # Adaptar prompt baseado no idioma
        prompts = {
            "pt": f"Responda em português: {user_message}",
            "es": f"Responde en español: {user_message}",
            "en": f"Respond in English: {user_message}"
        }

        prompt = prompts.get(idioma, prompts["pt"])

        # Chamar API local do Ollama
        try:
            response = requests.post(
                "http://localhost:11434/api/generate",
                json={"model": "mistral", "prompt": prompt, "stream": False}
            )

            if response.status_code == 200:
                answer = response.json().get("response", "Não consegui responder.")
            else:
                fallbacks = {
                    "pt": "Erro ao contactar o modelo local.",
                    "es": "Error al contactar el modelo local.",
                    "en": "Error contacting the local model."
                }
                answer = fallbacks.get(idioma, fallbacks["pt"])
        except:
            fallbacks = {
                "pt": "Serviço temporariamente indisponível.",
                "es": "Servicio temporalmente no disponible.",
                "en": "Service temporarily unavailable."
            }
            answer = fallbacks.get(idioma, fallbacks["pt"])

        dispatcher.utter_message(text=answer)
        return []