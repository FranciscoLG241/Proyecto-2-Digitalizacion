## Ciclo de vida del dato (5b)
1. ¿Cómo se gestionan los datos desde su generación hasta su eliminación en tu proyecto?
- En el caso de TriviaBot, los datos generados están principalmente relacionados con las preguntas de trivia y las respuestas de los usuarios. 
El ciclo de vida de estos datos es el siguiente:

- Generación de los datos: Los datos se generan cuando el bot carga el archivo preguntas.json que contiene las preguntas y respuestas de trivia. 
Estos datos son leídos cada vez que el bot selecciona una pregunta aleatoria.

- Uso de los datos: Cuando un usuario ejecuta el comando !trivia, el bot selecciona una pregunta de los datos y la presenta al usuario. 
Luego, espera la respuesta del usuario y compara esta respuesta con la correcta.

- Eliminación de los datos: Los datos relacionados con las respuestas no se almacenan de forma persistente en el sistema. Una vez que la 
pregunta se responde (correcta o incorrecta), la interacción termina y no se conserva un historial de respuestas.

---
## Almacenamiento en la nube (5f)
3. Si no usas la nube, ¿cómo podrías integrarla en futuras versiones?
- En futuras versiones, se podría considerar el uso de Firebase para almacenar datos de usuarios, historial de respuestas y puntuaciones, 
lo que permitiría una funcionalidad de clasificación y estadísticas personalizadas. También se podría integrar con bases de datos en la 
nube como MongoDB o AWS DynamoDB si se necesitara almacenar grandes volúmenes de datos de manera eficiente.

---

## Seguridad y regulación (5i)
3. Si no implementaste medidas de seguridad, ¿qué riesgos potenciales identificas y cómo los abordarías en el futuro?
- El principal riesgo sería que, en una versión futura que maneje información personal, los datos podrían ser manipulados
o expuestos. Para mitigar este riesgo, se implementaría cifrado de datos, autenticación de usuarios y validación exhaustiva de los datos.

---

## Implicación de las THD en negocio y planta (2e)
3. Si tu proyecto no aplica directamente a negocio o planta, ¿qué otros entornos podrían beneficiarse?
- TriviaBot podría beneficiar principalmente a entornos educativos o de formación, ayudando a estudiantes a repasar conceptos y a mejorar
su aprendizaje mediante una forma divertida y entretenida.

---

## Mejoras en IT y OT (2f)
3. Si no aplica a IT u OT, ¿cómo podrías adaptarlo para mejorar procesos tecnológicos concretos?
- TriviaBot podría integrarse con plataformas de educación en línea como Moodle o Google Classroom. El bot podría hacer preguntas sobre
el contenido de los cursos, exámenes o evaluaciones de los estudiantes, proporcionando una manera interactiva y divertida de repasar temas.
Además, ayudaría a los estudiantes a mejorar su comprensión del material y a mantenerse comprometidos con el proceso de aprendizaje.

---

## Tecnologías Habilitadoras Digitales (2g)
1. ¿Qué tecnologías habilitadoras digitales (THD) has utilizado o podrías integrar en tu proyecto?
- En este caso, TriviaBot hace uso de tecnologías habilitadoras digitales simples, como la automatización de interacciones a través de Discord
y la interacción en tiempo real utilizando APIs de Discord. Para enriquecer un poco mas el bot, se podrían integrar THD como el aprendizaje automático
para adaptar las preguntas según el nivel de conocimiento del usuario, o incluso procesamiento de lenguaje natural para interpretar las
respuestas de los usuarios y hacer el bot aún más interactivo.









