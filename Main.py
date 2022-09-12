from typing import List

def selectionSort(array, size) -> List[int]:
  # Write your code here
      for i in range(0,size-1):
        min=i
        for j in range(i+1,size):
            if array[j]<aarray[min]:
                min=j
        if min !=i:
            t=array[i]
            array[i]=array[min]
            array[min]=t

# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(selectionSort(data, len(data)))
