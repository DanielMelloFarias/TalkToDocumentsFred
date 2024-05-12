import streamlit as st
from typing import Generator
from groq import Groq

reference_text = "DOCUMENTO - DIÁRIO OFICIAL DA UNIAO:COORDENAÇÃO DE APERFEIÇOAMENTODE PESSOAL DE NÍVEL SUPERIORPORTARIA Nº 156, DE 28 DE NOVEMBRO DE 2014Aprova o regulamento do Programa deApoio à Pós-graduação - PROAP, que sedestina a proporcionar melhores condiçõespara a formação de recursos humanos e para a produção e o aprofundamento do conhecimento nos cursos de pós-graduaçãostricto sensu, mantidos por instituições pú-blicas brasileiras.O PRESIDENTE DA COORDENAÇÃO DE APERFEI-ÇOAMENTO DE PESSOAL DE NÍVEL SUPERIOR - CAPES, nouso das atribuições que lhe confere o art. 26, Inciso III do Anexo I doDecreto nº 7.692, de 02 de março de 2012, e considerando a necessidade de reformular a regulamentação do Programa de Apoio àPós-graduação - PROAP, resolve:Art. 1º Fica aprovado, na forma do anexo, o novo regulamento do Programa de Apoio à Pós-graduação - PROAP.Art. 2º Esta Portaria entra em vigor na data de sua publicação no DOU.Art. 3º Fica revogada a Portaria nº 64, de 24 de março de 2010.JORGE ALMEIDA GUIMARÃESANEXOREGULAMENTO DOPROGRAMA DE APOIO À PÓS-GRADUAÇÃO - PROAPCapítulo IOBJETIVO DO PROGRAMA E CRITÉRIOS PARA A APLICA-ÇÃO DOS RECURSOSArt. 1º O Programa de Apoio à Pós-Graduação - PROAP destina-se aproporcionar melhores condições para a formação de recursos humanos e para a produção e o aprofundamento do conhecimento noscursos de pós-graduação stricto sensu mantidos por instituições pú-blicas, envolvendo:I - apoio às atividades inovadoras dos programas de pós-graduação(PPGs), voltadas para o seu desenvolvimento acadêmico, visandooferecer formação cada vez mais qualificada e diversificada aos estudantes de pós-graduação e pesquisadores em estágio pós-doutoral;II - utilização dos recursos disponíveis no custeio das atividadescientífico- acadêmicas relacionadas à titulação de mestres e doutorese ao estágio pós-doutoral;III - o apoio ao desenvolvimento dos trabalhos de planejamento e deexecução da política institucional de pós-graduação.Capítulo IIREQUISITOS E ATRIBUIÇÕES DAS INSTITUIÇÕESArt. 2º A instituição participante do PROAP deverá:I - possuir personalidade jurídica de direito público;II - manter programa de pós-graduação (PPG) stricto sensu recomendado pela CAPES, em funcionamento e que possua cota de bolsado Programa de Demanda Social- DS;III - manter estrutura administrativa para gerência do PROAP nainstituição;IV - garantir infra-estrutura de ensino e pesquisa para o funcionamento dos PPGs apoiados pelo PROAP;V - responsabilizar-se pelo cumprimento das obrigações estipuladasnos convênios, termos de execução descentralizada e instrumentoscorrelatos firmados com a CAPES;VI - coordenar a execução, o acompanhamento orçamentário e financeiro e a fiscalização do PROAP, por meio da Pró-Reitoria dePesquisa e Pós-Graduação (PRPPG), ou órgão equivalente de gestãoda pós-graduação stricto sensu, que se responsabilizará pela interlocução com a CAPES;VII - encaminhar à CAPES os documentos necessários à adesão eimplementação do PROAP, conforme modelos disponibilizados napágina eletrônica da CAPES e legislação vigente;VIII - divulgar internamente todos os comunicados enviados pelaCAPES;IX - solicitar à CAPES, caso necessário, remanejamento de recursosentre os PPGs, de forma a otimizar sua execução plena;X - efetuar, de acordo com a legislação vigente e quando couber, aprestação de contas e apresentar os relatórios de cumprimento deobjeto, conforme modelos disponibilizados na página eletrônica daCAPES.Capítulo IIIATRIBUIÇÕES DA CAPESArt. 3 º São atribuições da CAPES:I - estabelecer as normas e diretrizes do PROAP;II - definir, divulgar e transferir os recursos orçamentários e financeiros destinados às instituições, com base nos valores de referênciacorrespondentes à cada PPG e à PRPPG ou órgão equivalente;III - acompanhar o desempenho dos PPGs nas instituições apoiadaspelo PROAP, por intermédio das Avaliações Trienais conduzidas pelaCAPES.Capítulo IVNORMAS OPERACIONAISArt. 4º O valor de referência para o repasse de recursos financeirosrelativos aos PPGs será fixado anualmente em função da disponibilidade orçamentária da CAPES e dos critérios abaixo:I - critérios principais:a) área do conhecimento;b) nível de formação (mestrado ou doutorado); ec) nota dos cursos na avaliação mais recente realizada pela CAPES.II - critérios subsidiários:a) grau de utilização das cotas de bolsas concedidas do Programa deDemanda Social (DS);b) grau de utilização das cotas de bolsas concedidas do ProgramaNacional de Pós-Doutorado (PNPD/CAPES); ec) grau de utilização dos recursos do PROAP em exercícios anteriores.§ 1º Será concedido um adicional de recursos à PRPPG ou órgãoequivalente, proporcional ao montante de recursos correspondentesaos PPGs de cada instituição, que integrará o Plano de Trabalho dorespectivo instrumento de repasse.§ 2º Os recursos financeiros do PROAP correspondentes aoPNPD/CAPES deverão ser utilizados exclusivamente para o desenvolvimento das atividades de pesquisa definidas pelos respectivosbolsistas em estágio pós-doutoral, conforme previsto no Plano deTrabalho Institucional aprovado pela CAPES.Art. 5º No repasse de recursos serão utilizados um dos seguintesinstrumentos, de acordo com respectiva legislação vigente:I - Termo de Convênio;II - Termo de Execução Descentralizada; ouIII - Termo de Solicitação e Concessão de Apoio Financeiro a ProjetoEducacional ou de Pesquisa - AUXPE, instrumento específico regulamentado pela CAPES§ 1º Quando utilizado o AUXPE, o mesmo será firmado entre aCAPES e o responsável legal pela Pró-Reitoria de Pesquisa e PósGraduação ou órgão equivalente, com anuência do dirigente máximoda Instituição beneficiada.§ 2º No caso de utilização do AUXPE, o responsável pelo recebimento do recurso submeter-se-á às normas correlatas deste instrumento.Art. 6º Deverá ser verificado junto às unidades responsáveis pelaexecução financeira e contábil da instituição o enquadramento doselementos de despesa nas atividades financiáveis descritas no art. 7º,bem como os procedimentos e a documentação comprobatória dasdespesas pagas na forma deste regulamento, observadas as disposições da Lei de Diretrizes Orçamentárias (LDO), do Manual deContabilidade Aplicada ao Setor Público (MCASP) e do ManualTécnico de Orçamento (MTO) vigentes no respectivo exercício, asnormas vinculantes e as alterações posteriores emitidas pela Secretaria do Tesouro Nacional (STN) e pela Secretaria de OrçamentoFederal (SOF).Art. 7º Poderão ser custeadas despesas correntes nos elementos eatividades abaixo, discriminados conforme objetivos dispostos no Artigo 1º:I - Elementos de despesa permitidos:a) material de consumo;b) serviços de terceiros (pessoa jurídica);c) serviços de terceiros (pessoa física);d) diárias;e) passagens e despesas com locomoção;f) auxílio financeiro a estudante; eg) auxílio financeiro a pesquisador.II - Atividades a serem custeadas:a) manutenção de equipamentos;b) manutenção e funcionamento de laboratório de ensino e pesquisa;c) serviços e taxas relacionados à importação;d) participação em cursos e treinamentos em técnicas de laboratório eutilização de equipamentos;e) produção, revisão, tradução, editoração, confecção e publicação deconteúdos científico-acadêmicos e de divulgação das atividades desenvolvidas no âmbito dos PPGs;f) manutenção do acervo de periódicos, desde que não contempladosno Portal de Periódicos da CAPES;g) apoio à realização de eventos científico-acadêmicos no país;h) participação de professores, pesquisadores e alunos em atividadese científico-acadêmicos no país e no exterior;i) participação de convidados externos em atividades científico-acadêmicas no país;j) participação de professores, pesquisadores e alunos em atividadesde intercambio e parcerias entre PPGs e instituições formalmenteassociados;k) participação de alunos em cursos ou disciplinas em outro PPG,desde que estejam relacionados às suas dissertações e teses; el) aquisição e manutenção de tecnologias em informática e da informação caracterizadas como custeio, conforme disposto no artigo6º.§ 1º As atividades descritas nas alíneas 'h', 'j' e 'k' do inciso II deste artigo referem-se exclusivamente aos professores vinculados aosPPGs, alunos matriculados nos PPGs e pesquisadores em estágio pósdoutoral.§ 2º A análise de mérito e de priorização das despesas caberá aosPPGs e respeitará os procedimentos administrativos de cada instituição, conforme Plano de Trabalho Institucional aprovado pela CAPES, bem como as atribuições fixadas no inciso VI do art. 2º. Nocaso das despesas relativas aos bolsistas PNPD, a análise de mérito ede priorização caberá aos bolsistas, conforme disposto no art. 4º, §2º.§ 3º Poderão ser utilizados outros elementos de despesa além dosprevistos no inciso I deste artigo, desde que guardem consonânciacom os objetivos dispostos no artigo 1º, sejam vinculados às atividades-fim da pós-graduação e estejam detalhados no plano de trabalho ou na previsão orçamentária com a devida aprovação da CAPES.Art. 8º Será vedado pagamento de pró-labore, consultoria, gratificação e remuneração para ministrar cursos, seminários, aulas, apresentar trabalhos e participar de bancas examinadoras;Art. 9º Não será permitida a contratação de serviços de terceiros paracobrir despesas que caracterizem contratos de longa duração, vínculoempregatício, contratações que não sejam utilizadas nas atividadesfim da pós-graduação ou contratações em desacordo com a legislaçãovigente;Art. 10 Será vedado o recebimento concomitante de diárias e auxíliofinanceiro para o custeio de despesas com hospedagem, alimentação elocomoção urbana.Art. 11 O valor do auxílio financeiro para o custeio de despesas comhospedagem, alimentação e locomoção urbana não poderá ser superior à quantia equivalente em diárias estabelecido para cargo denível superior, conforme parâmetros fixados em legislação federalvigente.Art. 12 Será vedado o custeio de despesas de capital.Capítulo VIDISPOSIÇÕES FINAISArt. 13 Os casos omissos serão analisados pela CAPESDOCUMENTO - Portaria nº 156, de 28 de Novembro de 2014OrigemGAB/CAPESFinalidade do atoAto normativoEmentaAprova o novo regulamento do Programa de Apoio à Pós-graduação - PROAP.SituaçãoVigenteFonteDOU - Seção 1 - 03/12/2014, pág. 11Revoga a(s) norma(s)/ato(s)Portaria nº 64, de 25 de Janeiro de 2010Aprova o regulamento do Programa deApoio à Pós-graduação - PROAP, que sedestina a proporcionar melhorescondições para a formação de recursoshumanos e para a produção e oaprofundamento do conhecimento noscursos de pós-graduação stricto sensu,mantidos por instituições públicasbrasileiras.O PRESIDENTE DA COORDENAÇÃO DE APERFEIÇOAMENTO DE PESSOAL DE NÍVEL SUPERIOR - CAPES, no usodas atribuições que lhe confere o art. 26, Inciso III do Anexo I do Decreto nº 7.692, de 02 de março de 2012, e considerando anecessidade de reformular a regulamentação do Programa de Apoio à Pós-graduação - PROAP, resolve:Art. 1º Fica aprovado, na forma do anexo, o novo regulamento do Programa de Apoio à Pós-graduação - PROAP.Art. 2º Esta Portaria entra em vigor na data de sua publicação no DOU.Art. 3º Fica revogada a Portaria nº 64, de 24 de março de 2010.JORGE ALMEIDA GUIMARÃESANEXOREGULAMENTO DO PROGRAMA DE APOIO À PÓS-GRADUAÇÃO - PROAPCapítulo IOBJETIVO DO PROGRAMA E CRITÉRIOS PARA A APLICAÇÃO DOS RECURSOSArt. 1º O Programa de Apoio à Pós-Graduação - PROAP destina-se a proporcionar melhores condições para a formação derecursos humanos e para a produção e o aprofundamento do conhecimento nos cursos de pós-graduação stricto sensu mantidospor instituições públicas, envolvendo:I - apoio às atividades inovadoras dos programas de pós-graduação (PPGs), voltadas para o seu desenvolvimentoacadêmico, visando oferecer formação cada vez mais qualificada e diversificada aos estudantes de pós-graduação epesquisadores em estágio pós-doutoral;II - utilização dos recursos disponíveis no custeio das atividades científico- acadêmicas relacionadas à titulação de mestres edoutores e ao estágio pós-doutoral;III - o apoio ao desenvolvimento dos trabalhos de planejamento e de execução da política institucional de pós-graduação.Capítulo IIREQUISITOS E ATRIBUIÇÕES DAS INSTITUIÇÕESArt. 2º A instituição participante do PROAP deverá:I - possuir personalidade jurídica de direito público;II - manter programa de pós-graduação (PPG) stricto sensu recomendado pela CAPES, em funcionamento e que possuacota de bolsa do Programa de Demanda Social- DS;III - manter estrutura administrativa para gerência do PROAP na instituição:IV - garantir infra-estrutura de ensino e pesquisa para o funcionamento dos PPGs apoiados pelo PROAP;V - responsabilizar-se pelo cumprimento das obrigações estipuladas nos convênios, termos de execução descentralizada einstrumentos correlatos firmados com a CAPES;VI - coordenar a execução, o acompanhamento orçamentário e financeiro e a fiscalização do PROAP, por meio da Pró-Reitoria de Pesquisa e Pós-Graduação (PRPPG), ou órgão equivalente de gestão da pós-graduação stricto sensu, que seresponsabilizará pela interlocução com a CAPES;VII - encaminhar à CAPES os documentos necessários à adesão e implementação do PROAP, conforme modelosdisponibilizados na página eletrônica da CAPES e legislação vigente;VIII - divulgar internamente todos os comunicados enviados pela CAPES;IX - solicitar à CAPES, caso necessário, remanejamento de recursos entre os PPGs, de forma a otimizar sua execuçãoplena;X - efetuar, de acordo com a legislação vigente e quando couber, a prestação de contas e apresentar os relatórios decumprimento de objeto, conforme modelos disponibilizados na página eletrônica da CAPES.Capítulo IIIATRIBUIÇÕES DA CAPESArt. 3 º São atribuições da CAPES:I - estabelecer as normas e diretrizes do PROAP;II - definir, divulgar e transferir os recursos orçamentários e financeiros destinados às instituições, com base nos valores dereferência correspondentes à cada PPG e à PRPPG ou órgão equivalente;III - acompanhar o desempenho dos PPGs nas instituições apoiadas pelo PROAP, por intermédio das Avaliações Trienaisconduzidas pela CAPES.Capítulo IVNORMAS OPERACIONAISArt. 4º O valor de referência para o repasse de recursos financeiros relativos aos PPGs será fixado anualmente em funçãoda disponibilidade orçamentária da CAPES e dos critérios abaixo:I - critérios principais:a) área do conhecimento;b) nível de formação (mestrado ou doutorado); ec) nota dos cursos na avaliação mais recente realizada pela CAPES.II - critérios subsidiários:a) grau de utilização das cotas de bolsas concedidas do Programa de Demanda Social (DS);b) grau de utilização das cotas de bolsas concedidas do Programa Nacional de Pós-Doutorado (PNPD/CAPES); ec) grau de utilização dos recursos do PROAP em exercícios anteriores.§ 1º Será concedido um adicional de recursos à PRPPG ou órgão equivalente, proporcional ao montante de recursoscorrespondentes aos PPGs de cada instituição, que integrará o Plano de Trabalho do respectivo instrumento de repasse.§ 2º Os recursos financeiros do PROAP correspondentes ao PNPD/CAPES deverão ser utilizados exclusivamente para odesenvolvimento das atividades de pesquisa definidas pelos respectivos bolsistas em estágio pós-doutoral, conforme previsto noPlano de Trabalho Institucional aprovado pela CAPES.Art. 5º No repasse de recursos serão utilizados um dos seguintes instrumentos, de acordo com respectiva legislaçãovigente:I - Termo de Convênio;II - Termo de Execução Descentralizada; ouIII - Termo de Solicitação e Concessão de Apoio Financeiro a Projeto Educacional ou de Pesquisa - AUXPE, instrumentoespecífico regulamentado pela CAPES.§ 1º Quando utilizado o AUXPE, o mesmo será firmado entre a CAPES e o responsável legal pela Pró-Reitoria de Pesquisae PósGraduação ou órgão equivalente, com anuência do dirigente máximo da Instituição beneficiada.§ 2º No caso de utilização do AUXPE, o responsável pelo recebimento do recurso submeter-se-á às normas correlatas desteinstrumento.Art. 6º Deverá ser verificado junto às unidades responsáveis pela execução financeira e contábil da instituição oenquadramento dos elementos de despesa nas atividades financiáveis descritas no art. 7º, bem como os procedimentos e adocumentação comprobatória das despesas pagas na forma deste regulamento, observadas as disposições da Lei de DiretrizesOrçamentárias (LDO), do Manual de Contabilidade Aplicada ao Setor Público (MCASP) e do Manual Técnico de Orçamento (MTO)vigentes no respectivo exercício, as normas vinculantes e as alterações posteriores emitidas pela Secretaria do Tesouro Nacional(STN) e pela Secretaria de Orçamento Federal (SOF).Art. 7º Poderão ser custeadas despesas correntes nos elementos e atividades abaixo, discriminados conforme objetivosdispostos no Artigo 1º:I - Elementos de despesa permitidos:a) material de consumo;b) serviços de terceiros (pessoa jurídica);c) serviços de terceiros (pessoa física);d) diárias;e) passagens e despesas com locomoção;f) auxílio financeiro a estudante; eg) auxílio financeiro a pesquisador.II - Atividades a serem custeadas:a) manutenção de equipamentos;b) manutenção e funcionamento de laboratório de ensino e pesquisa;c) serviços e taxas relacionados à importação;d) participação em cursos e treinamentos em técnicas de laboratório e utilização de equipamentos;e) produção, revisão, tradução, editoração, confecção e publicação de conteúdos científico-acadêmicos e de divulgação dasatividades desenvolvidas no âmbito dos PPGs;f) manutenção do acervo de periódicos, desde que não contemplados no Portal de Periódicos da CAPES;g) apoio à realização de eventos científico-acadêmicos no país;h) participação de professores, pesquisadores e alunos em atividades e científico-acadêmicos no país e no exterior;i) participação de convidados externos em atividades científico-acadêmicas no país;j) participação de professores, pesquisadores e alunos em atividades de intercambio e parcerias entre PPGs e instituiçõesformalmente associados;k) participação de alunos em cursos ou disciplinas em outro PPG, desde que estejam relacionados às suas dissertações eteses; el) aquisição e manutenção de tecnologias em informática e da informação caracterizadas como custeio, conforme dispostono artigo 6º.§ 1º As atividades descritas nas alíneas 'h', 'j' e 'k' do inciso II deste artigo referem-se exclusivamente aos professoresvinculados aos PPGs, alunos matriculados nos PPGs e pesquisadores em estágio pósdoutoral.§ 2º A análise de mérito e de priorização das despesas caberá aos PPGs e respeitará os procedimentos administrativos decada instituição, conforme Plano de Trabalho Institucional aprovado pela CAPES, bem como as atribuições fixadas no inciso VI doart. 2º. No caso das despesas relativas aos bolsistas PNPD, a análise de mérito e de priorização caberá aos bolsistas, conformedisposto no art. 4º, § 2º.§ 3º Poderão ser utilizados outros elementos de despesa além dos previstos no inciso I deste artigo, desde que guardemconsonância com os objetivos dispostos no artigo 1º, sejam vinculados às atividades-fim da pós-graduação e estejam detalhadosno plano de trabalho ou na previsão orçamentária com a devida aprovação da CAPES.Art. 8º Será vedado pagamento de pró-labore, consultoria, gratificação e remuneração para ministrar cursos, seminários,aulas, apresentar trabalhos e participar de bancas examinadoras;Art. 9º Não será permitida a contratação de serviços de terceiros para cobrir despesas que caracterizem contratos de longaduração, vínculo empregatício, contratações que não sejam utilizadas nas atividadesfim da pós-graduação ou contratações emdesacordo com a legislação vigente;Art. 10 Será vedado o recebimento concomitante de diárias e auxílio financeiro para o custeio de despesas comhospedagem, alimentação e locomoção urbana.Art. 11 O valor do auxílio financeiro para o custeio de despesas com hospedagem, alimentação e locomoção urbana nãopoderá ser superior à quantia equivalente em diárias estabelecido para cargo de nível superior, conforme parâmetros fixados em legislação federal vigente. Art. 12 Será vedado o custeio de despesas de capital."
st.set_page_config(page_icon="💬", layout="wide",
                   page_title="Mestrado Frederico - PROAP Dúvidas")


st.subheader("Tire suas Dúvidas sobre Portaria PROAP \nAutor: Frederico Joaquim Gomes de Mello", divider="rainbow", anchor=False)

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

    # Fetch response from Groq API
    try:
        chat_completion = client.chat.completions.create(
            model=model_option,
            messages=[
                {"role": "system", "content": f"Você é um especialista que responde apenas com base no seguinte texto: {reference_text}. Seu objetivo é explicar o que vc encontra no texto e citar em qual documento achou a informação, parágro e etc.. Seja claro nas respostas pois vc deve tirar dúvidas"},
                {
                    "role": m["role"],
                    "content": m["content"]
                }
                for m in st.session_state.messages
            ],
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