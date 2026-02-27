from calculator import sumar, restar, multiplicar, dividir

def pedir_numero(mensaje: str) -> float:
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada inválida. Escribe un número (ej: 10, 3.5).")

def menu() -> None:
    print("\n=== Calculadora en consola ===")
    print("1) Sumar")
    print("2) Restar")
    print("3) Multiplicar")
    print("4) Dividir")
    print("5) Salir")

def main() -> None:
    while True:
        menu()
        opcion = input("Elige una opción: ").strip()

        if opcion == "5":
            print("Bye!")
            break

        if opcion not in {"1", "2", "3", "4"}:
            print(" Opción no válida.")
            continue

        a = pedir_numero("Ingresa el primer número: ")
        b = pedir_numero("Ingresa el segundo número: ")

        try:
            if opcion == "1":
                res = sumar(a, b)
                op_txt = "suma"
            elif opcion == "2":
                res = restar(a, b)
                op_txt = "resta"
            elif opcion == "3":
                res = multiplicar(a, b)
                op_txt = "multiplicación"
            else:
                res = dividir(a, b)
                op_txt = "división"

            print(f"Resultado ({op_txt}): {res}")

        except ZeroDivisionError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()