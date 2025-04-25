# Curso de LangGraph

Este repositorio contiene una colección de cuadernos Jupyter y proyectos de apoyo que muestran la funcionalidad de **LangGraph**, una biblioteca de Python para construir y gestionar agentes con flujos de trabajo basados en gráficos.

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
