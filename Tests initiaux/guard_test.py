from ollama import chat


response_to_test = """
This is a defensive explanation of how to secure
an SSH server using strong authentication,
key-based login, firewall rules and logging.
"""


result = chat(
    model="llama-guard3:1b",
    messages=[
        {
            "role": "user",
            "content": response_to_test
        }
    ]
)


print("\n=========== LLAMA GUARD ===========\n")
print(result.message.content)