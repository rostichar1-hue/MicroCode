```markdown
# Micql — минималистичный язык запросов / Minimalistic Query Language

**Russian / Русский**

Micql (произносится "май-кью-эл") — язык запросов, который в 3-5 раз короче SQL.  
Работает с JSON, не требует сервера, запускается в Termux и Linux.
файлы MicQL имеют тип .mc

**English**

Micql (pronounced "my-queue-l") is a query language that is 3-5 times shorter than SQL.  
Works with JSON, no server required, runs on Termux and Linux.

---

## Синтаксис / Syntax

```

CREATE table (field1 TYPE, field2 TYPE)
+table {value1, value2, value3}
table:field1,field2(condition)limit
SAVE
LOAD

```

---

## Установка / Installation

```bash
git clone https://github.com/rostichar1-hue/Micql.git
cd Micql
./install.sh
source ~/.bashrc
```

---

Пример / Example

```bash
micro data.mc
```

---

Автор / Author

rostichar1-hue (Telegram: @darzx3)

Лицензия / License

MIT

```
