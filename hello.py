'''def main():
    name = input("what's your name\n")
    print(name)'''

password = "Apoorv"
attempt = 3

while True > 0:
    attempt = input("Enter the correct password\n")
if attempt == password:
    print("Correct Password!")
    exit

if attempt < 1:
    print(f"wrong password{attempt}")
else:
    print("password wrong")
    
