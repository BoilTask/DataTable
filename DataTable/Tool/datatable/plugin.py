
from datatable import common
from datatable import enum


def parse(data_type, data):
    enum_yaml_data = enum.get_enum_yaml_data()
    if data_type == "bool":
        if common.is_data_false(data):
            return "0"
        return "1"
    if data_type == "int32":
        if common.is_data_empty(data):
            return "0"
        data = str(data)
        data = data.strip()
        return str(int(float(data)))
    if data_type == "float":
        if common.is_data_empty(data):
            return "0"
        data = str(data)
        data = data.strip()
        return str(float(data)).rstrip('0').rstrip('.')
    if data_type == "string":
        if common.is_data_empty(data):
            return ""
        data = str(data)
        return data.replace("\"", "\"\"")
    if data_type in enum_yaml_data:
        if common.is_data_empty(data):
            return "0"
        data = str(data)
        data = data.strip()
        data = str(enum.get_enum_value(data_type, data))
        return data
    return ""


def bit(data_type, data):
    if common.is_data_empty(data):
        return "0"
    data = str(data)
    word_list = data.split(",")
    value = 0
    for word in word_list:
        value = value << 1 | int(parse("bool", word))
    return str(value)


def fill(data_type, data, v):
    value = "0"
    if not common.is_data_false(data):
        value = str(data)
    if(len(value) >= 9):
        return value
    v = str(v)
    return v + value.zfill(9 - len(str(v)))


def add(data_type, data, v):
    b, ok = common.get_float_from_string(v)
    if not ok:
        print("plugin add" + v + "not valid!")
        return data
    if common.is_data_false(data):
        return b
    a, ok = common.get_float_from_string(data)
    if not ok:
        print("plugin add" + data + "not valid!")
        return data
    return a + b
