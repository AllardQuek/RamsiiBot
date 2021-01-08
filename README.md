# Ramsii Bot 👨‍

**_Want to cook but missing an ingredient? Ask Ramsay!_**

## Inspiration
As students who cook ourselves and with limited budgets, we've always struggled with the disappointment of not being able to prepare a dish simply because we were missing 1 or 2 ingredients for a recipe. If only we could find substitutes for them!

## What it does
Ramsii is built to provide cooks with alternatives for ingredients they might be missing to complete a recipe. In addition, Ramsii offers users entertainment as well as a simple recipe recommendation for those who have a hard time deciding what they should cook. Below are the commands our bot currently supports:

/trivia: For users to learn some interesting facts about the food they eat
/hungry: Our "I'm Feeling Hungry" feature, which gives users a randomly selected recipe
/joke: Gives users a good laugh!
/end: A simple farewell from Gordon Ramsay himself

## How we built it
We created a Telegram bot using python-telegram-bot and deployed it on Heroku. Since we wanted to provide users different types of substitutes, we had to set up our own database using sqllite to store the different ingredients. Additionally, to implement features such as Food Trivia, we used Spoonacular, a Food API, to query responses.

## Challenges we ran into
- Populating our database from scratch and retrieving credible ingredient sources
- Testing the bot (since there were 2 of us but we only created 1 bot token)
- Understanding API endpoints from Spoonacular and python-telegram-bot
- Fixing merge conflicts in Git

## Accomplishments that we're proud of
- Completed our project in less than 24hrs considering our inexperience with bots
- Developing a rather smooth flow for users
- Managed to accomplish the features we set out to build and more
- Grabbing $31 worth of vouchers despite our busy schedules :D

## What we learned
- How to work with different APIs (python-telegram-bot, sqlalchemy)
- Designing, inserting and querying databases (sqllite)
- Deploying a bot to Heroku instead of ngrok
- How to work in a team (open communication and helping each other out where we can)

## What's next for Substitute Ramsay!
- We are looking to further populate our database with greater breadth and depth, be it through any open-source datasets, APIs, or user feedback
- Increasing customizability for the "I'm Feeling Hungry" feature, to allow users to indicate preference for certain types of meals
- Sourcing for and integrating other APIs (for example, to recommend products from stores or supermarkets like Fairprice)
- Integrating more Gordon Ramsay memes and quotes (for entertainment and inspirational purposes)
- Writing tests for different commands to ensure nothing breaks when we push new features
