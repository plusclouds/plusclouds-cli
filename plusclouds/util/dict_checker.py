from plusclouds.exceptions.controller_exception import ControllerException
import os.path

def path_checker(data: dict, paths: list):
    if not data:
        raise ControllerException("Data is empty or does not exist.")
    else:
        tmp_dict = data
        for item in paths:
            if item in tmp_dict:
                tmp_dict = tmp_dict[item]
            else:
                raise ControllerException(item + " does not exist in path. Cannot create with the following path.")


