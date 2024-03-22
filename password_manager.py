from cryptography.fernet import Fernet

def load_key():                        # to load the key to encrypt the password
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


print("Hello and welcome to my python password manager!")

master_pwd = input("Enter the master password: ")

key = load_key()        # to load the key
fer = Fernet(key)       # to initialize the encryption object

'''
def write_key():                        # to create the key to encrypt the password
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)

write_key()
'''

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            user, pwd = line.rstrip().split("|")
            print("Username: "+user+"   |   Password: "+fer.decrypt(pwd.encode()).decode())


def add():
    name = input("Enter the account username: ")
    pwd = input("Enter the password: ")
    
    with open("passwords.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")       # to encrypt the pwd in its bytes form

if master_pwd == "Spondan@08":
    while True:
        while True:
            mode = input("Enter the mode you want:\nEnter 1 to view the password.\nEnter 2 to add new password\nEnter 3 to quit\nEnter your choice: ").strip()
            if mode.isdigit():
                mode = int(mode)
                break
            else:
                print("Enter valid mode.")
        
        if mode == 1:
            view()
        elif mode == 2:
            add()
        elif mode == 3:
            break   
        else:
            print("Invalid mode.")
else:
    print("Wrong Password. Please try again later.")

