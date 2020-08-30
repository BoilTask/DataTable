
#include "data_table_manager.h"

#include <iostream>

DataTableManager* DataTableManager::DataTableManagerPtr_ = nullptr;

DataTableManager::DataTableManager()
	: is_init_success(false)
//Don't edit the following content.DATATABLE_REGISTER_START
	, REGISTER_DATATABLE(StringDataTable)
	, REGISTER_DATATABLE(ConfigDataTable)
	, REGISTER_DATATABLE(ExampleDataTable)
//Don't edit the above content.DATATABLE_REGISTER_END
{

}

void DataTableManager::Init()
{
	is_init_success = true;
	std::cout << "DataTableManager Init Success!" << std::endl;
}

