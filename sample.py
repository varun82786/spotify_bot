import random
print(list(map(chr, range(102, 123))))


name = "ramdev"+random.choice(list(map(chr, range(60, 123))))+ \
    random.choice(list(map(chr, range(60, 123)))) + \
    random.choice(list(map(chr, range(60, 123))))
domain="@gmail.com"
email=name+domain 
print(email)