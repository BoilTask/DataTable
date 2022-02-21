//Exported by Tool, please don't edit this file directly.

package datatablepacket

import (
	"encoding/csv"
	"io"
	"dataproject/common/config"
	"dataproject/datatable/dataenum"
	"dataproject/datatable/dataparse"
	"os"
)

type ExampleDataTable struct {
	DataId int32
	BoolType bool
	Int32Type int32
	FloatType float32
	StringType string
	BitType int32
	EnumType dataenum.EEnumType
	VectorBoolType []bool
	VectorInt32Type []int32
	VectorFloatType []float32
	VectorStringType []string
	EnumTypeList []dataenum.EEnumType
	VectorIndexBoolType []bool
	VectorIndexStringType []string
	FillPluginInt int32
	FillPluginInt32 []int32
	AddPlugin float32
}

func InitExampleDataTable() map[int32]ExampleDataTable {
	file, err := os.Open(config.Conf.DataTablePath + "/ExampleDataTable.csv")
	defer file.Close()
	if err != nil {
		return nil
	}
	ExampleDataTableMap := make(map[int32]ExampleDataTable)
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
		ExampleDataTableMap[DataId] = ExampleDataTable{
			dataparse.ParseInt32(line[1]),
			dataparse.ParseBool(line[2]),
			dataparse.ParseInt32(line[3]),
			dataparse.ParseFloat32(line[4]),
			dataparse.ParseString(line[5]),
			dataparse.ParseInt32(line[6]),
			dataparse.ParseEnumEEnumType(line[7]),
			dataparse.ParseVectorBool(line[8]),
			dataparse.ParseVectorInt32(line[9]),
			dataparse.ParseVectorFloat32(line[10]),
			dataparse.ParseVectorString(line[11]),
			dataparse.ParseVectorEnumEEnumType(line[12]),
			dataparse.ParseVectorBool(line[13]),
			dataparse.ParseVectorString(line[14]),
			dataparse.ParseInt32(line[15]),
			dataparse.ParseVectorInt32(line[16]),
			dataparse.ParseFloat32(line[17]),
		}
	}
	return ExampleDataTableMap
}
