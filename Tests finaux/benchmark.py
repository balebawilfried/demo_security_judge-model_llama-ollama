import json
from ollama import chat
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
TESTS_FILE = BASE_DIR / "tests.json"


#with open(r".\Tests finaux\tests", "r", encoding="utf-8") as file:
with open(TESTS_FILE, "r", encoding="utf-8") as file:
    tests = json.load(file)


def generate(prompt):

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

    return result.message.content.strip()


results = []


for test in tests:

    print("\n" + "=" * 70)
    print("TEST", test["id"])
    print("=" * 70)

    generated = generate(test["prompt"])

    decision = guard(generated)

    print("\nExpected:")
    print(test["category"])

    print("\nGenerated:")
    print(generated)

    print("\nGuard:")
    print(decision)

    results.append(
        {
            "id": test["id"],
            "expected": test["category"],
            "generated": generated,
            "decision": decision
        }
    )


with open(
    "results.json",
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        results,
        file,
        indent=4,
        ensure_ascii=False
    )


print("\n\nResults saved to results.json")