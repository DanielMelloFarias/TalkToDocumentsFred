import streamlit as st
from typing import Generator
from groq import Groq

reference_text = '''
Documento: Diário Oficial da União - Portaria Nº 156, de 28 de Novembro de 2014
Resumo:

A Portaria Nº 156, de 28 de Novembro de 2014, aprova o regulamento do Programa de Apoio à Pós-graduação - PROAP, que visa proporcionar melhores condições para a formação de recursos humanos e para a produção e aprofundamento do conhecimento nos cursos de pós-graduação stricto sensu mantidos por instituições públicas brasileiras. Esta portaria substitui a anterior (Portaria nº 64, de 24 de março de 2010).

Objetivos do PROAP:

Apoiar atividades inovadoras dos programas de pós-graduação (PPGs), voltadas para o desenvolvimento acadêmico, visando oferecer formação qualificada e diversificada aos estudantes de pós-graduação e pesquisadores em estágio pós-doutoral.
Utilizar os recursos disponíveis no custeio das atividades científico-acadêmicas relacionadas à titulação de mestres e doutores e ao estágio pós-doutoral.
Apoiar o desenvolvimento dos trabalhos de planejamento e execução da política institucional de pós-graduação.
Requisitos e Atribuições das Instituições Participantes:

Requisitos:

Possuir personalidade jurídica de direito público.
Manter programa de pós-graduação (PPG) stricto sensu recomendado pela CAPES, em funcionamento e que possua cota de bolsa do Programa de Demanda Social (DS).
Manter estrutura administrativa para gerência do PROAP na instituição.
Garantir infraestrutura de ensino e pesquisa para o funcionamento dos PPGs apoiados pelo PROAP.
Atribuições:

Responsabilizar-se pelo cumprimento das obrigações estipuladas nos convênios, termos de execução descentralizada e instrumentos correlatos firmados com a CAPES.
Coordenar a execução, acompanhamento orçamentário e financeiro, e fiscalização do PROAP, por meio da Pró-Reitoria de Pesquisa e Pós-Graduação (PRPPG) ou órgão equivalente de gestão da pós-graduação stricto sensu.
Encaminhar à CAPES os documentos necessários à adesão e implementação do PROAP, conforme modelos disponibilizados na página eletrônica da CAPES e legislação vigente.
Divulgar internamente todos os comunicados enviados pela CAPES.
Solicitar à CAPES, caso necessário, remanejamento de recursos entre os PPGs, de forma a otimizar sua execução plena.
Efetuar, de acordo com a legislação vigente e quando couber, a prestação de contas e apresentar os relatórios de cumprimento de objeto, conforme modelos disponibilizados na página eletrônica da CAPES.
Atribuições da CAPES:

Estabelecer as normas e diretrizes do PROAP.
Definir, divulgar e transferir os recursos orçamentários e financeiros destinados às instituições, com base nos valores de referência correspondentes a cada PPG e à PRPPG ou órgão equivalente.
Acompanhar o desempenho dos PPGs nas instituições apoiadas pelo PROAP, por intermédio das Avaliações Trienais conduzidas pela CAPES.
Normas Operacionais:

Valor de Referência:

O valor de referência para o repasse de recursos financeiros relativos aos PPGs será fixado anualmente em função da disponibilidade orçamentária da CAPES e dos critérios abaixo:
Área do conhecimento.
Nível de formação (mestrado ou doutorado).
Nota dos cursos na avaliação mais recente realizada pela CAPES.
Critérios subsidiários incluem:
Grau de utilização das cotas de bolsas concedidas do Programa de Demanda Social (DS).
Grau de utilização das cotas de bolsas concedidas do Programa Nacional de Pós-Doutorado (PNPD/CAPES).
Grau de utilização dos recursos do PROAP em exercícios anteriores.
Adicional de Recursos:

Será concedido um adicional de recursos à PRPPG ou órgão equivalente, proporcional ao montante de recursos correspondentes aos PPGs de cada instituição, que integrará o Plano de Trabalho do respectivo instrumento de repasse.
Os recursos financeiros do PROAP correspondentes ao PNPD/CAPES deverão ser utilizados exclusivamente para o desenvolvimento das atividades de pesquisa definidas pelos respectivos bolsistas em estágio pós-doutoral, conforme previsto no Plano de Trabalho Institucional aprovado pela CAPES.
Instrumentos de Repasse:

No repasse de recursos serão utilizados um dos seguintes instrumentos, de acordo com a legislação vigente:
Termo de Convênio.
Termo de Execução Descentralizada.
Termo de Solicitação e Concessão de Apoio Financeiro a Projeto Educacional ou de Pesquisa - AUXPE.
Quando utilizado o AUXPE, o mesmo será firmado entre a CAPES e o responsável legal pela PRPPG ou órgão equivalente, com anuência do dirigente máximo da Instituição beneficiada.
Despesas Financiáveis:

Despesas correntes nos elementos e atividades discriminadas conforme objetivos dispostos no Artigo 1º:
Material de consumo.
Serviços de terceiros (pessoa jurídica e pessoa física).
Diárias.
Passagens e despesas com locomoção.
Auxílio financeiro a estudante e a pesquisador.
Atividades custeáveis:
Manutenção de equipamentos.
Manutenção e funcionamento de laboratório de ensino e pesquisa.
Serviços e taxas relacionados à importação.
Participação em cursos e treinamentos em técnicas de laboratório e utilização de equipamentos.
Produção, revisão, tradução, editoração, confecção e publicação de conteúdos científico-acadêmicos e de divulgação das atividades desenvolvidas no âmbito dos PPGs.
Manutenção do acervo de periódicos, desde que não contemplados no Portal de Periódicos da CAPES.
Apoio à realização de eventos científico-acadêmicos no país.
Participação de professores, pesquisadores e alunos em atividades científico-acadêmicas no país e no exterior.
Participação de convidados externos em atividades científico-acadêmicas no país.
Participação de professores, pesquisadores e alunos em atividades de intercâmbio e parcerias entre PPGs e instituições formalmente associadas.
Participação de alunos em cursos ou disciplinas em outro PPG, desde que estejam relacionados às suas dissertações e teses.
Aquisição e manutenção de tecnologias em informática e da informação caracterizadas como custeio, conforme disposto no artigo 6º.
Restrições:

Será vedado pagamento de pró-labore, consultoria, gratificação e remuneração para ministrar cursos, seminários, aulas, apresentar trabalhos e participar de bancas examinadoras.
Não será permitida a contratação de serviços de terceiros para cobrir despesas que caracterizem contratos de longa duração, vínculo empregatício, contratações que não sejam utilizadas nas atividades-fim da pós-graduação ou contratações em desacordo com a legislação vigente.
Será vedado o recebimento concomitante de diárias e auxílio financeiro para o custeio de despesas com hospedagem, alimentação e locomoção urbana.
O valor do auxílio financeiro para o custeio de despesas com hospedagem, alimentação e locomoção urbana não poderá ser superior à quantia equivalente em diárias estabelecido para cargo de nível superior, conforme parâmetros fixados em legislação federal vigente.
Será vedado o custeio de despesas de capital.
Disposições Finais:

Os casos omissos serão analisados pela CAPES.
A portaria entra em vigor na data de sua publicação no Diário Oficial da União.
Anexo:

Tabela de auxílio diário no exterior, com valores em dólares norte-americanos para diferentes países, categorizados em grupos (A, B, C e D).
Trechos Específicos Importantes:

Capítulo I - Disposições Gerais:

Os discentes regularmente matriculados nos programas de pós-graduação stricto sensu da UFAL e os pesquisadores em estágio pós-doutoral (PNPD) poderão receber o auxílio para participação em eventos científico-acadêmicos no país ou no exterior, ou para realização de atividades técnico-científicas no país, que sejam de interesse do programa de pós-graduação e que estejam relacionados ao objeto de estudo do discente ou pesquisador, nos limites impostos por esta Instrução Normativa.
Consideram-se eventos científico-acadêmicos: congressos, encontros, simpósios, seminários, conferências e similares.
Consideram-se atividades técnico-científicas: os trabalhos de campo, visitas técnico-científicas, cursos e treinamentos.
O auxílio financeiro ao estudante de pós-graduação stricto sensu e ao pesquisador em estágio pós-doutoral (PNPD), custeado por recursos do PROAP, destina-se ao pagamento de despesas com hospedagem, alimentação e locomoção urbana.
Capítulo II - Das Condições para Solicitação do Auxílio Financeiro ao Estudante de Pós-Graduação:

O discente que participar de eventos científico-acadêmicos nacionais ou internacionais somente poderá receber o auxílio financeiro caso comprove a condição de apresentador de trabalho científico, palestrante ou debatedor, sendo vedada a concessão do auxílio financeiro para ouvinte.
Em caso de coautoria de trabalho entre discentes, será autorizado auxílio financeiro apenas para o apresentador.
O discente que participar de atividades técnico-científicas no país somente poderá receber o auxílio financeiro mediante a apresentação de documento contendo o período, o local e a descrição detalhada da atividade a ser realizada e a relevância para a sua formação.
A definição do teto orçamentário anual para o custeio das solicitações de auxílio financeiro ao estudante será de responsabilidade dos PPGs.
Caberá ao PPG a análise do mérito para a concessão do auxílio financeiro ao estudante, tendo como parâmetro a natureza e relevância das atividades a serem desenvolvidas pelo discente como instrumento para sua formação acadêmica e capacitação profissional.
Capítulo III - Das Condições para Solicitação do Auxílio Financeiro ao Pesquisador em Estágio Pós-Doutoral (PNPD):

Caberá ao bolsista PNPD a análise do mérito para o recebimento do auxílio financeiro ao pesquisador, tendo como parâmetro a natureza e relevância das atividades relacionadas ao seu objeto de estudo.
O pesquisador em estágio pós-doutoral que participar de atividades técnico-científicas no país somente poderá receber o auxílio financeiro mediante a apresentação de documento contendo o período, o local e a descrição detalhada da atividade a ser realizada e a relevância para o seu objeto de pesquisa.
Capítulo IV - Dos Procedimentos para Solicitação do Auxílio Financeiro:

Os interessados deverão solicitar o auxílio financeiro à Coordenação do PPG a que estiverem vinculados com, no máximo, 15 dias de antecedência.
Após a aprovação da solicitação, a Coordenação do PPG deverá abrir requisição no SIPAC seguindo as orientações composta no manual disponível em https://ufal.br/estudante/pos-graduacao/programa-de-apoio-a-pos-graduacao-proap-capes/auxilio-financeiro-ao-estudante-pesquisador/solicitacoes-de-auxilios-2023, encaminhando a requisição para unidade de destino da PRÓ-REITORIA DE PESQUISA E PÓS-GRADUAÇÃO (11.00.43.03), para aprovação do Pró-reitor, inserindo a documentação exigida para cada um dos tipos de motivos permitidos para a concessão do Auxílio Financeiro ao Estudante.
Não serão atendidas as requisições de auxílio financeiro cadastradas antes da data de abertura do empenho, que será informada aos PPGs pela Pró-reitoria de Pesquisa e Pós-graduação.
As requisições só poderão ser atendidas se todos os documentos anexados estiverem assinados pelo proponente ou o coordenador do programa. As assinaturas constantes nos documentos que compõem a requisição deverão estar de acordo com a Instrução Normativa GR nº 01, de 11 de fevereiro de 2021.
Capítulo V - Dos Procedimentos para Prestação de Contas do Auxílio Financeiro:

Em até 15 dias após o recebimento do auxílio, o beneficiário deverá efetuar a prestação de contas junto ao seu Programa de Pós-graduação, apresentando os seguintes documentos:
Comprovante de sua efetiva participação no evento/atividade (certificado/declaração).
Caso o interessado tenha recebido o auxílio para realização de trabalho de campo, deverá entregar relatório de atividades realizadas, conforme modelo disponível em: https://ufal.br/estudante/pos-graduacao/programa-de-apoio-a-pos-graduacao-proap-capes/auxilio-financeiro-ao-estudante-pesquisador.
Após a entrega dos documentos de prestação de contas, a Coordenação do PPG deverá apreciar, indicando o deferimento ou indeferimento da Prestação de Contas e realizar a Prestação de Contas no SIPAC seguindo as orientações composta no manual disponível em https://ufal.br/estudante/pos-graduacao/programa-de-apoio-a-pos-graduacao-proap-capes/auxilio-financeiro-ao-estudante-pesquisador/solicitacoes-de-auxilios-2023.
O beneficiário que não encaminhar a prestação de contas dentro do prazo estabelecido nesta Instrução Normativa ficará impedido de receber novo auxílio financeiro enquanto não sanada a pendência e estará sujeito à devolução dos recursos recebidos.
Capítulo VI - Das Disposições Finais:

Esta Instrução Normativa entra em vigor na data de sua publicação.
Os casos omissos desta Instrução Normativa serão analisados pela Pró-Reitoria de Pesquisa e Pós-Graduação – PROPEP.
Anexo I - Tabela de Auxílio Diário no Exterior:

Grupo A (180 USD): Afeganistão, Armênia, Bangladesh, Belarus, Benin, Bolívia, Burkina-Fasso, Butão, Chile, Comores, República Popular Democrática da Coréia, Costa Rica, El Salvador, Equador, Eslovênia, Filipinas, Gâmbia, Guiana, Guiné Bissau, Guiné, Honduras, Indonésia, Irã, Iraque, Laos, Líbano, Malásia, Maldivas, Marrocos, Mongólia, Myanmar, Namíbia, Nauru, Nepal, Nicarágua, Panamá, Paraguai, República Centro-Africana, República Togolesa, Salomão, Samoa, Serra Leoa, Síria, Somália, Sri Lanka, Suriname, Tadjiquistão, Tailândia, Timor Leste, Tonga, Tunísia, Turcomenistão, Turquia, Tuvalu, Vietnã, Zimbábue.
Grupo B (260 USD): África do Sul, Albânia, Andorra, Argélia, Argentina, Austrália, Belize, Bósnia-Herzegóvina, Burundi, Cabo Verde, Camarões, Camboja, Catar, Chade, China, Chipre, Colômbia, Dominica, Egito, Eritréia, Estônia, Etiópia, Gana, Geórgia, Guiné- Equatorial, Haiti, Hungria, Iêmen, Ilhas Marshall, Índia, Kiribati, Lesoto, Líbia, Macedônia, Madagascar, Malauí, Micronésia, Moçambique, Moldávia, Níger, Nigéria, Nova Zelândia, Palau, Papua Nova Guiné, Paquistão, Peru, Polônia, Quênia, República Dominicana, República Eslovaca, Romênia, Ruanda, São Tomé e Príncipe, Senegal, Sudão, Tanzânia, Uruguai, Uzbequistão, Venezuela.
Grupo C (310 USD): Antígua e Barbuda, Arábia Saudita, Azerbaijão, Bahamas, Barein, Botsuana, Brunei Darussalam, Bulgária, Canadá, Cingapura, Congo, Costa do Marfim, Cuba, Djibuti, Emirados Árabes, Fiji, Gabão, Guatemala, Jamaica, Jordânia, Letônia, Libéria, Lituânia, Mali, Malta, Maurício, Mauritânia, México, República Democrática do Congo, República Tcheca, Rússia, San Marino, Santa Lúcia, São Cristovão e Névis, São Vicente e Granadinas, Taiwan, Trinidad e Tobago, Ucrânia, Uganda, Zâmbia.
Grupo D (370 USD): Alemanha, Angola, Áustria, Barbados, Bélgica, Cazaquistão, Coréia do Sul, Croácia, Dinamarca, Espanha, Estados Unidos da América, Finlândia, França, Granada, Grécia, Hong Kong, Irlanda, Islândia, Israel, Itália, Japão, Kuaite, Liechtenstein, Luxemburgo, Mônaco, Montenegro, Noruega, Omã, Países Baixos, Portugal, Reino Unido, República Quirguiz, Seicheles, Sérvia, Suazilândia, Suécia, Suíça, Vanuatu.
'''


