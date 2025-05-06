# **TriviaBot Wiki**

## **Technical Documentation**

### **Project Architecture**

TriviaBot is developed in **Python 3.8+** and uses the `discord.py` library to interact with the Discord API. The bot allows users to play a trivia game within a Discord server, with questions selected from a JSON file. The architecture is simple and is based on three main components:

1. **Trivia command (`!trivia`)**: Users can invoke this command on the server for the bot to select a random question.
2. **Time Management**: The bot waits for 10 seconds for the user to answer.
3. **Answer Evaluation**: The bot compares the player's answer with the correct one and responds based on the result: congratulations for the correct answer or the correct answer if the time runs out or the answer was incorrect.

### **Technologies and Libraries Used**
- **Python 3.8+**: The programming language used to develop the bot.
- **discord.py**: A library for interacting with the Discord API and handling bot logic.
- **JSON**: Used to store the trivia questions and answers, allowing easy customization.

### **Data Flow**
1. **User Input**: The player uses the `!trivia` command in a Discord channel.
2. **Question Selection**: The bot selects a random question from the `preguntas.json` file.
3. **Interaction**: The bot waits 10 seconds for the user's answer.
4. **Evaluation**: The answer is evaluated, and the bot responds by congratulating the player if the answer is correct or showing the correct answer if it’s not.

### **Project Structure**
- **bot.py**: The main file that handles the bot's logic and interactions with Discord.
- **preguntas.json**: Contains the trivia questions and answers in JSON format. This is the file the bot reads to get the questions.
- **config.py** (optional): For future additional configurations like the API key or bot settings.

### **Installation Instructions**
1. **Clone the repository**:
    ```bash
    git clone https://github.com/FranciscoLG241/TriviaBot.git
    ```
2. **Install dependencies**:
    ```bash
    pip install discord
    ```
3. **Configure the bot**:
   - Go to the [Discord Developer Portal](https://discord.com/developers/applications).
   - Create a new application and enable the bot.
   - Get the **bot token** and replace the `TOKEN` variable in the `bot.py` file with your bot’s token.
   - Customize the `preguntas.json` file with questions and answers for the game.

4. **Run the bot**:
    ```bash
    python bot.py
    ```
   The bot will be active and ready to receive commands on your Discord server.

---

## **Devlog**

### **Phase 1**
- **Strategic Goal**: Create a functional bot to play trivia in Discord servers.
- **Changes Made**:
  - Created the repository and developed the basic bot functionality.
  - The bot responds to the `!trivia` command and selects a random question from the `preguntas.json` file.
  - The bot allows players to respond within a 10-second time limit.
  - Implemented a response to the player, either congratulating them for the correct answer or showing the correct answer in case of an incorrect answer or timeout.
- **Motivation**: Provide a simple and fun way to interact within Discord servers.

---

### **Phase 2**
- **Strategic Goal**: Improve the user experience.
- **Changes Made**:
  - Added more questions and answers to the `preguntas.json` file.
  - Improved error handling in case the `preguntas.json` file is malformed or missing.
- **Motivation**: Expand the variety of questions and improve the system's robustness against potential data issues.

---

### **Phase 3**
- **Strategic Goal**: Improve documentation and facilitate contributions.
- **Changes Made**:
  - Documented the code with comments and docstrings.
  - Added a `CONTRIBUTING.md` file that provides guidelines for new contributors.
  - Made the first public release of the code on GitHub with an initial version.
- **Motivation**: Make it easier for other developers to contribute to the project and improve the maintainability of the code.

---

### **Phase 4**
- **Strategic Goal**: Expand the bot's flexibility and customization.
- **Changes Made**:
  - Added support for server administrators to customize the bot's questions by editing the `preguntas.json` file.
  - Included a small guide in the Wiki on how to add custom questions.
- **Motivation**: Allow users to customize the game to their preferences and add more interactivity to the bot.

---

## **Future Improvements (Proposals)**

1. **Integration with external APIs**: Connect TriviaBot with external trivia databases like [Open Trivia Database](https://opentdb.com/) to get more up-to-date and diverse questions without the need to manually edit the `preguntas.json` file.
2. **Multilingual support**: Add support for multiple languages, allowing the bot to be used in different regions and communities.
3. **Scoring system**: Implement a scoring system where players accumulate points for correct answers, and display overall rankings.
4. **More customization options**: Allow administrators to configure not only the questions but also the time limit or the difficulty of the questions.

---

### **Changelog**
- **Phase 1**: Initial version of the bot.
- **Phase 2**: Expanded questions and improved error handling.
- **Phase 3**: Code documentation and public release on GitHub.
- **Phase 4**: Added question customization.


