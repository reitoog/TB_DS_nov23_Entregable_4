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
2) Luego, cada equipo (= el miembro designado de cada equipo) debería añadir una rama (branch) llamada "Feature [X]" (X siendo la letra de su equipo) a su fork.
3) A continuación, los otros miembros de cada equipo (a parte del designado) hacen cada uno un fork al fork del miembro designado de su equipo.
4) Y, por último, cada miembro de cada equipo hará una copia local (clona) del fork que hizo en su ordenador y agregará/modificará/descargará archivos allí para posteriormente pedir que se actualicen los cambios en el nivel de más arriba (upstream).
5) Cuando el trabajo de cada equipo se considera terminado se pueden subir los cambios al respositorio principal (haciendo un pull request).

**Ejemplo:**

1) El equipo A (Flask) designa a un miembro (puede ser el manager). El miembro accede a su cuenta de GitHub y abre el enlace del repositorio principal (https://github.com/Yomitear/TB_DS_nov23_Entregable_4). Hace un fork de este repositorio principal.
2) En este fork añade una nueva rama llamada "Feature A".
3) Luego, todos los miembros del equipo A excepto el miembro designado hacen un fork al fork que hizo el miembro designado (¡ que tendrá otra URL que la del repositorio principal ! - la proporcionará el miembro designado que hizo el fork).
4) A continuación, cada uno de los miembros, incluído el miembro designado, clonan en sus ordenadores el fork que hicieron.
Cada miembro del equipo trabaja en su parte del proyecto en su ordenador (**en la carpeta del clonado del fork del fork del repo principal**) y cuando quieren subir/modificar un archivo hacen un request de "commit changes" a su propio fork y luego un pull request al fork del miembro designado. El miembro designado tiene que aprobar/revisar esos pull requests.
5) Cuando dan el trabajo por hecho, y tendrán todo actualizado en el fork del miembro designado, se hace un pull request desde este fork al repositorio principal. Ese request lo aprobará/revisará el manager de Git (= desarrollador senior), que está escribiendo estás lineas ahora mismo :) El trabajo de cada uno de los equipos se mergeará en la rama Develop del repositorio principal.

### ¡ Actualización importante 2024.03.11 !
##### Solo el equipo A (Flask) necesita subir/modificar archivos a GitHub, ya que lo estamos usado exclusivamente para la parte de código y no para almacenar datos... Los otros equípos (B - Git, C - Cloud, D - PySpark/Databricks) basta con que hagan un fork por parte del miembro designado y creen una rama llamada "Feature [X]" (X siendo la letra de su equipo) en este fork.


