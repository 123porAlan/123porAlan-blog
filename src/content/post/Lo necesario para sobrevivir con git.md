---
title: "Lo necesario para sobrevivir con GIT"
description: "No importa la razón por la que quieras aprender Git, lo importante es que lo entiendas. Por eso, aquí tienes LA guía."
publishDate: "02 Jul 2025"
tags: ["Git", "Testing101", "SoftwareTesting", "Computación"]
draft: false
seriesId: citrus-docs
orderInSeries: 5
---
Cuando entré a la universidad, los profesores del área nos sugirieron tomar el propedéutico de la carrera. Yo, como cualquier persona joven e inexperta, pensé que era una idea fabulosa: un curso que nos enseñaría las bases antes de la materia que sí nos evaluaría. Procedí a tomar dicho propedéutico. ¿El paso final? Teníamos que hacer un fork a un proyecto y luego modificarlo para, al final, enviar un pull request. ¿Qué pasó en mi caso? No lo logré.

Fue entonces cuando, por mi cuenta, investigué en diferentes recursos. Hoy quiero compartirte lo que considero lo más esencial y necesario para sobrevivir tanto al inicio de la universidad como a los primeros días de trabajo, o al menos para tener noción de qué está pasando.


**1. Instalando Git (sin miedo padrino)**

