from django.db import models
from django.utils import timezone

from auth_service.models import AppUser
from common_utils.mixins import AutoDateMixin
from common_utils.validators import validate_positive_float

