import re

def is_valid_email(email: str) -> bool:
    # Регулярное выражение для проверки email-адреса
    email_regex = re.compile(
        r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    )
    return re.match(email_regex, email) is not None


print(is_valid_email("a@a.ru"))
print(is_valid_email("a@a.ff.fru "))
print(is_valid_email("aa.ru.ru"))
print(is_valid_email("@a.ru.ru"))

