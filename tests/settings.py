DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test.db',
    }
}
INSTALLED_APPS = [
    # texsite test apps
    'tests.cleanblog',

    # texsite apps
    'texsite.cleanblog',
    'texsite.bootstrap',
    'texsite.core',

    # texperience apps
    'bootstrap_ui',

    # Wagtail apps
    'wagtail.wagtailusers',
    'wagtail.wagtailimages',
    'wagtail.wagtailcore',

    # Third party apps
    'taggit',

    # Django apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
]
MIDDLEWARE_CLASSES = (
  'django.contrib.sessions.middleware.SessionMiddleware',
  'wagtail.wagtailcore.middleware.SiteMiddleware',
)
ROOT_URLCONF = 'tests.urls'
SECRET_KEY = 'test-key'
