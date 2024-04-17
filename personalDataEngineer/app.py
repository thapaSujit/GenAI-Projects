import os
from dotenv import load_dotenv
from src.utils import load_pdf, split_documents, create_faiss_vector_db
#from src.promptsTemplate import prompt_template
from flask import Flask, render_template, jsonify, request
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain import hub

app = Flask(__name__)
load_dotenv()
os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

inputFiles = load_pdf("/data/de.pdf")

split_documents_result = split_documents(inputFiles)

faiss_vector_db = create_faiss_vector_db(split_documents_result)

# Loads the latest version
prompt = hub.pull("rlm/rag-prompt", api_url="https://api.hub.langchain.com")

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.8)

qa_chain = RetrievalQA.from_chain_type(
    llm, retriever=faiss_vector_db.as_retriever(), chain_type_kwargs={"prompt": prompt}
)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    result=qa_chain({"query": input})
    print("Response : ", result["result"])
    return str(result["result"])


if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug= True)
