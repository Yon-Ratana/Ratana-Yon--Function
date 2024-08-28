# EX2.Create function to sum odd number in array [1,2,3,4,5,6]

def total(number):
    sum = 0
    for i in number:
        if i % 2 == 1:
            sum += i
    return sum
numbers = [1, 2, 3, 4, 5, 6]
print(total(numbers))