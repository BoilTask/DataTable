
#include "data_table_manager.h"

#include "data_table_def.hpp"

namespace data
{
	DataTableManager::DataTableManager()
		: is_init_success_(false)
//Don't edit the following content.SERVER_DATATABLE_REGISTER_START
			, REGISTER_DATATABLE_SERVER(ConfigDataTable)
			, REGISTER_DATATABLE_SERVER(StringDataTable)
			, REGISTER_DATATABLE_SERVER(ExampleDataTable)
//Don't edit the above content.SERVER_DATATABLE_REGISTER_END
	{

	}
	
	void DataTableManager::Init()
	{
		const ConfigDataTable* config_data_table_ptr = DATATABLE_GET_CONFIG();
		if (config_data_table_ptr && config_data_table_ptr->EnableGame)
		{
			is_init_success_ = true;
			
			std::cout << "DataTableManager Init Success!" << std::endl;
		}
		else
		{
			std::cout << "DataTableManager Init Fail!" << std::endl;
		}
	}
}
