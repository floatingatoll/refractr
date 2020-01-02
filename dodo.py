#!/usr/bin/env python3

DOIT_CONFIG = {
    'verbosity': 2,
}

def task_generate():
    return {
        'actions': [
            'bin/refractr > etc/nginx/conf.d/refractr.conf',
        ],
    }

def task_build():
    return {
        'task_dep': [
            'generate',
        ],
        'actions': [
            'docker build . -t refractr',
        ],
    }