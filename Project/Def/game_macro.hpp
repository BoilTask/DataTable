#ifndef __GAME_MACRO_HPP__
#define __GAME_MACRO_HPP__

#include "game_def.hpp"

#ifndef SAFE_DELETE
#define SAFE_DELETE(x)	if( (x)!=NULL ) { delete (x); (x)=NULL; }
#endif

#ifndef SAFE_DELETE_ARRAY
#define SAFE_DELETE_ARRAY(x)	if( (x)!=NULL ) { delete[] (x); (x)=NULL; }
#endif

#ifndef SAFE_FREE	
#define SAFE_FREE(x)	if( (x)!=NULL ) { free(x); (x)=NULL; }
#endif

#ifndef SAFE_RELEASE
#define SAFE_RELEASE(x)	if( (x)!=NULL ) { (x)->Release(); (x)=NULL; }
#endif

#ifndef GET_DATATABLE_REF
#define GET_DATATABLE_REF(DataTableName) DataTableName##_
#endif

#ifndef REGISTER_DATATABLE
#define REGISTER_DATATABLE(DataTableName) GET_DATATABLE_REF(DataTableName)(#DataTableName)
#endif

#ifndef DECLARE_DATATABLE
#define DECLARE_DATATABLE(DataTableName) \
public: \
	const DataTableName* Get##DataTableName##Row(int32 v) { \
		return GET_DATATABLE_REF(DataTableName).GetDataTableRow(v); \
	} \
private: \
	DataTableTemplate<DataTableName> GET_DATATABLE_REF(DataTableName);
#endif

#ifndef DATATABLE_GET_DATA
#define DATATABLE_GET_DATA(DataTableName, DataId) \
	DataTableManager::GetInstance().Get##DataTableName##Row(DataId);
#endif

#endif //__GAME_MACRO_HPP__
