import logging
from pathlib import Path

log_folder = Path(__file__).parent
log_file = log_folder / 'example.log'
# # Налаштування конфігурації логування
# logging.basicConfig(
#     filename=log_file,
#     format='%(asctime)s - %(levelname)s - %(message)s',
#     encoding="utf8")
# Створення логера
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
#Додавання обробника для виводу в консоль
console_handler = logging.StreamHandler()
# Створення обробника для запису в файл
file_handler = logging.FileHandler(log_file, encoding="utf8")

# Створення форматера для обробників
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# Налаштування форматера для обробників
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

console_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.DEBUG)
logger.addHandler(console_handler)
logger.addHandler(file_handler)
# logging.getLogger('').addHandler(console_handler)
# Логування подій різного рівня (DEBUG, INFO, WARNING, ERROR, CRITICAL)

# logger.debug('Це повідомлення рівня DEBUG')
# logger.info('Це повідомлення рівня INFO')
# logger.warning('Це повідомлення рівня WARNING')
# logger.error('Це повідомлення рівня ERROR')
# logger.critical('Це повідомлення рівня CRITICAL')

def divide(x, y):

    assert x > 0, f"x=={x}, але повинно бути додатнім числом"

    try:
        result = x / y
    except ZeroDivisionError as e:
        logger.error('Attempted to divide by zero')
        raise e
    else:
        logger.info(f'{x} divided by {y} is {result}')
        return result
    finally:
        logger.debug('Its message of level DEBUG')
        logger.info('Its message of level INFO')
        logger.warning('Its message of level WARNING')
        logger.error('Its message of level ERROR')
        logger.critical('Its message of level CRITICAL')

if __name__ == "__main__":
    p = divide(1, 2)
    print(p)
    p2 = divide(1, 0)
    print(p2)
