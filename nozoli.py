def nozoli(my_list):
  return my_list.sort(reverse=True)


my_list=[]
entery=True
while entery==True :
  user=input('''pls enter anything you want 
             for close the enter X ''')
  if user=='x':
    break
  else:
    my_list.append(user)
print (my_list , nozoli(my_list))