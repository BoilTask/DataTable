
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
void DataCsvParser::ParseVector(std::vector<T>& item_list)
{
	const std::string str_line = GetStringItem();
	std::istringstream line_stream(str_line.substr(1, str_line.length() - 2));
	std::string item_string;
	while (getline(line_stream, item_string, ',')){
		std::stringstream ss;
		ss << item_string;
		T item_value;
		ss >> item_value;
		item_list.push_back(item_value);
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
	
void DataCsvParser::ParseVectorBool(std::vector<bool>& item_list) {
	ParseVector(item_list);
}
	
void DataCsvParser::ParseVectorInt(std::vector<int>& item_list) {
	ParseVector(item_list);
}
	
void DataCsvParser::ParseVectorFloat(std::vector<float>& item_list) {
	ParseVector(item_list);
}

void DataCsvParser::ParseVectorString(std::vector<std::string>& item_list) {
	
	const std::string str_line = GetStringItem();

	// ("Te\"stA","Te)stB","Te,stC","Te\\stD")
	std::cout << str_line << std::endl;

	int32 item_index = 2;

	std::string item = "";

	while (true) {
		if (item_index + 1 >= str_line.length()) {
			item_list.push_back(item);
			break;
		}
		if (str_line[item_index] == '\\' ) {
			if (str_line[item_index + 1] == '"') {
				item += "\"";
				++item_index;
			}
			else if (str_line[item_index + 1] == '\\') {
				item += "\\";
				++item_index;
			}
		}
		else if (str_line[item_index] == '"') {
			item_list.push_back(item);
			item = "";
			item_index += 2;
		}
		else {
			item += str_line[item_index];
		}
		++item_index;
	}
}
