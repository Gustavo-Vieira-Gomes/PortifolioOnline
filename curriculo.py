import streamlit as st

st.set_page_config(page_title='Portifólio - Gustavo Vieira', layout='wide', initial_sidebar_state='collapsed')

with st.container(border=True):
    col1, col2, col3 = st.columns([0.15, 0.425, 0.425])
    col1.image('imagens/retrato_modelo.jpg', use_column_width=True)
    col2.subheader('Gustavo Vieira Gomes')
    col2.write(' - ***Idade:*** 19 Anos')
    col2.write(' - ***Local de Residência:*** São Paulo')
    col2.write(' - ***Analista de Dados/ Desenvolvedor Python Freelancer***')
    col3.subheader('Informações de Contato:')
    col3.write('- ***Email:*** g.vieiraa.gomes@gmail.com')
    col3.write('- ***Celular:*** +55  011 947747178 ')
    col3.write('- ***Github:*** https://github.com/Gustavo-Vieira-Gomes')
    col3.write('- ***Instagram Didático: https://www.instagram.com/pyhelpbr***')


col1, col2 = st.columns(2)
with col1.container(border=True):
    st.subheader('Perfil Profissional:')
    st.write('''Sou um Desenvolvedor Python apaixonado por programação e especialista no desenvolvimento de soluções robustas e eficientes. Possuo habilidades avançadas em visualização de dados através da criação de Dashboards e desenvolvimento de automações. Sou movido por novos desafios e estou sempre em busca de oportunidades de aplicar minhas habilidades para contribuir para o sucesso das organizações, pois me sinto realizado ao ver meus códigos fazendo a diferença na vida das pessoas.
    ''')
    
with col2.container(border=True):
    st.subheader("Habilidades")
    st.write("""
    - **Linguagens de Programação:** Python, SQL
    - **Ferramentas de Análise de Dados:** Pandas, NumPy, Matplotlib, Seaborn
    - **Bancos de Dados:** MySQL, PostgreSQL, SQLite
    - **Desenvolvimento Web:** Dash, Streamlit
    - **Controle de Versão:** Git, GitHub
    - **Outras Ferramentas:** Excel,
    """)

with col1.container(border=True):
    st.subheader('Educação:')
    st.write('''- **Ensino Médio Completo:** *Colégio Naval, 2021 a 2023*''')
    st.markdown('''- **Ensino Superior:** *Ciências Navais - Escola Naval, 2024-presente.
                Aspirante a oficial da Marinha do Brasil*''')
    st.write('- **Cursos:** *Asimov Academy, 2022-presente*')

with col2.container(border=True):
    st.subheader('Distinções:')
    st.write('- Bolsa integral para cursar o ensino médio no Colégio Mackenzie (SP) e Colégio Objetivo - Unidade Vergueiro (SP)')
    st.write('- Aprovado e classificado na Escola de Especialistas da Aeronáutica (EEAr) especialidade de controlador de voo aos 15 anos em 2020')
    st.write('- Aprovado e classificado na Escola Preparatória de Cadetes do Ar (EPCAr) em 2020')
    st.write('- Aprovado e Classificado em 8º Lugar do Brasil no Concurso do Colégio Naval em 2020')
    st.write('- Empossado oficial-aluno comandante de pelotão no Colégio Naval como decorrência de bom desempenho acadêmico, físico e moral (entre a 7º e 18º colocação do Corpo de Alunos)')
    st.write('- Diversas posições de liderança ocupadas: Comandante de Pelotão, Encarregado de Equipe, Instrutor no período de Adaptação dos calouros e responsável pela turma do primeiro ano durante 2023.')

with col1.container(border=True):
    st.subheader('Portifólio:')
    st.write('**Obtenha mais informações de alguns dos meus projetos nas páginas presentes na aba lateral desta aplicação. (Abrir sidebar no canto superior esquerdo)**')
    st.subheader('Diplomas:')
    st.write('**Acesse os diplomas dos cursos concluídos na escola de programação Asimov Academy no link abaixo**')
    st.write('**https://drive.google.com/drive/folders/1mpSJNjLfYNwcqq34K3P1EH23WuFuHnLd?usp=drive_link**')