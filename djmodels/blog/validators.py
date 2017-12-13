from django.core.exceptions import ValidationError


def validate_author_email(email):
    if '@' not in email:
        raise ValidationError('Not a valid email!')
    return email