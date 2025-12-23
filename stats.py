def get_num_words(text):
    word_arr = text.split()
    num_words = len(word_arr)
    print(f"Found {num_words} total words")

def get_char_frequency(text):
    char_frequency = {}
    for char in text:
        char = char.lower()
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1
    return char_frequency

def dict_to_sorted_list(items):
    sorted_list = []
    for k, v in items.items():
        sorted_list.append({"char": k, "num":v})

    sorted_list.sort(reverse=True, key=sort_on)
    sorted_dict = {item["char"]: item["num"] for item in sorted_list}
    for k, v in sorted_dict.items():
        if k.isalpha():
            print(f"{k}: {v}")
    
def sort_on(items):
    return items["num"]