
import os
import yaml

from datatable import config


def init():
    global enum_value_data
    global enum_yaml_data

    enum_value_data = {}
    enum_yaml_data = {}

    # 取枚举配置
    enum_config_file_path = config.config_yaml_data["enum"]["enum_config_path"]
    enum_config_file_list = os.listdir(enum_config_file_path)
    for enum_config_file in enum_config_file_list:
        with open(enum_config_file_path+"/"+enum_config_file, 'r', encoding='utf-8') as enum_yaml_file:
            enum_yaml_data.update(
                yaml.load(enum_yaml_file, Loader=yaml.FullLoader))
            enum_yaml_file.close()

    for enum_type in enum_yaml_data:
        enum_list = list(enum_yaml_data[enum_type].keys())
        enum_index = 0
        for enum_data in enum_list:
            if enum_data == "_":
                continue
            enum_value = enum_yaml_data[enum_type][enum_data]
            if enum_value:
                enum_index = int(enum_value)
            add_enum_value_data(enum_type, enum_data, enum_index)
            enum_index = enum_index + 1


def add_enum_value_data(key_a, key_b, val):
    if key_a in enum_value_data:
        enum_value_data[key_a].update({key_b: val})
    else:
        enum_value_data.update({key_a: {key_b: val}})


def get_enum_value(enum_type, enum_value):
    return enum_value_data[enum_type][enum_value]


def get_enum_type_comment(enum_type):
    if(enum_yaml_data[enum_type] and "_" in enum_yaml_data[enum_type]):
        return enum_yaml_data[enum_type]["_"]
    return ""


def get_enum_yaml_data():
    return enum_yaml_data
