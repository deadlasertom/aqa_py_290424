"""
https://petstore.swagger.io/

Опис: Swagger Petstore - це відкрите API, яке надає можливість управляти даними про домашніх тварин. За допомогою цього API можна додавати нових тварин, знаходити тварин за ідентифікатором, виконувати замовлення на тварин та багато іншого.

Вам потрібно реалізувати програму, яка взаємодіє з Swagger Petstore API, використовуючи HTTP запити. Основні методи запитів, які вам знадобляться: GET, POST, PUT, DELETE.

**Ваші завдання:**

1. Отримати список доступних тварин (метод GET).

1. Зробіть запит до /pet/findByStatus з параметром status, щоб отримати список усіх тварин.

    1. Обробіть відповідь сервера та виведіть список тварин на екран.

1. Додати нову тварину (метод POST).

    Створіть новий об'єкт тварини з необхідною інформацією, наприклад, ім'я та статус.

    Зробіть запит до /pet з об'єктом тварини в тілі запиту, щоб додати нову тварину.

    Обробіть відповідь сервера та виведіть підтвердження про додавання тварини на екран.

1. Знайти тварину за ідентифікатором (метод GET).

    1. Введіть ідентифікатор тварини, яку потрібно знайти.

    1. Зробіть запит до /pet/{petId}, де {petId} - ідентифікатор шуканої тварини.

    1. Обробіть відповідь сервера та виведіть інформацію про знайдену тварину на екран.

1. Видалити тварину за ідентифікатором (метод DELETE).

    1. Введіть ідентифікатор тварини, яку потрібно видалити.

    1. Зробіть запит до /pet/{petId}, де {petId} - ідентифікатор тварини, яку потрібно видалити.

    1. Обробіть відпові
"""