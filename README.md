<<<<<<< HEAD
# ![Django App](project-logo.png)
> Trabajo final de la materia Ingeniería de Software II - UNLP

Integrantes del grupo: 
* Tonelli, Manuela 
* Garea, Antonella
* García, Agustina 

Ayudante: Sobrado, Ariel

## Introducción
  El trabajo final consiste en que el grupo interprete el papel de desarrolladoras de software, y el ayudante el de cliente. Por medio de diversas tecnicas de elicitación de requerimientos el grupo fue conociendo en profundidad las necesidades del servicio a sistematizar.
  Combi19 se hizo usando [Django](https://www.djangoproject.com/) con Python 3
  
## Sobre el sistema
  El sistema a realizar corresponde a una empresa llamada Combi-19; esta brinda un servicio de viajes de corta, media y larga distancia mediante combis. El cliente quiere sistematizar este servicio, sobre todo la venta de pasajes y testeos de COVID-19 que se le harían a los pasajeros al momento de subirse a su transporte. Tanto los clientes (usuarios del sistema), como los choferes de combis deben poder acceder iniciando sesión. 
 #### Funionalidades para el usuario
   El usuario puede hacer compras y cancelaciones de pasajes, o compras de insumos para su viaje. También puede acceder a membresía GOLD, ya sea en el momento en que se registra o después.
#### Funcionalidades para los choferes
  El chofer carga una planillas de síntomas de COVID-19 por cada pasajero del viaje. También pueden tramitar la venta de un pasaje a un cliente de último momento. Al finalizar el viaje, puede cambiar el estado del mismo a "TERMINADO".
  
 ## Empezando
1.  Clona el repositorio:
 ~~~
    $ git clone https://github.com/agmontserrat/Combi19.git
    $ cd Combi19
~~~
2. Instala los requerimientos (esto todavia no funciona)
 ~~~
    $ pip install -r requirements.txt
~~~
3. Migrate
~~~
    $ python manage.py migrate
~~~
4. Y luego iniciá el servidor
~~~
    $ python manage.py runserver
~~~
=======
# ![Django App](project-logo.png)
> Trabajo final de la materia Ingeniería de Software II - UNLP

Integrantes del grupo: 
* Tonelli, Manuela 
* Garea, Antonella
* García, Agustina 

Ayudante: Sobrado, Ariel

## Introducción
  El trabajo final consiste en que el grupo interprete el papel de desarrolladoras de software, y el ayudante el de cliente. Por medio de diversas tecnicas de elicitación de requerimientos el grupo fue conociendo en profundidad las necesidades del servicio a sistematizar.
  Combi19 se hizo usando [Django](https://www.djangoproject.com/) con Python 3
  
## Sobre el sistema
  El sistema a realizar corresponde a una empresa llamada Combi-19; esta brinda un servicio de viajes de corta, media y larga distancia mediante combis. El cliente quiere sistematizar este servicio, sobre todo la venta de pasajes y testeos de COVID-19 que se le harían a los pasajeros al momento de subirse a su transporte. Tanto los clientes (usuarios del sistema), como los choferes de combis deben poder acceder iniciando sesión. 
 #### Funionalidades para el usuario
   El usuario puede hacer compras y cancelaciones de pasajes, o compras de insumos para su viaje. También puede acceder a membresía GOLD, ya sea en el momento en que se registra o después.
#### Funcionalidades para los choferes
  El chofer carga una planillas de síntomas de COVID-19 por cada pasajero del viaje. También pueden tramitar la venta de un pasaje a un cliente de último momento. Al finalizar el viaje, puede cambiar el estado del mismo a "TERMINADO".
  
 ## Empezando
1.  Clona el repositorio:
 ~~~
    $ git clone https://github.com/agmontserrat/Combi19.git
    $ cd Combi19
~~~
2. Instala los requerimientos (esto todavia no funciona)
 ~~~
    $ pip install -r requirements.txt
~~~
3. Migrate
~~~
    $ python manage.py migrate
~~~
4. Y luego iniciá el servidor
~~~
    $ python manage.py runserver
~~~
>>>>>>> 72ae3ff1594e004eb21a0595593efab7e900fe90
