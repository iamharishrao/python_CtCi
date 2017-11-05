phrase = "Hello World Welcome Here.This is Great!"
new_length = 0
old_list = []
new_list = []
for character in phrase:
    old_list.append(character)
i = 0
for element in old_list:
    if element == ' ':
        new_list.append('%')
        new_list.append('2')
        new_list.append('0')
        i+=1
    else:
        new_list.append(element)
        i+=1
print "".join(new_list)
