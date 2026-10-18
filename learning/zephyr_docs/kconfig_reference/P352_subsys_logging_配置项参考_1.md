---
id: learning.zephyr-docs.kconfig-reference.page-352
title: "`subsys/logging`配置项参考（1/30）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第352章\_`subsys/logging`配置项参考（1/30）

本章翻译官方 Kconfig 数据库中 `subsys/logging` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_ACPI_LOG_LEVEL_CHOICE"></a>

## 352.1 `CONFIG_ACPI_LOG_LEVEL_CHOICE`

**提示（Prompt）**：高级配置与电源接口（acpi）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_ACPI
```

**默认值（Defaults）**

```text
CONFIG_ACPI_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_ACPI_LOG_LEVEL_OFF
CONFIG_ACPI_LOG_LEVEL_ERR
CONFIG_ACPI_LOG_LEVEL_WRN
CONFIG_ACPI_LOG_LEVEL_INF
CONFIG_ACPI_LOG_LEVEL_DBG
CONFIG_ACPI_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options） → 高级配置与电源接口（ACPI）支持

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_ACPI`](P032_arch_common_配置项参考.md#CONFIG_ACPI)、[`CONFIG_ACPI_LOG_LEVEL_DEFAULT`](P352_subsys_logging_配置项参考_1.md#CONFIG_ACPI_LOG_LEVEL_DEFAULT)、[`CONFIG_ACPI_LOG_LEVEL_OFF`](P352_subsys_logging_配置项参考_1.md#CONFIG_ACPI_LOG_LEVEL_OFF)、[`CONFIG_ACPI_LOG_LEVEL_ERR`](P352_subsys_logging_配置项参考_1.md#CONFIG_ACPI_LOG_LEVEL_ERR)、[`CONFIG_ACPI_LOG_LEVEL_WRN`](P352_subsys_logging_配置项参考_1.md#CONFIG_ACPI_LOG_LEVEL_WRN)、[`CONFIG_ACPI_LOG_LEVEL_INF`](P352_subsys_logging_配置项参考_1.md#CONFIG_ACPI_LOG_LEVEL_INF)、[`CONFIG_ACPI_LOG_LEVEL_DBG`](P352_subsys_logging_配置项参考_1.md#CONFIG_ACPI_LOG_LEVEL_DBG)。

<a id="CONFIG_ACPI_LOG_LEVEL_DBG"></a>

## 352.2 `CONFIG_ACPI_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ACPI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options） → 高级配置与电源接口（ACPI）支持 → 高级配置与电源接口（acpi）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ACPI_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_ACPI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ACPI_LOG_LEVEL_DEFAULT"></a>

## 352.3 `CONFIG_ACPI_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ACPI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options） → 高级配置与电源接口（ACPI）支持 → 高级配置与电源接口（acpi）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ACPI_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_ACPI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ACPI_LOG_LEVEL_ERR"></a>

## 352.4 `CONFIG_ACPI_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ACPI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options） → 高级配置与电源接口（ACPI）支持 → 高级配置与电源接口（acpi）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ACPI_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_ACPI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ACPI_LOG_LEVEL_INF"></a>

## 352.5 `CONFIG_ACPI_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ACPI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options） → 高级配置与电源接口（ACPI）支持 → 高级配置与电源接口（acpi）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ACPI_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_ACPI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ACPI_LOG_LEVEL_OFF"></a>

## 352.6 `CONFIG_ACPI_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ACPI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options） → 高级配置与电源接口（ACPI）支持 → 高级配置与电源接口（acpi）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ACPI_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_ACPI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ACPI_LOG_LEVEL_WRN"></a>

## 352.7 `CONFIG_ACPI_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ACPI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options） → 高级配置与电源接口（ACPI）支持 → 高级配置与电源接口（acpi）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ACPI_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_ACPI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ADC_LOG_LEVEL_CHOICE"></a>

## 352.8 `CONFIG_ADC_LOG_LEVEL_CHOICE`

