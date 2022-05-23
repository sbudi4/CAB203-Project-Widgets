import graphs
import digraphs
import csv

# You can define some helper functions here if you like!

def optimiseWidgets(filename):

   # Reading the csv file:
   with open(filename, 'r') as csv_file:
      reader = csv.reader(csv_file)
      
      for row in reader:
        print(row)

   # SORT Machines, processes, and their capacities
   # determine entry - should be the one with ONE ENTRY
   # determine exits - neighbours and shit
   # determine exit - should be the one with ONE EXIT

   # Find maximum flow

   # Access functions from the imported files like this:
   n = graphs.N(V, E, u)
   t = digraphs.topOrdering(V, E)

   return machineSettings


## TEST HARNESS
# The following will be run if you execute the file like python3 widget_n1234567.py widgetsamplefile.csv
# Your solution should not depend on this code.
if __name__ == '__main__':
   import sys

   if len(sys.argv) < 2:
      print("Please provide a filename for the input CSV file.")
      sys.exit(1)

   filename = sys.argv[1]
   solution = optimiseWidgets(filename)
   print(solution)