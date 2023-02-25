#Pequeños ejemplos para aprender lo más básico de python

def hi(name):
    print("Hi " + name + "!")

girls = ["Rachel","Mónica","Phoebe","Ola","You"]

for name in girls:
    hi(name)
    print("Next girl")


for i in range(1,6):
    print(i)