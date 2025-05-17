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

### Using match case give me the above code

def greeting(name):
    current_hour = int(time.strftime("%H", time.localtime()))
    match current_hour:
        case hour if 5 <= hour < 12:
            print(f"Good Morning, {name}")
        case hour if 12 <= hour < 17:
            print(f"Good Afternoon, {name}")
        case hour if 17 <= hour < 20:
            print(f"Good Evening, {name}")
        case _:
            print(f"Good Night, {name}")

greet("Aditya")
greeting("John")