# -*- coding: UTF-8 -*-

import sys

from datatable import datatable
from datatable import color


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
        color.print_red_text("not valid!")


def process_all_file_choose():
    print("1.export_data")
    print("2.generate_enum")
    print("3.register_datatable")
    print("4.generate_code & export_data")
    print("5.game import")
    print("6.all besides import")
    print("0.all")
    choose_idx = input("please choose : ")
    if choose_idx == "0":
        datatable.process_all_file()
        datatable.game_import(True)
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
    elif choose_idx == "5":
        datatable.game_import(True)
    elif choose_idx == "6":
        datatable.process_all_file()


if __name__ == "__main__":

    if datatable.is_config_file_valid():
        exit_code = 0
        if len(sys.argv) > 1:
            if sys.argv[1] == "all":
                datatable.process_all_file()
            elif sys.argv[1] == "import":
                compile = False
                force = False
                if len(sys.argv) > 2:
                    if sys.argv[2] == "compile":
                        compile = True
                        if len(sys.argv) > 3:
                            if sys.argv[3] == "force":
                                force = True
                if not datatable.game_import(compile, force):
                    exit_code = 1
            elif sys.argv[1] == "export":
                datatable.export_data_all()
                if not datatable.game_import(True):
                    exit_code = 1
            exit(exit_code)

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
                color.print_red_text("not valid!")
            else:
                process_file(file_id)
    else:
        color.print_red_text("not valid!")
