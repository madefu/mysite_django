# mysite_django
参照https://www.runoob.com/django/django-model.html初始化工程

DB初始化使用

目录结构
```
| mysite
    |-- mysite
        --settings.py
    |-- polls
        |--templates
            --hello.html
        --testdb.py
        --urs.py
        --views.py
    |-- TestModel
        --apps.py
    -- manage.py
```
初始化DB
准备好mysql
初始化命令：
```
python manage.py makemigrations
python manage.py migrate TestModel
```

### 绘制序列图 Sequence Diagram

```seq
Andrew->China: Says Hello
Note right of China: China thinks\nabout it
China-->Andrew: How are you?
Andrew->>China: I am good thanks!
```
### End
