def reverse(num):
  num_float=num
  while num_float %1 != 0 :
    num_float*=10
  num_str=str(num_float)
  if (len(num_str))>=7 :
    num=str(num)
    return num[::-1]
  else:
    return ("your number is shorter than 5 digit")



number=float(input('pls enter at least 5 digit float number'))
print (f"{number} ===> {reverse(number)}")