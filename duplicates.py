from os import walk
from os import path
from hashlib import md5
from collections import Counter
from re import match


def are_files_duplicates(duplicate, file_hashes, print_hashes):

    for file_hash in file_hashes.items():
        if duplicate == file_hash[1]:
                print(file_hash[0].replace('\\', '/'))


def get_duplicate_hashes(file_hashes):
    
    # Считаем сигнатуры что повторяются и сохраняем их в отдельный словарь
    
    count_hashes = Counter(file_hashes.values())
    only_duplicates = {}

    for item in count_hashes.items():
        if item[1] > 1:
            only_duplicates[item[0]] = item[1]

    return only_duplicates


def hash_files(file_list):
    
    # Хэшируем каждый файл из списка по md5

    hash_table = {}

    for file in file_list:
        file_hash = md5(open(file, 'rb').read()).hexdigest()
        hash_table[file] = file_hash

    return hash_table


def scan_directory(directory):
    
    # Создаём список файлов в указанной папке

    file_paths = []

    for root, directories, files in walk(directory):
        for filename in files:
            filepath = path.join(root, filename)
            file_paths.append(filepath)

    return file_paths


def are_hashed_needed():
    while True:
        print("Выводить хэш-сумму файлов? (y/n): ")
        response = input()

        if match("[yY]", response):
            return True
        elif match("[nN]", response):
            return False
        else:
            print("Введено некорректное значение: {}".format(response))


if __name__ == '__main__':

    scan_folder = input('Введите папку для сканирования на дубликаты файлов: ')

    if not path.exists(scan_folder):
        print('Заданной папки не существует')
        exit()

    file_list = scan_directory(scan_folder)
    file_hashes = hash_files(file_list)
    duplicate_hashes = get_duplicate_hashes(file_hashes)
    
    # Спрашиваем выводить ли хэшы для файлов
    print_hashes = are_hashed_needed()

    # Если переменная останется на нуле, значит дубликатов не найдено
    duplicate_count = 0

    for duplicate in duplicate_hashes:
        print('')
        print('=========================================================')
        print('Найдены дубликаты: ')
        print('=========================================================')

        # Выводить ли md5 сигнатуру файлов дубликатов?

        if print_hashes:
            print('Сигнатура файла hash:', duplicate)
            print('')

        are_files_duplicates(duplicate, file_hashes, print_hashes)
        duplicate_count += 1

    if not duplicate_count:
        print('')
        print('=========================================================')
        print('Дубликаты не обнаружены')
        print('=========================================================')
