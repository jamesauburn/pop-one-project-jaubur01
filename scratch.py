#list of tuples
#file_name = 'Alabama\tMontgomery\t32.361538\t-86.279118\nAlaska\tJuneau\t58.301935\t-134.41974\nArizona\tPhoenix\t33.448457\t-112.073844'

#file_name = open('city-data.txt', 'r').read()
#print(file_name)
file_name = 'Alabama\tMontgomery\t32.361538\t-86.279118\nAlaska\tJuneau\t58.301935\t-134.41974\nArizona\tPhoenix\t33.448457\t-112.073844'
data_ = [i.split('\t') for i in file_name.split('\n')]

#b = set(int(i) for i in input().split())
for i in data_:
    [float(j) for j in data_[i][2:]]

print(data_)

print(type(data_[0][3]))
