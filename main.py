import hashlib
from PIL import Image, ImageDraw

floder_to_save = "~/Desctop" #Папка для сохранения по умолчанию(mac os)
#print(hashlib.md5("a".encode('utf-8')).hexdigest())


#fname = input(r"Введите абсолютный путь до файла: ")
fname = "text.txt" #Разобраться с путем
file = open(fname)
file_data = file.read()
file_md5 = hashlib.md5(file_data.encode('utf-8')).hexdigest()
file.close()

image = Image.new('1',[16,16])#Куб 16х16, где есть 2 одинаковых прямоугольника 8х16 

print(type(file_md5))
he = hex(file_md5)
print(type(he))


"""
hash_md5 = hashlib.md5()

with open(fname, "rb") as f:
    for chunk in iter(lambda: f.read(4096), b""):
        hash_md5.update(chunk)

print(hash_md5.hexdigest())
"""