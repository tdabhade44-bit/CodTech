import nltk
from nltk.tokenize import word_tokenize

# Download tokenizer
nltk.download('punkt')

print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    tokens = word_tokenize(user_input)

    if "hello" in tokens or "hi" in tokens:
        print("Chatbot: Hello! How can I help you?")
    
    elif "name" in tokens:
        print("Chatbot: I am an AI Chatbot built using NLP.")
    
    elif "help" in tokens:
        print("Chatbot: I can answer basic questions. Try asking about my name.")
    
    elif "bye" in tokens:
        print("Chatbot: Goodbye! Have a nice day ")
        break
    
    else:
        print("Chatbot: Sorry, I didn't understand that.")

