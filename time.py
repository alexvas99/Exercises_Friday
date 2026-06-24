import time


# def multiply_time(num1, num2):
#     time1 = time.time()
#     result = num1*num2
#     time2 = time.time()
#     print(f"The answer is {result} - this took {time2-time1} seconds")

# multiply_time(21342424265340394909034993469, 9324354938925892)

def stopwatch():

    proceed = input("Press Enter to start timer: ")
    start_time = time.time()

    proceed = input("Press Enter to stop timer: ")
    finish_time = time.time()
    
    print(f"{finish_time - start_time} seconds")

stopwatch()


