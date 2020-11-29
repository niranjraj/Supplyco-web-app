from django.core.exceptions import ValidationError
import re

def validate_aadhaar(value):
    pattern= bool(re.match("(\d{12})",value))
    if not pattern:
        raise ValidationError("Aadhaar is invalid") 
    return value
         
