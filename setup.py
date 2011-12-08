from distutils.core import setup


setup(
    name="django-jinja2",
    version=__import__("django_jinja2").__version__,
    description="A drop in conditional template loader to use jinja2 if the filename / path meets custom criteria",
    long_description='',
    author="Yuji Tomita",
    author_email="yuji@yujitomita.com",
    url="https://github.com/yuchant/django-jinja2",
    packages=[
        "django_jinja2",
        "django_jinja2.loaders",
    ],
    package_dir={"django_jinja2": "django_jinja2"},
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ]
)
