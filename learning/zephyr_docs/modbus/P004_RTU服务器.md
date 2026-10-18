---
id: learning.zephyr-docs.modbus.rtu-server
title: Modbus RTU服务器
kind: reference
status: maintained
domains: [zephyr, modbus, communication]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/modbus/rtu_server/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_Modbus RTU服务器

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/modbus/rtu_server/README.html)。本次读取日期：2026-10-14；基线为保存的`latest`页面，HTML摘要见[来源记录](../SOURCES.md)。

[官方示例源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/subsys/modbus/rtu_server)。本仓库的[源码参照](../../../samples/subsys/modbus/rtu_server/src/main.c)使用相对链接；本地版本不自动等同于官网版本。

<a id="modbus-rtu-server"></a>
<a id="overview"></a>

## 4.1\_概述

这是一个简单应用，演示Zephyr RTOS中的Modbus RTU服务器（Server）实现。

<a id="requirements"></a>

## 4.2\_要求

本示例已在nRF52840-DK和FRDM-K64F开发板上测试，但应适用于任何具有空闲UART接口或USB设备控制器（Device Controller）的开发板。开发板还应具有三个LED。

RTU服务器示例运行在评估板上，客户端运行在PC或笔记本电脑上。本示例说明使用[PyModbus](https://github.com/pymodbus-dev/pymodbus)的交互式环境（Pymodbus REPL）；也可以尝试其他客户端实现。

<a id="using-rs-485-transceiver"></a>

### 使用RS-485收发器（Using RS-485 transceiver）

这是本示例的默认配置。除评估板外，还需要USB转RS-485总线适配器，以及将UART TX、RX转换为RS-485的扩展板。可以使用兼容Arduino排针的扩展板，例如[joy-it RS-485 shield for Arduino](https://joy-it.net/en/products/ARD-RS485)。本例使用驱动器使能（Driver Enable，DE）信号，由JOY-IT扩展板的D9引脚控制。使用其他扩展板时，必须在应用覆盖文件[samples/subsys/modbus/rtu_server/app.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/modbus/rtu_server/app.overlay)中调整或移除`de-gpios`属性。

USB转RS-485适配器连接到计算机USB端口，其A+、B-两根线路应连接到RS-485扩展板。

<a id="using-cdc-acm-uart"></a>

### 使用CDC ACM UART（Using CDC ACM UART）

只需具有受支持USB设备控制器的评估板。将其USB设备端口连接到计算机USB端口。这里的CDC ACM指通信设备类的抽象控制模型（Communications Device Class, Abstract Control Model）。

虽然这种方式只是点对点连接，并非总线，但除测试服务器实现外，也可实际用于通过USB连接控制继电器或读取ADC值，无需实现自定义USB类或驱动。

<a id="building-and-running"></a>

## 4.3\_构建与运行

以下命令构建并烧录RTU服务器示例：

```shell
west build -b nrf52840dk/nrf52840 samples/subsys/modbus/rtu_server
west flash
```

以下命令构建并烧录使用CDC ACM UART的RTU服务器示例：

```shell
west build -b nrf52840dk/nrf52840 samples/subsys/modbus/rtu_server -- -DDTC_OVERLAY_FILE=cdc-acm.overlay -DEXTRA_CONF_FILE=overlay-cdc-acm.conf
west flash
```

在客户端PC或笔记本电脑上，以下命令将PyModbus连接到RTU服务器。使用CDC ACM UART时，应将`ttyUSB`替换为对应的`ttyACM`设备。

```shell
# pymodbus.console serial --port /dev/ttyUSB0 --baudrate 19200
                          --bytesize 8 --parity N --stopbits 2
```

> 译注：原页将上述终端命令分成两行，未写续行符；在Shell中执行时应合并为一条命令，开头的`#`为原例终端提示符。

服务器开发板上的LED通过Modbus功能码（Function Code）FC01、FC05和FC15控制。原文将点亮LED0的`write_coil`操作标为FC01。

> 译注：原文将FC01与FC05的读写名称写反了。[官方Modbus API](P008_Modbus完整API参考.md)和[本仓库头文件参照](../../../include/zephyr/modbus/modbus.h)均表明：**FC01读取线圈（Read Coils），FC05写单个线圈（Write Single Coil），FC15写多个线圈（Write Multiple Coils）**。下面的原命令不变，`write_coil`对应FC05，后面的`read_coils`对应FC01。

```text
> client.write_coil address=0 value=1 slave=1
```

客户端应确认通信成功，LED0应点亮。

```json
{
    "address": 0,
    "value": true
}
```

要使LED0熄灭、LED1和LED2点亮，使用FC15命令`write_coils`：

```text
> client.write_coils address=0 values=0,1,1 slave=1
```

读取LED0、LED1、LED2状态可使用`read_coils`；原文此处标为FC05，正确对应关系见上述译注。

```text
> client.read_coils address=0 count=3 slave=1
{
    "bits": [
        false,
        true,
        true,
        false,
        false,
        false,
        false,
        false
    ]
}
```

也可以读写保持寄存器（Holding Register），但目前这不会与开发板外设产生任何特殊交互。

写单个保持寄存器，使用FC06命令`write_register`：

```text
> client.write_register address=0 value=42 slave=1
```

或者使用FC16命令`write_registers`：

```text
> client.write_registers address=0 values=42,42,42 slave=1
```

读取保持寄存器，使用FC03命令`read_holding_registers`：

```text
> client.read_holding_registers address=0 count=3 slave=1
{
    "registers": [
        42,
        42,
        42
    ]
}
```


<a id="see-also"></a>

## 4.4\_另请参阅

- [MODBUS API](P008_Modbus完整API参考.md)

[上一章：Modbus RTU客户端](P003_RTU客户端.md) · [返回大纲](大纲.md) · [下一章：Modbus TCP转串行网关](P005_TCP转串行网关.md)
