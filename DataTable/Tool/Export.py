# -*- coding: UTF-8 -*-

import os
import sys
import json
import xlrd


def is_config_valid(file_id):
    if not "export_path" in config_data:
        return False
    if not "code_path" in config_data:
        return False
    if not file_id in config_data:
        return False
    if not "upper_case" in config_data[file_id]:
        return False
    if not "lower_case" in config_data[file_id]:
        return False
    if not "sheet_list" in config_data[file_id]:
        return False

    sheet_list = config_data[file_id]["sheet_list"]
    for sheet_info in sheet_list:
        if not "sheet_name" in sheet_info:
            return False
        if not "data_id_row" in sheet_info:
            return False
        if not "data_id_col" in sheet_info:
            return False
        if not "export_type" in sheet_info:
            return False
    return True


def is_file_valid(file_id):
    return file_id in config_data


def is_data_false(data):
    return data == "" or data == "0" or data == "False" or data == "false"


def get_data_type(data_type):
    if data_type == "bool":
        return "bool"
    if data_type == "int32":
        return "int32"
    if data_type == "float":
        return "float"
    if data_type == "string":
        return "std::string"
    if data_type == "vector<bool>":
        return "std::vector<bool>"
    if data_type == "vector<int32>":
        return "std::vector<int32>"
    if data_type == "vector<float>":
        return "std::vector<float>"
    if data_type == "vector<string>":
        return "std::vector<std::string>"
    return ''


def get_parse_function_name(data_type):
    if data_type == "bool":
        return "ParseBool"
    if data_type == "int32":
        return "ParseInt"
    if data_type == "float":
        return "ParseFloat"
    if data_type == "string":
        return "ParseString"
    if data_type == "vector<bool>":
        return "ParseVectorBool"
    if data_type == "vector<int32>":
        return "ParseVectorInt"
    if data_type == "vector<float>":
        return "ParseVectorFloat"
    if data_type == "vector<string>":
        return "ParseVectorString"
    return ''


def parse_data(data_type, data):
    if data_type == "bool":
        data = str(data)
        data = data.strip()
        if is_data_false(data):
            return "0"
        return "1"
    if data_type == "int32":
        return str(int(data))
    if data_type == "float":
        return str(float(data))
    if data_type == "string":
        data = str(data)
        return data.replace("\"", "\"\"")
    if data_type == "vector<bool>":
        data = str(data)
        data = data[1: len(data) - 1]
        word_list = data.split(",")
        data = "("
        is_first = True
        for word in word_list:
            if is_first:
                is_first = False
            else:
                data = data + ","
            if is_data_false(word):
                data = data + "0"
            else:
                data = data + "1"
        data = data + ")"
        return data
    if data_type == "vector<int32>":
        data = str(data)
        data = data[1: len(data) - 1]
        word_list = data.split(",")
        data = "("
        is_first = True
        for word in word_list:
            if is_first:
                is_first = False
            else:
                data = data + ","
            data = data + str(int(word))
        data = data + ")"
        return data
    if data_type == "vector<float>":
        data = str(data)
        data = data[1: len(data) - 1]
        word_list = data.split(",")
        data = "("
        is_first = True
        for word in word_list:
            if is_first:
                is_first = False
            else:
                data = data + ","
            data = data + str(float(word))
        data = data + ")"
        return data
    if data_type == "vector<string>":
        data = str(data)
        data = data[1: len(data) - 1]
        word_list = data.split(",")
        data = "("
        is_first = True
        for word in word_list:
            if is_first:
                is_first = False
            else:
                data = data + ","
            data = data + word.replace("\"", "\"\"")
        data = data + ")"
        return data
    return ''


def export_data(file_id):
    excel_file = xlrd.open_workbook(file_path + file_dict[file_id])
    file_config = config_data[file_id]
    sheet_list = file_config["sheet_list"]
    for sheet_info in sheet_list:

        excel_sheet = excel_file.sheet_by_name(sheet_info["sheet_name"])

        data_id_row = sheet_info["data_id_row"] - 1
        data_id_col = sheet_info["data_id_col"] - 1

        data_id_value = excel_sheet.cell_value(data_id_row, data_id_col)
        if data_id_value != "DataId":
            print("DataId row or col not valid!")
            return

        data_id_row_value = excel_sheet.row_values(data_id_row)
        data_id_col_value = excel_sheet.col_values(data_id_col)
        data_id_row_max = len(data_id_col_value)
        data_id_col_max = len(data_id_row_value)
        with open(file_path + config_data['export_path'] + file_config["upper_case"] + ".csv", 'w', encoding='utf-8') as export_file:
            if sheet_info["export_type"] == "Horizontal":

                csv_head_list = data_id_row_value[data_id_col:]
                data_type_list = excel_sheet.row_values(data_id_row - 1)

                export_file.write("---")
                for csv_head in csv_head_list:
                    export_file.write(",")
                    export_file.write(csv_head)

                export_file.write("\n")

                for data_id_item in range(data_id_row + 1, data_id_row_max):
                    data_row = excel_sheet.row_values(data_id_item)

                    export_file.write(parse_data(
                        data_type_list[data_id_col], data_row[data_id_col]))

                    for data_item in range(data_id_col, data_id_col_max):
                        export_file.write(",")
                        export_file.write("\"")

                        export_file.write(parse_data(
                            data_type_list[data_item], data_row[data_item]))

                        export_file.write("\"")
                    export_file.write("\n")
            elif sheet_info["export_type"] == "Vertical":

                csv_head_list = data_id_col_value[data_id_row:]
                data_type_list = excel_sheet.col_values(data_id_col - 1)

                export_file.write("---")
                for csv_head in csv_head_list:
                    export_file.write(",")
                    export_file.write(csv_head)

                export_file.write("\n")

                for data_id_item in range(data_id_col + 1, data_id_col_max):
                    data_row = excel_sheet.col_values(data_id_item)

                    export_file.write(parse_data(
                        data_type_list[data_id_row], data_row[data_id_row]))

                    for data_item in range(data_id_row, data_id_row_max):
                        export_file.write(",")
                        export_file.write("\"")

                        export_file.write(parse_data(
                            data_type_list[data_item], data_row[data_item]))

                        export_file.write("\"")
                    export_file.write("\n")
            export_file.close()
            print("Export Success!")


