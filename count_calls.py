calls = 0
def count_calls():
    global calls
    calls = calls + 1

def string_info(string_):
    count_calls()
    tuple_string_ = len(string_), string_.upper(), string_.lower()
    return tuple_string_

def is_contains(string_, list_to_search_):
    count_calls()
    cont_ = False
    for str_ in list_to_search_:
        if str_.lower() == string_.lower():
            cont_ = True
    return cont_

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)





