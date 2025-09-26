#!/bin/bash

# 🧪 Script de Teste - Chatbot PaperCare
# Verifica se o ambiente está configurado corretamente

echo "🧻 Testando Chatbot PaperCare..."
echo "================================="

# Verificar se está no diretório correto
if [ ! -f "domain.yml" ]; then
    echo "❌ Erro: Execute este script no diretório do projeto"
    exit 1
fi

# Verificar ambiente virtual
if [ -z "$VIRTUAL_ENV" ]; then
    echo "⚠️  Ambiente virtual não ativo. Tentando ativar..."
    if [ -f "venv/bin/activate" ]; then
        source venv/bin/activate
        echo "✅ Ambiente virtual ativado"
    else
        echo "❌ Ambiente virtual não encontrado. Execute: python -m venv venv"
        exit 1
    fi
else
    echo "✅ Ambiente virtual ativo: $VIRTUAL_ENV"
fi

# Verificar Python
PYTHON_VERSION=$(python --version 2>&1)
echo "✅ $PYTHON_VERSION"

# Verificar Rasa
if command -v rasa &> /dev/null; then
    RASA_VERSION=$(rasa --version 2>&1 | head -1)
    echo "✅ $RASA_VERSION"
else
    echo "❌ Rasa não encontrado. Execute: pip install -r requirements.txt"
    exit 1
fi

# Verificar Flask
if python -c "import flask; print(f'✅ Flask {flask.__version__}')" 2>/dev/null; then
    echo "✅ Flask instalado"
else
    echo "❌ Flask não encontrado"
    exit 1
fi

# Verificar estrutura do projeto
echo ""
echo "📁 Verificando estrutura do projeto..."

required_files=("config.yml" "domain.yml" "data/nlu.yml" "data/stories.yml" "app.py")
for file in "${required_files[@]}"; do
    if [ -f "$file" ]; then
        echo "✅ $file"
    else
        echo "❌ $file não encontrado"
    fi
done

# Verificar dados de treino
echo ""
echo "📊 Validando dados de treino..."
if rasa data validate --quiet; then
    echo "✅ Dados de treino válidos"
else
    echo "⚠️  Problemas encontrados nos dados de treino"
fi

# Verificar modelo
echo ""
echo "🧠 Verificando modelo..."
if ls models/*.tar.gz 1> /dev/null 2>&1; then
    latest_model=$(ls -t models/*.tar.gz | head -n1)
    echo "✅ Modelo encontrado: $(basename $latest_model)"
else
    echo "⚠️  Nenhum modelo encontrado. Execute: rasa train"
fi

# Teste de NLU
echo ""
echo "🧪 Testando NLU..."
if echo "olá" | rasa shell nlu --quiet 2>/dev/null | grep -q "intent"; then
    echo "✅ NLU funcionando"
else
    echo "⚠️  Problemas com NLU"
fi

# Verificar portas
echo ""
echo "🔍 Verificando portas..."
if lsof -i :5005 > /dev/null 2>&1; then
    echo "⚠️  Porta 5005 em uso (Rasa pode estar rodando)"
else
    echo "✅ Porta 5005 livre"
fi

if lsof -i :5020 > /dev/null 2>&1; then
    echo "⚠️  Porta 5020 em uso (Flask pode estar rodando)"
else
    echo "✅ Porta 5020 livre"
fi

echo ""
echo "🎯 Resumo dos Testes:"
echo "===================="

# Contar sucessos
success_count=0
if command -v rasa &> /dev/null; then ((success_count++)); fi
if python -c "import flask" 2>/dev/null; then ((success_count++)); fi
if [ -f "domain.yml" ]; then ((success_count++)); fi
if [ -f "data/nlu.yml" ]; then ((success_count++)); fi

if [ $success_count -eq 4 ]; then
    echo "🎉 Todos os testes passaram! Projeto pronto para usar."
    echo ""
    echo "📋 Próximos passos:"
    echo "1. Treinar modelo: rasa train"
    echo "2. Iniciar Rasa: rasa run --enable-api --cors '*' --port 5005"
    echo "3. Iniciar Flask: python app.py"
    echo "4. Abrir: http://localhost:5020"
else
    echo "⚠️  Alguns testes falharam. Verifique as mensagens acima."
    echo ""
    echo "💡 Dicas:"
    echo "- Ativar ambiente virtual: source venv/bin/activate"
    echo "- Instalar dependências: pip install -r requirements.txt"
    echo "- Treinar modelo: rasa train"
fi

echo ""
echo "📖 Documentação: README.md"
echo "👥 Para colaboradores: COLABORADORES.md"