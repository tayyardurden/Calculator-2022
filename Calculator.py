logo = """
 _____________________
|  _________________  |
| | Tayyaristan   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

#Toplama
def add(n1, n2):
  return n1+n2

#Çıkarma
def substract(n1, n2):
  return n1-n2

#Çarpma
def multiply(n1, n2):
  return n1*n2

#Bölme
def divide(n1, n2):
  return n1/2

operations = {
  "+" : add,
  "-" : substract,
  "*" : multiply,
  "/" : divide
}

def calculator():
  print(logo)
  num1 = float(input("Lütfen bir sayı gir: "))
  for symbol in operations:
    print(symbol)
  should_continue = True

  while should_continue:
    operation_symbol = input("Yukarıdaki sembollerden birini seç lütfen: ")
    num2 = float(input("Lütfen ikinci bir sayı gir?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input("Devam etmek için 'y', yeni hesaplama için 'n' yazın: ") == "y":
      num1 = answer
    else:
      should_continue = False
      calculator()

calculator()
