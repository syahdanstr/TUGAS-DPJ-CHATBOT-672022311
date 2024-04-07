import nltk
from nltk.chat.util import Chat, reflections

# Menggunakan corpus yang telah disediakan oleh NLTK
pairs = [
    ['my name is (.*)', ['Hi %1, how can I help you?']],
    ['(hi|hello|hey|hallo)', ['Hello, how can I assist you?']],
    ['(.*) your name?', ['I am just a chatbot, you can call me ChatX.']],
    ['(.*) help (.*)', ['Sure, I can help you with that.']],
    ['(.*) your age?', ['I am just a program, so I do not have an age.']],
    ['(.*) (location|city) ?', ['I am an AI and I exist everywhere.']],
    ['(.*) created you?', ['I was created by OpenAI using Python.']],
    ['(.*) (weather|temperature) ?', ['Sorry, I cannot provide real-time weather information.']],
    ['(.*)', ['Sorry, I did not understand that.']]

]

# Membuat chatbot menggunakan kelas Chat
chatbot = Chat(pairs, reflections)

def chat():
    print("Hello! I'm ChatX. How can I assist you today?")
    while True:
        user_input = input("You: ")
        response = chatbot.respond(user_input)
        print("ChatX:", response)
        if user_input.lower() == 'exit':
            break

if __name__ == "__main__":
    chat()
