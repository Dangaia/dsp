# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
     if count < 10:
             return("Number of donuts:" count)
     elif count >= 10:
             return("Number of donuts: many")


def both_ends(s):
     if len(s) >= 2: 
             return(s[:2]+s[-2:])
     else:
             return('')


def fix_start(s):
    first_char = s[0]
    for i in s[1:]:
        if i == s[0]:
            first_char = first_char + '*'
        else:
            first_char = first_char + i
    return first_char


def mix_up(a, b):
	return(b[:2]+a[2:]+' '+a[:2]+b[2:])


def verbings(s):
	if len(s) >= 3 and s[-3:] != 'ing':
		return (s+'ing')
	elif len(s) >=3 and s[-3:] == 'ing':
		return(s+'ly')
	elif len(s) < 3:
		return(s)


def not_bad(s):
    not_index = s.find('not')
    bad_index = s.find('bad')
    if bad_index > not_index:
        new_string = s[:not_index] + 'good' + s[(bad_index + 4):]
    else:
        new_string = s
    return new_string


def front_back(a, b):
    half_a = int(len(a)/2)
    half_b = int(len(b)/2)
    half_a_one = int((half_a + 1))
    half_b_one = int((half_b + 1))
    if len(a) %2 == 0:
        front_a = (a[:half_a])
        back_a = (a[half_a:])
    else:
        front_a = (a[:(half_a + 1)])
        back_a = (a[half_a_one:])
    if len(b) %2 == 0:
        front_b = (b[:half_b])
        back_b = (b[half_b:])
    else:
        front_b = (b[:half_b_one])
        back_b = (b[half_b_one:])
    return front_a + front_b + back_a + back_b
