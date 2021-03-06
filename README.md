# DataTable

### 项目介绍

一个为游戏项目设计的配置系统，可供策划配置游戏中相关参数。

本项目使用的`csv`格式参考`unreal engine`（`UE4.25`）中数据表格配置。

可调整`Export.py`与`data_csv_parser.cpp`等文件以满足自身项目所需。

### 文件目录

- DataTable，使用的配置表，可使用`Excel`等软件打开。
  - Export，导出的`.csv`文件将放于此处。
  - Tool，导出脚本与配置等文件放于此处。
- Project，提供的演示项目。
  - DataTable，生成的代码文件将放于此处。
- Build，编译生成示例项目成功后，可执行文件将放于此处。

### 项目环境

项目使用`Windows10` + `VS2019`开发，但在`Ubuntu`平台测试成功，可根据需要配置所需环境。

导出脚本通过`Python3`运行，需要提前安装。

脚本使用了`xlrd`库，可通过`Tool/Install.bat`安装。

Excel表需要使用支持宏的版本打开，并根据需要修改代码。

### 使用说明

#### 数据类型

本项目目前支持的数据类型如下：

- bool
- int32
- float
- string
- bit
- vector\<bool\>
- vector\<int32\>
- vector\<float>\>
- vector\<string\>

通过修改导出脚本与解析代码，可较为便捷的添加新类型。

#### 字符转义

本项目遵照UE4.25字符格式对文本进行解析，脚本输出的文件编码为UTF-8。

在Excel配置时，除了字符数组之外的可直接按照原文配置，不需要考虑转义。

字符数组中，需要使用两个双引号将数组元素包围，表示此为一个元素。如数组元素中需要使用双引号，应使用`\"`来表示。如数组元素中需要使用`\`，应使用`\\`来表示。

脚本生成`.csv`时，会根据需要，对数据表按照规则进行一次转义。

具体规则可参考示例配置表。

#### 修改配置

配置路径：`DataTable\Tool\Config.json`

打开对应配置表，修改后导出数据即可。

若需要新增列，则按照格式在其后新增，并生成代码文件且导出数据。

#### 新增配表

- 复制出一张新表
- 按照格式修改信息
- 在`Config.json`中添加配置项
- 运行`Export.bat`选择`0.All`并执行`register_datatable`
- 运行`Export.bat`选择对应表并执行`generate_code & export_data`

#### 配置使用

使用宏定义的语句，填入表名与数据ID，若有效，即可返回配置的数据类。