**提示（Prompt）**：模数转换器（ADC）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_ADC
```

**默认值（Defaults）**

```text
CONFIG_ADC_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_ADC_LOG_LEVEL_OFF
CONFIG_ADC_LOG_LEVEL_ERR
CONFIG_ADC_LOG_LEVEL_WRN
CONFIG_ADC_LOG_LEVEL_INF
CONFIG_ADC_LOG_LEVEL_DBG
CONFIG_ADC_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)、[`CONFIG_ADC_LOG_LEVEL_DEFAULT`](P352_subsys_logging_配置项参考_1.md#CONFIG_ADC_LOG_LEVEL_DEFAULT)、[`CONFIG_ADC_LOG_LEVEL_OFF`](P352_subsys_logging_配置项参考_1.md#CONFIG_ADC_LOG_LEVEL_OFF)、[`CONFIG_ADC_LOG_LEVEL_ERR`](P352_subsys_logging_配置项参考_1.md#CONFIG_ADC_LOG_LEVEL_ERR)、[`CONFIG_ADC_LOG_LEVEL_WRN`](P352_subsys_logging_配置项参考_1.md#CONFIG_ADC_LOG_LEVEL_WRN)、[`CONFIG_ADC_LOG_LEVEL_INF`](P352_subsys_logging_配置项参考_1.md#CONFIG_ADC_LOG_LEVEL_INF)、[`CONFIG_ADC_LOG_LEVEL_DBG`](P352_subsys_logging_配置项参考_1.md#CONFIG_ADC_LOG_LEVEL_DBG)。

<a id="CONFIG_ADC_LOG_LEVEL_DBG"></a>

## 352.9 `CONFIG_ADC_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ADC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → 模数转换器（ADC）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ADC_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_ADC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ADC_LOG_LEVEL_DEFAULT"></a>

## 352.10 `CONFIG_ADC_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ADC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → 模数转换器（ADC）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ADC_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_ADC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ADC_LOG_LEVEL_ERR"></a>

## 352.11 `CONFIG_ADC_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ADC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → 模数转换器（ADC）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ADC_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_ADC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ADC_LOG_LEVEL_INF"></a>

## 352.12 `CONFIG_ADC_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ADC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → 模数转换器（ADC）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ADC_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_ADC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ADC_LOG_LEVEL_OFF"></a>

## 352.13 `CONFIG_ADC_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ADC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → 模数转换器（ADC）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ADC_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_ADC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ADC_LOG_LEVEL_WRN"></a>

## 352.14 `CONFIG_ADC_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ADC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 模数转换器驱动（Analog-to-Digital Converter，ADC） → 模数转换器（ADC）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ADC_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_ADC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ARCH_LOG_LEVEL_CHOICE"></a>

## 352.15 `CONFIG_ARCH_LOG_LEVEL_CHOICE`

**提示（Prompt）**：体系结构（arch）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG
```

**默认值（Defaults）**

```text
CONFIG_ARCH_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_ARCH_LOG_LEVEL_OFF
CONFIG_ARCH_LOG_LEVEL_ERR
CONFIG_ARCH_LOG_LEVEL_WRN
CONFIG_ARCH_LOG_LEVEL_INF
CONFIG_ARCH_LOG_LEVEL_DBG
CONFIG_ARCH_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_ARCH_LOG_LEVEL_DEFAULT`](P352_subsys_logging_配置项参考_1.md#CONFIG_ARCH_LOG_LEVEL_DEFAULT)、[`CONFIG_ARCH_LOG_LEVEL_OFF`](P352_subsys_logging_配置项参考_1.md#CONFIG_ARCH_LOG_LEVEL_OFF)、[`CONFIG_ARCH_LOG_LEVEL_ERR`](P352_subsys_logging_配置项参考_1.md#CONFIG_ARCH_LOG_LEVEL_ERR)、[`CONFIG_ARCH_LOG_LEVEL_WRN`](P352_subsys_logging_配置项参考_1.md#CONFIG_ARCH_LOG_LEVEL_WRN)、[`CONFIG_ARCH_LOG_LEVEL_INF`](P352_subsys_logging_配置项参考_1.md#CONFIG_ARCH_LOG_LEVEL_INF)、[`CONFIG_ARCH_LOG_LEVEL_DBG`](P352_subsys_logging_配置项参考_1.md#CONFIG_ARCH_LOG_LEVEL_DBG)。

<a id="CONFIG_ARCH_LOG_LEVEL_DBG"></a>

## 352.16 `CONFIG_ARCH_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ARCH_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options） → 体系结构（arch）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_ARCH_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ARCH_LOG_LEVEL_DEFAULT"></a>

## 352.17 `CONFIG_ARCH_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ARCH_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options） → 体系结构（arch）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_ARCH_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ARCH_LOG_LEVEL_ERR"></a>

## 352.18 `CONFIG_ARCH_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ARCH_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options） → 体系结构（arch）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_ARCH_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ARCH_LOG_LEVEL_INF"></a>

## 352.19 `CONFIG_ARCH_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ARCH_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options） → 体系结构（arch）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_ARCH_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ARCH_LOG_LEVEL_OFF"></a>

## 352.20 `CONFIG_ARCH_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ARCH_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options） → 体系结构（arch）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_ARCH_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ARCH_LOG_LEVEL_WRN"></a>

## 352.21 `CONFIG_ARCH_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ARCH_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 通用架构选项（General Architecture Options） → 体系结构（arch）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_ARCH_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ARM64_PMUV3_LOG_LEVEL_CHOICE"></a>

## 352.22 `CONFIG_ARM64_PMUV3_LOG_LEVEL_CHOICE`

**提示（Prompt）**：ARM64 性能监控单元 v3（ARM64 PMUv3）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_ARM64_PMUV3 && (CONFIG_CPU_CORTEX_A || CONFIG_CPU_AARCH64_CORTEX_R) && CONFIG_ARM64
```

**默认值（Defaults）**

```text
CONFIG_ARM64_PMUV3_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_ARM64_PMUV3_LOG_LEVEL_OFF
CONFIG_ARM64_PMUV3_LOG_LEVEL_ERR
CONFIG_ARM64_PMUV3_LOG_LEVEL_WRN
CONFIG_ARM64_PMUV3_LOG_LEVEL_INF
CONFIG_ARM64_PMUV3_LOG_LEVEL_DBG
CONFIG_ARM64_PMUV3_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options） → ARMv8-A PMUv3 支持

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_ARM64_PMUV3`](P031_arch_arm64_配置项参考.md#CONFIG_ARM64_PMUV3)、[`CONFIG_CPU_CORTEX_A`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_CORTEX_A)、[`CONFIG_CPU_AARCH64_CORTEX_R`](P031_arch_arm64_配置项参考.md#CONFIG_CPU_AARCH64_CORTEX_R)、[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)、[`CONFIG_ARM64_PMUV3_LOG_LEVEL_DEFAULT`](P352_subsys_logging_配置项参考_1.md#CONFIG_ARM64_PMUV3_LOG_LEVEL_DEFAULT)、[`CONFIG_ARM64_PMUV3_LOG_LEVEL_OFF`](P352_subsys_logging_配置项参考_1.md#CONFIG_ARM64_PMUV3_LOG_LEVEL_OFF)、[`CONFIG_ARM64_PMUV3_LOG_LEVEL_ERR`](P352_subsys_logging_配置项参考_1.md#CONFIG_ARM64_PMUV3_LOG_LEVEL_ERR)、[`CONFIG_ARM64_PMUV3_LOG_LEVEL_WRN`](P352_subsys_logging_配置项参考_1.md#CONFIG_ARM64_PMUV3_LOG_LEVEL_WRN)、[`CONFIG_ARM64_PMUV3_LOG_LEVEL_INF`](P352_subsys_logging_配置项参考_1.md#CONFIG_ARM64_PMUV3_LOG_LEVEL_INF)、[`CONFIG_ARM64_PMUV3_LOG_LEVEL_DBG`](P352_subsys_logging_配置项参考_1.md#CONFIG_ARM64_PMUV3_LOG_LEVEL_DBG)。

<a id="CONFIG_ARM64_PMUV3_LOG_LEVEL_DBG"></a>

## 352.23 `CONFIG_ARM64_PMUV3_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ARM64_PMUV3_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options） → ARMv8-A PMUv3 支持 → ARM64 性能监控单元 v3（ARM64 PMUv3）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ARM64_PMUV3_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_ARM64_PMUV3_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ARM64_PMUV3_LOG_LEVEL_DEFAULT"></a>

## 352.24 `CONFIG_ARM64_PMUV3_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ARM64_PMUV3_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options） → ARMv8-A PMUv3 支持 → ARM64 性能监控单元 v3（ARM64 PMUv3）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ARM64_PMUV3_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_ARM64_PMUV3_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ARM64_PMUV3_LOG_LEVEL_ERR"></a>

## 352.25 `CONFIG_ARM64_PMUV3_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ARM64_PMUV3_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options） → ARMv8-A PMUv3 支持 → ARM64 性能监控单元 v3（ARM64 PMUv3）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ARM64_PMUV3_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_ARM64_PMUV3_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ARM64_PMUV3_LOG_LEVEL_INF"></a>

## 352.26 `CONFIG_ARM64_PMUV3_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ARM64_PMUV3_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options） → ARMv8-A PMUv3 支持 → ARM64 性能监控单元 v3（ARM64 PMUv3）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ARM64_PMUV3_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_ARM64_PMUV3_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ARM64_PMUV3_LOG_LEVEL_OFF"></a>

## 352.27 `CONFIG_ARM64_PMUV3_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ARM64_PMUV3_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options） → ARMv8-A PMUv3 支持 → ARM64 性能监控单元 v3（ARM64 PMUv3）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ARM64_PMUV3_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_ARM64_PMUV3_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ARM64_PMUV3_LOG_LEVEL_WRN"></a>

## 352.28 `CONFIG_ARM64_PMUV3_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ARM64_PMUV3_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → ARM64 选项（Options） → ARMv8-A PMUv3 支持 → ARM64 性能监控单元 v3（ARM64 PMUv3）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ARM64_PMUV3_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_ARM64_PMUV3_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ARM_SIP_SVC_DRIVER_LOG_LEVEL_CHOICE"></a>

## 352.29 `CONFIG_ARM_SIP_SVC_DRIVER_LOG_LEVEL_CHOICE`

**提示（Prompt）**：ARM SiP SVC 驱动（arm_sip_svc_driver）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_ARM_SIP_SVC_DRIVER
```

**默认值（Defaults）**

```text
CONFIG_ARM_SIP_SVC_DRIVER_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_ARM_SIP_SVC_DRIVER_LOG_LEVEL_OFF
CONFIG_ARM_SIP_SVC_DRIVER_LOG_LEVEL_ERR
CONFIG_ARM_SIP_SVC_DRIVER_LOG_LEVEL_WRN
CONFIG_ARM_SIP_SVC_DRIVER_LOG_LEVEL_INF
CONFIG_ARM_SIP_SVC_DRIVER_LOG_LEVEL_DBG
CONFIG_ARM_SIP_SVC_DRIVER_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → ARM SiP 服务调用（SIP SVC）驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_ARM_SIP_SVC_DRIVER`](P170_drivers_sip_svc_配置项参考.md#CONFIG_ARM_SIP_SVC_DRIVER)、[`CONFIG_ARM_SIP_SVC_DRIVER_LOG_LEVEL_DEFAULT`](P352_subsys_logging_配置项参考_1.md#CONFIG_ARM_SIP_SVC_DRIVER_LOG_LEVEL_DEFAULT)、[`CONFIG_ARM_SIP_SVC_DRIVER_LOG_LEVEL_OFF`](P352_subsys_logging_配置项参考_1.md#CONFIG_ARM_SIP_SVC_DRIVER_LOG_LEVEL_OFF)、[`CONFIG_ARM_SIP_SVC_DRIVER_LOG_LEVEL_ERR`](P352_subsys_logging_配置项参考_1.md#CONFIG_ARM_SIP_SVC_DRIVER_LOG_LEVEL_ERR)、[`CONFIG_ARM_SIP_SVC_DRIVER_LOG_LEVEL_WRN`](P352_subsys_logging_配置项参考_1.md#CONFIG_ARM_SIP_SVC_DRIVER_LOG_LEVEL_WRN)、[`CONFIG_ARM_SIP_SVC_DRIVER_LOG_LEVEL_INF`](P352_subsys_logging_配置项参考_1.md#CONFIG_ARM_SIP_SVC_DRIVER_LOG_LEVEL_INF)、[`CONFIG_ARM_SIP_SVC_DRIVER_LOG_LEVEL_DBG`](P352_subsys_logging_配置项参考_1.md#CONFIG_ARM_SIP_SVC_DRIVER_LOG_LEVEL_DBG)。

<a id="CONFIG_ARM_SIP_SVC_DRIVER_LOG_LEVEL_DBG"></a>

## 352.30 `CONFIG_ARM_SIP_SVC_DRIVER_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ARM_SIP_SVC_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → ARM SiP 服务调用（SIP SVC）驱动 → ARM SiP SVC 驱动（arm_sip_svc_driver）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ARM_SIP_SVC_DRIVER_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_ARM_SIP_SVC_DRIVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ARM_SIP_SVC_DRIVER_LOG_LEVEL_DEFAULT"></a>

## 352.31 `CONFIG_ARM_SIP_SVC_DRIVER_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ARM_SIP_SVC_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → ARM SiP 服务调用（SIP SVC）驱动 → ARM SiP SVC 驱动（arm_sip_svc_driver）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ARM_SIP_SVC_DRIVER_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_ARM_SIP_SVC_DRIVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ARM_SIP_SVC_DRIVER_LOG_LEVEL_ERR"></a>

## 352.32 `CONFIG_ARM_SIP_SVC_DRIVER_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ARM_SIP_SVC_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → ARM SiP 服务调用（SIP SVC）驱动 → ARM SiP SVC 驱动（arm_sip_svc_driver）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ARM_SIP_SVC_DRIVER_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_ARM_SIP_SVC_DRIVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ARM_SIP_SVC_DRIVER_LOG_LEVEL_INF"></a>

## 352.33 `CONFIG_ARM_SIP_SVC_DRIVER_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ARM_SIP_SVC_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → ARM SiP 服务调用（SIP SVC）驱动 → ARM SiP SVC 驱动（arm_sip_svc_driver）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ARM_SIP_SVC_DRIVER_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_ARM_SIP_SVC_DRIVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ARM_SIP_SVC_DRIVER_LOG_LEVEL_OFF"></a>

## 352.34 `CONFIG_ARM_SIP_SVC_DRIVER_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ARM_SIP_SVC_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → ARM SiP 服务调用（SIP SVC）驱动 → ARM SiP SVC 驱动（arm_sip_svc_driver）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ARM_SIP_SVC_DRIVER_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_ARM_SIP_SVC_DRIVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ARM_SIP_SVC_DRIVER_LOG_LEVEL_WRN"></a>

## 352.35 `CONFIG_ARM_SIP_SVC_DRIVER_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ARM_SIP_SVC_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → ARM SiP 服务调用（SIP SVC）驱动 → ARM SiP SVC 驱动（arm_sip_svc_driver）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ARM_SIP_SVC_DRIVER_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_ARM_SIP_SVC_DRIVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ARM_SIP_SVC_SUBSYS_LOG_LEVEL_CHOICE"></a>

## 352.36 `CONFIG_ARM_SIP_SVC_SUBSYS_LOG_LEVEL_CHOICE`

**提示（Prompt）**：ARM SiP SVC 子系统（arm_sip_svc_subsys）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_ARM_SIP_SVC_SUBSYS
```

**默认值（Defaults）**

```text
CONFIG_ARM_SIP_SVC_SUBSYS_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_ARM_SIP_SVC_SUBSYS_LOG_LEVEL_OFF
CONFIG_ARM_SIP_SVC_SUBSYS_LOG_LEVEL_ERR
CONFIG_ARM_SIP_SVC_SUBSYS_LOG_LEVEL_WRN
CONFIG_ARM_SIP_SVC_SUBSYS_LOG_LEVEL_INF
CONFIG_ARM_SIP_SVC_SUBSYS_LOG_LEVEL_DBG
CONFIG_ARM_SIP_SVC_SUBSYS_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ARM SiP SVC 服务（Service）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_ARM_SIP_SVC_SUBSYS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM_SIP_SVC_SUBSYS)、[`CONFIG_ARM_SIP_SVC_SUBSYS_LOG_LEVEL_DEFAULT`](P352_subsys_logging_配置项参考_1.md#CONFIG_ARM_SIP_SVC_SUBSYS_LOG_LEVEL_DEFAULT)、[`CONFIG_ARM_SIP_SVC_SUBSYS_LOG_LEVEL_OFF`](P352_subsys_logging_配置项参考_1.md#CONFIG_ARM_SIP_SVC_SUBSYS_LOG_LEVEL_OFF)、[`CONFIG_ARM_SIP_SVC_SUBSYS_LOG_LEVEL_ERR`](P352_subsys_logging_配置项参考_1.md#CONFIG_ARM_SIP_SVC_SUBSYS_LOG_LEVEL_ERR)、[`CONFIG_ARM_SIP_SVC_SUBSYS_LOG_LEVEL_WRN`](P352_subsys_logging_配置项参考_1.md#CONFIG_ARM_SIP_SVC_SUBSYS_LOG_LEVEL_WRN)、[`CONFIG_ARM_SIP_SVC_SUBSYS_LOG_LEVEL_INF`](P352_subsys_logging_配置项参考_1.md#CONFIG_ARM_SIP_SVC_SUBSYS_LOG_LEVEL_INF)、[`CONFIG_ARM_SIP_SVC_SUBSYS_LOG_LEVEL_DBG`](P352_subsys_logging_配置项参考_1.md#CONFIG_ARM_SIP_SVC_SUBSYS_LOG_LEVEL_DBG)。

<a id="CONFIG_ARM_SIP_SVC_SUBSYS_LOG_LEVEL_DBG"></a>

## 352.37 `CONFIG_ARM_SIP_SVC_SUBSYS_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ARM_SIP_SVC_SUBSYS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ARM SiP SVC 服务（Service） → ARM SiP SVC 子系统（arm_sip_svc_subsys）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ARM_SIP_SVC_SUBSYS_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_ARM_SIP_SVC_SUBSYS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ARM_SIP_SVC_SUBSYS_LOG_LEVEL_DEFAULT"></a>

## 352.38 `CONFIG_ARM_SIP_SVC_SUBSYS_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ARM_SIP_SVC_SUBSYS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ARM SiP SVC 服务（Service） → ARM SiP SVC 子系统（arm_sip_svc_subsys）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ARM_SIP_SVC_SUBSYS_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_ARM_SIP_SVC_SUBSYS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ARM_SIP_SVC_SUBSYS_LOG_LEVEL_ERR"></a>

## 352.39 `CONFIG_ARM_SIP_SVC_SUBSYS_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ARM_SIP_SVC_SUBSYS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ARM SiP SVC 服务（Service） → ARM SiP SVC 子系统（arm_sip_svc_subsys）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ARM_SIP_SVC_SUBSYS_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_ARM_SIP_SVC_SUBSYS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ARM_SIP_SVC_SUBSYS_LOG_LEVEL_INF"></a>

## 352.40 `CONFIG_ARM_SIP_SVC_SUBSYS_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ARM_SIP_SVC_SUBSYS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ARM SiP SVC 服务（Service） → ARM SiP SVC 子系统（arm_sip_svc_subsys）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ARM_SIP_SVC_SUBSYS_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_ARM_SIP_SVC_SUBSYS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ARM_SIP_SVC_SUBSYS_LOG_LEVEL_OFF"></a>

## 352.41 `CONFIG_ARM_SIP_SVC_SUBSYS_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ARM_SIP_SVC_SUBSYS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ARM SiP SVC 服务（Service） → ARM SiP SVC 子系统（arm_sip_svc_subsys）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ARM_SIP_SVC_SUBSYS_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_ARM_SIP_SVC_SUBSYS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ARM_SIP_SVC_SUBSYS_LOG_LEVEL_WRN"></a>

## 352.42 `CONFIG_ARM_SIP_SVC_SUBSYS_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ARM_SIP_SVC_SUBSYS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ARM SiP SVC 服务（Service） → ARM SiP SVC 子系统（arm_sip_svc_subsys）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ARM_SIP_SVC_SUBSYS_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_ARM_SIP_SVC_SUBSYS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_AUDIO_CODEC_LOG_LEVEL_CHOICE"></a>

## 352.43 `CONFIG_AUDIO_CODEC_LOG_LEVEL_CHOICE`

**提示（Prompt）**：音频编解码器（audio codec）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_AUDIO_CODEC && CONFIG_AUDIO
```

**默认值（Defaults）**

```text
CONFIG_AUDIO_CODEC_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_AUDIO_CODEC_LOG_LEVEL_OFF
CONFIG_AUDIO_CODEC_LOG_LEVEL_ERR
CONFIG_AUDIO_CODEC_LOG_LEVEL_WRN
CONFIG_AUDIO_CODEC_LOG_LEVEL_INF
CONFIG_AUDIO_CODEC_LOG_LEVEL_DBG
CONFIG_AUDIO_CODEC_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 音频编解码器驱动（Audio Codec Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_AUDIO_CODEC`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_CODEC)、[`CONFIG_AUDIO`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO)、[`CONFIG_AUDIO_CODEC_LOG_LEVEL_DEFAULT`](P352_subsys_logging_配置项参考_1.md#CONFIG_AUDIO_CODEC_LOG_LEVEL_DEFAULT)、[`CONFIG_AUDIO_CODEC_LOG_LEVEL_OFF`](P352_subsys_logging_配置项参考_1.md#CONFIG_AUDIO_CODEC_LOG_LEVEL_OFF)、[`CONFIG_AUDIO_CODEC_LOG_LEVEL_ERR`](P352_subsys_logging_配置项参考_1.md#CONFIG_AUDIO_CODEC_LOG_LEVEL_ERR)、[`CONFIG_AUDIO_CODEC_LOG_LEVEL_WRN`](P352_subsys_logging_配置项参考_1.md#CONFIG_AUDIO_CODEC_LOG_LEVEL_WRN)、[`CONFIG_AUDIO_CODEC_LOG_LEVEL_INF`](P352_subsys_logging_配置项参考_1.md#CONFIG_AUDIO_CODEC_LOG_LEVEL_INF)、[`CONFIG_AUDIO_CODEC_LOG_LEVEL_DBG`](P352_subsys_logging_配置项参考_1.md#CONFIG_AUDIO_CODEC_LOG_LEVEL_DBG)。

<a id="CONFIG_AUDIO_CODEC_LOG_LEVEL_DBG"></a>

## 352.44 `CONFIG_AUDIO_CODEC_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_AUDIO_CODEC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 音频编解码器驱动（Audio Codec Drivers） → 音频编解码器（audio codec）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO_CODEC_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_AUDIO_CODEC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_AUDIO_CODEC_LOG_LEVEL_DEFAULT"></a>

## 352.45 `CONFIG_AUDIO_CODEC_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_AUDIO_CODEC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 音频编解码器驱动（Audio Codec Drivers） → 音频编解码器（audio codec）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO_CODEC_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_AUDIO_CODEC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_AUDIO_CODEC_LOG_LEVEL_ERR"></a>

## 352.46 `CONFIG_AUDIO_CODEC_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_AUDIO_CODEC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 音频编解码器驱动（Audio Codec Drivers） → 音频编解码器（audio codec）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO_CODEC_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_AUDIO_CODEC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_AUDIO_CODEC_LOG_LEVEL_INF"></a>

## 352.47 `CONFIG_AUDIO_CODEC_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_AUDIO_CODEC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 音频编解码器驱动（Audio Codec Drivers） → 音频编解码器（audio codec）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO_CODEC_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_AUDIO_CODEC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_AUDIO_CODEC_LOG_LEVEL_OFF"></a>

## 352.48 `CONFIG_AUDIO_CODEC_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_AUDIO_CODEC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 音频编解码器驱动（Audio Codec Drivers） → 音频编解码器（audio codec）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO_CODEC_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_AUDIO_CODEC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_AUDIO_CODEC_LOG_LEVEL_WRN"></a>

## 352.49 `CONFIG_AUDIO_CODEC_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_AUDIO_CODEC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 音频编解码器驱动（Audio Codec Drivers） → 音频编解码器（audio codec）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO_CODEC_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_AUDIO_CODEC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_AUDIO_DMIC_LOG_LEVEL_CHOICE"></a>

## 352.50 `CONFIG_AUDIO_DMIC_LOG_LEVEL_CHOICE`

**提示（Prompt）**：数字麦克风音频（audio_dmic）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_AUDIO_DMIC && CONFIG_AUDIO
```

**默认值（Defaults）**

```text
CONFIG_AUDIO_DMIC_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_AUDIO_DMIC_LOG_LEVEL_OFF
CONFIG_AUDIO_DMIC_LOG_LEVEL_ERR
CONFIG_AUDIO_DMIC_LOG_LEVEL_WRN
CONFIG_AUDIO_DMIC_LOG_LEVEL_INF
CONFIG_AUDIO_DMIC_LOG_LEVEL_DBG
CONFIG_AUDIO_DMIC_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 数字麦克风音频驱动（Digital Microphone Audio Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_AUDIO_DMIC`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC)、[`CONFIG_AUDIO`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO)、[`CONFIG_AUDIO_DMIC_LOG_LEVEL_DEFAULT`](P352_subsys_logging_配置项参考_1.md#CONFIG_AUDIO_DMIC_LOG_LEVEL_DEFAULT)、[`CONFIG_AUDIO_DMIC_LOG_LEVEL_OFF`](P352_subsys_logging_配置项参考_1.md#CONFIG_AUDIO_DMIC_LOG_LEVEL_OFF)、[`CONFIG_AUDIO_DMIC_LOG_LEVEL_ERR`](P352_subsys_logging_配置项参考_1.md#CONFIG_AUDIO_DMIC_LOG_LEVEL_ERR)、[`CONFIG_AUDIO_DMIC_LOG_LEVEL_WRN`](P352_subsys_logging_配置项参考_1.md#CONFIG_AUDIO_DMIC_LOG_LEVEL_WRN)、[`CONFIG_AUDIO_DMIC_LOG_LEVEL_INF`](P352_subsys_logging_配置项参考_1.md#CONFIG_AUDIO_DMIC_LOG_LEVEL_INF)、[`CONFIG_AUDIO_DMIC_LOG_LEVEL_DBG`](P352_subsys_logging_配置项参考_1.md#CONFIG_AUDIO_DMIC_LOG_LEVEL_DBG)。

<a id="CONFIG_AUDIO_DMIC_LOG_LEVEL_DBG"></a>

## 352.51 `CONFIG_AUDIO_DMIC_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_AUDIO_DMIC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 数字麦克风音频驱动（Digital Microphone Audio Drivers） → 数字麦克风音频（audio_dmic）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO_DMIC_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_AUDIO_DMIC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_AUDIO_DMIC_LOG_LEVEL_DEFAULT"></a>

## 352.52 `CONFIG_AUDIO_DMIC_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_AUDIO_DMIC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 数字麦克风音频驱动（Digital Microphone Audio Drivers） → 数字麦克风音频（audio_dmic）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO_DMIC_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_AUDIO_DMIC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_AUDIO_DMIC_LOG_LEVEL_ERR"></a>

## 352.53 `CONFIG_AUDIO_DMIC_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_AUDIO_DMIC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 数字麦克风音频驱动（Digital Microphone Audio Drivers） → 数字麦克风音频（audio_dmic）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO_DMIC_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_AUDIO_DMIC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_AUDIO_DMIC_LOG_LEVEL_INF"></a>

## 352.54 `CONFIG_AUDIO_DMIC_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_AUDIO_DMIC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 数字麦克风音频驱动（Digital Microphone Audio Drivers） → 数字麦克风音频（audio_dmic）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO_DMIC_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_AUDIO_DMIC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_AUDIO_DMIC_LOG_LEVEL_OFF"></a>

## 352.55 `CONFIG_AUDIO_DMIC_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_AUDIO_DMIC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 数字麦克风音频驱动（Digital Microphone Audio Drivers） → 数字麦克风音频（audio_dmic）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO_DMIC_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_AUDIO_DMIC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_AUDIO_DMIC_LOG_LEVEL_WRN"></a>

## 352.56 `CONFIG_AUDIO_DMIC_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_AUDIO_DMIC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 数字麦克风音频驱动（Digital Microphone Audio Drivers） → 数字麦克风音频（audio_dmic）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO_DMIC_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_AUDIO_DMIC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_AUXDISPLAY_LOG_LEVEL_CHOICE"></a>

## 352.57 `CONFIG_AUXDISPLAY_LOG_LEVEL_CHOICE`

**提示（Prompt）**：辅助显示器（auxdisplay）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_AUXDISPLAY
```

**默认值（Defaults）**

```text
CONFIG_AUXDISPLAY_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_AUXDISPLAY_LOG_LEVEL_OFF
CONFIG_AUXDISPLAY_LOG_LEVEL_ERR
CONFIG_AUXDISPLAY_LOG_LEVEL_WRN
CONFIG_AUXDISPLAY_LOG_LEVEL_INF
CONFIG_AUXDISPLAY_LOG_LEVEL_DBG
CONFIG_AUXDISPLAY_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 辅助文字显示驱动（Auxiliary Textual Display Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_AUXDISPLAY`](P051_drivers_auxdisplay_配置项参考.md#CONFIG_AUXDISPLAY)、[`CONFIG_AUXDISPLAY_LOG_LEVEL_DEFAULT`](P352_subsys_logging_配置项参考_1.md#CONFIG_AUXDISPLAY_LOG_LEVEL_DEFAULT)、[`CONFIG_AUXDISPLAY_LOG_LEVEL_OFF`](P352_subsys_logging_配置项参考_1.md#CONFIG_AUXDISPLAY_LOG_LEVEL_OFF)、[`CONFIG_AUXDISPLAY_LOG_LEVEL_ERR`](P352_subsys_logging_配置项参考_1.md#CONFIG_AUXDISPLAY_LOG_LEVEL_ERR)、[`CONFIG_AUXDISPLAY_LOG_LEVEL_WRN`](P352_subsys_logging_配置项参考_1.md#CONFIG_AUXDISPLAY_LOG_LEVEL_WRN)、[`CONFIG_AUXDISPLAY_LOG_LEVEL_INF`](P352_subsys_logging_配置项参考_1.md#CONFIG_AUXDISPLAY_LOG_LEVEL_INF)、[`CONFIG_AUXDISPLAY_LOG_LEVEL_DBG`](P352_subsys_logging_配置项参考_1.md#CONFIG_AUXDISPLAY_LOG_LEVEL_DBG)。

<a id="CONFIG_AUXDISPLAY_LOG_LEVEL_DBG"></a>

## 352.58 `CONFIG_AUXDISPLAY_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_AUXDISPLAY_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 辅助文字显示驱动（Auxiliary Textual Display Drivers） → 辅助显示器（auxdisplay）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_AUXDISPLAY_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_AUXDISPLAY_LOG_LEVEL_CHOICE)。

