

import openpyxl

from datatable import parse
from datatable import config
from datatable import color


class MergeData:
    index = 0
    value = ""

    def __init__(self, i, v):
        self.index = i
        self.value = v

    def __repr__(self):
        return str(self.index) + " " + self.value

    def __lt__(self, other):
        return self.index < other.index


def init(file_id):
    global excel_file

    file_name = config.get_file_name(file_id)
    tool_file_path = config.get_tool_file_path()
    excel_file = openpyxl.load_workbook(
        tool_file_path + file_name, data_only=True)

    if not process(file_id):
        return False
    return True


def select(sheet):
    global excel_sheet
    global sheet_config
    sheet_config = sheet
    excel_sheet = excel_file[sheet_config["sheet_name"]]


def process(file_id):

    global excel_data_table

    file_config = config.get_file_config(file_id)
    sheet_list = file_config["sheet_list"]

    if not check_head(file_id, sheet_list):
        return False

    excel_data_table = []
    for sheet_info in sheet_list:
        if not process_data(sheet_info):
            color.print_red_text(str(file_id) + " " + sheet_info["sheet_name"]
                                 + " DataId row or col not valid!")
            continue

        if len(sheet_data_table) < 1:
            color.print_red_text(str(file_id) + " " + sheet_info["sheet_name"]
                                 + " Sheet not valid!")
            continue
        excel_data_table += sheet_data_table

    return True


def check_head(file_id, sheet_list):

    last_data_type_list = []
    last_head_name_list = []
    for sheet_info in sheet_list:
        if not process_head(sheet_info):
            color.print_red_text(str(file_id) + " " + sheet_info["sheet_name"]
                                 + " Head not valid!")
            return False

        data_type_list = get_data_type_list()
        if len(data_type_list) < 1:
            color.print_red_text(str(file_id) + " " + sheet_info["sheet_name"]
                                 + " Head not valid!")
            return False

        head_name_list = get_head_name_list()
        if len(head_name_list) < 1:
            color.print_red_text(str(file_id) + " " + sheet_info["sheet_name"]
                                 + " Head not valid!")
            return False

        if len(last_data_type_list) > 0 and last_data_type_list != data_type_list:
            color.print_red_text(str(file_id) + " " + sheet_info["sheet_name"]
                                 + " Head not valid!")
            return False
        if len(last_head_name_list) > 0 and last_head_name_list != head_name_list:
            color.print_red_text(str(file_id) + " " + sheet_info["sheet_name"]
                                 + " Head not valid!")
            return False

        last_data_type_list = data_type_list
        last_head_name_list = head_name_list
    return True


def process_head(sheet_info):
    global data_type_list
    global data_type_map
    global head_name_list
    global head_name_map
    global data_id_list

    global data_row_valid
    global data_col_valid

    global array_merge_map

    global data_row_max
    global data_col_max

    select(sheet_info)

    data_id_row = sheet_config["data_id_row"] - 1
    data_id_col = sheet_config["data_id_col"] - 1
    export_type = sheet_config["export_type"]

    if get_excel_value(data_id_row, data_id_col) != "DataId":
        return False

    excel_sheet_rows_data = tuple_rows()

    data_row_max = 0
    data_col_max = 0
    for data in excel_sheet_rows_data:
        data_row_max += 1
        data_col_max = max(data_col_max, len(data))

    data_type_list = []
    data_type_map = {}
    head_name_list = []
    head_name_map = {}
    data_id_list = []
    data_row_valid = {}
    data_col_valid = {}

    array_merge_map = {}

    if export_type == "Horizontal":
        for index in range(data_id_col, data_col_max):
            data_type_value = get_excel_value(data_id_row - 1, index)
            if data_type_value in [None, ""]:
                continue
            head_name_value = get_excel_value(data_id_row, index)
            if head_name_value in [None, ""]:
                continue

            if head_name_value in head_name_list:
                continue

            if parse.is_array_merge(data_type_value):
                array_merge_map[index] = True

            data_type_value = parse.get_data_type_real(data_type_value)

            data_type_list.append(data_type_value)
            head_name_list.append(head_name_value)
            data_col_valid[index] = True
            data_type_map[index] = data_type_value
            head_name_map[index] = head_name_value

        for index in range(data_id_row + 1, data_row_max):
            data_id_value = get_excel_value(index, data_id_col)
            if data_id_value in [None, ""]:
                continue
            data_id_list.append(data_id_value)
            data_row_valid[index] = True

    elif export_type == "Vertical":

        for index in range(data_id_row, data_row_max):
            data_type_value = get_excel_value(index, data_id_col - 1)
            if data_type_value in [None, ""]:
                continue
            head_name_value = get_excel_value(index, data_id_col)
            if head_name_value in [None, ""]:
                continue

            if head_name_value in head_name_list:
                continue

            if parse.is_array_merge(data_type_value):
                array_merge_map[index] = True

            data_type_value = parse.get_data_type_real(data_type_value)

            data_type_list.append(data_type_value)
            head_name_list.append(head_name_value)
            data_row_valid[index] = True
            data_type_map[index] = data_type_value
            head_name_map[index] = head_name_value

        for index in range(data_id_col + 1, data_col_max):
            data_id_value = get_excel_value(data_id_row, index)
            if data_id_value in [None, ""]:
                continue
            data_id_list.append(data_id_value)
            data_col_valid[index] = True

    else:
        return False

    return True


