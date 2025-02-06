import groq

client = groq.Client(api_key="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")

def get_ai_response(user_input):
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": user_input}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    print("Welcome to your AI Chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            print("\nGoodbye! 👋")
            break
        response = get_ai_response(user_input)
        print("AI:", response)