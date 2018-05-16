a = ['key', 'key2', 'key3']

b = ''.join(a)
print("\n\t''.join(a) {} >> {}\n".format(type(b), b))


b = ''.join(str(x+', ') for x in a)
print("\t''.join(str(x+', ') for x in a) {} >> {}\n".format(type(b), b))

b = ', '.join(map(str, a))
print("\t''.join(map(str, a)) {} >> {}\n".format(type(b), b))

# SQL Query
b = "'" + "', '".join(map(str, a)) + "'"
print("\t\"'\" + \"', '\".join(map(str, a)) + \"'\" {} >> {}\n".format(type(b), b))