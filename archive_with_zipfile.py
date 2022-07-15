from zipfile import ZipFile

zip_ = ZipFile('resources/hello.zip')
print(zip_.namelist())
# zip_.extract('Hello.txt', 'tmp')
text = zip_.read('Hello.txt')
print(text)
zip_.close()
with ZipFile('resources/hello.zip') as myzip:
    myzip.extract('Hello.txt')
