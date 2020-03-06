import hashlib
from PIL import Image, ImageDraw

floder_to_save = "~/Desctop" #Папка для сохранения по умолчанию(mac os)
pic_size = (16,16) # Размер картинки по умолчанию(!не рекомендуется менять!(наверное))


def toBin(str_heh): # превращает в бинарник и не только
    bin_mas = ('0000','0001','0010','0011','0100',
                '0101','0110','0111','1000','1001',
                '1010','1011','1100','1101','1110','1111')
    hex_mas = ('0','1','2','3',
            '4','5','6','7',
            '8','9','a','b',
            'c','d','e','f')
    ret_bin = ''
    set_color = []
    for i in range(len(str_heh)): 
        temp_ret_bin = bin_mas[hex_mas.index(str_heh[i])]
        if i < 3:
            set_color.append(int(hex_mas.index(str_heh[i])))
        ret_bin += temp_ret_bin 
    for i in range(len(set_color)):
        if set_color[i]*8 < 256:
            set_color[i] *= 8
        elif set_color[i]*4 < 256:
            set_color[i] *= 4
        elif set_color[i]*2 < 256:
            set_color[i] *= 2
    set_color = tuple(set_color) 
    return ret_bin,set_color



def file_to_md5(): # забирает файл и превращает его в md5
    #fname = input(r"Введите абсолютный путь до файла: ")
    fname = "text.txt" #Разобраться с путем
    file = open(fname)
    file_data = file.read()
    file_md5 = hashlib.md5(file_data.encode('utf-8')).hexdigest()
    file.close()
    return file_md5


def create_image(binr,color): # создает рисунок
    image = Image.new('RGB',pic_size,color)

    drw = ImageDraw.Draw(image)

    for x in range(int(pic_size[0] / 2)): 
        for y in range(int(pic_size[1])):
            if binr[x+y] == '1':
                drw.point([x,y])
                drw.point([pic_size[0] - x - 1,y])

    image.save('image.jpeg')


if __name__ == "__main__":
    binar, s_c = toBin(file_to_md5())
    create_image(binar,s_c)