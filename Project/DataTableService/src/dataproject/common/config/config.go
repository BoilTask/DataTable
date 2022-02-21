package config

import (
	"io/ioutil"

	"github.com/sirupsen/logrus"
	"gopkg.in/yaml.v2"
)

var Conf *Config

type Config struct {
	LinuxLogPath   string `yaml:"LinuxLogPath"`   // 日志文件
	WindowsLogPath string `yaml:"WindowsLogPath"` // 日志文件
	DataTablePath  string `yaml:"DataTablePath"`  // 数值配置
}

func InitConfig(filename string) {
	yamlFile, err := ioutil.ReadFile(filename)
	if err != nil {
		logrus.Error(err)
		return
	}

	Conf = &Config{}
	err = yaml.Unmarshal(yamlFile, Conf)
	if err != nil {
		logrus.Error(err)
	}
}
