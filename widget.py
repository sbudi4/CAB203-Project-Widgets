from contextlib import nullcontext
from gettext import find
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
   # Creating variables to sort stuff:
   vertex = []
   vertices = []
   edge = []
   edges = []

   sources = []
   drains = []
   outputs = []
   inputs = []

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

   #### determinining source and drains #####
   for each in range(len(components)):
      outputs.append(components[each][3])
      inputs.append(components[each][2])

   outputMaterial = list(set(inputs)-set(outputs))
   inputMaterial = list(set(outputs)-set(inputs))

   for each in range(len(components)):
      if outputMaterial[0] == components[each][2]:
         sources.append(components[each][0])
      if inputMaterial[0] == components[each][3]:
         drains.append(components[each][0])

   # Finding drain vertex





   print(edges)
   print(sources)
   print(drains)

   # Find maximum flow using function in digraphs.py
   machineSettings = digraphs.maxFlow(V, E, w, s, drain)

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