import discord
import json
import random
import asyncio

TOKEN = "MTM0Nzg4ODE3NTUxODk3ODA2OA.GcOpqJ.8KOvdsftDE8GY8MFLSRXaU687WPcevx_NTn_0A" 

intents = discord.Intents.default()
intents.message_content = True 
client = discord.Client(intents=intents)


def cargar_preguntas():
    with open("preguntas.json", "r", encoding="utf-8") as file:
        return json.load(file)

preguntas = cargar_preguntas()

@client.event
async def on_ready():
    print(f"✅ Bot conectado como {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == "!trivia":
        pregunta = random.choice(preguntas)
        pregunta_texto = pregunta["pregunta"]
        respuesta_correcta = pregunta["respuesta"].lower()

        await message.channel.send(f"🎲 Trivia: {pregunta_texto}\nTienes 10 segundos para responder.")

        def check(m):
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
