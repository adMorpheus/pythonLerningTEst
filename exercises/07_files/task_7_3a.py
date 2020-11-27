# -*- coding: utf-8 -*-
"""
Задание 7.3a

Сделать копию скрипта задания 7.3.

Дополнить скрипт:
- Отсортировать вывод по номеру VLAN

В результате должен получиться такой вывод:
10       01ab.c5d0.70d0      Gi0/8
10       0a1b.1c80.7000      Gi0/4
100      01bb.c580.7000      Gi0/1
200      0a4b.c380.7c00      Gi0/2
200      1a4b.c580.7000      Gi0/6
300      0a1b.5c80.70f0      Gi0/7
300      a2ab.c5a0.700e      Gi0/3
500      02b1.3c80.7b00      Gi0/5
1000     0a4b.c380.7d00      Gi0/9

Обратите внимание на vlan 1000 - он должен выводиться последним.
Правильной сортировки можно добиться, если vlan будет числом, а не строкой.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
with open('CAM_table.txt') as dst_file:
    vlan_list = []
    for line in dst_file:
        if len(line.split()) == 4:
            if len(line.split()[1].split('.')) == 3:
                result = line.strip().split()
                result.remove('DYNAMIC')
                result = f'{result[0]:<7}{result[1]:<7}{result[2]:>7}'
                vlan_list.append(result)
                # print(f'{result[0]:<7}{result[1]:<7}{result[2]:>7}')
# print(vlan_list)
vlan_dic = {}
vlan_numbers_list = []
for vlan_line in vlan_list:
    int_vlan_number = int(vlan_line.split()[0])
    if int_vlan_number in vlan_dic:
        vlan_dic[int_vlan_number].append(vlan_line)
    else:
        vlan_dic.update({int_vlan_number: [vlan_line]})
        vlan_numbers_list.append(int_vlan_number)

vlan_numbers_list.sort()
for vlan_number in vlan_numbers_list:

    for lines in vlan_dic.get(vlan_number):
        print(lines)
