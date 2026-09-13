from ollama import chat


def generate(prompt):

    response = chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.message.content


def guard(response):

    result = chat(
        model="llama-guard3:1b",
        messages=[
            {
                "role": "user",
                "content": response
            }
        ]
    )

    return result.message.content


prompt = """
Explain how to secure an SSH server.
Focus only on defensive security.
"""


print("\n================ INPUT ================\n")
print(prompt)


generated = generate(prompt)


print("\n================ GENERATOR ================\n")
print(generated)


decision = guard(generated)


print("\n================ GUARD ================\n")
print(decision)