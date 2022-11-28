# module1.py
import math
from midiutil.MidiFile import MIDIFile

def add_str(*args, **kwargs):
    kwargs_list = ['%s=%s' % (k, kwargs[k]) for k in kwargs]
    print(''.join(args), ','.join(kwargs_list))

def print_str(*args, **kwargs):
    kwargs_list = ['%s=%s' % (k, kwargs[k]) for k in kwargs]
    print(' '.join(args), ','.join(kwargs_list))

def add_num(*args, **kwargs):
    t = globals()['__builtins__'][kwargs['type']]
    print(sum(map(t, args)))

def mul_num(*args, **kwargs):
    t = globals()['__builtins__'][kwargs['type']]
    print(math.prod(map(t, args)))

def div_num(*args, **kwargs):
    if len(args) != 2:
        print('Only two numbers')
        pass
    else:
        t = globals()['__builtins__'][kwargs['type']]
        print(t(args[0]) / t(args[1]))

