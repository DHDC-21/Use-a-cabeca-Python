
# Use a Cabeca! Pyhton - Exemplo 03

# Importa do modulo datetime(1) a funcao datatime(2)
from datetime import datetime

# Parecido com a matriz em linguagem C
odds = [ 1,  3,  5,  7,  9,
        11, 13, 15, 17, 19,
        21, 23, 25, 27, 29,
        31, 33, 35, 37, 39,
        41, 43, 45, 47, 49,
        51, 53, 55, 57, 59 ]


# Loop com o for e range
for i in range(5):

    right_this_minute = datetime.today().minute
    
     # Se o minuto da hora atual for impar exibe mensagem(1) senao exibe mensagem (2)
    if right_this_minute in odds:
        print("This minute seams a little add.")
    else:
        print("Not an odd minute.")
    

print("fim do loop")