with open('Day1\Trebuchet1.txt') as f:
    lines = f.readlines()
    
  

def decode():
    i = 0
    while(i < 1000):
        lines[i] = lines[i].replace("six","s6x")
        lines[i] = lines[i].replace("seven","s7n")
        lines[i] = lines[i].replace("zero","z0o")
        lines[i] = lines[i].replace("one","o1e")
        lines[i] = lines[i].replace("two","t2o")
        lines[i] = lines[i].replace("three","t3e")
        lines[i] = lines[i].replace("four","f4r")
        lines[i] = lines[i].replace("five","f5fe")
        lines[i] = lines[i].replace("eight","e8t")
        lines[i] = lines[i].replace("nine","n9e")
        i = i+1
    
if __name__  ==  '__main__':
    decode()

    global numbers
    numbers = []
    sum = 0

    for words in lines:
        
        raw_numbers = []
        
        for letters in words:
            if(ord(letters) >= 48 and ord(letters) <= 57):
                raw_numbers.append(letters)
        
        x = int(raw_numbers[0] + raw_numbers[-1])
        numbers.append(x)
    

  
    for number in numbers:
        sum = sum + number
    print(sum)

   

        
