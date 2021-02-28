#pragma once

//Exported by Excel, please don't edit this file directly.

#include "type_def.hpp"
#include "Engine/DataTable.h"
#include "ConfigDataTable_C.generated.h"

USTRUCT(BlueprintType)
struct FConfigDataTable : public FTableRowBase
{
	GENERATED_USTRUCT_BODY()

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = FConfigDataTable)
		int32 DataId;
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = FConfigDataTable)
		bool EnableGame;
};
