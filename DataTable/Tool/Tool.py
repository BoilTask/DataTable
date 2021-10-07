# -*- coding: UTF-8 -*-

import sys

from datatable import datatable


def process_file(file_id):
    print("1.export_data")
    print("2.generate_code & export_data")
    choose_idx = input("plase choose : ")
    if choose_idx == "1":
        datatable.export_data(file_id)
    elif choose_idx == "2":
        datatable.generate_code(file_id)
        datatable.export_data(file_id)
    else:
        print("not valid!")


def process_all_file_choose():
    print("1.export_data")
    print("2.generate_enum")
    print("3.register_datatable")
    print("4.generate_code & export_data")
    print("0.all")
    choose_idx = input("please choose : ")
    if choose_idx == "0":
        datatable.process_all_file()
    elif choose_idx == "1":
        datatable.export_data_all()
    elif choose_idx == "2":
        datatable.generate_enum()
    elif choose_idx == "3":
        datatable.register_datatable()
    elif choose_idx == "4":
        datatable.clean_export_data()
        datatable.clean_generate_code()
        datatable.export_data_generate_code_all()


if __name__ == "__main__":

    if datatable.is_config_file_valid():
        if len(sys.argv) > 1:
            if sys.argv[1] == "all":
                datatable.process_all_file()
            elif sys.argv[1] == "export":
                datatable.export_data_all()
            exit(0)

        # 用户选择
        print("Init Success!")
        print("-------------")
        file_dict = datatable.get_file_dict()
        for file_key in file_dict:
            print(str(file_key) + "." + file_dict[file_key][3:])
        print("0.All")
        print("-------------")
        file_choose = input("Choose File : ")
        if file_choose == "0":
            process_all_file_choose()
        else:
            file_id = datatable.select_file_id(file_choose)
            if file_id < 0:
                print("not valid!")
            else:
                process_file(file_id)
    else:
        print("not valid!")
