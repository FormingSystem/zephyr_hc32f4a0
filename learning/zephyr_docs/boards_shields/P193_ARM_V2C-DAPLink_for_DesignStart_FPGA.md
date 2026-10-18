---
id: learning.zephyr-docs.boards-shields.page-193
title: ARM V2C-DAPLink for DesignStart FPGA
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/v2c_daplink/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="arm-v2c-daplink-for-designstart-fpga"></a>

<a id="v2c-daplink-shield"></a>

# 第193章\_面向DesignStart FPGA的ARM V2C-DAPLink

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/v2c_daplink/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

[面向DesignStart FPGA的ARM V2C-DAPLink](https://developer.arm.com/tools-and-software/development-boards/designstart-daplink-board)扩展板，为[Arty](../boards_cypress_to_dragino/P014_Arty.md#arty_a7)上实现的ARM DesignStart FPGA参考设计提供DAPLink调试访问。

<a id="id2"></a>

![官方原图：V2C-DAPLink](images/v2c_daplink.jpg)

V2C-DAPLink，图片来源：ARM Ltd.

除DAPLink调试访问外，V2C-DAPLink扩展板还提供：


- QSPI NOR Flash存储器
- microSD卡槽

<a id="programming"></a>

## 编程（Programming）

Cfg跳线J2断开时，CPU从指令紧耦合存储器（ITCM）启动，可自动烧录。控制台连接[Arty](../boards_cypress_to_dragino/P014_Arty.md#arty_a7)上的USB连接器J10，例如：

```text
# From the root of the zephyr repository
west build -b arty_a7_arm_designstart_m1 --shield v2c_daplink samples/hello_world
west flash
```

Cfg跳线J2闭合时，CPU从V2C-DAPLink的QSPI NOR Flash启动。控制台连接V2C-DAPLink上的USB连接器J1。须将生成的zephyr/zephyr.bin手动复制到扩展板提供的USB大容量存储设备进行烧录：

```text
# From the root of the zephyr repository
west build -b arty_a7_arm_designstart_m1 --shield v2c_daplink_cfg samples/hello_world
```

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [designstart-daplink-board](https://developer.arm.com/tools-and-software/development-boards/designstart-daplink-board)：<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)>。

---

[上一章](P192_TI_Building_Automation_Sensors_MKII_Building_Automation_Multi_sensor_shield.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P194_WAVESHARE_DSI_LCD_Panel.md)
