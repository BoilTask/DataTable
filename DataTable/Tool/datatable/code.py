
from datatable import common
from datatable import config
from datatable import excel
from datatable import enum
from datatable import parse
from datatable import color


def generate_enum():

    if config.enable_client_code():
        generate_client_enum()

    if config.enable_server_cpp_code():
        generate_server_cpp_enum()

    if config.enable_server_go_code():
        generate_server_go_enum()
        generate_server_go_enum_parse()

    print("Generate Enum Success!")


def register_datatable():

    if config.enable_client_code():
        register_client_datatable()

    if config.enable_server_cpp_code():
        register_server_cpp_datatable()

    if config.enable_server_go_code():
        register_server_go_datatable()

    print("Register DataTable Success!")


def generate_code(file_id):

    if not excel.init(file_id):
        color.print_red_text("Generate Code Fail!")
        return

    if config.enable_client_code_file(file_id):
        generate_client_code(file_id)

    if config.enable_server_cpp_code_file(file_id):
        generate_server_cpp_code(file_id)

    if config.enable_server_go_code_file(file_id):
        generate_server_go_code(file_id)


def generate_client_code(file_id):

    type_def_file_name = config.get_type_def_file_name()
    enum_def_file_name = config.get_client_enum_def_file_name()
    upper_case_name = config.get_file_upper_case_name(file_id)
    client_file_suffix = config.get_client_file_suffix()

    code_content = ""
    code_content += "#pragma once\n"
    code_content += "\n"
    code_content += "//Exported by Tool, please don't edit this file directly.\n"
    code_content += "\n"
    code_content += "#include \"" + type_def_file_name + "\"\n"
    code_content += "#include \"" + enum_def_file_name + "\"\n"
    code_content += "#include \"Engine/DataTable.h\"\n"
    code_content += "#include \"" + upper_case_name + \
        client_file_suffix + ".generated.h\"\n"
    code_content += "\n"
    code_content += "USTRUCT(BlueprintType)\n"
    code_content += "struct F" + upper_case_name + " : public FTableRowBase\n"
    code_content += "{\n"
    code_content += "\tGENERATED_USTRUCT_BODY()\n"
    code_content += "\n"

    data_type_list = excel.get_data_type_list()
    head_name_list = excel.get_head_name_list()

    for data_index in range(len(data_type_list)):
        data_type = data_type_list[data_index]
        head_name = head_name_list[data_index]

        code_content += "\tUPROPERTY(EditAnywhere, BlueprintReadWrite, Category = F" + \
            upper_case_name + ")\n"
        code_content += "\t\t"
        code_content += parse.get_client_data_type(data_type)
        code_content += " "
        code_content += head_name
        code_content += ";\n"

    code_content += "};\n"

    code_file_path = config.get_client_code_file_path(file_id)
    common.overwrite_file_content(code_file_path, code_content)

    print("Generate " + str(file_id) + " Client Code Success!")


def generate_server_cpp_code(file_id):

    type_def_file_name = config.get_type_def_file_name()
    enum_def_file_name = config.get_server_cpp_enum_def_file_name()
    upper_case_name = config.get_file_upper_case_name(file_id)
    code_namespace = config.get_code_namespace()

    code_content = ""

    code_content += "#pragma once\n"
    code_content += "\n"
    code_content += "//Exported by Tool, please don't edit this file directly.\n"
    code_content += "\n"
    code_content += "#include \"" + type_def_file_name + "\"\n"
    code_content += "#include \"" + enum_def_file_name + "\"\n"
    code_content += "#include \"data_table_base.h\"\n"
    code_content += "#include \"data_csv_parser.h\"\n"
    code_content += "\n"
    code_content += "namespace " + code_namespace + "\n"
    code_content += "{\n"
    code_content += "\tclass " + upper_case_name + " : public DataTableBase\n"
    code_content += "\t{\n"
    code_content += "\tpublic:\n"
    code_content += "\t\t" + upper_case_name + "(std::string data_string)\n"
    code_content += "\t\t{\n"
    code_content += "\t\t\tDataCsvParser csv_parser(data_string);\n"

    data_type_list = excel.get_data_type_list()
    head_name_list = excel.get_head_name_list()

    for data_index in range(len(data_type_list)):
        data_type = data_type_list[data_index]
        head_name = head_name_list[data_index]

        code_content += "\t\t\tcsv_parser."
        code_content += parse.get_cpp_parse_function_name(data_type)
        code_content += "("
        code_content += head_name
        code_content += ");\n"

    code_content += "\t\t};\n"
    code_content += "\n"

    for data_index in range(len(data_type_list)):
        data_type = data_type_list[data_index]
        head_name = head_name_list[data_index]
        code_content += "\t\t"
        code_content += parse.get_cpp_server_data_type(data_type)
        code_content += " "
        code_content += head_name
        code_content += ";\n"

    code_content += "\t};\n"
    code_content += "}\n"

    code_file_path = config.get_server_cpp_code_file_path(file_id)
    common.overwrite_file_content(code_file_path, code_content)

    print("Generate " + str(file_id) + " Server C++ Code Success!")


