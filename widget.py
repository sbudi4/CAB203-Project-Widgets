import graphs
import digraphs
import csv

# You can define some helper functions here if you like!

def optimiseWidgets(filename):

   # Reading the CSV file:
   components = []

   with open(filename, 'r') as csv_file:
      reader = csv.reader(csv_file)
      
      for row in reader:
        components.append(row)
   # Remove CSV Headers for processing:
   components.pop(0)

   #### Formatting the CSV to use numbers instead of names ####
   # Creating arrays to sort stuff:
   buffer1 = []
   buffer2 = []

   machine = []
   input = []
   output = []

   inputs = []
   machines = []
   outputs = []

   # Assigning each machine a vertex:
   for each in range(len(components)):
      machine = [components[each][0], each]
      machines.append(machine)

      # Sorting the rest of CSV data:
      # Assign each input a number of reference
      input = components[each][2] 
      if input not in buffer1:
            buffer1.append(input)
            inputs.append([input, each])

   for each in 




   print(machines)
   print(inputs)
   print(outputs)



   # determine entry - should be the one with ONE ENTRY
   # determine exits - neighbours and shit
   # determine exit - should be the one with ONE EXIT

   # Find maximum flow

   # Access functions from the imported files like this:

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