# Contribution Guide for TriviaBot

Thank you for your interest in contributing to TriviaBot! This project is open source and is open to community improvements.

## Current Software Goal

TriviaBot is an interactive trivia tool designed to be used in Discord servers. Its purpose is to provide users with an entertaining way to interact with each other through trivia questions and answers. The bot randomly selects a question, allows users to respond within a limited time, and provides feedback based on the user's answer. This software addresses the current entertainment needs within Discord communities, promoting engagement and learning in a fun way.

---

## Future Needs and Proposed Improvements

As the project grows, several needs have been identified that could expand its functionality and increase its impact:

### Functional Improvements
- **Expand the question set**: Currently, the bot relies on a local JSON file for the questions. It could integrate an online trivia API to get dynamic and up-to-date questions.
- **Multilingual support**: Allow the bot to be used in different languages to reach a broader audience.
- **Ranking and scoring**: Add a scoring system to track the best scores and encourage competition among players.
- **Custom question creation**: Allow server administrators to create their own trivia questions through an easy-to-use interface.

---

## System and Data Interaction

The bot operates autonomously within a Discord server. The main components of the system are:

1. **Trivia Command (`!trivia`)**: Users can invoke the bot in any channel with the `!trivia` command. This generates an interaction where the bot selects a random question from a local JSON file.
2. **User's Answer**: Users have 10 seconds to answer the question. The bot verifies the answer by comparing the user's input with the correct answer.
3. **Feedback**: If the answer is correct, the bot congratulates the user; if it is incorrect or the time runs out, the bot shows the correct answer.

### Example of data flow:
1. **Input**: User runs `!trivia`.
2. **Processing**: The bot selects a random question from the `preguntas.json` file and waits for a response for 10 seconds.
3. **Output**: The bot responds with a congratulatory message or shows the correct answer.

### Data Structure:
The `preguntas.json` file contains a list of objects with trivia questions and answers in JSON format:

```json
[
  {
    "pregunta": "What is the largest continent?",
    "respuesta": "Asia"
  },
  {
    "pregunta": "Who painted the Mona Lisa?",
    "respuesta": "Leonardo da Vinci"
  }
]
```

## Proposals to Improve Interoperability

The bot currently relies on static data (the `preguntas.json` file) to function. Here are some proposals to improve interoperability:

- **Integration with external trivia APIs**: This would allow the bot to obtain updated and diversified questions dynamically without the need to manually update the file. Examples include the [Open Trivia Database](https://opentdb.com/) or [JService](https://jservice.io/).
  
- **Interaction with other chat platforms**: In the future, TriviaBot could expand to other messaging platforms such as **Slack** or **Telegram** to provide support to a larger community.

---

## Skills Needed to Contribute

To contribute to TriviaBot, it is recommended to have experience with the following skills and technologies:

- **Python 3.8+**: The bot is developed in Python, so knowledge of this language is essential.
  
- **Discord API**: Familiarity with the `discord.py` library to interact with the Discord API.
  
- **JSON Handling**: Ability to work with JSON files, as the bot depends on this format to store trivia questions.

---

## Training Strategies for Contributors

If you wish to contribute or become an active collaborator on the project, here are some strategies to facilitate the integration process:

- **Internal Documentation**: Make sure to read the internal code documentation and Python style guides. This will help ensure your code follows the same conventions as the rest of the project.
  
- **Code Review**: New contributors should submit their changes for review via a Pull Request. This ensures the code meets quality standards and functions correctly.
  
- **Unit Tests**: Develop unit tests for any new functionality or improvement. This will help catch errors and improve the project's stability.
  
- **Training Sessions**: For new contributors, we offer training sessions on how to contribute to the project, how to clone and work with the repository, and how to run the bot locally.
  
- **Style Guide**: Refer to the style guide to ensure the code is clear and consistent with the rest of the project. This includes guidelines for code documentation, function names, and commit formats.

---

## How to Contribute

1. **Fork** the repository.

2. **Clone your fork locally**:

    ```bash
    git clone https://github.com/FranciscoLG241/TriviaBot.git
    cd TriviaBot
    ```

3. **Create a branch** for your contribution:

    ```bash
    git checkout -b my-improvement
    ```

4. Make the necessary changes and **write tests** if applicable.

5. **Make clear and concise commits**:

    ```bash
    git commit -m "Add new scoring functionality"
    ```

6. **Push to your fork**:

    ```bash
    git push origin my-improvement
    ```

7. **Open a Pull Request** on the original repository.

---

## Code Style

- Use **Python 3.8** or higher.
- Follow the **Python style guide (PEP8)**.
- **Document functions** with docstrings.
- Use **descriptive names** for functions and variables.

---

## Reporting Bugs or Suggestions

You can open an **issue** to:

- Report bugs.
- Suggest improvements or new features.
- Ask for help or clarification.

---
