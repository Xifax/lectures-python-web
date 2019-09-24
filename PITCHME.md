# VCS

@fa[code-fork fa-3x git-color]

Версионирование кода & **git**

---?image=img/0-vcs.png&size=auto 90%

---

## Содержание

@ul

- Системы контроля версий
- git
- CLI и сценарии использования
- Коммиты и практики
- Branching models 
- git hooks
- git UI & tools

@ulend

Note:

...

---

## Версионирование кода

Три поколения VCS

Тенденция в сторону всё большего распараллеливания и распределённости

Note:

...

---

### Первое: SCCS, RCS

*Операции*: над одним файлом
*Параллелизм*: file locks
*Распределённость*: нет

Один человек - один файл

Note:

Source Code Control System
Revision Control System

---

### Второе: CVS, SVN

*Операции*: над множеством файлов
*Параллелизм*: merge -> commit
*Распределённость*: централизованное хранилище

Мёрджим текущую ревизию с новым обновлением, прежде чем закоммитить изменения

Note:

Concurrent Versions Control
Subversion

---

### Третье: Git, Mercurial

*Операции*: набор изменений
*Параллелизм*: commit -> merge
*Распределённость*: имеет место быть

Distributed VCS: мёрдж и коммит разделены

---

## @fa[git fa-2x]


@box[text-blue fragment](/ˈgɪt/ noun: a foolish or worthless person)

@box[git-color fragment](GIT(1): the stupid content tracker)

<!-- Linus -->

---?image=img/linus.jpg&size=auto 90%

### Особенности

@ul

- множество параллельных веток
- распределённость
- производительность
- работа с большими проектами

@ulend

---

### Концепции

@ul

- репозиторий
- ветка
- коммит, hash/SHA
- index/staging area
- игнорируемые файлы
- remotes
- rebase/merge

@ulend

---

### Commit

@ul
При каждом коммите формируется *SHA* файлов и директорий, определяющий *состояние* репозитория

*Хэш* является *идентификатором* коммита для множества операций

*HEAD* указывает на какой SHA мы смотрим в данный момент

*Branch* можно считать *именем* совокупности SHA

*Detached HEAD* ~ мы смотрим на SHA *не связанный с какой-либо веткой*
@ulend

---

### Index

Позволяет "заморозить" текущий статус рабочего дерева файлов
Таким образом, для одного файла, в нашем препозитории в один момент могут находиться:

@ul

- последняя версия из репозитория
- файл с последними изменениями
- "замороженный" файл с другими изменениями 

@ulend

Note: 

- промежуточная стадия 
- удобно для стэйджинга частей файла
- при работе с большими мёрджами

---

### Remotes

Распределённость!

@ul
- clone
- add
- fetch
- pull
- push
@ulend


---

### Merge/rebase

---

### Workflow



---

##  Git CLI

Сценарии и общепринятые варианты их разрешения через команды


<!-- ---?image=img/push-force.png&size=contain -->
![PUSH](img/push-force.png)


### Workflow (one more time)


---

## Коммиты и практики


![XKCD example](img/xkcd-commit-messages.png)

---

## Branching models

Git-flow, trunk-based, lightweight models

---

## Git hooks

Методы конфигурации, примеры

---

##  Git UI

PyCharm, VisualCode, Fork, Sourcetree

---

## Ссылки

Данная презентация
https://gitpitch.com/xifax/lectures-python-web/git-lecture

Репозиторий презентации
https://github.com/xifax/lectures-python-web/tree/git-lecture

Репозиторий содержит примеры кода, картинки, тексты и "заметки на полях".
