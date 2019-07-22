# Latest 22-July-2019
# Made by Leni ♡

import io


def endian_converter(*, in_data):

    in_data.seek(0)
    try:
        with open(in_data, 'rb') as input_data:
            data = input_data.read()
    except Exception as e:
        print('open error')

    else:
        temp = io.BytesIO()

        i = 0
        file_size = len(data)
        while i < file_size:
            temp.write(data[i+1].to_bytes(length=1, byteorder='little'))
            temp.write(data[i].to_bytes(length=1, byteorder='little'))
            i += 2

        # with open('result.pcm', 'wb') as output:
            # temp.seek(0)
            # output.write(temp.read())

        temp.seek(0)
        return temp.read()

# USE
# a = endian_convert(in_data='data.pcm')
# a.seek(0)
# a.read()
