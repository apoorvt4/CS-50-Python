# This code show how to make file by asking there name

'''name = input("What's your name?")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")'''

# This code show to read a already exist file

'''with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("Hello,", line, line.rstrip())'''

# Another method of doing this

'''with open("names.txt", "r") as file:
    for line in file:
        print("hello,", line.rstrip())'''

# Another Method of doing this
names = []
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=True):
    print(f"hello, {name}") 


