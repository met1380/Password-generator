# این اسکریپت سه لیست را از کتابخانه استرینک میگیرد. از کاربر نوع لیست را میگیرد
# سپس بصورت رندوم ایندکس هایی را میگیرد و آنهارا در حلقه به رشته پسورد اضافه میکند
# با کتابخانه چهارم آنهارا در کلیپ بورد کپی میکند
import string
import random
import os
import pyperclip
os.system('cls')
while True :
    ask_type=input('enter including characters(1:lower , 2:lower and upper , 3: 1,2 and numbers): ')
    if ask_type == '1':
        char_list = list(string.ascii_lowercase)
    elif ask_type=='2':
        char_list = list(string.ascii_letters)
    elif ask_type=='3':
        char_list = list(string.ascii_letters) + list(string.digits)        
    else : print('invalid type, default is setted to lower') ; char_list = list(string.ascii_lowercase)
    while True:
        try:
            pass_length = int(input('enter the password length : '))
            break
        except:
            print('ERROR : enter a number !')
    count = 0
    guessed_pass = ''
    while count <= pass_length:
        RCI = random.randint(0, len(char_list)-1)  # random charachter index
        guessed_pass=guessed_pass.__add__(char_list[RCI])
        count += 1
    print('the pass is : *** ',guessed_pass,' ***')
    pyperclip.copy(guessed_pass)
    print('password is copied to clipboard ')
    print('==============================================')