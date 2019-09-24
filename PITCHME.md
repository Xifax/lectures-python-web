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

---

### Merge/rebase

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

```bash
# Откатим изменения файла или директории к последнему коммиту
git checkout -- [path/to/reset]

# Откатим git add
git reset

# Отбросим все текущие изменения в отслеживаемых файлах
git reset --hard

# Откатим последний коммит, но оставим модифицированные файлы как есть
git reset --soft HEAD^

# Уберём все неотслеживаемые файлы и директории
git clean -f -d

# Удалим конкретный файл, случайно добавленный ранее
git rm --cached [path/to/file]
```
---

### Сравним изменения из консоли

```bash
# Сравним локальную и удалённую ветки
git diff develop origin/master

# Сравним с тем, что было раньше
git diff master master~4

# Сравним конкретный файл с предыдущим коммитом
git diff HEAD HEAD^ -- README.md
```

---

### Модифицируем последний коммит

```bash
# Добавляем все изменения и коммитим
git commit -am "Include all required files"

# Добавим недостающие файлы
git add [files]

# Применим изменения
git commit --amend -m "Add forgotten file"
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

Продемонстрируем на простом репозитории

---

### Изменения затрагивающие других

Модифицировать коммит желательно только тогда, когда он существует локально, но не удалённо

Изменяя коммит уже запушенный в remote, можно сильно усложнить дальнейшие push/pull'ы, для себя и коллег

```bash
# Создадим новый коммит, откатывающий предыдущий

git revert [SHA]

# Обновим репозиторий для всех работающих с ним

git push [remote]

# Уберём merge commit
git rebase origin/[branch]

# Перепишем историю ДЛЯ ВСЕХ (не надо так T_T)
git rebase -i [SHA]
git push --force origin [branch]
```

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

### Поиск по истории

```bash
git log --oneline -S[query] --author [name]

git shortlog
```

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

### Практики

@ul

- Разделять коммит на краткое и подробное описание
- Отделять краткое описание пустой строкой
- Краткое описание желательно уложить в 50~70 символов
- Начать с большой буквы
- Не заканчивать краткое описание точкой
- Подробное описание должно быть не шире 80 символов
- В описании рассказать **что и почему**, а не **как**
- **Использовать императив**

@ulend

---

### Пример коммита

```bash
Демонстрирует пример практик описанных выше

Подробное описание, через пропуск строки, если необходимо. 
В английской практике удобно читать если описание 
задействует повелительное наклонение - отвечает на вопрос
"что делает/сделает этот коммит"?

К примеру:
- (if applied, this commit will) Fix pesky bug
- Update included dependencies
- Close the door and leave for lunch

Сам git в уведомлениях также использует подобный стиль:
> git merge
Merge branch 'develop'
> git revert
Revert "Add shiny JS libraries"

В случае наличии интеграции с чем-либо, можно также указать 
номера stories и issue. E.g., 

Resolve: #777

```

---

### Conventional commits

Альтернативный вариант

https://www.conventionalcommits.org

```bash
<type>[optional scope]: <description>

[optional body]

[optional footer]

e.g.

fix(configuration): allow reading empty configuration fields

see the issue for configuration example

fixes issue #777
```

---

### Squashing

```bash
# Используем отдельную ветку, на основе нашей текущей
git checkout -b squashed-feature
# Используем master, который не мёрджили в нашу отдельную ветку
git rebase -i master
# ...
pick # latest commit
squash # остальные коммиты
# Обновляем мастер
git checkout master
git merge squashed-feature
```

---

### Pull Request


---

## Branching models

Git-flow, trunk-based, lightweight models

### Git-flow

https://www.gitflow.com/

### Github-flow

...

### Trunk-based

https://trunkbaseddevelopment.com/

---

## Git hooks

Методы конфигурации, примеры

---

##  Git UI

@ul
- PyCharm
- VisualCode + GitLens
- Fork
- Sourcetree
- ...
@ulend

---

## Ссылки

Данная презентация
https://gitpitch.com/xifax/lectures-python-web/git-lecture

Репозиторий презентации
https://github.com/xifax/lectures-python-web/tree/git-lecture

Репозиторий содержит примеры кода, картинки, тексты и "заметки на полях".
