from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer  # Added missing import

# Create a new chatbot
chatbot = ChatBot("SimpleBot")

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
trainer.train("chatterbot.corpus.english")

# Start the conversation
print("Bot: Hello! How can I help you today?")

while True:
    # Get user input
    user_input = input("You: ")

    # Break the loop if the user wants to exit
    if user_input.lower() == 'exit':
        print("Bot: Goodbye!")
        break

    # Get the bot's response
    bot_response = chatbot.get_response(user_input)

    # Print the bot's response
    print("Bot:", bot_response)
