# PrisonersProblem

Este proyecto es una simulación del problema del prisionero. El problema del prisionero es un problema fundamental de la teoría de juegos que muestra que dos personas pueden no cooperar incluso si ello va en contra del interés de ambas.

Fue desarrollado originariamente por Merrill M. Flood y Melvin Dresher mientras trabajaban en RAND en 1950. Albert W. Tucker formalizó el juego con la frase sobre las recompensas penitenciarias y le dio el nombre del "dilema del prisionero" (Poundstone, 1995).

Enunciado original del problema:

> La policía arresta a dos sospechosos. No hay pruebas suficientes
> para condenarlos y, tras haberlos separado, los visita a cada 
> uno y les ofrece el mismo trato. Si uno confiesa y su cómplice
> no, el cómplice será condenado a la pena total, diez años, y el
> primero será liberado. Si uno calla y el cómplice confiesa, el 
> primero recibirá esa pena y será el cómplice quien salga libre. 
> Si ambos confiesan, ambos serán condenados a seis años. Si ambos
> lo niegan, todo lo que podrán hacer será encerrarlos durante un 
> año por un cargo menor.

Para simplificarlo tenemos el siguiente sistema de recompensas en función de si cooperan o no:

![Recompensas](https://github.com/AlejandroMolinosEligio/PrisonersProblem/blob/main/Photos/Recompensas.png?raw=true)


## Estrategias y individuos

Por el momento hay un total de 9 estrategias. Estas estrategias son utilizadas por cada integrante de la población de sobre como iteractuan con el entorno. Cada individuo de la población tiene asiganada una estrategia e interactua con cada uno de los individuos de la población además de una copia de sí mismo con un total de 200 acciones.

Las estrategias son las siguientes:

- **TitFotTat:** Esta estrategia en primer lugar siempre confía, y su siguiente acción será la misma que la anterior de su oponente. De forma adicional para hacer una simulación más fiel a la realidad dispone de una probabilidad del 10% mediante el cual puede que esta segunda política no se aplique y coopere independiente mente de la acción anterior del oponente.

![TitFotTat](https://github.com/AlejandroMolinosEligio/PrisonersProblem/blob/main/Photos/TitFotTat.png?raw=true)

- **Dumb:** Esta estrategia siempre colabora independientemente de lo que haga el oponente.

![Dumb](https://github.com/AlejandroMolinosEligio/PrisonersProblem/blob/main/Photos/Dumb.png?raw=true)


- **Devil:** Esta estrategia nunca colabora independientemente de lo que haga el oponente.

![Devil](https://github.com/AlejandroMolinosEligio/PrisonersProblem/blob/main/Photos/Devil.png?raw=true)

- **Friedman:** Esta estrategia parte de la cooperación, pero si el oponente en algún momento no coopera, Friedman nunca volverá a cooperar.

![Friedman](https://github.com/AlejandroMolinosEligio/PrisonersProblem/blob/main/Photos/Friedman.png?raw=true)

- **Joss:** Esta estrategia comienza cooperando y luego replica la acción del oponente, pero esta tiene un 10% de no cooperar.

![Joss](https://github.com/AlejandroMolinosEligio/PrisonersProblem/blob/main/Photos/Joss.png?raw=true)

- **Random:** Esta estrategia de forma con un 50% de probabilidad elige cooperar o no cooperar. 

![Random](https://github.com/AlejandroMolinosEligio/PrisonersProblem/blob/main/Photos/Random.png?raw=true)

- **Sample:** Con esta estrategia las dos primeras acciones siempre serán cooperar, y por defecto también. Solo no cooperará en caso de que el oponente no coopere dos veces seguidas.

![Sample](https://github.com/AlejandroMolinosEligio/PrisonersProblem/blob/main/Photos/Sample.png?raw=true)

- **Tester:** Esta estrategia parte de la cooperación y como segunda opción la no cooperación, si la segunda opción
del oponente es no cooperar comenzará a actuar como TitFotTat, en caso contrario alternará entre la cooperación y la no cooperación.

![Tester](https://github.com/AlejandroMolinosEligio/PrisonersProblem/blob/main/Photos/Tester.png?raw=true)

- **Clock:** Esta estrategia parte de la cooperación y solo no coopera cada 3 acciones.

![Clock](https://github.com/AlejandroMolinosEligio/PrisonersProblem/blob/main/Photos/Clock.png?raw=true)


## Clases

### Prisioner

Está clase en su versión final consta de 3 atributos:

- **Name:** Nombre de la estrategia
- **Func:** Nombre de la función de estrategia que utiliza
- **Score:** Puntuación del prisionero

### Estrategy

Esto no es una clase como tal y su función es contener el total de estrategias disponibles y sus funciones asociadas.

### Negotiation

Está clase en su versión final consta de 3 atributos:

- **Prio1:** Primer prisionero de la negociación
- **Prio2:** Segundo prisionero de la negociación
- **Prio1_values:** Acciones del primer prisionero
- **Prio2_values:** Acciones del segundo prisionero
- **Prio1_score:** Puntuación del primer prisionero
- **Prio2_score:** Puntuación del segundo prisionero
- **Iterations:** Número de acciones

También dispone de una función auxiliar **start()** que da inicio a la negociación. 


## First and Second version

Estas dos versiones son similares, la única diferencia entre ellos principal es el número de estrategias. Para la ejecución de estos se parte del escenario en el que disponemos de X estrategias y estas **negocian** una a una con cada estrategia además de una copia de ella misma. Estas versiones tienen la peculiaridad de que la población solo está conformada por una estrategia de cada tipo, es decir si tenemos X estrategias solo habrá X individuos en la población. Las negociaciones entre cada uno de ellos tiene un total de 200 acciones, estás siguen las métricas mencionadas al principio y si ejecutamos el código principal que es el archivo **rudio_Prisionero.py** veremos una salida por pantalla en la que veremos la valoración de cada una de las estrategias además de una lista que los ordena de mayor a menor puntuacion.

![First](https://github.com/AlejandroMolinosEligio/PrisonersProblem/blob/main/Photos/First.png?raw=true)

![Second](https://github.com/AlejandroMolinosEligio/PrisonersProblem/blob/main/Photos/Second.png?raw=true)

## Third version

Esta es la versión más compleja hasta el momento, estableciendo el marco esta versión crea una población inicial de (5 * total de estrategias). Mediante esto se establece una población inicial con el mismo número de Prisioneros con la misma estrategia de forma igualitaria. A su vez, cada uno de los prisioneros interactua con cada uno de los otros y una copia de sí mismo con un total de 200 acciones al igual que las versiones anteriores, pero dado que esta vez hay más de un tipo evaluaremos la puntuacion de cada uno de forma individual a fin de crear nuevas generaciones. Estas generaciones están conformadas por los 10 mejores individuos de la generación anterior y el resto se generan nuevos de forma aletoria. Esto se repite un total de 1000 generaciones y al final nos quedamos con la mejor de todas ellas.

![Third](https://github.com/AlejandroMolinosEligio/PrisonersProblem/blob/main/Photos/Third.png?raw=true)

## Fourth version

MEJORAR ALGORITMO GENÉTICO

