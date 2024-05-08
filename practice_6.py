import logging

logging.basicConfig(
    filename="logs.log",
    format="%(asctime)s | %(levelname)s | %(message)s",
    level=logging.ERROR,
)


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        raise ValueError("Нельзя делить на ноль")
    return x / y


def evaluate_expression(expr):

    expr = expr.strip().split()
    if len(expr) != 3:
        logging.error(
            f"Line #{expr[0]}: Неверное количество операндов и операторов: {expr}"
        )
        return None
    try:
        x = float(expr[0])
        operator = expr[1]
        y = float(expr[2])

        if operator == "+":
            result = add(x, y)
        elif operator == "-":
            result = subtract(x, y)
        elif operator == "*":
            result = multiply(x, y)
        elif operator == "/":
            result = divide(x, y)
        else:
            logging.error(f"Line #{expr[0]}: Недопустимый оператор: {operator}")
            return None

        return result

    except ValueError as e:
        logging.error(
            f"Line #{expr[0]}: Не удалось преобразовать строку в число: {str(e)}"
        )
        return None
    except ZeroDivisionError:
        logging.error(f"Line #{expr[0]}: Деление на ноль недопустимо")
        return None


def main():
    try:
        with open("exprs.txt", "r") as file:
            lines = file.readlines()

        with open("results.txt", "w") as result_file:
            for i, line in enumerate(lines, start=1):
                expr_result = evaluate_expression(line)
                if expr_result is not None:
                    result_file.write(f"{i} {expr_result}\n")

    except FileNotFoundError:
        logging.error("Файл с выражениями не найден")


if __name__ == "__main__":
    main()