def process_data(sheet_info):

    global sheet_data_table

    if not process_head(sheet_info):
        return False

    data_id_row = sheet_config["data_id_row"] - 1
    data_id_col = sheet_config["data_id_col"] - 1
    export_type = sheet_config["export_type"]

    if get_excel_value(data_id_row, data_id_col) != "DataId":
        return False

    sheet_data_table = []

    if export_type == "Horizontal":

        for i in range(data_id_row + 1, data_row_max):
            if not is_row_valid(i):
                continue
            row_table = []
            for j in range(data_id_col, data_col_max):
                if not is_col_valid(j):
                    continue
                data_type = data_type_map[j]
                head_name = head_name_map[j]

                value = ""
                if is_array_merge(j):
                    merge_array_list = []
                    for index in range(j, data_col_max):

                        head_name_value = get_excel_value(data_id_row, index)
                        if head_name == head_name_value:
                            data_type_value = get_excel_value(
                                data_id_row - 1, index)
                            merge_index = parse.get_array_merge_index(
                                data_type_value)

                            if merge_index >= 0:
                                content = get_excel_value(i, index)
                                merge_array_list.append(
                                    MergeData(merge_index, content))

                    merge_array_list = sorted(merge_array_list)

                    for merge_array_i in range(len(merge_array_list)):
                        data = merge_array_list[merge_array_i]
                        if(merge_array_i > 0):
                            value += ","
                        if data.value:
                            value += str(data.value)
                        else:
                            value += ""

                else:
                    value = get_excel_value(i, j)

                content = parse.parse_data(data_type, value)
                row_table.append(content)
            sheet_data_table.append(row_table)

    elif export_type == "Vertical":

        for i in range(data_id_col + 1, data_col_max):
            if not is_col_valid(i):
                continue
            row_table = []
            for j in range(data_id_row, data_row_max):
                if not is_row_valid(j):
                    continue
                data_type = data_type_map[j]
                head_name = head_name_map[j]

                value = ""
                if is_array_merge(j):
                    merge_array_list = []
                    for index in range(j, data_row_max):
                        head_name_value = get_excel_value(index, data_id_col)
                        if head_name == head_name_value:
                            data_type_value = get_excel_value(
                                index, data_id_col - 1)
                            merge_index = parse.get_array_merge_index(
                                data_type_value)

                            if merge_index >= 0:
                                content = get_excel_value(index, i)
                                merge_array_list.append(
                                    MergeData(merge_index, content))

                    merge_array_list = sorted(merge_array_list)

                    for merge_array_i in range(len(merge_array_list)):
                        data = merge_array_list[merge_array_i]
                        if(merge_array_i > 0):
                            value += ","
                        if data.value:
                            value += data.value
                        else:
                            value += ""

                else:
                    value = get_excel_value(j, i)

                content = parse.parse_data(data_type, value)
                row_table.append(content)
            sheet_data_table.append(row_table)

    else:
        return False

    return True


def get_excel_value(data_row, data_col):
    return select_excel_value(data_row + 1, data_col + 1)


def select_excel_value(data_row, data_col):
    return excel_sheet.cell(row=data_row, column=data_col).value


def tuple_rows():
    return tuple(excel_sheet.rows)


def tuple_columns():
    return tuple(excel_sheet.columns)


def is_data_valid(row, col):
    if row not in data_row_valid:
        return False
    if col not in data_col_valid:
        return False
    return data_row_valid[row] and data_col_valid[col]


def is_row_valid(row):
    if row not in data_row_valid:
        return False
    return data_row_valid[row]


def is_col_valid(col):
    if col not in data_col_valid:
        return False
    return data_col_valid[col]


def is_array_merge(index):
    return index in array_merge_map and array_merge_map[index]


def get_data_table():
    return excel_data_table


def get_data_type_list():
    return data_type_list


def get_head_name_list():
    return head_name_list
