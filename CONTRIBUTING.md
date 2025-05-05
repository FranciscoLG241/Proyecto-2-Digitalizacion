# Guía de Contribución a TriviaBot

¡Gracias por tu interés en contribuir a TriviaBot! Este proyecto es open source y está abierto a mejoras de la comunidad.

## Objetivo Actual del Software

TriviaBot es una herramienta de trivia interactiva diseñada para ser usada en servidores de Discord. Su propósito es proporcionar a los usuarios una forma entretenida de interactuar entre sí a través de preguntas y respuestas de trivia. El bot selecciona aleatoriamente una pregunta, permite a los usuarios responder dentro de un tiempo limitado y brinda retroalimentación según la respuesta del usuario. Este software cubre las necesidades actuales de entretenimiento dentro de comunidades de Discord, promoviendo la participación y el aprendizaje de manera divertida.

---

## Necesidades Futuras y Mejoras Propuestas

A medida que el proyecto crece, se identifican varias necesidades que podrían expandir su funcionalidad y aumentar su impacto:

### Mejoras de Funcionalidad
- **Ampliar el conjunto de preguntas**: Actualmente, el bot se basa en un archivo JSON local para las preguntas. Se podría integrar una API de trivia en línea para obtener preguntas dinámicas y actualizadas.
- **Soporte multilingüe**: Permitir que el bot sea utilizado en diferentes idiomas para llegar a una audiencia más amplia.
- **Clasificación y puntuación**: Añadir un sistema de puntuación para llevar el registro de las mejores puntuaciones y fomentar la competencia entre los jugadores.
- **Personalización de preguntas**: Permitir a los administradores de servidores crear sus propias preguntas de trivia desde una interfaz fácil de usar.

---

## Interacción de los Sistemas y Datos

El bot funciona de manera autónoma dentro de un servidor de Discord. Los principales componentes del sistema son:

1. **Comando de trivia (`!trivia`)**: Los usuarios pueden invocar el bot en cualquier canal con el comando `!trivia`. Esto genera una interacción donde el bot selecciona una pregunta aleatoria de un archivo JSON local.
2. **Respuesta del usuario**: Los usuarios tienen 10 segundos para responder a la pregunta. El bot verifica la respuesta utilizando una función que compara la entrada del usuario con la respuesta correcta.
3. **Retroalimentación**: Si la respuesta es correcta, el bot felicita al usuario; si es incorrecta o el tiempo se agota, muestra la respuesta correcta.

### Ejemplo de flujo de datos:
1. **Entrada**: Usuario ejecuta `!trivia`.
2. **Procesamiento**: El bot selecciona una pregunta aleatoria desde el archivo `preguntas.json` y espera una respuesta durante 10 segundos.
3. **Salida**: El bot responde con un mensaje de felicitaciones o muestra la respuesta correcta.

### Estructura de Datos:
El archivo `preguntas.json` contiene una lista de objetos con preguntas y respuestas en formato JSON:

```json
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

## Propuestas para Mejorar la Interoperabilidad

El bot actualmente depende de datos estáticos (el archivo `preguntas.json`) para funcionar. Aquí hay algunas propuestas para mejorar la interoperabilidad:

- **Integración con APIs externas de trivia**: Esto permitiría que el bot pueda obtener preguntas actualizadas y diversificadas de forma dinámica sin necesidad de actualizar el archivo manualmente. Ejemplos incluyen la [Open Trivia Database](https://opentdb.com/) o [JService](https://jservice.io/).
  
- **Interacción con otras plataformas de chat**: En el futuro, TriviaBot podría expandirse a otras plataformas de mensajería como **Slack** o **Telegram** para ofrecer soporte a una comunidad más amplia.

---

## Habilidades Necesarias para Contribuir

Para contribuir a TriviaBot, se recomienda tener experiencia con las siguientes habilidades y tecnologías:

- **Python 3.8+**: El bot está desarrollado en Python, por lo que es fundamental tener conocimientos de este lenguaje.
  
- **Discord API**: Familiaridad con la librería `discord.py` para interactuar con la API de Discord.
  
- **Manejo de JSON**: Habilidad para trabajar con archivos JSON, ya que el bot depende de este formato para almacenar las preguntas de trivia.

---

## Estrategias de Capacitación para Colaboradores

Si deseas contribuir o convertirte en colaborador activo del proyecto, aquí te dejamos algunas estrategias para facilitar el proceso de integración:

- **Documentación Interna**: Asegúrate de leer la documentación interna del código y las guías de estilo de Python. Esto ayudará a que tu código siga las mismas convenciones que el proyecto.
  
- **Revisión de Código**: Los nuevos colaboradores deben someter sus cambios a revisión a través de un Pull Request. Esto garantiza que el código cumple con los estándares de calidad y funciona correctamente.
  
- **Pruebas Unitarias**: Desarrolla pruebas unitarias para cualquier nueva funcionalidad o mejora. Esto facilitará la detección de errores y mejorará la estabilidad del proyecto.
  
- **Sesiones de Capacitación**: Para los colaboradores nuevos, ofrecemos sesiones de capacitación sobre cómo contribuir al proyecto, cómo clonar y trabajar con el repositorio, y cómo ejecutar el bot localmente.
  
- **Guía de Estilo**: Consulta la guía de estilo para garantizar que el código sea claro y consistente con el resto del proyecto. Aquí se incluyen pautas para la documentación del código, los nombres de funciones, y el formato de los commits.

---

## ¿Cómo Contribuir?

1. **Haz un fork** del repositorio.

2. **Clona tu fork localmente**:

    ```bash
    git clone https://github.com/FranciscoLG241/TriviaBot.git
    cd TriviaBot
    ```

3. **Crea una rama** para tu contribución:

    ```bash
    git checkout -b mi-mejora
    ```

4. Realiza los cambios necesarios y **escribe tests** si aplica.

5. **Haz commits claros y concisos**:

    ```bash
    git commit -m "Agrega nueva funcionalidad de puntuación"
    ```

6. **Haz push a tu fork**:

    ```bash
    git push origin mi-mejora
    ```

7. **Abre un Pull Request** en el repositorio original.

---

## Estilo de código

- Usa **Python 3.8** o superior.
- Sigue la **guía de estilo de Python (PEP8)**.
- **Documenta funciones** con docstrings.
- Usa **nombres descriptivos** para funciones y variables.

---

## Reportar errores o sugerencias

Puedes abrir un **issue** para:

- Informar de errores.
- Sugerir mejoras o nuevas funcionalidades.
- Pedir ayuda o clarificación.

---
