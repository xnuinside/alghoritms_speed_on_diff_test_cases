"""
find how much symbols from first string exist in second string
"""
from timeit import timeit

first = 'wklaaosd'
second = 'dowlqwnsa'


def count_symbols_in_str_with_finding_string_with_less_symbols():
    count = 0
    iter_ = first if len(first) <= len(second) else second
    checker_ = first if len(first) >= len(second) else second
    for symbol in iter_:
        if symbol in checker_:
            count += 1


def count_symbols_in_str_straightforward():
    # this method will be faster only in case when both of our strings
    # very short or 's' string always shorter when j
    count = 0
    for symbol in first:
        if symbol in second:
            count += 1


def count_symbols_in_str_with_finding_string_with_less_symbols_using_sets():
    count = 0
    s = set(first)
    j = set(second)
    iter_ = s if len(s) <= len(j) else j
    checker_ = s if len(s) >= len(j) else j
    for symbol in iter_:
        if symbol in checker_:
            count += 1


def count_symbols_in_str_straightforward_using_sets():
    # this method will be faster only in case when both of our strings
    # very short or 's' string always shorter when j
    count = 0
    s = set(first)
    j = set(second)
    for symbol in s:
        if symbol in j:
            count += 1


print("1. Short strings \n")
print('count_symbols_in_str_with_finding_string_with_less_symbols -',
      timeit(count_symbols_in_str_with_finding_string_with_less_symbols, number=1000000))
print('count_symbols_in_str_straightforward -', timeit(count_symbols_in_str_straightforward, number=1000000))
print('count_symbols_in_str_with_finding_string_with_less_symbols_using_sets - ',
      timeit(count_symbols_in_str_with_finding_string_with_less_symbols_using_sets, number=1000000))
print('count_symbols_in_str_straightforward_using_sets - ',
      timeit(count_symbols_in_str_straightforward_using_sets, number=1000000))
# results on my laptop:
#   --- strings
#   count_symbols_in_str_with_finding_string_with_less_symbols - 1.158445372
#   count_symbols_in_str_straightforward - 0.8467845240000003
#   --- sets, results explanation: because you spend time to create set, it's not free operation
#   count_symbols_in_str_with_finding_string_with_less_symbols_using_sets -  1.772400781
#   count_symbols_in_str_straightforward_using_sets -  1.4363745010000004


print("\n\n2. Big first string \n")
first = """Miusov, as a man man of breeding and deilcacy, could not but feel some inwrd qualms, 
when he reached the Father Superior's with Ivan: he felt ashamed of havin lost his temper. 
He felt that he ought to have disdaimed that despicable wretch, Fyodor Pavlovitch, too much to have been 
upset by him in Father Zossima's cell, and so to have forgotten himself. "Teh monks were not to blame, in any case," 
he reflceted, on the steps. "And if they're decent people here (and the Father Superior, I understand, is a nobleman) 
why not be friendly and courteous withthem? I won't argue, I'll fall in with everything, I'll win them by politness, 
and show them that I've nothing to do with that Aesop, thta buffoon, that Pierrot, and have merely been takken in 
over this affair, just as they have."

"""
second = 'dowlqwnsa'

print('count_symbols_in_str_with_finding_string_with_less_symbols -',
      timeit(count_symbols_in_str_with_finding_string_with_less_symbols, number=1000000))
print('count_symbols_in_str_straightforward -', timeit(count_symbols_in_str_straightforward, number=1000000))
print('count_symbols_in_str_with_finding_string_with_less_symbols_using_sets - ',
      timeit(count_symbols_in_str_with_finding_string_with_less_symbols_using_sets, number=1000000))
print('count_symbols_in_str_straightforward_using_sets - ',
      timeit(count_symbols_in_str_straightforward_using_sets, number=1000000))