def generate_server_go_code(file_id):

    upper_case_name = config.get_file_upper_case_name(file_id)

    data_type_list = excel.get_data_type_list()
    head_name_list = excel.get_head_name_list()
    go_project_name = config.get_serverv_go_project_name()

    code_content = ""
    code_content += "//Exported by Tool, please don't edit this file directly.\n"
    code_content += "\n"
    code_content += "package datatablepacket\n"
    code_content += "\n"

    code_content += "import (\n"
    code_content += "	\"encoding/csv\"\n"
    code_content += "	\"io\"\n"
    code_content += "	\"" + go_project_name + "/common/config\"\n"

    if enum.is_enum_exist(data_type_list):
        code_content += "	\"" + go_project_name + "/datatable/dataenum\"\n"

    code_content += "	\"" + go_project_name + "/datatable/dataparse\"\n"
    code_content += "	\"os\"\n"
    code_content += ")\n"

    code_content += "\n"

    code_content += "type " + upper_case_name + " struct {\n"

    for data_index in range(len(data_type_list)):
        data_type = data_type_list[data_index]
        data_name = head_name_list[data_index]

        code_content += "\t"
        code_content += parse.get_go_variable_definition(data_type, data_name)
        code_content += "\n"

    code_content += "}\n"

    code_content += "\n"

    code_content += "func Init"+upper_case_name + \
        "() map[int32]"+upper_case_name+" {\n"

    code_content += "	file, err := os.Open(config.Conf.DataTablePath + \"/" + \
        upper_case_name+".csv\")\n"
    code_content += "	defer file.Close()\n"
    code_content += "	if err != nil {\n"
    code_content += "		return nil\n"
    code_content += "	}\n"
    code_content += "	"+upper_case_name + \
        "Map := make(map[int32]"+upper_case_name+")\n"
    code_content += "	firstLine := true\n"
    code_content += "	reader := csv.NewReader(file)\n"
    code_content += "	for {\n"
    code_content += "		line, err := reader.Read()\n"
    code_content += "		if err == io.EOF {\n"
    code_content += "			break\n"
    code_content += "		}\n"
    code_content += "		if err != nil {\n"
    code_content += "			return nil\n"
    code_content += "		}\n"
    code_content += "		if firstLine {\n"
    code_content += "			firstLine = false\n"
    code_content += "			continue\n"
    code_content += "		}\n"
    code_content += "		DataId := dataparse.ParseInt32(line[1])\n"
    code_content += "		"+upper_case_name + \
        "Map[DataId] = "+upper_case_name+"{\n"

    for data_index in range(len(data_type_list)):
        data_type = data_type_list[data_index]
        data_name = head_name_list[data_index]

        code_content += "			"
        code_content += parse.get_go_parse_function_name(
            data_type, data_name, "line["+str(data_index+1)+"]")
        code_content += ",\n"

    code_content += "		}\n"
    code_content += "	}\n"
    code_content += "	return "+upper_case_name+"Map\n"
    code_content += "}\n"

    code_file_path = config.get_server_go_code_file_path(file_id)
    common.overwrite_file_content(code_file_path, code_content)

    print("Generate " + str(file_id) + " Server Go Code Success!")


