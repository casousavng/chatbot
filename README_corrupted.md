# 🧻 Chatbot PaperCare - Assistente de Papel Higiénico# � Chatbot PaperCare - Assistente de Papel Higiénico



![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)

![Rasa](https://img.shields.io/badge/Rasa-3.6.0+-orange.svg)![Rasa](https://img.shields.io/badge/Rasa-3.6.0+-orange.svg)

![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)

![License](https://img.shields.io/badge/License-MIT-yellow.svg)![License](https://img.shields.io/badge/License-MIT-yellow.svg)



Um chatbot inteligente especializado em produtos de papel higiénico, desenvolvido com Rasa Framework e Flask. O bot fornece informações detalhadas sobre produtos, preços, sustentabilidade, pontos de venda e suporte ao cliente, tudo em português.Um chatbot inteligente especializado em produtos de papel higiénico, desenvolvido com Rasa Framework e Flask. O bot fornece informações detalhadas sobre produtos, preços, sustentabilidade, pontos de venda e suporte ao cliente, tudo em português.



## 📋 Índice## 📋 Índice



- [Funcionalidades](#-funcionalidades)- [Funcionalidades](#-funcionalidades)

- [Tecnologias Utilizadas](#-tecnologias-utilizadas)- [Tecnologias Utilizadas](#-tecnologias-utilizadas)

- [Pré-requisitos](#-pré-requisitos)- [Pré-requisitos](#-pré-requisitos)

- [Instalação](#-instalação)- [Instalação](#-instalação)

- [Configuração](#-configuração)- [Configuração](#-configuração)

- [Execução](#-execução)- [Execução](#-execução)

- [Utilização](#-utilização)- [Utilização](#-utilização)

- [Estrutura do Projeto](#-estrutura-do-projeto)

- [API Endpoints](#-api-endpoints)### ✅ Reencaminhamento Comercial Inteligente

- [Treinar o Modelo](#-treinar-o-modelo)- **Roteamento por produto/mercado**: CRM, ERP, Analytics

- [Troubleshooting](#-troubleshooting)- **Especialistas específicos** por combinação produto-mercado

- [Contribuição](#-contribuição)- **Fallback inteligente** para especialistas gerais

- [Licença](#-licença)- **Matriz de roteamento configurável**



## ✨ Funcionalidades### ✅ Validação de Regras Comerciais

- **Validação de email** (formato RFC compliant)

### 🎯 Intents Principais- **Validação de telefone** (9-15 dígitos)

- **Informações de Produtos**: Tipos de papel higiénico (1, 2, 3 folhas)- **Validação de nome completo** (mínimo 2 palavras)

- **Qualidade e Resistência**: Especificações técnicas detalhadas- **Validação de empresa** (não vazio)

- **Preços e Ofertas**: Tabela de preços competitivos- **Formulário interativo** com validação em tempo real

- **Sustentabilidade**: Certificações ambientais e processo eco-friendly

- **Pontos de Venda**: Onde comprar (online e físico)### ✅ Sistema de KPIs Completo

- **Descontos Corporativos**: Ofertas para empresas- **Tempo médio de resposta** (calculado automaticamente)

- **Suporte ao Cliente**: Horários, contactos e reclamações- **Taxa de conversão de vendas** (conversas → leads)

- **Garantias**: Política de qualidade e trocas- **Satisfação do cliente** (escala 1-5 estrelas)

- **Redução de reclamações** (categorização automática)

### 🌟 Características Técnicas- **Dashboard administrativo** com gráficos e tabelas

- ✅ **Respostas 100% em Português**: Eliminação de confusão multilíngue

- ✅ **Interface Web Responsiva**: Frontend moderno com HTML/CSS/JavaScript## 🚀 Instalação e Configuração

- ✅ **Dashboard KPI**: Métricas e analytics do chatbot

- ✅ **Armazenamento de Conversas**: SQLite database para tracking### 1. Pré-requisitos

- ✅ **API RESTful**: Integração flexível com outros sistemas```bash

- ✅ **Botões Interativos**: Navegação guiada para melhor UX# Python 3.8+

python --version

## 🛠 Tecnologias Utilizadas

# Node.js (opcional, para desenvolvimento)

### Backendnode --version

- **[Rasa Framework 3.6+](https://rasa.com/)**: Motor de conversação e NLU```

- **[Flask 2.0+](https://flask.palletsprojects.com/)**: Web framework Python

- **[SQLite](https://sqlite.org/)**: Base de dados para tracking### 2. Instalar Dependências

- **[Python 3.9+](https://python.org/)**: Linguagem de programação```bash

# Navegar para o diretório do projeto

### Frontendcd /Users/andresousa/Desktop/chatbot

- **HTML5**: Estrutura da interface

- **CSS3**: Estilização responsiva# Instalar dependências Python

- **JavaScript (Vanilla)**: Interactividadepip install -r requirements.txt



### Machine Learning# Instalar langdetect se não estiver incluído

- **DIET Classifier**: Classificação de intents e entidadespip install langdetect

- **TED Policy**: Gestão de diálogo

- **Rule Policy**: Regras de conversação# Instalar Rasa se não estiver instalado

- **Memoization Policy**: Optimização de respostaspip install rasa[full]

```

## 📋 Pré-requisitos

### 3. Treinar o Modelo

Antes de começar, certifique-se que tem instalado:```bash

# Treinar o modelo Rasa com as novas funcionalidades

### Essenciaisrasa train

- **Python 3.9 ou superior** - [Download aqui](https://python.org/downloads/)

- **pip** (normalmente incluído com Python)# Verificar se o modelo foi criado

- **Git** - [Download aqui](https://git-scm.com/)ls models/

```

### Recomendado

- **pyenv** (para gestão de versões Python) - [Guia de instalação](https://github.com/pyenv/pyenv)### 4. Configurar Base de Dados

- **Visual Studio Code** - [Download aqui](https://code.visualstudio.com/)```bash

# O sistema criará automaticamente o banco SQLite

### Verificar Instalações# As tabelas serão criadas na primeira execução

```bashpython kpi_dashboard.py

# Verificar Python```

python --version  # Deve mostrar 3.9+

## 🔧 Execução do Sistema

# Verificar pip

pip --version### 1. Iniciar Servidor de Actions (Terminal 1)

```bash

# Verificar Gitcd /Users/andresousa/Desktop/chatbot

git --versionrasa run actions --port 5055

``````



## 🚀 Instalação### 2. Iniciar Servidor Rasa (Terminal 2)

```bash

### 1. Clonar o Repositóriocd /Users/andresousa/Desktop/chatbot

```bashrasa run --enable-api --cors "*" --port 5005

# Clonar o projeto```

git clone https://github.com/seu-usuario/chatbot-papercare.git

### 3. Iniciar Interface Web (Terminal 3)

# Navegar para o diretório```bash

cd chatbot-papercarecd /Users/andresousa/Desktop/chatbot

```python app.py

```

### 2. Criar Ambiente Virtual

```bash### 4. Acessar o Sistema

# Criar ambiente virtual- **Interface do Chatbot**: http://localhost:5000

python -m venv venv- **Dashboard Administrativo**: http://localhost:5000/admin

- **API de KPIs**: http://localhost:5000/kpis

# Ativar o ambiente virtual- **Health Check**: http://localhost:5000/health

# No macOS/Linux:

source venv/bin/activate## 📊 Monitoramento de KPIs



# No Windows:### Dashboard Administrativo

venv\Scripts\activateO dashboard fornece:

- **Métricas em tempo real**: Tempo de resposta, conversão, satisfação

# Verificar se está ativo (deve aparecer (venv) no prompt)- **Gráficos interativos**: Leads por produto e mercado

```- **Tabelas dinâmicas**: Últimos leads e reclamações

- **Auto-refresh**: Atualização automática a cada 5 minutos

### 3. Instalar Dependências

```bash### Relatórios por Linha de Comando

# Atualizar pip```bash

pip install --upgrade pip# Gerar relatório completo dos últimos 30 dias

python kpi_dashboard.py

# Instalar dependências do projeto

pip install -r requirements.txt# O arquivo kpis_chatbot.json será gerado com dados completos

```

# Verificar instalação do Rasa

rasa --version### APIs Disponíveis

``````bash

# Obter KPIs em JSON

### 4. Instalar Dependências Adicionais (se necessário)curl http://localhost:5000/kpis

```bash

# Para sistemas que precisem de dependências extras# Obter lista de leads

pip install wheel setuptoolscurl http://localhost:5000/leads



# Para problemas com TensorFlow no macOS M1/M2# Obter reclamações

pip install tensorflow-macos tensorflow-metalcurl http://localhost:5000/reclamacoes

```

# Verificar status dos serviços

## ⚙️ Configuraçãocurl http://localhost:5000/health

```

### 1. Estrutura de Arquivos

Certifique-se que tem esta estrutura:## 🌐 Matriz de Roteamento Comercial

```

chatbot-papercare/### Especialistas por Produto/Mercado

├── 📁 actions/           # Ações customizadas do Rasa| Produto | Mercado | Especialista |

├── 📁 data/             # Dados de treino (NLU, stories, rules)|---------|---------|--------------|

├── 📁 models/           # Modelos treinados| CRM | Tecnologia | especialista_crm_tech@empresa.com |

├── 📁 templates/        # Templates HTML| CRM | Retail | especialista_crm_retail@empresa.com |

├── 📁 tests/           # Testes do chatbot| ERP | Manufacturing | especialista_erp_manufacturing@empresa.com |

├── 📄 app.py           # Servidor Flask| ERP | Finance | especialista_erp_finance@empresa.com |

├── 📄 config.yml       # Configuração do Rasa| Analytics | Finance | especialista_analytics_finance@empresa.com |

├── 📄 domain.yml       # Domínio do chatbot| Analytics | Healthcare | especialista_analytics_health@empresa.com |

├── 📄 endpoints.yml    # Configuração de endpoints

├── 📄 credentials.yml  # Credenciais (não committar!)### Fallbacks por Produto

└── 📄 requirements.txt # Dependências Python- **CRM**: vendas_crm@empresa.com

```- **ERP**: vendas_erp@empresa.com

- **Analytics**: vendas_analytics@empresa.com

### 2. Configurar Credenciais (Opcional)- **Geral**: vendas_geral@empresa.com

```bash

# Copiar template de credenciais## 🎭 Exemplos de Conversas

cp credentials.yml.example credentials.yml

### Conversa em Português

# Editar com suas configurações (se aplicável)```

nano credentials.ymlUsuário: "Olá, quero informações sobre CRM"

```Bot: "Olá! 👋 Sou o assistente virtual. Como posso ajudar-te hoje?"

...

### 3. Variáveis de Ambiente (Opcional)Bot: "Para melhor atendê-lo, preciso de algumas informações. Pode fornecer-me o seu nome e email?"

```bash```

# Criar arquivo .env (opcional)

echo "RASA_PORT=5005" > .env### Conversa em Espanhol

echo "FLASK_PORT=5020" > .env```

```Usuario: "Hola, necesito información sobre ERP"

Bot: "¡Hola! 👋 Soy el asistente virtual. ¿Cómo puedo ayudarte hoy?"

## 🏃‍♂️ Execução...

Bot: "Para atenderle mejor, necesito algunos datos. ¿Puede proporcionarme su nombre y correo electrónico?"

### Método 1: Execução Completa (Recomendado)```



```bash### Conversa em Inglês

# 1. Ativar ambiente virtual```

source venv/bin/activateUser: "Hello, I need information about Analytics"

Bot: "Hello! 👋 I'm the virtual assistant. How can I help you today?"

# 2. Treinar o modelo (primeira vez ou após mudanças)...

rasa trainBot: "To better assist you, I need some information. Can you provide me with your name and email?"

```

# 3. Iniciar servidor Rasa (em uma terminal)

rasa run --enable-api --cors "*" --port 5005## 🔍 Validações Implementadas



# 4. Iniciar servidor Flask (em outra terminal)### Validação de Email

python app.py- Formato RFC compliant

```- Domínio válido obrigatório

- Rejeição de emails temporários

### Método 2: Execução em Background

### Validação de Telefone

```bash- 9-15 dígitos aceitos

# Ativar ambiente virtual- Remove espaços e hífens automaticamente

source venv/bin/activate- Suporte a códigos de país



# Iniciar Rasa em background### Validação de Nome

nohup rasa run --enable-api --cors "*" --port 5005 > rasa_server.log 2>&1 &- Mínimo 2 palavras

- Caracteres alfabéticos

# Iniciar Flask em background- Suporte a acentos e caracteres especiais

nohup python app.py > flask_server.log 2>&1 &

## 📈 Métricas de Sucesso

# Verificar processos

ps aux | grep -E "(rasa|python.*app.py)"### KPIs Alvo (configuráveis)

```- **Tempo médio de resposta**: < 30 segundos

- **Taxa de conversão**: > 15%

### 3. Verificar se Está Funcionando- **Satisfação média**: > 4.0/5.0

- **Reclamações**: < 5% das conversas

```bash

# Testar servidor Rasa### Categorias de Reclamação

curl -X POST http://localhost:5005/webhooks/rest/webhook \- **Produto**: Funcionalidades, bugs, erros

  -H "Content-Type: application/json" \- **Atendimento**: Suporte, vendas, serviço

  -d '{"sender": "test", "message": "olá"}'- **Cobrança**: Preços, faturação, pagamento

- **Entrega**: Prazos, delivery

# Testar servidor Flask- **Geral**: Outras categorias

curl http://localhost:5020/health

```## 🛠️ Personalização



## 📱 Utilização### Adicionar Novos Idiomas

1. Atualizar `actions/actions.py` - ActionDetectarIdioma

### Interface Web2. Adicionar templates em `domain.yml`

1. Abra o navegador em: `http://localhost:5020`3. Incluir exemplos NLU em `data/nlu.yml`

2. Digite suas perguntas na caixa de chat4. Retreinar o modelo

3. Use os botões sugeridos para navegação rápida

### Configurar Novos Produtos/Mercados

### Exemplos de Perguntas1. Editar matriz de roteamento em `actions/actions.py`

```2. Adicionar novos valores em `domain.yml` (lookup tables)

💬 "Olá"3. Atualizar exemplos NLU

💬 "Que tipos de papel têm?"4. Retreinar o modelo

💬 "Qual é o preço?"

💬 "É ecológico?"### Personalizar Interface

💬 "Onde posso comprar?"1. Editar `templates/index.html` para design

💬 "Horário de atendimento?"2. Modificar `templates/admin.html` para dashboard

💬 "Como fazer uma reclamação?"3. Ajustar CSS conforme branding

💬 "Informações técnicas"

```## 🔐 Segurança e Privacidade



### Dashboard KPI### Dados Armazenados

- Acesse: `http://localhost:5020/dashboard`- **Leads**: Nome, email, telefone, empresa (criptografar em produção)

- Visualize métricas de conversação- **Métricas**: Tempos de resposta, IDs de sessão

- Analise intents mais usados- **Satisfação**: Avaliações numéricas

- **Reclamações**: Texto da reclamação (anonimizar se necessário)

## 📁 Estrutura do Projeto

### Recomendações de Produção

```1. **Criptografar dados sensíveis** no banco

📦 chatbot-papercare/2. **Usar HTTPS** para todas as comunicações

│3. **Implementar rate limiting** para APIs

├── 📁 actions/4. **Logs de auditoria** para acesso aos dados

│   ├── __init__.py5. **Backup regular** da base de dados

│   └── actions.py              # Ações customizadas

│## 🚨 Troubleshooting

├── 📁 data/

│   ├── nlu.yml                 # Dados de treino NLU### Problema: Rasa não inicia

│   ├── stories.yml             # Histórias de conversação```bash

│   └── rules.yml               # Regras de conversação# Verificar versão do Rasa

│rasa --version

├── 📁 models/

│   └── [modelo-treinado].tar.gz # Modelos Rasa treinados# Reinstalar se necessário

│pip uninstall rasa

├── 📁 templates/pip install rasa[full]

│   ├── index.html              # Interface principal```

│   └── admin.html              # Dashboard admin

│### Problema: Actions não funcionam

├── 📁 tests/```bash

│   └── test_stories.yml        # Testes de conversação# Verificar se o servidor de actions está ativo

│curl http://localhost:5055/health

├── 📄 app.py                   # Servidor Flask principal

├── 📄 kpi_dashboard.py         # Dashboard de métricas# Verificar logs

├── 📄 config.yml               # Configuração do pipeline Rasarasa run actions --debug

├── 📄 domain.yml               # Domínio: intents, entities, responses```

├── 📄 endpoints.yml            # Configuração de endpoints

├── 📄 credentials.yml          # Credenciais (não versionar!)### Problema: Interface não carrega KPIs

├── 📄 requirements.txt         # Dependências Python```bash

├── 📄 chatbot_kpis.db         # Base de dados SQLite# Verificar se o banco foi criado

├── 📄 rasa_tracker.db         # Tracking do Rasals -la chatbot_kpis.db

└── 📄 README.md               # Este arquivo

```# Testar endpoint diretamente

curl http://localhost:5000/kpis

## 🔌 API Endpoints```



### Flask Server (Port 5020)### Problema: Detecção de idioma falha

```http```bash

GET  /                    # Interface web principal# Reinstalar langdetect

GET  /health              # Health checkpip uninstall langdetect

GET  /dashboard           # Dashboard KPIpip install langdetect==1.0.9

POST /webhook             # Receber mensagens do frontend```

```

## 📚 Estrutura do Projeto

### Rasa Server (Port 5005)

```http```

POST /webhooks/rest/webhook    # Enviar mensagens ao botchatbot/

GET  /model                    # Informações do modelo├── actions/

GET  /status                   # Status do servidor│   ├── __init__.py

POST /model/train              # Treinar novo modelo│   └── actions.py                 # Actions customizadas

```├── data/

│   ├── nlu.yml                   # Dados de treino NLU

### Exemplo de Integração│   ├── rules.yml                 # Regras de conversa

```javascript│   └── stories.yml               # Histórias de treino

// Frontend JavaScript├── models/                       # Modelos treinados

async function sendMessage(message) {├── templates/

    const response = await fetch('/webhook', {│   ├── index.html               # Interface principal

        method: 'POST',│   └── admin.html               # Dashboard administrativo

        headers: {├── app.py                       # Servidor Flask

            'Content-Type': 'application/json',├── config.yml                   # Configuração Rasa

        },├── domain.yml                   # Domínio do chatbot

        body: JSON.stringify({├── endpoints.yml                # Configuração de endpoints

            message: message,├── kpi_dashboard.py             # Sistema de KPIs

            sender: 'user'├── requirements.txt             # Dependências Python

        })└── README.md                    # Este arquivo

    });```

    return await response.json();

}## 🎉 Próximos Passos

```

### Melhorias Futuras

## 🎓 Treinar o Modelo1. **Integração com CRM** para sync automático de leads

2. **WhatsApp/Telegram** integrations

### Quando Treinar3. **Machine Learning** para otimização de roteamento

- ✅ Primeira execução4. **Análise de sentimento** avançada

- ✅ Após modificar `data/nlu.yml`5. **Chatbot por voz** com speech-to-text

- ✅ Após modificar `data/stories.yml` 6. **Multi-tenancy** para múltiplas empresas

- ✅ Após modificar `domain.yml`

- ✅ Após adicionar novas intents### Otimizações de Performance

1. **Redis** para cache de sessões

### Comandos de Treino2. **PostgreSQL** para produção

```bash3. **Load balancing** para múltiplas instâncias

# Treino básico4. **CDN** para assets estáticos

rasa train

---

# Treino com debug (mais informações)

rasa train --debug## 🆘 Suporte



# Treino forçado (ignora cache)Para dúvidas ou problemas:

rasa train --force1. Consultar logs do sistema

2. Verificar health checks

# Treino apenas NLU3. Testar endpoints individualmente

rasa train nlu4. Consultar documentação oficial do Rasa



# Treino apenas Core**Sistema desenvolvido com foco nos requisitos específicos do cliente:**

rasa train core- ✅ Detecção e validação de idioma

```- ✅ Reencaminhamento comercial inteligente  

- ✅ KPIs de performance e satisfação

### Validação- ✅ Validação de regras comerciais

```bash

# Validar dados antes do treino🚀 **Sistema pronto para produção!**
rasa data validate

# Testar modelo com dados de teste
rasa test

# Conversa interativa para teste
rasa shell
```

## 🐛 Troubleshooting

### Problemas Comuns

#### 1. Erro "rasa: command not found"
```bash
# Verificar se o ambiente virtual está ativo
source venv/bin/activate

# Reinstalar Rasa
pip install --upgrade rasa
```

#### 2. Porta 5005 já em uso
```bash
# Encontrar processo usando a porta
lsof -i :5005

# Matar processo
kill -9 [PID]

# Ou usar porta diferente
rasa run --port 5006
```

#### 3. Problemas de Dependências
```bash
# Limpar e reinstalar
pip uninstall rasa rasa-sdk
pip install --no-cache-dir rasa rasa-sdk

# Para macOS M1/M2
pip install --upgrade pip setuptools wheel
```

#### 4. Modelo não carrega
```bash
# Verificar modelos disponíveis
ls models/

# Treinar novamente
rasa train --force

# Especificar modelo manualmente
rasa run --model models/[seu-modelo].tar.gz
```

#### 5. Flask não conecta ao Rasa
```bash
# Verificar se Rasa está rodando
curl http://localhost:5005

# Verificar logs
tail -f rasa_server.log

# Verificar configuração de proxy no app.py
```

### Logs e Debug

#### Ver Logs em Tempo Real
```bash
# Logs do Rasa
tail -f rasa_server.log

# Logs do Flask
tail -f flask_server.log

# Logs detalhados do Rasa
rasa run --debug --cors "*" --port 5005
```

#### Testar Componentes Individualmente
```bash
# Testar apenas NLU
rasa shell nlu

# Testar conversa completa
rasa shell

# Testar com dados específicos
rasa test --stories tests/test_stories.yml
```

## 📊 Monitorização

### Métricas Disponíveis
- **Total de Conversas**: Número de sessões únicas
- **Mensagens por Dia**: Volume de interações
- **Intents Mais Populares**: Top intents utilizados
- **Taxa de Confiança**: Precisão das classificações
- **Tempo de Resposta**: Performance do sistema

### Base de Dados
```sql
-- Consultar conversas recentes
SELECT * FROM conversations ORDER BY timestamp DESC LIMIT 10;

-- Top intents
SELECT intent, COUNT(*) as count 
FROM messages 
GROUP BY intent 
ORDER BY count DESC;
```

## 🔧 Desenvolvimento

### Adicionar Novas Intents

1. **Editar `data/nlu.yml`**:
```yaml
- intent: nova_intent
  examples: |
    - exemplo de pergunta 1
    - exemplo de pergunta 2
```

2. **Editar `domain.yml`**:
```yaml
intents:
  - nova_intent

responses:
  utter_nova_resposta:
    - text: "Sua nova resposta aqui"
```

3. **Treinar novamente**:
```bash
rasa train
```

### Adicionar Ações Customizadas

1. **Editar `actions/actions.py`**:
```python
class ActionNovaAcao(Action):
    def name(self) -> Text:
        return "action_nova_acao"
    
    def run(self, dispatcher, tracker, domain):
        # Sua lógica aqui
        dispatcher.utter_message(text="Resultado da ação")
        return []
```

2. **Registrar no `domain.yml`**:
```yaml
actions:
  - action_nova_acao
```

3. **Iniciar servidor de ações**:
```bash
rasa run actions
```

## 🤝 Contribuição

### Como Contribuir

1. **Fork o repositório**
2. **Criar branch para feature**:
   ```bash
   git checkout -b feature/nova-funcionalidade
   ```
3. **Fazer commits descritivos**:
   ```bash
   git commit -m "feat: adicionar nova intent para devoluções"
   ```
4. **Push para o branch**:
   ```bash
   git push origin feature/nova-funcionalidade
   ```
5. **Criar Pull Request**

### Padrões de Código

- **Python**: Seguir PEP 8
- **Commits**: Usar [Conventional Commits](https://conventionalcommits.org/)
- **Documentação**: Atualizar README.md quando necessário
- **Testes**: Adicionar testes para novas funcionalidades

### Estrutura de Commits
```
feat: nova funcionalidade
fix: correção de bug
docs: alteração de documentação
style: formatação de código
refactor: refatoração
test: adição de testes
chore: tarefas de manutenção
```

## 🌐 Preparar para GitHub

### 1. Inicializar Repositório Git
```bash
# Inicializar Git (se ainda não foi feito)
git init

# Adicionar todos os arquivos
git add .

# Fazer commit inicial
git commit -m "feat: initial commit - chatbot papercare completo"
```

### 2. Criar .gitignore
```bash
# Criar arquivo .gitignore
cat > .gitignore << EOL
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
.venv/
pip-log.txt
pip-delete-this-directory.txt

# Rasa
models/*.tar.gz
.rasa/

# Database
*.db
*.sqlite3

# Logs
*.log
nohup.out

# OS
.DS_Store
Thumbs.db

# IDE
.vscode/
.idea/
*.swp
*.swo

# Credentials (IMPORTANTE!)
credentials.yml
.env

# Temporary files
*.tmp
*.temp
EOL
```

### 3. Configurar Repositório Remoto
```bash
# Adicionar origem remota (substituir pela sua URL)
git remote add origin https://github.com/seu-usuario/chatbot-papercare.git

# Verificar configuração
git remote -v

# Push inicial
git branch -M main
git push -u origin main
```

### 4. Criar Releases
```bash
# Criar tag para versão
git tag -a v1.0.0 -m "Versão 1.0.0 - Chatbot PaperCare completo"

# Push da tag
git push origin v1.0.0
```

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👥 Equipe

- **Desenvolvedor Principal**: André Sousa
- **Especialista em NLP**: [Nome do Colega]
- **Designer UX/UI**: [Nome do Designer]

## 📞 Suporte

### Contactos
- **Email**: suporte@papercare.pt
- **GitHub Issues**: [Link para issues]
- **Documentação**: [Link para docs]

### FAQ Técnica

**P: O modelo demora muito a treinar?**
R: O treino inicial pode demorar 2-5 minutos. Treinos subsequentes são mais rápidos devido ao cache.

**P: Posso usar em produção?**
R: Sim, mas recomenda-se configurar HTTPS, autenticação e monitorização adequada.

**P: Como fazer backup dos dados?**
R: Copie os arquivos `*.db` e a pasta `models/` regularmente.

---

## 🚀 Quick Start para Novos Developers

```bash
# Clone e configure em 3 passos
git clone https://github.com/seu-usuario/chatbot-papercare.git
cd chatbot-papercare
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# Treine e execute
rasa train
rasa run --enable-api --cors "*" --port 5005 &
python app.py

# Teste no navegador
open http://localhost:5020
```

---

**💡 Dica**: Para desenvolvimento rápido, use `rasa interactive` para treinar o modelo interativamente!

**🌟 Made with ❤️ by André Sousa - © 2024 PaperCare Chatbot**