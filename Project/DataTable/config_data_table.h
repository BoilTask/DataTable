#pragma once
 
#include "game_def.hpp"
#include "data_table_base.h"
#include "data_csv_parser.h"
 
class ConfigDataTable : public DataTableBase
{
public:
    ConfigDataTable(std::string data_string)
    {
        DataCsvParser csv_parser(data_string);
        csv_parser.ParseInt(DataId);
        csv_parser.ParseBool(IsOpen);
        csv_parser.ParseInt(GameType);
    };
 
    bool IsOpen;
    int32 GameType;
};
