Se ha creado el siguiente alias global -> git config --global alias.st status

Y el siguiente alias local -> git config alias.br branch

Simplemente haciendo "git st" o "git br" ejecutaremos "git status" o "git branch" respectivamente.

---------------------------------------------------------------

En main.py encontramos una calculadora basica en python. Esta calculadora incorpora varias funciones que permiten aplicar un calculo a numeros proporcionados por el ususario.

Durante la ultima ejecucion de la aplicacion nos damos cuenta de que la funcion de potencia de 2 realmente esta haciendo una potencia de 3.

Para solventar este problema primero tenemos que encontrar el commit donde se ha incorporado este error.

Usaremos el comando "git bisect"

Ejecutamos "git bisect start" y copiamos el ultimo commit que sabemos que no contiene error (HASH del commit). En este caso vamos a pegar el primer commit de todos con el comando "git bisect good [HASH_COMMIT]" seguido de "git bisect bad" para especificar que el commit actual tiene el bug. Este comando hara una busqueda binaria entre los commits delimitados por los primeros "bad" y "good" commits.

Probaremos la aplicacion despues de cada iteracion de "git bisect" hasta que demos con el commit que ha originado el fallo.

En nuestro caso "git bisect" nos arroja este resultado una vez finaliza con las iteraciones

ef59b90999b02f8f18e485e0f70a138f5f911fa8 is the first bad commit
commit ef59b90999b02f8f18e485e0f70a138f5f911fa8
Author: Ilya Slyusarchuk <ilyaniesvb@gmail.com>
Date:   Wed Dec 21 20:05:41 2022 +0100

    Creada funcion potencia

 main.py | 9 ++++++++-
 1 file changed, 8 insertions(+), 1 deletion(-)

 Esto nos dice que archivos se han cambiado, y el hash del primer commit que implementa el error. A partir de ahora ejecutamos "git bisect reset" para volver del modo "dettached" al commit apuntado por HEAD y procedemos a arreglar el error.