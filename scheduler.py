import time

def pump1():
    print("Execution pump 1")
    time.sleep(2)
    return 10

def pump2():
    print("Execution pump 2")
    time.sleep(3)
    return 20

def machine1(oil):
    print("Execution machine 1")
    time.sleep(5)
    return max(0, oil - 25), 1 if oil >= 25 else 0

def machine2(oil):
    print("Execution machine 2")
    time.sleep(3)
    return max(0, oil - 5), 1 if oil >= 5 else 0

def watchdog():
    oil = 0
    motor_count = 0
    wheel_count = 0
    while True:
        oil += pump1() if oil < 50 else 0
        oil += pump2() if oil < 50 else 0
        oil = min(50, oil)
        if wheel_count // 4 < motor_count:
            oil, motor = machine1(oil)
            motor_count += motor
        else:
            oil, wheel = machine2(oil)
            wheel_count += wheel
        print("Oil: ", oil)
        print("Motors: ", motor_count)
        print("Wheels: ", wheel_count)
        time.sleep(5)
        oil += pump1() if oil < 50 else 0
        time.sleep(15)
        oil += pump2() if oil < 50 else 0
        oil = min(50, oil)
        if wheel_count // 4 < motor_count:
            oil, motor = machine1(oil)
            motor_count += motor
        else:
            oil, wheel = machine2(oil)
            wheel_count += wheel
        print("Oil: ", oil)
        print("Motors: ", motor_count)
        print("Wheels: ", wheel_count)
        time.sleep(5)

if name == "main":
    watchdog()
