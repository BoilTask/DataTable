
import os


def get_int_from_string(data):
    if data:
        number = 0
        success = True
        try:
            number = int(data)
        except ValueError:
            success = False
        return number, success
    else:
        return 0, True


def get_float_from_string(data):
    if data:
        number = 0
        success = True
        try:
            number = float(data)
        except ValueError:
            success = False
        return number, success
    else:
        return 0, True


def is_data_empty(data):
    return data == None or data == ""


def is_data_false(data):
    data = str(data)
    data = data.strip()
    return is_data_empty(data) or data == "None" or data == "0" or data == "False" or data == "false"


def read_command(command):
    command_gbk_bytes = command.encode('gbk')
    command_gbk_str = command_gbk_bytes.decode('gbk')
    return os.popen(command_gbk_str).read()


def run_command(command):
    command_gbk_bytes = command.encode('gbk')
    command_gbk_str = command_gbk_bytes.decode('gbk')
    return os.system(command_gbk_str)


def overwrite_file_content(write_file_path, content, code="gbk"):
    with open(write_file_path, 'w', encoding=code) as target_file:
        target_file.write(content)
        target_file.close()


def write_file_content(write_file_path, start_key, end_key, content):
    file_content = ""
    with open(write_file_path, 'r', encoding='utf-8') as target_file:
        file_content = target_file.read()
        start_index = file_content.find(start_key)
        if start_index == -1:
            return
        head_end_index = file_content.find(end_key)
        if head_end_index == -1:
            return
        start_content = ""
        end_content = ""
        start_content = file_content[:(start_index + len(start_key))]
        end_content = file_content[head_end_index:]
        file_content = start_content + content + end_content

    with open(write_file_path, 'w', encoding='gbk') as target_file:
        target_file.write(file_content)
