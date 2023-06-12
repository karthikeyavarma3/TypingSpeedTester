from generator import *
import time
import random

print('''
                              Welcome to Typer-OC
                            '''
      )
time.sleep(2)

print('''
                                ....Loading....
                            ''')
time.sleep(2)


def words(userinput):
    words_cal = 0
    for i in range(len(userinput)):
        if userinput[i] == " ":
            words_cal+=1
    return words_cal

def speed(initial_time , final_time ,  userinput):
    delay_time = final_time - initial_time
    final_time_sec = round(delay_time, 2)
    speed = words(userinput)/final_time_sec                            
    final_speed = round(speed*60)

    return final_speed,final_time_sec




def errors(para, userinput , final_time_sec):
    error=0

    for i in range(0,len(para)):
        try:
            if para[i]!=userinput[i]:
                error+=1
        except:
            error+=1
    
    error_rate = error/final_time_sec

    return error , error_rate

def store_records(speed_test , error , error_rate , accuracy):
    fp = open('Records.txt' , 'a')
    fp.write(time.asctime(time.localtime()))
    fp.write(f"\n-->speed : {speed_test} wpm\n-->errors : {error}\n-->error rate : {error_rate} errors per sec\n-->Accuracy : {accuracy}\n")
    fp.close()
    
    

speed_test , accuracy = 0 , 0
while True:
    

    print(" Enter 1 to Start and 0 to quit ")
    user_input_ = int(input())

    if user_input_== 1:

        gnt = Generator_wpm()
        if 0<=speed_test<=38:
            para = gnt.beginner()
        elif 38<speed_test<=48 :
            para = gnt.medium()
        elif 48<speed_test<=60:
            para = gnt.advanced()
        elif speed_test>60:
            para = gnt.pro()

        
        

        print('''
                                ....loading....
        ''')
        time.sleep(2)

        print('''
                                        3
        ''')
        time.sleep(1)
        print('''
                                        2
        ''')
        time.sleep(1)
        print('''
                                        1
        ''')
        time.sleep(1)

        print(para)

        time_start = time.time()
        userinput = input()
        
        time_end = time.time()

        speed_test , final_time_sec = speed(time_start , time_end , userinput)
        error , error_rate = errors(para , userinput , final_time_sec)

        print('''
                                Results ...
        ''')
        time.sleep(2)

        print(f'''
                            Speed : {speed_test} wpm\n
                            No of errors : {error} , {error_rate} error per sec\n''')

        accuracy = ((len(userinput)-error)/len(userinput))*100
        if accuracy<0:
            accuracy=0

        print(f''' 
                            Accuracy : {accuracy}
            ''')

        store_records(speed_test , error , error_rate , accuracy)

    elif user_input_==0:
        print('''
                                            Thank you
        ''')
        break

    else:
        print("Invalid input - Try Again")





