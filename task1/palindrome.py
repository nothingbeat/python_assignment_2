
def is_palindrome(s: str) -> bool:
    """
    Проверить, является ли строка палиндромом
    
    Args:
        s: Строка для проверки
        
    Returns:
        bool: Возвращает True, если палиндром, иначе False
    """
    # Очистка строки: перевод в нижний регистр и удаление не буквенно-цифровых символов
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

# Тестовый код
if __name__ == "__main__":
    test_strings = ["radar", "hello", "A man a plan a canal Panama", "12321"]
    for test in test_strings:
        result = is_palindrome(test)
        print(f"'{test}' -> {result}")
