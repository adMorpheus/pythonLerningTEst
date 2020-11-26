# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Сообщение должно выводиться только один раз.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
ip = input('Enter ip address: ')
is_ip = True
try:
  is_ip = len(ip.split('.')) == 4
  for part in ip.split('.'):
      if(not(int(part) >=0 and int(part) <= 255)):
          is_ip = False
except:
    is_ip = False
if not is_ip:
    message = 'Incorrect ip'
else:
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