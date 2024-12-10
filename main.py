def main():
    source = "books/frankenstein.txt"
    file_content = open_file(source)

    wordcount = count_words(file_content)
    character_count = count_characters(file_content)
    character_list = formated_character_count(character_count)
    print(f"--- Begin report of {"books/frankenstein.txt"} ---")
    print(f"{wordcount} words found in the documment\n\n")
    for item in character_list:
        print(f"The {item["character"]} character was found {item["num"]} times")
    print("--- End report ---")

def formated_character_count(character_count):
    formatted_list = []
    for key, value in character_count.items():
        formatted_list.append({"character": key, "num": value})
        #print(f"{key} {value}")
    formatted_list.sort(reverse=True, key=sort_on)
    return formatted_list

def sort_on(dict):
    return dict["num"]


def count_characters(fille_content):
    lowered_string = fille_content.lower()
    character_count = dict()

    for char in lowered_string:
        if char.isalpha():
            if char in character_count:
                character_count[char] += 1
            #   print(f"{char}:{character_count[char]}  true")

            else:
                character_count[char] = 1
            #    print(f"{char}  false")
    return character_count
    

   
    
def open_file(path_to_file):
    with open(path_to_file) as file:
        file_contents = file.read()
    return file_contents

def count_words(file_contents):
    return len(file_contents.split())

    
main()