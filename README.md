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

### Prisoner

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

Esta es una versión más compleja, estableciendo el marco esta versión crea una población inicial de (5 * total de estrategias). Mediante esto se establece una población inicial con el mismo número de Prisioneros con la misma estrategia de forma igualitaria. A su vez, cada uno de los prisioneros interactua con cada uno de los otros y una copia de sí mismo con un total de 200 acciones al igual que las versiones anteriores, pero dado que esta vez hay más de un tipo evaluaremos la puntuacion de cada uno de forma individual a fin de crear nuevas generaciones. Estas generaciones están conformadas por los 10 mejores individuos de la generación anterior y el resto se generan nuevos de forma aletoria. Esto se repite un total de 1000 generaciones y al final nos quedamos con la mejor de todas ellas.

![Third](https://github.com/AlejandroMolinosEligio/PrisonersProblem/blob/main/Photos/Third.png?raw=true)

## Fourth version

En esta versión del estudio he optado por la creación de algoritmos genéticos. La población inicial es de (6 * total de estrategias), a su vez exiten un total de 1000 generaciones y al igual que en versiones anteriores un total de 200 acciones por negociación. 

Para la creación del algoritmo genético, dada la naturaleza del mismo problema solo he implementeado algunos métodos para la creación de padres e hijos. Para la selección de padres hay un total de 4 métodos, estos son:

-   **Roullete:** Este método escoge los padres en función del valor porcentual asociado a cada estrategia y se generan individuos con mayor o menor probabilidad en función de este mismo valor.

-   **Ranking:** Este método escoge los mejores N individuos de una población y el resto serán los hijos de estos mismos.

-   **Elistism:** Este método se basa en realizar reproducciones parciales, es decir, que los individuos con mejor fitness tengan una descendencia que sea exactamente igual que ellos.

-   **Pairs:** En este método se crean parejas de forma aleatoria y de cada pareja se seleccionará aquel que tenga mejor fitness.

En cuanto a los métodos para la creación de hijos solo he implementado uno que es:

-   **Uniform cross:** Se crea un hijo como una selección aleatoria de los valores de los padres, en este caso las estrategias.

Para mejorarlo más he implementado que en la creación de hijos de los métodos que lo utilicen exista una componente de aleatoriedad para que se puedan seguir generando individuos que ya hayan sido extintos. 

![Fourth](https://github.com/AlejandroMolinosEligio/PrisonersProblem/blob/main/Photos/Third.png?raw=true)

Las ejecuciones de todas estas versiones se hace a través del archivo **ruido_Prisionero.py** y para añadir a modificar las estrategias existentes se debe modificar el archivo **Estrategies.py**. 

## Conclusiones

Como estudio preeliminar podemos decir lo siguiente. Teniendo en cuenta las métricas que se tienen para la evaluación de las remcompensas en un entorno en el que solo hubiera una única opción, la acción con mayor tasa ganadora sería no cooperar. La acción de no cooperar puede tener dos posibles futuros, que el oponente no coopere y ambos ganen 1 punto, o que el oponente coopere que en ese caso el primero ganaría 5 puntos. En cualquiera de los dos casos los posibles escenarios son el empate o la victoria, así que la mejor opción simepre será no cooperar. Pero esto solo sería aplicable en el caso de que hubiera una única acción pero para el caso que estamos tratando he querido hacer una simulación de un entorno real en el que no existe una única acción en cada negociación. Partiendo de esta premisa el caso anterior de escoger siempre no cooperar no será la opción ganadora.

### First version

Esta primera versión partía de 7 estrategias, estas son Dumb, TitForTat, Devil, Joss, Random, Friedman y Sample. Con un total de 200 acciones por cada negociación. Si ejecutamos el entorno simulado podemos ver que el ganador dependiendo de la ejecucución es Sample o TitFotTat. 

![FirstVersion](https://github.com/AlejandroMolinosEligio/PrisonersProblem/blob/main/Photos/1.png?raw=true)

Podemos ver que aquellas estrategias que tienen mejor puntuación son aquellas que podríamos considerar "buenas" y aquellas que tienen peor puntuación son las "malas" que las categorizaremos como aquellas que en primera instacia no cooperan o mayoritariamente no cooperan.

### Second version

Esta versión la cree a fin de introduccir mejores estrategias y modificando en general las estrategias establecidas. La principal añadida fue una variante de una de las estrategias ganadoras anteriroes TitFotTat. Esta estrategia llamada Tester partía de la no cooperación y después de la cooperación, esta a su vez comprueba si el oponente respondió como segunda acción cooperar ante la primera no cooperación de la estrategia. Si esto es así la estrategia seguirá coomportandose como su antecesor TitFotTat, en caso contrario comenzará a cooperar y no cooperar de forma alterna.

![SecondVersion](https://github.com/AlejandroMolinosEligio/PrisonersProblem/blob/main/Photos/2.png?raw=true)

Como podemos ver, pese a que este sea un predecesor de una estrategia anterior que tuvo una buena puntuación esta no ha tenido los mismos resultados. Dado que también se ha modificado la población inicial podemos ver que se han modificado también las estrategias ganadoras y ahora la encabeza Friedman y TitFotTat.

### Third version 

Esta versión es un preeludio de la futura implementación del algoritmo genético, en este comenzamos con el escenario anterior con la diferenciación de que ahora la población se irá modificando generacionalmente. Las generaciones posteriores costarán de los 10 mejores individuos de la población anterior y el resto se generan de forma aleatoria de entre todas las estrategias disponibles. Después de 450 generaciones los valores suelen quedar estables y como podemos ver en la siguiente imagen vuelven a ganar las estrategias "buenas" y las "malas" tienden a disminuir.

![ThirdVersion](https://github.com/AlejandroMolinosEligio/PrisonersProblem/blob/main/Photos/3.png?raw=true)

### Fourth version

Esta es la última implementación en la que he creado un algortimo genético con todos los métodos expuestos anteirormente. Tras la ejecución de estos podemos ver lo siguiente:

- **Pairs:**

![ThirdVersion](https://github.com/AlejandroMolinosEligio/PrisonersProblem/blob/main/Photos/pairs.png?raw=true)

- **Roullete:**

![ThirdVersion](https://github.com/AlejandroMolinosEligio/PrisonersProblem/blob/main/Photos/roullete.png?raw=true)

- **Ranking:**

![ThirdVersion](https://github.com/AlejandroMolinosEligio/PrisonersProblem/blob/main/Photos/ranking.png?raw=true)

- **Elitism:**

![ThirdVersion](https://github.com/AlejandroMolinosEligio/PrisonersProblem/blob/main/Photos/elitism.png?raw=true)


Como podemos ver en todos los escenarios vemos que aquellas estrategias ganadoras son las "buenas" y las "malas" tienden a la extinción. Generacionalmente podemos ver que estas últimas pueden verse incrementadas en un pico al principio de las generaciones pero a medida que estas van creciendo tienden a desaparecer.

### Caso especial 

A modo de estudio me pareció interesante ver como se comportaría una población en la que mayoritariamente habitan individuos "malos" y solo existe un grupo reducido de buenos. Para la ejecución de este experimento he escogido la creación de padres por el método de **pairs** y la creación de hijos por **uniform_cross**. Este fue el resultado:

![Test](https://github.com/AlejandroMolinosEligio/PrisonersProblem/blob/main/Photos/Test.png?raw=true)

Pese a que solo había dos únicos individuos "buenos" estos tienden a absorber al resto de la población "mala", lo que nos da a entender que por norma general como hemos podido ver en todas las simulaciones este patrón se repite y podemos concluir que esto se aplica a cualquiera de los niveles.