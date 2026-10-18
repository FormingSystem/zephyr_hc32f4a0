---
id: learning.zephyr-docs.hardware.firmware-1
title: ARM系统控制与管理接口
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/hardware/firmware/arm-scmi.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第597章\_ARM系统控制与管理接口

原文：[ARM System Control and Management Interface](https://docs.zephyrproject.org/latest/hardware/firmware/arm-scmi.html)。读取日期：2026-10-13，`latest`。

## 597.1\_概述

**系统控制与管理接口（System Control and Management Interface，SCMI）**是 ARM 制定的规范，定义一组与**操作系统（Operating System，OS）**无关的软件接口，用于时钟控制、引脚控制等系统管理操作。在这里，Zephyr 作为一个 **SCMI代理（SCMI Agent）**运行。

**Zephyr 的实现可能只包含本文所述特性或功能的一部分。**

## 597.2\_标准协议

本页“标准协议”指 SCMI 规范涵盖的协议。支持情况如下：

| 标识符（ID） | 协议 | 支持版本 |
| --- | --- | --- |
| `0x10` | 基础协议（Base Protocol） | `2.1` |
| `0x11` | 电源域管理协议（Power Domain Management Protocol） | `3.1` |
| `0x12` | 系统电源管理协议（System Power Management Protocol） | `2.1` |
| `0x14` | 时钟管理协议（Clock Management Protocol） | `3.0` |
| `0x19` | 引脚控制协议（Pin Control Protocol） | `1.0` |

## 597.3\_传输方式

两种传输方式均使用**共享内存（Shared Memory）**，通过不同的**门铃（Doorbell）**机制通知另一侧：

| 名称 | 说明 | 兼容字符串 |
| --- | --- | --- |
| MBOX | 基于**邮箱（Mailbox，MBOX）**门铃的共享内存传输 | [`arm,scmi`](https://docs.zephyrproject.org/latest/build/dts/api/bindings/firmware/arm%2Cscmi.html#std-dtcompatible-arm-scmi) |
| SMC | 基于**安全监控调用（Secure Monitor Call，SMC）**门铃的共享内存传输 | [`arm,scmi-smc`](https://docs.zephyrproject.org/latest/build/dts/api/bindings/firmware/arm%2Cscmi-smc.html#std-dtcompatible-arm-scmi-smc) |

## 597.4\_厂商扩展

SCMI 规范允许厂商增加协议，也允许平台固件在某些情况下选择不同的行为。本文将这些情况统称为**厂商扩展（Vendor Extension）**。

NXP 提供符合 SCMI 的平台固件，称为**系统管理器（System Manager，SM）**，详情见 [NXP i.MX System Manager](https://github.com/nxp-imx/imx-sm)。当前支持的 NXP 专属协议如下：

| 标识符 | 协议 | 支持版本 |
| --- | --- | --- |
| `0x82` | 中央处理器（Central Processing Unit，CPU）协议 | `1.0` |

支持的 NXP 特殊处理规则如下：根据平台固件的配置，共享内存中可能包含消息**循环冗余校验（Cyclic Redundancy Check，CRC）**字段；固件会对每条接收到的消息检查该字段。相关配置见 [`CONFIG_ARM_SCMI_NXP_VENDOR_EXTENSIONS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM_SCMI_NXP_VENDOR_EXTENSIONS)。

---

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：平台固件说明](P596_平台固件说明.md) · [本模块主线目录](../reading/hardware.md) · [全部主线](../reading/README.md) · [下一篇：硬件支持目录](P614_硬件支持目录.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：平台固件说明](P596_平台固件说明.md) · [下一章：固件驱动示例目录](P598_固件驱动示例目录.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
