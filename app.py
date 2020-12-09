from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

app = Flask(__name__)



# Create object of ChatBot class with Storage Adapter
food_bot = ChatBot(
    'Foodbot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.TimeLogicAdapter']
)
# Data used for training the chatbot
trainingList=[
    'Hi',
    'Hi, so nice to have you here, welcome to Niger Fitfam. We are here to answer your questions on how to be fit the Nigerian way.',
    'Hello',
    'Hi, so nice to have you here, welcome to Niger Fitfam. We are here to answer your questions on how to be fit the Nigerian way.',
    'Good day',
    'Hi, so nice to have you here, welcome to Niger Fitfam. We are here to answer your questions on how to be fit the Nigerian way.',
    'Good morning',
    'Hi, so nice to have you here, welcome to Niger Fitfam. We are here to answer your questions on how to be fit the Nigerian way.',
    'Good afternoon',
    'Hi, so nice to have you here, welcome to Niger Fitfam. We are here to answer your questions on how to be fit the Nigerian way.',
    'Good evening',
    'Hi, so nice to have you here, welcome to Niger Fitfam. We are here to answer your questions on how to be fit the Nigerian way.',
    'I am overweight, what food can I',
    'For breakfast, Lunch or Dinner',
    'Can you recommend what food to eat',
    'For breakfast, Lunch or Dinner',
    'Can you recommend a diet plan',
    'For breakfast, Lunch or Dinner',
    'What can I have for Breakfast',
    'There are a list of options... \
        \n(1.	Lean green smoothie. (4 handful of kale, ½ large cucumber, thumb-size fresh ginger, 1 large banana, pinch of cinnamon.\
        \n(2.	Fat Flush smoothie. (1 green apple, 1 thumb-size fresh ginger, ¼ of hot pepper, 1 orange, juice 1 lemon, ¼ cup of parsley, 4 sprigs fresh mint)\
        \n(3.	Egg Avocado bowl ( 1 taespoon of oil, 2 large tomatoes, ½ large cucumber, 1 large egg, ½ large avocado, ½ lemon juice, salt and pepper)',
    'What can I have for lunch',
   'There are a list of options... \
        \n(1.	Stewed Cabbage. (I head of cabbage, minced turkey or beef, 2 small tomatoes, 1 tablespoon tomato paste, 1 green/red bell pepper, 1 hot pepper, 1 large onion, curry, thyme and ginger, 2 bay leaves, 2 maggi cubes, 2 tbs of oil, salt for taste)\
        \n(2.	Ofada rice and vegetables. (Ofada rice, hot pepper, tomatoes, tatase, 1 tbs palm oil, dried fish,)\
        \n(3.	Wilted vegetables (10 cups of Ugwu or gbure, 1 maggi cube, onions, ½ spoon of olive oil)',
    'What can I have for dinner',
    'There are a list of options... \
        \n(1.	Okro soup. (2 cups of okro, 1 tablespoon palmoil, crayfish, fish, shrimps, ponmo, 2 maggi cubes and salt to taste.)\
        \n(2.	Goat meat peppersoup. (600G of goat meat, 3 hot peppers, 1 onion, 2 garlic cloves, 2 tablespoon peppersoup mix)\
        \n(3.	Suya Lettuce wrap (Suya, onions, tomatoes, bell peppers, 6 lettuce, dressing(Greek yoghurt, lemon juice, pepper and salt)',
    'Please, Provide me with your order id',
    'How many calories do I need to consume in a day to lose weight / be healthy',
    'What is your gender',
    'Male',
    'You should eat a minimum of 1400 calories',
    'Female',
    'You should eat a minimum of 1200 calories',
    'Can you recommend exercises',
    '30 minutes on the treadmill, 30 minutes of Jogging, 10 minute of Burpees, 10 Minutes of Mountain climbing, Russian twists'
]

#declaring the chatbot
trainer = ListTrainer(food_bot)

#Training starts here
trainer.train(trainingList)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(food_bot.get_response(userText))


if __name__ == "__main__":
    app.run()

