def count_some_words(filename,count_word):
    """
    Count some words in text:
    #filename = the name of your text file
    #count_word - the word which you want to count in the txt file or files
    """

    try:
        with open(filename, encoding='utf-8') as f:
            lines = f.readlines()  # read lines in files
    except FileNotFoundError:
        print(f"\nFile {filename} doesn't exist")
    else:

        word_counter = []  # empty list of count_word each lines
        for line in lines:
            my_line = line.rstrip()  #print every single line separately
            count_in_line = my_line.count(count_word.lower())  #count_word in line
            word_counter.append(count_in_line)  #apend to the list
            # print(my_line)
        # print(word_counter)
        count_word_quantity = sum(word_counter)
        # print(count_word_quantity)
        print(f"\nFile: {filename} using '{count_word}' word: "
              + str(count_word_quantity) + " times.")

count_some_words('example.txt.', 'word')

