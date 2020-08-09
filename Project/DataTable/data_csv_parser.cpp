
#include "data_csv_parser.h"

#include <iostream>
#include <sstream>
#include <utility>


DataCsvParser::DataCsvParser(std::string str)
	: data_string_(std::move(str))
{
	empty_string_ = "";
	data_index_ = -1;
	InitDataItemList();
}
	
void DataCsvParser::InitDataItemList() {

	int32 item_index = 0;
	while (item_index < data_string_.length()) {
		if (data_string_[item_index] == ',') {
			break;
		}
		item_index++;
	}

	ParseDataItem(item_index + 2);
}

void DataCsvParser::ParseDataItem(int32 item_index)
{
	if (item_index >= data_string_.length()) {
		return;
	}

	std::string item = "";
	while (true) {
		if (item_index + 1 >= data_string_.length()) {
			data_item_list_.push_back(item);
			break;
		}
		if (data_string_[item_index] == '"') {
			if (data_string_[item_index + 1] == '"') {
				item += '"';
				++item_index;
			}
			else {
				data_item_list_.push_back(item);
				ParseDataItem(item_index + 3);
				break;
			}
		}
		else {
			item += data_string_[item_index];
		}
		++item_index;
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
