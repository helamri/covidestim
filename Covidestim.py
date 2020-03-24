from colorama import init, Fore, Back, Style
from os import system, name 
init(convert=True)
import tkinter as tk
import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Covid-19 Expectation")

def ProgramResult(inpu):
    if inpu==1:
        print('Calculate the number of confirmed patients after n days based on the number of confirmed patients over 2 days.\n')
        Conf0DayBef=input('Please enter the number of total confirmed persons on the current day.\n')
        Conf1DayBef=input('Please enter the number of total confirmed persons 1 day before the current day.\n')
        TargetDay=input('Please enter the number of the day (after current day) you would like to calculate the number of confirmed persons from the current day\n')
        print('=================================\n\n')
        root = tk.Tk()
        num = TwoDayFunction(Conf0DayBef, Conf1DayBef, TargetDay)
        root.destroy()
        create_window(root, num)
    elif inpu==2:
        print('Calculate the number of confirmed patients after n days based on the number of confirmed patients over 3 days.\n')
        Conf0DayBef=input('Please enter the number of total confirmed persons on the current day.\n')
        Conf1DayBef=input('Please enter the number of total confirmed persons 1 day before the current day.\n')
        Conf2DayBef=input('Please enter the number of total confirmed persons 2 days before the current day.\n')
        TargetDay=input('Please enter the number of the day (after current day) you would like to calculate the number of confirmed persons from the current day\n')
        print('=================================\n\n')
        root = tk.Tk()
        num = ThreeDayFunction(Conf0DayBef, Conf1DayBef, Conf2DayBef, TargetDay)
        root.destroy()
        create_window(root, num)
    elif inpu==3:
        print('Calculate the number of confirmed patients after n days based on the number of confirmed patients over 4 days.\n')
        Conf0DayBef=input('Please enter the number of total confirmed persons on the current day.\n')
        Conf1DayBef=input('Please enter the number of total confirmed persons 1 day before the current day.\n')
        Conf2DayBef=input('Please enter the number of total confirmed persons 2 days before the current day.\n')
        Conf3DayBef=input('Please enter the number of total confirmed persons 3 days before the current day.\n')
        TargetDay=input('Please enter the number of the day (after current day) you would like to calculate the number of confirmed persons from the current day\n')
        print('=================================\n\n')
        root = tk.Tk()
        num = FourDayFunction(Conf0DayBef, Conf1DayBef, Conf2DayBef, Conf3DayBef, TargetDay)
        root.destroy()
        create_window(root, num)
    elif inpu==4:
        qinput=input('Are you sure you want to exit the program?? (y/n)\n')
        return ProgramQuitting(qinput)
    else:
        print('Error: Please enter the correct option.\n\n')

def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 

def create_window(ro, num):
    tk.Label(text=num, foreground="red", font=("Calibri",80)).pack(padx=15, pady=15)

def TwoDayFunction(Conf0DayBef, Conf1DayBef, TargetDay):
    CommonRatio=int(Conf0DayBef) / int(Conf1DayBef)
    ConfirmedinTarday=int(Conf0DayBef)*CommonRatio**int(TargetDay)
    return int(ConfirmedinTarday)

def ThreeDayFunction(Conf0DayBef, Conf1DayBef, Conf2DayBef, TargetDay):
    CommonRatio_0_to_1=int(Conf0DayBef) / int(Conf1DayBef)
    CommonRatio_1_to_2=int(Conf1DayBef) / int(Conf2DayBef)
    RevisedCommonRatio=(CommonRatio_0_to_1 * CommonRatio_1_to_2) ** 0.5
    ConfirmedinTarday=int(Conf0DayBef)*RevisedCommonRatio**int(TargetDay)
    return int(ConfirmedinTarday)

def FourDayFunction(Conf0DayBef, Conf1DayBef,Conf2DayBef, Conf3DayBef, TargetDay):
    CommonRatio_0_to_1=int(Conf0DayBef) / int(Conf1DayBef)
    CommonRatio_1_to_2=int(Conf1DayBef) / int(Conf2DayBef)
    CommonRatio_2_to_3=int(Conf2DayBef) / int(Conf3DayBef)
    RevisedCommonRatio=(CommonRatio_0_to_1 * CommonRatio_1_to_2 * CommonRatio_2_to_3) ** (1/3)
    ConfirmedinTarday=int(Conf0DayBef)*RevisedCommonRatio**int(TargetDay)
    return int(ConfirmedinTarday)

def ProgramQuitting(qinpu):
    if str(qinpu)=="y":
        quit()
    elif str(qinpu)=="n":
        print('Program termination canceled. Restart the program.\n\n')
    else:
        print('Error: Please enter the correct option.\n\n')
        return ProgramResult(5)

print(Style.BRIGHT + Fore.GREEN +'Covidestim version 1.0.0')
print(Fore.GREEN +'Developed by'+ Fore.CYAN +' helamri'+ Fore.GREEN +', Mar 19 2020')
print(Fore.GREEN +'Program Description:\nThis program estimates the number of infected patients of COVID-19 on a targeted day, based on user input data.')
print(Fore.GREEN +'This program uses input values to calculate the expected number of confirmed patients for any date.\n')
print(Fore.RED + 'Note: This program only calculates simple calculations through the geometric sequence. Estimated figures are very different from the actual numbers.\nThe more data entered, the more accurate the prediction\n')

while True:
    print(Fore.WHITE +'Please enter the function number to be executed.')
    print('Function 1: Predict the number of confirmed patients with data of 1 day before the current day, for a total of 2 days')
    print('Function 2: Predict the number of confirmed patients with data of 2 days before the current day, for a total of 3 days')
    print('Function 3: Predict the number of confirmed patients with data of 3 days before the current day, for a total of 4 days')
    print('Type 4 to exit\n')
    inpu=(input('Function number: '))
    clear()
    print('=================================\n')
    ProgramResult(int(inpu))
