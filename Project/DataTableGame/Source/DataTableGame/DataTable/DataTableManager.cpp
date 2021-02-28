
#include "DataTableManager.h"

#include "data_table_def.hpp"

UDataTableManager* UDataTableManager::S_UDataTableManager_ = nullptr;

UDataTableManager::UDataTableManager()
{
	Init();
}

UDataTableManager::~UDataTableManager()
{

}

UDataTableManager* UDataTableManager::GetInstancePtr()
{
	if (S_UDataTableManager_ == nullptr)
	{
		S_UDataTableManager_ = NewObject<UDataTableManager>();
		S_UDataTableManager_->AddToRoot();
	}
	return S_UDataTableManager_;
}

UDataTableManager& UDataTableManager::GetInstance()
{
	if (S_UDataTableManager_ == nullptr)
	{
		S_UDataTableManager_ = NewObject<UDataTableManager>();
		S_UDataTableManager_->AddToRoot();
	}
	return *S_UDataTableManager_;
}

void UDataTableManager::Init()
{
//Don't edit the following content.CLIENT_DATATABLE_REGISTER_START
	REGISTER_DATATABLE_CLIENT(ConfigDataTable)
	REGISTER_DATATABLE_CLIENT(StringDataTable)
	REGISTER_DATATABLE_CLIENT(ExampleDataTable)
//Don't edit the above content.CLIENT_DATATABLE_REGISTER_END
}

UDataTable* UDataTableManager::GetDataTable(EDataTableType Type)
{
	UDataTable** TablePtr = DataTableMap_.Find(Type);
	if (TablePtr)
	{
		return *TablePtr;
	}
	return nullptr;
}

TArray<FString> const& UDataTableManager::GetStrListByDataID(int32 DataId)
{
	const FStringDataTable* DataTablePtr = DATATABLE_GET_ROW(StringDataTable, DataId);
	if (DataTablePtr == nullptr)
	{
		UE_LOG(LogMemory, Display, TEXT("UDataTableManager::GetStrListByDataID nullptr DataId = %d"), DataId);
		return EmptyStringArray_;
	}
	return DataTablePtr->StrList;
}
