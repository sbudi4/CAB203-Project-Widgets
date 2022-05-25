from contextlib import nullcontext
import graphs
import digraphs
import csv

# You can define some helper functions here if you like!

def optimiseWidgets(filename):

   #### Reading the CSV file: ####
   components = []

   with open(filename, 'r') as csv_file:
      reader = csv.reader(csv_file)
      
      for row in reader:
        components.append(row)
   # Remove CSV Headers for processing:
   components.pop(0)

   #### Formatting the CSV to use numbers instead of names ####
   # Creating arrays to sort stuff:
   vertex = []
   vertices = []
   edge = []
   edges = []

   sources = []
   source = 'null'

   # Assigning each machine a vertex:
   for each in range(len(components)):
      vertex = [components[each][0], components[each][2]]
      vertices.append(vertex)

   
   # Creating graph edges and assigning their weights
   for each in range(len(vertices)):
      for product in range(len(components)):
         if vertices[each][1] == components[product][3]:
            edge = [components[product][0], vertices[each][0], components[product][4]]
            edges.append(edge)

   # determine source - should be UNIQUE INPUT
   for input in components:
      if input not in sources:
         sources.append(input)


   # determine drain - should be UNIQUE OUTPUT


   print(edges)
   print(sources)

   # Find maximum flow using function in digraphs.py
   machineSettings = digraphs.maxFlow(V, E, w, s, d)

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