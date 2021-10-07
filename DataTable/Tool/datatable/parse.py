
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

    enum_yaml_data = enum.get_enum_yaml_data()
    if data_type == "bool":
        return "bool"
    if data_type == "int32":
        return "int32"
    if data_type == "float":
        return "float"
    if data_type == "string":
        return "std::string"
    if data_type in enum_yaml_data:
        return data_type

    index = data_type.find("[")
    if index >= 0:
        return "std::vector<" + get_cpp_server_data_type(data_type[:index]) + ">"

    return data_type


def get_client_data_type(data_type):
    data_type_list = data_type.split(":", 1)
    data_type = data_type_list[0]

    enum_yaml_data = enum.get_enum_yaml_data()
    if data_type == "bool":
        return "bool"
    if data_type == "int32":
        return "int32"
    if data_type == "float":
        return "float"
    if data_type == "string":
        return "FString"
    if data_type in enum_yaml_data:
        return "TEnumAsByte<" + data_type + ">"

    index = data_type.find("[")
    if index >= 0:
        return "TArray<" + get_client_data_type(data_type[:index]) + ">"

    return data_type


def get_cpp_parse_function_name(data_type):
    data_type_list = data_type.split(":", 1)
    data_type = data_type_list[0]

    enum_yaml_data = enum.get_enum_yaml_data()
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
    if data_type in enum_yaml_data:
        return "ParseEnum<" + data_type + ">"
    else:
        data_type = data_type.rstrip("[]")
        if data_type in enum_yaml_data:
            return "ParseVectorEnum<" + data_type + ">"

    index_l = data_type.find("[")
    if index_l >= 0:
        index_r = data_type.rfind("]")
        if index_r >= 0:
            return get_cpp_parse_function_name(data_type[:index_l] + data_type[index_r:])

    return ''


def get_go_parse_function_name(data_type, data_name):
    data_type_list = data_type.split(":", 1)
    data_type = data_type_list[0]

    enum_yaml_data = enum.get_enum_yaml_data()
    if data_type == "bool":
        return "ParseBool"
    if data_type == "int32":
        return "ParseInt32"
    if data_type == "float":
        return "ParseFloat32"
    if data_type == "string":
        return "ParseString"
    if data_type == "bool[]":
        return "ParseVectorBool"
    if data_type == "int32[]":
        return "ParseVectorInt32"
    if data_type == "float[]":
        return "ParseVectorFloat32"
    if data_type == "string[]":
        return "ParseVectorString"
    if data_type in enum_yaml_data:
        return "ParseEnum"
    else:
        data_type = data_type.rstrip("[]")
        if data_type in enum_yaml_data:
            return "ParseVectorEnum"
    return ''


def get_go_variable_definition(data_type, data_name):
    data_type_list = data_type.split(":", 1)
    data_type = data_type_list[0]

    enum_yaml_data = enum.get_enum_yaml_data()
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
    if data_type in enum_yaml_data:
        return data_name + " int32"
    else:
        data_type = data_type.rstrip("[]")
        if data_type in enum_yaml_data:
            return data_name + " []int32"
    return ''


def parse_data(data_type_all, data):
    enum_yaml_data = enum.get_enum_yaml_data()

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

    if data_type == "bool":
        return plugin.parse(data_type, data)

    if data_type == "int32":
        return plugin.parse(data_type, data)

    if data_type == "float":
        return plugin.parse(data_type, data)

    if data_type == "string":
        return plugin.parse(data_type, data)

    if data_type in enum_yaml_data:
        return plugin.parse(data_type, data)

    if data_type == "bool[]":
        if common.is_data_empty(data):
            return ""
        data = str(data)
        word_list = data.split(",")
        data = "("
        is_first = True
        for word in word_list:
            if is_first:
                is_first = False
            else:
                data = data + ","
            data = data + plugin.parse("bool", word)
        data = data + ")"
        return data

    if data_type == "int32[]":
        if common.is_data_empty(data):
            return ""
        data = str(data)
        word_list = data.split(",")
        data = "("
        is_first = True
        for word in word_list:
            if is_first:
                is_first = False
            else:
                data = data + ","
            if word == "":
                data = data + "0"
            else:
                data = data + plugin.parse("int32", word)
        data = data + ")"
        return data

    if data_type == "float[]":
        if common.is_data_empty(data):
            return ""
        data = str(data)
        word_list = data.split(",")
        data = "("
        is_first = True
        for word in word_list:
            if is_first:
                is_first = False
            else:
                data = data + ","
            data = data + plugin.parse("float", word)
        data = data + ")"
        return data

    if data_type == "string[]":
        if common.is_data_empty(data):
            return ""
        data = str(data)
        word_list = data.split(",")

        real_word_list = []
        i = 0
        while i < len(word_list):
            word = word_list[i]
            real_word = ""
            j = 0
            while j < len(word):
                c = word[j]
                if c == '\\':
                    if j + 1 < len(word):
                        real_word += word[j + 1]
                        j += 1
                    else:
                        real_word += ","
                        if i + 1 < len(word_list):
                            word += word_list[i + 1]
                        i += 1
                else:
                    real_word += c

                j += 1

            real_word_list.append(real_word)

            i += 1

        data = "("
        is_first = True
        for word in real_word_list:
            if is_first:
                is_first = False
            else:
                data = data + ","

            word = word.replace("\\", "\\\\")
            word = word.replace("\"", "\\\"\"")

            data = data + "\"\"" + word + "\"\""

        data = data + ")"
        return data

    else:

        if common.is_data_empty(data):
            return ""
        data = str(data)
        data_type = data_type.rstrip("[]")
        if data_type in enum_yaml_data:
            word_list = data.split(",")
            data = "("
            is_first = True
            for word in word_list:
                if is_first:
                    is_first = False
                else:
                    data = data + ","
                data = data + plugin.parse(data_type, word)
            data = data + ")"
            return data

    return ""
