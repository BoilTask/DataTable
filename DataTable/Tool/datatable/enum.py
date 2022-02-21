
import os
import yaml

from datatable import config


def init():
    global enum_value_data
    global enum_comment_data

    global enum_packet_config
    global enum_packet_data
    global enum_packet_name

    enum_value_data = {}
    enum_comment_data = {}

    enum_packet_yaml = {}
    enum_packet_config = {}
    enum_packet_data = {}
    enum_packet_name = {}

    # 取枚举配置
    enum_config_file_path = config.config_yaml_data["enum"]["enum_config_path"]
    enum_config_file_list = os.listdir(enum_config_file_path)
    for enum_config_file in enum_config_file_list:
        with open(enum_config_file_path + "/" + enum_config_file, 'r', encoding='utf-8') as enum_yaml_file:
            enum_config_file_name = os.path.splitext(enum_config_file)[0]
            enum_packet_yaml[enum_config_file_name] = yaml.load(
                enum_yaml_file, Loader=yaml.FullLoader)
            enum_yaml_file.close()

    for packet_name in enum_packet_yaml:

        enum_packet_data.update({packet_name: {}})

        for enum_type in enum_packet_yaml[packet_name]:
            if enum_type == "_":
                enum_packet_config[packet_name] = enum_packet_yaml[packet_name][enum_type]
                continue

            enum_packet_name.update({enum_type: packet_name})

            enum_packet_data[packet_name].update({enum_type: []})

            enum_yaml_data = enum_packet_yaml[packet_name][enum_type]

            enum_list = list(enum_yaml_data.keys())
            enum_index = 0

            for enum_data in enum_list:
                if enum_data == "_":
                    enum_comment_data.update(
                        {enum_type: enum_yaml_data[enum_data]})
                    continue

                enum_value = enum_yaml_data[enum_data]
                if enum_value:
                    enum_index = int(enum_value)
                add_enum_value_data(enum_type, enum_data, enum_index)

                enum_packet_data[packet_name][enum_type].append(enum_data)

                enum_index = enum_index + 1


def add_enum_value_data(key_a, key_b, val):
    if key_a in enum_value_data:
        enum_value_data[key_a].update({key_b: val})
    else:
        enum_value_data.update({key_a: {key_b: val}})


def get_enum_value(enum_type, enum_value):
    return enum_value_data[enum_type][enum_value]


def get_enum_type_comment(enum_type):
    if enum_type in enum_comment_data:
        return enum_comment_data[enum_type]
    return ""


def is_enum_exist(data_type_list):
    for data_type in data_type_list:
        if is_valid_enum(data_type):
            return True
    return False


def is_valid_enum(data_type):
    if data_type in enum_value_data:
        return True
    return False


def get_enum_packet_data():
    return enum_packet_data


def get_enum_value_data():
    return enum_value_data


def is_enable_server_cpp(packet_name):
    if packet_name in enum_packet_config:
        if "EnableServerCpp" in enum_packet_config[packet_name]:
            return enum_packet_config[packet_name]["EnableServerCpp"]
    return True


def is_enable_server_go(packet_name):
    if packet_name in enum_packet_config:
        if "EnableServerGo" in enum_packet_config[packet_name]:
            return enum_packet_config[packet_name]["EnableServerGo"]
    return True


def is_enable_client(packet_name):
    if packet_name in enum_packet_config:
        if "EnableClient" in enum_packet_config[packet_name]:
            return enum_packet_config[packet_name]["EnableClient"]
    return True


def is_enable_blueprint(packet_name):
    if packet_name in enum_packet_config:
        if "EnableBlueprint" in enum_packet_config[packet_name]:
            return enum_packet_config[packet_name]["EnableBlueprint"]
    return True


def get_enum_packet_name(enum_type):
    if enum_type in enum_packet_name:
        return enum_packet_name[enum_type]
    return ""


def is_enum_enable_blueprint(enum_type):
    packet_name = get_enum_packet_name(enum_type)
    if packet_name in enum_packet_config:
        if "EnableBlueprint" in enum_packet_config[packet_name]:
            return enum_packet_config[packet_name]["EnableBlueprint"]
    return True
