#ifndef __DATA_TABLE_MANAGER_HPP__
#define __DATA_TABLE_MANAGER_HPP__

#include <map>

#include "game_macro.hpp"

#include"data_table_template.hpp"

#include"string_data_table.h"
#include"config_data_table.h"
#include"example_data_table.h"

class DataTableManager
{
public:
	DataTableManager()
		: REGISTER_DATATABLE(StringDataTable)
		, REGISTER_DATATABLE(ConfigDataTable)
		, REGISTER_DATATABLE(ExampleDataTable)
	{
			
	}
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
	void Init();

	DECLARE_DATATABLE(StringDataTable)
	DECLARE_DATATABLE(ConfigDataTable)
	DECLARE_DATATABLE(ExampleDataTable)

};

#endif