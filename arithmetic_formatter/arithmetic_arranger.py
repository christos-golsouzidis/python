

def read_operands(problems):
    '''
    Params: 
        problems: a list of strings, required
    Returns:
        a list of tuples if successful else
        a string defining the error
    '''
    out = []

    for problem in problems:
        n1, op, n2 = problem.split()
        if len(n1) > 4 or len(n2) > 4:
            return 'ERROR_DIGIT'
        if op != '+' and op != '-':
            return 'ERROR_OPER'
        try:
            _ = int(n1)
            _ = int(n2)
        except:
            return 'ERROR_NUMBER'
        out.append((n1, op, n2))
    return out


def format_operands(problems, result):
    
    # formatted problem
    fproblem = []

    for problem in problems:
        fnum1 = '' #formatted num1
        fnum2 = ''
        fdashes = ''

        num1, op, num2 = problem
        formatlen = max(len(num1),len(num2))

        # padding which spaces so that both operands have the same length
        for k in range(formatlen - len(num1)):
            fnum1 += ' '
        fnum1 += num1
        for k in range(formatlen - len(num2)):
            fnum2 += ' '
        fnum2 += num2

        # add 2 extra spaces to fnum1
        # and op plus 1 extra space to fnum2
        fnum1 = '  ' + fnum1
        fnum2 = op + ' ' + fnum2

        # add dashes
        for k in range(formatlen + 2):
            fdashes += '-'
        
        # add result if true
        fres = ''
        if result == True:
            res = str(int(num1) + int(num2)) if op == '+' else str(int(num1) - int(num2))
            for k in range(formatlen + 2 - len(res)):
                fres += ' '
            fres += res

        # test the printing
        #print(f'{fnum1}\n{fnum2}\n{fdashes}\n{fres}\n')

        fproblem.append((fnum1,fnum2,fdashes,fres))

    return fproblem


def format_lines(fproblems):
    line1 = ''
    line2 = ''
    lined = ''
    liner = ''
    separator = '    ' # 4 spaces

    for fproblem in fproblems:
        fnum1,fnum2,fdashes,fres = fproblem
        line1 += fnum1 + separator
        line2 += fnum2 + separator
        lined += fdashes + separator
        liner += fres + separator

    line1 = line1[:-4]
    line2 = line2[:-4]
    lined = lined[:-4]
    liner = liner[:-4]

    return line1, line2, lined, liner


def arithmetic_arranger(problems, result=False):
    '''
    Params: 
        problems: a list of strings, required
        result: Display the results if true; default=False, optional
    Returns:
        a string of the formatted output
        a string defining the error
    '''
    if len(problems) > 5:
        return 'Error: Too many problems.'
    out = read_operands(problems)
    if out == 'ERROR_DIGIT':
        return 'Error: Numbers cannot be more than four digits.'
    elif out == 'ERROR_OPER':
        return "Error: Operator must be '+' or '-'."
    elif out == 'ERROR_NUMBER':
        return 'Error: Numbers must only contain digits.'
    
    fouts = format_operands(out, result)

    line1, line2, lined, liner = format_lines(fouts)
    arranged_problems = f'{line1}\n{line2}\n{lined}\n'
    if result:
        arranged_problems += f'{liner}\n'


    return arranged_problems
