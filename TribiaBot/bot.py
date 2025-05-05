import discord
import json
import random
import asyncio

TOKEN = "MTM0Nzg4ODE3NTUxODk3ODA2OA.G4KmvF.qGBlzxvpxTy1m1_w_vrOFRYIdL5EF4ro8MqbBU"  # Pega aquí el token de tu bot

intents = discord.Intents.default()
intents.message_content = True  # Habilita la lectura de mensajes
client = discord.Client(intents=intents)

# Cargar preguntas desde JSON
def cargar_preguntas():
    """
    Carga las preguntas de trivia desde un archivo JSON.

    Abre el archivo preguntas.json, lee su contenido y lo devuelve como una lista de diccionarios.

    Returns:
        list: Lista de preguntas de trivia en formato diccionario, cada uno con una clave 'pregunta' y 'respuesta'.
    """
    with open("preguntas.json", "r", encoding="utf-8") as file:
        return json.load(file)

preguntas = cargar_preguntas()

@client.event
async def on_ready():
    """
    Evento que se ejecuta cuando el bot se conecta correctamente a Discord.

    En este evento, el bot imprime un mensaje indicando que está listo para recibir comandos.
    """
    print(f"✅ Bot conectado como {client.user}")

@client.event
async def on_message(message):
    """
    Evento que se ejecuta cuando el bot recibe un mensaje.

    Si el mensaje es el comando '!trivia', el bot selecciona una pregunta aleatoria
    y espera 10 segundos para que el usuario responda.

    Args:
        message (discord.Message): El mensaje recibido por el bot.
    """
    if message.author == client.user:
        return

    if message.content.lower() == "!trivia":
        pregunta = random.choice(preguntas)
        pregunta_texto = pregunta["pregunta"]
        respuesta_correcta = pregunta["respuesta"].lower()

        await message.channel.send(f"🎲 Trivia: {pregunta_texto}\nTienes 10 segundos para responder.")

        def check(m):
            """
            Función de verificación para asegurarse de que el mensaje recibido
            es del autor correcto y en el canal correcto.

            Args:
                m (discord.Message): El mensaje que se va a verificar.

            Returns:
                bool: True si el mensaje es del autor correcto y en el canal correcto, False en caso contrario.
            """
            return m.author == message.author and m.channel == message.channel
        
        try:
            msg = await client.wait_for("message", timeout=10.0, check=check)
            if msg.content.lower() == respuesta_correcta:
                await message.channel.send("✅ ¡Correcto! 🎉")
            else:
                await message.channel.send(f"❌ Incorrecto. La respuesta era: **{respuesta_correcta}**")
        except asyncio.TimeoutError:
            await message.channel.send(f"⏳ Tiempo agotado. La respuesta era: **{respuesta_correcta}**")

client.run(TOKEN)
