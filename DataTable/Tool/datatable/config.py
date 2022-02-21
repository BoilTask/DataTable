
import os
import sys
import yaml

from datatable import common


def init():
    global config_yaml_data
    global datatable_yaml_data
    global excel_file_dict
    global tool_file_path

    # 设置环境变量
    tool_file_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    os.chdir(tool_file_path)

    # 取数据配置
    with open('../Config/Config.yaml', 'r', encoding='utf-8') as config_yaml_file:
        config_yaml_data = yaml.load(config_yaml_file, Loader=yaml.FullLoader)
        config_yaml_file.close()

    # 取表格配置
    with open('../Config/DataTable.yaml', 'r', encoding='utf-8') as datatable_yaml_file:
        datatable_yaml_data = yaml.load(
            datatable_yaml_file, Loader=yaml.FullLoader)
        datatable_yaml_file.close()

    # 取数据表
    excel_file_dict = {}
    tool_file_path = tool_file_path + "\\..\\"
    file_list = os.listdir(tool_file_path)
    for excel_file in file_list:
        file_id, success = common.get_int_from_string(excel_file[0:3])
        if success and is_file_valid(file_id) and is_config_valid(file_id):
            excel_file_dict[file_id] = excel_file
            # print(tool_file_path + excel_file)


def is_file_valid(file_id):
    return file_id in datatable_yaml_data


def is_config_file_valid():
    if not "export_path" in config_yaml_data:
        print("config hasn't export_path")
        return False
    if not "client_code_path" in config_yaml_data:
        print("config hasn't client_code_path")
        return False
    if not "namespace" in config_yaml_data:
        print("config hasn't namespace")
        return False
    return True


def is_config_valid(file_id):
    if not is_file_valid(file_id):
        print("config hasn't " + file_id)
        return False
    if not "upper_case" in datatable_yaml_data[file_id]:
        print(file_id + " hasn't upper_case")
        return False
    if not "lower_case" in datatable_yaml_data[file_id]:
        print(file_id + " hasn't lower_case")
        return False
    if not "sheet_list" in datatable_yaml_data[file_id]:
        print(file_id + " hasn't sheet_list")
        return False

    sheet_list = datatable_yaml_data[file_id]["sheet_list"]
    sheet_index = 0
    for sheet_info in sheet_list:
        if not "sheet_name" in sheet_info:
            print(file_id + "sheet_info " + sheet_index+" hasn't sheet_name")
            return False
        if not "data_id_row" in sheet_info:
            print(file_id + "sheet_info " + sheet_index+" hasn't data_id_row")
            return False
        if not "data_id_col" in sheet_info:
            print(file_id + "sheet_info " + sheet_index+" hasn't data_id_col")
            return False
        if not "export_type" in sheet_info:
            print(file_id + "sheet_info " + sheet_index+" hasn't export_type")
            return False
        sheet_index += 1
    return True


def get_config_data():
    return config_yaml_data


def get_file_config(file_id):
    return datatable_yaml_data[file_id]


def get_file_name(file_id):
    return excel_file_dict[file_id]


def get_tool_file_path():
    return tool_file_path


def get_file_dict():
    return excel_file_dict


def get_client_export_path():
    return get_tool_file_path() + config_yaml_data['export_path']['client_path']


def get_client_export_file(file_id):
    file_config = get_file_config(file_id)
    return get_client_export_path() + file_config["upper_case"] + ".csv"


def get_server_cpp_export_file(file_id):
    file_config = get_file_config(file_id)
    return get_tool_file_path() + \
        config_yaml_data['export_path']['server_cpp_path'] + \
        file_config["upper_case"] + ".csv"


def get_server_go_export_file(file_id):
    file_config = get_file_config(file_id)
    return get_tool_file_path() + \
        config_yaml_data['export_path']['server_go_path'] + \
        file_config["upper_case"] + ".csv"


def enable_escape():
    if "enable_escape" in config_yaml_data['client_register'] and config_yaml_data['client_register']["enable_escape"] == True:
        return True
    return False


def enable_client_code():
    if "enable_client_code" not in config_yaml_data:
        return False
    if config_yaml_data["enable_client_code"] == False:
        return False
    return True


def enable_client_code_file(file_id):
    if "enable_client_code" not in config_yaml_data:
        return False
    if config_yaml_data["enable_client_code"] == False:
        return False
    file_config = get_file_config(file_id)
    if "enable_client_code" in file_config and file_config["enable_client_code"] == False:
        return False
    return True


def enable_server_cpp_code():
    if "enable_server_code" not in config_yaml_data:
        return False
    if "enable_server_cpp_code" not in config_yaml_data["enable_server_code"]:
        return False
    if "enable_server_cpp_code" not in config_yaml_data["enable_server_code"]:
        return False
    if config_yaml_data["enable_server_code"]["enable_server_cpp_code"] == False:
        return False
    return True


