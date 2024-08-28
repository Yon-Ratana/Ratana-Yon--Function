# EX3.Create function to find Max number in array [2,3,5,0,11,5,2]
def sum(number):
    min = number[0]
    for i in range(len(number)):
        if number[i]>min:
            min = number[i]
    return min
number=[2,3,5,0,11,5,2]
print(sum(number))