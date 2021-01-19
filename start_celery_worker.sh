#!/bin/bash
. celery.env && celery -A celery_runner worker --loglevel=info
