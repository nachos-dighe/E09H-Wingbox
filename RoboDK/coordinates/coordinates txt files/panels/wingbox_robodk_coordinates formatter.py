z = str(input('enter file name exactly, with .txt at the end'))
f = open(z, 'r')

txt = f.readlines()
f.close()
print(txt[0],txt[1],txt[2], sep ='\n') #testing
del txt[1]
del txt[0]
line_last = txt.index('\t\t\t\t\t\t\t\t\t\n')
length_txt = len(txt)
#print(len(txt), line_last)#testing
for count_delete in range(length_txt-1,line_last-1,-1): 
    #print(count_delete) #testing
    del txt[count_delete]
#print(txt) #testing


#VERY VERY IMPORTANT: WHEN DELEING ITEMS FROM LIST USING INDEX, USE A REVERSED INDEX (IE: ITEM 2 SHOULD BE DELETED AFTER ITEM 4). IT IS IMPORTANT TO DO THIS TO AVOID LISTS BEING MOVED UP/DOWN UNEXPECTEDLY

f = open(z, 'w')
f = f.writelines(txt)
f.close()