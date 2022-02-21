//Exported by Tool, please don't edit this file directly.

package datatablepacket

import (
	"encoding/csv"
	"io"
	"dataproject/common/config"
	"dataproject/datatable/dataparse"
	"os"
)

type ConfigDataTable struct {
	DataId int32
	EnableGame bool
}

func InitConfigDataTable() map[int32]ConfigDataTable {
	file, err := os.Open(config.Conf.DataTablePath + "/ConfigDataTable.csv")
	defer file.Close()
	if err != nil {
		return nil
	}
	ConfigDataTableMap := make(map[int32]ConfigDataTable)
	firstLine := true
	reader := csv.NewReader(file)
	for {
		line, err := reader.Read()
		if err == io.EOF {
			break
		}
		if err != nil {
			return nil
		}
		if firstLine {
			firstLine = false
			continue
		}
		DataId := dataparse.ParseInt32(line[1])
		ConfigDataTableMap[DataId] = ConfigDataTable{
			dataparse.ParseInt32(line[1]),
			dataparse.ParseBool(line[2]),
		}
	}
	return ConfigDataTableMap
}
