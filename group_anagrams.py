def group_anagrams(strings):
    my_dict = {}
    for char in strings:
        sorted_string = ''.join(sorted(char))
        if sorted_string in my_dict:
            my_dict[sorted_string].append(char)
        else:
            my_dict[sorted_string] = [char]

    return list(my_dict.values())

print("1st set:")
print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )

print("\n2nd set:")
print( group_anagrams(["abc", "cba", "bac", "foo", "bar"]) )