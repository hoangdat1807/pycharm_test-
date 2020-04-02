class exercise :
    def __int__(selfself ,list_1,list_2):
        self.list_1= list1
        self.list_2=list2

    def sum_2_list(self):
        sum = 0
        new_list =[]
        for i in range (0,len (self.list_1)):
            new_list.append(self.list_1[i] + self.list_2[i])
            print ("new list is =" + str(new_list))
        for i in range (0,len (new_list)):
            sum= sum + new_list[i]
list1= [1,3,5,7,9]
list2= [0,5,7,8,10]
print ( "tong của list ",sum )
test=exercise(list1,list2)
test.sum_2_list()




        