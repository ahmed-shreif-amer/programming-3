import os 
os.system("cls")

## factory quiz

class o1 : ### first class 
    def __init__ (self):
        print ("this is option1")

class o2 : ### second class
    def __init__ (self):
        print("this is option2")

class factory : ### main factory
    def choose (option):
        if (option == "a"):
            return o1() ### return first 
        elif (option=="b"):
            return o2() ### return second 

object = factory.choose("a")

# ### queue quiz 
# import multiprocessing

# def put(list , q):
#     for n in list :
#         q.put(n) ## put element in queue

# def print_queue(q):
#     while not q.empty ():
#         print (q.get()) ## get elemnt from queue while it is not empty 
#     print ("queue is now empty")

# if __name__ == "__main__":
#     list = [1,2,3,4,5,6] ### the list will put in queue 
#     q = multiprocessing.Queue() ## queue 

#     p1 = multiprocessing.Process (target=put , args=((list , q))) ### process 1
#     p2 = multiprocessing.Process (target=print_queue , args=(q,)) ### process 2

#     p1.start() ## start put elemnt in queue 
#     p1.join() ### excute other after the join 

#     p2.start() ## start get element from queue
#     p2.join() ### excute all after the queue