#pragma once

//Exported by Excel, please don't edit this file directly.

#include "type_def.hpp"
#include "Engine/DataTable.h"
#include "StringDataTable_C.generated.h"

USTRUCT(BlueprintType)
struct FStringDataTable : public FTableRowBase
{
	GENERATED_USTRUCT_BODY()

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = FStringDataTable)
		int32 DataId;
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = FStringDataTable)
		TArray<FString> StrList;
};
