import re

text = """
Телефонний номер: (123) 456-7890
Тел: (044) 456-2390
Моб: (097) 456-7832
"""
pattern = r"\(\d{3}\) \d{3}-\d{4}"

match_ = re.search(pattern, text)
if match_:
    print(match_)
    phone_number = match_.group()
    print("Найдено номер телефону:", phone_number)

def is_valid_mail(mail_str:str) -> bool:
    """What can I do?"""
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(email_pattern, mail_str):
        return True
    else:
        return False

email = "user@domain.name"
print(is_valid_mail(email))
