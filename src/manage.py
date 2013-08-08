#!/usr/bin/env python

import os
import sys

if __name__ == "__main__":
    PROJECT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    
    sys.path.insert(1, PROJECT_DIR)
    sys.path.insert(1, os.path.join(PROJECT_DIR, 'django'))
    
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)