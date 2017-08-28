import sys

if len(sys.argv) == 1:
    text = raw_input("Please enter binary data: ")
    chars = text.split()
else:
    chars = sys.argv[1:]

str_ = ""

for code in chars:
    code = int(code, 2)
    char = chr(code)
    str_ += char
print(str_)