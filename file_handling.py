import csv
#import matplotlib.pyplot as plt
#def scatter_plot(x, y):
#  plt.scatter(x, y)
#  plt.xlabel('Number')
#  plt.ylabel('Square')
#  plt.show()


def read_csv(filename):
  numbers=[]
  with open(filename) as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
      numbers.append(int(row[0]))
    print(numbers)
    
     
  


if __name__ == '__main__':
  read_csv('csv_file.csv')
  #print(numbers, squared)
#  scatter_plot(numbers, squared)