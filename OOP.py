import math

class ComplexNumber:

    def __init__(self, real=0, imaginary=0):

        self.real = real

        self.imaginary = imaginary



    def __init_with_params__(self, real, imaginary):

        self.real = real

        self.imaginary = imaginary



    def __del__(self):

        print(f"Объект комплексного числа {self.real} + {self.imaginary}i уничтожен")



    def multiply_by_scalar(self, scalar):

        return ComplexNumber(self.real * scalar, self.imaginary * scalar)



    def calculate_argument(self):

        return math.degrees(math.atan2(self.imaginary, self.real))



    def __str__(self):

        return f"{self.real} + {self.imaginary}i"





if __name__ == "__main__":

    complex_number = ComplexNumber(3, 4)

    print("Создано комплексное число:", complex_number)



    scalar = 2

    multiplied = complex_number.multiply_by_scalar(scalar)

    print(f"Произведение на {scalar}:", multiplied)



    argument = complex_number.calculate_argument()

    print("Аргумент числа в градусах:", argument)



    real_part = float(input("Введите действительную часть: "))

    imaginary_part = float(input("Введите мнимую часть: "))

    user_complex_number = ComplexNumber(real_part, imaginary_part)

    print("Созданное число:", user_complex_number)



    user_scalar = float(input("Введите скаляр для умножения: "))

    user_multiplied = user_complex_number.multiply_by_scalar(user_scalar)

    print(f"Результат умножения на {user_scalar}:", user_multiplied)



    user_argument = user_complex_number.calculate_argument()

    print("Аргумент пользовательского числа в градусах:", user_argument)

