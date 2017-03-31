# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def match_ends(words):
    count = 0
    for word in words:
        if len(word) >= 2 and word[0] == word[-1]:
            count = count + 1
    return count


def front_x(words):
    word_x = []
    other_words = []
    for word in words:
        if word[0] == 'x':
            word_x.append(word)
            #not sure if this sorted function is in the correct place
        else:
            other_words.append(word)
    sorted_x = sorted(word_x)
    sorted_other = sorted(other_words)
    sorted_words = sorted_x + sorted_other
    return sorted_words


def sort_last(tuples):
    return sorted(tuples, key = lambda x: x[-1])


def remove_adjacent(nums):
    new_nums = []
    for i in range(nums[-1]):
        if nums[i] != nums[i+1]:
            new_nums.append(nums[i])
    if len(nums) > 1 and nums[-1] != new_nums[-1]:
        new_nums.append(nums[-1])
    return new_nums


def linear_merge(list1, list2):
    list_sorted = sorted(list1 + list2)
    return list_sorted
