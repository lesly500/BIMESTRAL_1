# BIMESTRAL_1

# VideoGames For Pygame

En este juego basico creado con la herramienta de Pygame, bueno la pregunta es ¿En que consiste este juego?. Consiste en una nave espacial y tu mision es evitar colisionar con planetas que caen en el medio del espacio.

## Condiciones para la creacion del videojuego

* Python 3.x
* Pygame (`pip install pygame`)
* Imágenes del cohete y los planetas (asegúrate de que estén en la carpeta `img/`):
    * `img/COHETE.png`
    * `img/PLANETA.png`

## Proceso de ejecucion del programa

1.  Asegúrate de tener Python y Pygame instalados.
2.  Coloca las imágenes del cohete y los planetas en la carpeta `img/`.
3.  Ejecuta el script de Python: `python tu_script.py` (reemplaza `tu_script.py` con el nombre de tu archivo).

## Controles bacicos para la version de Pc

* **Flecha Derecha**: Mueve el cohete a la derecha.
* **Flecha Izquierda**: Mueve el cohete a la izquierda.
* **ESC**: Cierra el juego.

### Elementos del Juego

* **Cohete**: Controlado por el jugador, se mueve horizontalmente.
* **Planetas**: Caen desde la parte superior de la pantalla.
* **Puntuación**: Aumenta en 1 cada vez que un planeta llega a la parte inferior de la pantalla sin colisionar con el cohete.

### Lógica del Juego

* El juego utiliza un bucle principal para actualizar la pantalla y manejar los eventos.
* Los planetas se generan aleatoriamente en la parte superior de la pantalla y se mueven hacia abajo.
* Se detectan las colisiones entre el cohete y los planetas.
* La puntuación se muestra en la parte inferior de la pantalla.

## Estructura del Código

* **Variables**: Se definen variables para la ventana, el cohete, los planetas y la puntuación.
* **Imágenes**: Se cargan las imágenes del cohete y los planetas.
* **Bucle Principal**: Se manejan los eventos, se actualiza la posición de los objetos y se dibuja en la pantalla.
* **Colisiones**: Se detectan las colisiones entre el cohete y los planetas.
* **Puntuación**: Se actualiza y se muestra la puntuación.

## Créditos

* Este juego fue creado usando Pygame.
* Las imágenes del cohete y los planetas fueron obtenidas de [fuente de las imágenes].