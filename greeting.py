import time

def greet(name):
    if(time.strftime("%H", time.localtime()) >= "05" and time.strftime("%H", time.localtime()) < "12"):
        print(f"Good Morning, {name}")
    elif(time.strftime("%H", time.localtime()) >= "12" and time.strftime("%H", time.localtime()) < "17"):
        print(f"Good Afternoon, {name}")
    elif(time.strftime("%H", time.localtime()) >= "17" and time.strftime("%H", time.localtime()) < "20"):
        print(f"Good Evening, {name}")
    else:
        print(f"Good Night, {name}")

greet("John")