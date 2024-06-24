import logging
import logging.config
from pathlib import Path

log_folder = Path(__file__).parent
log_file = log_folder / 'example.log'

# Створення логера
logger = logging.getLogger(__name__)

# Налаштування рівня логування
logger.setLevel(logging.DEBUG)

# Створення обробника для виводу в stdout (консоль)
console_handler = logging.StreamHandler()

# Створення обробника для запису в файл
file_handler = logging.FileHandler(log_file, encoding="utf8")

# Налаштування рівня логування для обробників
console_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.DEBUG)

# Створення форматера для обробників
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(lineno)d - %(message)s')

# Налаштування форматера для обробників
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Додавання обробників до логера
logger.addHandler(console_handler)
logger.addHandler(file_handler)
