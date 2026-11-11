def vowel(s):
    count = 0
    for v in s:
        if v in "aeiouAEIOU":
            count += 1
    return count