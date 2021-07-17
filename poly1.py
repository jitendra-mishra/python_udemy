class File:
    def __init__(self, name, extension):
        self.name = name
        self.extension = extension

    def open(self):
        print("Opening a generic file")

class PDFFile(File):
    def __init__(self, name):
        File.__init__(self, name, ".pdf")
    def open(self):
        print(f"Opening a PDF file, named {self.name}")

class TextFile(File):
    def __init__(self, name):
        File.__init__(self, name, ".txt")

    def open(self):
        print(f"Opening a Text file, named {self.name}")

def open_files(files):
    for file in files:
        file.open()

pdf1 = PDFFile("p1")
pdf2 = PDFFile("myp1")
txt1 = TextFile("text1")

files = [pdf1, pdf2, txt1]

open_files(files)
