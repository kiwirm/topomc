import logging
import time 

class Logger:

    prev_time = time.perf_counter()
    time_next = False

    @classmethod
    def log(self, level, msg, sub=0, time_it=True):
        curr_time = time.perf_counter()
        
        if self.time_next:
            print(f" {(curr_time - self.prev_time):0.2f}s")
        else:
            self.time_next = True
            print()
        
        if not time_it: self.time_next = False
        print(f"({level.__name__.upper()})", ("    "*sub) + msg, end="")
        self.prev_time = curr_time
    
    def log_done(self, sub=0):
        self.log(logging.info, "Done", sub=sub, time_it=False)

    def __str__(self):
        return "Custom Logger class"