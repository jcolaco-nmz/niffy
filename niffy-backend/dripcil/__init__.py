# coding=utf-8
import re
import unicodedata


def slugify(value, allow_unicode=False, lowercase=False):
    """
    Convert to ASCII if 'allow_unicode' is False. Convert spaces to hyphens.
    Remove characters that aren't alphanumerics, underscores, or hyphens.
    Convert to lowercase. Also strip leading and trailing whitespace.
    Adapted from: https://github.com/django/django/blob/master/django/utils/text.py
    """
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
        value = re.sub('[^\w\s-]', '', value, flags=re.U).strip()
        if (lowercase):
            value = value.lower()
        return re.sub('[-\s]+', '-', value, flags=re.U)
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub('[^\w\s-]', '', value).strip()
    if (lowercase):
        value = value.lower()
    return re.sub('[-\s]+', '-', value)
