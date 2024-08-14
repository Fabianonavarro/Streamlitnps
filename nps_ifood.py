import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Configuração da página
st.set_page_config(page_title="Análise de NPS")

# Definição da cor vermelha do iFood
IFOOD_RED = '#FF595E'

# Título principal com cor personalizada
st.markdown(
    """
    <style>
    .title {
        color: #FF595E;
        font-size: 44px;
        font-weight: bold;
    }
    </style>
    <div class="title">Cálculo de NPS da iFood Dev Week</div>
    """,
    unsafe_allow_html=True
)

st.subheader("Análise do Net Promoter Score (NPS)")

@st.cache_data
def carregar_dados():
    """
    Carrega os dados de feedbacks do arquivo CSV e retorna um DataFrame.
    """
    try:
        # Simular uma pausa para carregamento
        import time
        time.sleep(2)
        
        # Carregar dados
        dados = pd.read_csv('feedbacks.csv', delimiter=';')
        
        # Verificar se as colunas necessárias existem
        if 'nota' not in dados.columns or 'comentario' not in dados.columns:
            st.error("O arquivo CSV deve conter as colunas 'nota' e 'comentario'.")
            return None
        
        return dados
    except FileNotFoundError:
        st.error("Arquivo 'feedbacks.csv' não encontrado.")
        return None
    except pd.errors.EmptyDataError:
        st.error("O arquivo 'feedbacks.csv' está vazio.")
        return None
    except pd.errors.ParserError:
        st.error("Erro ao processar o arquivo 'feedbacks.csv'. Verifique o formato.")
        return None
    except Exception as e:
        st.error(f"Erro inesperado ao carregar os dados: {e}")
        return None

def calcular_nps(dados):
    """
    Calcula o NPS com base nos dados fornecidos.
    """
    try:
        feedbacks = dados['nota']
        detratores = sum(1 for nota in feedbacks if nota <= 6)
        promotores = sum(1 for nota in feedbacks if nota >= 9)
        nps = (promotores - detratores) / len(feedbacks) * 100
        return nps
    except ZeroDivisionError:
        st.error("Não há feedbacks suficientes para calcular o NPS.")
        return 0

def criar_grafico_nps(nps):
    """
    Cria e exibe um gráfico de barras horizontal mostrando o NPS.
    """
    # Definição das cores e zonas para o gráfico
    NPS_ZONAS = ['Crítico', 'Aperfeiçoamento', 'Qualidade', 'Excelência']
    NPS_VALORES = [-100, 0, 50, 75, 100]
    NPS_CORES = ['#FF595E', '#FFCA3A', '#8AC926', '#1982C4']
    
    fig, ax = plt.subplots(figsize=(10, 2))

    # Adiciona as zonas do gráfico com cores personalizadas
    for i in range(len(NPS_ZONAS)):
        ax.barh([0], width=NPS_VALORES[i+1] - NPS_VALORES[i], left=NPS_VALORES[i], color=NPS_CORES[i], edgecolor='none')

    # Adiciona a linha preta indicando o NPS
    ax.barh([0], width=1, left=nps, color='black')

    # Ajusta o gráfico
    ax.set_yticks([])
    ax.set_xlim(-100, 100)
    ax.set_xticks(NPS_VALORES)
    ax.set_xticklabels([f'{val}' for val in NPS_VALORES], fontsize=10)

    # Adiciona o valor do NPS no gráfico
    plt.text(nps, 0, f'{nps:.2f}', ha='center', va='center', color='white', bbox=dict(facecolor='black', edgecolor='none', pad=2))

    # Adiciona a legenda
    patches = [mpatches.Patch(color=NPS_CORES[i], label=NPS_ZONAS[i]) for i in range(len(NPS_ZONAS))]
    plt.legend(handles=patches, bbox_to_anchor=(1, 1), loc='upper left')

    # Adiciona o título
    plt.title('Gráfico de NPS da iFood Dev Week', fontsize=14, color='black')

    # Exibe o gráfico
    st.pyplot(fig)

# Carregar dados e calcular NPS
dados = carregar_dados()

if dados is not None:
    with st.spinner("Carregando dados..."):
        nps = calcular_nps(dados)
        criar_grafico_nps(nps)

# Informações adicionais
st.write("---")
st.markdown("""
### Mais informações

- **Perfil do LinkedIn:** [Fabiano de Navarro](https://www.linkedin.com/in/fabiano-de-navarro)
- **Perfil na DIO:** [Nav Info Suporte](https://www.dio.me/users/nav_info_suporte)
- **GitHub:** [Fabiano Navarro](https://github.com/Fabianonavarro)
""")
