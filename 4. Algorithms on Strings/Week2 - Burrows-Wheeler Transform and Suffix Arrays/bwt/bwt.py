# python3
import sys

def BWT(text):
    result = ''
    bwt_strings = []
    bwt_strings.append(text)

    for index in range(1, len(text)):
        temp_text = text[index:] + text[:index]
        # print('Rotating Strings', temp_text)
        bwt_strings.append(temp_text)

    bwt_strings.sort()

    for string in bwt_strings:
        result += string[-1]

    return result

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    # print('Outside the Fn:',text)
    print(BWT(text))
    
