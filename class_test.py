class Exercise :
    def __init__(self,list1,list2 ):
        self.list_1= list1
        self.list_2= list2
    def sum_2_list(self):
        sum=0
        new_list= [] # cai nay dung để làm gì vậy anh ?
        for i in range (0, len(self.list_1 )):
            new_list.append(self.list_1[i]+self.list_2[i])
            print ("new list is :"+str(new_list))
        for i in range (0, len (new_list)):
            sum =sum+ new_list[i]
        print ("sum of new_list", sum )

list1=[1,3,5,6,8,9]
list2=[2,4,6,9,10,12]
test =Exercise(list1,list2)
test.sum_2_list()
print(test.sum())


