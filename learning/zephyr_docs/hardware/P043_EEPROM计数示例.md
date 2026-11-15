---
id: learning.zephyr-docs.hardware.hwapi-eeprom-sample
title: EEPROM计数示例
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/eeprom/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="eeprom"></a>

# 第43章\_EEPROM计数示例

原文：[EEPROM](https://docs.zephyrproject.org/latest/samples/drivers/eeprom/README.html)。读取日期：2026-10-13，`latest`。

## 43.1\_用持久化计数观察设备启动

本示例通过 **电可擦可编程只读存储器（Electrically Erasable Programmable Read-Only Memory，EEPROM）**驱动的 **应用程序编程接口（Application Programming Interface，API）**实现一个简单的启动计数器。接口含义见[EEPROM接口参考](P040_EEPROM接口参考.md)；示例源目录 `samples/drivers/eeprom` 为官方已有内容。

以下命令均以实验Zephyr源码根目录为当前位置。先完成对应平台的主机工具和依赖准备；`build` 目录由构建工具产生。各板命令是替代分支，切换目标时应使用独立构建目录或先按构建章节清理旧配置，避免把前一目标的缓存用于后一目标。

## 43.2\_已有设备别名的板

如果目标板已定义EEPROM，并给它设置 `eeprom-0` **别名（Alias）**，示例可以直接构建，无需额外配置。例如 **原生模拟器（Native Simulator）** `native_sim`：

```shell
west build -b native_sim samples/drivers/eeprom
west build -t run
```

这一分支在已满足原生模拟器依赖的Linux Bash环境执行；`west build -t run` 运行构建产物。不能把该运行步骤直接解释为Windows原生终端可执行，也不能把模拟设备结果当作真实EEPROM硬件验证。

## 43.3\_通过覆盖文件或扩展板提供设备

如果板上没有相应定义，需要添加针对该板的设备树 **覆盖文件（Overlay）**，或启用 **扩展板（Shield）**。对于具有Arduino排针的板，原文给出下列例子，使用 `x_nucleo_eeprma2` 扩展板：

```shell
west build -b nrf52840dk/nrf52840 --shield x_nucleo_eeprma2 samples/drivers/eeprom
```

在已准备该板工具链的Ubuntu Bash或UCRT64 Bash中执行；此命令完成构建，扩展板必须与实际连接和目标板配置一致。若提示别名或设备缺失，应返回覆盖文件、扩展板选择及设备树定义检查，而不是删除示例中的设备访问。

## 43.4\_GD32F450I-EVAL分支

对于GD32F450I-EVAL，先使用跳线帽将JP5接到 **通用同步异步收发器（Universal Synchronous/Asynchronous Receiver/Transmitter，USART）**一侧，再构建和烧录：

```shell
west build -b gd32f450i_eval samples/drivers/eeprom
west flash
```

执行位置仍是实验Zephyr源码根目录，终端为已准备对应工具的Ubuntu Bash或UCRT64 Bash。JP5连接要求针对这块官方示例板，不是HC32或其他板的接线依据。烧录前必须先完成构建。

## 43.5\_输出和重复启动

输出表示找到名为 `EEPROM_M24C02` 的设备，容量为256字节，示例中保存的启动计数为7。复位 **微控制器（Microcontroller Unit，MCU）**后可观察计数增加；7是原文某次运行的示例值，不是新设备固定初始值。

原文给出的控制台输出如下：

```text
Found EEPROM device "EEPROM_M24C02"
Using eeprom with size of: 256.
Device booted 7 times.
Reset the MCU to see the increasing boot counter.
```

本次仅核对文档，未执行模拟运行、EEPROM写入或实板复位。相关概览见[EEPROM入口](P035_EEPROM入口.md)。

[上一章：CRC校验示例](P042_CRC校验示例.md) · [下一章：CAN计数器示例](P044_CAN计数器示例.md) · [返回大纲](大纲.md)
