import enum


def NullableParameters():
	return [ParameterType.folder_path]


class ParameterType(enum.Enum):
	plusclouds_api_path = 1  # API Path
	token = 2
	email = 3
	password = 4
	folder_path = 5
