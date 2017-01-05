import os
from collections import Counter


def list_files(folder):
    all_files = {}
    for path, dirs, files in os.walk(folder):
        for file_name in files:
            full_path = os.path.join(path, file_name)
            all_files[full_path] = '{} {} bytes'.format(file_name, os.path.getsize(full_path))
    return all_files


def find_duplicates(files):
    files_descriptions = files.values()
    files_descriptions = Counter(files_descriptions)
    duplicates = list(filter(lambda file_name:
                             files_descriptions[file_name] > 1,
                             files_descriptions.keys()))
    return duplicates


def print_duplicates(files, duplicates):
    if len(duplicates) == 0:
        print('duplicate files not found')
        return
    for duplicate_file_description in duplicates:
        print('duplicate of {} found in the following directories:'
              .format(duplicate_file_description))
        print()
        duplicate_dirs = list(filter(lambda full_path: files[full_path] == duplicate_file_description, files.keys()))
        for duplicate_dir in duplicate_dirs:
            print(duplicate_dir)
        print()


if __name__ == '__main__':
    folder = input('Input folder to search duplicates: \n')
    file_list = list_files(folder)
    duplicate_files = find_duplicates(file_list)
    print_duplicates(file_list, duplicate_files)
