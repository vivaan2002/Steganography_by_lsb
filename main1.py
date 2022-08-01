import time
import numpy as np #For mathamatics calculation
from PIL import Image #Python lib to read image

file=open("Message.txt","r")
data=file.read()
file.close()

result=""

def Encode(src, message, dest):

    img = Image.open(src, 'r') #Open cover image
    width, height = img.size #Dimetion of cover image
    array = np.array(list(img.getdata())) #Image to intgral value

    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4

    total_pixels = array.size//n #count number of pixel

    message += "@r7D1" 
    b_message = ''.join([format(ord(i), "08b") for i in message]) #Add a Point at which decoding will stop 
    req_pixels = len(b_message) 

    if req_pixels > total_pixels: 
        print("ERROR: Need larger file size") # check if secret data can be fited in image or not
    


    else:
        index=0
        for p in range(total_pixels):
            for q in range(0, 3):
                if index < req_pixels:
                    array[p][q] = int(bin(array[p][q])[2:9] + b_message[index], 2) # At this point we are replacing 2 lsb
                    index += 1

        array=array.reshape(height, width, n)
        enc_img = Image.fromarray(array.astype('uint8'), img.mode)
        enc_img.save(dest) #this 3 line define creating stago
        print("Image Encoded Successfully")

def Decode(src):

    img = Image.open(src, 'r')
    array = np.array(list(img.getdata()))

    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4
    total_pixels = array.size//n
    #start
    hidden_bits = ""
    for p in range(total_pixels):
        for q in range(0, 3):
            hidden_bits += (bin(array[p][q])[2:][-1])

    hidden_bits = [hidden_bits[i:i+8] for i in range(0, len(hidden_bits), 8)]
    #end reading all bits of stago image
    #start
    message = ""
    for i in range(len(hidden_bits)):
        if message[-5:] == "@r7D1":
            break
        else:
            message += chr(int(hidden_bits[i], 2))
    #end read bit and covert it into the character until we reach end or @r7D1 is found
    #start
    if "@r7D1" in message:
        result="Hidden Message:"+message[:-5]
        print(result)
    else:
        result="No Hidden Message Found"
        print(result)
    #end if @r7D1 is found in msg remaing msg is returned or else No Hidden Message Found is returned

def Stego():
    print("--Welcome to @r7D1--")
    print("1: Encode")
    print("2: Decode")

    func = input()

    if func == '1':
        print("Enter Source Image Path")
        src = input()
        print("Enter Message to Hide")
        message = data
        print("Enter Destination Image Path")
        dest = input()
        print("Encoding...")
        st=time.time()
        Encode(src, message, dest)
        et=time.time()
        print("Time = ",et-st)

    elif func == '2':
        print("Enter Source Image Path")
        src = input()
        print("Decoding...")
        st=time.time()
        Decode(src)
        et=time.time()
        print("Time = ",et-st)
        print(result)

    else:
        print("ERROR: Invalid option chosen")

Stego()
