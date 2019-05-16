from commons import runtime

name_list = open('assets/22_names.txt').read().replace('"', '').split(',')
alfabet_init = ord('A') - 1

def name_value(name):
    return sum([ord(l) - alfabet_init for l in name])

def resolve():
    name_list.sort()
    print(name_value('COLIN'))
    total = 0
    for x in range(0, len(name_list)):
        total += name_value(name_list[x]) * (x + 1)
    print(total)

runtime(resolve)
    
