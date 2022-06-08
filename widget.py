### Importing dependencies ###
from platform import machine
import digraphs
import csv

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
   vertex = []
   vertices = []
   edge = []
   edges = []
   sources = []
   drains = []
   outputs = []
   inputs = []
   machines = []

   # Assigning each machine a vertex:
   for each in range(len(components)):
      machines.append(components[each][0])
      vertex = [components[each][0], components[each][2]]
      vertices.append(vertex)

   # Creating graph edges and assigning their weights
   for each in range(len(vertices)):
      for product in range(len(components)):
         if vertices[each][1] == components[product][3]:
            edge = [components[product][0], vertices[each][0], components[product][4]]
            edges.append(edge)

   #### determinining sources and drains #####
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

   #### Creating variables for use in the maxFlow function: #####
   V = set(machines)
   source = sources[0]
   drain = drains[0]
   w = {}
   for each in range(len(edges)):
      w[edges[each][0], edges[each][1]] = int(edges[each][2])
   E = set(w.keys()) #MODIFIED FROM CAB203 digraphs.py

   # Find maximum flow using function FROM CAB203 digraphs.py
   maxFlowData = digraphs.maxFlow(V, E, w, source, drain)

   # Converting result back into machine configurations
   machineConfigsArray = []
   machineConfigs = {}

   for each in maxFlowData:
      if maxFlowData[each]:
         preVertex, postVertex = each
         machineConfigsArray.append([preVertex, maxFlowData[each]])
   
   for each in range(len(machineConfigsArray)):
      machineConfigs[machineConfigsArray[each][0]] = int(machineConfigsArray[each][1])

   return machineConfigs

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