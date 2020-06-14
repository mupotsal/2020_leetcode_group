def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """

    # split the string
    # concatenate from the end

    words_list = split(s)
    # can use words_list.reverse()
    req_rever = ""
    for i in range(len(words_list) - 1, -1, -1):
        req_rever += words_list[i]
        if i != 0:
            req_rever += " "
    return req_rever
