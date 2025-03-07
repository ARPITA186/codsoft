
def chatagent():
    print("Hey! What's up? Do you want me to assist you today?")

    while True:
        use_input = input("You: ").lower()

        if use_input in ['bye','tata','quit','see you again','exit']:
            print("Bye! Have you a great day!")
            break

        elif 'how are you' in use_input or 'what is up' in use_input:
             print("Chatagent: Hey!Doing Great.What about you?")

        elif 'hello' in use_input or 'hi' in use_input or 'hey' in use_input:
            print("Chatagent: Hey! Need help? Feel free to ask!")
        elif 'fine' in use_input or 'okay' in use_input or 'nice' in use_input or 'great' in use_input or 'awsome' in use_input:
            print("Chatagent: Nice to hear that!")
        elif 'not good' in use_input or 'bad' in use_input or 'feeling too sad' in use_input or 'unhappy' in use_input :
            print("Chatagent: Sad to hear that !Aww! what happened? Are you depressed upon something? Don't worry all will be okay")
        elif 'help' in use_input or 'Help' in use_input or 'Can you please help me' in use_input:
            print(" Chatagent: Sure!That's why I am here. Tell me, how can I help you?")
        elif 'what is your name' in use_input or 'tell me your name' in use_input or 'your name' in use_input:
            print("Chatagent: Hi! I am Chatagent who is here to help you 24*7 hours ! You can ask for help at any time!!!")
        elif 'thanks' in use_input or 'thank you' in use_input or 'thanks a lot' in use_input:
            print("Chatagent: It's means a lot. Let me know if you need any thing else!")

        else:
            print("Chatagent: I'm sorry, I don't understand that. Can you ask me again?")

chatagent()
