
def total_salary(path):
    try:
        with open(path, encoding="utf-8") as file:
            salaries = []
            for line in file:
                    _, salary = line.strip().split(",")
                    salaries.append(int(salary))

        average = total / len(salaries)
        return total, average
   
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return 0, 0


path = "1_salaries.txt"
total, average = total_salary(path)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
