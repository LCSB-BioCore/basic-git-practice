
import os 

file = os.listdir('/Users/roxaneduparc/Documents/basic-git-practice/_attendees')

path = os.getcwd()
path = path[:-7]

index_list = open('index_list.md', 'a')
index_list.truncate(0)

index_list = open('index_list.md', 'a')

for i in range (len(file)) :
    index_list.write(file[i])
    index_list.write(" and the relative link to the file : " + path+"_attendees/"+file[i])
    index_list.write("\n")
    
