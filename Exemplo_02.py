
## Use a Cabeca! Python - Exemplo 02
## Estudo dos modulos (bibliotecas) Python


## Importa da biblioteca os a funcao getcwd
from os import getcwd
## getcwd exibe a pasta a qual o codigo esta sendo executado
where_am_I = getcwd() # Usa uma variavel para chamar a funcao

## Modulo necessario para descobrir o nome do Kernel
import sys
sys.platform

print(sys.version)

## Em programacao e muito comum a utilizacao das datas
import datetime
datetime.date.today() # Retorna a data de hoje
## As partes do componetes da data
datetime.date.today().day
datetime.date.today().month
datetime.date.today().year