st.set_page_config(page_icon="💬", layout="wide",
                   page_title="Mestrado Frederico - PROAP Dúvidas")


st.subheader("Tire suas Dúvidas sobre Portaria PROAP \nAutor: Daniel Gomes de Mello Farias", divider="rainbow", anchor=False)

# Sidebar com botão para limpar a janela de chat.
with st.sidebar:
    if st.button("Limpar Chat", use_container_width=True, type="primary"):
        st.session_state.messages = []
        st.rerun()


client = Groq(
    api_key=st.secrets["GROQ_API_KEY"],
)

# Initialize chat history and selected model
if "messages" not in st.session_state:
    st.session_state.messages = []

if "selected_model" not in st.session_state:
    st.session_state.selected_model = None




model_option = "llama3-70b-8192"

# Detect model change and clear chat history if model has changed
if st.session_state.selected_model != model_option:
    st.session_state.messages = []
    st.session_state.selected_model = model_option


max_tokens = 8192

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    avatar = '🤖' if message["role"] == "assistant" else '👨‍💻'
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])


def generate_chat_responses(chat_completion) -> Generator[str, None, None]:
    """Yield chat response content from the Groq API response."""
    for chunk in chat_completion:
        if chunk.choices[0].delta.content:
            yield chunk.choices[0].delta.content


