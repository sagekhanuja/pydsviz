from sys import getsizeof
import numpy as np

class array(object):
    def __init__(self, arr = None):

        if arr:
            self.arr = arr
        else:
            self.arr = []


    def help(self):

        print('this is an array object')
   
    def append(self, val):

        self.arr.append(val)

    def info(self):  ## core functionality of giving info regarding an existing array
        
        shape = np.asarray(self.arr).shape

        if len(shape)==1:
            info_help_func(self.arr)
            print("max value "+ str(max(self.arr)))
            print("min value " + str(min(self.arr)))
            print("average value "+ str(sum(self.arr)/len(self.arr)))
        else:
            info_help_func(self.arr)

    def __str__(self):
        test = [i for i in range(len(self.arr))]
        print("indexes  = "+str(test)+'\n\n'+ "array  = "+str(self.arr))  
        return ''   

##helper function for info 
def info_help_func(arr):
    print(str(np.asarray(arr).shape)+" dimensional array")
    print("length " + str(len(arr)))  
    print(str(getsizeof(arr))+" bytes")