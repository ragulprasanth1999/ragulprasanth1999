import re
inp = input("Enter camel case: ")
var = re.findall("[A-Z]", inp)
var2 = re.sub(r"([a-z])([A-Z])", r"\1_\2", inp)
result = var2.split('_')
final_result = ('_'.join(result)).lower()
print(final_result)
