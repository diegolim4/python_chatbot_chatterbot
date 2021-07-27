from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Nome do meu chatbot
chatbot = ChatBot('Petrus')

trainer = ListTrainer(chatbot)

trainer.train([
    'Hello!',
    'Hi, how are you',
    'I fine and you:'
])

while True:
    request = input('You: ')
    response = chatbot.get_response(request)
    print('Bot: ', response)

