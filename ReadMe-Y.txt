From FreeCodingCamp's tutorial: https://www.youtube.com/watch?v=JIFqqdRxmVo
(Django Rest Framework & React Tutorial: Learning Management System (Blackboard / Moodle Clone))


1. rename "base_name" to "basename"

2. python manage.py migrate --run-syncdb (to address error "django.db.utils.OperationalError: no such table: users_user" )

3. (To address error "rigin 'localhost' in CORS_ORIGIN_WHITELIST is missing scheme or netloc HINT: Add a scheme (e.g. https://) or netloc (e.g. example.com).")

CORS_ORIGIN_WHITELIST = (
    u'http://localhost:8888',
    u'http://127.0.0.1:8000',
    ...
)

AND: ALLOWED_HOSTS = ['localhost']

# ******

coco => woof (teacher, staff, superuser)
pumps => meowmeow  (teacher, staff, superuser)
miao => miaomiao    (student)
elon => woofwoof    (teacher, staff)

# ******

$ python manage.py shell
>>> from users.models import User
>>> coco = User.objects.get(username='coco')
>>> coco
<User: coco>
>>> coco.is_superuser = True
>>> coco.is_staff = True
>>> coco.save()
>>> exit()

>>> for coco in c:
...     print(coco)
... 
coco
>>> 


$ python manage.py shell
>>> from users.models import User
>>> coco = User.objects.get(username='coco')
>>> coco.is_superuser
True
>>> coco.set_password('woof')
>>> coco.save()
>>> exit()