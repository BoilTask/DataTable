#pragma once
 
#include "game_def.hpp"
#include "data_table_base.h"
#include "data_csv_parser.h"
 
class StringDataTable : public DataTableBase
{
public:
    StringDataTable(std::string data_string)
    {
        DataCsvParser csv_parser(data_string);
        csv_parser.ParseInt(DataId);
        csv_parser.ParseVectorString(StrList);
    };
 
    std::vector<std::string> StrList;
};
