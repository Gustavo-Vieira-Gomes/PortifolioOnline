import streamlit as st

# Título e cabeçalho
st.title("Currículo Online - Desenvolvedor Python e Analista de Dados")
st.header("Seu Nome")

# Informações de Contato
st.subheader("Informações de Contato")
st.write("""
- **Email:** seuemail@example.com
- **Telefone:** (00) 00000-0000
- **LinkedIn:** [linkedin.com/in/seu-perfil](https://linkedin.com/in/seu-perfil)
- **GitHub:** [github.com/seu-usuario](https://github.com/seu-usuario)
""")

# Perfil Profissional
st.subheader("Perfil Profissional")
st.write("""
Sou um Desenvolvedor Python e Analista de Dados com experiência em desenvolvimento de soluções robustas e eficientes. Possuo habilidades avançadas em análise de dados, visualização de dados e desenvolvimento de software. Estou sempre em busca de novos desafios e oportunidades para aplicar minhas habilidades e contribuir para o sucesso das organizações.
""")

# Habilidades
st.subheader("Habilidades")
st.write("""
- **Linguagens de Programação:** Python, SQL, R
- **Ferramentas de Análise de Dados:** Pandas, NumPy, Matplotlib, Seaborn
- **Machine Learning:** Scikit-Learn, TensorFlow, Keras
- **Bancos de Dados:** MySQL, PostgreSQL, SQLite
- **Desenvolvimento Web:** Flask, Django, Streamlit
- **Controle de Versão:** Git, GitHub
- **Outras Ferramentas:** Excel, Power BI, Tableau
""")

# Experiência de Trabalho
st.subheader("Experiência de Trabalho")
st.write("""
**Desenvolvedor Python e Analista de Dados Freelancer**  
*Jan 2020 - Presente*  
- Desenvolvimento de scripts e aplicações em Python para análise de dados.
- Criação de dashboards interativos e relatórios utilizando ferramentas de visualização de dados.
- Colaboração com clientes para entender suas necessidades e fornecer soluções personalizadas.

**Analista de Dados na Empresa XYZ**  
*Jun 2018 - Dez 2019*  
- Realização de análise de dados para identificar tendências e insights.
- Desenvolvimento de modelos de machine learning para previsões e classificação.
- Apresentação de resultados e recomendações para a equipe de gerenciamento.
""")

# Educação
st.subheader("Educação")
st.write("""
**Bacharel em Ciência da Computação**  
*Universidade ABC, 2014 - 2018*

**Certificação em Análise de Dados**  
*Curso Online, 2019*
""")

# Projetos
st.subheader("Projetos")
st.write("""
**Análise de Vendas**  
- Desenvolvimento de um dashboard interativo para análise de vendas utilizando Streamlit e Pandas.
- [Repositório no GitHub](https://github.com/seu-usuario/analise-vendas)

**Modelo de Previsão de Preços Imobiliários**  
- Criação de um modelo de machine learning para prever preços de imóveis utilizando Scikit-Learn.
- [Repositório no GitHub](https://github.com/seu-usuario/previsao-precos-imoveis)

**Aplicativo Web de Visualização de Dados**  
- Desenvolvimento de um aplicativo web para visualização de dados utilizando Flask e D3.js.
- [Repositório no GitHub](https://github.com/seu-usuario/app-visualizacao-dados)
""")

# Rodapé
st.write("""
Para mais informações, entre em contato pelo email seuemail@example.com ou visite meu perfil no LinkedIn.
""")
