
def reverseAndUnique(s):
    reversed_str = s[::-1]
    result = []
    for char in reversed_str:
        if not result or char != result[-1]:
            result.append(char)
    return ''.join(result)

print(reverseAndUnique("aaabbc"))
print(reverseAndUnique("hello"))