from app.search_index import retrieve_relevant_chunks
from llama_cpp import Llama

llm = Llama(model_path="./model/zephyr-7b-beta.Q4_0.gguf", n_ctx=2048)

async def generate_answer(query: str):
    context_chunks = retrieve_relevant_chunks(query)
    context = "\n\n".join(context_chunks)

    prompt = f"""Use the context below to answer the question.

Context:
{context}

Question: {query}
Answer:"""
    
    print(prompt)

    response = llm(prompt, max_tokens=2048, temperature=0.7)
    response = response["choices"][0]["text"].strip()
    yield response
    #for chunk in response:
    #    if word is not None:
    #        yield word
    #        await asyncio.sleep(0.01)
    
    