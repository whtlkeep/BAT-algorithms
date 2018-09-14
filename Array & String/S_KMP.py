def compute_temporary_array(pattern):
    size_p = len(pattern)
    lsp = [0] * size_p
    index = 0
    i = 1
    while i < size_p:
        if pattern[i] == pattern[index]:
            lsp[i] = index + 1
            index += 1
            i += 1
        else:
            if index != 0:
                index = lsp[index - 1]
            else:
                lsp[i] = 0
                i += 1
    return lsp


def kmp(text, pattern):
    lsp = compute_temporary_array(pattern)
    i, j = 0, 0
    size_t = len(text)
    size_p = len(pattern)
    count = 0
    while i < size_t and j < size_p:
        count += 1
        print(count)
        if text[i] == pattern[j]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = lsp[j - 1]
            else:
                i += 1
    if j == size_p:
        return i - size_p
    else:
        return -1


if __name__ == '__main__':
    src = 'ababcabcabd'
    sub_string = 'abcabd'
    result = kmp(src, sub_string)
    print(result)
