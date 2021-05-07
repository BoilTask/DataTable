#pragma once

#include "type_def.hpp"
#include "data_table_base.h"

namespace data
{
	class DataCsvParser
	{
	public:
		DataCsvParser(std::string str);
		void ParseBool(bool& item);
		void ParseInt(int32& item);
		void ParseFloat(float& item);
		void ParseString(std::string& item);

		template <typename T>
		void ParseEnum(T& item)
		{
			int32 enum_value;
			ParseInt(enum_value);
			item = static_cast<T>(enum_value);
		}

		void ParseVectorBool(std::vector<bool>& item_list);
		void ParseVectorInt(std::vector<int32>& item_list);
		void ParseVectorFloat(std::vector<float>& item_list);
		void ParseVectorString(std::vector<std::string>& item_list);

		template <typename T>
		void ParseVectorEnum(std::vector<T>& item_list)
		{
			std::vector<int32> enum_value_list;
			ParseVectorInt(enum_value_list);
			for (auto& item : enum_value_list)
			{
				item_list.emplace_back(static_cast<T>(item));
			}
		}

	private:
		void InitDataItemList();
		void ParseDataItem(int32 item_index);
		std::string& GetStringItem();

		template <class T>
		void ParseVector(std::vector<T>& item_list);

	private:
		std::string data_string_;
		int32 data_index_;
		std::string empty_string_;
		std::vector<std::string> data_item_list_;
	};
}
