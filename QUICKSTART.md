# 🚀 Início Rápido - Chatbot PaperCare

## Para Desenvolvedores Experientes (2 minutos)

```bash
git clone https://github.com/seu-usuario/chatbot-papercare.git
cd chatbot-papercare
chmod +x setup.sh
./setup.sh
./start_servers.sh
```

**Pronto!** Acesse: http://localhost:5020

## Para Novatos (5 minutos)

### 1. Pré-requisitos
- Python 3.9+ instalado
- Git instalado (opcional)

### 2. Clonar e Configurar
```bash
# Baixar projeto
git clone https://github.com/seu-usuario/chatbot-papercare.git
cd chatbot-papercare

# Executar setup automático
./setup.sh
```

### 3. Iniciar Chatbot
```bash
# Método 1: Script automático (recomendado)
./start_servers.sh

# Método 2: Manual
source venv/bin/activate
rasa run --enable-api --cors "*" --port 5005 &
python app.py
```

### 4. Testar
- Abra: http://localhost:5020
- Digite: "olá"
- Experimente os botões

## Comandos Úteis

```bash
# Parar servidores
./stop_servers.sh

# Retreinar após mudanças
./retrain_model.sh

# Debug
rasa shell
tail -f rasa_server.log
```

## Estrutura Básica

```
📦 chatbot-papercare/
├── 🗂️ data/               # Dados de treino
├── 🧠 models/             # Modelos treinados
├── 🎨 templates/          # Interface web
├── ⚙️ config.yml          # Configuração ML
├── 🎯 domain.yml          # Intents e respostas
├── 🐍 app.py             # Servidor Flask
└── 📖 README.md          # Documentação completa
```

## Problemas Comuns

**"rasa: command not found"**
```bash
source venv/bin/activate
```

**"Port already in use"**
```bash
./stop_servers.sh
./start_servers.sh
```

**Modelo não funciona**
```bash
rasa train --force
```

## Desenvolvimento

1. **Adicionar nova pergunta**: Editar `data/nlu.yml`
2. **Mudar resposta**: Editar `domain.yml`
3. **Sempre retreinar**: `./retrain_model.sh`

## Ajuda

- 📖 **Documentação completa**: README.md
- 👥 **Guia para desenvolvedores**: CONTRIBUTING.md
- 🐛 **Problemas**: GitHub Issues

---

**🎉 Bem-vindo ao Chatbot PaperCare!**