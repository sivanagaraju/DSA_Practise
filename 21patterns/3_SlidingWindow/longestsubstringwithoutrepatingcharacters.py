def longest_substring_without_repeating_characters(str):
    left = 0
    max_length = 0
    char_index_amp = {}
    for right in range(len(str)):
        # shrink the window if repeating character found
        if str[right] in char_index_amp and char_index_amp[str[right]] > left:
            left = char_index_amp[str[right]] + 1
            
        # udpdate character index map
        char_index_amp[str[right]] = right 
        
        # update max length
        max_length = max(max_length, right-left+1)
    return max_length