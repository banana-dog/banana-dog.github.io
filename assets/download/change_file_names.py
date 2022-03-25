import os 

# здесь я указала путь к папке, из которой нужно импортировать файлы
folder = 'full_size' 
# файлы импортируются в виде списка, кладу его в переменную
pics = os.listdir(folder) 
# какое расширение должно быить у файлов
extension = ".jpg" 

for pic in pics:
    # программа не будет переименовывать файлы уже нужного расширения
    if not pic.endswith(extension): 
        new_file = pic + extension
        # используем os.path.join, 
        # чтобы компьютер без проблем нашел нужные файлы
        before = os.path.join(folder, pic)
        after = os.path.join(folder, new_file)
        os.rename(before, after) 