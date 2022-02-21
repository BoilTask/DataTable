package config

import (
	"io/ioutil"

	"github.com/sirupsen/logrus"
	"gopkg.in/yaml.v2"
)

var ConfigProject *configProject

type configProject struct {
	Version string `yaml:"Version"`
}

func InitConfigProject(filename string) {
	yamlFile, err := ioutil.ReadFile(filename)
	if err != nil {
		logrus.Error(err)
		return
	}

	ConfigProject = &configProject{}
	err = yaml.Unmarshal(yamlFile, ConfigProject)
	if err != nil {
		logrus.Error(err)
	}
}
