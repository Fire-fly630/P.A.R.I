#PARI Responses
import random

# setting the array of converstation starting responses
Greeting = ["Hello", "Salutations", "What do you need", "Hello, how are you?", "How can I help?"]

# setting the array of conversation ending responses
Goodbye = ["Glad I could help", "Good-Bye", "Until we meet again", "Have a good day"]

# setting the array of greeting keywords
greeting_keywords = ["hello", "hi", "hey", "greetings"]

keywords = ["game", "pet", "book", "computer"]

chat_response = ["games are a great past time", "pets light up your life", "books are nice and relaxing", "computers are continually getting better"]

def main():
    # Start with a greeting
    print("P.A.R.I: " + random.choice(Greeting))

    userInput = input("Type something (or type 'bye' to end interaction): ")
    userInput = userInput.lower()

    while (userInput != "bye"):
        keyword_found = False
        greeting_found = False
        
        # Check if user input contains a greeting keyword
        for word in greeting_keywords:
            if word in userInput:
                print("P.A.R.I: " + random.choice(Greeting))
                greeting_found = True
                break
        
        # If no greeting was found, check for other keywords
        if not greeting_found:
            for index in range(len(keywords)):
                if (keywords[index] in userInput):
                    print("P.A.R.I: " + chat_response[index])
                    keyword_found = True
                    break
            
            if (keyword_found == False):
                add_keyword = input("I don't have a response to that. What should I be responding to? ")
                add_response = input("How should I respond to " + add_keyword + "? ")
                keywords.append(add_keyword)  # Fixed: append add_keyword instead of userInput
                chat_response.append(add_response)  # Fixed: append add_response instead of userInput
        
        # Ask for new input before looping again
        userInput = input("Type something (or type 'bye' to end interaction): ")
        userInput = userInput.lower()
if __name__ == '__main__':
    main()
# print("P.A.R.I: " + random.choice(Goodbye))
# print("Keywords:", keywords)
# print("Responses:", responses)