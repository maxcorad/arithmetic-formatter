import re


def arithmetic_arranger(problems, answer=False):
    # limit number of problems to max. 5
    if len(problems) > 5:
        return "Error: Too many problems."
    # init dict for problem components
    problems_dict = {
        "operand1": [],
        "operand2": [],
        "dashes": [],
        "result": []
    }
    # iterate through problems to generate problem components
    for problem in problems:
        problem = problem.split(" ")
        operand1, operator, operand2 = problem
        # check for valid operations
        if operator not in ("+", "-"):
            return "Error: Operator must be '+' or '-'."
        # check that operand strings are digits and no longer than 4
        if re.match("\d+$", operand1) and re.match("\d+$", operand2):
            if len(operand1) > 4 or len(operand2) > 4:
                return "Error: Numbers cannot be more than four digits."
        else:
            return "Error: Numbers must only contain digits."
        # calculate results
        if operator == "+":
            result = str(int(operand1) + int(operand2))
        else:
            result = str(int(operand1) - int(operand2))
        # calculate number of dashes in result line
        dash_num = max(len(operand1), len(operand2)) + 2
        problems_dict["dashes"].append(dash_num * "-")
        # add leading whitespaces and operator to operands and result
        ws1 = dash_num - len(operand1)
        operand1 = ws1 * " " + operand1
        ws2 = dash_num - len(operand2) - 2
        operand2 = operator + (ws2 + 1) * " " + operand2
        wsr = dash_num - len(result)
        result = wsr * " " + result
        # add operands and result to corresponding lists in dict
        problems_dict["operand1"].append(operand1)
        problems_dict["operand2"].append(operand2)
        problems_dict["result"].append(result)
    # form the arranged lines
    lines = ["    ".join(problems_dict[key]) for key in problems_dict]
    # output with results or not
    if answer:
        arranged_problems = "\n".join(lines)
    else:
        arranged_problems = "\n".join(lines[:-1])
    return arranged_problems
