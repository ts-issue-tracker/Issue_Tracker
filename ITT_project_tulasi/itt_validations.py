import re
INVALID_INPUT_ERR=-2
EXCEED_LIMIT_ERR=-1
SUCCESS=0

def username_check(s2):
    pattern = re.compile(r'^([a-z]+)([a-z]+)*([a-z]+)*$',
    re.IGNORECASE)
    if re.match(pattern,s2):
        if len(s2)>15:
            return EXCEED_LIMIT_ERR
        return SUCCESS
    else:
        return INVALID_INPUT_ERR

def password_check(s2):
    pattern = re.compile(r'^([a-z0-9]+)([a-z0-9]+)*([a-z0-9]+)*$',
    re.IGNORECASE)
    if re.match(pattern, s2):
        if len(s2) > 15:
            return EXCEED_LIMIT_ERR
        return SUCCESS
    else:
        return INVALID_INPUT_ERR
