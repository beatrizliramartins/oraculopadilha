Oráculo de Maria Padilha

Visão Geral

Este projeto implementa um chatbot chamado "Oráculo de Maria Padilha" utilizando Streamlit. O bot pode interagir com os usuários, processar arquivos de diferentes formatos e utilizar modelos de IA para fornecer respostas com base em um documento carregado. O projeto usa a biblioteca LangChain para gerenciar memória e inferência dos modelos.

Dependências

O projeto requer as seguintes bibliotecas:

streamlit - Interface de usuário

tempfile - Manipulação de arquivos temporários

langchain - Memória da conversa e processamento de modelos

langchain_groq - Uso do modelo da Groq

langchain_openai - Uso do modelo da OpenAI

loads - Funções auxiliares para carregar arquivos (deve ser um módulo pré-existente no projeto)


Como Usar

Inicie o aplicativo executando streamlit run nome_do_arquivo.py.

Utilize a barra lateral para carregar um arquivo ou escolher um modelo.

Interaja com o chatbot na interface principal digitando mensagens.

Para resetar a conversa, clique no botão "Apagar Histórico de Conversa".



Conclusão

Este projeto fornece um chatbot personalizável baseado em documentos, utilizando modelos de IA para fornecer respostas contextuais. Ele pode ser expandido para suportar novos provedores, novos formatos de documentos e mais funcionalidades interativas.

