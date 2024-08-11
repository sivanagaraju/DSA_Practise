

def merge_intervals(intervals):
    if not intervals:
        return None
    
    result = []
    result.append([intervals[0][0], intervals[0][1]])
    
    for i in range(1, len(intervals)):
        last_added_interval = result[len(result) - 1]
        cur_start = intervals[i][0]
        cur_end = intervals[i][1]
        prev_end = last_added_interval[1]
        
        if cur_start <= prev_end:
            result[-1][1] = max(cur_end, prev_end)
        else:
            result.append([cur_start, cur_end])
    return result

print(merge_intervals([[1, 5], [4, 6], [6, 8], [11, 15]]))
