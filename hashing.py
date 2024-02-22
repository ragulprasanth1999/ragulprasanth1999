from typing import List

def getFrequencies(v: List[int]) -> List[int]:
    # Count frequencies of elements in the list
    freq_dict = {}
    for num in v:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    
    # Find the element with the highest frequency
    max_freq = max(freq_dict.values())
    max_freq_element = min([key for key, value in freq_dict.items() if value == max_freq])
    
    # Find the elements with the lowest frequency and pick the smallest one
    min_freq = min(freq_dict.values())
    min_freq_elements = [key for key, value in freq_dict.items() if value == min_freq]
    min_freq_element = min(min_freq_elements)
    
    return [max_freq_element, min_freq_element]

