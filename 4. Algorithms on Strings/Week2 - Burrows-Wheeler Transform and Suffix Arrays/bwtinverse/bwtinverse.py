# python3
import sys

# Implementation1 - Slower
def InverseBWT(bwt_text):
    # write your code here
    inverse = []
    bwt_text_list = []
    letter_freq = dict()

    for letter in bwt_text:
        if letter in letter_freq:
            letter_freq[letter] += 1
        else:
            letter_freq[letter] = 1

        bwt_text_list.append(letter+str(letter_freq[letter]))

#    print(bwt_text_list)

    sort_bwt_text_list = sorted(bwt_text_list)
 #   print(sort_bwt_text_list)

    i = 0
    while i < len(sort_bwt_text_list):
        if i == 0:
            l = bwt_text_list[0]
        else:
            l_idx = sort_bwt_text_list.index(l)
            l = bwt_text_list[l_idx]

        i += 1
        inverse.append(l)

    new_string = ''

    inverse = inverse[::-1]

    for letter in inverse:
        new_string += letter[0]

    return new_string[1:] + '$'

# Implementation2 - Faster
def InverseBWT(bwt_text):
    # write your code here
    inverse = []
    bwt_text_list = []
    letter_freq = dict()
    
    for letter in bwt_text:
        if letter in letter_freq:
            letter_freq[letter] += 1
        else:
            letter_freq[letter] = 1

        bwt_text_list.append(letter+str(letter_freq[letter]))

  #  print(bwt_text_list)

    sort_bwt_text_list = sorted(bwt_text_list)
 #   print(sort_bwt_text_list)

    zip_map = dict(zip(sort_bwt_text_list, bwt_text_list))
#    print(zip_map)
    # print(zip_map)
    new_string = ''
    mid = '$1'

    i = 0
    while i < len(sort_bwt_text_list):
        new_string += zip_map[mid][0]
        mid = zip_map[mid]
        i += 1


    return new_string[::-1][1:] + '$'

if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))
