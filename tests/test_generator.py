from generator.password_generator import generator_password, has_lowercase, has_uppercase, has_number, has_symbol

def test_password_length(): # Esta función de prueba verifica que la longitud de la contraseña generada sea igual a la longitud especificada. Se llama a la función generator_password con una longitud de 12 y se comprueba que la longitud de la contraseña generada sea efectivamente 12.
    password = generator_password(12)
    assert len(password) == 12

def test_password_is_string():
    password = generator_password(12)
    assert isinstance(password, str)

def test_has_lowercase():
    assert has_lowercase("abc") is True

def test_has_uppercase():
    assert has_uppercase("ABC") is True

def test_has_number():
    assert has_number("abc1") is True

def test_has_symbol():
    assert has_symbol("abc!") is True 

def test_generator_password_length_range():
    for length in range(12,20):
        password = generator_password(length)
        assert len(password) == length

print("All tests passed successfully!")