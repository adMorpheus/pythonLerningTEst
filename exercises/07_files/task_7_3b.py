# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

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
for lines in vlan_dic.get(int(input('Enter vlan number: ')),['vlan not exist']):
    print(lines)