from collections import deque

class stack(object):
    def __init__(self, array=None, stack=None):
        """stack is an existing collections.deque object"""
        if array:
            self.stack = deque(array)
        elif stack:
            self.stack = stack
    def push(self, val):
        try:
            self.stack.appendleft(val)
        except:
            print('failed to execute push')
    def pop(self):
        try:
            del self.stack[0]
        except:
            print("failed to execute pop")
    def info(self):
        print("length: "+ str(len(self.stack)))
        print("average value: " + str(sum(self.stack)/len(self.stack)))
        print("max value: " + str(max(self.stack)))
        print("min value: " + str(min(self.stack)))
    def __str__(self):
            for num in self.stack:
              print("*---*\n| "+str(num)+" |")
            print("*---*")
            return ''


