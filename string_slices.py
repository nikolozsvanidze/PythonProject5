#we can slice a string

s = "0123456789"
print(s)
print(s[1:2])#first index is included, last index is excluded
print(s[4:7])
print(s[:7]) #if you omit the first index, it starts from beginning

s = "I go to school early in the morning"
print(s[:20])
print(s[20:]) #includes alltheway to the end

print(s[:]) # the whole thing
print(s[::2]) # this means step of 2 (every second character)
print(s[::-1])
print("racecar"[::-1])