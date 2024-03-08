# TB_DS_nov23_Entregable_4

Este es el repositorio principal del proyecto de productivización.

Tiene 3 ramas (branches):
  - main
  - develop
  - release

El modelo que pondremos en producción será una regresión lineal sobre el dataset de Kaggle de videojuegos que se puede encontrar en este enlace:
https://www.kaggle.com/datasets/gregorut/videogamesales

En la rama main se han subido unos archivos iniciales: el csv del dataset y un notebook donde un miembro del equipo de trabajo hizo pruebas con él.

### Flujo de trabajo con Git/GitHub:

1) Equipos A (Flask), B (Git), C (Cloud) y D (PySpark/Database) - tenéis que hacer un fork a este repositorio en vuestro GitHub (designar uno por cada equipo - puede ser el del manager del equipo). Así vamos a tener 4 forks (o repos forkeados), que son copias online del respositorio principal.
2) Luego, cada equipo debería añadir una rama (branch) llamada "Feature [X]" (X siendo la letra de su equipo) a su fork. Y ejecutar el trabajo allí.
3) Cada miembro de cada equipo puede hacer una copia local (clonar) del fork en su ordenador y agregar/modificar/descargar archivos allí para posteriormente subir los cambios al fork.
4) Cuando el trabajo de cada equipo se considera terminado se pueden subir los cambios al respositorio principal.

**Ejemplo:**

1) El equipo A (Flask) designa a un miembro (puede ser el manager). El miembro accede a su cuenta de GitHub y abre el enlace del repositorio principal (https://github.com/Yomitear/TB_DS_nov23_Entregable_4). Hace un fork de este repositorio principal.
2) En este fork añade una nueva rama llamada "Feature A".
3) Luego, todos los miembros del equipo A clonan en sus ordenadores el repositorio forkeado (¡ que tendrá otra URL que la del repositorio principal ! - la proporcionará el miembro designado que hizo el fork).
Cada miembro del equipo trabaja en su parte del proyecto en su ordenador (**en la carpeta del repo clonado del fork**) y cuando quieren subir/modificar un archivo hacen un request de "commit changes" al fork. El miembro designado tiene que aprobar/revisar esos pull requests.
4) Cuando dan el trabajo por hecho, y tendrán todo actualizado en el fork, se hace un pull request de commit desde el fork al repositorio principal. Ese request lo aprobará/revisará el manager de Git, que está escribiendo estás lineas ahora mismo :) El trabajo de cada uno de los equipos se mergeará en la rama Develop de este repositorio principal.

   * Sugiero que hagáis todos los equipos un pull request de commit con el trabajo parcial (por ejemplo el lunes o el martes) y luego sobreescribimos futuros cambios, si surgen. Es para simular mejor un flujo real de trabajo.


