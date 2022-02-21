#pragma once

//Exported by Tool, please don't edit this file directly.

#include "type_def.hpp"
#include "data_def_s.h"
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
			csv_parser.ParseEnum<EEnumType>(EnumType);
			csv_parser.ParseVectorBool(VectorBoolType);
			csv_parser.ParseVectorInt(VectorInt32Type);
			csv_parser.ParseVectorFloat(VectorFloatType);
			csv_parser.ParseVectorString(VectorStringType);
			csv_parser.ParseVectorEnum<EEnumType>(EnumTypeList);
			csv_parser.ParseVectorBool(VectorIndexBoolType);
			csv_parser.ParseVectorString(VectorIndexStringType);
			csv_parser.ParseInt(FillPluginInt);
			csv_parser.ParseVectorInt(FillPluginInt32);
			csv_parser.ParseFloat(AddPlugin);
		};

		int32 DataId;
		bool BoolType;
		int32 Int32Type;
		float FloatType;
		std::string StringType;
		int32 BitType;
		EEnumType EnumType;
		std::vector<bool> VectorBoolType;
		std::vector<int32> VectorInt32Type;
		std::vector<float> VectorFloatType;
		std::vector<std::string> VectorStringType;
		std::vector<EEnumType> EnumTypeList;
		std::vector<bool> VectorIndexBoolType;
		std::vector<std::string> VectorIndexStringType;
		int32 FillPluginInt;
		std::vector<int32> FillPluginInt32;
		float AddPlugin;
	};
}
