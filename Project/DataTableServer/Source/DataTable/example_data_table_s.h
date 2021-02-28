#pragma once

//Exported by Excel, please don't edit this file directly.

#include "type_def.hpp"
#include "data_table_base.h"
#include "data_csv_parser.h"

namespace data
{
	class ExampleDataTable : public DataTableBase
	{
	public:
		ExampleDataTable(std::string data_string)
		{
			DataCsvParser csv_parser(data_string);
			csv_parser.ParseInt(DataId);
			csv_parser.ParseBool(BoolType);
			csv_parser.ParseInt(Int32Type);
			csv_parser.ParseFloat(FloatType);
			csv_parser.ParseString(StringType);
			csv_parser.ParseInt(BitType);
			csv_parser.ParseVectorBool(VectorBoolType);
			csv_parser.ParseVectorInt(VectorInt32Type);
			csv_parser.ParseVectorFloat(VectorFloatType);
			csv_parser.ParseVectorString(VectorStringType);
		};

		int32 DataId;
		bool BoolType;
		int32 Int32Type;
		float FloatType;
		std::string StringType;
		int32 BitType;
		std::vector<bool> VectorBoolType;
		std::vector<int32> VectorInt32Type;
		std::vector<float> VectorFloatType;
		std::vector<std::string> VectorStringType;
	};
}