def enable_server_cpp_code_file(file_id):
    if "enable_server_code" not in config_yaml_data:
        return False
    if "enable_server_cpp_code" not in config_yaml_data["enable_server_code"]:
        return False
    if "enable_server_cpp_code" not in config_yaml_data["enable_server_code"]:
        return False
    if config_yaml_data["enable_server_code"]["enable_server_cpp_code"] == False:
        return False
    file_config = get_file_config(file_id)
    if "enable_server_code" in file_config and file_config["enable_server_code"] == False:
        return False
    return True


def enable_server_go_code():
    if "enable_server_code" not in config_yaml_data:
        return False
    if "enable_server_go_code" not in config_yaml_data["enable_server_code"]:
        return False
    if "enable_server_go_code" not in config_yaml_data["enable_server_code"]:
        return False
    if config_yaml_data["enable_server_code"]["enable_server_go_code"] == False:
        return False
    return True


def enable_server_go_code_file(file_id):
    if "enable_server_code" not in config_yaml_data:
        return False
    if "enable_server_go_code" not in config_yaml_data["enable_server_code"]:
        return False
    if "enable_server_go_code" not in config_yaml_data["enable_server_code"]:
        return False
    if config_yaml_data["enable_server_code"]["enable_server_go_code"] == False:
        return False
    file_config = get_file_config(file_id)
    if "enable_server_code" in file_config and file_config["enable_server_code"] == False:
        return False
    return True


def get_code_namespace():
    return config_yaml_data['namespace']


def get_type_def_file_name():
    return config_yaml_data['type_def_file']


def get_client_enum_def_file_name():
    return config_yaml_data['enum']['enum_def_client_file']


def get_server_cpp_enum_def_file_name():
    return config_yaml_data['enum']['enum_def_server_cpp_file']


def get_server_go_enum_def_file_name():
    return config_yaml_data['enum']['enum_def_server_go_file']


def get_client_file_suffix():
    return config_yaml_data['client_file_suffix']


def get_file_upper_case_name(file_id):
    file_config = get_file_config(file_id)
    return file_config["upper_case"]


def get_file_lower_case_name(file_id):
    file_config = get_file_config(file_id)
    return file_config["lower_case"]


def get_client_code_file_name(file_id):
    return get_file_upper_case_name(file_id) \
        + config_yaml_data['client_file_suffix'] \
        + config_yaml_data['client_file_extension']


def get_client_code_file_path(file_id):
    return get_tool_file_path() + config_yaml_data['client_code_path'] \
        + get_client_code_file_name(file_id)


def get_server_cpp_code_file_name(file_id):
    return get_file_lower_case_name(file_id) \
        + config_yaml_data['cpp_server']['server_file_suffix'] \
        + config_yaml_data['cpp_server']['server_file_extension']


def get_server_cpp_code_file_path(file_id):
    return get_tool_file_path() + config_yaml_data['cpp_server']['server_code_path']  \
        + get_server_cpp_code_file_name(file_id)


def get_server_go_code_file_name(file_id):
    return get_file_lower_case_name(file_id) \
        + config_yaml_data['go_server']['server_file_suffix'] \
        + config_yaml_data['go_server']['server_file_extension']


def get_server_go_code_file_path(file_id):
    return get_tool_file_path() + config_yaml_data['go_server']['server_code_path']  \
        + get_server_go_code_file_name(file_id)


def get_client_enum_file_path():
    return get_tool_file_path() + config_yaml_data['enum']['enum_def_client_path'] + config_yaml_data['enum']['enum_def_client_file']


def get_server_cpp_enum_file_path():
    return get_tool_file_path() + config_yaml_data['enum']['enum_def_server_cpp_path'] + config_yaml_data['enum']['enum_def_server_cpp_file']


def get_server_go_enum_file_path():
    return get_tool_file_path() + config_yaml_data['enum']['enum_def_server_go_path'] + config_yaml_data['enum']['enum_def_server_go_file']


def get_server_go_enum_parse_file_path():
    return get_tool_file_path() + config_yaml_data['enum']['enum_parse_server_go_path'] + config_yaml_data['enum']['enum_parse_server_go_file']


def get_client_register_h_path():
    return get_tool_file_path() + config_yaml_data['client_register']['client_register_path'] + config_yaml_data['client_register']['client_register_h_file']


def get_client_register_cpp_path():
    return get_tool_file_path() + config_yaml_data['client_register']['client_register_path'] + config_yaml_data['client_register']['client_register_cpp_file']


def get_register_type_path():
    return get_tool_file_path() + config_yaml_data['type_register_path'] + config_yaml_data["type_register_file"]


def get_serverv_cpp_register_h_path():
    return get_tool_file_path() + config_yaml_data['server_cpp_register']['server_register_path'] + config_yaml_data['server_cpp_register']['server_register_h_file']


def get_serverv_cpp_register_cpp_path():
    return get_tool_file_path() + config_yaml_data['server_cpp_register']['server_register_path'] + config_yaml_data['server_cpp_register']['server_register_cpp_file']


def get_serverv_go_register_path():
    return get_tool_file_path() + config_yaml_data['go_server']['server_register_path'] + config_yaml_data['go_server']['server_register_file']


def get_serverv_go_project_name():
    return config_yaml_data['go_server']['server_project_name']
