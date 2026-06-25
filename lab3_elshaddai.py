
# Elshaddai l Lab 3 l Hustle

# Ticket 1
username = "queen"
# 4
print (len(username))
# yes len() counted every character and symbols included


#Ticket 2
print (username[0])
print(username[len(username) - 1])
# "q" and "n" will print
# because the number minus 1 is the index number


#Ticket 3
print("Welcome to Loop, @" + username + "!")
print(f"Welcome to Loop, @{username}!")
# yes both lines will look identical on screen
# the concatention was easier because it requires less code


#Ticket 4
#username[0] = "X" #run this, it breaks on purpose
# Error message: TypeError: 'str' object does not support item assignment
print(username.upper())
# for a string, immutable means that once a string is made you cannot change a letter inside it. To change it you build a brand new string


#Ticket 5
feed = ["First Post!", "At the gym", "I love my dog!"]
print(len(feed))
print(feed[0])
# The count will be 3 and the "First Post!" caption will print first
# I used index 0


#Ticket 6
feed.append("Loving this weather")
# The index is 3
# Since python starts counting at 0, the fourth post has the index of3


#Ticket 7
feed.pop(0)
feed.sort()
print(feed)
# The post that was at index 0 gets removed and the rest are in alphabetical order
# .pop(0) removed what was in idex 0 and .sort(0) rearranged the list to alphabetical order


#Ticket 8
profile = {"username": "queen", 
"followers": 200,
"verified": False}
print(profile["followers"])
#print (profile[0])
# Error message: KeyError: 0 (Dictionaries do not use numerical indexes)
# Keys are like labels and make things easier to find. As for lists, the order matters. And dictionaries look up specific things by name


#Ticket 9
profile["followers"] = profile["followers"] +50
profile["bio"] = "Live Laugh Love Life!"
print(profile)
print(profile.get("age"))
# When the key is missing, it prints "None"
# It's safer because your code won't give you an error message or crash


#Ticket 10
profile = {"username":"@queen", 
"followers": 250}
feed = ["First day at Loop", ...]
print(f" {profile['username']} has {profile['followers']} followers and {len(feed)} posts. Top post: {feed[0]}")
# @queen has 250 followers and 3 posts. Top post: First day at Loop
# I used dictionary for the profile and I used list for the feed