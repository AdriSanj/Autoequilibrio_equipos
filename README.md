# Autoequilibrio_equipos
Módulo para autoequilibrar la selección de jugadores de equipos en videojuegos.

Introducir en el archivo .txt los nombres y puntuaciones de los jugadores. Dichas puntuaciones es recomentable obtenerlas de las páginas de dichos videojuegos para obtener
una mayor exactitud. El código convierte dichas puntuaciones a valores del 1 al 10, tomando como referencia al jugador con mayor puntuación, y genera equipos aleatorios,
a la vez que suma las puntuaciones de ambos equipos. Una vez dichas puntuaciones tengan una diferencia de puntuación menor que 3 por defecto (es decir, si hay un equipo
con 31 puntos y otros con 34, o uno con 32 y otro con 33), el programa devuelve la lista de jugadores de dichos equipos. En caso contrario, sigue comparando equipos 
y puntuaciones. 
Nótese que si dos jugadores tienen 10 puntos, tomando la diferencia de puntos máxima entre equipos como 3, estos dos jugadores no serán emparejados en el mismo equipo.
