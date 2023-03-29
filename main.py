import re

with open('document.txt') as f:
    contents = f.read()

numbers = re.findall(r'\d+', contents)
total = sum(map(int, numbers))
print('Total:', total)
