def num_words(file_contents):
    my_list =file_contents.split()
    return len(my_list)

def word_and_count(file_contents):
    wc = dict()
    my_list =file_contents.split()
    for word in my_list:
        if word in wc:
            wc[word] = wc.get(word) + 1
        else:
            wc.update({word : 1})
    print(wc)
    
