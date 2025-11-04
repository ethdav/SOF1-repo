sample_text = (" As Python s creator, I'd like to say a few words about its "+
              "origins adding a bit of personal philosophy. "+
              "Over six years ago in December I was looking for a "+
              "hobby programming project that would keep me occupied "+
              "during the week around Christmas. My office, "+
              "a government run research lab in Amsterdam would be closed "+
              "but I had a home computer and not much else on my hands "+
              " I decided to write an interpreter for the new scripting "+
              "language  I had been thinking about lately a descendant of ABC "+
              "that would appeal to UnixC hackers I chose Python as a "+
              "working title for   the project being in a slightly irreverent "+
              "mood and a big fan of Monty Python s Flying Circus.  ")

######################### EXERCISE 1 ##########################################

from string import punctuation as punc

def split_text(text, separators=" "):
    """Emulates the split() function

    Args:
        text (str): the string to be split
        separators (str, optional): All of the characters used to split
        the text. Defaults to " ".
    Returns:
        A list of strings, where each element is all characters in
        between separators
    """
    sep_list = [x for x in separators]
    temp_word = None
    separated = []
    for char in range(len(text)):
        if text[char] in sep_list:
            if temp_word == None:
                pass
            else:
                separated.append(temp_word)
                temp_word = None
        else:
            if temp_word == None:
                temp_word = text[char]
            else:
                temp_word += text[char]
    if temp_word is not None:
        separated.append(temp_word)
    return separated

def get_words_frequencies(text):
    """Returns a dictionary containing each word and its frequencies

    Args:
        text (_type_): _description_
    """
    split = split_text(text,punc+" ")
    freq_dict = dict()
    for item in split:
        if item.lower() not in freq_dict:
            freq_dict[item.lower()] = 1
        else:
            freq_dict[item.lower()] += 1
    return freq_dict

def flatten(list_2d):
    """Flattens a 2D list

    Args:
        list_2d (_type_): _description_
    """
    flattened = []      # I feel like theres a way to do this with list comprehension
    for index in list_2d:
        for item in index:
            flattened.append(item)
    return flattened

def flatten_w_comprehension(list_2d):
    flattened = [x for sublist in list_2d for x in sublist]
    return flattened

def main():
    # sample = "This is a, somewhat, more complicated test."
    # print(split_text(sample," ',."))
    # print(get_words_frequencies(sample_text))
    list_2d = [[1,2,3],[],[4,5,6]]
    print(flatten(list_2d))
    print(flatten_w_comprehension(list_2d))

main()