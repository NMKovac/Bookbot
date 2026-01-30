def num_words(file_contents):
    my_list =file_contents.split()
    return len(my_list)

def word_and_count(file_contents):
    wc = dict()
    my_list =file_contents.split()
    for word in my_list:
        for char in word:
            if char in wc:
                wc[char] = wc.get(char) + 1
            else:
                wc.update({char : 1})
    sortedDIC = list(sorted(wc.items(), key=lambda item: item[1], reverse=True))
    return(sortedDIC)
    
