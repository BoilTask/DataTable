
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

void UDataTableManager::TestDataTable()
{
	UE_LOG(LogDataTable, Display, TEXT("UDataTableManager::TestDataTable()"));

	const FExampleDataTable* DataTablePtr = DATATABLE_GET_ROW(ExampleDataTable, 900000000);
	if (DataTablePtr == nullptr)
	{
		return;
	}

	UE_LOG(LogDataTable, Display
		, TEXT("DataId = %d BoolType = %d Int32Type = %d FloatType = %f StringType = %s BitType = %d EnumType = %d")
		, DataTablePtr->DataId
		, DataTablePtr->BoolType
		, DataTablePtr->Int32Type
		, DataTablePtr->FloatType
		, *DataTablePtr->StringType
		, DataTablePtr->BitType
		, DataTablePtr->EnumType);

	bool First;
	FString Str;

	First = true;
	Str = "[";
	for (auto const& Item : DataTablePtr->VectorBoolType)
	{
		if (First)
		{
			First = false;
		}
		else
		{
			Str.Append(" ");
		}
		Str.AppendInt(Item);
	}
	Str.Append("]");
	UE_LOG(LogDataTable, Display, TEXT("DataTablePtr->VectorBoolType = %s"), *Str);

	First = true;
	Str = "[";
	for (auto const& Item : DataTablePtr->VectorInt32Type)
	{
		if (First)
		{
			First = false;
		}
		else
		{
			Str.Append(" ");
		}
		Str.AppendInt(Item);
	}
	Str.Append("]");
	UE_LOG(LogDataTable, Display, TEXT("DataTablePtr->VectorInt32Type = %s"), *Str);

	First = true;
	Str = "[";
	for (auto const& Item : DataTablePtr->VectorFloatType)
	{
		if (First)
		{
			First = false;
		}
		else
		{
			Str.Append(" ");
		}
		Str.Append(FString::SanitizeFloat(Item));
	}
	Str.Append("]");
	UE_LOG(LogDataTable, Display, TEXT("DataTablePtr->VectorFloatType = %s"), *Str);

	First = true;
	Str = "[";
	for (auto const& Item : DataTablePtr->VectorStringType)
	{
		if (First)
		{
			First = false;
		}
		else
		{
			Str.Append(" ");
		}
		Str.Append(Item);
	}
	Str.Append("]");
	UE_LOG(LogDataTable, Display, TEXT("DataTablePtr->VectorStringType = %s"), *Str);

	First = true;
	Str = "[";
	for (auto const& Item : DataTablePtr->EnumTypeList)
	{
		if (First)
		{
			First = false;
		}
		else
		{
			Str.Append(" ");
		}
		Str.AppendInt(Item);
	}
	Str.Append("]");
	UE_LOG(LogDataTable, Display, TEXT("DataTablePtr->EnumTypeList = %s"), *Str);
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
