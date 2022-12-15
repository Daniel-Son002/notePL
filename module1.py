# module1.py
import math
from midi_func import lst_to_mid
from midi_func import nums

def concat_str(*args, **kwargs):
    # C
    start_pitch = 60
    nums(args, 'concat_str', start_pitch)
    kwargs_list = ['%s=%s' % (k, kwargs[k]) for k in kwargs]
    print(''.join(args), ','.join(kwargs_list))

def print_str(*args, **kwargs):
    kwargs_list = ['%s=%s' % (k, kwargs[k]) for k in kwargs]
    # D
    start_pitch = 62
    nums(args, 'print_str', start_pitch)
    print(' '.join(args), ','.join(kwargs_list))

def add_num(*args, **kwargs):
    t = globals()['__builtins__'][kwargs['type']]
    # G
    start_pitch = 67
    nums(args, 'add_num', start_pitch)
    print(sum(map(t, args)))

def mul_num(*args, **kwargs):
    t = globals()['__builtins__'][kwargs['type']]
    # A
    start_pitch = 69
    nums(args, 'mul_num', start_pitch)
    print(math.prod(map(t, args)))

def div_num(*args, **kwargs):
    if len(args) != 2:
        print('Only two numbers')
        pass
    else:
        t = globals()['__builtins__'][kwargs['type']]
        # C
        start_pitch = 72
        nums(args, 'div_num', start_pitch)
        print(t(args[0]) / t(args[1]))

