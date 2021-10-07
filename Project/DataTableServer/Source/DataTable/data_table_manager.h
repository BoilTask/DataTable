#ifndef __DATA_TABLE_MANAGER_HPP__
#define __DATA_TABLE_MANAGER_HPP__

#include "singleton.hpp"
#include "data_table_register.hpp"

#include"data_table_template.hpp"
//Don't edit the following content.SERVER_DATATABLE_HEADER_START
#include "config_data_table_s.h"
#include "example_data_table_s.h"
//Don't edit the above content.SERVER_DATATABLE_HEADER_END

namespace data
{
	
	class DataTableManager : public Singleton<DataTableManager>
	{
	public:
		DataTableManager();
//Don't edit the following content.SERVER_DATATABLE_DECLARE_START
		DECLARE_DATATABLE_SERVER(ConfigDataTable)
		DECLARE_DATATABLE_SERVER(ExampleDataTable)
//Don't edit the above content.SERVER_DATATABLE_DECLARE_END
		
	public:
		void Init();
		
	private:
		bool is_init_success_;
	};
	
}
#endif