def register_client_datatable():

    config_data = config.get_config_data()
    register_config = config_data['register']
    client_register_config = config_data['client_register']
    file_dict = config.get_file_dict()

    client_header_content = "\n"
    for file_id in file_dict:

        if not config.enable_client_code_file(file_id):
            continue

        client_header_content += "#include \"" + \
            config.get_client_code_file_name(file_id) + "\"\n"

    common.write_file_content(config.get_client_register_h_path(),
                              client_register_config["client_header_start"], client_register_config["client_header_end"], client_header_content)

    client_register_content = "\n"
    for file_id in file_dict:

        if not config.enable_client_code_file(file_id):
            continue
        upper_case_name = config.get_file_upper_case_name(file_id)
        client_register_content += "\tREGISTER_DATATABLE_CLIENT(" + \
            upper_case_name + ")\n"

    common.write_file_content(config.get_client_register_cpp_path(),
                              client_register_config["client_register_start"], client_register_config["client_register_end"], client_register_content)

    data_table_type = "\nenum EDataTableType\n{\n"
    for file_id in file_dict:

        if not config.enable_client_code_file(file_id):
            continue

        upper_case_name = config.get_file_upper_case_name(file_id)
        data_table_type += "\tEDataTableType_" + \
            upper_case_name + " = "+str(file_id)+",\n"

    data_table_type += "\tEDataTableType_Max\n};\n"

    common.write_file_content(config.get_register_type_path(),
                              register_config["type_start"], register_config["type_end"], data_table_type)

    if config.enable_escape():

        data_table_escape = "\n"
        for file_id in file_dict:

            if not config.enable_client_code_file(file_id):
                continue

            data_table_escape += "#define " + upper_case_name + " F" + upper_case_name+"\n"

        common.write_file_content(config.get_register_type_path(),
                                  register_config["escape_start"], register_config["escape_end"], data_table_escape)

    print("Register Client DataTable Success!")


def register_server_cpp_datatable():

    config_data = config.get_config_data()
    register_config = config_data['register']
    server_register_config = config_data['server_cpp_register']
    file_dict = config.get_file_dict()

    server_header_content = "\n"
    for file_id in file_dict:
        if not config.enable_server_cpp_code_file(file_id):
            continue
        server_header_content += "#include \"" + \
            config.get_server_cpp_code_file_name(file_id) + "\"\n"
    common.write_file_content(config.get_serverv_cpp_register_h_path(),
                              server_register_config["server_header_start"], server_register_config["server_header_end"], server_header_content)

    server_register_content = "\n"
    for file_id in file_dict:
        if not config.enable_server_cpp_code_file(file_id):
            continue
        upper_case_name = config.get_file_upper_case_name(file_id)

        server_register_content += "\t\t\t, REGISTER_DATATABLE_SERVER(" + \
            upper_case_name + ")\n"

    common.write_file_content(config.get_serverv_cpp_register_cpp_path(),
                              server_register_config["server_register_start"], server_register_config["server_register_end"], server_register_content)

    server_declare_content = "\n"
    for file_id in file_dict:
        if not config.enable_server_cpp_code_file(file_id):
            continue
        upper_case_name = config.get_file_upper_case_name(file_id)

        server_declare_content += "\t\tDECLARE_DATATABLE_SERVER(" + \
            upper_case_name + ")\n"

    common.write_file_content(config.get_serverv_cpp_register_h_path(),
                              server_register_config["server_declare_start"], server_register_config["server_declare_end"], server_declare_content)

    print("Register Server C++ DataTable Success!")


