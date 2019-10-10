# -*- coding: utf-8 -*-

import os, time, shutil, zipfile


# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.


class SortedFile:

    def __init__(self, folder_path, current_dir):
        self.newdir = current_dir
        self.newdict = {}
        if zipfile.is_zipfile(folder_path):
            self.zip_path = folder_path
            self.folder_path = os.path.dirname(folder_path)
            self._try_zip()
        else:
            self.folder_path = folder_path
            self.get_file_path()

    def _try_zip(self):
        with zipfile.ZipFile(self.zip_path) as zip_ref:
            for file in zip_ref.namelist():
                full_file_path = os.path.normpath(os.path.join(self.folder_path, file))
                if '.png' in full_file_path:
                    file_name = file
                    date_time_file = zip_ref.getinfo(file).date_time
                    self.newdict[str(full_file_path)] = [str(full_file_path), file_name, date_time_file]
            self._extract_files_from_zip()

    def get_file_path(self):
        walking = os.walk(self.folder_path)
        for dirpath, dirnames, filenames in walking:
            for file in filenames:
                file_dir = dirpath + '\\'
                file_path = file_dir + file
                self.newdict[file_path] = [file_path, file]
        self.add_time_in_newdict()

    def show_path_of_the_source_file(self):
        for i in self.newdict.keys():
            print(i)

    def add_time_in_newdict(self):
        for k, v in self.newdict.items():
            get_time = os.path.getmtime(k)
            gm_time = time.gmtime(get_time)
            v.append(gm_time)
        self.copy_files()

    def copy_files(self):
        for k, v in self.newdict.items():
            print(v)
            sort_file_folder = os.path.normpath(f'{v[2][0]}/{v[2][1]}')
            print(sort_file_folder)
            fullpath = os.path.join(self.folder_path, self.newdir, sort_file_folder)
            norm_path = os.path.normpath(fullpath)
            new_file_path = os.path.join(norm_path, v[1])

            if not os.path.exists(norm_path):
                os.makedirs(norm_path)
            if not os.path.exists(new_file_path):
                shutil.copy2(k, new_file_path)

    def _extract_files_from_zip(self):
        for k, v in self.newdict.items():
            sort_file_folder = os.path.normpath(f'{v[2][0]}/{v[2][1]}')
            fullpath = os.path.join(self.folder_path, self.newdir, sort_file_folder)
            norm_path = os.path.normpath(fullpath)
            if not os.path.exists(norm_path):
                os.makedirs(norm_path)
            with zipfile.ZipFile(self.zip_path, 'r') as zip_ref:
                file_in_zip_archive = v[1]
                print(file_in_zip_archive)
                read_file = zip_ref.read(file_in_zip_archive)
                new_file_path = os.path.join(norm_path, os.path.basename(file_in_zip_archive))
                with open(new_file_path, 'wb') as write_file:
                    write_file.write(read_file)

    def count_files(self):
        count = 0
        for _ in self.newdict.keys():
            count += 1
        print(count)


path = os.getcwd()
sort_path = 'icons.zip'
fullpath = os.path.join(path, sort_path)
normalized_path = os.path.normpath(fullpath)

search = SortedFile(normalized_path, 'sort_by_year')

# search.show_path_of_the_source_file()
# search.get_file_path()
# search.add_time_in_newdict()
# search.copy_files()
# search.count_files()


# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
