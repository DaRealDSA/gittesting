# The collaz collection
running = True
def collaz(number): 
    global running 
    method_a = number // 2 
    method_b = 3 * number + 1 
    if number % 2 == 0: 
        if method_a == 1: 
            running = False 
        print(method_a) 
    elif number % 2 == 1: 
        if method_b == 1: 
            running = False 
        print(method_b) 
    else: 
        running = False
print("Enter number:")
while running: 
    try: 
        response = int(input()) 
    except ValueError: 
        print("Please enter numbers only!") 
        continue 
    else: collaz(response)