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
- git hooks, alias, configs
- git UI & tools
- прочее: tags, submodules, etc

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

**Операции**: над одним файлом

**Параллелизм**: file locks

**Распределённость**: нет

Один человек - один файл

Note:

Source Code Control System
Revision Control System

---

### Второе: CVS, SVN

**Операции**: над множеством файлов

**Параллелизм**: merge -> commit

**Распределённость**: централизованное хранилище

Мёрджим текущую ревизию с новым обновлением, прежде чем закоммитить изменения

Note:

Concurrent Versions Control
Subversion

---

### Третье: Git, Mercurial

**Операции**: набор изменений

**Параллелизм**: commit -> merge

**Распределённость**: имеет место быть

Distributed VCS: мёрдж и коммит разделены

---

## @fa[git fa-2x]


@box[text-blue fragment](/ˈgɪt/ noun: a foolish or worthless person)

@box[git-color fragment](GIT(1): the stupid content tracker)

<!-- Linus -->

---?image=img/linus.jpg&size=auto 90%

---

### Особенности

@ul

- множество параллельных веток
- распределённость
- производительность
- работа с большими проектами
- коммиты и файлы ~ объекты в базе git'а

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

@box[fragment](При каждом коммите формируется *SHA* файлов и директорий, определяющий *состояние* репозитория)

@box[fragment](*Хэш* является *идентификатором* коммита для множества операций)

@box[fragment](*HEAD* указывает на какой SHA мы смотрим в данный момент)

---

### Commit

@box[fragment](*Branch* это подвижный указатель на коммит/SHA)

@box[fragment](*Detached HEAD* ~ мы смотрим на SHA *не связанный с какой-либо веткой*)

@box[fragment](*Tag* ~ указывает на определённый коммит и содержит дополнительную информацию)

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

### Branches

Локальные и удалённые

```bash
$ tail .git/config
[branch "master"]
	remote = origin
	merge = refs/heads/master
```

`master` tracks the upstream `origin/master`

---

### Merge/rebase

@box[fragment](**merge** ~ попробует скомбинировать последние коммиты/SHA двух веток в один)
@box[fragment](**fast-forward merge** ~ если история коммитов без конфликтов, новые коммиты будут включены в неё а HEAD "перемотается*)
@box[fragment](**merge commit** ~ при разрешении конфликта создаётся новый коммит)
@box[fragment](**rebase** ~ в случае конфликта применит изменения *поверх* целевой ветки, без дополнительного коммита)
@box[fragment](**cherry-pick** ~ применяем конкретный коммит по SHA на текущую ветку)

---

### Remotes

> имя url:refspec (fetch/push)

@ul
- **clone** ~ сделать локальную копию и пометить как origin
- **add** ~ добавить удалённый источник
- **fetch** ~ скачать информацию о тегах и ветках
- **pull** ~ fetch + merge из удалённого источника 
- **push** ~ добавить локальные коммиты в удалённый источник
@ulend

---

### .gitignore

Возможно, самый главный файл в репозитории

Подборка шаблонов для разных целей

https://www.gitignore.io/

Желательно исключать артефакты/генерируемы файлы, личные настройки и пароли

Note:

- рассмотреть примеры
- игнорирование конкретных путей и файлов
- file globs

---

### Workflow

@ul
- `status`
- `pull`
- меняем/добавляем файлы
- `add` .
- `commit -m "Ясделаль"`
- `push target-remote new-branch`
@ulend

---

##  Git CLI

Сценарии и общепринятые варианты их разрешения через команды

GUI заменяет консоль, но иногда не заменяет консоль

---?image=img/push-force.png&size=auto 90%

---

### Различные ситуации

@ul
- локальный мусор, проба пера
- закоммитили что-то не то или не так
- история превратилась в хитросплетение всего и вся
- что-то не туда запушили
- надо скопировать с сохранением истории
- много разных пересекающихся репозиториев
- поиск по истории
@ulend

---

### Локальные изменения 

@box[fragment](

Откатим изменения файла или директории к последнему коммиту

> git checkout -- [path/to/reset]
)

@box[fragment](

Отбросим все текущие изменения

> git reset --hard
)

> git reset --hard HEAD^


### Сравним изменения из консоли

```bash
# Сравним локальную и удалённую ветки
git diff develop origin/master

# Сравним с тем, что было раньше
git diff master master~4

# Сравним конкретный файл
git diff HEAD HEAD^ -- README.md
```

---

### Модифицируем последний коммит

```bash
git add [files]
git commit --amend
```

---

### Модификация локальной истории

```
git checkoud test_branch

git log --oneline
3b86653 Update requirements
fcf4c2d Include new tests and example payload
...

git log --oneline develop
43ab021 Tweak id field for criteria and constraints
7df5d41 Debug models and schema

# Используем rebase, с текущей ветки на на develop
git rebase develop

git log --oneline
69f61e9 Update requirements
11a5589 Include new tests and example payload
43ab021 Tweak id field for criteria and constraints
7df5d41 Debug models and schema
```

Note:

A rebase operation is similar to a merge, but it can produce a much cleaner history.
When you rebase, Git will find the common ancestor between your current branch and the specified branch.
It will then take all of the changes after that common ancestor from your branch and “replay” them on top of the other branch.
The result will look like you did all of your changes after the other branch.

---

### Интерактивный rebase

Идея та же, что и раньше, но мы можем менять конечный результат

Продемонстрируем на простеньком репозитории

---

### Изменения затрагивающие других

Создадим новый коммит, откатывающий предыдущий

> git revert [SHA]

Обновим репозиторий для всех работающих с ним

> git push

---

### Отложим изменения

```bash
# сохраним текущие изменения
git stash save
# можем даже назвать stash и включить новые файлы
git stash save --include-untracked "for later"
# можем сделать pull для применения чужих правок
git pull
# восстановим по мере надобности
git stash apply
# посмотрим список всех stash'ей
git stash list
```

---

### Добавим ветку из другого репозитория

```bash
git remote add [branch] [URL]
git fetch [branch]
git checkout -b [new_branch] remote/[branch]
```

Или без добавления remote'а

```bash
git checkout --orphan [target/branch]
git reset --hard
git pull [URL] [branch]
```

---

### Применим изменения из другого репозитория 

```bash
git branch [new-merge-from-repo]
git checkout [new-merge-from-repo]
git remote add [repo-a] git@[repo-url]
git merge [repo-a]/[target-branch] --allow-unrelated-histories
```

---

### Workflow (one more time)

---

### Git CLI tools

@ul

- pre-commit: https://pre-commit.com/
- tig: https://jonas.github.io/tig/
- grv: https://github.com/rgburke/grv
- gg: https://github.com/qw3rtman/gg

@ulend

Note:

GUI in your CLI vs git alias alternative

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
