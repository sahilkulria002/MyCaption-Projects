import os
a = input('Input the Filename')
b = os.path.splitext(a) #b is tuple with second element as extention name
ext = {'.py': 'python', '.img' : 'image'} # complete file type name getting from extention, we can add more
print('The extension of the file is :', end=' ')
print(ext[b[1]])