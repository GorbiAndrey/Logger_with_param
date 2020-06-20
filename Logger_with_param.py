from datetime import datetime
from inspect import signature
import os

def param_logger(path):
    logs_file_name = os.path.join(path, 'out.txt')

    def logger(function):
        def log_function(*args, **kwargs):
            now = datetime.now()
            function_name = function.__name__

            sig = signature(function)
            param = sig.bind(*args, **kwargs)
            args = param.args
            kwargs = param.kwargs

            function_return = function(*args, **kwargs)

            f = open(logs_file_name, 'w')
            f.write(str(now) + '\t' + str(function_name) + '\t' + 
                    str(args) + str(kwargs) + '\t' + 
                    str(function_return) + '\t' + '\n')
            f.close()
            return
        return log_function

    return logger


@param_logger('')
def some_function(*args, **kwargs):
    return 'func_result'

some_function('hello', name='world')