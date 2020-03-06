import hashlib
from PIL import Image, ImageDraw

floder_to_save = "~/Desctop" #Папка для сохранения по умолчанию(mac os)
pic_size = (16,16) # Размер картинки по умолчанию(!не рекомендуется менять!(наверное))


def toBin(str_heh):
    bin_mas = ('0000','0001','0010','0011','0100',
                '0101','0110','0111','1000','1001',
                '1010','1011','1100','1101','1110','1111')
    hex_mas = ('0','1','2','3',
            '4','5','6','7',
            '8','9','a','b',
            'c','d','e','f')
    ret_bin = ''
    for i in range(len(str_heh)): 
        temp_ret_bin = bin_mas[hex_mas.index(str_heh[i])]
        ret_bin += temp_ret_bin  
    return ret_bin




#fname = input(r"Введите абсолютный путь до файла: ")
fname = "text.txt" #Разобраться с путем
file = open(fname)
file_data = file.read()
file_md5 = hashlib.md5(file_data.encode('utf-8')).hexdigest()
file.close()

binar = toBin(file_md5)

image = Image.new('1',pic_size)#Куб 16х16, где есть 2 одинаковых прямоугольника 8х16 

drw = ImageDraw.Draw(image)

for x in range(int(pic_size[0] / 2)):
    for y in range(int(pic_size[1])):
        if binar[x+y] == '1':
            drw.point([x,y])
            drw.point([pic_size[0] - x,y])

image.save('image.jpeg')





