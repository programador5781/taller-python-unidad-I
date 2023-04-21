# taller-python-unidad-I
### 1. Hacer fork del repo
#### En el contexto de la programación y el uso de repositorios de código en plataformas como GitHub, hacer "fork" de un repositorio significa crear una copia personal de ese repositorio en tu propia cuenta de GitHub. Al hacer fork de un repositorio, puedes hacer cambios en tu propia copia del código sin afectar el código original en el repositorio original.

Una vez que has hecho fork de un repositorio, puedes trabajar en tu propia versión del código y hacer todos los cambios que necesites, como agregar nuevas características o corregir errores. Luego, puedes enviar tus cambios de vuelta al repositorio original mediante un "pull request" (solicitud de extracción), lo que permitirá al propietario del repositorio original revisar tus cambios y decidir si los acepta o no.

Hacer fork de un repositorio es una herramienta útil en colaboraciones de código abierto, ya que permite a otros desarrolladores trabajar en su propia versión del código sin afectar el trabajo original del propietario del repositorio. También es una forma de colaborar con otros desarrolladores, ya que pueden hacer fork de tu repositorio y trabajar en sus propias versiones del código.

### 2. Clonar el repo
#### Clonar un repositorio" es el proceso de copiar un repositorio de código de una plataforma de alojamiento de repositorios, como GitHub o GitLab, a tu propia computadora local. Esto significa que puedes trabajar en el código en tu propia computadora y hacer cambios sin afectar el repositorio original en la plataforma de alojamiento.

Para clonar un repositorio, generalmente se utiliza la herramienta de línea de comandos de Git. Primero, debes tener Git instalado en tu computadora. Luego, debes encontrar la URL del repositorio que deseas clonar desde la plataforma de alojamiento. Luego, desde la línea de comandos, puedes ejecutar el comando git clone [url] seguido de la URL del repositorio. Git descargará todo el contenido del repositorio en una nueva carpeta en tu computadora local.

Una vez que has clonado el repositorio, puedes trabajar en el código en tu propia computadora y hacer cambios, agregar nuevas características o corregir errores. Luego, puedes enviar tus cambios de vuelta al repositorio original en la plataforma de alojamiento mediante un "push" (empujar), lo que permitirá al propietario del repositorio original revisar tus cambios y decidir si los acepta o no.

### 3. Crear una rama
En Git, una rama es una línea de desarrollo independiente que se deriva del tronco principal del repositorio. Las ramas permiten trabajar en nuevas características o cambios de código sin afectar el tronco principal. Para crear una nueva rama en Git, sigue estos pasos:

Abre la terminal o línea de comandos en tu computadora y navega hasta el directorio del repositorio clonado.
Asegúrate de estar en la rama principal (master) del repositorio ejecutando el comando git checkout master.
Crea una nueva rama ejecutando el comando git branch [nombre_de_la_rama]. El nombre de la rama debe ser descriptivo para identificar el objetivo de la rama, por ejemplo, nueva_funcionalidad o correccion_de_errores.
Cambia a la nueva rama que acabas de crear ejecutando el comando git checkout [nombre_de_la_rama].
Ahora estás en una nueva rama donde puedes trabajar en tu nueva funcionalidad o hacer cambios en el código sin afectar la rama principal. Una vez que hayas completado los cambios, puedes fusionar los cambios de la nueva rama de vuelta a la rama principal (master) mediante un "merge" o enviar la nueva rama a la plataforma de alojamiento mediante un "push".

## INSTRUCCIONES

### Paso a paso
Haz un "fork" del repositorio original en la plataforma de alojamiento, como GitHub. Para hacer esto, ve al repositorio original y haz clic en el botón "Fork" en la esquina superior derecha de la página. Esto creará una copia del repositorio en tu cuenta.

Clona el repositorio en tu computadora. Para hacer esto, ve a la página de tu repositorio recién creado y copia la URL del repositorio. Luego, abre la terminal o línea de comandos en tu computadora y ejecuta el siguiente comando:

``` 
git clone [URL_del_repositorio]
```
Asegúrate de reemplazar "[URL_del_repositorio]" con la URL que acabas de copiar.

Cambia al directorio del repositorio recién clonado. Para hacer esto, ingresa el siguiente comando en la terminal:
cd [nombre_del_repositorio]
Asegúrate de reemplazar "[nombre_del_repositorio]" con el nombre del repositorio que acabas de clonar.

Verifica que estás en la rama principal del repositorio. Para hacer esto, ingresa el siguiente comando:
```
git branch
```
Esto mostrará una lista de todas las ramas en el repositorio y resaltará la rama actual en la que te encuentras. Si la rama actual es "master", entonces estás en la rama principal.

Crea una nueva rama para trabajar. Ingresa el siguiente comando en la terminal:
```
git branch nombre_de_tu_rama
```
Asegúrate de reemplazar "nombre_de_tu_rama" con un nombre descriptivo para tu nueva rama.

Cambia a la nueva rama. Ingresa el siguiente comando:
```
git checkout nombre_de_tu_rama
```
Ahora estás en la nueva rama y puedes trabajar en ella sin afectar la rama principal.

¡Eso es todo! Ahora puedes agregar nuevos archivos, hacer cambios en el código o cualquier otra cosa que necesites en tu nueva rama. Cuando hayas terminado, puedes fusionar la rama de vuelta a la rama principal o enviar la nueva rama a la plataforma de alojamiento, como GitHub.

