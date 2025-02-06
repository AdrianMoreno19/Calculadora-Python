def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

def calculadora():
    print("Calculadora en Python")
    print("Operaciones disponibles: +, -, *, /")
    
    while True:
        op = input("Ingrese la operación (+, -, *, /) o 'salir' para terminar: ")
        if op.lower() == 'salir':
            print("Saliendo de la calculadora...")
            break
        
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            
            if op == '+':
                print("Resultado:", suma(num1, num2))
            elif op == '-':
                print("Resultado:", resta(num1, num2))
            elif op == '*':
                print("Resultado:", multiplicacion(num1, num2))
            elif op == '/':
                print("Resultado:", division(num1, num2))
            else:
                print("Operación no válida. Intente nuevamente.")
        except ValueError:
            print("Error: Entrada no válida. Ingrese números válidos.")
        
if __name__ == "__main__":
    calculadora()
