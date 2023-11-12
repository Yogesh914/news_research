import os
import gradio as gr
import langchain
from langchain.llms import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.chains.qa_with_sources.loading import load_qa_with_sources_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from dotenv import load_dotenv


load_dotenv() # take .env variables
llm = OpenAI(temperature=0.9, max_tokens=500)

def echo(message, history, links):
    question = message
    urls = links.split()
    loader = UnstructuredURLLoader(urls)
    data = loader.load()
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = text_splitter.split_documents(data)
    
    vectorindex_openai = FAISS.from_documents(docs, OpenAIEmbeddings())
    chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vectorindex_openai.as_retriever())

    response = chain({"question": question}, return_only_outputs=True)
    formatted_response = response['answer']
    if 'sources' in response:
        formatted_response += "\nSources: " + response['sources']

    return formatted_response

demo = gr.ChatInterface(echo, 
                        additional_inputs=[
                            gr.Textbox("[Paste Links Here]", label="News Links"),
                        ]
                       )
    
if __name__ == "__main__":
    demo.launch(show_api=False)   
    
    