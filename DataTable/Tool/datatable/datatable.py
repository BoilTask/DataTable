

from datatable import config
from datatable import common
from datatable import clean
from datatable import data
from datatable import code


def get_file_dict():
    return config.get_file_dict()


def is_config_file_valid():
    return config.is_config_file_valid()


def select_file_id(file_choose):
    file_id, ok = common.get_int_from_string(file_choose)
    if ok and is_file_id_valid(file_id):
        return file_id
    return -1


def is_file_id_valid(file_id):
    if config.is_file_valid(file_id):
        return True
    else:
        return False


def process_all_file():
    clean.clean_export_data()
    clean.clean_generate_code()
    code.register_datatable()
    code.generate_enum()
    export_data_generate_code_all()


def export_data_all():
    clean.clean_export_data()
    file_dict = get_file_dict()
    for file_key in file_dict:
        export_data(file_key)


def export_data_generate_code_all():
    file_dict = get_file_dict()
    for file_key in file_dict:
        generate_code(file_key)
        export_data(file_key)


def export_data(file_id):
    data.export_data(file_id)


def generate_code(file_id):
    code.generate_code(file_id)


def clean_export_data():
    clean.clean_export_data()


def clean_generate_code():
    clean.clean_generate_code()


def generate_enum():
    code.generate_enum()


def register_datatable():
    code.register_datatable()
