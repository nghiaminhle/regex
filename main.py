
def regex_matcher(s, pattern):
    return match(s, '', 0, pattern)

def match(s, prefix_str, p_index, pattern):
    if s == prefix_str:
        if p_index == len(pattern):
            return True
        else:
            return False
    if len(prefix_str) > len(s) or p_index == len(pattern):
        return False
    if pattern[p_index] == '.':
        new_prefix = prefix_str + s[len(prefix_str)]
        return match(s, new_prefix, p_index + 1, pattern)
    elif pattern[p_index] == '*':
        new_prefix = prefix_str
        s_index = len(prefix_str)
        while s_index < len(s):
            new_prefix = new_prefix + s[s_index]
            if match(s, new_prefix, p_index, pattern):
                return True
            if match(s, new_prefix, p_index + 1, pattern):
                return True
            s_index += 1
        return False
    else:
        if s[len(prefix_str)] != pattern[p_index]:
            return False
        new_prefix = prefix_str + s[len(prefix_str)]
        return match(s, new_prefix, p_index + 1, pattern)

def main():
    testcases = [
        ['a', 'a', True],
        ['a', 'b', False],
        ['c', '.', True],
        ['abcd', 'a.c', False],
        ['abcabfxyza', '*ab*klm', False],
        ['abcabf', '*abf', True],
        ['abccccc', '*ccc', True],
        ['abc', 'c*', False],
        ['abc', '*d', False],
        ['abcd', 'a*d', True]
        #['', '*', True],
        #['abc', '*c*', True],
        #['bedc', '*b*c', True],
        #['abcd', 'a.c*', True],
        #['abcd', 'a.c*.', True],
        #['', '*.', False]
    ]

    for case in testcases:
        print('Executing test case %s %s %s' % (case[0], case[1], case[2]))
        assert regex_matcher(case[0], case[1]) == case[2]
    
    #print(regex_matcher('abcd', 'a.c*.'))


if __name__ == "__main__":
    main()
