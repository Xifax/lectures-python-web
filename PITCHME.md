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

---

### Что такое веб приложение

- Компоненты веба
- Какая-нибудь симпатичная схема
- Встроенные модули питона

---

### Симпатичная (наверное) схема

![Simple Diagramm](example.png)

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

или

> python -m SimpleHTTPServer 8000
