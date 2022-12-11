# python 3
# author: Silviu Draghici

'''

'''

# in case I want to specify file with command line
#import sys
#fileName = sys.argv[1]

if __name__ == "__main__":
  print("")
  
  fileName = 'input_test.txt'
  inputFile = open(fileName, 'r')
  
  line = inputFile.readline()
  while line:
    line = line.strip()
    
    print(line)
    
    line = inputFile.readline()
  inputFile.close()

  print("")