def generate_code(file_id):
    excel_file = xlrd.open_workbook(file_path + file_dict[file_id])
    file_config = config_data[file_id]
    sheet_list = file_config["sheet_list"]
    for sheet_info in sheet_list:

        excel_sheet = excel_file.sheet_by_name(sheet_info["sheet_name"])

        data_id_row = sheet_info["data_id_row"] - 1
        data_id_col = sheet_info["data_id_col"] - 1

        data_id_value = excel_sheet.cell_value(data_id_row, data_id_col)
        if data_id_value != "DataId":
            print("DataId row or col not valid!")
            return

        data_id_row_value = excel_sheet.row_values(data_id_row)
        data_id_col_value = excel_sheet.col_values(data_id_col)

        if sheet_info["export_type"] == "Horizontal":
            csv_head_list = data_id_row_value[data_id_col:]
            data_type_list = excel_sheet.row_values(
                data_id_row - 1)[data_id_col:]
        elif sheet_info["export_type"] == "Vertical":
            csv_head_list = data_id_col_value[data_id_row:]
            data_type_list = excel_sheet.col_values(
                data_id_col - 1)[data_id_row:]

        with open(file_path + config_data['code_path'] + file_config["lower_case"] + ".h", 'w', encoding='utf-8') as server_code_file:

            server_code_file.write("#pragma once\n")
            server_code_file.write("\n")
            server_code_file.write(
                "//Exported by Excel, please don't edit this file directly.\n")
            server_code_file.write("\n")
            server_code_file.write("#include \"game_def.hpp\"\n")
            server_code_file.write("#include \"data_table_base.h\"\n")
            server_code_file.write("#include \"data_csv_parser.h\"\n")
            server_code_file.write("\n")
            server_code_file.write(
                "class " + file_config["upper_case"] + " : public DataTableBase\n")
            server_code_file.write("{\n")
            server_code_file.write("    public:\n")
            server_code_file.write(
                "    " + file_config["upper_case"] + "(std::string data_string)\n")
            server_code_file.write("    {\n")
            server_code_file.write(
                "        DataCsvParser csv_parser(data_string);\n")

            for data_index in range(len(csv_head_list)):
                server_code_file.write("        csv_parser.")
                server_code_file.write(
                    get_parse_function_name(data_type_list[data_index]))
                server_code_file.write("(")
                server_code_file.write(csv_head_list[data_index])
                server_code_file.write(");\n")

            server_code_file.write("    };\n")
            server_code_file.write("    \n")

            for data_index in range(len(csv_head_list)):
                server_code_file.write("    ")
                server_code_file.write(
                    get_data_type(data_type_list[data_index]))
                server_code_file.write(" ")
                server_code_file.write(csv_head_list[data_index])
                server_code_file.write(";\n")

            server_code_file.write("};\n")

            server_code_file.close()
            print("Generate Code Success!")


def process_file(file_id):
    print("1.export_data")
    print("2.generate_code & export_data")
    choose_idx = input("plase choose : ")
    if choose_idx == "1":
        export_data(file_id)
    elif choose_idx == "2":
        generate_code(file_id)
        export_data(file_id)
    else:
        print("not valid!")


# 设置环境变量
file_path = os.path.dirname(os.path.abspath(sys.argv[0]))
os.chdir(file_path)
cwd = os.getcwd()

# 取数据配置
with open('Config.json', 'r') as config_file:
    config_data = json.loads(config_file.read())
    config_file.close()

# 取数据表
file_dict = {}

file_path = file_path + "\\..\\"
file_list = os.listdir(file_path)
for excel_file in file_list:
    if is_file_valid(excel_file[0:3]) and is_config_valid(excel_file[0:3]):
        file_dict[excel_file[0:3]] = excel_file
        # print(file_path + excel_file)

# 用户选择
print("Init Success!")
print("-------------")
# print("0.All")
for file_key in file_dict:
    print(file_key + "." + file_dict[file_key][3:])
print("-------------")
file_choose = input("Choose File : ")
# if file_choose == 0 :

if not is_file_valid(file_choose):
    print("not valid!")
else:
    process_file(file_choose)
