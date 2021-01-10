# RamsiiBot 👨‍🍳

**_Want to cook but missing an ingredient? Ask Ramsii!_**

Read on to see what Ramsii offers, check out our [Devpost submission](https://devpost.com/software/substitute-ramsay), or try our bot out [here](https://t.me/RamsiiBot)! 🙂

## Inspiration 💡
As cash-strapped students who cook from time to time, we've always struggled with the disappointment of not being able to prepare a dish simply because we were missing 1 or 2 ingredients for a recipe. If only we could find substitutes for them!

## What it does 💪
Inspired by a certain legendary and over-memed British chef, Ramsii is built to provide cooks with alternatives for ingredients they might be missing to complete a recipe. There is also a rating function for users to judge whether our proposed substitution actually worked; the aggregate percentage score of the ingredient will be displayed for all to see. (Some examples to try: butter, wine, eggs, saffron, arrowroot

In addition, Ramsii offers users entertainment as well as a simple recipe recommendation for those who have a hard time deciding what they should cook. Below are the other commands our bot currently supports:

- /trivia: For users to learn some interesting facts about food in general
- /hungry: Our "I'm Feeling Hungry" feature, which gives users a randomly selected recipe
- /joke: Gives users a good laugh!
- /end: A simple farewell from Gordon Ramsay himself

## How we built it 🛠
We created a Telegram bot using python-telegram-bot and deployed it on Heroku. Since we wanted to provide users different types of substitutes, we had to set up our own database using sqllite to store the different ingredients. Additionally, to implement features such as Food Trivia, we used Spoonacular, a Food API, to query responses.

## Challenges we ran into 🧗‍
- Populating our database from scratch and retrieving credible ingredient sources
- Testing the bot (since there were 2 of us but we only created 1 bot token)
- Understanding API endpoints from Spoonacular and python-telegram-bot
- Fixing merge conflicts in Git
- Lots and lots of sleep-deprived debugging

## Accomplishments that we're proud of 🎖
- Completed our project in less than 24hrs considering our inexperience with bots
- Developing a rather smooth flow for users
- Managed to accomplish the core features we set out to build and more
- Worked decently well with each other despite being in the East and West (over Zoom!)
- Grabbing $31 worth of vouchers (so far) despite our busy schedules :D

## What we learned 🙇
- How to work with different APIs (python-telegram-bot, sqlalchemy, spoonacular)
- Designing, inserting and querying databases (SQLite)
- Deploying a bot to Heroku instead of ngrok
- How to work in a team (open communication and helping each other out where we can)
- Design consideration and thinking about how to write cleaner code

## What's next for RamsiiBot! 🔮
- We are looking to further populate our database with greater breadth and depth, be it through any open-source datasets, APIs, or user feedback
- Increasing customizability for the "I'm Feeling Hungry" feature, to allow users to indicate preference for certain types of meals
- Sourcing for and integrating other APIs (for example, to recommend products from stores or supermarkets like Fairprice)
- Integrating more Gordon Ramsay memes and quotes (for entertainment and inspirational purposes)
- Writing tests for different commands to ensure nothing breaks when we push new features
- Refactoring code and making it more readable
- Moving to a cloud database on Google Cloud Platform which could make updates more convenient

## Special thanks 🙏
For precise substitute information:
- The Farmer's Almanac
- JoyofBaking.com
- AllRecipes

For the image that the logo adapted:
Popsugar.Food (https://www.popsugar.com/food/Gordon-Ramsay-Net-Worth-45983315)