if prompt := st.chat_input("Digite sua pergunta - Estamos aqui pra tirar suas dúvidas..."):
    st.session_state.messages.append({"role": "user", "content": prompt})    

    with st.chat_message("user", avatar='👨‍💻'):
        st.markdown(prompt)

    # Adicione o texto de referência como contexto no prompt
    messages = [
        {"role": "system", "content": f"Você é um assistente virtual especializado em responder perguntas com base no seguinte texto: {reference_text}. Seu objetivo é fornecer explicações claras e concisas, citando a localização exata (documento, parágrafo, etc.) onde a informação foi encontrada no texto. Responda apenas com base no texto fornecido. Responda sempre com no máximo 1 parágrafo"},
        *[
            {"role": m["role"], "content": m["content"]}
            for m in st.session_state.messages
        ]
    ]

    # Fetch response from Groq API
    try:
        chat_completion = client.chat.completions.create(
            model=model_option,
            messages=messages,
            max_tokens=max_tokens,
            stream=True
        )

        # Use the generator function with st.write_stream
        with st.chat_message("assistant", avatar="🤖"):
            chat_responses_generator = generate_chat_responses(chat_completion)
            full_response = st.write_stream(chat_responses_generator)
    except Exception as e:
        st.error(e, icon="🚨")

    # Append the full response to session_state.messages
    if isinstance(full_response, str):
        st.session_state.messages.append(
            {"role": "assistant", "content": full_response})
    else:
        # Handle the case where full_response is not a string
        combined_response = "\n".join(str(item) for item in full_response)
        st.session_state.messages.append(
            {"role": "assistant", "content": combined_response})