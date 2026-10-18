---
id: learning.zephyr-docs.firmware_update.mgmtex-osdp
title: OSDP设备协议示例
kind: reference
status: maintained
domains: [zephyr, firmware_update]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/mgmt/osdp/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第26章\_OSDP设备协议示例

原文：[Open Supervised Device Protocol (OSDP)](https://docs.zephyrproject.org/latest/samples/subsys/mgmt/osdp/README.html)。读取日期：2026-10-13，`latest`。

## 26.1\_协议定位与通信方式

**开放式受监控设备协议（Open Supervised Device Protocol，OSDP）**是一项 **国际电工委员会（International Electrotechnical Commission，IEC）**标准，编号IEC 60839-11-5，旨在提高门禁与安防产品之间的互操作性。它支持 **安全通道（Secure Channel，SC）**，为配置好的设备提供加密与认证通信。

OSDP规定一个 **控制面板（Control Panel，CP）**如何经两线RS-485多点串行通道连接一个或多个 **外围设备（Peripheral Device，PD）**。RS-485是差分串行电气接口标准名称。协议也可在其他基于字节流的物理通道上传输安全数据；更多信息见[libosdp项目](https://github.com/goToMain/libosdp/)。

虽然主要面向门禁与安防行业，OSDP也可用作资源需求不高的通用设备通信协议。原文认为其 **128位高级加密标准（Advanced Encryption Standard，AES-128）**安全能力并非“最高等级”，但相对于完全不提供安全机制仍有价值。

> 译注：这是原作者的定性表述；不能只凭算法位数判断系统安全等级，还取决于密钥配置、认证过程和实现。这里不将该措辞改写为对AES-128的失效判断。

## 26.2\_外围设备功能

OSDP可控制或读取外围设备上的下列部件和状态：

- **发光二极管（Light-Emitting Diode，LED）**指示灯。
- 蜂鸣器（Buzzer）。
- 键盘（Keypad）。
- 输出（Output）：**通用输入输出（General-Purpose Input/Output，GPIO）**。
- 输入控制（Input Control）：GPIO。
- 显示器（Display）。
- 设备状态（Device Status），例如防拆与电源状态。
- 卡片读卡器（Card Reader）。
- 指纹读入器（Fingerprint Reader）。

原页仅有协议与能力介绍，没有提供构建命令、示例输出或媒体附件。

[上一章：UpdateHub升级示例](P025_UpdateHub升级示例.md) · [下一章：hawkBit接口](P027_hawkBit接口.md) · [返回大纲](大纲.md)
