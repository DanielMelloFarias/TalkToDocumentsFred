import streamlit as st
from typing import Generator
from groq import Groq
from streamlit_chat import message
import random

st.set_page_config(page_icon="💬", layout="wide",
                   page_title="Groq Goes Brrrrrrrr...")


st.subheader("Groq Chat Streamlit App", divider="rainbow", anchor=False)

if "history" not in st.session_state:
    st.session_state.history = []

api_key = st.secrets["GROQ_API_KEY"]
app_key = api_key

if "app_key" not in st.session_state:
    app_key = api_key
    if app_key:
        st.session_state.app_key = api_key

client = Groq(
    api_key=st.secrets["GROQ_API_KEY"],
)

chat = client.start_chat(history = st.session_state.history)

# Initialize chat history and selected model
if "messages" not in st.session_state:
    st.session_state.messages = []

if "selected_model" not in st.session_state:
    st.session_state.selected_model = None

# Define model details
models = {
    "gemma-7b-it": {"name": "Gemma-7b-it", "tokens": 8192, "developer": "Google"},
    "llama2-70b-4096": {"name": "LLaMA2-70b-chat", "tokens": 4096, "developer": "Meta"},
    "llama3-70b-8192": {"name": "LLaMA3-70b-8192", "tokens": 8192, "developer": "Meta"},
    "llama3-8b-8192": {"name": "LLaMA3-8b-8192", "tokens": 8192, "developer": "Meta"},
    "mixtral-8x7b-32768": {"name": "Mixtral-8x7b-Instruct-v0.1", "tokens": 32768, "developer": "Mistral"},
}

models = "llama3-70b-8192"

# Layout for model selection and max_tokens slider
col1, col2 = st.columns(2)

with col1:
    model_option = st.selectbox(
        "Choose a model:",
        options=list(models.keys()),
        format_func=lambda x: models[x]["name"],
        index=4  # Default to mixtral
    )

# Detect model change and clear chat history if model has changed
if st.session_state.selected_model != model_option:
    st.session_state.messages = []
    st.session_state.selected_model = model_option

max_tokens_range = models[model_option]["tokens"]

with col2:
    # Adjust max_tokens slider dynamically based on the selected model
    max_tokens = st.slider(
        "Max Tokens:",
        min_value=512,  # Minimum value to allow some flexibility
        max_value=max_tokens_range,
        # Default value or max allowed if less
        value=min(32768, max_tokens_range),
        step=512,
        help=f"Adjust the maximum number of tokens (words) for the model's response. Max for selected model: {max_tokens_range}"
    )

max_tokens = 8192

# Sidebar com botão para limpar a janela de chat.
with st.sidebar:
    if st.button("Clear Chat Window", use_container_width=True, type="primary"):
        st.session_state.history = []
        st.rerun()

# Exibe as mensagens de chat anteriores.
for message in chat.history:
    role ="assistant" if message.role == 'model' else message.role
    with st.chat_message(role):
        st.markdown(message.parts[0].text)

contexto = "Voce está numa entrevista para uma vaga de Especialista em Inovação e IA para empresa: Magnum Tires. Agora esse é um texto da minha vida e currículo. Com uma jornada profissional marcada por inovação, liderança e um profundo compromisso com a transformação digital na saúde, eu, Daniel Gomes de Mello Farias, trilhei um caminho que mescla conhecimento técnico avançado com uma visão estratégica voltada para o futuro da tecnologia aplicada à saúde. Mestre em Modelagem Computacional do Conhecimento e Ciência e Tecnologia na Saúde, minha formação acadêmica e profissional reflete uma dedicação contínua ao aprimoramento e aplicação prática de soluções inovadoras. Minha experiência como Líder Técnico no Hospital Sírio Libanês e PMO de Projetos Estratégicos na Secretaria de Saúde do Estado de Alagoas destaca minha capacidade de conduzir equipes e projetos com o objetivo de integrar tecnologias emergentes como a Inteligência Artificial, Realidade Aumentada/Virtual, e Ciência de Dados, para transformar a experiência de pacientes e profissionais de saúde. Essa trajetória é complementada por minha atuação como mentor e avaliador de startups no programa Inovativa Brasil, onde auxilio na orientação de jovens empresas que buscam revolucionar o mercado de saúde com tecnologias disruptivas. As certificações profissionais em Gestão de Projetos e Inteligência Artificial e Machine Learning atestam meu compromisso com a excelência e a constante atualização em áreas chave para a inovação na saúde. Além disso, a honra de ter sido reconhecido com o 3º melhor paper no XI North Northeast Congress of Research and Innovation sublinha minha contribuição acadêmica e profissional para o campo da engenharia e tecnologia. Minha visão é conduzida pela crença de que a verdadeira inovação surge na interseção entre a tecnologia, a saúde e a capacidade de antecipar as necessidades futuras da sociedade. Por isso, me dedico a explorar como a análise de dados e as tecnologias emergentes podem ser aplicadas para prever tendências de saúde, otimizar tratamentos e promover um sistema de saúde mais integrado e eficiente. Em busca de novos desafios e oportunidades, estou sempre aberto a colaborações que permitam utilizar minha expertise técnica, liderança e paixão por inovação, para criar soluções que não apenas resolvam problemas complexos, mas que também melhorem a qualidade de vida das pessoas. Através da minha jornada, pretendo continuar impactando positivamente o setor da saúde, liderando pelo exemplo e inspirando outros a explorarem o potencial ilimitado da tecnologia para fazer a diferença no mundo. Você está sendo entrevistado então responda sempre de maneira educada as perguntas, seja gentil e responda sempre na 1 pessoa. Ao final da resposta (baseado no texto anterior) faça uma outra pergunta pra pessoa (mas n mencione saúde). Responda smepre em até 1 parágrafo de até 50 palavras. Caso for falar da empresa Magnum Tires, pode ser criativo e pegar da sua base."
# Permite ao usuário enviar uma nova mensagem e exibe a resposta do assistente
if "app_key" in st.session_state:
    if prompt := st.chat_input(""):
        prompt = prompt.replace('\n', ' \n')
        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            message_placeholder.markdown("Thinking...")
            try:
                full_response = ""
                for chunk in chat.send_message(contexto + prompt, stream=True):
                    word_count = 0
                    random_int = random.randint(5,10)
                    for word in chunk.text:
                        full_response+=word
                        word_count+=1
                        if word_count == random_int:
                            time.sleep(0.05)
                            message_placeholder.markdown(full_response + "_")
                            word_count = 0
                            random_int = random.randint(5,10)
                message_placeholder.markdown(full_response)
            except client.types.generation_types.BlockedPromptException as e:
                st.exception(e)
            except Exception as e:
                st.exception(e)
            # Atualiza o histórico de chat no estado da sessão para incluir a interação mais recente.
            st.session_state.history = chat.history
            st.session_state.history = []




