from django.core.exceptions import ValidationError


def min_len_validator(value):
    if value < 2:
        raise ValidationError(f'The username must be a minimum of 2 chars')


def validate_year(value):
    if value < 1980 or value > 2049:
        raise ValidationError(f'Year must be between 1980 and 2049')