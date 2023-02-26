#binary search
#least to greatest

def binary_search(l,target,low=None,high=None):
  if high == None:
    high = len(l) - 1

  if low == None:
    low = 0

  if high < low:
    return -1


  midpoint = (low + high) // 2

  if l[midpoint] == target:
    return midpoint

  elif target < l[midpoint]:
    return binary_search(l,target,low,midpoint-1)

  else:
    return binary_search(l,target,midpoint+1,high)

if __name__ == '__main__':
  l = [1,4,8,9,10]
  target = 10

  print(binary_search(l,target))
  
  



    