<a id="CONFIG_AUXDISPLAY_LOG_LEVEL_DEFAULT"></a>

## 352.59 `CONFIG_AUXDISPLAY_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_AUXDISPLAY_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 辅助文字显示驱动（Auxiliary Textual Display Drivers） → 辅助显示器（auxdisplay）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_AUXDISPLAY_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_AUXDISPLAY_LOG_LEVEL_CHOICE)。

<a id="CONFIG_AUXDISPLAY_LOG_LEVEL_ERR"></a>

## 352.60 `CONFIG_AUXDISPLAY_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_AUXDISPLAY_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 辅助文字显示驱动（Auxiliary Textual Display Drivers） → 辅助显示器（auxdisplay）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_AUXDISPLAY_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_AUXDISPLAY_LOG_LEVEL_CHOICE)。

<a id="CONFIG_AUXDISPLAY_LOG_LEVEL_INF"></a>

## 352.61 `CONFIG_AUXDISPLAY_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_AUXDISPLAY_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 辅助文字显示驱动（Auxiliary Textual Display Drivers） → 辅助显示器（auxdisplay）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_AUXDISPLAY_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_AUXDISPLAY_LOG_LEVEL_CHOICE)。

<a id="CONFIG_AUXDISPLAY_LOG_LEVEL_OFF"></a>

