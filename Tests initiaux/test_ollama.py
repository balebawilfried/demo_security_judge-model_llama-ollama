from ollama import chat


response = chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "user",
            "content": "Explain what a firewall is in simple terms."
        }
    ]
)

print("\n=== GENERATEUR ===\n")
print(response.message.content)