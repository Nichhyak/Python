import time  

# Asking the user to enter the time in seconds
my_time = int(input("Enter the time in seconds: "))

# Loop to count down from my_time to 0
for x in range(my_time, 0, -1):
    # Calculate hours, minutes, and seconds
    hours = x // 3600
    minutes = (x % 3600) // 60
    seconds = x % 60
    
    # Printing the time in the format HH:MM:SS
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    
    # Setting (wait) 1 second before the next loop iteration
    time.sleep(1)

# When the loop ends, prints "Your time's up!"
print("Your time's up!")
