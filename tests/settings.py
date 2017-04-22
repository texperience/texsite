DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test.db',
    }
}
INSTALLED_APPS = [
    # texsite test apps
    'tests.cleanblog',
    'tests.core',

    # texsite apps
    'texsite.cleanblog',
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
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