## 352.62 `CONFIG_AUXDISPLAY_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_AUXDISPLAY_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 辅助文字显示驱动（Auxiliary Textual Display Drivers） → 辅助显示器（auxdisplay）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_AUXDISPLAY_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_AUXDISPLAY_LOG_LEVEL_CHOICE)。

<a id="CONFIG_AUXDISPLAY_LOG_LEVEL_WRN"></a>

## 352.63 `CONFIG_AUXDISPLAY_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_AUXDISPLAY_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 辅助文字显示驱动（Auxiliary Textual Display Drivers） → 辅助显示器（auxdisplay）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_AUXDISPLAY_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_AUXDISPLAY_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BBRAM_LOG_LEVEL_CHOICE"></a>

## 352.64 `CONFIG_BBRAM_LOG_LEVEL_CHOICE`

**提示（Prompt）**：电池备份 RAM（bbram）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BBRAM
```

**默认值（Defaults）**

```text
CONFIG_BBRAM_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BBRAM_LOG_LEVEL_OFF
CONFIG_BBRAM_LOG_LEVEL_ERR
CONFIG_BBRAM_LOG_LEVEL_WRN
CONFIG_BBRAM_LOG_LEVEL_INF
CONFIG_BBRAM_LOG_LEVEL_DBG
CONFIG_BBRAM_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池备份 RAM 驱动（Battery-Backed RAM，BBRAM）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BBRAM`](P052_drivers_bbram_配置项参考.md#CONFIG_BBRAM)、[`CONFIG_BBRAM_LOG_LEVEL_DEFAULT`](P352_subsys_logging_配置项参考_1.md#CONFIG_BBRAM_LOG_LEVEL_DEFAULT)、[`CONFIG_BBRAM_LOG_LEVEL_OFF`](P352_subsys_logging_配置项参考_1.md#CONFIG_BBRAM_LOG_LEVEL_OFF)、[`CONFIG_BBRAM_LOG_LEVEL_ERR`](P352_subsys_logging_配置项参考_1.md#CONFIG_BBRAM_LOG_LEVEL_ERR)、[`CONFIG_BBRAM_LOG_LEVEL_WRN`](P352_subsys_logging_配置项参考_1.md#CONFIG_BBRAM_LOG_LEVEL_WRN)、[`CONFIG_BBRAM_LOG_LEVEL_INF`](P352_subsys_logging_配置项参考_1.md#CONFIG_BBRAM_LOG_LEVEL_INF)、[`CONFIG_BBRAM_LOG_LEVEL_DBG`](P352_subsys_logging_配置项参考_1.md#CONFIG_BBRAM_LOG_LEVEL_DBG)。

<a id="CONFIG_BBRAM_LOG_LEVEL_DBG"></a>

## 352.65 `CONFIG_BBRAM_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BBRAM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池备份 RAM 驱动（Battery-Backed RAM，BBRAM） → 电池备份 RAM（bbram）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BBRAM_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_BBRAM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BBRAM_LOG_LEVEL_DEFAULT"></a>

