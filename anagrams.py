word1 = "SCADA"
word2 = raw_input("Enter word to check""\n")
if (len(word1) != len(word2)):
    print "Unequal length. No chance!"
cha = {}
cha2={}
for character in word1:
    if character not in cha:
        cha[character] = 1
    else:
        cha[character] +=1
print cha
for char in word2:
    if char not in cha2:
        cha2[char] = 1
    else:
        cha2[char] +=1
print cha2

if(cha == cha2):
    print "True"
else:
    print "False"
