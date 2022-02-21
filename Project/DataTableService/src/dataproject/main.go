package main

import (
	"dataproject/app"
	"dataproject/common/config"
	"dataproject/datatable"
	"flag"

	log "github.com/sirupsen/logrus"
)

var configDeployFile = flag.String("config-deploy", "./config/deploy_config.yaml", "部署配置文件路径")

func init() {
	// 初始化配置
	config.InitConfig(*configDeployFile)

	// 初始化日志
	app.InitLogrus()

	//初始化数值配置
	datatable.Init()
}

func main() {

	data := datatable.GetExampleDataTable(900000000)

	if data == nil {
		log.Error("DataTable Error!")
	} else {

		println(data.DataId)
		println(data.BoolType)
		println(data.Int32Type)
		println(data.FloatType)
		println(data.StringType)
		println(data.BitType)
		println(data.EnumType)

		for i, v := range data.VectorBoolType {
			print(v)
			if i == len(data.VectorBoolType)-1 {
				println()
			} else {
				print(" ")
			}
		}

		for i, v := range data.VectorInt32Type {
			print(v)
			if i == len(data.VectorInt32Type)-1 {
				println()
			} else {
				print(" ")
			}
		}

		for i, v := range data.VectorFloatType {
			print(v)
			if i == len(data.VectorFloatType)-1 {
				println()
			} else {
				print(" ")
			}
		}

		for i, v := range data.VectorStringType {
			print(v)
			if i == len(data.VectorStringType)-1 {
				println()
			} else {
				print(" ")
			}
		}

		for i, v := range data.EnumTypeList {
			print(v)
			if i == len(data.EnumTypeList)-1 {
				println()
			} else {
				print(" ")
			}
		}

		for i, v := range data.VectorIndexBoolType {
			print(v)
			if i == len(data.VectorIndexBoolType)-1 {
				println()
			} else {
				print(" ")
			}
		}

		for i, v := range data.VectorIndexStringType {
			print(v)
			if i == len(data.VectorIndexStringType)-1 {
				println()
			} else {
				print(" ")
			}
		}

		println(data.FillPluginInt)

		for i, v := range data.FillPluginInt32 {
			print(v)
			if i == len(data.FillPluginInt32)-1 {
				println()
			} else {
				print(" ")
			}
		}

		println(data.AddPlugin)
	}

}
