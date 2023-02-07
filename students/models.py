from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from institute.constants import FLOOR_OPTIONS
from institute.validators import numeric_only