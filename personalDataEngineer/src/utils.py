from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

def load_pdf(file_path):
    """
    Load a PDF file using PyPDFLoader.

    Parameters:
        file_path (str): The path to the PDF file.

    Returns:
        list: List of loaded documents.
    """
    loader = PyPDFLoader(file_path)
    return loader.load()

# Example usage:
#pdf_file_path = 'attention.pdf'
#documents = load_pdf(pdf_file_path)

from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_documents(inputFile):
    """
    Split documents using RecursiveCharacterTextSplitter.

    Parameters:
        docs (list): List of documents to be split.

    Returns:
        list: List of split documents.
    """
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return text_splitter.split_documents(inputFile)

# Example usage:
#split_documents_result = split_documents(inputFiles)


def create_faiss_vector_db(documents):
    """
    Create a FAISS vector database from documents using OpenAI embeddings.

    Parameters:
        documents (list): List of documents.

    Returns:
        FAISS: FAISS vector database.
    """
    embeddings = OpenAIEmbeddings()
    return FAISS.from_documents(documents, embeddings)

# Example usage:
#faiss_vector_db = create_faiss_vector_db(documents)

