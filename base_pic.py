from PIL import Image
import numpy as np
from os import path

class BasePic:
    def __init__(self, file_loc):
        self.file = Image.open(file_loc, "r")
        self.bin_array = None
        self.file_name = None
        self.file_extension = None
        self.auto_run()

    def to_binary_array(self):
        """Takes a picture object and converts it to an array of bytes"""
        im_data = np.asarray(self.file)
        eba = []
        bin_color_dic = {}
        for x in im_data:
            col = []
            for y in x:
                rgb = []
                for color in y:
                    if color not in bin_color_dic:
                        bin_color_dic[color] = bin(color)[2:].zfill(8)
                    rgb.append(bin_color_dic[color])
                col.append(rgb)
            eba.append(col)
        eba = np.array(eba)
        return eba

    def get_file_extension(self):
        """Gets the file extension from the file name"""
        return path.splitext(path.split(self.file.filename)[-1])[-1][1:]

    def get_file_name(self):
        """Gets the base of the file name"""
        return path.splitext(path.split(self.file.filename)[-1])[0]

    def auto_run(self):
        """Auto fill the variables at the head of the object"""
        self.bin_array = self.to_binary_array()
        self.file_extension = self.get_file_extension()
        self.file_name = self.get_file_name()

