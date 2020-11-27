# -*- coding: utf-8 -*-
"""
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ignore = ["duplex", "alias", "Current configuration"]

import sys

src_file_name = sys.argv[1]
src_file_name = 'config_sw1.txt'
dst_file_name = sys.argv[2]
dst_file_name = 'config_sw1_cleared.txt'

print(sys.argv)
with open(src_file_name) as config, open('config_sw1_cleared.txt', 'w') as dst:
    for line in config:
        is_common_elements_exist = False
        for ignore_pattern in ignore:
            if ignore_pattern in line:
                is_common_elements_exist = True
        if not is_common_elements_exist:
            print(line.rstrip())
            dst.write(line)
