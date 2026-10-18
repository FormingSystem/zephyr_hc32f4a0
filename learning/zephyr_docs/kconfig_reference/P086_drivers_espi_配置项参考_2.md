---
id: learning.zephyr-docs.kconfig-reference.page-86
title: "`drivers/espi`配置项参考（2/2）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第86章\_`drivers/espi`配置项参考（2/2）

本章翻译官方 Kconfig 数据库中 `drivers/espi` 的 6 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_IT8XXX2_H2RAM_HC_SIZE_2048"></a>

## 86.1 `CONFIG_IT8XXX2_H2RAM_HC_SIZE_2048`

**提示（Prompt）**：2048

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IT8XXX2_H2RAM_HC_SIZE_CHOICE>
```

**定义位置（Location）**：[`drivers/espi/Kconfig.it8xxx2:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.it8xxx2#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动 → ITE IT8XXX2 嵌入式控制器（Embedded Controller）eSPI 驱动 → EC 主机命令（Host Command）的 H2RAM 空间

**配置项引用（Symbol References）**：[`CONFIG_IT8XXX2_H2RAM_HC_SIZE_CHOICE`](P086_drivers_espi_配置项参考_2.md#CONFIG_IT8XXX2_H2RAM_HC_SIZE_CHOICE)。

<a id="CONFIG_IT8XXX2_H2RAM_HC_SIZE_256"></a>

## 86.2 `CONFIG_IT8XXX2_H2RAM_HC_SIZE_256`

**提示（Prompt）**：256。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IT8XXX2_H2RAM_HC_SIZE_CHOICE>
```

**定义位置（Location）**：[`drivers/espi/Kconfig.it8xxx2:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.it8xxx2#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动 → ITE IT8XXX2 嵌入式控制器（Embedded Controller）eSPI 驱动 → EC 主机命令（Host Command）的 H2RAM 空间

**配置项引用（Symbol References）**：[`CONFIG_IT8XXX2_H2RAM_HC_SIZE_CHOICE`](P086_drivers_espi_配置项参考_2.md#CONFIG_IT8XXX2_H2RAM_HC_SIZE_CHOICE)。

<a id="CONFIG_IT8XXX2_H2RAM_HC_SIZE_32"></a>

## 86.3 `CONFIG_IT8XXX2_H2RAM_HC_SIZE_32`

**提示（Prompt）**：32

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IT8XXX2_H2RAM_HC_SIZE_CHOICE>
```

**定义位置（Location）**：[`drivers/espi/Kconfig.it8xxx2:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.it8xxx2#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动 → ITE IT8XXX2 嵌入式控制器（Embedded Controller）eSPI 驱动 → EC 主机命令（Host Command）的 H2RAM 空间

**配置项引用（Symbol References）**：[`CONFIG_IT8XXX2_H2RAM_HC_SIZE_CHOICE`](P086_drivers_espi_配置项参考_2.md#CONFIG_IT8XXX2_H2RAM_HC_SIZE_CHOICE)。

<a id="CONFIG_IT8XXX2_H2RAM_HC_SIZE_512"></a>

## 86.4 `CONFIG_IT8XXX2_H2RAM_HC_SIZE_512`

**提示（Prompt）**：512

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IT8XXX2_H2RAM_HC_SIZE_CHOICE>
```

**定义位置（Location）**：[`drivers/espi/Kconfig.it8xxx2:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.it8xxx2#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动 → ITE IT8XXX2 嵌入式控制器（Embedded Controller）eSPI 驱动 → EC 主机命令（Host Command）的 H2RAM 空间

**配置项引用（Symbol References）**：[`CONFIG_IT8XXX2_H2RAM_HC_SIZE_CHOICE`](P086_drivers_espi_配置项参考_2.md#CONFIG_IT8XXX2_H2RAM_HC_SIZE_CHOICE)。

<a id="CONFIG_IT8XXX2_H2RAM_HC_SIZE_64"></a>

## 86.5 `CONFIG_IT8XXX2_H2RAM_HC_SIZE_64`

**提示（Prompt）**：64

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IT8XXX2_H2RAM_HC_SIZE_CHOICE>
```

**定义位置（Location）**：[`drivers/espi/Kconfig.it8xxx2:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.it8xxx2#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动 → ITE IT8XXX2 嵌入式控制器（Embedded Controller）eSPI 驱动 → EC 主机命令（Host Command）的 H2RAM 空间

**配置项引用（Symbol References）**：[`CONFIG_IT8XXX2_H2RAM_HC_SIZE_CHOICE`](P086_drivers_espi_配置项参考_2.md#CONFIG_IT8XXX2_H2RAM_HC_SIZE_CHOICE)。

<a id="CONFIG_IT8XXX2_H2RAM_HC_SIZE_CHOICE"></a>

## 86.6 `CONFIG_IT8XXX2_H2RAM_HC_SIZE_CHOICE`

**提示（Prompt）**：EC 主机命令（Host Command）的 H2RAM 空间

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI_PERIPHERAL_EC_HOST_CMD && CONFIG_ESPI_IT8XXX2 && CONFIG_ESPI
```

**默认值（Defaults）**

```text
CONFIG_IT8XXX2_H2RAM_HC_SIZE_256
```

**可选项（Choices）**

```text
CONFIG_IT8XXX2_H2RAM_HC_SIZE_16
CONFIG_IT8XXX2_H2RAM_HC_SIZE_32
CONFIG_IT8XXX2_H2RAM_HC_SIZE_64
CONFIG_IT8XXX2_H2RAM_HC_SIZE_128
CONFIG_IT8XXX2_H2RAM_HC_SIZE_256
CONFIG_IT8XXX2_H2RAM_HC_SIZE_512
CONFIG_IT8XXX2_H2RAM_HC_SIZE_1024
CONFIG_IT8XXX2_H2RAM_HC_SIZE_2048
```

**定义位置（Location）**：[`drivers/espi/Kconfig.it8xxx2:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/Kconfig.it8xxx2#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动 → ITE IT8XXX2 嵌入式控制器（Embedded Controller）eSPI 驱动

**配置项引用（Symbol References）**：[`CONFIG_ESPI_PERIPHERAL_EC_HOST_CMD`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_PERIPHERAL_EC_HOST_CMD)、[`CONFIG_ESPI_IT8XXX2`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_IT8XXX2)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)、[`CONFIG_IT8XXX2_H2RAM_HC_SIZE_256`](P086_drivers_espi_配置项参考_2.md#CONFIG_IT8XXX2_H2RAM_HC_SIZE_256)、[`CONFIG_IT8XXX2_H2RAM_HC_SIZE_16`](P085_drivers_espi_配置项参考_1.md#CONFIG_IT8XXX2_H2RAM_HC_SIZE_16)、[`CONFIG_IT8XXX2_H2RAM_HC_SIZE_32`](P086_drivers_espi_配置项参考_2.md#CONFIG_IT8XXX2_H2RAM_HC_SIZE_32)、[`CONFIG_IT8XXX2_H2RAM_HC_SIZE_64`](P086_drivers_espi_配置项参考_2.md#CONFIG_IT8XXX2_H2RAM_HC_SIZE_64)、[`CONFIG_IT8XXX2_H2RAM_HC_SIZE_128`](P085_drivers_espi_配置项参考_1.md#CONFIG_IT8XXX2_H2RAM_HC_SIZE_128)、[`CONFIG_IT8XXX2_H2RAM_HC_SIZE_512`](P086_drivers_espi_配置项参考_2.md#CONFIG_IT8XXX2_H2RAM_HC_SIZE_512)、[`CONFIG_IT8XXX2_H2RAM_HC_SIZE_1024`](P085_drivers_espi_配置项参考_1.md#CONFIG_IT8XXX2_H2RAM_HC_SIZE_1024)、[`CONFIG_IT8XXX2_H2RAM_HC_SIZE_2048`](P086_drivers_espi_配置项参考_2.md#CONFIG_IT8XXX2_H2RAM_HC_SIZE_2048)。

<!-- kconfig-navigation -->

[上一章](P085_drivers_espi_配置项参考_1.md) · [返回大纲](大纲.md) · [下一章](P087_drivers_ethernet_配置项参考_1.md)
