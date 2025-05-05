# **Wiki de TriviaBot**

## **Documentación Técnica**

### **Arquitectura del Proyecto**

TriviaBot está desarrollado en **Python 3.8+** y utiliza la librería `discord.py` para interactuar con la API de Discord. El bot permite a los usuarios jugar a un juego de trivia dentro de un servidor de Discord, con preguntas seleccionadas de un archivo JSON. La arquitectura es simple y se basa en tres componentes principales:

1. **Comando de trivia (`!trivia`)**: Los usuarios pueden invocar este comando en el servidor para que el bot seleccione una pregunta al azar.
2. **Gestión del tiempo**: El bot espera 10 segundos para que el usuario responda.
3. **Evaluación de respuesta**: El bot compara la respuesta del jugador con la correcta y responde de acuerdo al resultado: felicitaciones por la respuesta correcta o la respuesta correcta si el tiempo se agotó o la respuesta fue incorrecta.

### **Tecnologías y Librerías Utilizadas**
- **Python 3.8+**: El lenguaje de programación utilizado para desarrollar el bot.
- **discord.py**: Librería para interactuar con la API de Discord y manejar la lógica del bot.
- **JSON**: Usado para almacenar las preguntas y respuestas del juego, permitiendo una fácil personalización.

### **Flujo de Datos**
1. **Entrada del usuario**: El jugador utiliza el comando `!trivia` en un canal de Discord.
2. **Selección de la pregunta**: El bot selecciona una pregunta aleatoria de un archivo `preguntas.json`.
3. **Interacción**: El bot espera 10 segundos para la respuesta del usuario.
4. **Evaluación**: Se evalúa la respuesta y el bot responde, felicitando al jugador si la respuesta es correcta o mostrando la correcta si no lo es.

### **Estructura del Proyecto**
- **bot.py**: El archivo principal que maneja la lógica del bot y las interacciones con Discord.
- **preguntas.json**: Contiene las preguntas y respuestas en formato JSON. Es el archivo que el bot lee para obtener las preguntas.
- **config.py** (opcional): Para futuras configuraciones adicionales como la clave de API o ajustes del bot.

### **Instrucciones de Instalación**
1. **Clonar el repositorio**:
    ```bash
    git clone https://github.com/FranciscoLG241/TriviaBot.git
    ```
2. **Instalar dependencias**:
    ```bash
    pip install discord
    ```
3. **Configurar el bot**:
   - Ve al [Discord Developer Portal](https://discord.com/developers/applications).
   - Crea una nueva aplicación y habilita el bot.
   - Obtén el **token de bot** y reemplaza la variable `TOKEN` en el archivo `bot.py` con el token de tu bot.
   - Personaliza el archivo `preguntas.json` con las preguntas y respuestas para el juego.

4. **Ejecutar el bot**:
    ```bash
    python bot.py
    ```
   El bot estará activo y listo para recibir comandos en tu servidor de Discord.

---

## **Devlog**

### **1º Fase**
- **Objetivo estratégico**: Crear un bot funcional para jugar a trivia en servidores de Discord.
- **Cambios realizados**:
  - Creación del repositorio y desarrollo de la funcionalidad básica del bot.
  - El bot responde a comandos `!trivia` y elige una pregunta aleatoria del archivo `preguntas.json`.
  - El bot permite a los jugadores responder dentro de un límite de 10 segundos.
  - Implementación de una respuesta al jugador, ya sea felicitaciones por la respuesta correcta o mostrando la respuesta correcta en caso de error o tiempo agotado.
- **Motivación**: Proporcionar una forma sencilla y divertida de interactuar dentro de los servidores de Discord.

---

### **2º Fase**
- **Objetivo estratégico**: Mejorar la experiencia del usuario.
- **Cambios realizados**:
  - Se agregaron más preguntas y respuestas al archivo `preguntas.json`.
  - Mejorado el manejo de errores si el archivo `preguntas.json` está mal formado o no existe.
- **Motivación**: Ampliar la variedad de preguntas y mejorar la robustez del sistema frente a posibles fallos en los datos.

---

### **3º Fase**
- **Objetivo estratégico**: Mejorar la documentación y facilitar las contribuciones.
- **Cambios realizados**:
  - Se documentó el código con comentarios y docstrings.
  - Se añadió un archivo `CONTRIBUTING.md` que proporciona guías para nuevos colaboradores.
  - Se realizó la primera publicación del código en GitHub con una versión inicial.
- **Motivación**: Facilitar que otros desarrolladores contribuyan al proyecto y mejorar la mantenibilidad del código.

---

### **4º Fase**
- **Objetivo estratégico**: Ampliar la flexibilidad y personalización del bot.
- **Cambios realizados**:
  - Añadido soporte para que los administradores de los servidores puedan personalizar las preguntas del bot editando el archivo `preguntas.json`.
  - Se incluyó una pequeña guía en la Wiki sobre cómo agregar preguntas personalizadas.
- **Motivación**: Permitir que los usuarios personalicen el juego según sus preferencias y agregar más interactividad al bot.

---

## **Futuras Mejoras (Propuestas)**

1. **Integración con APIs externas**: Conectar TriviaBot con bases de datos de trivia externas como la [Open Trivia Database](https://opentdb.com/) para obtener preguntas más actualizadas y diversas sin necesidad de editar el archivo `preguntas.json` manualmente.
2. **Soporte multilingüe**: Añadir soporte para múltiples idiomas, permitiendo que el bot sea utilizado en diferentes regiones y comunidades.
3. **Sistema de puntuación**: Implementar un sistema de puntuación donde los jugadores acumulen puntos por respuestas correctas, y mostrar clasificaciones generales.
4. **Más opciones de personalización**: Permitir a los administradores configurar no solo las preguntas, sino también el límite de tiempo o la dificultad de las preguntas.

---

### **Changelog**
- **1º Fase**: Versión inicial del bot.
- **2º Fase**: Ampliación de preguntas y mejoras en el manejo de errores.
- **3º Fase**: Documentación del código y publicación en GitHub.
- **4º Fase**: Añadida la personalización de preguntas.