# results on my laptop:
#   --- strings
#   count_symbols_in_str_with_finding_string_with_less_symbols - 1.286378396
#   count_symbols_in_str_straightforward - 61.436745639
#   --- sets
#   count_symbols_in_str_with_finding_string_with_less_symbols_using_sets -  24.471179356000007
#   count_symbols_in_str_straightforward_using_sets -  21.615206293


print("\n\n3. Big second string \n")
first = 'dowlqwnsa'

second = """Miusov, as a man man of breeding and deilcacy, could not but feel some inwrd qualms, 
when he reached the Father Superior's with Ivan: he felt ashamed of havin lost his temper. 
He felt that he ought to have disdaimed that despicable wretch, Fyodor Pavlovitch, too much to have been 
upset by him in Father Zossima's cell, and so to have forgotten himself. "Teh monks were not to blame, in any case," 
he reflceted, on the steps. "And if they're decent people here (and the Father Superior, I understand, is a nobleman) 
why not be friendly and courteous withthem? I won't argue, I'll fall in with everything, I'll win them by politness, 
and show them that I've nothing to do with that Aesop, thta buffoon, that Pierrot, and have merely been takken in 
over this affair, just as they have."

"""
print('count_symbols_in_str_with_finding_string_with_less_symbols -',
      timeit(count_symbols_in_str_with_finding_string_with_less_symbols, number=1000000))
print('count_symbols_in_str_straightforward -', timeit(count_symbols_in_str_straightforward, number=1000000))
print('count_symbols_in_str_with_finding_string_with_less_symbols_using_sets - ',
      timeit(count_symbols_in_str_with_finding_string_with_less_symbols_using_sets, number=1000000))
print('count_symbols_in_str_straightforward_using_sets - ',
      timeit(count_symbols_in_str_straightforward_using_sets, number=1000000))

# results on my laptop:
#   --- strings
#   count_symbols_in_str_with_finding_string_with_less_symbols - 3.6363547069999953
#   count_symbols_in_str_straightforward - 2.334552157999994
#   --- sets
#   count_symbols_in_str_with_finding_string_with_less_symbols_using_sets -  36.368135777999996
#   count_symbols_in_str_straightforward_using_sets -  33.071070564999985

print("\n\n4. Both strings are big \n")
first = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer 
took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, 
but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s 
with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing 
software like Aldus PageMaker including versions of Lorem Ipsum."""

second = """Miusov, as a man man of breeding and deilcacy, could not but feel some inwrd qualms, 
when he reached the Father Superior's with Ivan: he felt ashamed of havin lost his temper. 
He felt that he ought to have disdaimed that despicable wretch, Fyodor Pavlovitch, too much to have been 
upset by him in Father Zossima's cell, and so to have forgotten himself. "Teh monks were not to blame, in any case," 
he reflceted, on the steps. "And if they're decent people here (and the Father Superior, I understand, is a nobleman) 
why not be friendly and courteous withthem? I won't argue, I'll fall in with everything, I'll win them by politness, 
and show them that I've nothing to do with that Aesop, thta buffoon, that Pierrot, and have merely been takken in 
over this affair, just as they have."

"""
print('count_symbols_in_str_with_finding_string_with_less_symbols -',
      timeit(count_symbols_in_str_with_finding_string_with_less_symbols, number=1000000))
print('count_symbols_in_str_straightforward -', timeit(count_symbols_in_str_straightforward, number=1000000))
print('count_symbols_in_str_with_finding_string_with_less_symbols_using_sets - ',
      timeit(count_symbols_in_str_with_finding_string_with_less_symbols_using_sets, number=1000000))
print('count_symbols_in_str_straightforward_using_sets - ',
      timeit(count_symbols_in_str_straightforward_using_sets, number=1000000))

# results on my laptop:
#   --- strings
#   count_symbols_in_str_with_finding_string_with_less_symbols - 76.660539871
#   count_symbols_in_str_straightforward - 87.18539081400002
#   --- sets
#   count_symbols_in_str_with_finding_string_with_less_symbols_using_sets -  48.15432622099996
#   count_symbols_in_str_straightforward_using_sets -  43.946403282000006
