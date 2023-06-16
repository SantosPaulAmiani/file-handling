import re
f = open('cat.txt', 'r')

text = f.read()
match = '@' in text
print(match)


pattern = '@'
print(re.search(pattern,text))
match2 = re.findall(pattern,text)
print(match2)
print(len(match2))

for x in match2:
    print(x)

text = 'My phone number is 923-575-8888 '
numbers = re.search(r' \d{3}-\d{3}-\d{4} ', text)
print(numbers)
print(re.findall(r'...at', 'The cat in the hat went splat'))



