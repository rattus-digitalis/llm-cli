import readline
import sys
from llm.api import ask_mistral

def main():
    print("Welcome to LLM CLI — Mistral local chat. Type 'exit' to quit.")
    while True:
        try:
            question = input(">>> ").strip()
            if question.lower() in {"exit", "quit"}:
                break
            if not question:
                continue

            response = ask_mistral(question)
            print(response)

        except KeyboardInterrupt:
            print("\nExiting.")
            break
        except Exception as e:
            print(f"Error: {e}")
