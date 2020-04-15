import re
import operator
import sys

inFile = sys.argv[1]
file_object = open(inFile, 'r+') 

li = list( file_object.read().split(' ') )

new = []
for word in li:
    new.append( re.split(';|,|\n|\r|=|\"|\'.|\? ' , word ) )

    

new2 = []
start = 0
end = 0
    
for ii in new:
    for word in ii:
        z = len(word)
        for i in range(1,z):
            if word[-i].isalpha():
                end = z - i + 1
                break
        for j in range(z):
            if word[j].isalpha():
                start = j
                break
        new2.append(word[start:end].lower())

word_dict = {}

for word in new2:
    if word not in word_dict.keys():
        word_dict[word] = new2.count(word)
    


print(len(word_dict))
print('\n')

file_object.close()


with open('Alphabetical.txt' , 'w') as alpha:
    for i in sorted(word_dict):
        alpha.write( i + " : " + str(word_dict[i]) + "\n" )


with open('most_popular.txt' , 'r+') as mp_file:
    sorted_list = sorted(word_dict.items() , key = operator.itemgetter(1))

    sorted_list.reverse()

    for item in sorted_list:
        mp_file.write(item[0] + " : " + str(item[1]) + '\n' )





