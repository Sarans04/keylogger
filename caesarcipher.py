def encrypt(sentence,key,val):
    cipher_string=""
    for letter in sentence:
        if letter.isspace():
            cipher_string+=''
            continue
        index=val.find(letter.lower())
        index=index+key%len(val)
        cipher_string+=val[index]
    print("Encrypted String : " + cipher_string)
    return 
def decrypt(sentence,key,val):
    cipher_string=""
    for letter in sentence:
        if letter.isspace():
            cipher_string+=''
            continue
        index=val.find(letter)
        index=(index-key)%len(val)
        cipher_string+=val[index]
    print("Decrypted String : " + cipher_string)
    return 
def main():
    val="abcdefghijklmnopqrstuvwxyz"
    print("""
░█████╗░░█████╗░███████╗░██████╗░█████╗░██████╗░  ░█████╗░██╗██████╗░██╗░░██╗███████╗██████╗░
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗  ██╔══██╗██║██╔══██╗██║░░██║██╔════╝██╔══██╗
██║░░╚═╝███████║█████╗░░╚█████╗░███████║██████╔╝  ██║░░╚═╝██║██████╔╝███████║█████╗░░██████╔╝
██║░░██╗██╔══██║██╔══╝░░░╚═══██╗██╔══██║██╔══██╗  ██║░░██╗██║██╔═══╝░██╔══██║██╔══╝░░██╔══██╗
╚█████╔╝██║░░██║███████╗██████╔╝██║░░██║██║░░██║  ╚█████╔╝██║██║░░░░░██║░░██║███████╗██║░░██║
░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝  ░╚════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝""")
    word=input("e or d :").lower()
    if word == 'e':
        sentence=input("Sentence :")
        key=int(input("Key"))
        encrypt(sentence,key,val)
    elif word == 'd':
        sentence=input("Enter Encrypted String :")
        key=int(input("Key"))
        decrypt(sentence,key,val)
    else:
        print("Enter valid character")
        main()
    return
main()