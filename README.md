<!-- CREATE README-->
# REPOSITORIO DE PRACTICA GIT
Este repositorio se crea con el propósito de practicar los comandos principales de Git y familiarizarse con su flujo de trabajo.

![GitHub Logo](/img/logo.png)

## **COMANDOS DE GIT**

A continuación, se presentan algunos comandos principales de Git que puedes utilizar en este repositorio:
### **CONFIGURACION INICIAL**
Configura tu nombre de usuario y dirección de correo electrónico:
```git
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"
```

### **INICIALIZAR UN REPOSITORIO**
Crea un nuevo repositorio local:
```git
git init
```

Clona un repositorio existente desde un repositorio remoto:
```git
git clone <URL del repositorio>
```

### **REALIZAR CAMBIOS**
Verifica el estado actual de los archivos en tu repositorio:
```git
git status
```

Agrega un archivo modificado o nuevo al área de preparación:
```git
git add <nombre del archivo>
```

Realiza un commit con los cambios agregados en el área de preparación:
```git
git commit -m "Mensaje del commit"
```

### **TRABAJAR CON RAMAS**
Crea una nueva rama:
```git
git branch <nombre de la rama>
```

Cambia a una rama existente:
```git
git checkout <nombre de la rama>
```
Combina una rama con la rama actual:
```
git merge <nombre de la rama>
```

Elimina una rama:
```git
git branch -d <nombre de la rama>
```

### **SINCRONIZACIÓN REMOTA**
Agrega un repositorio remoto:
```
git remote add <nombre remoto> <URL del repositorio>
```

Envía tus cambios al repositorio remoto:
```git
git push <nombre remoto> <nombre de la rama>
```

Actualiza tu repositorio local con los cambios más recientes del repositorio remoto:
```git
git pull <nombre remoto> <nombre de la rama>
```

### **REGISTRO  Y EXPLOTACIÓN**
Muestra el historial de commits:
```git
git log
```

Muestra los cambios realizados en un commit específico:
```git
git show <identificador del commit>
```
### **RAMAS REMOTAS**
Lista todas las ramas remotas:
```git
git branch -r
```

Sincroniza tus ramas locales con las ramas remotas:
```git
git fetch
```

Esos son solo algunos de los comandos más utilizados en Git. Para obtener más información sobre los comandos y opciones disponibles, puedes consultar la documentación oficial de Git o utilizar el comando **´git --help´**.







