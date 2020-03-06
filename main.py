import hashlib
from PIL import Image, ImageDraw

floder_to_save = "~/Desctop" #Папка для сохранения по умолчанию(mac os)
#print(hashlib.md5("a".encode('utf-8')).hexdigest())


def toHex(str_heh):
    bin_mas = ('0000','0001','0010','0011','0100',
                '0101','0110','0111','1000','1001',
                '1010','1011','1100','1101','1110','1111')
    hex_mas = ('0','1','2','3',
            '4','5','6','7',
            '8','9','a','b',
            'c','d','e','f')
    ret_bin = ''
    for i in range(len(str_heh)):  # '1d4a' -> '0001 1101 0100 1000'   
        temp_ret_bin = bin_mas[hex_mas.index(str_heh[i])]# компорация 1 и 2 массива со сложением рез.
        ret_bin += temp_ret_bin  
    
    return ret_bin




#fname = input(r"Введите абсолютный путь до файла: ")
fname = "text.txt" #Разобраться с путем
file = open(fname)
file_data = file.read()
file_md5 = hashlib.md5(file_data.encode('utf-8')).hexdigest()
file.close()

image = Image.new('1',[16,16])#Куб 16х16, где есть 2 одинаковых прямоугольника 8х16 

toHex(file_md5)


"""
def toHex(s):
    lst = []
    for ch in s:
        hv = hex(ord(ch)).replace('0x', '')
        if len(hv) == 1:
            hv = '0'+hv
        lst.append(hv)
    
    return reduce(lambda x,y:x+y, lst)
"""


