#ifndef __DATA_TABLE_MANAGER_HPP__
#define __DATA_TABLE_MANAGER_HPP__

#include <map>
#include "game_macro.hpp"
//Don't edit the following content.DATATABLE_HEADER_START
#include "string_data_table.h"
#include "config_data_table.h"
#include "example_data_table.h"
//Don't edit the above content.DATATABLE_HEADER_END
#include"data_table_template.hpp"

class DataTableManager
{
public:
	DataTableManager();

public:
	static DataTableManager& GetInstance() {
		if (!DataTableManagerPtr_) {
			DataTableManagerPtr_ = new DataTableManager();
		}
		return *DataTableManagerPtr_;
	}

private:
	static DataTableManager* DataTableManagerPtr_;

public:
//Don't edit the following content.DATATABLE_DECLARE_START
	DECLARE_DATATABLE(StringDataTable)
	DECLARE_DATATABLE(ConfigDataTable)
	DECLARE_DATATABLE(ExampleDataTable)
//Don't edit the above content.DATATABLE_DECLARE_END

public:
	void Init();

private:
	bool is_init_success;

};

#endif