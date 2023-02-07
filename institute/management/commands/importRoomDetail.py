import os, csv, traceback
from django.utils import timezone
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

class Command(BaseCommand):
    help = "Imports Students from given CSV file to Student Model."

    
    