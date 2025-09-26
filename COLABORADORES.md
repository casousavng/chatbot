# 📋 Instruções para Colaboradores

## 🎯 Para Começar (5 minutos)

### 1. Requisitos
- Python 3.9+ instalado
- Git instalado
- Terminal/Command Prompt

### 2. Setup do Projeto
```bash
# Clonar repositório
git clone https://github.com/casousavng/chatbot.git
cd chatbot

# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
source venv/bin/activate  # macOS/Linux
# ou
venv\Scripts\activate     # Windows

# Instalar dependências
pip install -r requirements.txt

# Treinar modelo
rasa train
```

### 3. Testar Instalação
```bash
# Verificar Rasa
rasa --version

# Teste rápido
rasa shell nlu
# Digite: "olá" e pressione Enter
# Deve mostrar classificação de intent
```

## 🚀 Executar o Chatbot

### Opção A: Dois Terminais (Recomendado)

**Terminal 1 - Rasa:**
```bash
cd chatbot
source venv/bin/activate
rasa run --enable-api --cors "*" --port 5005
```

**Terminal 2 - Flask:**
```bash
cd chatbot
source venv/bin/activate
python app.py
```

**Aceder:** http://localhost:5020

### Opção B: Script Único
```bash
# Criar script de conveniência
cat > start.sh << 'EOF'
#!/bin/bash
source venv/bin/activate
nohup rasa run --enable-api --cors "*" --port 5005 > rasa.log 2>&1 &
sleep 5
python app.py
EOF

chmod +x start.sh
./start.sh
```

## 🔧 Desenvolvimento

### Workflow Diário
1. **Sempre ativar ambiente:** `source venv/bin/activate`
2. **Após mudanças:** `rasa train`
3. **Testar:** `rasa shell`
4. **Commit:** Git com mensagens claras

### Estrutura Importante
```
data/
├── nlu.yml      # Exemplos de frases dos usuários
├── stories.yml  # Fluxos de conversação
└── rules.yml    # Regras fixas

domain.yml       # Intents, entities e respostas
config.yml       # Configuração do pipeline ML
app.py          # Servidor web Flask
```

### Adicionar Nova Funcionalidade

1. **Nova Intent (pergunta do usuário):**
   - Editar `data/nlu.yml`
   - Adicionar intent em `domain.yml`
   - Criar resposta `utter_*` em `domain.yml`
   - Treinar: `rasa train`

2. **Modificar Resposta:**
   - Encontrar `utter_*` em `domain.yml`
   - Alterar texto
   - Treinar: `rasa train`

## 🐛 Resolução de Problemas

### Problema: "Command not found"
```bash
# Verificar ambiente virtual ativo
source venv/bin/activate

# Reinstalar se necessário
pip install rasa flask
```

### Problema: "Port in use"
```bash
# macOS/Linux
lsof -i :5005
kill -9 [PID]

# Windows
netstat -ano | findstr :5005
taskkill /PID [PID] /F
```

### Problema: Modelo não treina
```bash
# Validar dados
rasa data validate

# Debug detalhado
rasa train --debug
```

### Problema: Interface não carrega
```bash
# Verificar se Rasa está rodando
curl http://localhost:5005/status

# Verificar logs
tail -f rasa.log
```

## 📊 Testes

### Teste Manual
```bash
# Conversa interativa
rasa shell

# Teste específico
rasa shell nlu
# Digite suas perguntas para testar classificação
```

### Validação
```bash
# Verificar integridade dos dados
rasa data validate

# Testes automatizados
rasa test
```

## 🎯 Tarefas Comuns

### Ver Conversas Recentes
```bash
# Consultar base de dados SQLite
sqlite3 rasa_tracker.db
.tables
SELECT * FROM events ORDER BY timestamp DESC LIMIT 10;
.quit
```

### Backup do Modelo Treinado
```bash
# Copiar modelo mais recente
cp models/$(ls -t models/ | head -1) backup_model.tar.gz
```

### Reset Completo
```bash
# Limpar cache e retreinar
rm -rf models/* .rasa/
rasa train
```

## 📝 Convenções do Projeto

### Commits
```bash
# Formato: tipo: descrição
git commit -m "feat: adicionar intent para devoluções"
git commit -m "fix: corrigir resposta de preços"
git commit -m "docs: atualizar README"
```

### Nomes de Intents
- Use snake_case: `tipos_papel`, `horario_atendimento`
- Seja descritivo: `empresa_desconto` em vez de `desconto`

### Nomes de Responses
- Sempre `utter_` + nome da intent
- Exemplo: `utter_tipos_papel`, `utter_precos`

## 🔄 Sincronização com GitHub

### Primeiro Setup
```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"
```

### Workflow de Contribuição
```bash
# Atualizar repositório local
git pull origin main

# Criar branch para nova feature
git checkout -b feature/minha-funcionalidade

# Fazer mudanças...
# Treinar modelo: rasa train
# Testar: rasa shell

# Commit das mudanças
git add .
git commit -m "feat: adicionar nova funcionalidade"

# Push para GitHub
git push origin feature/minha-funcionalidade

# Criar Pull Request no GitHub
```

## 📞 Ajuda

### Documentação Oficial
- [Rasa Docs](https://rasa.com/docs/)
- [Flask Docs](https://flask.palletsprojects.com/)

### Dúvidas Frequentes
1. **Sempre ativar venv** antes de trabalhar
2. **Sempre treinar** após mudanças nos dados
3. **Testar localmente** antes de commit
4. **Verificar logs** em caso de erro

### Contacto
- **Repositório**: https://github.com/casousavng/chatbot
- **Issues**: Criar issue no GitHub para problemas
- **Discussões**: Usar Discussions no GitHub

---

**✅ Com estas instruções, qualquer colaborador deve conseguir configurar e desenvolver o projeto em poucos minutos!**