def register_server_go_datatable():
    config_data = config.get_config_data()
    register_config = config_data['go_server']
    file_dict = config.get_file_dict()

    server_declare_content = "\n"
    for file_id in file_dict:
        if not config.enable_server_go_code_file(file_id):
            continue
        upper_case_name = config.get_file_upper_case_name(file_id)

        server_declare_content += "	" + upper_case_name + \
            "Map map[int32]" + upper_case_name + "\n"

    common.write_file_content(config.get_serverv_go_register_path(),
                              register_config["server_declare_start"], register_config["server_declare_end"],
                              server_declare_content, 'utf-8')

    server_register_content = "\n"
    for file_id in file_dict:
        if not config.enable_server_go_code_file(file_id):
            continue
        upper_case_name = config.get_file_upper_case_name(file_id)

        server_register_content += "	Manager." + \
            upper_case_name+"Map = Init" + upper_case_name+"()\n"

    common.write_file_content(config.get_serverv_go_register_path(),
                              register_config["server_register_start"], register_config["server_register_end"],
                              server_register_content, 'utf-8')

    server_get_content = "\n"
    for file_id in file_dict:
        if not config.enable_server_go_code_file(file_id):
            continue
        upper_case_name = config.get_file_upper_case_name(file_id)

        server_get_content += "\nfunc Get" + upper_case_name + \
            "Map() *map[int32]" + upper_case_name+" {\n"
        server_get_content += "	return &Manager." + upper_case_name + "Map\n"
        server_get_content += "}\n"

        server_get_content += "\nfunc Get" + upper_case_name + \
            "(DataId int32) *" + upper_case_name + " {\n"
        server_get_content += "\tres, ok := Manager." + \
            upper_case_name + "Map[DataId]\n"
        server_get_content += "\tif ok {\n"
        server_get_content += "\t\treturn &res\n"
        server_get_content += "\t} else {\n"
        server_get_content += "\t\treturn nil\n"
        server_get_content += "\t}\n"
        server_get_content += "}\n"

    server_get_content += "\n"

    common.write_file_content(config.get_serverv_go_register_path(),
                              register_config["server_get_start"], register_config["server_get_end"],
                              server_get_content, 'utf-8')

    print("Register Server Go DataTable Success!")


def generate_client_enum():

    type_def_file_name = config.get_type_def_file_name()
    enum_packet_data = enum.get_enum_packet_data()

    code_content = ""

    code_content += "#pragma once\n"
    code_content += "\n"
    code_content += "//Exported by Tool, please don't edit this file directly.\n"
    code_content += "\n"
    code_content += "#include \"" + type_def_file_name + "\"\n"

    for enum_packet in enum_packet_data:
        packet_enum_data = enum_packet_data[enum_packet]

        if enum.is_enable_client(enum_packet):
            enable_blueprint = enum.is_enable_blueprint(enum_packet)

            for enum_type in packet_enum_data:

                code_content += "\n"
                if enable_blueprint:
                    code_content += "UENUM(BlueprintType, Blueprintable)\n"
                code_content += "enum " + enum_type

                enum_comment = enum.get_enum_type_comment(enum_type)
                if enum_comment != "":
                    code_content += " //" + enum_comment
                code_content += "\n"
                code_content += "{"

                enum_data = packet_enum_data[enum_type]

                for index in range(len(enum_data)):
                    enum_data_value = enum_data[index]
                    code_content += "\n\t" + enum_data_value
                    code_content += " = "
                    code_content += str(enum.get_enum_value(enum_type,
                                                            enum_data_value))
                    if(index != len(enum_data) - 1):
                        code_content += ","
                code_content += "\n};\n"

    code_file_path = config.get_client_enum_file_path()
    common.overwrite_file_content(code_file_path, code_content)

    print("Generate Client Enum Success!")


