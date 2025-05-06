# TriviaBot

**TriviaBot** is a Discord bot that allows users to play a trivia game directly in their Discord server. The bot selects a random question and gives the user 10 seconds to answer correctly. If the answer is correct, the bot congratulates the player; if not, it shows the correct answer.

This bot is built in Python using the discord.py library and works simply and efficiently on any Discord server.

---

## Features

- Responds to the `!trivia` command with a trivia question.
- Players have 10 seconds to answer each question.
- If the answer is correct, the bot congratulates the player.
- If the answer is incorrect or time runs out, the bot shows the correct answer.
  
## Technologies Used

- **Python**: Programming language used to develop the bot.
- **discord.py**: Python library that facilitates interaction with the Discord API.
- **asyncio**: Python library for handling asynchronous tasks, such as waiting for user responses.

---

## Installation

### 1. Clone this repository

To get a copy of the project, clone it to your local machine:

```bash
https://github.com/FranciscoLG241/Proyecto-2-Digitalizacion.git
```

---


### 2. Install the dependencies
To install the necessary libraries, use pip:

```bash
pip install discord asyncio
```

---

### 3. Get your bot token
To make the bot work, you will need a Discord bot token. If you don’t have one yet, follow these steps:

- Go to the [Discord Developer Portal](https://discord.com/developers/applications).
- Create a new application and enable the bot.
- Copy the token provided by Discord for your bot.

---

### 4. Configure the bot
- Open the file `bot.py` in a text editor.
- Replace the following line with your actual bot token:

```python
TOKEN = "your_token_here"
```

---

### 5. Configure the trivia questions
The bot uses a file called preguntas.json to store the questions and answers. Make sure your preguntas.json file contains questions in JSON format like this example:

```bash
[
    {
        "pregunta": "¿Cuál es el continente más grande?",
        "respuesta": "Asia"
    },
    {
        "pregunta": "¿Quién pintó la Mona Lisa?",
        "respuesta": "Leonardo da Vinci"
    }
]
```
- You can add more questions in the same format so the bot has more variety.

---

### Running
Once you have configured the bot, you can run it with the following command:

```bash
python bot.py
```
The bot will connect to Discord and will be ready to use. It will listen for the !trivia command in the channels where it has permissions.

---

### Usage
- Command: !trivia
- Description: The bot will select a random question and give 10 seconds for the player to respond. If the answer is correct, the player is congratulated; if it is incorrect or time runs out, the correct answer is displayed.
- Invite the bot to your server
- If you want TriviaBot to join your server, follow these steps:

1. Go to the Discord Developer Portal.
2. Select your bot application.
3. In the OAuth2 section, select "bot" under "scopes".
4. In "permissions", check the permissions the bot needs, such as Send Messages, Read Messages, etc.
5. Copy the generated link and paste it into your browser to invite the bot to your server.












