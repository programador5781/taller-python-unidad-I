# taller-python-unidad-I
### 1. fork 
#### En el contexto de la programación y el uso de repositorios de código en plataformas como GitHub, hacer "fork" de un repositorio significa crear una copia personal de ese repositorio en tu propia cuenta de GitHub. Al hacer fork de un repositorio, puedes hacer cambios en tu propia copia del código sin afectar el código original en el repositorio original.

Una vez que has hecho fork de un repositorio, puedes trabajar en tu propia versión del código y hacer todos los cambios que necesites, como agregar nuevas características o corregir errores. Luego, puedes enviar tus cambios de vuelta al repositorio original mediante un "pull request" (solicitud de extracción), lo que permitirá al propietario del repositorio original revisar tus cambios y decidir si los acepta o no.

Hacer fork de un repositorio es una herramienta útil en colaboraciones de código abierto, ya que permite a otros desarrolladores trabajar en su propia versión del código sin afectar el trabajo original del propietario del repositorio. También es una forma de colaborar con otros desarrolladores, ya que pueden hacer fork de tu repositorio y trabajar en sus propias versiones del código.

### 2. Clonar el repo
#### Clonar un repositorio" es el proceso de copiar un repositorio de código de una plataforma de alojamiento de repositorios, como GitHub o GitLab, a tu propia computadora local. Esto significa que puedes trabajar en el código en tu propia computadora y hacer cambios sin afectar el repositorio original en la plataforma de alojamiento.

Para clonar un repositorio, generalmente se utiliza la herramienta de línea de comandos de Git. 
1. Debes tener Git instalado en tu computadora. 
2. Debes encontrar la URL del repositorio que deseas clonar desde la plataforma de alojamiento. 
3. Desde la línea de comandos, puedes ejecutar el comando: 
```
git clone [url] 
```
seguido de la URL del repositorio. Git descargará todo el contenido del repositorio en una nueva carpeta en tu computadora local.

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

1. Clona el repositorio en tu computadora. Para hacer esto, ve a la página del repositorio https://github.com/programador5781/taller-python-unidad-I.git copia la URL del repositorio. 
2. Abre la terminal o línea de comandos en tu computadora y ejecuta el siguiente comando:

``` 
git clone [URL_del_repositorio]
```
Asegúrate de reemplazar "[URL_del_repositorio]" con la URL que acabas de copiar.

3. Cambia al directorio del repositorio recién clonado. Para hacer esto, ingresa el siguiente comando en la terminal:
```
cd [nombre_del_repositorio]
```
Asegúrate de reemplazar "[nombre_del_repositorio]" con el nombre del repositorio que acabas de clonar. En nuestro caso el nombre del repositorio es taller-python-unidad-I.

4. Verifica que estás en la rama principal del repositorio. Para hacer esto, ingresa el siguiente comando:
```
git branch
```
Esto mostrará una lista de todas las ramas en el repositorio y resaltará la rama actual en la que te encuentras. Si la rama actual es "main", entonces estás en la rama principal.

5. Crea una nueva rama para trabajar. Ingresa el siguiente comando en la terminal:
```
git branch nombre_de_tu_rama
```
Asegúrate de reemplazar "nombre_de_tu_rama" con un nombre descriptivo para tu nueva rama. Puede ser tu nombre, con esto se identificamos más facilmente a los miembros del equipo, en este caso.

6. Cambia a la nueva rama. Ingresa el siguiente comando:
```
git checkout nombre_de_tu_rama
```
Ahora estás en la nueva rama y puedes trabajar en ella sin afectar la rama principal.


Para subir tus cambios, sigue los mismos pasos, que cuando trabajas de forma individual. Asegurate de estar en tu rama.

1. nuevamente la terminal en VSCode, ejecuta el comando:
```
git add nombre_del_archivo
```
asegurate de reemplazar nombre_del_archivo por el nombre del archivo que estás trabajando.

2. realiza un commit
```
git commit -m "tu_mensaje"
```

3. realiza un push
```
git push
```
si al hacer el push te arroja un error: 

```
fatal: The current branch [nombre_de_tu_rama] has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin nombre_de_tu_rama

To have this happen automatically for branches without a tracking
upstream, see 'push.autoSetupRemote' in 'git help config'.
```

Lo podemos solucionar ejecutando el siguiente comando:

```
git config --global push.autoSetupRemote true
```

De esta manera ya podemos hacr nuestro push a nuestra rama, el cual se verá en el repo de la siguiente manera:


![image](https://user-images.githubusercontent.com/88601627/233657286-af2b5604-b4b3-4e4f-bee6-fb55d8746a7d.png)

4. Una vez en el github, presionamos donde dice:

![image](https://user-images.githubusercontent.com/88601627/233658918-bd212885-b6b6-4919-876b-68962d93b67e.png)

aquí veremos la siguiente imagen:

![image](https://user-images.githubusercontent.com/88601627/233659051-5ab1451f-75e8-4b64-aa82-9c2b8b09806d.png)


Aquí podemos escribir un comentario sobre el ejercicio y finalmente presionar el botón CREATE PULL REQUEST

![image](https://user-images.githubusercontent.com/88601627/233659523-72dffbcc-c910-4fef-8744-d349b48daea6.png)

Ahora se nos muestra la siguiente pantalla:

![image](https://user-images.githubusercontent.com/88601627/233660107-5ab42bad-faaf-40c9-9c6b-96093c0b8c9c.png)

Click en Merge pull request y después en confirm merge

¡Eso es todo! 

