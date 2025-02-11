import random
import time

# Users: Creating a list of users in the format user_1, user_2, ..., user_17
user = [f"user_{i+1}" for i in range(17)]

# Messages: List of entry messages and chat messages
enter_message = [f"message_{i+1}" for i in range(3)]  # Example entry messages
messages = [f"message_{i+4}" for i in range(21)]  # Example chat messages starting from message_4

# Variables
Active = True  # Control variable to keep the chat running
posisubtime = ["one", "two", "three", "five", "nine", "eleven"]  # Possible subscription times
mesdesub = ""  # Placeholder for the chosen subscription time
Sub = f" has joined for {mesdesub} months"  # Subscription message template

# Initial simulation: Simulate users entering the chat with a random message
for i in range(11):  # Loop to simulate the first 11 entries
    print(f"{random.choice(user)}: {random.choice(enter_message)}")  # Print a random user and their entry message
    time.sleep(random.randint(2, 5))  # Wait a random time between 2 and 5 seconds

# Chat simulation
while Active:
    # 20% chance to simulate a subscription message
    if random.random() < 0.2:
        user_sub = random.choice(user)  # Choose a random user
        mesdesub = random.choice(posisubtime)  # Choose a random subscription time
        finalchat = f"{user_sub}{Sub.replace('{mesdesub}', mesdesub)}"  # Format the subscription message
    else:
        # Regular chat message
        takemessage = random.choice(messages)  # Choose a random chat message
        takeuser = random.choice(user)  # Choose a random user
        finalchat = f"{takeuser}: {takemessage}"  # Format the chat message

    print(finalchat)  # Print the chat message
    time.sleep(random.randint(1, 4))  # Wait a random time between 1 and 4 seconds
