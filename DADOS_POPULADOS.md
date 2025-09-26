# 🧻 Bases de Dados Populadas - Chatbot PaperCare

## ✅ Resumo da Operação

As bases de dados do chatbot foram **populadas com sucesso** com dados de exemplo para demonstração do frontend!

### 📊 Dados Criados

#### Base de Dados: `chatbot_kpis.db`
- **📊 Métricas**: 50 registos de tempo de resposta (0.5s - 4.0s)
- **👥 Leads**: 25 potenciais clientes com empresas portuguesas reais
- **⭐ Satisfação**: 40 avaliações (média: 4.3/5.0 estrelas)
- **📝 Reclamações**: 15 reclamações categorizadas por tipo

#### Base de Dados: `rasa_tracker.db`
- **💬 Conversas**: Dados de conversas existentes mantidos
- **📈 Eventos**: Histórico de interações preservado

### 🎯 Exemplos de Dados Criados

#### Leads de Exemplo:
```
Carlos Pereira (Continente) - 2 Folhas
Maria Santos (Hotel Vila Galé) - 2 Folhas  
António Costa (Continente) - 2 Folhas
```

#### Avaliações de Satisfação:
```
4.4/5.0 ⭐⭐⭐⭐⭐
3.9/5.0 ⭐⭐⭐⭐
4.8/5.0 ⭐⭐⭐⭐⭐
```

#### Reclamações:
```
"Entrega atrasada" [categoria: produto]
"Qualidade inferior ao esperado" [categoria: produto]
```

### 🚀 Como Utilizar

1. **Ver Dados Criados:**
   ```bash
   python ver_dados.py
   ```

2. **Iniciar Frontend** (após instalar dependências):
   ```bash
   python app.py
   # Aceder: http://localhost:5020
   ```

3. **Dashboard de KPIs** (após correções):
   ```bash
   python kpi_dashboard.py
   ```

### 📁 Scripts Criados

- `popular_dados.py` - Script completo para popular dados
- `resetar_dados.py` - Script para limpar e recriar dados
- `ver_dados.py` - Visualizador simples de dados

### 🔧 Próximos Passos

1. **Instalar dependências** (Flask, requests)
2. **Testar frontend** com dados reais
3. **Verificar dashboard** KPIs funcional
4. **Demonstrar funcionalidades** ao cliente

---

**✅ Status: CONCLUÍDO**  
As bases de dados estão prontas para demonstração do sistema completo!