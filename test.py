word = "harish"
cha = {}
count = 0
for character in word:
    if character not in cha:
        cha[character] = 1
    else:
        cha[character]+=1
        print "Not Unique"
print cha
