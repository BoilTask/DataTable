package datatable

import (
	. "dataproject/datatable/datapacket"

	log "github.com/sirupsen/logrus"
)

var Manager = newDataTableManager()

var gameConfig *ConfigDataTable

func newDataTableManager() *dataTableManager {
	return &dataTableManager{}
}

type dataTableManager struct {
	//Don't edit the following content.SERVER_DATATABLE_DECLARE_START
	ConfigDataTableMap map[int32]ConfigDataTable
	ExampleDataTableMap map[int32]ExampleDataTable
	//Don't edit the above content.SERVER_DATATABLE_DECLARE_END
}

func Init() {
	//Don't edit the following content.SERVER_DATATABLE_REGISTER_START
	Manager.ConfigDataTableMap = InitConfigDataTable()
	Manager.ExampleDataTableMap = InitExampleDataTable()
	//Don't edit the above content.SERVER_DATATABLE_REGISTER_END

	intConfig()

	log.Info("DataTable Init Success!")
}

func intConfig() {
	gameConfig = GetConfigDataTable(100000000)
}

func GetGameConfig() *ConfigDataTable {
	return gameConfig
}

//Don't edit the following content.SERVER_DATATABLE_GET_START

func GetConfigDataTableMap() *map[int32]ConfigDataTable {
	return &Manager.ConfigDataTableMap
}

func GetConfigDataTable(DataId int32) *ConfigDataTable {
	res, ok := Manager.ConfigDataTableMap[DataId]
	if ok {
		return &res
	} else {
		return nil
	}
}

func GetExampleDataTableMap() *map[int32]ExampleDataTable {
	return &Manager.ExampleDataTableMap
}

func GetExampleDataTable(DataId int32) *ExampleDataTable {
	res, ok := Manager.ExampleDataTableMap[DataId]
	if ok {
		return &res
	} else {
		return nil
	}
}

//Don't edit the above content.SERVER_DATATABLE_GET_END
