 #employee data

class Keyboard:
    @staticmethod
    def input_string(prompt):
        return input(prompt)

    @staticmethod
    def input_integer(prompt):
        return int(input(prompt))

    @staticmethod
    def input_real(prompt):
        return float(input(prompt))

    @staticmethod
    def input_boolean(prompt):
        answer = input(prompt).strip().lower()
        return answer in ("y", "yes", "t", "true")


keyboard = Keyboard()

first_name = keyboard.input_string("Enter name: ")

last_name = keyboard.input_string("Enter surname: ")

age = keyboard.input_integer("Enter age: ")

salary = keyboard.input_real("Enter salary: ")

is_salary_hidden = keyboard.input_boolean("Hide salary? (y/n): ")

print("DATA RECORD")
print("===========")
print("Name:", first_name, last_name)
print("Age:", age)

if not is_salary_hidden:

    print("Salary:", salary)