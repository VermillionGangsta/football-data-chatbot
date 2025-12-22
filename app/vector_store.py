from pathlib import Path
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.docstore.document import Document

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data" / "processed"
VECTOR_DIR = BASE_DIR / "data" / "vectorstore"


def load_facts():
    documents = []

    print(f"Reading facts from: {DATA_DIR}")

    for file_path in DATA_DIR.glob("*.txt"):
        print(f"Loading file: {file_path.name}")
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    documents.append(Document(page_content=line))

    return documents


def create_vector_store(documents):
    if len(documents) == 0:
        raise ValueError("No documents found. Vector store cannot be created.")

    embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
    vectorstore = FAISS.from_documents(documents, embeddings)

    VECTOR_DIR.mkdir(parents=True, exist_ok=True)
    vectorstore.save_local(VECTOR_DIR)


if __name__ == "__main__":
    print("Loading football facts...")
    docs = load_facts()
    print(f"Loaded {len(docs)} documents")

    print("Creating vector store...")
    create_vector_store(docs)

    print("Vector store created successfully.")

