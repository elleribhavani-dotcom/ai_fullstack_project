import ollama
response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "user",
            "content":"what is AI ? give important key points and easy to understand the  beginers"
        }
    ]
)
print(response["message"]["content"])
