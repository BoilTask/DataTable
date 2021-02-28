#ifndef __DATA_TABLE_DEF_HPP__
#define __DATA_TABLE_DEF_HPP__

#ifdef DATATABLE_SERVER
#include "data_table_manager.h"
#else
#include "DataTableManager.h"
#endif

#ifdef DATATABLE_SERVER
#define DATATABLE_ARRAY_GET_SIZE(InArrayName) \
		InArrayName.size()
#else
#define DATATABLE_ARRAY_GET_SIZE(InArrayName) \
		InArrayName.Num()
#endif

#ifndef DATATABLE_GET_CONFIG
#define DATATABLE_GET_CONFIG() \
	DATATABLE_GET_ROW(ConfigDataTable, GAME_CONFIG_DATA_ID)
#endif

#ifndef DATATABLE_GET_ROW
#ifdef DATATABLE_SERVER
#define DATATABLE_GET_ROW(DataTableName, DataId) \
	DataTableManager::GetInstance().Get##DataTableName##Row(DataId)
#else
#define DATATABLE_GET_ROW(DataTableName, DataId) \
	UDataTableManager::GetInstance().GetTableRow<F##DataTableName>(EDataTableType_##DataTableName, DataId)
#endif
#endif

#endif //__DATA_TABLE_DEF_HPP__
