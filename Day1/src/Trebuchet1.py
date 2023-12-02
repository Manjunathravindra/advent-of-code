total = 0
for lines in open("Day1\Trebuchet.txt"):
    numbers = []
    for letters in lines:
        if(letters.isdigit()):
           numbers.append(letters)
    total += int(numbers[0]+numbers[-1])


print(total)



