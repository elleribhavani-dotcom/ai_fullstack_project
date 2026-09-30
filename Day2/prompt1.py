import ollama
response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "user",
            "content":"what is AI? give answer in 5 lines"
        }
    ]
)
print(response["message"]["content"])
