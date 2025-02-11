# Жадібні алгоритми та динамічне програмування

## Завдання 1

### Оптимізація черги 3D-принтера в університетській лабораторії.

Розробіть програму для оптимізації черги завдань 3D-друку з урахуванням пріоритетів та технічних обмежень принтера, використовуючи жадібний алгоритм.

**Опис завдання**

1. Використовуйте вхідні дані у вигляді списку завдань на друк, де кожне завдання містить: ID, об'єм моделі, пріоритет та час друку.

2. Реалізуйте основну функцію optimize_printing, яка буде:
   - Враховувати пріоритети завдань.
   - Групувати моделі для одночасного друку.
   - Перевіряти обмеження об'єму та кількості.
   - Розраховувати загальний час друку.
   - Повертати оптимальний порядок друку.

3. Виведіть оптимальний порядок друку та загальний час виконання всіх завдань.

**Пріоритети завдань:**

- 1 (найвищий) - Курсові/дипломні роботи
- 2 - Лабораторні роботи
- 3 (найнижчий) - Особисті проєкти

## Завдання 2

### Оптимальне розрізання стрижня для максимального прибутку (Rod Cutting Problem)

Розробіть програму для знаходження оптимального способу розрізання стрижня, щоб отримати максимальний прибуток.
Необхідно реалізувати два підходи: через рекурсію з мемоізацією та через табуляцію.

**Опис завдання**

1. На вхід подається довжина стрижня та масив цін, де `price[i]` — це ціна стрижня довжини `i+1`.

2. Потрібно визначити, як розрізати стрижень, щоб отримати максимальний прибуток.

3. Реалізувати обидва підходи динамічного програмування.

4. Вивести оптимальний спосіб розрізання та максимальний прибуток.
