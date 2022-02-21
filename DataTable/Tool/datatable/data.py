
import openpyxl

from datatable import common
from datatable import config
from datatable import excel
from datatable import color


def process_data(file_id):
    global data_table
    data_table = []

    enable_client_code = config.enable_client_code_file(file_id)
    enable_server_cpp_code = config.enable_server_cpp_code_file(file_id)
    enable_server_go_code = config.enable_server_go_code_file(file_id)

    if not enable_client_code and not enable_server_cpp_code and not enable_server_go_code:
        return

    if not excel.init(file_id):
        color.print_red_text(str(file_id) + " Process Data Fail!")
        return

    process_csv_data()


def process_csv_data():
    global csv_data_table

    data_table = excel.get_data_table()
    if len(data_table) < 1:
        return

    csv_data_table = "---"
    head_name_list = excel.get_head_name_list()

    for head_name in head_name_list:
        csv_data_table += (",")
        csv_data_table += (head_name)
    csv_data_table += ("\n")

    for data_table_row in data_table:
        if len(data_table_row) < 1:
            continue
        csv_data_table += data_table_row[0]
        for content in data_table_row:
            csv_data_table += (",")
            csv_data_table += ("\"")
            csv_data_table += content
            csv_data_table += ("\"")
        csv_data_table += ("\n")


def export_csv_file(file_id):

    if config.enable_client_code_file(file_id):
        common.overwrite_file_content(
            config.get_client_export_file(file_id), csv_data_table, "utf-8")

    if config.enable_server_cpp_code_file(file_id):
        common.overwrite_file_content(
            config.get_server_cpp_export_file(file_id), csv_data_table, "utf-8")

    if config.enable_server_go_code_file(file_id):
        common.overwrite_file_content(
            config.get_server_go_export_file(file_id), csv_data_table, "utf-8")

    print("Export " + str(file_id) + " Success!")


def export_data(file_id):

    process_data(file_id)

    export_csv_file(file_id)
