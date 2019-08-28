import os

if __name__ == "__main__":

    # Задача-1:
    # Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
    # из которой запущен данный скрипт.
    # И второй скрипт, удаляющий эти папки.

    # создание
    main_dir_path = os.path.abspath('.')
    for i in range(1,10):
        new_dir = os.path.join(main_dir_path, f'dir_{i}')

        if not os.path.exists(new_dir):
            os.makedirs(new_dir)

    # удаление
    child_dirs = [x[0] for x in os.walk(main_dir_path)][1:]

    for directory in child_dirs:

        os.rmdir(directory)

    # Задача-2:
    # Напишите скрипт, отображающий папки текущей директории.

    print([x[0] for x in os.walk(os.path.abspath('.'))][1:])

    print(list(filter(lambda item: item, [x if os.path.isdir(x) else None for x in os.listdir(os.path.abspath('.'))])))

    with os.scandir(os.path.abspath('.')) as it:
        for entry in it:
            if not entry.name.startswith('.') and entry.is_dir():
                print(entry.name)

    # Задача-3:
    # Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

    path = os.path.realpath(__file__)
    print(path)


def remove_dir(directory):

    main_dir_path = os.path.abspath('.')

    directory_path = os.path.join(main_dir_path, directory)

    if os.path.exists(directory_path):

        os.rmdir(directory_path)

    else:

        print("Невозможно удалить")


def create_dir(directory):

    main_dir_path = os.path.abspath('.')

    directory_path = os.path.join(main_dir_path, directory)

    if not os.path.exists(directory_path):

        os.makedirs(directory_path)

    else:

        print("Невозможно создать")


def change_dir(directory):

    main_dir_path = os.path.abspath('.')

    directory_path = os.path.join(main_dir_path, directory)

    if os.path.exists(directory_path):

        os.chdir(directory_path)

    else:

        print("Невозможно перейти")


def show_dir():
    with os.scandir(os.path.abspath('.')) as it:
        for entry in it:
            if not entry.name.startswith('.') and entry.is_dir():
                print(entry.name)
