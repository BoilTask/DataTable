

import os
from datatable import config


def clean_file_path(path):
    path = config.get_tool_file_path() + path
    file_list = os.listdir(path)
    for file_name in file_list:
        os.remove(path + "/" + file_name)


def clean_export_data():
    config_yaml_data = config.get_config_data()
    if config.enable_client_code():
        clean_file_path(config_yaml_data['export_path']['client_path'])
    if config.enable_server_cpp_code():
        clean_file_path(config_yaml_data['export_path']['server_cpp_path'])
    if config.enable_server_go_code():
        clean_file_path(config_yaml_data['export_path']['server_go_path'])

    print("Clean Export Path Success!")


def clean_generate_code():
    config_yaml_data = config.get_config_data()
    if config.enable_client_code():
        clean_file_path(config_yaml_data['client_code_path'])
    if config.enable_server_cpp_code():
        clean_file_path(config_yaml_data['cpp_server']['server_code_path'])
    if config.enable_server_go_code():
        clean_file_path(config_yaml_data['go_server']['server_code_path'])

    print("Clean Generate Path Success!")
