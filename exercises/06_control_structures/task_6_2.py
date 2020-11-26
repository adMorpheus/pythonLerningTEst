# -*- coding: utf-8 -*-
"""
Задание 6.2

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip = input('Enter ip address: ')
first_byte = int(ip.split('.')[0])

if first_byte >=1 and first_byte <=223:
    message = f'{ip} is unicast address'
elif first_byte >= 224 and first_byte <=239:
    message = f'{ip} is multicast address'
elif ip == '255.255.255.255':
    message = f'{ip} is local broadcast address'
elif ip == '0.0.0.0':
    message = f'{ip} is unassigned address'
else:
    message = f'{ip} is unused address'

print(message)