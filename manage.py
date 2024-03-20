#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
#django 프로젝트와 다양한 방법으로 상호작용하는 커맨드라인의 유틸리티

def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()

#python manage.py runserver를 통해서 django 서버를 킬 수 있고 https://127.0.0.1:8000 을 통해서 접속할 수 있다. 
#장고 서버는 파일 수정했다고 해서 서버를 재기동하지 않아도된다. 하지만 어떠한 오류가 발생하면 재시작하자.