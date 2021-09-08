from base_pic import BasePic
from base_file import BaseFile
from steganographizer import Stegan

def run():
    image_loc = input('Please enter the location of the image you wish to use: ')
    file_loc = input('Please enter the location of the text file you wish to hide: ')
    pic = BasePic(image_loc)
    file = BaseFile(file_loc)
    hide = Stegan(pic, file)
    hide.auto_run()
    print('Process complete')


if __name__ == '__main__':
    run()