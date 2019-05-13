from time import process_time as pt

def runtime(function):
    time = pt()
    function()
    print(f'Runtime: {pt() - time} seconds')
