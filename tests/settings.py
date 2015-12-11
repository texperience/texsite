DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test.db',
    }
}
INSTALLED_APPS = [
    # texsite apps
    'texsite.cleanblog',
    'texsite.bootstrap',
    'texsite.core',

    # texperience apps
    'bootstrap_ui',

    # Wagtail apps
    'wagtail.wagtailcore',

    # Django apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
]
SECRET_KEY = 'test-key'
