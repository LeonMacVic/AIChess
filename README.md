# AIChess

### Autonomous Chess Engine & Reinforcement Learning Project

AIChess es un proyecto personal cuyo objetivo es desarrollar desde cero un motor de ajedrez autónomo, capaz de analizar posiciones, tomar decisiones estratégicas y mejorar progresivamente mediante técnicas de inteligencia artificial y aprendizaje por refuerzo (*Reinforcement Learning*).

El proyecto busca combinar algoritmia, desarrollo de software, aprendizaje automático y optimización computacional, siguiendo una metodología de desarrollo incremental y pruebas automatizadas.

## Objetivos del proyecto

- Desarrollar un motor de ajedrez autónomo.
- Implementar algoritmos de búsqueda como Minimax, poda alfa-beta y Monte Carlo Tree Search (MCTS).
- Diseñar redes neuronales propias utilizando PyTorch.
- Implementar un sistema de entrenamiento autónomo mediante *self-play*.
- Evaluar el rendimiento del motor y su evolución mediante partidas automatizadas y métricas Elo.
- Optimizar el rendimiento computacional del motor.
- Desarrollar una interfaz web interactiva para jugar contra AIChess.

## Tecnologías

### Tecnologías actuales
- **Python 3.12:** lenguaje principal de desarrollo.
- **python-chess:** gestión del tablero, movimientos legales y reglas del ajedrez.
- **Git y GitHub:** control de versiones y documentación.

### Tecnologías previstas
- **PyTorch:** desarrollo y entrenamiento de redes neuronales.
- **C++:** optimización de algoritmos críticos.
- **FastAPI:** desarrollo de la API del motor.
- **React y TypeScript:** interfaz web.
- **Docker:** contenedorización.
- **MLflow:** seguimiento de experimentos y modelos.

## Estado actual

**Versión 0.1 — Motor autónomo básico**

Funcionalidades implementadas:

- Representación del tablero.
- Generación y ejecución de movimientos legales.
- Identificación de turnos y resultados.
- Selección aleatoria de movimientos.
- Simulación autónoma de partidas completas.
- Límite de movimientos para controlar la ejecución.

El motor todavía no incorpora una función de evaluación estratégica ni aprendizaje automático.

## Hoja de ruta

- [x] Configuración del entorno Python.
- [x] Implementación del tablero y movimientos legales.
- [x] Desarrollo de un agente autónomo básico.
- [x] Configuración de Git y GitHub.
- [ ] Función de evaluación de posiciones.
- [ ] Algoritmo Minimax y poda alfa-beta.
- [ ] Pruebas automatizadas.
- [ ] Red neuronal de evaluación.
- [ ] Monte Carlo Tree Search.
- [ ] Entrenamiento mediante self-play.
- [ ] Optimización de rendimiento.
- [ ] Interfaz web y API.

## Metodología

El proyecto se desarrolla incrementalmente. Cada versión incorpora nuevas funcionalidades y se registra mediante Git.

El rendimiento del motor se evaluará mediante pruebas, experimentos reproducibles y partidas contra versiones anteriores y motores de referencia.

## Autor

León Macías Vicente