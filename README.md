# TriviaBot

**TriviaBot** es un bot de Discord que permite a los usuarios jugar a un juego de trivia directamente en su servidor de Discord. El bot selecciona una pregunta al azar y le da al usuario 10 segundos para responder correctamente. Si la respuesta es correcta, el bot felicita al jugador; si no, muestra la respuesta correcta.

Este bot está diseñado en **Python** usando la librería `discord.py` y funciona de forma sencilla y eficiente en cualquier servidor de Discord.

---

## Funcionalidades

- Responde al comando `!trivia` con una pregunta de trivia.
- Los jugadores tienen 10 segundos para responder a cada pregunta.
- Si la respuesta es correcta, el bot felicita al jugador.
- Si la respuesta es incorrecta o el tiempo se agota, el bot muestra la respuesta correcta.
  
## Tecnologías usadas

- **Python**: Lenguaje de programación utilizado para desarrollar el bot.
- **discord.py**: Librería de Python que facilita la interacción con la API de Discord.
- **asyncio**: Librería de Python para manejar tareas asincrónicas, como esperar respuestas de los usuarios.

---

## Instalación

### 1. Clona este repositorio

Para obtener una copia del proyecto, clónalo en tu máquina local:

```bash
https://github.com/FranciscoLG241/Proyecto-2-Digitalizacion.git
```

---


### 2. Instala las dependencias
Para instalar las librerías necesarias, usa pip:

```bash
pip install discord asyncio
```

---

### 3. Obtén el token de tu bot
Para que el bot funcione, necesitarás un token de bot de Discord. Si aún no tienes uno, sigue estos pasos:

1. Ve a Discord Developer Portal.
2. Crea una nueva aplicación y habilita el bot.
3. Copia el token que te proporciona Discord para tu bot.

---

### 4. Configura el bot
- Abre el archivo bot.py en un editor de texto.
Reemplaza la línea TOKEN = "tu_token_aqui" con el token de tu bot que copiaste en el paso anterior:

```bash
TOKEN = "tu_token_aqui"
```

### 5. Configura las preguntas de trivia
El bot utiliza un archivo preguntas.json para almacenar las preguntas y respuestas. Asegúrate de que tu archivo preguntas.json contenga preguntas en formato JSON como este ejemplo:

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
- Puedes agregar más preguntas en el mismo formato para que el bot tenga variedad.

---

### Ejecución
Una vez que hayas configurado el bot, puedes ejecutarlo con el siguiente comando:

```bash
python bot.py
```
El bot se conectará a Discord y estará listo para usar. El bot buscará el comando !trivia en los canales donde tenga permisos.

---

### Uso
- Comando: !trivia
- Descripción: El bot elegirá una pregunta al azar y dará 10 segundos para que el jugador responda. Si la respuesta es correcta, se felicita al jugador, y si es incorrecta o el tiempo se agota, se muestra la respuesta correcta.
- Invitar al bot a tu servidor
- Si deseas que TriviaBot se una a tu servidor, sigue estos pasos:

1. Ve al Discord Developer Portal.
2. Selecciona tu aplicación de bot.
3. En la sección de OAuth2, selecciona bot en los "scopes".
4. En "permissions", marca los permisos que el bot necesita, como Enviar mensajes, Leer mensajes, etc.
5. Copia el enlace generado y pégalo en tu navegador para invitar al bot a tu servidor.











