# -*- coding: utf-8 -*-
"""
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
import sys
ignore = ["duplex", "alias", "Current configuration"]

# file_name = sys.argv[1]
file_name = 'config_sw1.txt'
print(sys.argv)
with open(file_name) as config, open('config_sw1_cleared.txt', 'w') as dst:
    for line in config:
        is_common_elements_exist = False
        for ignore_pattern in ignore:
            if ignore_pattern in line:
                is_common_elements_exist = True
        if not is_common_elements_exist:
            print(line.rstrip())
            dst.write(line)
