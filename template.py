# python 3
# author: Silviu Draghici

'''

'''

if __name__ == "__main__":
  print(f"")
  
  fileName = 'input_test.txt'
  inputFile = open(fileName, 'r')
  
  line = inputFile.readline()
  while line:
    line = line.strip()
    
    print(line)
    
    line = inputFile.readline()
  inputFile.close()

  print(f"")
