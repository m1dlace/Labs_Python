def non_empty(listRetFunction):
    def wrapper():
        returned = listRetFunction()
        deleted = 0
        for i in returned:
            if i is None or i == '':
                returned.pop(deleted)
            deleted += 1
        return returned
    return  wrapper

@non_empty
def getList():
    return ['chapter1', '', 'contents', '', 'line1']

print(getList())