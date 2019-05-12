from time import process_time as pt

print(pt())

ones = {
    '0': '',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}

tens = {
    '10': 'ten',
    '11': 'eleven',
    '12': 'twelve',
    '13': 'thirteen',
    '14': 'fourteen',
    '15': 'fifteen',
    '16': 'sixteen',
    '17': 'seventeen',
    '18': 'eighteen',
    '19': 'nineteen',
    '2': 'twenty',
    '3': 'thirty',
    '4': 'forty',
    '5': 'fifty',
    '6': 'sixty',
    '7': 'seventy',
    '8': 'eighty',
    '9': 'ninety',
    '0': ''
}

def in_words(n):
    n = str(n)
    l = len(n)
    if l == 1:
        return ones[n]
    elif l == 2:
        if n[0] == '1':
            return tens[n]
        else:
            return tens[n[0]] + ' ' + ones[n[1]]
    elif l == 3:
        return ones[n[0]] + ' hundred' + (' and ' + in_words(n[1:]) if n[1] != '0' or n[2] != '0' else '')
    elif l == 4:
        return ones[n[0]] + ' thousand' + (' and ' + in_words(n[1:]) if n[1] != '0' or n[2] != '0' or n[3] != '0' else '')

print(sum([len(in_words(x).replace(' ', '')) for x in range(1, 1001)]))

print(pt())