def generate_server_cpp_enum():

    type_def_file_name = config.get_type_def_file_name()
    code_namespace = config.get_code_namespace()
    enum_packet_data = enum.get_enum_packet_data()

    code_content = ""

    code_content += "#pragma once\n"
    code_content += "\n"
    code_content += "//Exported by Tool, please don't edit this file directly.\n"
    code_content += "\n"
    code_content += "#include \"" + type_def_file_name + "\"\n"
    code_content += "\n"
    code_content += "namespace " + code_namespace + "\n"
    code_content += "{"

    for enum_packet in enum_packet_data:
        packet_enum_data = enum_packet_data[enum_packet]

        if enum.is_enable_server_cpp(enum_packet):

            for enum_type in packet_enum_data:

                code_content += "\n"
                code_content += "\tenum " + enum_type
                enum_comment = enum.get_enum_type_comment(enum_type)
                if enum_comment != "":
                    code_content += " //"+enum_comment
                code_content += "\n"
                code_content += "\t{"

                enum_data = packet_enum_data[enum_type]

                for index in range(len(enum_data)):
                    enum_data_value = enum_data[index]
                    code_content += "\n\t\t" + enum_data_value
                    code_content += " = "
                    code_content += str(enum.get_enum_value(enum_type,
                                                            enum_data_value))
                    if(index != len(enum_data) - 1):
                        code_content += ","
                code_content += "\n\t};\n"

    code_content += "}\n"

    code_file_path = config.get_server_cpp_enum_file_path()
    common.overwrite_file_content(code_file_path, code_content)

    print("Generate Server C++ Enum Success!")


def generate_server_go_enum():

    enum_packet_data = enum.get_enum_packet_data()

    code_content = ""

    code_content += "//Exported by Tool, please don't edit this file directly.\n"
    code_content += "\n"
    code_content += "package dataenum\n"

    for enum_packet in enum_packet_data:
        packet_enum_data = enum_packet_data[enum_packet]

        if enum.is_enable_server_go(enum_packet):

            for enum_type in packet_enum_data:

                code_content += "\n"

                code_content += "type " + enum_type + " int32"
                enum_comment = enum.get_enum_type_comment(enum_type)
                if enum_comment != "":
                    code_content += "\t//"+enum_comment
                code_content += "\n"

                code_content += "const ("

                enum_data = packet_enum_data[enum_type]

                for index in range(len(enum_data)):
                    enum_data_value = enum_data[index]
                    code_content += "\n	" + enum_data_value + " "+enum_type
                    code_content += " = "
                    code_content += str(enum.get_enum_value(enum_type,
                                                            enum_data_value))
                code_content += "\n)\n"

    code_file_path = config.get_server_go_enum_file_path()
    common.overwrite_file_content(code_file_path, code_content)

    print("Generate Server Go Enum Success!")


def generate_server_go_enum_parse():

    enum_packet_data = enum.get_enum_packet_data()
    go_project_name = config.get_serverv_go_project_name()

    code_content = ""

    code_content += "//Exported by Tool, please don't edit this file directly.\n"
    code_content += "\n"
    code_content += "package dataparse\n"

    code_content += "\n"
    code_content += "import (\n"
    code_content += "\t\"" + go_project_name + "/datatable/dataenum\"\n"
    code_content += "\t\"strings\"\n"
    code_content += ")\n"

    for enum_packet in enum_packet_data:
        packet_enum_data = enum_packet_data[enum_packet]

        if enum.is_enable_server_go(enum_packet):

            for enum_type in packet_enum_data:
                code_content += "\n"
                code_content += "func ParseEnum" + \
                    enum_type+"(s string) dataenum." + enum_type + " {\n"
                code_content += "\treturn dataenum." + \
                    enum_type+"(ParseInt32(s))\n"
                code_content += "}\n"

                code_content += "\n"
                code_content += "func ParseVectorEnum" + \
                    enum_type+"(s string) []dataenum." + enum_type + " {\n"
                code_content += "\tvar v []dataenum." + enum_type + "\n"
                code_content += "\tif s == \"\" {\n"
                code_content += "\t\treturn v\n"
                code_content += "\t}\n"
                code_content += "\tslice := strings.Split(s[1:len(s)-1], \", \")\n"
                code_content += "\tfor _, c := range slice {\n"
                code_content += "\t\tv = append(v, dataenum." + \
                    enum_type+"(ParseInt32(c)))\n"
                code_content += "\t}\n"
                code_content += "\treturn v\n"
                code_content += "}\n"

    code_file_path = config.get_server_go_enum_parse_file_path()
    common.overwrite_file_content(code_file_path, code_content)

    print("Generate Server Go Enum Success!")
