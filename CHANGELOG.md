# Historial de cambios — AIChess

Este documento registra los cambios más relevantes realizados durante el desarrollo de AIChess.

El proyecto utiliza una numeración de versiones con el formato `MAJOR.MINOR.PATCH` como referencia para organizar sus entregas.

## [Sin publicar]

### Previsto
- Implementación de una función de evaluación material.
- Desarrollo de un algoritmo de búsqueda de profundidad 1.
- Incorporación de pruebas automatizadas mediante pytest.
- Mejora de la selección de movimientos.

---

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