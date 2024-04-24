import os


os.environ["AZURESEARCH_FIELDS_ID"] = "chunk_id"
os.environ["AZURESEARCH_FIELDS_CONTENT"] = "chunk"
os.environ["AZURESEARCH_FIELDS_CONTENT_VECTOR"] = "vector"
os.environ["AZURESEARCH_FIELDS_TAG"] = "metadata"

from langchain_community.vectorstores.azuresearch import AzureSearch
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_openai import AzureChatOpenAI, AzureOpenAIEmbeddings

if not os.getenv("AZURE_OPENAI_ENDPOINT"):
    raise ValueError("Please set the environment variable AZURE_OPENAI_ENDPOINT")

if not os.getenv("AZURE_OPENAI_API_KEY"):
    raise ValueError("Please set the environment variable AZURE_OPENAI_API_KEY")

if not os.getenv("AZURE_EMBEDDINGS_DEPLOYMENT"):
    raise ValueError("Please set the environment variable AZURE_EMBEDDINGS_DEPLOYMENT")

if not os.getenv("AZURE_CHAT_DEPLOYMENT"):
    raise ValueError("Please set the environment variable AZURE_CHAT_DEPLOYMENT")

if not os.getenv("AZURE_SEARCH_ENDPOINT"):
    raise ValueError("Please set the environment variable AZURE_SEARCH_ENDPOINT")

if not os.getenv("AZURE_SEARCH_KEY"):
    raise ValueError("Please set the environment variable AZURE_SEARCH_KEY")

api_version = os.getenv("OPENAI_API_VERSION", "2023-03-15-preview")
index_name = os.getenv("AZURE_SEARCH_INDEX_NAME", "kodekveld-mdir-test")

embeddings = AzureOpenAIEmbeddings(
    deployment=os.environ["AZURE_EMBEDDINGS_DEPLOYMENT"],
    chunk_size=1,
)

vector_store: AzureSearch = AzureSearch(
    azure_search_endpoint=os.environ["AZURE_SEARCH_ENDPOINT"],
    azure_search_key=os.environ["AZURE_SEARCH_KEY"],
    index_name=index_name,
    embedding_function=embeddings.embed_query,
)

"""
(Optional) Example document - 
Uncomment the following code to load the document into the vector store
or substitute with your own.
"""
# import pathlib
# from langchain.text_splitter import CharacterTextSplitter
# from langchain_community.document_loaders import TextLoader
#
# current_file_path = pathlib.Path(__file__).resolve()
# root_directory = current_file_path.parents[3]
# target_file_path = "state_of_the_union.txt"
#
# loader = TextLoader(str(target_file_path), encoding="utf-8")
#
# documents = loader.load()
# text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
# docs = text_splitter.split_documents(documents)
#
# vector_store.add_documents(documents=docs)

# RAG prompt
template = """Answer the question based only on the following context:
{context}
Question: {question}

answer all questions in Norwegian (nynorsk)
"""

# Perform a similarity search
retriever = vector_store.as_retriever()

_prompt = ChatPromptTemplate.from_template(template)
_model = AzureChatOpenAI(
    azure_deployment=os.environ["AZURE_CHAT_DEPLOYMENT"],
    api_version=api_version
)
chain = (
        RunnableParallel({"context": retriever, "question": RunnablePassthrough()})
        | _prompt
        | _model
        | StrOutputParser()
)


query = "Har det nylig blitt gjort noen tiltak for jerv i Snåsa?"
print("Query:" + query)
print("Answer:" + chain.invoke(query))
# print("\n\n Context used: " + str(retriever.invoke(query)[0]))
