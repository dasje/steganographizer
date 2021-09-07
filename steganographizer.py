import numpy as np

from base_pic import BasePic
from base_file import BaseFile

class Stegan:
    def __init__(self, pic_array, file_array):
        self.pic_array = pic_array
        self.file_array = file_array

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
        print(np.array(msb))
        print(np.array(lsb))
        return [msb, lsb]

    def combine_arrays(self):
        """Takes the MSBs from the pic and systematically adds each 4-bit from the file array in place of the LSB"""
        countdown = len(self.file_array)


    def fill_to_8bit(self):
        """Systematically goes through an array to look for bits of length less than 8. Fill the bit with zeroes to len 8"""
        pass

    def auto_run(self):
        self.split_MSB_LSB_in_pic()

x = BasePic("imgs/testimg01.jpg")
x.auto_run()
y = BaseFile("imgs/small.txt")
y.auto_run()
z = Stegan(x.bin_array, y.binary_array)
a = z.split_MSB_LSB_in_pic()
#print(a)