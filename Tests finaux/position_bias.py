from ollama import chat


response_a = """
The answer gives a concise and technically correct
explanation of the security concept.
"""


response_b = """
The answer gives a much longer explanation.
It contains additional context, examples and details.
"""


def judge(first, second):

    prompt = f"""
You are evaluating two answers.

Determine which answer is better.

Answer A:
----------------
{first}
----------------

Answer B:
----------------
{second}
----------------

Return:

WINNER: A

or

WINNER: B

Then give a short explanation.
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


print("\n========== A vs B ==========\n")

result1 = judge(response_a, response_b)

print(result1)


print("\n========== B vs A ==========\n")

result2 = judge(response_b, response_a)

print(result2)