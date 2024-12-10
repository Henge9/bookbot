def main():
  
    file_content = open_file("books/frankenstein.txt")

    wordcount = count_words(file_content)
    character_count = count_characters(file_content)



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