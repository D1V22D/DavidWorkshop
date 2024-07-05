import time
import logging
from functools import wraps
class Usage_of_decorators:
    def __init__(self) :
        self.side = 0
        
    def Timely(Original_method):
        @wraps(Original_method) # this will handle the multi decorator passing
        def wrapper(*args, **kwargs):
            start , end = 0.0,0.0
            start = time.time()
            result = Original_method(*args, **kwargs)
            time.sleep(0.5)
            end = time.time()
            print(f"start time :{start}\n end time :{end}")
            print(f"the {Original_method.__name__} executed in {(end - start)} second ")
            return result
        return wrapper
    
    def my_logger(orig_func):
        logging.basicConfig(filename="{}.log".format(orig_func.__name__),level=logging.INFO)
        @wraps(orig_func)
        def wrapper(*args, **kwargs):
            logging.info('Ran with args :{} and kwargs :{}'.format(args,kwargs))
            print('Ran with args :{} and kwargs :{}'.format(args,kwargs))
            return orig_func(*args, **kwargs)
        return wrapper
        
    @my_logger    
    @Timely
    def Sqare_of_sides(self):
        a = int(input("ENTER THE SIDE ="))
        self.side = a
        return f"Square ={self.side*self.side}" 
        # the return is overrided by the return in the wraper class only show if print the funcion call 
    
    @my_logger
    @Timely
    def Volume_of_sides(self):
        return f"Square ={self.side*self.side*self.side}"
    
ud = Usage_of_decorators()
print(ud.Sqare_of_sides())
print(ud.Volume_of_sides())