import copy

def processFunc(op_index, full_program, func):

    a = full_program[op_index + 1]
    b = full_program[op_index + 2]
    c = full_program[op_index + 3]

    full_program[c] = func(full_program[a], full_program[b])
    return full_program


def processOp(op_index, full_program):
    op_code = full_program[op_index]

    if (op_code == 1):
        full_program = processFunc(op_index, full_program, lambda a, b: a + b)
    elif (op_code == 2):
        full_program = processFunc(op_index, full_program, lambda a, b: a * b)
    elif (op_code == 99):
        return full_program
    else:
        print("Got op code {} at position {}".format(op_code, op_index))
        raise Exception('Incorrect op')

    return processOp(op_index + 4, full_program)


if __name__ == "__main__":

    with open("code.txt") as code_file:
        code = [int(i) for i in code_file.readline().split(",")]

    original_code = copy.deepcopy(code)

    code[1] = 12
    code[2] = 2

    program = processOp(0, code)
    print("Answer part 1: {}".format(program[0]))


    desired_res = 19690720
    for noun in range(0,99):
        for verb in range(0,99):
            code = copy.deepcopy(original_code)
            code[1] = noun
            code[2] = verb
            program = processOp(0, code)
            if program[0] == desired_res:
                print("Answer part 2: {}".format(100 * noun + verb))
                exit()

