import streamlit as st
import pandas as pd
import gdown
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

st.set_page_config(page_title="NAVINFO")

with st.container():

    st.title("Exemplo de Calculo NPS da iFood Dev Week ")

    st.subheader("Navinfo + Streamlit + iFood Dev Week")
    
    st.write("Informações sobre Gráfico de NPS da iFood Dev Week")

   
    
@st.cache_data

class Feedback:
  def __init__(self, nota, comentario):
    self.nota = nota
    self.comentario = comentario

class AnalisadorFeedback:
  def __init__(self, feedbacks):
    self.feedbacks = feedbacks

  def calcular_nps(self):
    # Por ser uma list do Python, aplicamos o conceito de "list comprehension" para filtrar nossos Feedbacks.
    detratores = sum(1 for feedback in self.feedbacks if feedback.nota <= 6)
    promotores = sum(1 for feedback in self.feedbacks if feedback.nota >= 9)

    return (promotores - detratores) / len(self.feedbacks) * 100

    def carregar_dados():dados = pd.read_csv('feedbacks.csv', delimiter = ';')

    feedbacks = [Feedback(linha['nota'], linha['comentario'])  for i, linha in dados.iterrows()]

    analisador = AnalisadorFeedback(feedbacks)
    nps = analisador.calcular_nps()
    return tabela
    st.write("---")

with st.container():
    st.write("---")
# Definição das constantes que usaremos para visualizar o NPS
    NPS_ZONAS =   ['Crítico', 'Aperfeiçoamento', 'Qualidade', 'Excelência']
    NPS_VALORES = [-100, 0, 50, 75, 100]
    NPS_CORES =   ['#FF595E', '#FFCA3A', '#8AC926', '#1982C4']

def criar_grafico_nps(nps):
  # Inicia a figura e os eixos.
   fig, ax = plt.subplots(figsize=(10, 2))

  # Itera sobre as zonas para criar a barra de cores do gráfico.
   for i, zona in enumerate(NPS_ZONAS):
       ax.barh([0], width=NPS_VALORES[i+1]-NPS_VALORES[i], left=NPS_VALORES[i], color=NPS_CORES[i])

  # Cria a "seta" que vai indicar o NPS no gráfico.
       ax.barh([0], width=1, left=nps, color='black')
  # Remove os ticks do eixo Y
       ax.set_yticks([])
  # Define os limites do eixo X
       ax.set_xlim(-100, 100)
  # Define os ticks do eixo X
       ax.set_xticks(NPS_VALORES)
  
  # Inclui um texto com o valor de NPS, o qual ficará alinhado com a "seta" criada anteriormente.
       plt.text(nps, 0, f'{nps:.2f}', ha='center', va='center', color='white', bbox=dict(facecolor='black'))

  # Cria a legenda do gráfico
       patches = [mpatches.Patch(color=NPS_CORES[i], label=NPS_ZONAS[i]) for i in range(len(NPS_ZONAS))]
       plt.legend(handles=patches, bbox_to_anchor=(1,1))

  # Inclui um título no gráfico.

       plt.title('Gráfico de NPS da iFood Dev Week')

  # Mostra o gráfico.
plt.show()

#criar_grafico_nps(nps)

st.write("---")

st.write("Quer Saber mais sobre o Fabiano ? [Clique aqui](https://www.linkedin.com/in/fabiano-de-navarro)")

