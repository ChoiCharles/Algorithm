import sys
sys.stdin = open("swea_15041_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    lst = list(input().split())
    stack = []
    while lst:
        a = lst.pop(0)
        try:
            a = int(a)
            stack.append(a)
        except:
            try:
                if a == '+':
                    A = stack.pop()
                    B = stack.pop()
                    stack.append(B + A)
                elif a == '-':
                    A = stack.pop()
                    B = stack.pop()
                    stack.append(B - A)
                elif a == '*':
                    A = stack.pop()
                    B = stack.pop()
                    stack.append(B * A)
                elif a == '/':
                    A = stack.pop()
                    B = stack.pop()
                    stack.append(B / A)
                elif a == '.' and len(stack) == 1:
                    A = int(stack.pop())
                else:
                    A = 'error'
            except:
                A = 'error'
                break
    print(f'#{test_case} {A}')
