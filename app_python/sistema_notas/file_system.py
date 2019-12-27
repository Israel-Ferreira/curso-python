import shutil


class FileSystem:
    def __init__(self,file_name):
        self.file_name = file_name


    def read_file(self):
        fl = open(self.file_name,"r")
        content = fl.read()
        return content


    def write_file(self,text):
        self.handle_file(text,"w")


    def append_file(self,text):
        self.handle_file(text,"a")


    def copy_file(self,directory):
        shutil.copy(self.file_name,directory)


    def move_file(self,directory):
        shutil.move(self.file_name,directory)

    def handle_file(self,text,mode):
        if mode == "w" or mode == "a":
            fl = open(self.file_name, mode)
            fl.write(text)
            fl.close()

    
    

