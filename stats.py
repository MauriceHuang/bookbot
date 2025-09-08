def get_character_count(path_to_file):
    characters={}
    unique_characters = set()
    with open(path_to_file) as f:
        file_contents = f.read()
        for s in file_contents:
            if s.lower() in unique_characters :
                characters[s.lower()] += 1
            else:
                unique_characters.add(s.lower())
                characters[s.lower()] = 1
    # print(characters)
    return characters

def sort_on(items):
    return items['num']

def sorting(path_to_file):
    char_dic = get_character_count(path_to_file)
    char_dic_arr = []
    for key, value in char_dic.items():
        char_dic_kv = {}
        char_dic_kv['char'] = key
        char_dic_kv['num'] = value
        char_dic_arr.append(char_dic_kv)

    char_dic_arr.sort(reverse=True,key=sort_on)
    for item in char_dic_arr:
        print(f"{item['char']}: {item['num']}")

def get_num_words(path_to_file):
    text = []
    with open(path_to_file) as f:
        file_contents = f.read()
        text = file_contents.split()
        leng = len(text)
        print('----------- Word Count ----------')
        print(f"Found {leng} total words")


