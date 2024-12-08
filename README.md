### Backend (Django)

El backend está desarrollado con **Django**, que se conecta a una API externa para obtener los datos de consumo mensual del usuario. La API se consume para obtener los datos de consumo de datos y los minutos utilizados por el usuario durante los meses anteriores.

#### Características del Backend:
- **Django Rest Framework**: Se utiliza para crear una API que interactúa con los datos del usuario.
- **Consumo de la API**: Django se conecta a una API externa para obtener los detalles del consumo de cada mes para el usuario y luego los envía al frontend para su visualización.
