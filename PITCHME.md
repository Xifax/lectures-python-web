# Web Python

Веб приложения на питоне и с чем их едят

---

## Предварительное содержание

@ul

- Что такое веб приложение
- Фреймворки
- Flask
- Django
- Развёртывание на сервере
- Микросервисы
- Практическое задание

@ulend

Note:

- Заострить внимание на применении и структуре приложений
- Добавить NOTA BENE после каждой темы

---

### Что такое веб приложение

- Компоненты веба
- Какая-нибудь симпатичная схема
- Встроенные модули питона

---

### Симпатичная (наверное) схема

![Simple Diagramm](img/example.svg)

---

### SimpleHTTPServer


```
import SimpleHTTPServer
import SocketServer

PORT = 8000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()
```
@[1-2, 3, 5-6, 9-10]


или

> python -m SimpleHTTPServer 8000
