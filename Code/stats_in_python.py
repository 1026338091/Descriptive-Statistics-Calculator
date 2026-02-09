"""method: python3 stats_in_python.py <filename><column_number>"""
import sys
import math

def main():
    """
       Calculate statistics for a given list, such as mean, variance, standard deviation, and median

       parameters：
       datas : datas after calculation
       number (list): total datas
       column_to_parse (int): Users order column number
    """
    filename = sys.argv[1]

    numbers = []
    count = 0

    try:
        column_to_parse = int(sys.argv[2])
    except ValueError:
        print("Error:please enter integer column index")
        sys.exit(1)
    try:
        with open (filename, 'r', encoding='utf-8') as in_file:
            for line_number , line  in enumerate(in_file, start=1):
                count += 1
                column = line.strip().split("\t")

                try:
                    value = column[column_to_parse]
                    num = float(value)
                    if not math.isnan(num):
                        numbers.append(num)
                except IndexError:
                    print(f"There is no valid 'list index' in column {column_to_parse} "
                          f"in line {line_number} in file {filename}")
                    sys.exit(1)
                except ValueError:
                    print(f"skipping line number：{line_number} "
                          f"can't convert string to float：{value}")
                    continue
    except FileNotFoundError:
        print(f"Erorr: The file '{filename}' not found")
        sys.exit(1)
    if len(numbers) == 0:
        print(f"There were no valid number(s) in column{column_to_parse} in file{filename}")
        sys.exit(1)

    datas = calculate(numbers)

    if datas:
        print_calculation(datas, count, column_to_parse )

def calculate(numbers):
    """
           Calculate statistics for a given list, such as mean, variance,
           standard deviation, and median

           parameters：
           datas: datas after calculation
           number (list): total datas
           column_to_parse (int): Users order column number

           return：
           dic：  Number of valid values, Average,Maximum , Minimum, value, Variance,
           Standard deviation (Std Dev), Median
    """
    n = len(numbers)
    if n == 0:
        return None

    average = sum(numbers) / n

    if n > 1:
        variance = sum((x - average) ** 2 for x in numbers) / ( n - 1 )
        standard_deviation = math.sqrt(variance)
    else:
        variance = 0
        standard_deviation = 0

    if n % 2 ==0 :
        median = (numbers[n // 2]) + (numbers[n // 2 - 1])
    else:
        median = numbers[n // 2]
    return {
        "Count": n,
        "ValidNum": n,
        "Average": average,
        "Maximum": max(numbers),
        "Minimum": min(numbers),
        "Variance": variance,
        "Std Dev": standard_deviation,
        "Median": median
    }

def print_calculation(datas, count, column_to_parse):
    """
        print the statistical result after calculation： Number of valid values,
        Average,Maximum , Minimum, value,
        Variance , Standard deviation (Std Dev), Median
    """
    print(f"\n    Column: {column_to_parse}")
    print(f"        Count     =   {count:.3f}")
    print(f"        ValidNum  =   {datas['ValidNum']:.3f}")
    print(f"        Average   =   {datas['Average']:.3f}")
    print(f"        Maximum   =   {datas['Maximum']:.3f}")
    print(f"        Minimum   =   {datas['Minimum']:.3f}")
    print(f"        Variance  =   {datas['Variance']:.3f}")
    print(f"        Std Dev   =   {datas['Std Dev']:.3f}")
    print(f"        Median    =   {datas['Median']:.3f}")

if __name__ == "__main__" :
    main()
