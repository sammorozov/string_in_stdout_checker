import sys
from io import StringIO
import matplotlib.pyplot as plt

# Redirect 
old_stdout = sys.stdout
sys.stdout = StringIO()

help(plt.text)

help_info = sys.stdout.getvalue()

# Restore 
sys.stdout = old_stdout

# 'help_info' contains the help information

# parser
def string_in_stdout_checker():
    temp_str = ''
    for i in help_info:
        if i != '\n':
            temp_str += i
        else:
            if 'ha' in temp_str:
                print(temp_str)
            temp_str = ''

        
string_in_stdout_checker()

    

    
