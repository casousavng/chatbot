#!/bin/bash

# 🧻 Chatbot PaperCare - Script de Setup Automático
# Autor: André Sousa
# Descrição: Script para configuração automática do ambiente

set -e  # Parar em caso de erro

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Função para imprimir com cores
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_header() {
    echo -e "${BLUE}"
    echo "🧻 ======================================"
    echo "   CHATBOT PAPERCARE - SETUP"
    echo "   Configuração Automática"
    echo "======================================${NC}"
    echo
}

# Verificar pré-requisitos
check_prerequisites() {
    print_status "Verificando pré-requisitos..."
    
    # Verificar Python
    if ! command -v python3 &> /dev/null; then
        print_error "Python 3 não encontrado. Instale Python 3.9+ primeiro."
        exit 1
    fi
    
    PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
    print_status "Python $PYTHON_VERSION detectado"
    
    # Verificar pip
    if ! command -v pip3 &> /dev/null; then
        print_error "pip3 não encontrado. Instale pip primeiro."
        exit 1
    fi
    
    # Verificar Git (opcional)
    if command -v git &> /dev/null; then
        print_status "Git detectado - $(git --version)"
    else
        print_warning "Git não encontrado - versioning não estará disponível"
    fi
    
    print_success "Pré-requisitos verificados!"
}

# Criar ambiente virtual
setup_virtual_environment() {
    print_status "Configurando ambiente virtual..."
    
    if [ -d "venv" ]; then
        print_warning "Ambiente virtual já existe. Removendo..."
        rm -rf venv
    fi
    
    python3 -m venv venv
    
    # Ativar ambiente virtual
    source venv/bin/activate
    
    # Atualizar pip
    pip install --upgrade pip
    
    print_success "Ambiente virtual criado e ativado!"
}

# Instalar dependências
install_dependencies() {
    print_status "Instalando dependências..."
    
    if [ ! -f "requirements.txt" ]; then
        print_error "Arquivo requirements.txt não encontrado!"
        exit 1
    fi
    
    # Instalar dependências do projeto
    pip install -r requirements.txt
    
    # Verificar instalação do Rasa
    if rasa --version &> /dev/null; then
        RASA_VERSION=$(rasa --version)
        print_success "Rasa instalado: $RASA_VERSION"
    else
        print_error "Erro na instalação do Rasa"
        exit 1
    fi
    
    print_success "Dependências instaladas com sucesso!"
}

# Verificar estrutura do projeto
check_project_structure() {
    print_status "Verificando estrutura do projeto..."
    
    required_files=("config.yml" "domain.yml" "data/nlu.yml" "data/stories.yml" "app.py")
    missing_files=()
    
    for file in "${required_files[@]}"; do
        if [ ! -f "$file" ]; then
            missing_files+=("$file")
        fi
    done
    
    if [ ${#missing_files[@]} -ne 0 ]; then
        print_error "Arquivos obrigatórios não encontrados:"
        for file in "${missing_files[@]}"; do
            echo "  - $file"
        done
        exit 1
    fi
    
    print_success "Estrutura do projeto verificada!"
}

# Treinar modelo inicial
train_initial_model() {
    print_status "Treinando modelo inicial..."
    
    # Validar dados primeiro
    if rasa data validate; then
        print_success "Dados de treino validados!"
    else
        print_warning "Problemas encontrados nos dados, mas continuando..."
    fi
    
    # Treinar modelo
    if rasa train --quiet; then
        print_success "Modelo treinado com sucesso!"
        
        # Listar modelos disponíveis
        if ls models/*.tar.gz 1> /dev/null 2>&1; then
            latest_model=$(ls -t models/*.tar.gz | head -n1)
            print_status "Modelo mais recente: $(basename $latest_model)"
        fi
    else
        print_error "Erro no treino do modelo"
        exit 1
    fi
}

# Testar instalação
test_installation() {
    print_status "Testando instalação..."
    
    # Testar Rasa NLU
    echo "olá" | rasa shell nlu --quiet > /dev/null 2>&1
    if [ $? -eq 0 ]; then
        print_success "Rasa NLU funcionando!"
    else
        print_warning "Problemas com Rasa NLU"
    fi
    
    # Testar Flask (básico)
    if python3 -c "import flask; print('Flask OK')" > /dev/null 2>&1; then
        print_success "Flask funcionando!"
    else
        print_warning "Problemas com Flask"
    fi
    
    print_success "Testes básicos completados!"
}

# Criar scripts de conveniência
create_convenience_scripts() {
    print_status "Criando scripts de conveniência..."
    
    # Script para iniciar servidores
    cat > start_servers.sh << 'EOF'
#!/bin/bash
# Script para iniciar os servidores do chatbot

echo "🚀 Iniciando Chatbot PaperCare..."

# Ativar ambiente virtual
source venv/bin/activate

# Verificar se as portas estão livres
if lsof -i :5005 > /dev/null 2>&1; then
    echo "⚠️  Porta 5005 já em uso. Finalizando processo..."
    pkill -f "rasa run"
fi

if lsof -i :5020 > /dev/null 2>&1; then
    echo "⚠️  Porta 5020 já em uso. Finalizando processo..."
    pkill -f "python.*app.py"
fi

# Iniciar Rasa em background
echo "🔄 Iniciando servidor Rasa (porta 5005)..."
nohup rasa run --enable-api --cors "*" --port 5005 > rasa_server.log 2>&1 &

# Aguardar Rasa inicializar
sleep 10

# Iniciar Flask
echo "🔄 Iniciando servidor Flask (porta 5020)..."
python app.py

echo "✅ Servidores iniciados!"
echo "📱 Interface: http://localhost:5020"
echo "🤖 API Rasa: http://localhost:5005"
EOF

    chmod +x start_servers.sh
    
    # Script para parar servidores
    cat > stop_servers.sh << 'EOF'
#!/bin/bash
# Script para parar os servidores do chatbot

echo "🛑 Parando servidores..."

# Parar Rasa
pkill -f "rasa run"

# Parar Flask
pkill -f "python.*app.py"

echo "✅ Servidores parados!"
EOF

    chmod +x stop_servers.sh
    
    # Script para retreinar modelo
    cat > retrain_model.sh << 'EOF'
#!/bin/bash
# Script para retreinar o modelo

echo "🎓 Retreinando modelo..."

# Ativar ambiente virtual
source venv/bin/activate

# Validar dados
echo "📋 Validando dados..."
rasa data validate

# Treinar modelo
echo "🔄 Treinando..."
rasa train

echo "✅ Modelo retreinado!"
echo "🔄 Reinicie os servidores para aplicar: ./start_servers.sh"
EOF

    chmod +x retrain_model.sh
    
    print_success "Scripts criados: start_servers.sh, stop_servers.sh, retrain_model.sh"
}

# Mostrar instruções finais
show_final_instructions() {
    print_success "🎉 Setup completado com sucesso!"
    echo
    echo "📋 Próximos passos:"
    echo "  1. Para iniciar o chatbot:"
    echo "     ./start_servers.sh"
    echo
    echo "  2. Acesse no navegador:"
    echo "     http://localhost:5020"
    echo
    echo "  3. Para parar os servidores:"
    echo "     ./stop_servers.sh"
    echo
    echo "  4. Para retreinar o modelo após mudanças:"
    echo "     ./retrain_model.sh"
    echo
    echo "📚 Documentação:"
    echo "  - README.md - Guia completo"
    echo "  - CONTRIBUTING.md - Guia para desenvolvedores"
    echo
    echo "🐛 Em caso de problemas:"
    echo "  - Verifique logs: tail -f rasa_server.log"
    echo "  - Ative ambiente: source venv/bin/activate"
    echo "  - Valide dados: rasa data validate"
    echo
    print_success "Divirta-se desenvolvendo! 🚀"
}

# Função principal
main() {
    print_header
    
    check_prerequisites
    echo
    
    setup_virtual_environment
    echo
    
    install_dependencies
    echo
    
    check_project_structure
    echo
    
    train_initial_model
    echo
    
    test_installation
    echo
    
    create_convenience_scripts
    echo
    
    show_final_instructions
}

# Executar função principal
main