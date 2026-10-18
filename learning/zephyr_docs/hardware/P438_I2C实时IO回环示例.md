---
id: learning.zephyr-docs.hardware.i2csamples-3
title: I2C实时IO回环示例
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/i2c/rtio_loopback/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="i2c-rtio-loopback"></a>

# 第438章\_I2C实时IO回环示例

原文：[I2C RTIO loopback](https://docs.zephyrproject.org/latest/samples/drivers/i2c/rtio_loopback/README.html)。读取日期：2026-10-13，`latest`。

## 438.1\_概述

本示例展示如何使用**实时输入输出（Real-Time Input/Output，RTIO）**进行同步（Synchronous）和异步（Asynchronous）的 **I2C（Inter-Integrated Circuit，集成电路互连）**传输。它最多使用两个 I2C 控制器硬件实例，分别承担控制器（Controller）和目标（Target）角色。

## 438.2\_硬件要求

需要满足以下两种条件之一：

- 使用两个 I2C 控制器硬件实例，一个支持控制器角色，另一个支持外设/目标角色（Peripheral/Target Role），二者接到同一条 I2C 总线。
- 使用一个能够同时支持控制器与外设角色的 I2C 硬件实例。

务必搭建好总线：为**串行时钟（Serial Clock，SCL）**和**串行数据（Serial Data，SDA）**连接上拉电阻（Pull-up Resistor），并将相关 I2C 硬件实例实际连接到总线上。

## 438.3\_开发板支持

满足要求的开发板需要通过设备树覆盖文件（Devicetree Overlay）指定哪个 I2C 实例承担控制器角色、哪个承担目标角色；二者可以是同一个硬件实例。

设备树别名（Devicetree Alias）`i2c-controller` 指定控制器，`i2c-controller-target` 指定目标。例如，下列 `i2c1`、`i2c2` 是相应控制器的设备树节点标签：

```dts
/ {
        aliases {
                i2c-controller = &i2c1;
                i2c-controller-target = &i2c2;
        };
};
```

如果需要，添加板级配置。官方给出的目标缓冲模式（Target Buffer Mode）配置如下：

```kconfig
CONFIG_I2C_TARGET_BUFFER_MODE=y
```

译注：原文将板级配置也称为 board specific overlay。上面这一行是 Kconfig 配置项，应放入对应配置片段；它不是可直接写入设备树 `.overlay` 的 DTS 语句。

## 438.4\_传输数据大小

以下配置项调节测试中交换的数据字节数：

| 配置项 | 含义 |
| --- | --- |
| `CONFIG_I2C_RTIO_LOOPBACK_DATA_READ_MAX_SIZE` | 回环测试读取数据的最大大小 |
| `CONFIG_I2C_RTIO_LOOPBACK_DATA_WRITE_MAX_SIZE` | 回环测试写入数据的最大大小 |

另见[RTIO 接口参考](../rtio_core_reference/P001_RTIO公共接口.md)、[I2C 接口参考](https://docs.zephyrproject.org/latest/doxygen/html/group__i2c__interface.html)及[示例源代码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/drivers/i2c/rtio_loopback)。

---

[上一章：I2C目标EEPROM示例](P437_I2C目标EEPROM示例.md) · [下一章：ADC设备树示例](P439_ADC设备树示例.md) · [返回大纲](大纲.md)
