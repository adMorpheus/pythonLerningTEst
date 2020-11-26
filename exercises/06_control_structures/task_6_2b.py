# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip = input('Enter ip: ')

while True:
    parts = ip.split('.')
    contains_four_parts = len(parts)==4
    all_parts_is_digits = True
    all_parts_in_range = True
    for part in parts:
        if not part.isdigit():
            all_parts_is_digits =False
            break
        if not (int(part)>=0 and int(int(part)<=255)):
            all_parts_in_range = False
            break
    if  contains_four_parts and all_parts_in_range and all_parts_is_digits:
        break
    else:
        ip = input(f'Incorrect ip ({ip})!\nPlease try again: ')


first_byte = int(ip.split('.')[0])
if first_byte >= 1 and first_byte <= 223:
    message = f'{ip} is unicast address'
elif first_byte >= 224 and first_byte <= 239:
    message = f'{ip} is multicast address'
elif ip == '255.255.255.255':
    message = f'{ip} is local broadcast address'
elif ip == '0.0.0.0':
    message = f'{ip} is unassigned address'
else:
    message = f'{ip} is unused address'

print(message)
