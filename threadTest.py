from threading import Thread

class Worker(Thread):

    def __init__(self,id):
        Thread.__init__(self)
        self.id = id


    def run(self, results, index):
        results[index] = self.id





threads = [None] * 10
results = [None] * 10

for i in range(len(threads)):
    threads[i] = Worker(i)
    threads[i].start()
    # threads[i].run(results, i)


for i in range(len(threads)):
    threads[i].join()
    # print(results[i])
