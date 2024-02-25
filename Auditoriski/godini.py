import datetime


def calculate_to_hundred(godini):
    year_born = datetime.date.today().year - godini
    return year_born + 100


print("Vnesete ime i godini:")
vnes = list(input().split(" "))
name = vnes[0]
age = int(vnes[1])
print(f"{name} ke ima 100 godini vo {calculate_to_hundred(age)}")
