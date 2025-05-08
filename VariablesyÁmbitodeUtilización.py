# Variable global
global_variable = "Soy una variable global"

def my_function():
    # Variable local
    local_variable = "Soy una variable local"
    print(local_variable)  # Accediendo a la variable local
    print(global_variable)  # Accediendo a la variable global desde dentro de la función

# Intentando acceder a la variable local fuera de su ámbito

def intentando():
    try:
        print(local_variable)  # Esto generará un error porque local_variable no es accesible aquí
    except NameError as e:
        print(f"Error: {e}")

    # Accediendo a la variable global fuera de la función
    print(global_variable)

if __name__ == "__main__":
    # Llamando a la función
    my_function()
    intentando()
    