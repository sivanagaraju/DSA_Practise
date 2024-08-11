def find_averages_subarrays(k, arr):
    result = []
    for i in range(len(arr)-k+1):
        _sum = 0.0
        for j in range(i, i+k):
            _sum += arr[j]
        result.append(_sum/k)
    return result

def find_averages_of_subarrays(k, arr):
    result = []
    windowSum, windowStart = 0.0, 0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        if windowEnd >= k -1:
            result.append(windowSum/k)
            windowSum -= arr[windowStart]
            windowStart += 1
    return result
        

def main():
  result = find_averages_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
  result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
  print("Averages of subarrays of size K: " + str(result))


main()