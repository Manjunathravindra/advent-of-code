import re
count = []
total = 0
for line in open("Day2\Cube_Conundrum.txt"):
  count.append(int((re.findall("[0-9]*:",line).pop()).replace(":","")))
  red = ""
  blue = ""
  green = ""
  red = red.join(re.findall("[0-9]*\sred",line)).replace(" red"," ").split()
  blue = blue.join(re.findall("[0-9]*\sblue",line)).replace(" blue"," ").split()
  green = green.join(re.findall("[0-9]*\sgreen",line)).replace(" green"," ").split()
  red_arr = []
  for rnum in red:
      red_arr.append(int(rnum))
  rmin = max(red_arr)

  green_arr = []
  for gnum in green:
      green_arr.append(int(gnum))
  gmin = max(green_arr)      

  blue_arr = []
  for bnum in blue:
     blue_arr.append(int(bnum))
  bmin = max(blue_arr)         
  
  mul = bmin * rmin * gmin
  total = total + mul
  
print(total)
