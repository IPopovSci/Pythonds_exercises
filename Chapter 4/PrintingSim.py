from Queue import Queue
import random

class Printer:
    def __init__(self,ppm):
        self.page_rate = ppm #printing rate per minute
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task!=None:
            self.time_remaining-=1
            if self.time_remaining<=0:
                self.current_task=None
    def busy(self):
        if self.current_task != None:
            return True
        else:
            return False

    def start_next(self,task):
        self.current_task=task
        self.time_remaining=task.get_pages() * (60/self.page_rate)

class Task:
    def __init__(self,time):
        self.timestamp = time
        self.pages = random.randrange(1,21)

    def get_stamp(self):
        return self.timestamp

    def get_pages(self):
        return self.pages

    def wait_time(self,current_time):
        return current_time - self.timestamp
    @classmethod
    def new_print_task(cls,start_second,sec_per_task):
        avg_secs_to_task=int(3600/sec_per_task)
        num = random.randrange(1, avg_secs_to_task+1)
        #print(num,avg_secs_to_task)
        if num == avg_secs_to_task:
            return cls(start_second)
        else:
            return False
class PrintingSimulation:
    def __init__(self,ppm,num_students,avg_tasks_per_hour,seconds):
        self.ppm = ppm
        self.printer = Printer(ppm)
        self.job_queue = Queue()
        self.waiting_times = [0]
        self.num_students=num_students
        self.avg_tasks_per_hour=avg_tasks_per_hour
        self.seconds_run_time=seconds
        self.sec_per_task=self.num_students*self.avg_tasks_per_hour

    def run(self):
        for second in range(self.seconds_run_time):
            task = Task.new_print_task(second,self.sec_per_task)
            #print(task)
            if isinstance(task, Task):
                self.job_queue.enqueue(task)
            if (not self.printer.busy()) and (not self.job_queue.isEmpty()):
                next_task = self.job_queue.dequeue()
                self.waiting_times.append(next_task.wait_time(second))
                self.printer.start_next(next_task)

            self.printer.tick()

        wait_time = sum(self.waiting_times) / len(self.waiting_times)

        print("Average Wait %6.2f secs %3d tasks remaining." % (wait_time, self.job_queue.size()))
    #Need to research why the behavior is so different between having init_simulation, just running .run and re-insta the class inside
    # @classmethod
    # def init_simulation(cls,ppm,num_students,avg_tasks_per_hour,seconds):
    #     return cls(ppm,num_students,avg_tasks_per_hour,seconds)
    #
    # def run_simulations(self,num_simulations):
    #     for i in range(num_simulations):
    #         simulation=self.init_simulation(self.ppm,self.num_students,self.avg_tasks_per_hour,self.seconds_run_time)
    #         simulation.run()
class SimRunner:
    def __init__(self,Simulation,num_simulations):
        self.num_simulations=num_simulations
        self.simulation=Simulation
    def run_simulations(self,**kwargs):
        for i in range(self.num_simulations):
            sim_instance=self.simulation(**kwargs)
            sim_instance.run()

sim_runner=SimRunner(PrintingSimulation,10)
sim_runner.run_simulations(ppm=5,num_students=10,avg_tasks_per_hour=2,seconds=3600)
