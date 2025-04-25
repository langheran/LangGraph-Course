# Curso de LangGraph

Este repositorio contiene una colección de cuadernos Jupyter y proyectos de apoyo que muestran la funcionalidad de **LangGraph**, una biblioteca de Python para construir y gestionar agentes con flujos de trabajo basados en gráficos.

## Tabla de Contenido

Slide | Título / Tema Principal | Contenido Detallado
-|-|-
1 | ¿Por qué aprender LangGraph y de este instructor? | Introducción a los agentes de IA como tendencia clave en 2025. Relevancia de aprender LangGraph. Credenciales del instructor con experiencia real en producción.
2 | Qué cubre el curso (y qué no) | Enfoque en LangGraph con herramientas open-source. No se cubre la plataforma comercial de LangGraph. Despliegue con FastAPI, Docker, y soluciones autohospedadas.
3 | Prerrequisitos del curso | Nivel intermedio de Python, experiencia previa con LangChain, conocimientos básicos de ingeniería de software, Git, terminal y (opcionalmente) Docker.
4 | ¿Por qué se creó LangGraph? | Crítica a diseños monolíticos (God classes). Limitaciones de LangChain Expression Language (LCL). Ventajas de LangGraph como arquitectura modular.
5 | Filosofía de diseño de LangGraph | Introducción al uso de máquinas de estado. Componentes: nodos, aristas, y estado compartido. Ventajas de modularidad, mantenibilidad y claridad.
6 | Configuración del entorno local | Clonación del repositorio, instalación de dependencias, configuración del entorno virtual y API Key de OpenAI. Preparación del entorno para usar notebooks.
7 | TypedDict vs Pydantic | Comparación entre estructuras de datos: diferencias en validación estática y en tiempo de ejecución. Uso de mypy y validación con Pydantic.
8 | Primer gráfico simple con LangGraph | Creación de un grafo básico sin LLM. Explicación de nodos, estado y conexiones. Ejecución y visualización con Mermaid.
9 | ¿Por qué usar LangGraph en lugar de solo LCL? | Comparación entre LCL y LangGraph. Cuándo conviene usar cada uno. Integración de ambos en flujos más complejos.
10 | Flujo cíclico y condicional en LangGraph | Ejemplo de grafo con lógica condicional y bucles. Uso de funciones enrutadoras para controlar el flujo basado en el estado.
11 | Uso de reductores en el estado | Aplicación de funciones reductoras (reducer) en claves específicas del estado. Uso de Annotated para acumular datos automáticamente.
12 | Estado alternativo con Pydantic | Uso de Pydantic como alternativa a TypedDict para validación en tiempo de ejecución. Diferencias de acceso a atributos.
13 | Introducción a tool calling | Definición y propósito. Cómo los LLM generan argumentos para herramientas, y el usuario ejecuta la lógica real.
14 | Tool calling básico con LangChain | Uso del decorador @tool, definición de herramientas personalizadas, enlace con LLM, análisis del flujo de mensajes.
15 | Primer agente basado en LLM | Construcción de un agente LangGraph que usa herramientas. Uso de tool_node, rutas condicionales, y persistencia de mensajes.
16 | Persistencia de estado con checkpointing | Introducción al uso de MemorySaver para almacenar el historial de conversación. Uso de thread_id en la configuración del grafo.
17 | Teoría de RAG (Retrieval-Augmented Generation) | Explicación conceptual de RAG: etapas de indexación y recuperación, embedding, y flujo de datos para generar respuestas enriquecidas.
18 | Ejemplo práctico de RAG | Embedding de documentos sobre un restaurante ficticio. Uso de ChromaDB como vector store. Creación de prompt contextual.
19 | Primer agente RAG con clasificación | Construcción de un agente que decide si una pregunta es “on topic” o no. Flujo condicional con recuperación de información solo si es relevante.
20 | RAG con herramientas (tool calling) | Alternativa al enfoque anterior: convertir el retriever en una herramienta. Ventajas y desventajas de usar tool calling para RAG.
21 | Diseño de un agente conversacional complejo | Agente completo con múltiples componentes: reescritura de preguntas, clasificación, recuperación, validación de documentos, y generación final de respuestas.
22 | Implementación del agente conversacional con memoria | Implementación completa del agente descrito en el slide 21. Uso de checkpointers, múltiples nodos, y lógica cíclica controlada para reintentos de recuperación.
23 | Reducción del estado visible | Enseña a separar el estado en partes: input, intermedio y output. Esto permite ocultar información innecesaria y enfocarse solo en lo relevante como la respuesta final del LLM​.
24 | Configuración dinámica en tiempo de ejecución | Explica cómo hacer que el comportamiento del grafo sea configurable en tiempo de ejecución (por ejemplo, cambiar idioma del modelo sin recompilar) usando RunnableConfig​.
25 | Human-in-the-loop: introducción | Introduce flujos con intervención humana usando checkpointers, interrupt_before, y command class. Se muestra un ejemplo con herramientas y un chatbot que requiere confirmación antes de usar herramientas​.
26 | Human-in-the-loop: concepto | Justificación de por qué se necesitan flujos con humanos en el lazo: para mayor precisión en escenarios sensibles como cumplimiento, toma de decisiones o generación de contenido​.
27 | Time Travel y edición de estado | Introducción a la función de “viaje en el tiempo” que permite modificar la ejecución pasada del grafo. Se usa para simular respuestas, corregir errores o cambiar decisiones en ejecución​.
28 | Time Travel y edición de estado | Se presenta cómo interrumpir la ejecución de un grafo y modificar el estado con la técnica de "viaje en el tiempo", útil para corregir o reanudar flujos​.
29 | Streaming y ejecución asíncrona | Muestra cómo ejecutar grafos de forma asíncrona y cómo hacer streaming de respuestas del LLM en tiempo real, incluyendo token por token​.
30 | Ejecución paralela | Se construye un grafo con nodos que se ejecutan en paralelo y cuyos resultados se combinan. Útil para acelerar procesos que no dependen entre sí​.
31 | Diseño de grafos de producción | Introducción a prácticas de software como modularidad, ejecución paralela, y uso de subgrafos para lograr sistemas escalables y mantenibles​.
32–34 | [No tienen títulos explícitos, forman parte del desarrollo técnico del punto anterior] | Explicaciones detalladas sobre implementación de los subgrafos, ejecución condicional y rutas de errores. Ejemplos paso a paso.
35 | Introducción a subgrafos | Se describe cómo dividir un sistema complejo en componentes reutilizables con subgrafos. Útil para agentes especializados​.
36 | Introducción a sistemas multi-agente | Justificación del uso de múltiples agentes: planificación, toma de decisiones, especialización de tareas. Se presentan varios patrones de diseño​.
37 | Patrones de arquitectura multi-agente | Explicación de diferentes estructuras: agente único, red descentralizada, supervisor, jerárquico, supervisor como herramienta, flujo personalizado​.
38 | Caso de uso: agencia de noticias deportivas | Se diseña un sistema multi-agente para procesar artículos de fútbol: clasificación, verificación de datos, generación de texto final​.
39 | Human-in-the-loop para publicación de artículos | Se añade revisión humana antes de publicar artículos. Se usa el grafo del supervisor y checkpoints para validar el contenido​.
40 | De notebook a aplicación real | Transición de notebooks a aplicaciones de producción usando API con FastAPI, Postgres para persistencia, y Docker para despliegue​.
41 | Estructura de la aplicación Fullstack | Explicación de los servicios en docker-compose: backend con FastAPI y LangGraph, base de datos Postgres, y frontend en Angular​.
42 | Interacción en la UI y revisión humana | Demostración de cómo un humano puede aprobar, editar o rechazar artículos antes de publicarlos desde una interfaz gráfica conectada al backend​.
43 | Memoria a corto y largo plazo | Introducción a la memoria en agentes. Diferencias entre memoria por sesión (checkpoints) y memoria persistente (almacenamiento a largo plazo)​.
44 | Implementación de memoria persistente | Uso del objeto store para recordar información entre sesiones y mejorar la continuidad de las conversaciones​.
45 | Recuperación de memoria cruzada | Cómo hacer que agentes recuerden detalles pasados usando memoria de largo plazo. Demostración con usuarios y preferencias personales.
46 | Cierre y próximos pasos | Conclusiones del curso. Revisión de habilidades aprendidas. Invitación a seguir explorando LangGraph en producción.