## 352.66 `CONFIG_BBRAM_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BBRAM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池备份 RAM 驱动（Battery-Backed RAM，BBRAM） → 电池备份 RAM（bbram）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BBRAM_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_BBRAM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BBRAM_LOG_LEVEL_ERR"></a>

## 352.67 `CONFIG_BBRAM_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BBRAM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池备份 RAM 驱动（Battery-Backed RAM，BBRAM） → 电池备份 RAM（bbram）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BBRAM_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_BBRAM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BBRAM_LOG_LEVEL_INF"></a>

## 352.68 `CONFIG_BBRAM_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BBRAM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池备份 RAM 驱动（Battery-Backed RAM，BBRAM） → 电池备份 RAM（bbram）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BBRAM_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_BBRAM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BBRAM_LOG_LEVEL_OFF"></a>

## 352.69 `CONFIG_BBRAM_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BBRAM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池备份 RAM 驱动（Battery-Backed RAM，BBRAM） → 电池备份 RAM（bbram）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BBRAM_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_BBRAM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BBRAM_LOG_LEVEL_WRN"></a>

## 352.70 `CONFIG_BBRAM_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BBRAM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池备份 RAM 驱动（Battery-Backed RAM，BBRAM） → 电池备份 RAM（bbram）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BBRAM_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_BBRAM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BINDESC_READ_LOG_LEVEL_CHOICE"></a>

