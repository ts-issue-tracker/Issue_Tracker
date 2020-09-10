import re
INVALID_INPUT_ERR=-2
EXCEED_LIMIT_ERR=-1
SUCCESS=0
BLANK=-3
from PyQt5.QtWidgets import *

def assigneename_check(s2):
    pattern = re.compile(r'^([a-z]+)([a-z]+)*([a-z]+)*$',
    re.IGNORECASE)
    if re.match(pattern,s2) or len(s2)==0:
        if (len(s2)-s2.count(" ")) == 0:
            return BLANK
        if len(s2)>15:
            return EXCEED_LIMIT_ERR
        return SUCCESS
    else:
        return INVALID_INPUT_ERR

def cr_check(s2):
    pattern = re.compile(r'^\d{1,6}$')
    if re.match(pattern, s2) or len(s2)==0:
        if (len(s2)-s2.count(" ")) == 0:
            return BLANK
        return SUCCESS
    elif len(s2) > 6:
        return EXCEED_LIMIT_ERR
    else:
        return INVALID_INPUT_ERR





