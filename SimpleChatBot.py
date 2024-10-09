import re

# Define a set of predefined responses for various user inputs
def respond(user_input):
    # Greeting responses
    if re.search(r'\bhello\b|\bhi\b|\bhey\b', user_input, re.IGNORECASE):
        return "Hello! How can I assist you today?"

    # Farewell responses
    elif re.search(r'\bbye\b|\bexit\b|\bquit\b', user_input, re.IGNORECASE):
        return "Goodbye! Have a great day!"

    # Asking about chatbot's identity
    elif re.search(r'who are you|what can you do', user_input, re.IGNORECASE):
        return "I am a simple chatbot created to assist you with basic queries."

    # Simple weather inquiry
    elif re.search(r'weather|temperature', user_input, re.IGNORECASE):
        return "I'm not connected to live data, but typically it's sunny this time of the year."

    # User asking for help
    elif re.search(r'help|assist', user_input, re.IGNORECASE):
        return "I'm here to assist you. You can ask me about basic queries like greetings, weather, or anything else!"

    # Default response when no matching pattern is found
    else:
        return "I'm sorry, I don't understand. Could you please rephrase your question?"

# Main function for chatbot loop
def chatbot():
    print("Chatbot: Hello! I am your chatbot. Type 'quit' to end the conversation.")
    
    while True:
        # Get input from the user
        user_input = input("You: ")

        # If user types 'quit', break the loop and exit
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye! Have a nice day.")
            break

        # Get response from chatbot
        response = respond(user_input)
        
        # Print the chatbot's response
        print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
