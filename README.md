## Emplea Frameworks para el Desarrollo de Aplicaciones

Profesor: [@bidkar](https://github.com/bidkar)<br>
Alumno(a): [@usuario-alumno](https://github.com/usuario-alumno)

### Instalación de Git
1. Visitar el sitio https://git-scm.com y descargar el instalador para tu sistema operativo.
2. Si utilizas Windows 10 o superior, desde una terminal ejecuta<br>
    `winget install Git.Git`
3. Verificar la instalación<br>
    Cerrar y abrir la terminal, y ejecutar<br>
    `git --version`

### Configuración Git
**Si es tu computadora**
```shell
# configurar el nombre de usuario
git config --global user.name "Bidkar Aragón Cárdenas"

# configurar el correo electrónico
git config --global user.email bidkar@cetis108.edu.mx
```

**Si NO es tu computadora**
```shell
# configurar el nombre de usuario a nivel de proyecto
# en la terminal ejectura
git config user.name "Bidkar Aragón Cárdenas"

# configurar el correo electrónico
git config user.email bidkar@cetis108.edu.mx
```

**Para todos**
```shell
# configurar el nombre de la rama principal (master)
git config --global init.defaultbranch main

# inicializar el repositorio (decirle a git que un directorio será repositorio)
# te ubicas en el directorio del código y ejectuas
git init

# guardar tu primera versión
# revisa el estado del repositorio (detecta archivos nuevos y cambios)
git status

# si hay archivos nuevos o cambios, prepararlos
git add -A

# si preparaste archivos, guarda la versión
git commit -m "Mi primera versión"
```