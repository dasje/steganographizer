from os import path

class BaseFile:
    def __init__(self, file_loc):
        self.file_loc = file_loc
        with open(file_loc, 'r') as obj:
            self.file = obj.read()
        self.binary_array = None
        self.file_name = None
        self.file_extension = None
        self.auto_run()

    def to_binary(self):
        """Converts the file to a list of binary numbers"""
        return_array = []
        for i in range(len(self.file)):
            # ord converts to ascii, format converts to binary
            return_array.append(format(ord(self.file[i]), '08b')[:4])
            return_array.append(format(ord(self.file[i]), '08b')[4:])
        return return_array

    def get_file_extension(self):
        """Returns the extension type of the input file"""
        return path.splitext(path.split(self.file_loc)[-1])[-1][1:]

    def get_file_name(self):
        """Returns the root file name"""
        return path.splitext(path.split(self.file_loc)[-1])[0]

    def auto_run(self):
        self.binary_array = self.to_binary()
        self.file_name = self.get_file_name()
        self.file_extension = self.get_file_extension()

x = BaseFile("imgs/small.txt")
print(x.to_binary())
print(x.get_file_extension())
print(x.get_file_name())