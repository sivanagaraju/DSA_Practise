def insert_interval(existing_intervals, new_interval):
    if existing_intervals:
        return new_interval
    
    new_start = new_interval[0]
    new_end = new_interval[1]
    
    n = len(existing_intervals)
    i =0 
    output = []
    
    while i < n and existing_intervals[i][0] < new_start:
        output.append(existing_intervals[i])
        i = i + 1
        
    if not output or output[-1][1] < new_start:
        output.append(new_interval)
    else:
        output[-1][1] = max(output[-1][1], new_end)
        
    while i < n:
        ei = existing_intervals[i]
        start, end = ei[0], ei[1]
        if output[-1][1] < start:
            output.append(ei)
        else:
            output[-1][1] = max(output[-1][1], end)
        i += 1
    return output

def main():
    new_interval = [[5, 7], [8, 9], [10, 12], [1, 3], [1, 10]]
    existing_intervals = [
        [[1, 2], [3, 5], [6, 8]],
        [[1, 3], [5, 7], [10, 12]],
        [[8, 10], [12, 15]],
        [[5, 7], [8, 9]],
        [[3, 5]]
    ]
    
    for i in range(len(new_interval)):
        print(i + 1, ".\tExiting intervals: ", existing_intervals[i], sep="")
        print("\tNew interval: ", new_interval[i], sep="")
        output = insert_interval(existing_intervals[i], new_interval[i])
        print("\tUpdated intervals: ", output, sep = "")
        print("-"*100)


if __name__ == "__main__":
    main()
        