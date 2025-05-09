from cryptography.fernet import Fernet
import hashlib
import hmac

# Generar y guardar una clave para cifrado
def generar_clave():
    clave = Fernet.generate_key()
    with open("clave.key", "wb") as archivo_clave:
        archivo_clave.write(clave)
    print("Clave generada y guardada en 'clave.key'.")

# Cargar la clave para cifrado
def cargar_clave():
    with open("clave.key", "rb") as archivo_clave:
        return archivo_clave.read()

# Cifrado y descifrado de datos
def cifrar_datos(mensaje):
    clave = cargar_clave()
    fernet = Fernet(clave)
    mensaje_cifrado = fernet.encrypt(mensaje.encode())
    return mensaje_cifrado

def descifrar_datos(mensaje_cifrado):
    clave = cargar_clave()
    fernet = Fernet(clave)
    mensaje_descifrado = fernet.decrypt(mensaje_cifrado).decode()
    return mensaje_descifrado

# Hashing de contraseñas
def hash_contraseña(contraseña):
    return hashlib.sha256(contraseña.encode()).hexdigest()

# Prevención de ataques con HMAC
def verificar_integridad(mensaje, clave_secreta):
    firma = hmac.new(clave_secreta.encode(), mensaje.encode(), hashlib.sha256).hexdigest()
    return firma

if __name__ == "__main__":
    # Generar clave para cifrado
    generar_clave()

    # Cifrado y descifrado
    mensaje = "Este es un mensaje secreto."
    mensaje_cifrado = cifrar_datos(mensaje)
    print(f"Mensaje cifrado: {mensaje_cifrado}")
    mensaje_descifrado = descifrar_datos(mensaje_cifrado)
    print(f"Mensaje descifrado: {mensaje_descifrado}")

    # Hashing de contraseñas
    contraseña = "mi_contraseña_segura"
    hash_resultado = hash_contraseña(contraseña)
    print(f"Hash de la contraseña: {hash_resultado}")

    # Prevención de ataques con HMAC
    mensaje = "Datos importantes"
    clave_secreta = "clave_secreta"
    firma = verificar_integridad(mensaje, clave_secreta)
    print(f"Firma HMAC del mensaje: {firma}")