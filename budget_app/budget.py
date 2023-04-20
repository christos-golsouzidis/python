class Category:
    def __init__(self,category):
        self.category = category
        self.ledger = []
    
    def __str__(self):
         output = self.__addtitle()
         output += self.__addline()
         output += self.__addtotal()
         return output
    
    def __addtitle(self):
        # find starting position
        # + int(len(self.category) % 2) for left alignment on odd length
        sp = int(len(self.category) / 2) + int(len(self.category) % 2) 
        title = ''
        for _ in range(15 - sp):
            title += '*'

        title += self.category

        for _ in range(30 - len(title)):
            title += '*'

        return title + '\n'
    
    def __addline(self):
        output = ''
        for event in self.ledger:
            formater = ''
            description = event['description']
            amount = str('%.2f' % event['amount'])
            for _ in range(30 - (len(description[:23]) + len(amount[:7]))):
                formater += ' '
            output += description[:23] + formater + amount[:7] + '\n'

        return output

    def __addtotal(self):
        return f'Total: {self.get_balance()}\n'

    def deposit(self, amount, description=''):
        '''
        A deposit method that accepts an amount and description. If no description is given,
        it should default to an empty string. The method should append an object to the ledger 
        list in the form of {"amount": amount, "description": description}.
        '''
        self.ledger.append({'amount':amount, 'description':description})

    def withdraw(self, amount, description=''):
        '''
        A withdraw method that is similar to the deposit method, but the amount passed in 
        should be stored in the ledger as a negative number. If there are not enough funds, 
        nothing should be added to the ledger. This method should return True if the 
        withdrawal took place, and False otherwise.
        '''
        if not self.check_funds(amount):
            return False
        amount *= -1
        self.ledger.append({'amount':amount, 'description':description})
        return True

    def get_balance(self):
        '''
        A get_balance method that returns the current balance of the budget category based on 
        the deposits and withdrawals that have occurred.
        '''
        r = 0
        for k in range(len(self.ledger)):
            r += self.ledger[k]['amount']
        return round(r,2)
    
    def transfer(self, amount, destcat):
        '''
        A transfer method that accepts an amount and another budget category as arguments. 
        The method should add a withdrawal with the amount and the description "Transfer to 
        [Destination Budget Category]". The method should then add a deposit to the other 
        budget category with the amount and the description "Transfer from [Source Budget 
        Category]". If there are not enough funds, nothing should be added to either ledgers. 
        This method should return True if the transfer took place, and False otherwise.
        '''
        if not self.check_funds(amount):
            return False
        
        self.withdraw(amount, f'Transfer to {destcat.category}')
        destcat.deposit(amount, f'Transfer from {self.category}')

        return True
    
    def check_funds(self, amount):
        '''
        A check_funds method that accepts an amount as an argument. It returns False if the 
        amount is greater than the balance of the budget category and returns True otherwise. 
        This method should be used by both the withdraw method and transfer method.
        '''
        if self.get_balance() < amount:
            return False
        return True


def calculate_percentages(categories):

    from math import floor

    nextcat = 0
    fl_amount = [0,0,0,0] # up to 4 categories
    str_category = ['','','','']
    for category in categories:
        for k in range(len(category.ledger)):
            if category.ledger[k]['amount'] < 0:
                fl_amount[nextcat] += category.ledger[k]['amount']
        fl_amount[nextcat] = round(-fl_amount[nextcat],2)

        str_category[nextcat] = category.category
        nextcat += 1
        if nextcat == 4:
            break

    percentage = [0,0,0,0]
    sum = 0
    for k in range(4): sum += fl_amount[k]
    
    for k in range(4): percentage[k] = floor(10 * fl_amount[k] / sum)

    output = [(str_category[k], percentage[k]) for k in range(4)]
    
    return output


def format_percentages(percentages):

    # find max len
    max_len = 0
    for percentage in percentages:
        if len(percentage[0]) > max_len:
            max_len = len(percentage[0])

    line = ['','','','']
    next_line = 0
    for percentage in percentages:
        if not percentage[0]: 
            continue
        # bar padding
        for _ in range(10 - percentage[1]):
            line[next_line] += ' '
        for _ in range(percentage[1]+1):
            line[next_line] += 'o'
        line[next_line] += '-' + percentage[0]
        # text padding
        for _ in range(max_len - len(percentage[0])):
            line[next_line] += ' '
        next_line += 1

    return line


def convert_vertical(lines):
    
    max_rows = len(lines)
    max_columns = len(lines[0])
    vlines = ''

    for v in range(max_columns):
        for h in range(max_rows):
            vlines += lines[h][v]
        vlines += '\n'

    vlines = vlines.splitlines()

    return vlines


def add_spacing(lines):
    
    # add 2 rows for spacing
    empty_line = ''
    for k in range(len(lines[0])):
        empty_line += ' ' if k != 11 else '-'
    
    spaced_lines = []
    for line in lines:
        if not line: continue
        spaced_lines.append(line)
        spaced_lines.append(empty_line)
        spaced_lines.append(empty_line)

    return spaced_lines


def add_pading(lines):
    
    # a label has 5 chars
    labels = ['100| ',
              ' 90| ',
              ' 80| ',
              ' 70| ',
              ' 60| ',
              ' 50| ',
              ' 40| ',
              ' 30| ',
              ' 20| ',
              ' 10| ',
              '  0| ',
              '    -'
              ]
    text = ''
    next_line = 0
    for line in lines:
        # add labels and crlf
        text += labels[next_line] + line + '\n' if next_line < 12 else '     ' + line + '\n'
        next_line += 1

    return text[:-1]


def create_spend_chart(categories):
    '''
    Takes a list of categories as an argument and returns a string that is a bar chart.
    '''

    output = 'Percentage spent by category\n'
    percentages = calculate_percentages(categories)
    lines = format_percentages(percentages)
    lines = add_spacing(lines)
    lines = convert_vertical(lines)
    output += add_pading(lines)

    return output
