import sys

def show_environment():
    if is_virtual_environment():
        print('I am inside virtual environment')        
    else:
        print('I am outside virtual environment')

def is_virtual_environment():
    return (hasattr(sys, 'real_prefix')
        or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix))