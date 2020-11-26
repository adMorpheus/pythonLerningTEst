# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
import sys
ignore = ["duplex", "alias", "Current configuration"]

# file_name = sys.argv[1]
file_name = 'config_sw1.txt'
print(sys.argv)
with open(file_name) as config:
    for line in config:
        is_common_elements_exist = False
        for ignore_pattern in ignore:
            if ignore_pattern in line:
                is_common_elements_exist = True
        if (not line.startswith('!')) and not is_common_elements_exist:
            print(line.rstrip())
