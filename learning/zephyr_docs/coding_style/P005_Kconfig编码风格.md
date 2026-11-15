---
id: learning.zephyr-docs.coding-style.page-5
title: Kconfig编码风格
kind: reference
status: maintained
domains: [zephyr, documentation, style]
source_url: https://docs.zephyrproject.org/latest/contribute/style/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_Kconfig编码风格

原文：[官方页面](https://docs.zephyrproject.org/latest/contribute/style/kconfig.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 5.1\_指南目的

本指南说明 Zephyr 项目中 Kconfig 文件的编写风格。遵循这些规则，可以使代码库保持一致且易读，方便开发者理解和维护配置选项。下文通过示例说明正确的格式和命名约定。

## 5.2\_基本格式规则（Basic Formatting Rules）

- 每行不超过 100 列。
- 使用制表符缩进；`help` 条目的正文例外，应缩进一个制表符再加两个空格。
- 选项声明之间保留一个空行。
- 注释写成 `# Comment`，不要写成 `#Comment`。
- 每个顶层 `if` 和 `endif` 语句前后各插入一个空行。
- 文件以恰好一个换行符结束。

关于 `select` 等语句的用法，参见 [Kconfig 提示与最佳实践](../kconfig/P004_Kconfig技巧与最佳实践.md#kconfig-tips-and-tricks)。

持续集成（Continuous Integration，CI）通过 `KconfigFormat` 合规检查执行这些格式规则。也可以使用 `scripts/kconfig/kconfig_style.py` 在本地检查；脚本报告风格问题，传入目录时递归查找 Kconfig 文件：

```sh
./scripts/kconfig/kconfig_style.py path/to/Kconfig
./scripts/kconfig/kconfig_style.py drivers/sensor/
```

> 译注：以上检查命令从 Zephyr 源码根目录解析。第一行的 `path/to/Kconfig` 是待读者替换的文件路径，第二行检查已有的传感器驱动目录；选择对应分支即可。原文注释中的 `Comment` 表示“注释文字”。本批没有运行这些源码风格检查器。

## 5.3\_符号命名与结构（Symbol Naming and Structure）

以下示例展示 Kconfig 符号的命名和组织方式：

```kconfig
# Symbol to enable/disable the feature ("enabling symbol")
config ADC_AD405X
	bool "AD405X ADC driver"
	depends on DT_HAS_ADI_AD4052_ADC_ENABLED || DT_HAS_ADI_AD4050_ADC_ENABLED
	select SPI
	default y
	help
	  Enable ADC driver for AD405X.
```

译注——示例文字译文：注释说明它是启用或关闭某项功能的“启用符号（enabling symbol）”；提示文字为“AD405X ADC 驱动”，帮助文字为“启用 AD405X 的模数转换器（Analog-to-Digital Converter，ADC）驱动”。

```kconfig
# Symbol to enable/disable the feature ("enabling symbol")
menuconfig ADC_AD4114
	bool "AD4114 ADC driver"
	depends on DT_HAS_ADI_AD4114_ADC_ENABLED
	select SPI
	default y
	help
	  Enable the AD4114 ADC driver.

if ADC_AD4114

# Symbol to configure the behavior of the feature ("config symbol")
config ADC_AD4114_ACQUISITION_THREAD_STACK_SIZE
	int "Stack size for the data acquisition thread"
	default 512
	help
	  Size of the stack used for the internal data acquisition
	  thread.

# Symbol to configure the behavior of the feature ("config symbol")
config ADC_AD4114_ACQUISITION_THREAD_PRIO
	int "Priority for the data acquisition thread"
	default 0
	help
	  Priority level for the internal ADC data acquisition thread.

endif # ADC_AD4114
```

译注——第二个示例文字译文：`ADC_AD4114` 是启用符号，提示为“AD4114 ADC 驱动”，帮助为“启用 AD4114 ADC 驱动”。后续两个是配置功能行为的“配置符号（config symbol）”：`ADC_AD4114_ACQUISITION_THREAD_STACK_SIZE` 的提示为“数据采集线程的栈大小”，帮助为“内部数据采集线程所使用的栈大小”；`ADC_AD4114_ACQUISITION_THREAD_PRIO` 的提示为“数据采集线程的优先级”，帮助为“内部 ADC 数据采集线程的优先级”。数值与标识符保留原文。

### 5.3.1\_命名约定（Naming Conventions）

一般来说，同一组件的符号应与其他符号区分开，通常可以通过共同前缀实现。前缀可以是一个关键词；对于驱动等需要更精确区分的情况，也可以由多个关键词组成。

共同前缀通常标明符号所属的子系统或组件。启用符号的名称应由关键词组成，按范围从最通用到最具体的顺序提供上下文，例如“驱动类型 → 驱动名称”。启用符号的提示文字（prompt）采用同样的逻辑，但关键词顺序反过来。这样在用户界面（User Interface，UI）中可以按范围关键词筛选，更容易搜索符号。

如果启用符号依赖设备树节点，可以考虑依赖[自动生成的](../devicetree/P005_设备树与Kconfig.md#auto-dts-kconfig) `DT_HAS_<node>_ENABLED` 符号。根据设备树节点的兼容标识（compatible）构建复杂表达式时，应使用[自动定义的](../devicetree/P005_设备树与Kconfig.md#auto-dts-kconfig) `DT_COMPAT_VND_DEVICE`，不要手动定义一个值为 `vnd,device` 的变量。

各源码子树的格式如下。这里的 `/drivers` 等表示官方源码树内的位置：

| 子树 | 符号与提示的命名规则 |
| --- | --- |
| 驱动（Drivers，`/drivers`） | 符号使用 `{Driver Type}_{Driver Name}`；提示使用 `{Driver Name} {Driver Type} driver`，即“驱动名称、驱动类型、driver”。 |
| 传感器（Sensors，原文 `/drivers/sensors`） | 符号使用 `SENSOR_{Sensor Name}`；提示使用 `{Sensor Name} {Sensor Type} sensor driver`，即“传感器名称、传感器类型、sensor driver”。 |
| 架构（Architecture，`/arch`） | 很多符号由不同架构共享；新增前先检查其他架构中是否已有相似符号。 |
| 示例（Samples，`/samples`） | 使用 `SAMPLE_` 前缀，避免与外部模块冲突。 |
| 测试（Tests，`/tests`） | 使用 `TEST_` 前缀，避免与外部模块冲突。 |
| 开发板（Boards，`/boards`） | 使用 `BOARD_` 前缀。 |
| 片上系统（System on Chip，SoC，`/soc`） | 根据适用范围选择下面的前缀，避免与其他厂商及外部模块冲突。 |

SoC 符号选择最合适的前缀：

- 涉及同一厂商的多个家族（family）：`SOC_VENDOR_{SoC vendor}_`。
- 涉及整个家族：`SOC_FAMILY_{SoC family}_`。
- 涉及整个系列（series）：`SOC_SERIES_{SoC series}_`。
- 涉及特定 SoC：`SOC_{SoC}_`。

这些术语的定义，以及名称应从哪里取得，参见 [SoC 移植指南](../hardware/P002_SoC移植指南.md#soc-porting-guide)。

> 译注：本页原文传感器子树写作 `/drivers/sensors`；前面的检查命令和本仓库实际目录使用 [`drivers/sensor`](../../../drivers/sensor)。上表保留原文写法供对照，跟踪源码时使用实际目录。表内前导 `/` 是源码树位置的原文表示法，不是要求把文件存放到操作系统的根目录。

### 5.3.2\_示例（Examples）

> 注意：为简洁起见，原文说明下列示例只展示符号和提示行。

驱动示例：

```kconfig
config ADC_AD405X
	bool "AD405X ADC driver"

config CAN_MAX32
	bool "MAX32 CAN driver"

config I2C_EMUL
	bool "I2C emulator driver"
```

提示译文依次为“AD405X ADC 驱动”“MAX32 控制器局域网（Controller Area Network，CAN）驱动”“I2C 仿真器驱动”。

传感器示例：

```kconfig
config SENSOR_BMP581
	bool "BMP581 barometric pressure sensor driver"

config SENSOR_TMP007
	bool "TMP007 infrared thermopile sensor driver"

config SENSOR_LM75
	bool "LM75 temperature sensor driver"
```

提示译文依次为“BMP581 大气压力传感器驱动”“TMP007 红外热电堆传感器驱动”“LM75 温度传感器驱动”。

示例程序的配置：

```kconfig
config SAMPLE_LOCK
	bool "Locking feature"

config SAMPLE_TEMPERATURE_READINGS
	bool "Fetch readings from temperature sensor"
```

提示译文依次为“锁定功能”“获取温度传感器的读数”。

测试示例：

```kconfig
config TEST_ITERATIONS
	int "Number of times test should run"
	default 3
```

提示译文为“测试应运行的次数”。原例同时包含 `default 3`，这里也完整保留。

SoC 示例：

```kconfig
# This assumes the following soc.yml file for the vendor "hotel":
# family:
#   - name: alpha
#     series:
#       - name: foxtrot
#         socs:
#           - name: charlie

config SOC_VENDOR_HOTEL_FLASH_PREFETCH
	bool "Flash prefetch"

config SOC_FAMILY_ALPHA_JTAG_LOCK
	bool "Lock JTAG access"

config SOC_SERIES_FOXTROT_EMULATE_POWER_OFF
	bool "Emulate power off mode"

config SOC_CHARLIE_IMAGE_HEADER
	bool "Include image header"
```

注释译文为“这里假定厂商 `hotel` 的 `soc.yml` 文件具有以下内容”，随后给出 `alpha` 家族、`foxtrot` 系列和 `charlie` SoC 的层次。四项提示依次为“Flash 预取”“锁定 JTAG 访问”“模拟断电模式”“包含镜像头”。

## 5.4\_配置符号组织（Configuration Symbol Organization）

当某项功能使用配置符号来配置其行为时：

- 用 `menuconfig` 而不是 `config` 定义启用该功能的符号，即使配置符号没有提示文字也是如此。
- 将配置符号放在 `if` 语句内，以声明它们依赖启用符号；这会在用户界面中自动把它们分组到启用符号之下。
- 配置符号以启用符号的名称为前缀，表明作用范围和上下文。
- 配置符号的提示只描述其配置的内容，不重复范围关键词，因为界面中的分组已经提供了该上下文。

## 5.5\_文件组织（File Organization）

Kconfig 文件应靠近它所配置的源文件。对于较大的 Kconfig 文件，例如包含许多配置符号的文件，可以考虑将其中一部分符号分组到单独文件，再通过 `source` 指令导入，以提高可读性。


对应官方文档源码：[doc/contribute/style/kconfig.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/contribute/style/kconfig.rst)。

本仓库的[对应源码](../../../doc/contribute/style/kconfig.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="kconfig-style-guidelines"></a>
<a id="kconfig-style"></a>
<a id="basic-formatting-rules"></a>
<a id="symbol-naming-and-structure"></a>
<a id="naming-conventions"></a>
<a id="examples"></a>
<a id="configuration-symbol-organization"></a>
<a id="file-organization"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：设备树编码风格](P004_设备树编码风格.md) · [本模块主线目录](../reading/coding_style.md) · [全部主线](../reading/README.md) · [下一篇：命名规范](P006_命名规范.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P004_设备树编码风格.md) · [返回大纲](大纲.md) · [下一章](P006_命名规范.md)

</details>

<!-- reading-navigation:end -->
