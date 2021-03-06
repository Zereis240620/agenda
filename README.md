## Projeto Agenda Django
-  Projeto Agenda de Eventos, feito no Curso de DJANGO da <a href="https://digitalinnovation.one/sign-in" target="_blank">Digital Innovation One</a>
## Tecnologias Usadas
- Python, Django e Bulma
<p float="left">
<a href="https://www.python.org/"><img width="100px" height="100px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"/></a>
<a href="https://www.djangoproject.com/"><img width="100px" height="100px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-original.svg"/></a>
<a href="https://bulma.io/"><img width="100px" height="100px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bulma/bulma-plain.svg" /></a>
</p>

## Comandos Importantes Django

Criar Projeto Django:
```
django-admin startproject projectname
```

Criar Novo App:
``` 
django-admin startapp (appName)
```

Criar Tabelas Django-Admin:
```
python manage.py migrate
```

Criar Usuário Django-Admin:
```
python manage.py createsuperuser --username admin
```

Criar Migrations:
```
python manage.py makemigrations (appName)
```

Gerar Migrations Sql:
```
python manage.py sqlmigrate (appName) (Migration File)
```

Executar Migrations:
```
python manage.py migrate (appName) (Migration File)
```