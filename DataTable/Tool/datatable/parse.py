
from datatable import common
from datatable import enum
from datatable import plugin


def is_array_merge(data_type):
    index_l = data_type.find("[")
    index_r = data_type.rfind("]")
    if index_l >= 0 and index_r >= 0 and index_r - index_l > 1:
        return True

    return False


def get_array_merge_index(data_type):
    index_l = data_type.find("[")
    index_r = data_type.rfind("]")
    if index_l >= 0 and index_r >= 0 and index_r - index_l > 1:
        v, ok = common.get_int_from_string(data_type[index_l + 1:index_r])
        if ok:
            return v

    return -1


def get_data_type_real(data_type):
    if data_type == "bit":
        return "int32:bit()"

    index_l = data_type.find("[")
    index_r = data_type.rfind("]")
    if index_l >= 0 and index_r >= 0 and index_r - index_l > 1:
        return get_data_type_real(data_type[:index_l + 1] + data_type[index_r:])

    return data_type


def get_cpp_server_data_type(data_type):
    data_type_list = data_type.split(":", 1)
    data_type = data_type_list[0]

    if data_type == "bool":
        return "bool"
    if data_type == "int32":
        return "int32"
    if data_type == "float":
        return "float"
    if data_type == "string":
        return "std::string"
    if enum.is_valid_enum(data_type):
        return data_type

    index = data_type.find("[")
    if index >= 0:
        return "std::vector<" + get_cpp_server_data_type(data_type[:index]) + ">"

    return data_type


def get_client_data_type(data_type):
    data_type_list = data_type.split(":", 1)
    data_type = data_type_list[0]

    if data_type == "bool":
        return "bool"
    if data_type == "int32":
        return "int32"
    if data_type == "float":
        return "float"
    if data_type == "string":
        return "FString"
    if enum.is_valid_enum(data_type):
        if enum.is_enum_enable_blueprint(data_type):
            return "TEnumAsByte<" + data_type + ">"
        else:
            return "int32"

    index = data_type.find("[")
    if index >= 0:
        return "TArray<" + get_client_data_type(data_type[:index]) + ">"

    return data_type


def get_cpp_parse_function_name(data_type):
    data_type_list = data_type.split(":", 1)
    data_type = data_type_list[0]

    if data_type == "bool":
        return "ParseBool"
    if data_type == "int32":
        return "ParseInt"
    if data_type == "float":
        return "ParseFloat"
    if data_type == "string":
        return "ParseString"

    if data_type == "bool[]":
        return "ParseVectorBool"
    if data_type == "int32[]":
        return "ParseVectorInt"
    if data_type == "float[]":
        return "ParseVectorFloat"
    if data_type == "string[]":
        return "ParseVectorString"
    if enum.is_valid_enum(data_type):
        return "ParseEnum<" + data_type + ">"
    else:
        data_type = data_type.rstrip("[]")
        if enum.is_valid_enum(data_type):
            return "ParseVectorEnum<" + data_type + ">"

    index_l = data_type.find("[")
    if index_l >= 0:
        index_r = data_type.rfind("]")
        if index_r >= 0:
            return get_cpp_parse_function_name(data_type[:index_l] + data_type[index_r:])

    return ''


def get_go_parse_function_name(data_type, data_name, data_value):
    data_type_list = data_type.split(":", 1)
    data_type = data_type_list[0]

    if data_type == "bool":
        return "dataparse.ParseBool("+data_value+")"
    if data_type == "int32":
        return "dataparse.ParseInt32("+data_value+")"
    if data_type == "float":
        return "dataparse.ParseFloat32("+data_value+")"
    if data_type == "string":
        return "dataparse.ParseString("+data_value+")"
    if data_type == "bool[]":
        return "dataparse.ParseVectorBool("+data_value+")"
    if data_type == "int32[]":
        return "dataparse.ParseVectorInt32("+data_value+")"
    if data_type == "float[]":
        return "dataparse.ParseVectorFloat32("+data_value+")"
    if data_type == "string[]":
        return "dataparse.ParseVectorString("+data_value+")"
    if enum.is_valid_enum(data_type):
        return "dataparse.ParseEnum"+data_type+"("+data_value+")"
    else:
        data_type = data_type.rstrip("[]")
        if enum.is_valid_enum(data_type):
            return "dataparse.ParseVectorEnum"+data_type+"("+data_value+")"
    return ''


def get_go_variable_definition(data_type, data_name):
    data_type_list = data_type.split(":", 1)
    data_type = data_type_list[0]

    if data_type == "bool":
        return data_name + " bool"
    if data_type == "int32":
        return data_name + " int32"
    if data_type == "float":
        return data_name + " float32"
    if data_type == "string":
        return data_name + " string"
    if data_type == "bool[]":
        return data_name + " []bool"
    if data_type == "int32[]":
        return data_name + " []int32"
    if data_type == "float[]":
        return data_name + " []float32"
    if data_type == "string[]":
        return data_name + " []string"
    if enum.is_valid_enum(data_type):
        return data_name + " dataenum." + data_type
    else:
        data_type = data_type.rstrip("[]")
        if enum.is_valid_enum(data_type):
            return data_name + " []dataenum." + data_type
    return ''


def parse_data(data_type_all, data):

    plugin_index = data_type_all.find(":")

    if(plugin_index > 0):

        data_type = data_type_all[:plugin_index]
        plugin_content = data_type_all[plugin_index:]

        plugin_name_index = plugin_content.find("(")
        if(plugin_name_index > 0):

            plugin_name = plugin_content[1:plugin_name_index]

            plugin_excel_param = plugin_content[plugin_name_index:]
            plugin_excel_param = plugin_excel_param.lstrip("(").rstrip(")")
            plugin_param = "(data_type, data"
            if plugin_excel_param != "":
                plugin_param += "," + plugin_excel_param
            plugin_param += ")"
            data = eval("plugin." + plugin_name + plugin_param)

            return str(data)

    data_type = data_type_all

    return plugin.parse(data_type, data)
