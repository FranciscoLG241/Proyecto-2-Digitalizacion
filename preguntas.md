## Ciclo de vida del dato (5b)
1. ¿Cómo se gestionan los datos desde su generación hasta su eliminación en tu proyecto?
En el caso de TriviaBot, los datos generados están principalmente relacionados con las preguntas de trivia y las respuestas de los usuarios. 
El ciclo de vida de estos datos es el siguiente:

- Generación de los datos: Los datos se generan cuando el bot carga el archivo preguntas.json que contiene las preguntas y respuestas de trivia. 
Estos datos son leídos cada vez que el bot selecciona una pregunta aleatoria.

- Uso de los datos: Cuando un usuario ejecuta el comando !trivia, el bot selecciona una pregunta de los datos y la presenta al usuario. 
Luego, espera la respuesta del usuario y compara esta respuesta con la correcta.

- Eliminación de los datos: Los datos relacionados con las respuestas no se almacenan de forma persistente en el sistema. Una vez que la 
pregunta se responde (correcta o incorrecta), la interacción termina y no se conserva un historial de respuestas.
