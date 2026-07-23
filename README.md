```markdown
# Micql — минималистичный язык запросов

Micql (произносится "май-кью-эл") — язык запросов, который в 3-5 раз короче SQL.  
Работает с JSON, не требует сервера, запускается в Termux, Linux, macOS и Windows.

---

## Быстрый старт

Установка:
```bash
pip install git+https://github.com/rostichar1-hue/Micql.git
```

Базовый пример

```mc
CREATE users (id INT, name STRING, age INT)
+users {1, "Alex", 28}
+users {2, "Kate", 22}
users:name(age>20)10
SAVE
```

Запуск:

```bash
micro data.mc
```

Вывод:

```
+--------+
| name   |
+--------+
| Alex   |
| Kate   |
+--------+
```

---

Синтаксис

```mc
CREATE table (field1 TYPE, field2 TYPE)
+table {value1, value2, value3}
table:field1,field2(condition)limit
SAVE
LOAD
```

---

Установка

```bash
git clone https://github.com/rostichar1-hue/Micql.git
cd Micql

```

---

Автор

rostichar1-hue (Telegram: @darzx3)

Лицензия

MIT

```
