from array import * 

value = array('i',(1,2,3,4))

new_value = array(value.typecode,(a for a in value))
for i in range(len(value)):
    print(new_value[i],end=" ")

print(value.typecode)
for i in range(len(value)):
    print(value[i],end=" ")
value.append(5) 
for i in range(len(value)):
    print(value[i],end=" ")
value.remove(5)
for i in range(len(value)):
    print(value[i],end=" ")
print(value.buffer_info())
print(value.index)
print(value.extend)