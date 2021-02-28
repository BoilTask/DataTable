#pragma once

//Exported by Excel, please don't edit this file directly.

#include "type_def.hpp"
#include "data_table_base.h"
#include "data_csv_parser.h"

namespace data
{
	class ConfigDataTable : public DataTableBase
	{
	public:
		ConfigDataTable(std::string data_string)
		{
			DataCsvParser csv_parser(data_string);
			csv_parser.ParseInt(DataId);
			csv_parser.ParseBool(EnableGame);
		};

		int32 DataId;
		bool EnableGame;
	};
}
