---
id: learning.zephyr-docs.hardware.hwapi-can-babbling
title: CAN持续发送示例
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/can/babbling/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="can-babbling"></a>

# 第45章\_CAN持续发送示例

原文：[Controller Area Network (CAN) babbling node](https://docs.zephyrproject.org/latest/samples/drivers/can/babbling/README.html)。读取日期：2026-10-13，`latest`。

## 45.1\_持续发送节点的含义

在 **控制器局域网（Controller Area Network，CAN）**中，**持续发送节点（Babbling Node）**不断发送优先级相同、且常常优先级很高的CAN帧，这种持续发送通常是错误行为。它会阻止较低优先级帧访问总线，因为这些帧会不断输掉 **总线仲裁（Bus Arbitration）**。

本示例模拟这样的CAN节点，用于观察同一总线上其他节点在持续仲裁失败时的行为。发送帧的属性可通过Zephyr配置系统Kconfig设置。由于只关注帧的仲裁部分，**发送帧不携带数据**。官方源码位于 `samples/drivers/can/babbling`。

## 45.2\_控制器和停止按钮

需要一块具有CAN控制器的板，并通过设备树chosen节点属性 `zephyr,canbus` 选择该控制器。

示例支持可选的停止按钮。若有按钮，必须通过设备树别名 `sw0` 配置，通常位于板的 `BOARD.dts` 文件中。**设备树源文件（Devicetree Source，DTS）**描述硬件和连接；这里的 `BOARD` 代表相应板名，`sw0` 是逻辑别名，不是物理引脚编号0。

## 45.3\_构建和运行

原文以TWR-KE18F为例。准备Zephyr主机环境、对应工具链和烧录工具，连接目标板；在Ubuntu Bash或已准备好的UCRT64 Bash中，从实验Zephyr源码根目录执行：

```shell
# From the root of the zephyr repository
west build -b twr_ke18f samples/drivers/can/babbling
west flash
```

构建工具生成 `build` 目录，构建成功后再烧录。若无法找到所选CAN设备，应先返回chosen节点、驱动和板配置检查。运行后节点将持续参与总线仲裁，使用已配置的停止按钮可中止这一行为。

## 45.4\_输出含义

以下为原文输出，保留其固件版本和按钮名称：

```text
*** Booting Zephyr OS build zephyr-v3.1.0-4606-g8c1efa8b96bb  ***
babbling on can@40024000 with standard (11-bit) CAN ID 0x010, RTR 0, CAN FD 0
abort by pressing User SW3 button
```

示例使用标准11位标识符，CAN ID为 `0x010`。ID是 **标识符（Identifier）**；RTR指 **远程传输请求（Remote Transmission Request）**；CAN FD指 **可变数据速率CAN（CAN with Flexible Data-Rate）**。这里RTR和CAN FD都显示为0。`can@40024000` 是设备名称的一部分，不是主机文件路径。

> 译注：日志中的Zephyr 3.1.0构建字符串是官方页面保留的历史输出，不代表当前 `latest` 版本。User SW3也是该示例板上的按钮名称，其他板应以 `sw0` 实际映射为准。本次未执行持续发送或实板通信验证。

相关 **应用程序编程接口（Application Programming Interface，API）**及工作模式见[CAN控制器](P030_CAN控制器.md)。

[上一章：CAN计数器示例](P044_CAN计数器示例.md) · [下一章：CRC上下文结构](P046_CRC上下文结构.md) · [返回大纲](大纲.md)
