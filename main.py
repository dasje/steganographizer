from PIL import Image
import numpy as np

#image class

class Pics:
    def __init__(self, picture):
        self.picture = picture #contains picture location

        #create picture object
        self.image = Image.open(self.picture)
        self.image_array = self.convert_to_array()
        self.eight_bit_array = None
        self.msb_array = None

    def get_dimensions(self):
        """Returns image size as tuple (width, height)"""
        return self.image.size

    def convert_to_array(self):
        """Converts image to numpy array"""
        self.image.convert(mode="P")
        return np.array(self.image)

    def convert_array_to_8bit(self):
        """Converts the pixels in array to 8bit binary"""
        eba = []
        bin_color_dic = {}
        for x in self.image_array:
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
        self.eight_bit_array = eba

    def get_msbs(self):
        """Creates array of most significant bits from each pixel"""
        msb_array = []
        for x in self.eight_bit_array:
            col = []
            for y in x:
                rgb = []
                for color in y:
                    rgb.append(color[:4])
                col.append(rgb)
            msb_array.append(col)
        msb_array = np.array(msb_array)
        self.msb_array = msb_array

#get dimensions
#convert image to numpy array
#split pixels and return msb's of pixels

x = Pics('test_images/test1.jpg')
#print(x.image_array)
x.convert_array_to_8bit()
print(x.eight_bit_array)
x.get_msbs()
print(x.msb_array)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
