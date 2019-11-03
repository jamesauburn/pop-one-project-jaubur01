
file_name = open('city-data.txt', 'r').read()

#file_name = 'Alabama\tMontgomery\t32.361538\t-86.279118\nAlaska\tJuneau\t58.301935\t-134.41974\nArizona\tPhoenix\t33.448457\t-112.073844'
data_ = [i.split('\t') for i in file_name.split('\n')] # Convert to List of List
for i in data_:
    i[2:4] = [float(j) for j in i[2:4]] #Convert co-ordinated to float
data_ = [tuple(i) for i in data_] #Convert to List of tuples


print(data_)


#data_ = [tuple(map(str, i.split('\t'))) for i in file_name.split('\n')]
#x = map(lambda x: str(x), x)
#a = tuple(i for i in list)
#test = list(map(list, l))


#semi_ = data_[0]
#print(semi_)
#b = set(int(i) for i in input().split())
#for i in data_:
#semi = [float(j) for j in semi_[2:]]
#print(semi_)
#print(data_)

#print(type(semi_[2]))
