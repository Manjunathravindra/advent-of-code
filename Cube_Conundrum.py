import re
count = []
total = 0
for line in open("Day2\Cube_Conundrum.txt"):
  count.append(int((re.findall("[0-9]*:",line).pop()).replace(":","")))
  set = 0
  red = ""
  blue = ""
  green = ""
  red = red.join(re.findall("[0-9]*\sred",line)).replace(" red"," ").split()
  blue = blue.join(re.findall("[0-9]*\sblue",line)).replace(" blue"," ").split()
  green = green.join(re.findall("[0-9]*\sgreen",line)).replace(" green"," ").split()
  for rnum in red:
      if int(rnum) > 12: 
        count.pop()
        set = 1
        break
  if(set != 1):
       for gnum in green:
         if int(gnum) > 13: 
            set = 1
            count.pop()
            break
  if(set!=1):
       for bnum in blue:
           if int(bnum) > 14: 
            count.pop()
            break
for num in count:
    total = total +int(num)
print(total)