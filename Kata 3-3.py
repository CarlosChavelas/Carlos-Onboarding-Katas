#Escribe un programa que emita la advertencia o información correcta a la gente de la Tierra, 
#según la velocidad y el tamaño de un asteroide.

Velocidad= 25
Tamaño= 25

if Tamaño< 25 and Velocidad<= 25:
    print('Fuera de peligro. El asteroide se quemará al entrar a la atmósfera terrestre. Posible avistamiento de rayo de luz.')
elif Tamaño> 25:
    print('Peligro inminente. Daños en la corteza.')
elif Velocidad> 25:
    print('Advertencia. Asteroide viajando a más de 25 km/s con dirección a la Tierra.')
else:
    print('Sólo queda esperar...')