## 352.71 `CONFIG_BINDESC_READ_LOG_LEVEL_CHOICE`

**提示（Prompt）**：二进制描述符读取（Binary Descriptor read）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BINDESC_READ && CONFIG_BINDESC
```

**默认值（Defaults）**

```text
CONFIG_BINDESC_READ_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BINDESC_READ_LOG_LEVEL_OFF
CONFIG_BINDESC_READ_LOG_LEVEL_ERR
CONFIG_BINDESC_READ_LOG_LEVEL_WRN
CONFIG_BINDESC_READ_LOG_LEVEL_INF
CONFIG_BINDESC_READ_LOG_LEVEL_DBG
CONFIG_BINDESC_READ_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 二进制描述符（Binary Descriptors） → 读取二进制描述符（Binary Descriptors Read）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BINDESC_READ`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_READ)、[`CONFIG_BINDESC`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC)、[`CONFIG_BINDESC_READ_LOG_LEVEL_DEFAULT`](P352_subsys_logging_配置项参考_1.md#CONFIG_BINDESC_READ_LOG_LEVEL_DEFAULT)、[`CONFIG_BINDESC_READ_LOG_LEVEL_OFF`](P352_subsys_logging_配置项参考_1.md#CONFIG_BINDESC_READ_LOG_LEVEL_OFF)、[`CONFIG_BINDESC_READ_LOG_LEVEL_ERR`](P352_subsys_logging_配置项参考_1.md#CONFIG_BINDESC_READ_LOG_LEVEL_ERR)、[`CONFIG_BINDESC_READ_LOG_LEVEL_WRN`](P352_subsys_logging_配置项参考_1.md#CONFIG_BINDESC_READ_LOG_LEVEL_WRN)、[`CONFIG_BINDESC_READ_LOG_LEVEL_INF`](P352_subsys_logging_配置项参考_1.md#CONFIG_BINDESC_READ_LOG_LEVEL_INF)、[`CONFIG_BINDESC_READ_LOG_LEVEL_DBG`](P352_subsys_logging_配置项参考_1.md#CONFIG_BINDESC_READ_LOG_LEVEL_DBG)。

<a id="CONFIG_BINDESC_READ_LOG_LEVEL_DBG"></a>

## 352.72 `CONFIG_BINDESC_READ_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BINDESC_READ_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 二进制描述符（Binary Descriptors） → 读取二进制描述符（Binary Descriptors Read） → 二进制描述符读取（Binary Descriptor read）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BINDESC_READ_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_BINDESC_READ_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BINDESC_READ_LOG_LEVEL_DEFAULT"></a>

## 352.73 `CONFIG_BINDESC_READ_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BINDESC_READ_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 二进制描述符（Binary Descriptors） → 读取二进制描述符（Binary Descriptors Read） → 二进制描述符读取（Binary Descriptor read）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BINDESC_READ_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_BINDESC_READ_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BINDESC_READ_LOG_LEVEL_ERR"></a>

## 352.74 `CONFIG_BINDESC_READ_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BINDESC_READ_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 二进制描述符（Binary Descriptors） → 读取二进制描述符（Binary Descriptors Read） → 二进制描述符读取（Binary Descriptor read）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BINDESC_READ_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_BINDESC_READ_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BINDESC_READ_LOG_LEVEL_INF"></a>

## 352.75 `CONFIG_BINDESC_READ_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BINDESC_READ_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 二进制描述符（Binary Descriptors） → 读取二进制描述符（Binary Descriptors Read） → 二进制描述符读取（Binary Descriptor read）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BINDESC_READ_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_BINDESC_READ_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BINDESC_READ_LOG_LEVEL_OFF"></a>

