temp =dict()
def type_of_data_given(*data):
    global temp 
    for i in data:
        if type(i) in temp:
            # temp[type(i)].append(i)
            temp[type(i)]  = [i]
         
        else:
            temp[type(i)]  = [i]

type_of_data_given(1,2,3,[4,5,6],'a',[9,8,7],9.9,9.0,8)
print(temp)
print("Diffrernece between appending and inserting by = in python dictionary ")

temp2 =dict()
def type_of_data_given2(*data):
    global temp2 
    for i in data:
        if type(i) in temp2:
            temp2[type(i)].append(i)
           
         
        else:
            temp2[type(i)]  = [i]

type_of_data_given2(1,2,3,[4,5,6],'a',[9,8,7],9.9,9.0,8)
print(temp2)