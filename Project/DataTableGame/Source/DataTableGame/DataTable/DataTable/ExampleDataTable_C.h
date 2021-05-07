#pragma once

//Exported by Excel, please don't edit this file directly.

#include "type_def.hpp"
#include "data_def_c.h"
#include "Engine/DataTable.h"
#include "ExampleDataTable_C.generated.h"

USTRUCT(BlueprintType)
struct FExampleDataTable : public FTableRowBase
{
	GENERATED_USTRUCT_BODY()

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = FExampleDataTable)
		int32 DataId;
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = FExampleDataTable)
		bool BoolType;
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = FExampleDataTable)
		int32 Int32Type;
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = FExampleDataTable)
		float FloatType;
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = FExampleDataTable)
		FString StringType;
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = FExampleDataTable)
		int32 BitType;
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = FExampleDataTable)
		TEnumAsByte<EEnumType> EnumType;
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = FExampleDataTable)
		TArray<bool> VectorBoolType;
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = FExampleDataTable)
		TArray<int32> VectorInt32Type;
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = FExampleDataTable)
		TArray<float> VectorFloatType;
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = FExampleDataTable)
		TArray<FString> VectorStringType;
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = FExampleDataTable)
		TArray<TEnumAsByte<EEnumType2>> EnumTypeList;
};
