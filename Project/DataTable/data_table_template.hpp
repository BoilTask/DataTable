#pragma once

#include <fstream>
#include <map>
#include <string>

#include "game_def.hpp"

template<typename T>
class DataTableTemplate {
	public:
		DataTableTemplate(std::string data_table_name) {
			const std::string& data_csv_file_path = SERVER_DATA_CSV_PATH + data_table_name + ".csv";
			std::ifstream csv_f(data_csv_file_path, std::ios::in);
			std::vector<std::string> line_list;
			std::string line_string;
			bool is_first_line = true;
			while (getline(csv_f, line_string))
			{
				if (is_first_line)
				{
					is_first_line = false;
					continue;
				}
				T* data_row_ptr = new T(line_string);
				int32 data_id = data_row_ptr->DataId;
				data_row_list_[data_id] = data_row_ptr;
			}
		}

		T* GetDataTableRow(int32 data_id){
			auto item_iter = data_row_list_.find(data_id);
			if (item_iter != data_row_list_.end()) {
				return item_iter->second;
			}
			return nullptr;
		}
private:
	std::map<int32, T*> data_row_list_;
};
