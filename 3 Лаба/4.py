import string
import re

class StringFormatter(object):
    separator = [' ']

    def __init__(self, line):
        self._line = line

    def delete_by_num(self, n):
        temp = []
        words = self._line.split(' ')
        for i in range(len(words)):
            if len(words[i]) < n:
                temp.append(words[i])
        return ' '.join(temp)

    def replace_nums(self):
        return re.sub('\d', '*', self._line)

    def insert_spaces(self):
        tmp = []
        line = self._line
        for i in range(len(line)):
            tmp.append(line[i])
            tmp.append(' ')
        return ''.join(tmp)

    def sort_by_size(self):
        words = self._line.split()
        return ' '.join(sorted(words, key=lambda word: len(word)))

    def sort_by_lec(self):
        words = self._line.split()
        return ' '.join(sorted(words))

example = 'Hello New Fuck1ng W0rld'
obj = StringFormatter(example)

print('Basic string: ', example, end='\n')
print('String, where was deleted all wards, that have len lesser than 6: ', obj.delete_by_num(6), end='\n')
print('String, where all nums were replace by \'*\': ', obj.replace_nums(), end='\n')
print('String, where between all symbols were placed \' \': ', obj.insert_spaces(), end='\n')
print('Sorted string by words size: ', obj.sort_by_size(), end='\n')
print('Sorted string by lexographica: ', obj.sort_by_lec(), end='\n')