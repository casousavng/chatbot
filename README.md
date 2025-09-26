# 🧻 Chatbot PaperCare - Assistente de Papel Higiénico

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Rasa](https://img.shields.io/badge/Rasa-3.6.0+-orange.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

Um chatbot inteligente especializado em produtos de papel higiénico, desenvolvido com Rasa Framework e Flask. Fornece informações sobre produtos, preços, sustentabilidade e suporte ao cliente em português.

## 📋 Índice

- [Início Rápido](#-início-rápido)
- [Funcionalidades](#-funcionalidades)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Pré-requisitos](#-pré-requisitos)
- [Instalação](#-instalação)
- [Execução](#-execução)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [API Endpoints](#-api-endpoints)
- [Contribuição](#-contribuição)
- [Licença](#-licença)
- [Suporte](#-suporte)

## 🚀 Início Rápido

> **Nota:** Antes de tudo, é necessário instalar o Ollama e baixar o modelo Llama3 para rodar o chatbot corretamente.

### 1. Instalar Ollama

#### macOS
```bash
brew install ollama
```
Ou baixe diretamente em: [ollama.com/download](https://ollama.com/download)

#### Windows
Baixe o instalador em: [ollama.com/download](https://ollama.com/download)

### 2. Baixar o modelo Llama3

Após instalar o Ollama, execute:
```bash
ollama pull llama3
```

### 3. Clonar o projeto e instalar dependências

```bash
git clone https://github.com/casousavng/chatbot.git
cd chatbot

python -m venv venv
source venv/bin/activate  # Linux/macOS
# ou venv\Scripts\activate  # Windows

pip install -r requirements.txt
rasa train
```

### 4. Executar os servidores

**Terminal 1 - Ollama (LLM local):**
```bash
ollama run llama3
```

**Terminal 2 - Servidor Rasa:**
```bash
source venv/bin/activate
rasa run --enable-api --cors "*" --port 5005
```

**Terminal 3 - Servidor Flask:**
```bash
source venv/bin/activate
python app.py
```

### 5. Aceder ao chatbot

Abra o navegador em: [http://localhost:5020](http://localhost:5020)

## ✨ Funcionalidades

- 🧻 **Informações de Produtos**: Tipos de papel higiénico (1, 2, 3 folhas)
- 💰 **Preços**: Tabela de preços competitivos e ofertas
- 🌱 **Sustentabilidade**: Certificações ambientais e processo eco-friendly
- 🛒 **Pontos de Venda**: Onde comprar (online e lojas físicas)
- 🏢 **Descontos Corporativos**: Ofertas especiais para empresas
- 🕐 **Suporte ao Cliente**: Horários de atendimento e contactos
- ✅ **Garantias**: Política de qualidade e trocas
- 📊 **Dashboard KPI**: Métricas e analytics do chatbot
- 🔄 **Roteamento Comercial Inteligente**: CRM, ERP, Analytics, especialistas por produto/mercado

## 🛠 Tecnologias Utilizadas

- **[Rasa 3.6+](https://rasa.com/)** - Framework de conversação e NLU
- **[Flask 2.0+](https://flask.palletsprojects.com/)** - Servidor web Python
- **[SQLite](https://sqlite.org/)** - Base de dados para conversas
- **Python 3.9+** - Linguagem de programação
- **HTML/CSS/JS** - Interface web

## 📋 Pré-requisitos

- **Ollama** instalado e modelo Llama3 baixado
- **Python 3.9+** instalado
- **pip** (package manager)
- **Git** (opcional mas recomendado)

Verificar instalações:
```bash
python --version  # Deve mostrar 3.9+
pip --version
ollama --version
```

## 📦 Instalação

Siga os passos da seção [Início Rápido](#-início-rápido) para garantir que o Ollama está instalado e o modelo Llama3 baixado antes de instalar as dependências do projeto.

## 🏃‍♂️ Execução

Veja os comandos na seção [Início Rápido](#-início-rápido) para rodar todos os servidores necessários.

## 🎯 Como Usar

1. Abrir navegador: http://localhost:5020
2. Digitar mensagens na caixa de chat
3. Usar botões para navegação rápida

### Exemplos de Perguntas

- "Olá"
- "Que tipos de papel têm?"
- "Qual é o preço?"
- "É ecológico?"
- "Onde posso comprar?"
- "Horário de atendimento?"

## 📁 Estrutura do Projeto

```
chatbot/
├── actions/           # Ações customizadas do Rasa
├── data/              # Dados de treino (NLU, stories, rules)
├── models/            # Modelos treinados
├── templates/         # Interface web (HTML)
├── app.py             # Servidor Flask
├── config.yml         # Configuração do Rasa
├── domain.yml         # Intents, entities e respostas
├── requirements.txt   # Dependências Python
└── README.md          # Este arquivo
```

## 🔌 API Endpoints

### Flask Server (Port 5020)
- `GET /` - Interface web principal
- `GET /health` - Health check
- `GET /dashboard` - Dashboard KPI
- `POST /webhook` - Receber mensagens do frontend

### Rasa Server (Port 5005)
- `POST /webhooks/rest/webhook` - Enviar mensagens ao bot
- `GET /model` - Informações do modelo
- `GET /status` - Status do servidor

## 🤝 Contribuição

1. Fork do repositório
2. Criar branch: `git checkout -b minha-feature`
3. Commit: `git commit -m "Nova funcionalidade"`
4. Push: `git push origin minha-feature`
5. Criar Pull Request

**Padrões de Código**
- Python: PEP 8
- Commits: Conventional Commits
- Documentação: Atualizar README.md
- Testes: Adicionar testes para novas funcionalidades

## 📄 Licença

Este projeto está sob a licença MIT. Veja [LICENSE](LICENSE) para mais detalhes.

## 📞 Suporte

- **GitHub**: [Issues](https://github.com/casousavng/chatbot/issues)

---

**Desenvolvido com ❤️ usando Rasa, Flask e Ollama**
