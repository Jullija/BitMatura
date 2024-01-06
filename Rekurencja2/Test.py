import time as tm

class Test():
    def __init__(self,func,args):
        self.func = func
        self.args = args
        


    def runtest(self):
        t = 0
        counter = 0
        leng = len(self.args)
        for i in range (leng):
            a = self.args[i][0]
            sol = self.args[i][1]
            s_time = tm.process_time()
            my_sol = self.func(a)
            e_time = tm.process_time()
            t += (e_time - s_time)
            if my_sol == sol:
                counter += 1
                print("Test {}: Passed".format(i+1))
            else:
                print("Test {}: Wrong result, Your result: {}, Corect result: {}".format(i+1, my_sol, sol))
        print("Final time: {:.3f} s, Result {}/{}".format(t,counter,leng))
    