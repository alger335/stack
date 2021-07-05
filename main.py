from stack import *


if __name__ == "__main__":
    brackets = '{{[()]}}'
    stack = Stack()
    balance = stack.BalanceCheck(brackets)
    if balance:
        print("Сбалансированно")
    else:
        print("Несбалансированно")
