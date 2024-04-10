def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

print("Is 'listen' an anagram of 'silent'?", is_anagram("listen", "silent"))
