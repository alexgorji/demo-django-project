#!/usr/bin/env python
def main():
    try:
        from django.core.management.utils import get_random_secret_key
        print(get_random_secret_key())
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc


if __name__ == '__main__':
    main()
