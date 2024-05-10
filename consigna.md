# Consigna

Suponer un sistema de reserva de asientos para un anfiteatro. El teatro cuenta con 10 filas de 10 asientos cada una. Se necesita desarollar un sistema (sin uso de BD, unicamente manejo de datos de forma logica) que permita llevar a cabo lo siguiente:

1- Cargar el "mapa" de las filas y asientos. Indicando con una "X" los asientos ocupados con una "L" los asientos libres. AL iniciar el programa, todos los asientos deben de estar libres.

2- Manejar la reseva de asientos contemplando que un asiento SOLO PUEDE SER RESEVADO si se encuentra en estado "L" en caso de que este en estado "X" se debera permitir al comprador elegir otro asiento. Si se encuentra en estado "L" debera pasar automaticamente al estado "X".

3- Para finalizar el programa se debera ingresar un valor en particular. Contemplar que no existe una cantidad exacta de veces que el programa se pueda ejecutar.

4- Contemplar que SOLO EXISTEN 10 FILAS y 10 ASIENTOS. No se puedes vender asientos fuera de esas numeraciones. No se permite "sobreventa".

* Consideraciones: No es necesaria la implementacion de IGU ni de BD. Se evaluara 100% el manejo logico del desarrollo de la aplicacion.

Extra: En caso de que un cliente solicite vizualizar cuales son los asientos libres, el sistema debe permitir mostrar de forma grafica el mapa de asientos. NO UTILIZAR IGU para este caso. Utilizar UNICAMENTE logica y la salida por consola.

Fuente del ejercicio: https://www.youtube.com/watch?v=npfzSC8B3aM&t=317s&ab_channel=TodoCode