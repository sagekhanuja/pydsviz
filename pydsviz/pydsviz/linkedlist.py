#plain listnode object, representing nodes in linked list
class listnode(object):
    def __init__(self, val):
        self.val = val
        self.next = None 

class linkedlist(object):
    def __init__(self, head):
        self.head = head ##head type is listnode 
    def info(self):
        count = 0
        temphead = self.head
        vals = []
        while temphead:
            vals.append(temphead.val)
            temphead = temphead.next
            count+=1
        print("count: "+str(count))
        print("average value: " + str(sum(vals)/count))
        print("min value: "+ str(min(vals)))
        print("max value: " + str(max(vals)))

    ## pretty prints out the linked list
    def __str__(self):
        print("head", end = " ")
        temphead = self.head
        while temphead.next:
            print(str(temphead.val)+'->', end = " ")
            temphead = temphead.next
        print(str(temphead.val) + " tail", end = " ")
        return ''

        