## Cuadernos

- **00_TypedDict.ipynb**
  Explicación de las diferencias entre `TypedDict` y Pydantic para la gestión del estado.

- **Basics.ipynb**
  Introducción a los conceptos básicos de LangGraph, incluyendo cómo construir flujos de trabajo de agentes sencillos.

- **Tool_calling_basics.ipynb**
  Demuestra cómo permitir que los agentes llamen a herramientas de manera efectiva dentro de LangChain (¡no LangGraph!).

- **Agent_basics.ipynb**
  Explora las características fundamentales de la creación y gestión de agentes utilizando LangGraph.

- **RAG_Basics.ipynb**
  Visión general de los conceptos básicos de Generación Aumentada por Recuperación (RAG) con LangGraph.

- **RAG_Agent.ipynb**
  Implementación de un agente que aprovecha RAG para una recuperación de información mejorada.

- **RAG_Agent_with_memory.ipynb**
  Muestra cómo extender un agente RAG con capacidades de memoria para respuestas contextuales.

- **Advanced_State.ipynb**
  Técnicas avanzadas para la gestión de estados de agentes dentro de los flujos de trabajo de LangGraph.

- **Human_in_the_Loop.ipynb**
  Incorpora la entrada humana en los flujos de trabajo de LangGraph para la toma de decisiones guiada.

- **ParallelExecution.ipynb**
  Demuestra la ejecución paralela de nodos en LangGraph para un procesamiento eficiente.

- **AsyncAndStreaming.ipynb**
  Explora la ejecución asíncrona y las salidas en streaming en los flujos de trabajo de LangGraph.

- **Subgraphs.ipynb**
  Ilustra cómo utilizar subgrafos para modularizar y reutilizar partes de un flujo de trabajo.

- **Agent_Patterns.ipynb**
  Muestra patrones de diseño de agentes comunes y plantillas reutilizables.

- **LongTermMemory.ipynb**
  Implementa la funcionalidad de memoria a largo plazo en agentes utilizando LangGraph.

## Contenido Adicional

### unit_tests

**Descripción**: Demuestra cómo probar aplicaciones de LangGraph de manera efectiva.

- Incluye ejemplos de pruebas unitarias para los nodos de LangGraph.

### fullstackapp

**Descripción**: Proyecto final que demuestra la integración de una aplicación completa con un flujo de trabajo con participación humana.

- **Frontend**: Construido con Angular.
- **Backend**: Construido con FastAPI (¡asíncrono!).
- **Base de datos**: PostgreSQL.
