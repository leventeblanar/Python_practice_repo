text = "aaaabbaaababbabbbaaababbbbbaaabab"
pattern = "aaabab"

def find_pattern(text, pattern):
    for start in range(len(text) - len(pattern) + 1):
        match = True

        for offset in range(len(pattern)):
            if text[start + offset] != pattern[offset]:
                match = False
                break

        if match:
            return start

    return -1


print(find_pattern(text, pattern)) 