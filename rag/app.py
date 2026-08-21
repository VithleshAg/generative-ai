from src.data_loader import load_all_documents
# from src.embedding import EmbeddingPipeline
from src.vectorstore import FaissVectorStore
from src.search import RAGSearch

## Example usage

if __name__ == "__main__":
    # documents = load_all_documents("data")

    # 1. Embedding example
    # chunks = EmbeddingPipeline().chunk_documents(documents)
    # chunkVectors = EmbeddingPipeline().embed_chunks(chunks)
    # print(chunkVectors)

    # # 2. Vectorstore example
    # store = FaissVectorStore("faiss_store")
    # # store.build_from_documents(documents)
    # store.load()
    # print(store.query("Please tell me about VRML history?", top_k=3))

    # 3. Search
    store = FaissVectorStore("faiss_store")
    store.load()

    rag_search = RAGSearch()
    summary = rag_search.search_and_summarize("Please tell me about VRML history?", top_k=3)
    print("Summary: ", summary)
