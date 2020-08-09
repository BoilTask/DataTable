#ifndef __DATA_CSV_PARSER_H__
#define __DATA_CSV_PARSER_H__

#include "game_def.hpp"
#include "data_table_base.h"

class DataCsvParser
{
public:
	DataCsvParser(std::string str);
    void ParseBool(bool& item);
    void ParseInt(int32& item);
    void ParseFloat(float& item);
    void ParseString(std::string& item);
    void ParseVectorBool(std::vector<bool>& item_list);
    void ParseVectorInt(std::vector<int>& item_list);
    void ParseVectorFloat(std::vector<float>& item_list);
    void ParseVectorString(std::vector<std::string>& item_list);
		
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

#endif
