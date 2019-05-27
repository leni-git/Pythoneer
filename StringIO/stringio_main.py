# Latest 27-May-2019
# Made by Leni ♡

# Python Ver 3.6.5
# io - Core tools for working with streams
# https://docs.python.org/3/library/io.html#io.RawIOBase

import io

# Text I/O  + + + + + + + + + + + + + + + + +
f = io.StringIO("some initial text data")
print('io.StringIO: {}'.format(type(f)))
print(f.getvalue())
f.close()
# End [ Text I/O ] + + + + + + + + + + + + + + + + +

print('{}'.format('- ' * 20))

# Binary I/O  + + + + + + + + + + + + + + + + +
binary_f = io.BytesIO(b"some initial binary data: \x00\x01")
print('io.BytesIO: {}'.format(type(binary_f)))
print(binary_f.getvalue())
binary_f.close()
# End [ Binary I/O ] + + + + + + + + + + + + + + + + +

print('{}'.format('- ' * 20))

# Raw I/O  + + + + + + + + + + + + + + + + +
# f = io.RawIOBase()
# with open('kitty.raw', 'rb') as file:
#     f.write(file.read())
#     # { NotImplementedError }
#     # ㄴPython internal error, It generates when part of important was not implemented.

file_f = io.FileIO('kitty.raw')
# FileIO(name, mode='r', closefd=True, opener=None)
# You have to insert a file name.
# `FileExistsError` will be raised if it already exists when opened for creating.
print('io.FileIO: {}'.format(type(file_f)))
print(file_f.read())
file_f.close()
# End[Raw I / O] + + + + + + + + + + + + + + + + +

# Compare files + + + + + + + + + + + + + + + + +
binary_raw = io.BytesIO()
with open('kitty.raw', 'rb') as file:
    binary_raw.write(file.read())

if binary_raw.getvalue() == file_f.read():
    print('same')
else:
    print('not same')
# End [ Comapare ] + + + + + + + + + + + + + + + + +
