# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

import os
import sys
import shutil
print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("ls - отображение полного пути текущей директории")
    print("cp <file_name> - создает копию указанного файла")
    print("rm <file_name> - удаляет указанный файл (запросить подтверждение операции)")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")


def make_dir():
    if not fs_object_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), fs_object_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(fs_object_name))
    except FileExistsError:
        print('директория {} уже существует'.format(fs_object_name))


def ping():
    print("pong")


def file_copy():
    if not fs_object_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    file_path = os.path.join(os.getcwd(), fs_object_name)
    try:
        shutil.copy2(file_path)
        print('файл {} создан'.format(fs_object_name))
    except FileExistsError:
        print('файл {} уже существует'.format(fs_object_name))


def file_drop():
    if not fs_object_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    if input(f'Удалить файл {fs_object_name}? y/n').lower() == 'y':
        file_path = os.path.join(os.getcwd(), fs_object_name)

        if os.path.exists(file_path):
            os.remove(file_path)
            print('файл {} удален'.format(fs_object_name))
        else:
            print('файл {} не существует'.format(fs_object_name))
    else:
        return
def change_dir():

    if not fs_object_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), fs_object_name)

    if os.path.exists(dir_path):
        os.chdir(dir_path)
        print('текущая директория {}'.format(fs_object_name))
    else:
        print('директория {} не существует'.format(fs_object_name))

def abs_path():
    print(os.path.abspath('.'))

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": file_copy,
    "rm": file_drop,
    "cd": change_dir,
    "ls": abs_path,

}

try:
    fs_object_name = sys.argv[2]
except IndexError:
    fs_object_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")


# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.
