#ifndef __DATA_TABLE_REGISTER_HPP__
#define __DATA_TABLE_REGISTER_HPP__

#ifndef DATATABLE_SERVER

//Don't edit the following content.CLIENT_DATATABLE_TYPE_START
enum EDataTableType
{
	EDataTableType_ConfigDataTable = 100,
	EDataTableType_StringDataTable = 101,
	EDataTableType_ExampleDataTable = 900,
	EDataTableType_Max
};
//Don't edit the above content.CLIENT_DATATABLE_TYPE_END

//Don't edit the following content.CLIENT_DATATABLE_ESCAPE_START
#define ConfigDataTable FConfigDataTable
#define StringDataTable FStringDataTable
#define ExampleDataTable FExampleDataTable
//Don't edit the above content.CLIENT_DATATABLE_ESCAPE_END

#ifndef REGISTER_DATATABLE_CLIENT // Client Register
#define REGISTER_DATATABLE_CLIENT(DataTableName) \
	DataTableMap_.Add(EDataTableType_##DataTableName, Cast<UDataTable>(StaticLoadObject(UDataTable::StaticClass(), NULL, TEXT("DataTable'/Game/Data/"#DataTableName"."#DataTableName"'"))));
#endif

#endif

#ifndef GET_DATATABLE_REF
#define GET_DATATABLE_REF(DataTableName) DataTableName##_
#endif

#ifndef REGISTER_DATATABLE_SERVER // Server Register
#define REGISTER_DATATABLE_SERVER(DataTableName) GET_DATATABLE_REF(DataTableName)(#DataTableName)
#endif

#ifndef DECLARE_DATATABLE_SERVER // Server Declare
#define DECLARE_DATATABLE_SERVER(DataTableName) \
public: \
	DataTableName* Get##DataTableName##Row(int32 v) { \
		return GET_DATATABLE_REF(DataTableName).GetDataTableRow(v); \
	} \
private: \
	DataTableTemplate<DataTableName> GET_DATATABLE_REF(DataTableName);
#endif

#endif //__DATA_TABLE_REGISTER_HPP__
