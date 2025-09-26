# Guia de Contribuição - Chatbot PaperCare

## 📋 Para Novos Colaboradores

### 🚀 Setup Rápido (< 5 minutos)

```bash
# 1. Clonar o repositório
git clone https://github.com/seu-usuario/chatbot-papercare.git
cd chatbot-papercare

# 2. Configurar ambiente Python
python -m venv venv
source venv/bin/activate  # Linux/macOS
# ou
venv\Scripts\activate     # Windows

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Treinar modelo inicial
rasa train

# 5. Testar instalação
rasa --version
python app.py --help
```

### ✅ Checklist de Verificação

- [ ] Python 3.9+ instalado
- [ ] Ambiente virtual ativo `(venv)` no terminal
- [ ] Rasa instalado sem erros
- [ ] Modelo treinado em `models/`
- [ ] Testes básicos passaram

### 🔧 Comandos Essenciais

```bash
# Desenvolvimento diário
source venv/bin/activate    # Sempre primeiro!
rasa train                 # Após mudanças nos dados
rasa run --cors "*" --enable-api --port 5005 &  # Servidor Rasa
python app.py              # Servidor Flask

# Debug e testes
rasa shell                 # Conversa interativa
rasa test                  # Testes automatizados
rasa data validate         # Validar dados de treino

# Logs e monitorização
tail -f rasa_server.log    # Ver logs Rasa
tail -f flask_server.log   # Ver logs Flask
```

## 🏗️ Estrutura de Desenvolvimento

### Fluxo de Trabalho

1. **Criar branch para feature**:
   ```bash
   git checkout -b feature/nome-da-funcionalidade
   ```

2. **Desenvolver e testar**:
   ```bash
   # Fazer mudanças...
   rasa train
   rasa test
   ```

3. **Commit com padrão**:
   ```bash
   git add .
   git commit -m "feat: adicionar intent para devoluções"
   ```

4. **Push e Pull Request**:
   ```bash
   git push origin feature/nome-da-funcionalidade
   # Criar PR no GitHub
   ```

### Padrões de Commit

```
feat: nova funcionalidade
fix: correção de bug
docs: documentação
style: formatação
refactor: refatoração
test: testes
chore: manutenção
```

## 📁 Arquivos Importantes

### Não Modificar Diretamente
- `models/` - Gerado automaticamente
- `__pycache__/` - Cache Python
- `*.db` - Bases de dados
- `.rasa/` - Cache do Rasa

### Arquivos de Configuração
- `config.yml` - Pipeline ML
- `domain.yml` - Intent/responses
- `endpoints.yml` - Configuração de serviços
- `credentials.yml` - Credenciais (não versionar!)

### Dados de Treino
- `data/nlu.yml` - Exemplos de frases
- `data/stories.yml` - Fluxos de conversa
- `data/rules.yml` - Regras fixas

## 🎯 Tarefas Comuns

### Adicionar Nova Intent

1. **Editar `data/nlu.yml`**:
```yaml
- intent: devolucoes
  examples: |
    - quero devolver um produto
    - como faço para devolver
    - política de devolução
```

2. **Editar `domain.yml`**:
```yaml
intents:
  - devolucoes

responses:
  utter_devolucoes:
    - text: "Nossa política de devolução permite..."
```

3. **Treinar e testar**:
```bash
rasa train
rasa shell  # Testar: "quero devolver"
```

### Modificar Resposta Existente

1. **Encontrar no `domain.yml`**:
```yaml
responses:
  utter_sustentabilidade:
    - text: "🌍 Texto atual..."
```

2. **Modificar conteúdo**:
```yaml
responses:
  utter_sustentabilidade:
    - text: "🌍 Novo texto melhorado..."
      buttons:
        - title: "Mais Info"
          payload: "info tecnica"
```

3. **Treinar novamente**:
```bash
rasa train
```

### Adicionar Botões Interativos

```yaml
responses:
  utter_resposta_com_botoes:
    - text: "Escolha uma opção:"
      buttons:
        - title: "🧻 Produtos"
          payload: "tipos de papel"
        - title: "💰 Preços"
          payload: "precos"
        - title: "🌱 Sustentabilidade"
          payload: "sustentabilidade"
```

## 🐛 Problemas Comuns

### "rasa: command not found"
```bash
# Ativar ambiente virtual
source venv/bin/activate

# Reinstalar se necessário
pip install rasa
```

### "Port 5005 already in use"
```bash
# Encontrar processo
lsof -i :5005

# Matar processo
kill -9 [PID]
```

### Modelo não treina
```bash
# Validar dados primeiro
rasa data validate

# Treino forçado
rasa train --force

# Debug detalhado
rasa train --debug
```

### Flask não conecta ao Rasa
```bash
# Verificar se Rasa está rodando
curl http://localhost:5005/status

# Verificar configuração proxy em app.py
```

## 📊 Testes e Validação

### Testes Manuais
```bash
# Conversa interativa
rasa shell

# Testar intent específica
rasa shell nlu
# Digite: "qual o preço?"
```

### Testes Automatizados
```bash
# Executar todos os testes
rasa test

# Testar apenas NLU
rasa test nlu

# Testar apenas stories
rasa test core
```

### Validação de Dados
```bash
# Verificar consistência
rasa data validate

# Verificar stories
rasa data validate stories

# Verificar NLU
rasa data validate nlu
```

## 🎨 Frontend (Templates)

### Modificar Interface
- `templates/index.html` - Página principal
- `templates/admin.html` - Dashboard admin

### CSS Customizado
```css
/* Adicionar em templates/index.html */
<style>
.chat-container {
    /* Seus estilos aqui */
}
</style>
```

### JavaScript Personalizado
```javascript
// Adicionar funções personalizadas
function minhaFuncao() {
    // Sua lógica aqui
}
```

## 🗄️ Base de Dados

### Estrutura SQLite
- `chatbot_kpis.db` - Métricas e KPIs
- `rasa_tracker.db` - Conversas do Rasa

### Consultas Úteis
```sql
-- Ver conversas recentes
SELECT * FROM conversations ORDER BY timestamp DESC LIMIT 10;

-- Intents mais usados
SELECT intent, COUNT(*) as count 
FROM messages 
GROUP BY intent 
ORDER BY count DESC;
```

## 🔧 Configurações Avançadas

### Ajustar Pipeline ML
```yaml
# config.yml
pipeline:
  - name: WhitespaceTokenizer
  - name: RegexFeaturizer
  - name: LexicalSyntacticFeaturizer
  - name: CountVectorsFeaturizer
  - name: DIETClassifier
    epochs: 100  # Ajustar conforme necessário
```

### Configurar Policies
```yaml
# config.yml
policies:
  - name: MemoizationPolicy
  - name: RulePolicy
  - name: UnexpecTEDIntentPolicy
    max_history: 5
  - name: TEDPolicy
    max_history: 5
    epochs: 100
```

## 📞 Suporte

### Dúvidas Frequentes
1. **Ambiente virtual**: Sempre ativar antes de trabalhar
2. **Treino**: Sempre após mudanças em dados
3. **Testes**: Validar antes de commit
4. **Logs**: Verificar em caso de erro

### Contactos
- **Lead Developer**: André Sousa
- **Documentation**: README.md
- **Issues**: GitHub Issues

---

**🚀 Pronto para contribuir? Siga este guia e será produtivo em minutos!**