# 视成影院


### 使用方法
在`CinemaSystem/settings.py`中第78行处，分别修改USER和PASSWORD为MySQL数据库对应的用户名和密码。
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cinemasystem',
        'USER': '(此处填入mysql用户名)',
        'PASSWORD': '(此处填入mysql密码)',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