## 352.76 `CONFIG_BINDESC_READ_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BINDESC_READ_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 二进制描述符（Binary Descriptors） → 读取二进制描述符（Binary Descriptors Read） → 二进制描述符读取（Binary Descriptor read）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BINDESC_READ_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_BINDESC_READ_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BINDESC_READ_LOG_LEVEL_WRN"></a>

## 352.77 `CONFIG_BINDESC_READ_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BINDESC_READ_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 二进制描述符（Binary Descriptors） → 读取二进制描述符（Binary Descriptors Read） → 二进制描述符读取（Binary Descriptor read）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BINDESC_READ_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_BINDESC_READ_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BIOMETRICS_LOG_LEVEL_CHOICE"></a>

## 352.78 `CONFIG_BIOMETRICS_LOG_LEVEL_CHOICE`

**提示（Prompt）**：生物识别（biometrics）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BIOMETRICS
```

**默认值（Defaults）**

```text
CONFIG_BIOMETRICS_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BIOMETRICS_LOG_LEVEL_OFF
CONFIG_BIOMETRICS_LOG_LEVEL_ERR
CONFIG_BIOMETRICS_LOG_LEVEL_WRN
CONFIG_BIOMETRICS_LOG_LEVEL_INF
CONFIG_BIOMETRICS_LOG_LEVEL_DBG
CONFIG_BIOMETRICS_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 生物识别驱动（Biometrics Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BIOMETRICS`](P053_drivers_biometrics_配置项参考.md#CONFIG_BIOMETRICS)、[`CONFIG_BIOMETRICS_LOG_LEVEL_DEFAULT`](P352_subsys_logging_配置项参考_1.md#CONFIG_BIOMETRICS_LOG_LEVEL_DEFAULT)、[`CONFIG_BIOMETRICS_LOG_LEVEL_OFF`](P352_subsys_logging_配置项参考_1.md#CONFIG_BIOMETRICS_LOG_LEVEL_OFF)、[`CONFIG_BIOMETRICS_LOG_LEVEL_ERR`](P352_subsys_logging_配置项参考_1.md#CONFIG_BIOMETRICS_LOG_LEVEL_ERR)、[`CONFIG_BIOMETRICS_LOG_LEVEL_WRN`](P352_subsys_logging_配置项参考_1.md#CONFIG_BIOMETRICS_LOG_LEVEL_WRN)、[`CONFIG_BIOMETRICS_LOG_LEVEL_INF`](P352_subsys_logging_配置项参考_1.md#CONFIG_BIOMETRICS_LOG_LEVEL_INF)、[`CONFIG_BIOMETRICS_LOG_LEVEL_DBG`](P352_subsys_logging_配置项参考_1.md#CONFIG_BIOMETRICS_LOG_LEVEL_DBG)。

<a id="CONFIG_BIOMETRICS_LOG_LEVEL_DBG"></a>

## 352.79 `CONFIG_BIOMETRICS_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BIOMETRICS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 生物识别驱动（Biometrics Drivers） → 生物识别（biometrics）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BIOMETRICS_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_BIOMETRICS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BIOMETRICS_LOG_LEVEL_DEFAULT"></a>

## 352.80 `CONFIG_BIOMETRICS_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BIOMETRICS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 生物识别驱动（Biometrics Drivers） → 生物识别（biometrics）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BIOMETRICS_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_BIOMETRICS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BIOMETRICS_LOG_LEVEL_ERR"></a>

## 352.81 `CONFIG_BIOMETRICS_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BIOMETRICS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 生物识别驱动（Biometrics Drivers） → 生物识别（biometrics）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BIOMETRICS_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_BIOMETRICS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BIOMETRICS_LOG_LEVEL_INF"></a>

## 352.82 `CONFIG_BIOMETRICS_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BIOMETRICS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 生物识别驱动（Biometrics Drivers） → 生物识别（biometrics）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BIOMETRICS_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_BIOMETRICS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BIOMETRICS_LOG_LEVEL_OFF"></a>

## 352.83 `CONFIG_BIOMETRICS_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BIOMETRICS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 生物识别驱动（Biometrics Drivers） → 生物识别（biometrics）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BIOMETRICS_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_BIOMETRICS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BIOMETRICS_LOG_LEVEL_WRN"></a>

## 352.84 `CONFIG_BIOMETRICS_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BIOMETRICS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 生物识别驱动（Biometrics Drivers） → 生物识别（biometrics）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BIOMETRICS_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_BIOMETRICS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BSP_SEDI_LOG_LEVEL_CHOICE"></a>

## 352.85 `CONFIG_BSP_SEDI_LOG_LEVEL_CHOICE`

