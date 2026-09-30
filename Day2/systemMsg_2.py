import ollama
response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "system",
            "content":"Give answer in 2 lines only.I am the teacher of 5 yrs old kid."
        },
        {
            "role":"user",
            "content":"Explain AI"
        }
    ]
)
print(response["message"]["content"])
