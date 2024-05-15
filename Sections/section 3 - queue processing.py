import multiprocessing 

def square ( mylist ,q ):
    for num in mylist:
        q.put (num*num) ## put element in queue

def print_queue (q):
    while not q.empty ():
        print (q.get()) ## get elemnt from queue 
    print ("queue not empty")

if __name__ == "__main__":
    mylist = [1,3,4,5]
    q = multiprocessing.Queue() ## this create queue

    p1=multiprocessing.Process(target=square , args=(mylist,q))
    p2=multiprocessing.Process(target=print_queue , args=(q,))

    p1.start()
    p1.join()

    p2.start()
    p2.join()