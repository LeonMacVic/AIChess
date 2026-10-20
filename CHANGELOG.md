# Historial de cambios — AIChess

Este documento registra los cambios más relevantes realizados durante el desarrollo de AIChess.

El proyecto utiliza una numeración de versiones con el formato `MAJOR.MINOR.PATCH` como referencia para organizar sus entregas.

## [0.2.0] — 20/10/2026

### Añadido

**Evaluación estratégica**
- Implementación de una función de evaluación material en `evaluacion_tablero.py`.
- Valoración de peones, caballos, alfiles, torres y damas mediante centipeones.
- Detección y valoración de posiciones de jaque mate.
- Asignación de una evaluación neutral a posiciones terminales de tablas.

**Selección de movimientos**
- Implementación de búsqueda exhaustiva de profundidad 1.
- Selección de movimientos según la mejor evaluación inmediata.
- Maximización de la evaluación para las blancas y minimización para las negras.
- Simulación de movimientos mediante `push()` y restauración mediante `pop()`.
- Resolución aleatoria de empates entre movimientos con idéntica puntuación.

**Pruebas automatizadas**
- Incorporación de pytest.
- Pruebas de igualdad y ventaja material.
- Pruebas de detección de jaque mate y tablas.
- Verificación de la legalidad de los movimientos seleccionados.
- Verificación de la captura de una pieza de mayor valor.
- Comprobación de que la búsqueda conserva el estado original del tablero.

### Limitaciones conocidas
- Búsqueda limitada a una jugada de profundidad.
- Ausencia de anticipación de respuestas del rival.
- Evaluación basada únicamente en material y resultados terminales.
- Ausencia de aprendizaje automático.

## [0.1.0] — 18/10/2026

### Añadido

**Motor de ajedrez**
- Creación y representación del tablero inicial mediante python-chess.
- Generación de movimientos legales.
- Ejecución y deshacer de movimientos.
- Identificación del jugador al que corresponde el turno.
- Comprobación de finalización de partidas.

**Autonomía**
- Implementación de una función de selección aleatoria de movimientos legales.
- Simulación de partidas completas entre dos agentes autónomos.
- Registro de las jugadas ejecutadas en la Terminal.
- Identificación del resultado y la causa de finalización.
- Incorporación de un límite de movimientos como mecanismo de seguridad.

### Infraestructura

- Configuración de Python 3.12.
- Creación de un entorno virtual `.venv`.
- Configuración de Visual Studio Code.
- Inicialización del repositorio Git.
- Publicación del repositorio en GitHub.
- Configuración del archivo `.gitignore`.
- Incorporación de la documentación inicial.

### Limitaciones conocidas

- El motor no evalúa la calidad de las posiciones.
- La selección de movimientos es aleatoria.
- No existe búsqueda estratégica de movimientos futuros.
- No incorpora aprendizaje automático.
- El rendimiento competitivo todavía no ha sido evaluado.

---