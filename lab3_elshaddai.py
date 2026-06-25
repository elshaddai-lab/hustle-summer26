
# Elshaddai l Lab 3 l Hustle

# Ticket 1
username = "queen"
# 4 characters are in the handle
print (len(username))
# yes, len() counted every character and symbols included


#Ticket 2
print (username[0])
print(username[len(username) - 1])
# "q" and "n" will print
# because the number minus 1 is the index number


#Ticket 3
print("Welcome to Loop, @" + username + "!")
print(f"Welcome to Loop, @{username}!")
# yes, both lines will look identical on screen
# the concatention was easier because it requires less code


#Ticket 4
#username[0] = "X" 
# Error message: TypeError: 'str' object does not support item assignment
print(username.upper())
# it will crash and give an error message
# for a string, immutable means that once a string is made, you cannot change a letter inside it


#Ticket 5
feed = ["First Post!", "At the gym", "I love my dog!"]
print(len(feed))
print(feed[0])
# The count will be 3, and the "First Post!" caption will print first
# I used index 0


#Ticket 6
feed.append("Loving this weather")
# The index will be 3
# Since python starts counting at 0, the fourth post has the index of 3


#Ticket 7
feed.pop(0)
feed.sort()
print(feed)
# The post that was at index 0 will be removed, and the rest will be in alphabetical order
# .pop(0) removed what was in idex 0 and .sort(0) rearranged the list to alphabetical order


#Ticket 8
profile = {"username": "queen", 
"followers": 200,
"verified": False}
print(profile["followers"])
#print (profile[0])
# Error message: KeyError: 0 (Dictionaries do not use numerical indexes)
#the follower number will print 250, and an error message will print for profile[0]
# it looks things up by key name because they are unordered, so the values cannot be called by an index number 


#Ticket 9
profile["followers"] = profile["followers"] +50
profile["bio"] = "Live Laugh Love Life!"
print(profile)
print(profile.get("age"))
# When the key is missing, age will print "None"
#  .get() is safer than profile["age"] because it won't make the code crash or give an error message


#Ticket 10
profile = {"username":"@queen", 
"followers": 250}
feed = ["First day at Loop", ...]
print(f" {profile['username']} has {profile['followers']} followers and {len(feed)} posts. Top post: {feed[0]}")
# it will print @queen has 250 followers and 3 posts. Top post: First day at Loop
# I used a dictionary for the profile, and I used a list for the feed
