from sentence_transformers import util, SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2")
Sentences = [
    "I love playing football",
    "I enjoy playing soccer",
    "I like eating pizza",
]
sentence_embedding = model.encode(sentences)
print(sentence_embedding[0])