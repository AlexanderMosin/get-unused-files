import io
import sys
import glob

"""
Как пользоваться:

1) прописываем в переменную path_to_feature абсолютный путь до \ru.cft.qpay.online.features
2) вызываем скрипт

get_unused_files.py <имя .feature папки>

или python get_unused_files.py <имя .feature папки>
например, 
:> get_unused_files.py crediting-to-card-rus

3) получаем список неиспользуемых файлов в сценариях
"""
def searching(searching_file, source_for_search):
    for feature in source_for_search:
        with io.open(feature, encoding='utf-8') as file:
            for line in file:
                if searching_file in line:
                    return 'exist'

    return searching_file


if __name__ == '__main__':
    feature_dir = sys.argv[1]
    path_to_feature = r'c:\Source\qpay-online\itest\src\test\resources\ru.cft.qpay.online.features' + '\\' + feature_dir
    data_files_dirs = [r'\initialization-data-files', r'\expected-data-files']

    data_files = []

    # Формирование списка файлов из директорий initialization-data-files и expected-data-files
    for dir in data_files_dirs:
        for file in glob.glob(path_to_feature + dir + '\\**\\*.*', recursive=True):
            data_files.append(file.replace(path_to_feature + dir + '\\', '').replace('\\', '/'))

    # print("DEBUG: ")
    # for file in data_files:
    #     print(file)

    # Формирование списка feature-файлов в директории path_to_feature
    feature_files = []
    for file in glob.glob(path_to_feature + '\\*.*'):
        feature_files.append(file.replace(r'\\', '\\'))

    # print("DEBUG: ")
    # print(feature_files)

    unused_files = []

    for file in data_files:
        result = searching(file, feature_files)

        if result != 'exist':
            unused_files.append(result)

    print("Файлы, которые не используются в feature-файлах папки " + path_to_feature, end='\n\n')
    for file in unused_files:
        print(file)
