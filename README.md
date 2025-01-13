# Resumen del Proyecto: Buscador de Anime con Flask
![image](https://github.com/user-attachments/assets/fe41e915-84d7-4dc3-8c23-432973f5dc8d)

Este proyecto es una aplicación web desarrollada con Python y Flask que permite a los usuarios buscar y reproducir episodios de anime. La aplicación utiliza una API externa para obtener información sobre animes y sus episodios.

**Características Principales:**

1.  **Búsqueda de Animes:**
    *   **Formulario de Búsqueda:** La página principal contiene un formulario para que los usuarios ingresen un término de búsqueda.
    *   **Resultados de Búsqueda:** Al enviar el formulario, la aplicación realiza una consulta a una API externa (https://animeflv-api-1ius.onrender.com) y muestra los resultados en una lista. Cada resultado muestra el título y la sinopsis del anime, con un enlace para ver más información sobre los episodios.
2.  **Información del Anime:**
    *   **Página de Información:** Al hacer clic en un anime en los resultados de búsqueda, se muestra una página con información detallada, incluyendo el título, la sinopsis, el ID, los géneros, el estado y la lista de episodios disponibles.
    *    **Enlaces a los Episodios:** Cada episodio tiene un enlace que lleva a la página para ver los servidores donde se puede reproducir el episodio.
3.  **Lista de Episodios:**
    *   **Visualización de Servidores:** Muestra la lista de servidores disponibles para el episodio.
    *    **Reproducción de Video:** Al hacer clic en un botón, se muestra un reproductor de video que utiliza un iframe para mostrar el video desde la URL proporcionada.
4.  **Reproducción de Episodios:**
    *   **Adaptación de URLs:** La aplicación adapta las URL de mega y streamtape antes de mostrarlas en el iframe. En mega reemplaza `#!` por `embed/` y `!` por `#` y en streamtape reemplaza `v` por `e` para que funcionen en el iframe
5.  **API Externa:**
    *   **Uso de AnimeFLV API:** La aplicación utiliza la API `https://animeflv-api-1ius.onrender.com` para buscar animes, obtener información sobre ellos y obtener los enlaces de los episodios.

**Tecnologías Utilizadas:**

*   **Python:** Lenguaje de programación principal.
*   **Flask:** Framework web para construir la aplicación.
*   **Requests:** Librería para realizar solicitudes HTTP a la API externa.
*   **HTML:** Para la estructura de las páginas.

**Propósito:**

La aplicación está diseñada como un proyecto demostrativo para buscar y reproducir animes utilizando una API externa. Es un ejemplo sencillo de una aplicación web que interactúa con una API y muestra los resultados al usuario.

**Para un Trabajo:**

Este proyecto puede ser un buen ejemplo para demostrar habilidades en el desarrollo web con Python y Flask, especialmente en la interacción con APIs externas y en la manipulación de datos JSON. Es un buen punto de partida para crear aplicaciones web más complejas que consuman APIs. Se centra en la funcionalidad, la experiencia de usuario básica y la interacción con una API externa.

**Enlace del proyecto**: https://animewebsite-animeflv.onrender.com

![image](https://github.com/user-attachments/assets/deee8a8e-20d3-47bd-b5be-36279a156486)
