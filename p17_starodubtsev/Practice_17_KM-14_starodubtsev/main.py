import factorial.factorial
import logarithm.logarithm
import exp_root


def check(n, type):
    try:
        n = type(n)
        return True
    except ValueError:
        return False


def main():

    print("Виберіть функцію, яка буде виконуватись")
    print("1 Знайти х в квадраті")
    print("2 х в третій степені")
    print("3 Корінь х")
    print("4 Корінь третьої степені")
    print("5 Факторіал х")
    print("6 log")
    print("7 ln")
    print("8 lg10")
    q=True
    while(q):
        num = input(
            "Ваше число: ")
        if num == '1':
            n = input("Введіть x: ")
            if check(n, float):
                print("Відповіть  ", round(exp_root.exponentiation.exp2(float(n)), 4))
            else:
                print("Неправильно ввели число")
        elif num == '2':
            n = input("Введіть x: ")
            if check(n, float):
                print("Відповіть  ", round(exp_root.exponentiation.exp3(float(n)), 4))
            else:
                print("Неправильно ввели число")
        elif num == '3':
            n = input("Введіть x: ")
            if check(n, float) and float(n) >= 0:
                print("Відповіть ", round(exp_root.root.root2(float(n)), 4))
            else:
                print("Неправильно ввели число")
        elif num == '4':
            n = input("Введіть x: ")
            if check(n, float):
                print("∛x = ", round(exp_root.root.root3(float(n)), 4))
            else:
                print("Неправильно ввели число")
        elif num == '5':
            n = input("Please, input x: ")
            if check(n, int) and int(n) > 0:
                print("Відповіть ", factorial.factorial.fact(int(n)))
            else:
                print("Неправильно ввели число")
        elif num == '6':
            a = input("Введіть базу логарифму: ")
            b = input("Введіть x: ")
            if check(a, float) and check(b, float) and float(b) > 0 and float(a) > 0 and float(a) != 1:
                print("Відповіть  ", round(logarithm.logarithm.logf(float(b), float(a)), 4))
            else:
                print("Неправильно ввели число")
        elif num == '7':
            b = input("Введіть x: ")
            if check(b, float) and float(b) > 0:
                print("Відповіть  ", round(logarithm.logarithm.ln(float(b)), 4))
            else:
                print("Неправильно ввели число")
        elif num == '8':
            b = input("Введіть x: ")
            if check(b, float) and float(b) > 0:
                print("Відповіть  ", round(logarithm.logarithm.log10(float(b)), 4))
            else:
                print("Неправильно ввели число")
        else:
            print("Неправильний номер функції")
        y="e"
        y = input("Якщо хочете завершити, то введіть у ")

        if y=="y":
            q =False


if __name__ == '__main__':
    main()
