def password_generator():
    import string
    import random

    while True:
        password_length = int(input("Introduce la longitud deseada de la contraseña (mínimo 8): "))
        use_special = input("¿Incluir caracteres especiales? (s/n): ").strip().lower() == 's'
        
        if password_length < 8:
            print("La longitud mínima de la contraseña debe ser 8.")
        else:
            break
    
    characters = string.ascii_letters + string.digits
    if use_special:
        characters += string.punctuation
        
    password = ''
    for i in range(password_length):
        password += random.choice(characters)

    print(f"Contraseña generada: {password}")

