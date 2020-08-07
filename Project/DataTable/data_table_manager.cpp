
#include "data_table_manager.h"

#include <iostream>

DataTableManager* DataTableManager::DataTableManagerPtr_ = nullptr;

void DataTableManager::Init()
{
	std::cout << "DataTableManager Init Success!" << std::endl;
}
