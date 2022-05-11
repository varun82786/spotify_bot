import random
test_data=[]


for i in range(101):
    if i%3==0:
        test_data.append(["ramdevbyd@gmail.com", "ratQ129#2!@", "Ram dev"])
    elif(i%2==0):
        test_data.append(["ramdevgwo@gmail.com", "ratQ129#2!@", "Ram dev"])
    else:
        name = "ramdev"+random.choice(list(map(chr, range(97, 123)))) + \
            random.choice(list(map(chr, range(97, 123)))) + \
            random.choice(list(map(chr, range(97, 123))))
        domain = "@gmail.com"
        email = name+domain
        test_data.append([email, "ratQ129#2!@", "Ram dev"])
        
    
    

print(test_data)