**提示（Prompt）**：bsp_sedi 板级支持组件（bsp_sedi）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_INTEL_HAL
```

**默认值（Defaults）**

```text
CONFIG_BSP_SEDI_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BSP_SEDI_LOG_LEVEL_OFF
CONFIG_BSP_SEDI_LOG_LEVEL_ERR
CONFIG_BSP_SEDI_LOG_LEVEL_WRN
CONFIG_BSP_SEDI_LOG_LEVEL_INF
CONFIG_BSP_SEDI_LOG_LEVEL_DBG
CONFIG_BSP_SEDI_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_intel`（Intel 硬件抽象层模块；工作区相对路径 `modules/hal/intel`） → Intel HAL 的 Zephyr 配置（Configuration）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_INTEL_HAL`](P203_modules_Kconfig.intel_配置项参考.md#CONFIG_INTEL_HAL)、[`CONFIG_BSP_SEDI_LOG_LEVEL_DEFAULT`](P352_subsys_logging_配置项参考_1.md#CONFIG_BSP_SEDI_LOG_LEVEL_DEFAULT)、[`CONFIG_BSP_SEDI_LOG_LEVEL_OFF`](P352_subsys_logging_配置项参考_1.md#CONFIG_BSP_SEDI_LOG_LEVEL_OFF)、[`CONFIG_BSP_SEDI_LOG_LEVEL_ERR`](P352_subsys_logging_配置项参考_1.md#CONFIG_BSP_SEDI_LOG_LEVEL_ERR)、[`CONFIG_BSP_SEDI_LOG_LEVEL_WRN`](P352_subsys_logging_配置项参考_1.md#CONFIG_BSP_SEDI_LOG_LEVEL_WRN)、[`CONFIG_BSP_SEDI_LOG_LEVEL_INF`](P352_subsys_logging_配置项参考_1.md#CONFIG_BSP_SEDI_LOG_LEVEL_INF)、[`CONFIG_BSP_SEDI_LOG_LEVEL_DBG`](P352_subsys_logging_配置项参考_1.md#CONFIG_BSP_SEDI_LOG_LEVEL_DBG)。

<a id="CONFIG_BSP_SEDI_LOG_LEVEL_DBG"></a>

## 352.86 `CONFIG_BSP_SEDI_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BSP_SEDI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_intel`（Intel 硬件抽象层模块；工作区相对路径 `modules/hal/intel`） → Intel HAL 的 Zephyr 配置（Configuration） → bsp_sedi 板级支持组件（bsp_sedi）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BSP_SEDI_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_BSP_SEDI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BSP_SEDI_LOG_LEVEL_DEFAULT"></a>

## 352.87 `CONFIG_BSP_SEDI_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BSP_SEDI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_intel`（Intel 硬件抽象层模块；工作区相对路径 `modules/hal/intel`） → Intel HAL 的 Zephyr 配置（Configuration） → bsp_sedi 板级支持组件（bsp_sedi）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BSP_SEDI_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_BSP_SEDI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BSP_SEDI_LOG_LEVEL_ERR"></a>

## 352.88 `CONFIG_BSP_SEDI_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BSP_SEDI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_intel`（Intel 硬件抽象层模块；工作区相对路径 `modules/hal/intel`） → Intel HAL 的 Zephyr 配置（Configuration） → bsp_sedi 板级支持组件（bsp_sedi）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BSP_SEDI_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_BSP_SEDI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BSP_SEDI_LOG_LEVEL_INF"></a>

## 352.89 `CONFIG_BSP_SEDI_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BSP_SEDI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_intel`（Intel 硬件抽象层模块；工作区相对路径 `modules/hal/intel`） → Intel HAL 的 Zephyr 配置（Configuration） → bsp_sedi 板级支持组件（bsp_sedi）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BSP_SEDI_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_BSP_SEDI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BSP_SEDI_LOG_LEVEL_OFF"></a>

## 352.90 `CONFIG_BSP_SEDI_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BSP_SEDI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_intel`（Intel 硬件抽象层模块；工作区相对路径 `modules/hal/intel`） → Intel HAL 的 Zephyr 配置（Configuration） → bsp_sedi 板级支持组件（bsp_sedi）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BSP_SEDI_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_BSP_SEDI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BSP_SEDI_LOG_LEVEL_WRN"></a>

## 352.91 `CONFIG_BSP_SEDI_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BSP_SEDI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_intel`（Intel 硬件抽象层模块；工作区相对路径 `modules/hal/intel`） → Intel HAL 的 Zephyr 配置（Configuration） → bsp_sedi 板级支持组件（bsp_sedi）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BSP_SEDI_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_BSP_SEDI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_A2DP_LOG_LEVEL_CHOICE"></a>

## 352.92 `CONFIG_BT_A2DP_LOG_LEVEL_CHOICE`

**提示（Prompt）**：蓝牙高级音频分发配置文件（Bluetooth A2DP）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_CLASSIC && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_A2DP_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_A2DP_LOG_LEVEL_INHERIT
CONFIG_BT_A2DP_LOG_LEVEL_OFF
CONFIG_BT_A2DP_LOG_LEVEL_ERR
CONFIG_BT_A2DP_LOG_LEVEL_WRN
CONFIG_BT_A2DP_LOG_LEVEL_INF
CONFIG_BT_A2DP_LOG_LEVEL_DBG
CONFIG_BT_A2DP_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_A2DP_LOG_LEVEL_DEFAULT`](P352_subsys_logging_配置项参考_1.md#CONFIG_BT_A2DP_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_A2DP_LOG_LEVEL_INHERIT`](P352_subsys_logging_配置项参考_1.md#CONFIG_BT_A2DP_LOG_LEVEL_INHERIT)、[`CONFIG_BT_A2DP_LOG_LEVEL_OFF`](P352_subsys_logging_配置项参考_1.md#CONFIG_BT_A2DP_LOG_LEVEL_OFF)、[`CONFIG_BT_A2DP_LOG_LEVEL_ERR`](P352_subsys_logging_配置项参考_1.md#CONFIG_BT_A2DP_LOG_LEVEL_ERR)、[`CONFIG_BT_A2DP_LOG_LEVEL_WRN`](P352_subsys_logging_配置项参考_1.md#CONFIG_BT_A2DP_LOG_LEVEL_WRN)、[`CONFIG_BT_A2DP_LOG_LEVEL_INF`](P352_subsys_logging_配置项参考_1.md#CONFIG_BT_A2DP_LOG_LEVEL_INF)、[`CONFIG_BT_A2DP_LOG_LEVEL_DBG`](P352_subsys_logging_配置项参考_1.md#CONFIG_BT_A2DP_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_A2DP_LOG_LEVEL_DBG"></a>

## 352.93 `CONFIG_BT_A2DP_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_A2DP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙高级音频分发配置文件（Bluetooth A2DP）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_A2DP_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_BT_A2DP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_A2DP_LOG_LEVEL_DEFAULT"></a>

## 352.94 `CONFIG_BT_A2DP_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_A2DP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙高级音频分发配置文件（Bluetooth A2DP）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_A2DP_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_BT_A2DP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_A2DP_LOG_LEVEL_ERR"></a>

## 352.95 `CONFIG_BT_A2DP_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_A2DP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙高级音频分发配置文件（Bluetooth A2DP）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_A2DP_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_BT_A2DP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_A2DP_LOG_LEVEL_INF"></a>

## 352.96 `CONFIG_BT_A2DP_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_A2DP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙高级音频分发配置文件（Bluetooth A2DP）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_A2DP_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_BT_A2DP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_A2DP_LOG_LEVEL_INHERIT"></a>

## 352.97 `CONFIG_BT_A2DP_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_A2DP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 选择项（Choice）：`BT_A2DP_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_A2DP_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_BT_A2DP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_A2DP_LOG_LEVEL_OFF"></a>

## 352.98 `CONFIG_BT_A2DP_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_A2DP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙高级音频分发配置文件（Bluetooth A2DP）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_A2DP_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_BT_A2DP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_A2DP_LOG_LEVEL_WRN"></a>

## 352.99 `CONFIG_BT_A2DP_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_A2DP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙高级音频分发配置文件（Bluetooth A2DP）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_A2DP_LOG_LEVEL_CHOICE`](P352_subsys_logging_配置项参考_1.md#CONFIG_BT_A2DP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_AICS_CLIENT_LOG_LEVEL_CHOICE"></a>

## 352.100 `CONFIG_BT_AICS_CLIENT_LOG_LEVEL_CHOICE`

**提示（Prompt）**：音频输入控制服务客户端（Audio Input Control Service client）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_AICS_CLIENT && CONFIG_BT_AUDIO && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_AICS_CLIENT_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_AICS_CLIENT_LOG_LEVEL_INHERIT
CONFIG_BT_AICS_CLIENT_LOG_LEVEL_OFF
CONFIG_BT_AICS_CLIENT_LOG_LEVEL_ERR
CONFIG_BT_AICS_CLIENT_LOG_LEVEL_WRN
CONFIG_BT_AICS_CLIENT_LOG_LEVEL_INF
CONFIG_BT_AICS_CLIENT_LOG_LEVEL_DBG
CONFIG_BT_AICS_CLIENT_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_AICS_CLIENT`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AICS_CLIENT)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_AICS_CLIENT_LOG_LEVEL_DEFAULT`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AICS_CLIENT_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_AICS_CLIENT_LOG_LEVEL_INHERIT`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AICS_CLIENT_LOG_LEVEL_INHERIT)、[`CONFIG_BT_AICS_CLIENT_LOG_LEVEL_OFF`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AICS_CLIENT_LOG_LEVEL_OFF)、[`CONFIG_BT_AICS_CLIENT_LOG_LEVEL_ERR`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AICS_CLIENT_LOG_LEVEL_ERR)、[`CONFIG_BT_AICS_CLIENT_LOG_LEVEL_WRN`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AICS_CLIENT_LOG_LEVEL_WRN)、[`CONFIG_BT_AICS_CLIENT_LOG_LEVEL_INF`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AICS_CLIENT_LOG_LEVEL_INF)、[`CONFIG_BT_AICS_CLIENT_LOG_LEVEL_DBG`](P353_subsys_logging_配置项参考_2.md#CONFIG_BT_AICS_CLIENT_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<!-- kconfig-navigation -->

[上一章](P351_subsys_llext_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P353_subsys_logging_配置项参考_2.md)
