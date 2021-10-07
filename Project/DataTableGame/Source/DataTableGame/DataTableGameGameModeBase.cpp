// Copyright Epic Games, Inc. All Rights Reserved.


#include "DataTableGameGameModeBase.h"

#include "DataTableManager.h"

void ADataTableGameGameModeBase::InitGameState()
{
	UDataTableManager::GetInstance().TestDataTable();
}
