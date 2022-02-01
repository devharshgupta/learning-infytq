
def find_correct(word_dict):
    data = [0, 0, 0]

    for word in word_dict:
        count = 0
    # start writing your code here
        if len(word) != len(word_dict[word]):
            data[2] += 1
            continue
        elif word == word_dict[word]:
            data[0] += 1
            continue

        else:
            for i in range(0, len(word)):
                if word[i] != word_dict[word][i]:
                    count += 1

            if count > 2:
                data[2] += 1
            else:
                data[1] += 1
    return data


word_dict = {"THEIR": "THEIR", "BUSINESS": "BISINESS",
             "WINDOWS": "WINDMILL", "WERE": "WEAR", "SAMPLE": "SAMPLE"}
print(find_correct(word_dict))
