---
id: learning.zephyr-docs.hardware.i2csamples-2
title: I2C目标EEPROM示例
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/i2c/target_eeprom/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="i2c-eeprom-target"></a>

# 第437章\_I2C目标EEPROM示例

原文：[I2C Target](https://docs.zephyrproject.org/latest/samples/drivers/i2c/target_eeprom/README.html)。读取日期：2026-10-13，`latest`。

## 437.1\_概述

本示例通过设备 `zephyr,i2c-target-eeprom`，演示如何设置和使用 **I2C（Inter-Integrated Circuit，集成电路互连）目标应用程序接口（Target Application Programming Interface，Target API）**。

**EEPROM（Electrically Erasable Programmable Read-Only Memory，电可擦可编程只读存储器）**是这里所模拟的目标设备类型；设备标识见[目标 EEPROM 设备树绑定](../mtd_nxp_st_ti_partition_binding_reference/P022_zephyr_i2c-target-eeprom.md#std-dtcompatible-zephyr-i2c-target-eeprom)，接口说明见[I2C 目标接口](https://docs.zephyrproject.org/latest/hardware/peripherals/i2c.html#i2c-target-api)。

## 437.2\_要求

需要支持目标角色（Target Role）的 I2C 外设（Peripheral）。官方已在 [LPCXPRESSO55S69 开发板](https://docs.zephyrproject.org/latest/boards/nxp/lpcxpresso55s69/doc/index.html#lpcxpresso55s69) 上测试本示例。

## 437.3\_构建与运行

源代码位于 Zephyr 仓库的 [samples/drivers/i2c/target_eeprom](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/drivers/i2c/target_eeprom)。在 Zephyr 仓库根目录的开发终端执行以下命令，构建并烧录（Flash）应用程序：

```shell
west build -b lpcxpresso55s69/lpc55s69/cpu0 samples/drivers/i2c/target_eeprom
west flash
```

另见[I2C 接口参考](https://docs.zephyrproject.org/latest/doxygen/html/group__i2c__interface.html)。

---

[上一章：I2C自定义目标示例](P436_I2C自定义目标示例.md) · [下一章：I2C实时IO回环示例](P438_I2C实时IO回环示例.md) · [返回大纲](大纲.md)
