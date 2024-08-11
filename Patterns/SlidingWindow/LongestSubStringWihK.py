def longest_substring_with_k_distinct(str1, k):
  # TODO: Write your code here
  """
  Given a string, find the length of the longest substring in it with no more than K distinct characters.
    Input: String="araaci", K=2
    Output: 4
    Explanation: The longest substring with no more than '2' distinct characters is "araa".

    Input: String="cbbebi", K=3
    Output: 5
    Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
  """
  str_o = []
  start_window = 0
  end_window = 0
  n_size = 0
  n_size_list =[0]
  if len(str1) < k:
      return len(str1)
  else:
    while end_window < len(str1):
        if str1[end_window] in str_o:
            n_size = n_size + 1
            end_window = end_window + 1
        elif len(str_o) < k:
            str_o.append(str1[end_window])
            n_size = n_size + 1
            end_window = end_window + 1
        else:
            end_pos = end_window
            dist_list = []
            while end_pos >= start_window:
                if len(dist_list) == k and (str1[end_pos] not in dist_list):
                    n_size_list.append(n_size)
                    n_size = end_window - end_pos
                    start_window = end_pos + 1
                    end_window = end_window + 1
                    str_o = dist_list
                elif(str1[end_pos] not in dist_list):
                    dist_list.append(str1[end_pos])
                    end_pos = end_pos - 1
                elif str1[end_pos] in dist_list:
                    end_pos = end_pos - 1
    n_size_list.append(n_size)    
    print(max(n_size_list))
    return max(n_size_list)

# print(longest_substring_with_k_distinct("cbcbcedbbddbbccb", 3))
print(longest_substring_with_k_distinct("araaci", 2))
            
              
