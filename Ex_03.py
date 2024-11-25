from inputs import input_int

def bank(a,years, percent):
    return a*(1+percent*0.01)**years

a = input_int("Введите сумму вклада: ")
years = input_int("Введите количество лет: ")
# percent = input_int("Введите процентную ставку: ")
percent = 10

print(round(bank(a,years,percent),2))
