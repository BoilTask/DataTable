
import os
import re

from datatable import common
from datatable import config
from datatable import color


def game_compile(force=False):

    project_root_path = config.get_tool_file_path() + "/../"

    system_cmd_prefix = "cd " + project_root_path
    system_cmd_prefix += " & "

    is_compile = False

    if force:
        is_compile = True
    else:
        system_cmd = "cd Project/YeloliGame/Source/YeloliGame/DataTable"
        system_cmd += " & "
        system_cmd += "svn status"
        cmd_content = common.read_command(system_cmd_prefix + system_cmd)

        if cmd_content == "":
            system_cmd = "cd Project/YeloliGame/Source/YeloliGame/Def"
            system_cmd += " & "
            system_cmd += "svn status"
            cmd_content = common.read_command(system_cmd_prefix + system_cmd)

        if cmd_content != "":
            is_compile = True

    exit_code = 0
    if is_compile:
        system_cmd = "cd Tool/Package"
        system_cmd += " & "
        system_cmd += "python -u compile_game.py"

        exit_code = common.run_command(system_cmd_prefix + system_cmd)
    return exit_code == 0


def game_import(compile, force):

    project_root_path = config.get_tool_file_path() + "/../"
    client_export_path = config.get_client_export_path()

    system_cmd_prefix = "cd " + project_root_path
    system_cmd_prefix += " & "

    system_cmd = "cd " + client_export_path
    system_cmd += " & "
    system_cmd += "svn status"
    cmd_content = common.read_command(system_cmd_prefix + system_cmd)

    re_pattern = re.compile(r"[M?]\s+(\S+).csv")
    file_list = re_pattern.findall(cmd_content)

    compile_success = False
    if len(file_list) > 0:
        compile_success = game_compile(force)
    else:
        compile_success = True

    if compile_success:
        for file_name in file_list:
            system_cmd = get_import_cmd(file_name)

            print(system_cmd_prefix + system_cmd)

            common.run_command(system_cmd_prefix + system_cmd)

        re_pattern = re.compile(r"[!]\s+(\S+).csv")
        file_list = re_pattern.findall(cmd_content)
        for file_name in file_list:
            system_cmd = "cd " + client_export_path + "../"
            system_cmd += " & "
            system_cmd += "svn del " + file_name + ".uasset --force"
            common.run_command(system_cmd_prefix + system_cmd)

        return True

    else:
        color.print_red_text("Compile Fail!")
        return False


def get_import_cmd(csv_name):
    project_root_path = config.get_tool_file_path() + "/../"
    client_export_path = config.get_client_export_path()

    UE4_package_file = os.environ['UE4_PATH'] + \
        "/Engine/Binaries/Win64/UE4Editor.exe"
    if not os.path.exists(UE4_package_file):
        print("Maybe the environment variable UE4_PATH is set incorrectly!")

    # cmd_content = "del " + client_export_path + "..\\" + csv_name + ".uasset /F"

    # cmd_content += " & "

    cmd_content = ""

    cmd_content += UE4_package_file + " " + project_root_path + "\Project\YeloliGame\YeloliGame.uproject -run=ImportAssets -nosourcecontrol -dest=\"/Game/Data/\" -source=\"" + \
        client_export_path+"/" + csv_name + \
        ".csv\" -factoryname=\"CSVImportFactory\" -replaceexisting"

    return cmd_content
