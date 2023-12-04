print('This program calculates the net salaray after various deductions')

# Constants
FEDERAL_STANDARD_DEDUCTION = 13200

FICA_MAX = 147000
FICA_RATE = 0.0765

STATE_STANDARD_DEDUCTION = {
 'california': 4609,
 'new york': 8000 
}

FEDERAL_TAX_BRACKETS = [
(10400, 0.10),
(41225, 0.12),
(89400, 0.22),
(174050, 0.24),
(215400, 0.32),
(549900, 0.35),
(1000000, 0.37)
]

STATE_TAX_BRACKETS = {
 'california': [
(9076, 0.01),
(22771, 0.02),
(34211, 0.04),
(48898, 0.06),
(48897, 0.08),
(59878, 0.093),
(71805, 0.103),
(100000, 0.113)
],
 'new york': [
(8500, 0.04),
(11700, 0.045),
(13900, 0.0525),
(21400, 0.059),
(80650, 0.0645),
(215400, 0.0685),
(1077550, 0.0882),
(1000000, 0.103)
]
}

def standard_state_deduction(state):
    """
    Returns the standard deductions for state
    """
    return STATE_STANDARD_DEDUCTION[state]

def calculate_federal_tax(salary):
    """
    Federal tax rate
    """
    tax_rate = 0
    for tax_bracket in enumerate(FEDERAL_TAX_BRACKETS):
        if salary < tax_bracket[1][0]:
            print(f'Federal Tax Rate: {tax_rate}')
            return salary * tax_rate
        tax_rate = tax_bracket[1][1]

def fica(salary):
    """
    FICA
    """
    if salary > FICA_MAX:
        return FICA_MAX * FICA_RATE
    return salary * FICA_RATE

def calculate_state_tax(state, salary):
    """
    Returns the tax bracket for the new york state based upon salary
    """
    tax_rate = 0
    for tax_bracket in enumerate(STATE_TAX_BRACKETS[state]):
        if salary < tax_bracket[1][0]:
            print(f'State Tax Rate: {tax_rate}')
            return salary * tax_rate
        tax_rate = tax_bracket[1][1]

gross_salary = input('Please input your gross salary: ')
state = input('Please input the state you live in: ')

try:
    gross_salary = float(gross_salary)
    net_salary = gross_salary

    # Calculate Federal Tax Rate
    deducted_fed_salary = net_salary - FEDERAL_STANDARD_DEDUCTION
    federal_tax = calculate_federal_tax(deducted_fed_salary)

    # Calculate State Tax Rate
    deducted_state_salary = net_salary - standard_state_deduction(state)
    state_tax = calculate_state_tax(state.lower(), deducted_state_salary)

    # Calculate FICO
    fica_tax = fica(net_salary)

    # Calculate Net
    net_salary = net_salary - federal_tax - state_tax - fica_tax # type: ignore

    print(f'Gross Salary: ${gross_salary}')
    print(f'Federal Tax: ${federal_tax}')
    print(f'State Tax: ${state_tax}')
    print(f'FICA: ${fica(fica_tax)}')
    print(f'Net Salary: ${net_salary}')
except ValueError:
    print('Gross salary must be a digit value')
