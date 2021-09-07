from PIL import Image
import numpy as np

from base_pic import BasePic
from base_file import BaseFile

class Stegan:
    def __init__(self, pic, file):
        self.pic = pic
        self.file = file
        self.pic_array = self.pic.bin_array
        self.file_array = self.file.binary_array
        self.pic_msb_array = None
        self.pic_lsb_array = None
        self.combined_arrays = None

    def split_MSB_LSB_in_pic(self):
        """Splits the binary elements in an array into MSB and LSB. Returns two arrays"""
        msb = []
        lsb = []
        for x in self.pic_array:
            col_msb = []
            col_lsb = []
            for y in x:
                rgb_msb = []
                rgb_lsb = []
                for color in y:
                    rgb_msb.append(color[:4])
                    rgb_lsb.append(color[4:])
                col_msb.append(rgb_msb)
                col_lsb.append(rgb_lsb)
            msb.append(col_msb)
            lsb.append(col_lsb)
        return [msb, lsb]

    def combine_arrays(self):
        """Takes the MSBs from the pic and systematically adds each 4-bit from the file array in place of the LSB"""
        countdown = 0
        eba = []
        while True:
            for x in self.pic_msb_array:
                col = []
                for y in x:
                    rgb = []
                    for color in y:
                        try:
                            rgb.append(self.convert_binary(color + self.file_array[countdown]))
                            countdown += 1
                        except:
                            rgb.append(self.convert_binary(self.fill_to_8bit(color)))
                    col.append(rgb)
                eba.append(col)
            break
        return eba

    def fill_to_8bit(self, var):
        """Fills a variable that is less than 8 bits up to length 8 with 0's to the right"""
        return var.ljust(8, '0')

    def convert_binary(self, bin):
        return int(bin, 2)

    def convert_back_to_image(self):
        """Converts the processed array back to an image"""
        data = Image.fromarray(self.combined_arrays)
        data.save('{}_steganographized.{}'.format(self.pic.file_name, self.pic.file_extension))

    def auto_run(self):
        two_arrays = self.split_MSB_LSB_in_pic()
        self.pic_lsb_array = two_arrays[1]
        self.pic_msb_array = two_arrays[0]
        self.combined_arrays = self.combine_arrays()
        self.convert_back_to_image()


x = BasePic("imgs/testimg01.jpg")
y = BaseFile("imgs/small.txt")
z = Stegan(x, y)
z.auto_run()
#print(a)
