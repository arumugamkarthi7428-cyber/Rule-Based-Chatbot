def chatbot():
    print("Chatbot: Hello! I am a simple rule-based chatbot.")
    print("Chatbot: Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input in ["hi", "hello", "hey"]:
            print("Chatbot: Hello! How can I help you?")

        elif "your name" in user_input:
            print("Chatbot: I am a rule-based chatbot created as an internship project.")

        elif "help" in user_input:
            print("Chatbot: I can respond to greetings, basic questions, and exit commands.")

        elif "time" in user_input:
            print("Chatbot: I don't track real time, but I'm always ready to chat!")

        elif user_input in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye! Have a nice day 😊")
            break

        else:
            print("Chatbot: Sorry, I didn't understand that. Try something else.")

if __name__ == "__main__":
    chatbot()
