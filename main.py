import sys #Esta es una librería que nos permite interactuar con el sistema operativo y acceder a funcionalidades del sistema, como la lectura de argumentos de línea de comandos, la manipulación de rutas de archivos, entre otras.   
from generator.password_generator import generator_password #Esta línea importa la función generate_password desde el módulo password_generator ubicado en el paquete generate. Esta función se utilizará para generar contraseñas según los parámetros proporcionados por el usuario.

def main(): #Esta es la función principal del programa. Se define como main() y se ejecutará cuando se llame a este script directamente.
    if len(sys.argv) < 2:
        print("Uso: python main.py <longitud>") #Esta línea verifica si el número de argumentos proporcionados en la línea de comandos es menor que 2. Si es así, significa que el usuario no ha proporcionado la longitud deseada para la contraseña, y se imprime un mensaje de uso adecuado para informar al usuario sobre cómo ejecutar correctamente el script.
        return

    try:
        length = int(sys.argv[1]) #Esta línea intenta convertir el primer argumento de línea de comandos (sys.argv[1]) en un número entero. Este argumento representa la longitud deseada para la contraseña generada.
    except ValueError:
        print("La longitud debe ser un número entero.") #Si la conversión a entero falla (por ejemplo, si el usuario proporciona un valor no numérico), se captura la excepción ValueError y se imprime un mensaje de error indicando que la longitud debe ser un número entero.
        return

    if length < 12:
        print("La longitud mínima de la contraseña es 12.") #Esta línea verifica si la longitud proporcionada es menor que 12. Si es así, se imprime un mensaje indicando que la longitud mínima de la contraseña debe ser 12.
        return

    password = generator_password(length) #Si todas las verificaciones anteriores pasan, se llama a la función generator_password con la longitud proporcionada para generar una contraseña aleatoria.

    print("Contraseña generada:", password) #Finalmente, se imprime la contraseña generada en la consola.

if __name__ == "__main__": #Esta línea verifica si el script se está ejecutando directamente (no importado como un módulo). Si es así, se llama a la función main() para iniciar la ejecución del programa.
    main()
