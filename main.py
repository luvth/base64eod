import base64
import os 

os.system('clear')

print("Made by luvthexclusive")
print(" ")

def encode_base64():
    a = input("Base 64 encoder : ")
    a_bytes = a.encode("utf-8")
    encoded_bytes = base64.b64encode(a_bytes)
    encoded_str = encoded_bytes.decode("utf-8")
    print(a , "= " , f"Base64 : {encoded_str}")

def decode_base64():
    a = input("Base 64 decoder : ")
    try:
        decoded_bytes = base64.b64decode(a)
        decoded_str = decoded_bytes.decode("utf-8")
        print(f"Texte décodé : {decoded_str}")
    except Exception as e:
        print("Not base64 ")

def main():
    while True:
        action = input("Base64 : encode , decode   ~/").strip().lower()

        if action == "encode":
            encode_base64()
        elif action == "decode":
            decode_base64()
        elif action == "exit":
            break
        else:
            print("Not a valid option" )

if __name__ == "__main__":
    main()
