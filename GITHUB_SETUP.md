# 📚 Guia de Publicação no GitHub

## 🚀 Passos para Publicar o Projeto

### 1. Preparar o Repositório Local

```bash
# Navegar para o diretório do projeto
cd "/Users/andresousa/Desktop/Mars Shot Projects/chatbot"

# Inicializar Git (se ainda não foi feito)
git init

# Adicionar todos os arquivos
git add .

# Fazer commit inicial
git commit -m "feat: initial commit - Chatbot PaperCare v1.0.0

- Sistema completo de FAQ para produtos de papel higiénico
- Interface web responsiva com chat interativo
- Respostas 100% em português
- 12 intents principais implementados
- Dashboard KPI básico
- Documentação completa
- Scripts de setup automático"
```

### 2. Criar Repositório no GitHub

1. **Acesse**: https://github.com
2. **Clique**: "New repository" 
3. **Nome**: `chatbot-papercare`
4. **Descrição**: `🧻 Chatbot inteligente para produtos de papel higiénico - Rasa + Flask`
5. **Tipo**: Public (ou Private se preferir)
6. **NÃO** inicializar com README (já temos)
7. **Clique**: "Create repository"

### 3. Conectar Repositório Local ao GitHub

```bash
# Adicionar origem remota (substituir SEU-USUARIO)
git remote add origin https://github.com/SEU-USUARIO/chatbot-papercare.git

# Verificar configuração
git remote -v

# Definir branch principal
git branch -M main

# Fazer push inicial
git push -u origin main
```

### 4. Configurar o Repositório

#### Adicionar Tópicos (GitHub Topics)
Na página do repositório, clique em "Add topics":
- `chatbot`
- `rasa`
- `flask`
- `python`
- `machine-learning`
- `nlp`
- `portuguese`
- `customer-service`

#### Atualizar Descrição
```
🧻 Chatbot inteligente especializado em produtos de papel higiénico. Desenvolvido com Rasa Framework e Flask, fornece informações sobre produtos, preços, sustentabilidade e suporte ao cliente em português.
```

#### Configurar GitHub Pages (opcional)
1. Vá em Settings > Pages
2. Source: Deploy from a branch
3. Branch: main
4. Folder: / (root)

### 5. Criar Release v1.0.0

```bash
# Criar tag para versão
git tag -a v1.0.0 -m "Release v1.0.0: Chatbot PaperCare

Funcionalidades principais:
✅ Sistema de FAQ completo
✅ Interface web responsiva  
✅ Respostas 100% em português
✅ 12 intents implementados
✅ Dashboard KPI básico
✅ Documentação completa
✅ Scripts de setup automático

Tecnologias:
- Rasa 3.6+ (NLU/Core)
- Flask 2.0+ (Backend)
- Python 3.9+
- SQLite (Database)
- HTML/CSS/JS (Frontend)"

# Push da tag
git push origin v1.0.0
```

No GitHub:
1. Vá em "Releases"
2. Clique "Create a new release"
3. Tag: v1.0.0
4. Title: "🧻 Chatbot PaperCare v1.0.0"
5. Descrição: (copiar da tag)
6. Marcar "Set as the latest release"
7. Publish release

### 6. Configurar Issues e Pull Requests

#### Labels Sugeridos
Criar labels em Settings > Labels:
- `bug` 🐛 - Correções de bugs
- `enhancement` ✨ - Novas funcionalidades  
- `documentation` 📝 - Melhorias na documentação
- `good first issue` 👋 - Bom para iniciantes
- `help wanted` 🤝 - Precisa de ajuda
- `intent` 🎯 - Relacionado a intents
- `frontend` 🎨 - Interface web
- `backend` ⚙️ - Servidor/API
- `ml-model` 🧠 - Modelo de ML

#### Templates de Issue
Criar `.github/ISSUE_TEMPLATE/`:

**bug_report.md**:
```markdown
---
name: Bug Report
about: Reportar um problema
title: '[BUG] '
labels: bug
---

**Descreva o bug**
Descrição clara e concisa do problema.

**Para Reproduzir**
Passos para reproduzir:
1. Vá para '...'
2. Digite '...'
3. Veja o erro

**Comportamento Esperado**
O que deveria acontecer.

**Screenshots**
Se aplicável, adicione screenshots.

**Ambiente:**
- OS: [e.g. macOS, Windows, Linux]
- Python: [e.g. 3.9.1]
- Rasa: [e.g. 3.6.20]
```

### 7. Configurar CI/CD (opcional)

Criar `.github/workflows/ci.yml`:
```yaml
name: CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v3
      with:
        python-version: '3.9'
        
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        
    - name: Validate Rasa data
      run: |
        rasa data validate
        
    - name: Train model
      run: |
        rasa train
        
    - name: Test model
      run: |
        rasa test nlu --cross-validation
```

### 8. Adicionar Badges ao README

Adicionar no topo do README.md:
```markdown
![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Rasa](https://img.shields.io/badge/Rasa-3.6.0+-orange.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![GitHub release](https://img.shields.io/github/v/release/SEU-USUARIO/chatbot-papercare)
![GitHub issues](https://img.shields.io/github/issues/SEU-USUARIO/chatbot-papercare)
![GitHub stars](https://img.shields.io/github/stars/SEU-USUARIO/chatbot-papercare)
```

### 9. Convidar Colaboradores

1. Vá em Settings > Manage access
2. Clique "Invite a collaborator"
3. Digite o username dos colegas
4. Escolha permissões (Write para colaboradores)

### 10. Criar Branch de Desenvolvimento

```bash
# Criar branch de desenvolvimento
git checkout -b develop
git push -u origin develop

# Configurar develop como branch padrão no GitHub
# Settings > Branches > Default branch > develop
```

## 📋 Checklist Final

### Antes de Publicar
- [ ] Código testado e funcionando
- [ ] Documentação completa (README, CONTRIBUTING, etc.)
- [ ] .gitignore configurado
- [ ] Dependências listadas em requirements.txt
- [ ] Licença definida (MIT)
- [ ] Commits organizados e descritivos

### Após Publicar
- [ ] Repository configurado (descrição, tópicos)
- [ ] Release v1.0.0 criado
- [ ] Issues e PR templates configurados
- [ ] CI/CD configurado (opcional)
- [ ] Colaboradores convidados
- [ ] Branch development criado

### Para Colaboradores
- [ ] README enviado aos colegas
- [ ] QUICKSTART testado
- [ ] Scripts de setup validados
- [ ] Permissões de acesso concedidas

## 🎯 Próximos Passos

1. **Testar com colegas**: Pedir para seguirem o QUICKSTART.md
2. **Coletar feedback**: Criar issues para melhorias
3. **Planejar v1.1.0**: Baseado no feedback recebido
4. **Documentar problemas**: Atualizar troubleshooting
5. **Otimizar performance**: Monitorar uso e performance

---

## 📞 Comandos de Referência Rápida

```bash
# Clonar (para novos colaboradores)
git clone https://github.com/SEU-USUARIO/chatbot-papercare.git
cd chatbot-papercare

# Setup automático
./setup.sh

# Iniciar desenvolvimento
git checkout -b feature/minha-feature
# ... fazer mudanças ...
git add . && git commit -m "feat: minha nova feature"
git push origin feature/minha-feature
# Criar PR no GitHub

# Atualizar com mudanças remotas
git checkout main
git pull origin main
git checkout develop
git pull origin develop
```

**🚀 Projeto pronto para o GitHub e colaboradores!**