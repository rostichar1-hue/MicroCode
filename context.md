```markdown
# Micql (MQ) — контекст проекта

Micql — минималистичный язык запросов. Альтернатива SQL для быстрых скриптов, работы с JSON и встраиваемых систем.

**Отличия от SQL:**
- Короче в 3-5 раз
- Хранит данные в JSON
- Не требует сервера БД
- Работает в Termux и Linux

**Автор:** rostichar1-hue  
**Telegram:** @darzx3

## Синтаксис

```

CREATE table (field1 TYPE, field2 TYPE)
+table {value1, value2, value3}
table:field1,field2(condition)limit
SAVE
LOAD

```

## Установка

```bash
git clone https://github.com/rostichar1-hue/Micql.git
cd Micql
./install.sh
source ~/.bashrc
```

Пример

```bash
micro data.mc
```

Ссылки

· Репозиторий: https://github.com/rostichar1-hue/Micql
· Лицензия: MIT

```
