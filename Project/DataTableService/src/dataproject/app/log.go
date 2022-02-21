package app

import (
	"bytes"
	"dataproject/common/config"
	"fmt"
	"os"
	"runtime"
	"strings"
	"time"

	"github.com/sirupsen/logrus"
)

type LogFormatter struct{}

func (s *LogFormatter) Format(entry *logrus.Entry) ([]byte, error) {

	var b *bytes.Buffer
	if entry.Buffer != nil {
		b = entry.Buffer
	} else {
		b = &bytes.Buffer{}
	}

	msg := fmt.Sprintf("[%s] [%s] %s", time.Now().Format("2006-01-02 15:04:05.000"), strings.ToUpper(entry.Level.String()), entry.Message)
	b.WriteString(msg)
	for k, v := range entry.Data {
		b.WriteByte(' ')
		b.WriteString(k)
		b.WriteByte('=')

		stringVal, ok := v.(string)
		if !ok {
			stringVal = fmt.Sprint(v)
		}
		b.WriteString(stringVal)
	}
	b.WriteByte('\n')

	return b.Bytes(), nil
}

func InitLogrus() {

	nowTime := time.Now()

	logFilePath := ""
	if runtime.GOOS == "windows" {
		logFilePath = config.Conf.WindowsLogPath
	} else {
		logFilePath = config.Conf.LinuxLogPath
	}
	logFilePath += "game_"
	logFilePath += nowTime.Format("20060102_150405")
	logFilePath += ".log"

	logrus.SetFormatter(new(LogFormatter)) //注册自定义格式

	file, err := os.OpenFile(logFilePath, os.O_CREATE|os.O_WRONLY|os.O_APPEND, 0666)
	if err == nil {
		logrus.SetOutput(file)
		// Add mysql log
		/*model.GameLogHook = hook.Default(common.DB(), "t_game_log",
			//hook.SetLevels(logrus.TraceLevel),
			hook.SetFilter(func(entry *logrus.Entry) *logrus.Entry {
				if _, ok := entry.Data[""]; ok {
					fmt.Println("entry : ", entry.Data[""])
				}
				return entry
			}))
		logrus.AddHook(model.GameLogHook)*/
		//defer model.GameLogHook.Flush()
		logrus.Info("Log Init Success")
	} else {
		logrus.Error(err)
	}
}
