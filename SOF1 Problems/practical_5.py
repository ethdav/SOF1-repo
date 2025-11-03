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

def split_text(text, separators=" "):
    """Emulates the split() function

    Args:
        text (_type_): _description_
        separators (str, optional): _description_. Defaults to " ".
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

def main():
    sample = "This is a, somewhat, more complicated test."
    print(split_text(sample," ,"))

main()