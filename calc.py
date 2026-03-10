#!/usr/bin/env python3
import operator
ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

def repl():
    print('Simple calculator. Enter expressions like: 2 + 3')
    while True:
        try:
            s = input('> ').strip()
            if not s:
                continue
            if s in ('quit','exit'):
                break
            parts = s.split()
            if len(parts)!=3:
                print('Use format: <num> <op> <num>')
                continue
            a,op_sym,b = parts
            a = float(a)
            b = float(b)
            if op_sym not in ops:
                print('Supported ops: + - * /')
                continue
            if op_sym=='/' and b==0:
                print('Error: division by zero')
                continue
            res = ops[op_sym](a,b)
            print(res)
        except Exception as e:
            print('Error:', e)

if __name__=='__main__':
    repl()
