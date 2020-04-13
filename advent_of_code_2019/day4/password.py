from functools import reduce

smallest = 272091
largest = 815432

actual_min = 277777
actual_largest = 777777

def isDoublePresent(seq):
    double_present = [ a == b for a, b in zip(seq[:-1], seq[1:])]
    return any(double_present)

def isASingleDoublePresent(seq):
    doubles = [a if a == b else -1 for a, b in zip(seq[:-1], seq[1:])]
    doubles = filter(lambda x : x >= 0, doubles)
    double_counts = [doubles.count(num) for num in doubles]
    return any(count == 1 for count in double_counts)

#     if len(doubles) == 0:
#         return False
#     if len(doubles) == 1:
#         return True
# 
#     return not isDoublePresent(doubles)

def isIncreasing(seq):
   increasing = [ a <= b for a, b in zip(seq[:-1], seq[1:])]
   return reduce((lambda x, y: x and y), increasing)

def seqToNumber(seq):
    return int("".join([str(x) for x in seq]))

def numberToSeq(num):
    return [int(x) for x in str(num)]

def passwordValid(num):
    seq = numberToSeq(num)
    return isDoublePresent(seq) and isIncreasing(seq)

def passwordValidPt2(num):
    seq = numberToSeq(num)
    return isASingleDoublePresent(seq) and isIncreasing(seq)

def countValidSequences(cur_seq, double_created):
    if len(cur_seq) == 6:
        if not double_created:
            return 0

        password = seqToNumber(cur_seq)
        if smallest <= password and password <= largest:
            return 1
        return 0

    # All possible except double
    valid_range_for_next = range(cur_seq[-1] + 1, 10)

    counts = [countValidSequences(cur_seq + [next_elem], double_created) for next_elem in valid_range_for_next]
    # Special case on creating a double
    counts.append(countValidSequences(cur_seq + cur_seq[-1:], True))
    return sum(counts)

def countValidSequencesPt2(cur_seq, last_double, valid_double):
    # double is None if not made yet
    if len(cur_seq) == 6:
        if not valid_double:
            return 0

        password = seqToNumber(cur_seq)
        if smallest <= password and password <= largest:
            print (password)
            return 1
        return 0

    # All possible except double
    valid_range_for_next = range(cur_seq[-1] + 1, 10)
    counts = [countValidSequencesPt2(cur_seq + [next_elem], last_double, valid_double) for next_elem in valid_range_for_next]

    # Special case on creating a double if this value wasn't already used to make a double
    if cur_seq[-1] > last_double:
        counts.append(countValidSequencesPt2(cur_seq + cur_seq[-1:], cur_seq[-1], True))
    elif cur_seq[-1] == last_double:
        counts.append(countValidSequencesPt2(cur_seq + cur_seq[-1:], last_double, False))

    return sum(counts)


if __name__ == "__main__":

    num_passwords = 0
    for start in range(2, 9):
        num_passwords += countValidSequences([start], False)

    # valid_passwords = [1 if passwordValid(num) else 0 for num in range(smallest, largest + 1)]
    # num_passwords = sum(valid_passwords)

    print ("Num valid passwords: {}".format(num_passwords))

    # Doesn't work, not sure why
    # num_passwords = 0
    # for start in range(2, 9):
    #     num_passwords += countValidSequencesPt2([start], 0, False)

    # print ("Num valid passwords part 2: {}".format(num_passwords))

    valid_passwords_pt2 = [1 if passwordValidPt2(num) else 0 for num in range(smallest, largest + 1)]
    num_passwords_pt2 = sum(valid_passwords_pt2)

    print ("Num valid passwords Pt2: {}".format(num_passwords_pt2))

