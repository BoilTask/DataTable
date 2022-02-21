
from datatable import common
from datatable import enum
from datatable import color


def parse(data_type, data):
    if data_type == "bool":
        if common.is_data_false(data):
            return "0"
        return "1"
    if data_type == "int32":
        if common.is_data_empty(data):
            return "0"
        data = str(data)
        data = data.strip()

        num, ok = common.get_int_from_string(data)
        if ok:
            return str(num)
        else:
            data_type_index = data.find("_")
            return parse(data[:data_type_index], data)

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
    if enum.is_valid_enum(data_type):
        if common.is_data_empty(data):
            return "0"
        data = str(data)
        data = data.strip()
        data = str(enum.get_enum_value(data_type, data))
        return data

    if data_type == "bool[]":
        if common.is_data_empty(data):
            return ""
        data = str(data)

        word_list = common.split_str_list(data)

        data = "("
        is_first = True
        for word in word_list:
            if is_first:
                is_first = False
            else:
                data = data + ","
            data = data + parse("bool", word)
        data = data + ")"
        return data

    if data_type == "int32[]":
        if common.is_data_empty(data):
            return ""
        data = str(data)

        word_list = common.split_str_list(data)

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
                data = data + parse("int32", word)
        data = data + ")"
        return data

    if data_type == "float[]":
        if common.is_data_empty(data):
            return ""
        data = str(data)

        word_list = common.split_str_list(data)

        data = "("
        is_first = True
        for word in word_list:
            if is_first:
                is_first = False
            else:
                data = data + ","
            data = data + parse("float", word)
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
            word = word.replace("\n", "\\n")
            word = word.replace("\"", "\\\"\"")

            data = data + "\"\"" + word + "\"\""

        data = data + ")"
        return data

    else:

        if common.is_data_empty(data):
            return ""
        data = str(data)
        data_type = data_type.rstrip("[]")
        if enum.is_valid_enum(data_type):
            word_list = data.split(",")
            data = "("
            is_first = True
            for word in word_list:
                if is_first:
                    is_first = False
                else:
                    data = data + ","
                data = data + parse(data_type, word)
            data = data + ")"
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

    if data_type == "int32":
        num, ok = common.get_int_from_string(value)
        if not ok:
            color.print_red_text(value + " invalid int!")
            return 0
        if num > 0:
            if(len(value) >= 9):
                return value
            v = str(v)
            return v + value.zfill(9 - len(str(v)))
        return str(num)

    if data_type == "int32[]":
        if common.is_data_empty(data):
            return ""
        word_list = value.split(",")
        value = "("
        is_first = True
        for word in word_list:
            if is_first:
                is_first = False
            else:
                value = value + ","
            if word == "":
                value = value + "0"
            else:
                value = value + fill("int32", word, v)
        value = value + ")"
        return value

    return value


def add(data_type, data, v):
    b, ok = common.get_float_from_string(v)
    if not ok:
        color.print_red_text("plugin add" + v + "not valid!")
        return data
    if common.is_data_false(data):
        return b
    a, ok = common.get_float_from_string(data)
    if not ok:
        color.print_red_text("plugin add" + data + "not valid!")
        return data
    return a + b
