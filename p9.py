input = input("Input: ")
lis = list(input)
filtered_list = [char for char in lis if char not in "AEIOUaeiou"]
output_str = "".join(filtered_list)
print("Output:", output_str)