def smallest_subarray_with_given_sum(s, arr):
  # TODO: Write your code here
  n_size = len(arr)
  start_window = 0
  end_window= 0

  """
  for end_window in range(0, len(arr)):
    if sum(arr[start_window:end_window+1]) >= s:
      n_size = end_window - start_window + 1 if n_size <= (end_window - start_window + 1) else n_size
      while start_window < end_window:
        start_window = start_window + 1
  """   
  while end_window <= len(arr):
    if sum(arr[start_window:end_window]) >= s:
      n_size = (end_window - start_window)  if (end_window - start_window ) <=  n_size  else n_size
      start_window = start_window + 1
    else:
      end_window = end_window + 1

  print(n_size)
  return n_size

def main():
    print(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8]))
    
main()