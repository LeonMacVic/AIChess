# AIChess

### Motor de ajedrez autónomo basado en inteligencia artificial y aprendizaje por refuerzo

AIChess es un proyecto personal cuyo objetivo es desarrollar progresivamente un motor de ajedrez autónomo, capaz de analizar posiciones, tomar decisiones estratégicas y mejorar su nivel de juego mediante técnicas de inteligencia artificial y aprendizaje por refuerzo (*Reinforcement Learning*).

El proyecto combina algoritmia, ingeniería del software, aprendizaje automático y optimización computacional. Su desarrollo se realiza de forma incremental, incorporando nuevas funcionalidades, pruebas y mejoras en cada versión.

## 1. Objetivos del proyecto

- Desarrollar un motor de ajedrez capaz de jugar partidas completas de manera autónoma.
- Implementar algoritmos de búsqueda como Minimax, poda alfa-beta y Monte Carlo Tree Search (MCTS).
- Diseñar y entrenar redes neuronales mediante PyTorch.
- Incorporar aprendizaje por refuerzo mediante partidas contra sí mismo (*self-play*).
- Evaluar el rendimiento del motor mediante pruebas automatizadas y estimaciones de Elo.
- Optimizar el uso de CPU, GPU y memoria.
- Desarrollar una interfaz web interactiva para jugar contra AIChess.
- Documentar y publicar los resultados experimentales y la evolución del proyecto.

## 2. Tecnologías

### Tecnologías actuales

- **Python 3.12:** lenguaje principal de programación.
- **python-chess:** gestión del tablero, generación de movimientos legales y reglas del ajedrez.
- **pytest:** desarrollo y ejecución de pruebas automatizadas para verificar el funcionamiento de los algoritmos.
- **Git:** control de versiones.
- **GitHub:** alojamiento y documentación del repositorio.
- **Visual Studio Code:** entorno de desarrollo.

### Tecnologías previstas

- **PyTorch:** implementación y entrenamiento de redes neuronales.
- **C++:** optimización de algoritmos críticos.
- **FastAPI:** desarrollo de la API.
- **React y TypeScript:** interfaz web.
- **Docker:** despliegue mediante contenedores.
- **MLflow:** seguimiento de experimentos y modelos.
- **PostgreSQL:** almacenamiento de partidas y estadísticas.

## 3. Estado actual del proyecto

**Versión 0.2.0 — Motor con evaluación estratégica básica**

### Funcionalidades implementadas

- Representación del tablero mediante python-chess.
- Generación, validación y ejecución de movimientos legales.
- Ejecución autónoma de partidas completas.
- Evaluación de posiciones mediante el valor material de las piezas.
- Sistema de puntuación en centipeones.
- Identificación y valoración de jaques mate y tablas.
- Búsqueda exhaustiva de movimientos de profundidad 1 (*one-ply search*).
- Selección de la jugada con mejor evaluación inmediata.
- Deshacer movimientos simulados para conservar la posición original.
- Pruebas automatizadas mediante pytest.

### Limitaciones actuales

- El motor no anticipa las respuestas del adversario.
- La evaluación no considera factores posicionales como movilidad, control del centro o seguridad del rey.
- El sistema todavía no dispone de redes neuronales ni aprendizaje automático.
- No se ha establecido una clasificación Elo del motor.

El próximo objetivo será implementar Minimax y poda alfa-beta para analizar secuencias de movimientos.

## 4. Historial de versiones

| Versión | Fecha | Descripción |
|---|---|---|
| 0.1.0 | 18/10/2026 | Primer motor autónomo con selección aleatoria de movimientos |
| 0.2.0 | 20/10/2026 | Evaluación material y búsqueda de profundidad 1 |
| 0.3.0 | Pendiente | Algoritmo Minimax y poda alfa-beta |
| 0.4.0 | Pendiente | Integración de redes neuronales |
| 0.5.0 | Pendiente | Aprendizaje por refuerzo mediante self-play |

Para consultar los cambios detallados de cada versión, consultar `CHANGELOG.md`.

## 5. Roadmap

### Fase 1 — Motor básico
- [x] Configuración del entorno de desarrollo.
- [x] Implementación del tablero y movimientos legales.
- [x] Desarrollo de un agente autónomo básico.
- [x] Configuración de Git y GitHub.

### Fase 2 — Inteligencia estratégica
- [x] Función de evaluación material.
- [x] Búsqueda exhaustiva de profundidad 1.
- [x] Pruebas automatizadas iniciales.
- [ ] Algoritmo Minimax.
- [ ] Optimización mediante poda alfa-beta.
- [ ] Evaluación posicional avanzada.

### Fase 3 — Aprendizaje automático
- [ ] Diseño de una red neuronal.
- [ ] Entrenamiento mediante PyTorch.
- [ ] Implementación de Monte Carlo Tree Search.
- [ ] Sistema de aprendizaje por refuerzo mediante self-play.

### Fase 4 — Optimización y producto final
- [ ] Optimización del rendimiento computacional.
- [ ] API para la comunicación con el motor.
- [ ] Interfaz web interactiva.
- [ ] Evaluación competitiva y análisis estadístico.
- [ ] Documentación de resultados experimentales.

## 6. Metodología de desarrollo

AIChess sigue una metodología incremental.

Cada nueva funcionalidad se desarrolla, verifica y registra mediante Git. Las versiones principales se documentan en el historial de cambios y, cuando corresponda, se publican en GitHub.

El rendimiento del motor se evaluará mediante pruebas automatizadas, partidas contra versiones anteriores y comparaciones con motores de referencia.

## 7. Autor

León Macías Vicente