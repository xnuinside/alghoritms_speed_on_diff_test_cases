"""
find how much symbols from first string exist in second string
"""
from timeit import timeit

s = 'wklaaosd'
j = 'dowlqwnsa'


def count_symbols_in_str_with_finding_string_with_less_symbols():
    count = 0
    iter_ = s if len(s) <= len(j) else j
    checker_ = s if len(s) >= len(j) else j
    for symbol in iter_:
        if symbol in checker_:
            count += 1


def count_symbols_in_str_straightforward():
    # this method will be faster only in case when both of our strings
    # very short or 's' string always shorter when j
    count = 0
    for symbol in s:
        if symbol in j:
            count += 1


print(timeit(count_symbols_in_str_with_finding_string_with_less_symbols, number=1000000))
print(timeit(count_symbols_in_str_straightforward, number=1000000))
# results on my laptop:
#   count_symbols_in_str_with_finding_string_with_less_symbols - 1.092139339
#   count_symbols_in_str_straightforward - 0.785285663

s = """Miusov, as a man man of breeding and deilcacy, could not but feel some inwrd qualms, 
when he reached the Father Superior's with Ivan: he felt ashamed of havin lost his temper. 
He felt that he ought to have disdaimed that despicable wretch, Fyodor Pavlovitch, too much to have been 
upset by him in Father Zossima's cell, and so to have forgotten himself. "Teh monks were not to blame, in any case," 
he reflceted, on the steps. "And if they're decent people here (and the Father Superior, I understand, is a nobleman) 
why not be friendly and courteous withthem? I won't argue, I'll fall in with everything, I'll win them by politness, 
and show them that I've nothing to do with that Aesop, thta buffoon, that Pierrot, and have merely been takken in 
over this affair, just as they have."

"""
j = 'dowlqwnsa'

print(timeit(count_symbols_in_str_with_finding_string_with_less_symbols, number=1000000))
print(timeit(count_symbols_in_str_straightforward, number=1000000))
# results on my laptop:
#   count_symbols_in_str_with_finding_string_with_less_symbols - 1.272056298
#   count_symbols_in_str_straightforward - 52.103340614

# Huge difference, right?
