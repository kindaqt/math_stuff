import re
from utils import gcds, denominators

def solve_polynomial(equation: str) -> list:
    parts = re.split('[+-]', equation)
    print(parts)
    return []




if __name__ == "__main__":
    equations = [
        'x**3-12x**2-45x-50'
    ]
    for equation in equations:
        solve_polynomial(equation)