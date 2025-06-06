[Вернуться][main]

---

# Почему RPC и Protocol Buffers?

Окей, почему же следует использовать этот формальный синтаксис для определения вашего API? Если вам нужно отправить
запрос от одного микросервиса к другому, разве вы не можете просто совершить HTTP-запрос и получить JSON-ответ? Ну, это
возможно, но использование Protocol Buffers имеет свои преимущества.

## Документация

Первое преимущество использования Protocol Buffers заключается в том, что они предоставляют вашему API чётко
определённую и самодокументированную схему. Если вы используете JSON, то вам необходимо документировать поля и их типы.
Как и в случае с любой документацией, вы рискуете столкнуться с неточностями, неполнотой или устареванием документации.

Когда вы пишете ваш API на языке Protocol Buffers, вы можете генерировать код Python из него. Ваш код никогда не
будет несоответствовать документации. Документация хороша, но самодокументируемый код лучше.

## Валидация

Второе преимущество заключается в том, что когда вы генерируете код Python из Protocol Buffers, вы бесплатно
получаете некоторую базовую валидацию. Например, сгенерированный код не примет поля неверного типа.
Кроме того, в сгенерированный код встроены все шаблоны RPC.

Если вы используете HTTP и JSON для вашего API, тогда вам необходимо написать код, который строит запрос, отправляет
его, ждет ответа, проверяет код состояния, а затем анализирует и валидирует ответ. С Protocol Buffers, вы можете
генерировать код, который выглядит как обычный вызов функции, но под капотом делает сетевой запрос.

## Производительность

Фреймворк gRPC, как правило, более эффективен, чем использование типичных HTTP-запросов. gRPC построен на основе HTTP/2,
который может выполнять несколько запросов параллельно на долгоживущем соединении безопасно для потока. Настройка
соединения относительно медленная, так что её однократное выполнение и использование соединения для множества запросов
экономит время. Сообщения gRPC также бинарные и меньше по размеру, чем JSON. Более того, HTTP/2 имеет встроенное сжатие
заголовков.

## Дружелюбность к Разработчику

Возможно, самая интересная причина, по которой многие люди предпочитают gRPC REST, заключается в том, что вы можете
определить ваш API в терминах функций, а не HTTP-глаголов и ресурсов. Как инженер, вы привыкли думать в терминах вызовов
функций, и именно так выглядят API на gRPC.

## Вывод:

- **Protocol Buffers** предоставляют чётко определённую и самодокументированную схему для API, отличаясь от JSON
  более строгим схематизмом и компактностью при передаче по сети.
- **gRPC** обладает высокой производительностью благодаря использованию HTTP/2, поддержке бинарной передачи данных,
  сжатия заголовков и возможности параллельных запросов.
- Основное преимущество gRPC в его **дружелюбности к разработчику**: API определяется в терминах функций, что делает его
  более интуитивно понятным и лёгким в использовании по сравнению с REST.

---

[Вернуться][main]


[main]: ../../README.md "содержание"