Primero lo primero: necesitas tener Git instalado. Si usas Windows, baja el instalador desde [git-scm.com](https://git-scm.com/). En Mac, abre la terminal y escribe:

```bash
brew install git
```

En Linux, lo clásico:

```bash
sudo apt-get install git
```

Si usas la distro buena (Fedora) que por cierto ya hablaremos esa distro en el siguiente post, ya se esta cocinando eso.

```shell
sudo dnf install git
```

¿Ya? Seguimos.

**2. Configura tu identidad (para que no seas “unknown”)**

Git quiere saber quién eres. Así tus cambios no aparecen como “misterioso usuario”. Solo pon esto en la terminal (cambia los datos por los tuyos):

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"
```

¿Quieres ver cómo quedó? Usa:

```bash
git config --list
```

**3. Inicia tu repositorio (el punto de partida)**

Ve a la carpeta de tu proyecto y ejecuta:

```bash
git init
```

Eso crea la carpeta `.git` donde Git guarda todo la configuración de tu proyecto.

**4. Agrega tus archivos y haz tu primer commit**

Para decirle a Git qué archivos quieres guardar, usa:

```bash
git add .
```

El punto significa “todos los archivos”. Si solo quieres uno, pon el nombre en lugar de solo poner el punto.

Ahora, guarda ese momento con un commit:

```bash
git commit -m "Primer commit"
```

**5. Conecta con un repositorio remoto (GitHub, GitLab, etc.)**

Ya tienes tu repo en GitHub (o el que uses). Copia la URL y enlázalo así:

```bash
git remote add origin https://github.com/tuusuario/tu-repo.git
```

**6. Sube tu proyecto (push)**

Hora de mandar todo a la nube:

```bash
git push -u origin main
```

O si tu rama principal se llama `master`:

```bash
git push -u origin master
```

El `-u` es para que la próxima vez solo tengas que poner `git push` y Git ya sabe a dónde.

**7. Baja cambios (pull)**

¿Trabajas en equipo o desde varias compus? Antes de empezar, siempre es buena idea traer los últimos cambios de tus compañeros:

```bash
git pull
```

Así evitas sorpresas.

---

## ¿Cómo funcionan las ramas en Git?


Si alguna vez has escuchado frases como “haz una rama para esa nueva funcionalidad” o “no trabajes directo en main”, pero no tienes idea de qué va eso, aquí te digo, de echó es mas fácil de lo que parece.

**¿Para qué sirven las ramas?**

Las ramas en Git son como líneas paralelas de tiempo donde puedes trabajar en nuevas ideas, corregir errores o experimentar, sin afectar el código principal. Imagina que tu proyecto es un árbol: la rama principal (`main` o `master`) es el tronco, y cada rama nueva es una ramita donde puedes hacer cambios sin miedo a romper todo.

Esto es útil porque te permite:

- Probar cosas nuevas sin arriesgar el proyecto completo.
- Trabajar en varias tareas al mismo tiempo (por ejemplo, una rama para una nueva función y otra para corregir un bug).
- Colaborar con otras personas sin pisarse los cambios.

**¿Cómo crear una rama?**

Crear una rama es tan fácil como escribir:

```bash
git branch nombre-de-tu-rama
```

Pero lo más común es crearla y cambiarte a ella de una vez:

```bash
git checkout -b nombre-de-tu-rama
```

Ahora, todo lo que hagas quedará guardado en esa rama, no en la principal.

**¿Cómo moverse entre ramas?**

Para cambiarte de rama, solo usa:

```bash
git checkout nombre-de-tu-rama
```

O, si usas una versión moderna de Git, puedes usar:

```bash
git switch nombre-de-tu-rama
```

Así puedes saltar entre diferentes líneas de trabajo sin perder nada.

**¿Cómo ver las ramas que tienes?**

Para ver todas las ramas de tu proyecto:

```bash
git branch
```

La rama en la que estás parado aparecerá con un asterisco.

---

¿Ves? Las ramas no son tan difíciles. Son tu mejor amigo para trabajar ordenado y sin miedo a romper nada.  
 En la siguiente sección te cuento cómo unir ramas y qué hacer si Git te dice que hay conflictos.

---

## ¿Cómo hacer merge y solucionar conflictos?


Llegó el momento de unir caminos. Cuando trabajas con ramas, tarde o temprano vas a querer juntar los cambios de una rama con otra. A eso se le llama **merge**. Pero, como en toda historia que valga la pena, a veces hay choques y aparecen los temidos **conflictos**. Aquí te explico cómo enfrentarlos sin perder la calma.

**¿Qué es un merge?**

Hacer un merge en Git es básicamente decir: “Quiero que los cambios de esta rama se mezclen con los de otra”. Por lo general, lo más común es unir tu rama de trabajo con la rama principal (`main` o `master`).

**¿Cómo hacer un merge?**

Supón que tienes una rama llamada `feature-x` y quieres unirla a `main`. Haz lo siguiente:

1. Cambia a la rama donde quieres juntar los cambios (por ejemplo, `main`):
    
    ```bash
    git checkout main
    ```
    
2. Haz el merge:
    
    ```bash
    git merge feature-x
    ```
    

Si todo va bien, Git mezclará los cambios automáticamente y listo.

### ¿Qué pasa si hay conflictos?

A veces, Git no puede decidir solo cómo unir los cambios porque dos ramas modificaron la misma parte de un archivo. Eso es un **conflicto**.

Cuando esto pasa, Git te avisa y marca los archivos en conflicto. Dentro de esos archivos verás algo así:

```
<<<<<<< HEAD
Este es el contenido en tu rama actual.
=======
Este es el contenido en la rama que quieres unir.
>>>>>>> feature-x
```

Tu trabajo es elegir qué parte conservar, o incluso combinar ambas. Borra las marcas (`<<<<<<<`, `=======`, `>>>>>>>`) y deja el resultado final como tú quieras.

### ¿Cómo soluciono el conflicto?

1. Abre el archivo en conflicto y edítalo hasta que quede como debe ser.
    
2. Guarda los cambios.
    
3. Marca el conflicto como resuelto:
    
    ```bash
    git add nombre-del-archivo
    ```
    
4. Termina el merge con un commit (si Git no lo hace solo):
    
    ```bash
    git commit
    ```
    

¡Listo! Ya resolviste el conflicto y tus ramas están unidas.

---

Los conflictos pueden parecer difíciles al principio, pero con práctica se vuelven parte del día a día. Lo importante es leer con calma, entender qué cambió y decidir qué versión quieres dejar. Ahora estas listo para trabajar con git. ¡Suerte!


**Post data:** 
## ¿Y si quiero regresar a un commit anterior?

A veces, después de varios cambios, te das cuenta de que algo salió mal y quieres volver a una versión anterior de tu proyecto. No te preocupes, Git también te cubre en eso.

Primero, para ver el historial de commits, usa:

```bash
git log --oneline
```

Esto te mostrará una lista de commits con sus identificadores (ese código raro al inicio de cada línea).

Si solo quieres ver cómo era tu proyecto en un commit anterior (sin perder nada), puedes moverte temporalmente con:

```bash
git checkout id-del-commit
```

Pero si quieres regresar tu rama a ese punto (¡cuidado, esto sí cambia la historia!), puedes usar:

```bash
git reset --hard id-del-commit
```

O si solo quieres deshacer los últimos cambios pero guardarlos para después, usa:

```bash
git reset --soft id-del-commit
```

**Tip:** Si solo quieres deshacer el último commit pero dejar los archivos como estaban, puedes hacer:

```bash
git reset --soft HEAD~1
```

Recuerda: antes de hacer un reset, asegúrate de que no tienes cambios importantes sin respaldar, porque podrías perderlos.

¡Y listo! Así puedes viajar en el tiempo con Git y salvarte de cualquier desastre.
