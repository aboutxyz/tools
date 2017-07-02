import difflib

aa = "thunder://QUFodHRwOi8vZGwxMjUuODBzLmltOjkyMC8xNzA2L1vmnYBCU13nrKwxMumbhi9b5p2AQlNd56ysMTLpm4ZfYmQubXA0Wlo="
bb = "thunder://QUFodHRwOi8vZGwxMjUuODBzLmltOjkyMC8xNzA2L1vmnYBCU13nrKwxMembhi9b5p2AQlNd56ysMTHpm4ZfYmQubXA0Wlo="

def inner_compare(str1, str2):
    str1 = str(str1)
    str2 = str(str2)
    str1 += '\n'
    str2 += '\n'
    diff_result = difflib.ndiff(str1.splitlines(1), str2.splitlines(1))
    list_diff = list(diff_result)
    diff_result = ''.join(list_diff)
    return diff_result
    
print inner_compare(aa,bb)
