__author__ = "Supratik Majumdar"
__status__ = "Development"

def check_atleast_one_param(params: dict):
    flag = False
    for key, value in params.items():
        if value is not None:
            flag = True
            break
    return flag
