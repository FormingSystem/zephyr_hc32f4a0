---
id: learning.zephyr-docs.modbus.rtu-client
title: Modbus RTU客户端
kind: reference
status: maintained
domains: [zephyr, modbus, communication]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/modbus/rtu_client/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_Modbus RTU客户端

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/modbus/rtu_client/README.html)。本次读取日期：2026-10-14；基线为保存的`latest`页面，HTML摘要见[来源记录](../SOURCES.md)。

[官方示例源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/subsys/modbus/rtu_client)。本仓库的[源码参照](../../../samples/subsys/modbus/rtu_client/src/main.c)使用相对链接；本地版本不自动等同于官网版本。

<a id="modbus-rtu-client"></a>
<a id="overview"></a>

## 3.1\_概述

这是一个简单应用，演示Zephyr RTOS中的Modbus RTU客户端（Client）实现。

<a id="requirements"></a>

## 3.2\_要求

本示例已在nRF52840-DK和FRDM-K64F开发板上测试，但应适用于任何具有空闲通用异步收发器（Universal Asynchronous Receiver-Transmitter，UART）接口的开发板。

RTU客户端示例运行在评估板上，与另一块运行[Modbus RTU服务器示例](P004_RTU服务器.md#modbus-rtu-server)的开发板通信。

除评估板外，还可使用RS-485扩展板（Shield），将UART TX、RX信号转换为RS-485。可以使用兼容Arduino排针的扩展板，例如[joy-it RS-485 shield for Arduino](https://joy-it.net/en/products/ARD-RS485)。本例使用驱动器使能（Driver Enable，DE）信号，由JOY-IT扩展板的D9引脚控制。使用其他扩展板时，必须在应用覆盖文件[samples/subsys/modbus/rtu_client/app.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/modbus/rtu_client/app.overlay)中调整或移除`de-gpios`属性。

两块RS-485扩展板的A+、B-线路应对应相连。另一种方式是将两块开发板的UART RX、TX信号交叉连接。

<a id="building-and-running"></a>

## 3.3\_构建与运行

以下命令构建并烧录RTU客户端示例：

```shell
west build -b frdm_k64f samples/subsys/modbus/rtu_client
west flash
```

示例与RTU服务器通信，使LED依次点亮。

```text
*** Booting Zephyr OS build zephyr-v2.3.0-1993-g07e8d80ae028  ***
[00:00:00.005,000] <inf> mb_rtu: RTU timeout 2005 us
[00:00:00.050,000] <inf> mbc_sample: WR|RD holding register:
48 00 65 00 6c 00 6c 00  6f 00 00 00 00 00 00 00 |H.e.l.l. o.......
[00:00:00.062,000] <inf> mbc_sample: Coils state 0x00
[00:00:00.864,000] <inf> mbc_sample: Coils state 0x07
```

<a id="see-also"></a>

## 3.4\_另请参阅

- [MODBUS API](P008_Modbus完整API参考.md)

[上一章：Modbus示例目录](P002_Modbus示例目录.md) · [返回大纲](大纲.md) · [下一章：Modbus RTU服务器](P004_RTU服务器.md)
