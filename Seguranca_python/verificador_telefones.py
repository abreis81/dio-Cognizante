## verifica o telefone e fornece a localização/cidade do mesmo

## usado a biblioteca phonenumbers - fornece recursos, como informações básicas de um nome de telefone, validação de um numero de telefone e etc

import phonenumbers

from phonenumbers import geocoder

phone = input('Digir o telefone no format +551122223333: ')

## string passada será convertida para um numero de telefone
phone_number = phonenumbers.parse(phone)

print(geocoder.description_for_number(phone_number, 'pt'))