class queue(object):
    def __init__(self, array=None, queue=None):
        """queue is an existing collections.deque object"""
        if array:
            self.queue = array
        elif queue:
            self.queue = queue
    def enqueue(self, val):
        try:
            self.queue.append(val)
        except:
            print('failed to execute push')
    def dequeue(self):
        try:
            del self.queue[-1]
        except:
            print("failed to execute pop")

    def info(self):
        print("length: "+ str(len(self.queue)))
        print("average value: " + str(sum(self.queue)/len(self.queue)))
        print("max value: " + str(max(self.queue)))
        print("min value: " + str(min(self.queue)))

    def __str__(self):
            for num in self.queue:
              print("*---*\n| "+str(num)+" |")
            print("*---*")
            return ''


