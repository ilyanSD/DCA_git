Se ha creado el siguiente alias global -> git config --global alias.st status

Y el siguiente alias local -> git config alias.br branch

Simplemente haciendo "git st" o "git br" ejecutaremos "git status" o "git branch" respectivamente.

---------------------------------------------------------------

En main.py encontramos una calculadora basica en python. Esta calculadora incorpora varias funciones que permiten aplicar un calculo a numeros proporcionados por el ususario.

Durante la ultima ejecucion de la aplicacion nos damos cuenta de que la funcion de potencia de 2 realmente esta haciendo una potencia de 3.

Para solventar este problema primero tenemos que encontrar el commit donde se ha incorporado este error.

Usaremos el comando "git bisect"

Ejecutamos "git bisect start"