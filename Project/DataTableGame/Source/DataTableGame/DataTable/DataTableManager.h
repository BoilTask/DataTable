#pragma once

#include "type_def.hpp"
#include "data_table_register.hpp"
#include "Engine/DataTable.h"
//Don't edit the following content.CLIENT_DATATABLE_HEADER_START
#include "ConfigDataTable_C.h"
#include "StringDataTable_C.h"
#include "ExampleDataTable_C.h"
//Don't edit the above content.CLIENT_DATATABLE_HEADER_END

#include "DataTableManager.generated.h"

UCLASS()
class UDataTableManager : public UObject
{
	GENERATED_BODY()
	
public:
	UDataTableManager();
	~UDataTableManager();

	UFUNCTION(BlueprintCallable, Category = UDataTableManager)
		static UDataTableManager* GetInstancePtr();
	static UDataTableManager& GetInstance();

private:
	static UDataTableManager* S_UDataTableManager_;
	
public:
	template<class T>
	T* GetTableRow(EDataTableType Type, int32 DataId)
	{
		UDataTable* DataTablePtr = GetDataTable(Type);
		if (nullptr == DataTablePtr)
		{
			return nullptr;
		}
		T* DataLinePtr = DataTablePtr->FindRow<T>(*FString::Printf(TEXT("%d"), DataId), TEXT("UDataTableManager"));
		return DataLinePtr;
	};

public:
	void Init();

	void TestDataTable();
	
	UDataTable* GetDataTable(EDataTableType Type);

	UFUNCTION(BlueprintCallable, Category = UDataTableManager)
		TArray<FString> const& GetStrListByDataID(int32 DataId);
	
private:
	FString EmptyString_;
	TArray <FString> EmptyStringArray_;
	TMap<EDataTableType, UDataTable*> DataTableMap_;
};
