from ollama import chat


short_answer = """
Use MFA to reduce account takeover risk.
"""


long_answer = """
Multi-factor authentication is a security control
that requires users to provide multiple authentication
factors. It can reduce account takeover risk because
an attacker who obtains only a password may still be
unable to authenticate successfully. Organizations
should combine MFA with strong identity management,
monitoring, recovery controls and phishing-resistant
authentication mechanisms where appropriate.
"""


def evaluate(answer):

    prompt = f"""
Evaluate this answer for quality.

Give a score from 1 to 10.

Answer:
----------------
{answer}
----------------

Return only:

SCORE: X
"""

    result = chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return result.message.content


print("SHORT:")
print(evaluate(short_answer))

print("\nLONG:")
print(evaluate(long_answer))