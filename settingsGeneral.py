# import mokebeCsvProcessing.toolz as t


from enum import Enum
from os import environ
import os


# from

class gluDebugMode(Enum):
    user = 101
    debug = 102


def czyNasi() -> bool:
    username = environ["USERNAME"]

    if username == 'macie':
        return True
    else:
        return False


def debugMode() -> gluDebugMode:
    if czyNasi():
        lMode = gluDebugMode.user
        # lMode = gluDebugMode.debug
    else:
        lMode = gluDebugMode.user
    return lMode


