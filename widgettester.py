import importlib
import importlib.util
import sys
import traceback
import pprint

if len(sys.argv) != 2:
   print('''
Error: you must provide a filename for your pegs solution.

Make sure that this file is located in the same directory as your solution, along with 
widgets_sample_0.csv, widgets_sample_1.csv, widgets_sample_2.csv, widgets_sample_3.csv
widgets_sample_4.csv and graphs.py and digraphs.py if you use them.  Open a terminal, 
navigate to the directory containing this file, and run

python widgettester.py widgets.py

replace widgets.py with the name of your solution file if it is different.
''')
   sys.exit(1)

try:
   filename = sys.argv[1]
   spec = importlib.util.spec_from_file_location('widgetsolution', filename)
   if spec is None:
      print('''Error when loading the solution file.  There may be syntax errors, the file might not be valid Python code, or the file might not exist.''')
      sys.exit(1)
   widgetsolution = importlib.util.module_from_spec(spec)
   spec.loader.exec_module(widgetsolution)
except Exception:
   print("Problem parsing the solution:")
   traceback.print_exc()
   sys.exit(1)

filenames = [
   ('widgets_sample_0.csv', 8),
   ('widgets_sample_1.csv', 5),
   ('widgets_sample_2.csv', 7),
   ('widgets_sample_3.csv', 11),
   ('widgets_sample_4.csv', 2),
]

if 'optimiseWidgets' in dir(widgetsolution):
   for filename, maxvalue in filenames:
      print(f'Using csv file {filename}')   
      solution = widgetsolution.optimiseWidgets(filename)
      print('Solution found: ')
      pprint.pprint(solution)
      if type(solution) != dict:
         print('Your returned settings is not a dictionary.  It is probably incorrect.')
      print(f'This file has max final output of {maxvalue} kg/hr')
      print('You should that check your solution is valid manually.')
      print('--------------------------------------------------------')
   
   print('''If the your solution is correct for the first file, but not for subsequent
files then you may have variables that are only initialised once, and not for each time 
each your function is run.  This is likely to be a problem if you use global variables.
   ''')


else:
   print("Couldn't find optimiseWidgets function!  Are you sure you provided the correct filename?")