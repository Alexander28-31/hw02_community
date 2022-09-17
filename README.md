## Проект спринта сообщества
## Описание проекта

- Создано и защищено приложение Posts

- Подключена база данных

- Десять последних записей помещенно на главную

В админ-зоне доступно управление объектами моделей Сообщение: можно публиковать новые записи или сильно/удалять тревогу. Пользователь может перейти на страницу любой сообщества, где отображаются последние публикации из этой группы.

## Модели (models.py)
### Post - запись
#### Поля:
- text(текст записи) - тип поля - Текст
- pub_date(дата публикации) - тип поля - Дата (автоматически создается текущая дата)
- автор(Автор) - тип поля - Ссылка на модель Пользователь (связь «один-ко-многим»)
- group(Сообщество) - тип поля - Ссылка на модель Group (связь «один-ко-многим»)

### Group - сообщества
#### Поля:
- title(Имя) - тип поля - Строка
- slug(Адрес) - тип поля - slug
- description(Описание) - тип поля - Текст метода str возвращает имя отзыва (название)

## Админка (admin.py)
- Зарегистрирована модель Group.
- Для модели Post создана кастомная админка:
    - В списке объектов в админке отображаются поля pk, text, pub_date, author, group.
    - Содержимое поля group можно редактировать в админке прямо в списке объектов Post.
    - Доступен поиск по полю text.
    - Доступна фильтрация по полю pub_date.
    - Если какое-то поле не заполнено, в нём отображается текст -пусто-.

## View-функции (views.py)
- index(): передаёт в шаблон posts/index.html десять последних объектов модели Post.
- group_posts(): передаёт в шаблон posts/group_list.html десять последних объектов модели Post, отфильтрованных по полю group, и содержимое для тега <title>.

## Адреса (urls.py)
- Для приложения Posts установлен namespace='posts'.
Для главной страницы установлен name='index'.
Страница с постами из определённой группы доступна по URL вида group/<slug>/.
- Для страницы с постами группы установлен name='group_list'.

## Шаблоны
- Файлы шаблонов хранятся на уровне проекта.
- Шаблоны разбиты на логические блоки и собираются с помощью тегов include и extend.
- К шаблонам подключена статика.
- Шаблоны соответствуют дизайну:
web_hw02_community_with_text.zip
- В шаблоне index.html ссылка <a href="">все записи группы</a> адресует пользователя на страницу той группы, которой принадлежит пост.
- Из view-функций в словаре context передаётся основное содержимое страницы.
- Содержимое тега <title> — для разных страниц разное:
    - для страницы группы: Записи сообщества <имя_группы>;
    - для главной страницы: Последние обновления на сайте.
    
 ## Запуск проекта

Клонируйте репозиторий и перейдите в него в командной строке:
```
git clone https://github.com/Alexander28-31/hw02_community.git
```
```
cd hw02_community 
```

Создайте виртуальное окружение и активируйте его
```
python -m venv venv
```
```
source venv/Scripts/activate
```

Установите зависимости из файла 
```
pip install -r requirements.txt
```

Создайте миграции и запустите их
```
python manage.py makemigrations
```
```
python manage.py migrate
```

Есть возможность создать суперпользователя
```
python manage.py createsuperuser 
```

Запустите проект
```
python manage.py runserver
```
