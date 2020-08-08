
#include "data_csv_parser.h"


#include <sstream>
#include <utility>


DataCsvParser::DataCsvParser(std::string str)
	: data_string_(std::move(str))
{
	empty_string_ = "";
	data_index_ = 0;
	InitDataItemList();
}
	
void DataCsvParser::InitDataItemList() {
	std::istringstream line_stream(data_string_);
	std::string item_string;
	while (getline(line_stream, item_string, ','))
	{
		data_item_list_.push_back(item_string.substr(1, item_string.length() - 2));
	}
}

template <class T>
void DataCsvParser::ParseVector(std::vector<T>& item)
{
	const std::string str = GetStringItem();
		
	auto word_begin = str.begin();
	std::string sub_string;
	bool is_set_begin = false;
	for (auto iter = str.begin(); iter != str.end(); ++iter)
	{
		if (*iter == '(')
			continue;

		if (*iter != ',' && *iter != ')')
		{
			if (is_set_begin)
				continue;

			word_begin = iter;
			is_set_begin = true;
		}
		else
		{
			if (!is_set_begin)
				break;
			sub_string = std::string(word_begin, iter);
			T TValue;
			std::stringstream ss;
			ss << sub_string;
			ss >> TValue;
			item.push_back(TValue);
			is_set_begin = false;

			if (*iter == ')')
				break;
		}
	}
}


std::string& DataCsvParser::GetStringItem(){
	++data_index_;
	if(data_index_ >= 0 && data_index_ < data_item_list_.size())
	{
		return data_item_list_[data_index_];
	}
	return empty_string_;
}
	
void DataCsvParser::ParseBool(bool& item){
	int32 value = std::atoi(GetStringItem().c_str());
	item = (value != 0);
}

void DataCsvParser::ParseInt(int32& item)
{
	item = std::atoi(GetStringItem().c_str());
}
	
void DataCsvParser::ParseFloat(float& item){
	item = (float)std::atof(GetStringItem().c_str());
}
	
void DataCsvParser::ParseString(std::string& item){
	item = GetStringItem();
}
	
void DataCsvParser::ParseVectorBool(std::vector<bool>& item) {
	ParseVector(item);		
}
	
void DataCsvParser::ParseVectorInt(std::vector<int>& item) {
	ParseVector(item);
}
	
void DataCsvParser::ParseVectorFloat(std::vector<float>& item) {
	ParseVector(item);
}

void DataCsvParser::ParseVectorString(std::vector<std::string>& item) {
	ParseVector(item);
}
