def main ():
    file_path = "books/frankenstein.txt"
    book_text = get_text(file_path)
    words = text_split(book_text)
    char_dict = word_to_char(words)
    sorted_char_list = sort_chars(char_dict)

    print (f">>> Information from {file_path} <<<")
    print (f"The book conatains {len(words)} words.")
    print ("")
    for each_char in sorted_char_list:
        print (f"There are {each_char['count']} instances of of the letter '{each_char['character']}'")
    print(">>> END <<<")

def get_text(path):
    with open(path) as f:
        return f.read()
    
def text_split(long_string):
    words = long_string.split()
    return words

def word_to_char(word_list):
    new_dict = {}
    for word in word_list:
        lower = word.lower()
        for letter in lower:
            if letter in new_dict:
                new_dict[letter] += 1
            else:
                new_dict[letter] = 1
    return new_dict

def sort_on(d):
    return d['count']
            
def sort_chars(chardict):
    sort_list = []
    for c in chardict:
        dict_c = {}
        if c.isalpha():
            dict_c['character'] = c
            dict_c['count'] = chardict[c]
            sort_list.append(dict_c)
    sort_list.sort(reverse=True, key=sort_on)
    return (sort_list)

main()
