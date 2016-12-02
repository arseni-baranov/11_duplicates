from os import path, walk


def are_files_duplicates(file_path1, file_path_2):

    getsize = lambda file_path, fname: path.getsize(path.join(file_path, fname))
    printer = lambda path1, path2, file1, file2: print("Duplicates found (size: {}): \n{}\n{} \n".
                                                       format(getsize(path1, file1), path.join(path1, file1),
                                                              path.join(path2, file2)))

    for chunk1 in walk(file_path1):
        for chunk_2 in walk(file_path_2):
            for fname1 in chunk1[2]:
                for fname_2 in chunk_2[2]:
                    if fname1 == fname_2 and getsize(file_path1, fname1) == getsize(file_path_2, fname_2):
                        print()
                        printer(file_path1, file_path_2, fname1, fname_2)


def main():
    file_path1 = input('Enter the first folder to scan: ')
    file_path_2 = input('Enter the second folder to scan: ')

    if not path.exists(file_path1 or file_path_2):
        print('Folder you entered does not exist')
        exit()

    are_files_duplicates(file_path1, file_path_2)

if __name__ == '__main__':
    main()
