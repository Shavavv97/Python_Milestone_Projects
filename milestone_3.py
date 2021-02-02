from math import sqrt, sin, cos, tan, log
from random import randint
from datetime import time
from sys import exit

choices = ('1', '2', '3', '4', '5')
print('What do you want to do?')
choice = input('1.Get the Fibonacci Secuence\n2.Coin Flip Simulator\n3.Calculator\n4.Patient / Doctor Scheduler\n5.Exit\n')

while choice not in choices:
    print('Sorry that is not a choice')
    choice = input('1.Get the Fibonacci Secuence\n2.Coin Flip Simulator\n3.Calculator\n4.Patient / Doctor Scheduler\n5.Exit\n')


if choice == '1':
# Fibonacci Sequence

    while True:
        try:
            counter = int(input('How many numbers from the Fibonacci Sequence you want to see? '))
        except ValueError:
            print('That is not a number')
            continue
        if counter < 0:
            print('The number has to be a positive number')
            continue
        else:
            break

    def fibonacci_sequence(num):
        a, b = 0, 1
        for i in range(num):
            print(a)
            a, b = b, a + b

    print(fibonacci_sequence(counter))

elif choice == '2':
# Coin Flip Simulator

    heads = 0
    tails = 0

    while True:
        try:
            flips = int(input('How many times you are going to flip the coin? '))
        except ValueError:
            print('That is not a number')
            continue
        if flips < 0:
            print('The number has to be a positive number')
            continue
        else:
            break

    for i in range(flips):
        result = randint(0, 1)
        if result == 0:
            print(str(i + 1) + '.- Heads')
            heads += 1
        else:
            print(str(i + 1) + '.-Tails')
            tails += 1

    print('\nResults: ')
    print('\tHeads:', heads, 'times')
    print('\tTails:', tails, 'times')

elif choice == '3':
# Calculator

    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        return x / y

    def power(x, y):
        return x ** y

    def square_root(x):
        return sqrt(x)

    def trigonometric_fun(x):
        print('\n', f'Sine of {x}:', sin(x), '\n', f'Cosine of {x}:', cos(x), '\n', f'Tangent of {x}:', tan(x), '\n')
        print(f'Inverted sine of {x}:', (sin(x) ** -1),'\n', f'Inverted cosine of {x}:', (cos(x) ** -1), '\n', f'Inverted tangent of {x}:', (tan(x) ** -1), '\n')

    def logarithm(x, y):
        return log(x, y)

    options = ('1', '2', '3', '4', '5', '6', '7', '8')
    choice = input('Select operation.\n 1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Square\6.Squere root\n7.Trigonometric functions\n8.Logarithm\n')

    while choice not in options:
        print('That is not a valid option')
        choice = input('Select operation.\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Square\n6.Squere root\n7.Trigonometric functions\n8.Logarithm\n')

    while True:

        if choice in ('1', '2', '3', '4', '5', '8'):

            while True:
                try:
                    num1 = float(input('Enter first number: '))
                    num2 = float(input('Enter second number: '))
                except ValueError:
                    print('Both have to be integers or floating numbers')
                    continue
                break

            if choice == '1':
                print(num1, '+', num2, '=', add(num1, num2))

            elif choice == '2':
                print(num1, '-', num2, '=', subtract(num1, num2))

            elif choice == '3':
                print(num1, '*', num2, '=', multiply(num1, num2))

            elif choice == '4':
                print(num1, '/', num2, '=', divide(num1, num2))
            
            elif choice == '5':
                print(num1, '**', num2, '=', power(num1, num2))

            elif choice == '8':
                print('The logarith of', num1, 'with base', num2, '=', logarithm(num1, num2))
            break

        elif choice in ('6', '7'):

            while True:
                try:
                    num = float(input('Enter first number: '))
                except ValueError:
                    print('Have to be an integer or floating number')
                    continue
                break

            if choice == '6':
                print('The square root of', num, '=', square_root(num))
            elif choice == '7':
                print('The trigonometric functions of', num, 'are:', trigonometric_fun(num))

        else:
            print('Invalid Input')

elif choice == '4':
# Patient / Doctor Scheduler

    class Doctor:
        patients = []

        def __init__(self, name, speciality, calendar):
            self.name = name
            self.speciality = speciality
            self.calendar = calendar

        def add_patient(self, patient):
            self.patients.append(patient)

        def show_details(self):
            details = 'Doctor: ' + self.name + '\nSpeciality: ' + self.speciality + '\n\nPatients:'
            for patient in self.patients:
                details += '\n' + patient.name + ' ' + patient.sickness
            details += '\n' + self.calendar.show_calendar()
            return details


    class Patient:

        def __init__(self, name, sickness):
            self.name = name
            self.sickness = sickness

        def show_details(self):
            return 'Name: ' + self.name + '\n' + 'Sickness: ' + self.sickness


    class DailyCalendar:
        hours = {}
        appointments = []

        def __init__(self):
            for hour in range(8, 17):
                self.hours[time(hour).strftime('%H:%M')] = time(hour).strftime('%H:%M')
                self.hours[time(hour, 30).strftime('%H:%M')] = time(hour, 30).strftime('%H:%M')
                print(hour)

        def show_calendar(self):
            details = '\nToday appointments:'
            for appointment in self.appointments:
                details += '\n' + appointment['Hour'] + ' with ' + appointment['Patient']
            return details


    def schedule(patient, doctor, hour, calendar):
        if hour in calendar.hours:
            calendar.appointments.append({'Patient': patient.name, 'Doctor': doctor.name, 'Hour': hour})
            del calendar.hours[hour]

            if patient not in doctor.patients:
                doctor.add_patient(patient)
        else:
            print('That hour is unavailable.')


    patient_1 = Patient('John Doe', 'Cold')
    patient_2 = Patient('Salvador Vidal', 'Sore throat')
    calendar = DailyCalendar()
    doctor = Doctor('Fausto Zaruma', 'General', calendar)

    schedule(patient_1, doctor, '09:30', calendar)
    schedule(patient_1, doctor, '10:30', calendar)
    schedule(patient_2, doctor, '15:30', calendar)
    schedule(patient_2, doctor, '16:30', calendar)

    print(doctor.show_details())

elif  choice == '5':
    exit()