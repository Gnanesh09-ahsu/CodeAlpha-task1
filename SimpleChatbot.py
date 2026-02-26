def basic_chatbot():
    print("Chatbot: Hello! I am your basic chatbot.")
    print("Chatbot: You can say 'hello', 'how are you', or 'bye' to exit.")

    while True:
        user_input = input("You: ").lower() 

        if user_input == "hello":
            print("Chatbot: Hi!")

        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")

        elif user_input == "bye":
            print("Chatbot: Goodbye!")
            break  

        else:
            print("Chatbot: Sorry, I don't understand that.")

basic_chatbot()
