#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        try:
            import django
        except ImportError:
            raise ImportError(
                "Django yüklenemedi "
                "Django yüklenemedi "
                "Django yüklenemedi "
            )
        raise
    execute_from_command_line(sys.argv)
