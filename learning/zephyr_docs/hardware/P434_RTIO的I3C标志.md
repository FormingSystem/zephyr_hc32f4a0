---
id: learning.zephyr-docs.hardware.i3csamples-4
title: RTIO的I3C标志
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__rtio__i3c__flags.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第434章\_RTIO的I3C标志

原文：[group__rtio__i3c__flags](https://docs.zephyrproject.org/latest/doxygen/html/group__rtio__i3c__flags.html)。读取日期：2026-10-13，`latest`。

## 434.1\_用途与头文件

本页列出**实时输入输出（Real-Time Input/Output，RTIO）**中 **I3C（Improved Inter-Integrated Circuit，改进型集成电路互连）**输入输出设备（I/O Device，IODEV）的标志。它们用于表示消息终止、重复起始、高数据速率及其模式和命令码。

```c
#include <zephyr/rtio/sqe.h>
```

## 434.2\_基础标志

以下为官方宏值及其等价的 I3C 消息标志；`BIT(n)` 表示第 n 位。具体消息行为见[I3C传输接口](P394_I3C传输接口.md)。

| RTIO 宏 | 定义值 | 等价的 I3C 标志及含义 |
| --- | --- | --- |
| <a id="ga671a479885f4d9abbdad677ddfbc47df"></a>[`RTIO_IODEV_I3C_STOP`](https://docs.zephyrproject.org/latest/doxygen/html/group__rtio__i3c__flags.html#ga671a479885f4d9abbdad677ddfbc47df) | `BIT(1)` | `I3C_MSG_STOP`，消息之后发出停止条件（Stop Condition） |
| <a id="ga9d30e1b8f22da07a25fd379c27dc2afe"></a>[`RTIO_IODEV_I3C_RESTART`](https://docs.zephyrproject.org/latest/doxygen/html/group__rtio__i3c__flags.html#ga9d30e1b8f22da07a25fd379c27dc2afe) | `BIT(2)` | `I3C_MSG_RESTART`，消息之前发出重复起始（Repeated Start） |
| <a id="ga857a1b2a766faa1438b4b07d73ca05ed"></a>[`RTIO_IODEV_I3C_HDR`](https://docs.zephyrproject.org/latest/doxygen/html/group__rtio__i3c__flags.html#ga857a1b2a766faa1438b4b07d73ca05ed) | `BIT(3)` | `I3C_MSG_HDR`，高数据速率（High Data Rate，HDR）模式 |
| <a id="ga258aae8fdda81c71d08dc3e26feb843d"></a>[`RTIO_IODEV_I3C_NBCH`](https://docs.zephyrproject.org/latest/doxygen/html/group__rtio__i3c__flags.html#ga258aae8fdda81c71d08dc3e26feb843d) | `BIT(4)` | `I3C_MSG_NBCH`，跳过广播头（No Broadcast Header），仅用于私有传输（Private Transfer） |
| <a id="gaeea22dddf91eb4e9de44a907d799044e"></a>[`RTIO_IODEV_I3C_NOACK_EXPECTED`](https://docs.zephyrproject.org/latest/doxygen/html/group__rtio__i3c__flags.html#gaeea22dddf91eb4e9de44a907d799044e) | `BIT(5)` | `I3C_MSG_NOACK_EXPECTED`，预期目标返回否定应答（Negative Acknowledgement，NACK） |

## 434.3\_HDR命令码位域

<a id="ga0642bb5c69d01ea0fe148da9b8475328"></a>

HDR 的 7 位命令码（Command Code）位域位于 22:16，宏 [`RTIO_IODEV_I3C_HDR_CMD_CODE_MASK`](https://docs.zephyrproject.org/latest/doxygen/html/group__rtio__i3c__flags.html#ga0642bb5c69d01ea0fe148da9b8475328) 定义为 `GENMASK(22, 16)`。`GENMASK(h, l)` 生成覆盖高位 h 至低位 l 的位掩码。

<a id="ga881fcb3d955aece099266ef5b57e767b"></a>

`RTIO_IODEV_I3C_HDR_CMD_CODE_GET(flags)` 使用位域提取宏 [`FIELD_GET`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-pinctrl-siwx91x_8h.html#aa49a456f06f7bdbedfcf3517e461947e)，从参数 [`flags`](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9) 所给标志值中提取命令码。原展开式为：

```c
FIELD_GET(RTIO_IODEV_I3C_HDR_CMD_CODE_MASK, flags)
```

<a id="ga4d0b165eb8f4a7cc63c35e9f9438ee5a"></a>

`RTIO_IODEV_I3C_HDR_CMD_CODE_SET(flags)` 使用位域装配宏 [`FIELD_PREP`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-pinctrl-siwx91x_8h.html#aa03c8b31bf67a097dd9f8153a04ef86b)，把参数 [`flags`](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9) 所给命令码值放入上述位域。原展开式为：

```c
FIELD_PREP(RTIO_IODEV_I3C_HDR_CMD_CODE_MASK, flags)
```

## 434.4\_HDR模式位域

<a id="ga5e278e6ec0c31de2246c0fa9a96425c8"></a>

HDR 模式位掩码 [`RTIO_IODEV_I3C_HDR_MODE_MASK`](https://docs.zephyrproject.org/latest/doxygen/html/group__rtio__i3c__flags.html#ga5e278e6ec0c31de2246c0fa9a96425c8) 定义为 `GENMASK(15, 8)`，对应位 15:8。

<a id="ga902a66ba8772f7a2395069e6725776da"></a>

`RTIO_IODEV_I3C_HDR_MODE_GET(flags)` 从参数 [`flags`](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9) 所给标志值中提取 HDR 模式。原展开式为：

```c
FIELD_GET(RTIO_IODEV_I3C_HDR_MODE_MASK, flags)
```

<a id="gae2b6caf5fa82cc7dc07508dccfeb423b"></a>

`RTIO_IODEV_I3C_HDR_MODE_SET(flags)` 把参数 [`flags`](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9) 所给模式值放入上述位域。原展开式为：

```c
FIELD_PREP(RTIO_IODEV_I3C_HDR_MODE_MASK, flags)
```

译注：四个宏均保留原参数名 [`flags`](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。GET 的输入是包含相应位域的值，SET 的输入是准备写入该位域的值；[`FIELD_PREP`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-pinctrl-siwx91x_8h.html#aa03c8b31bf67a097dd9f8153a04ef86b) 产生位域编码，并不是对变量作原地修改。

---

[上一章：IKS4A1标准I3C示例](P433_IKS4A1标准I3C示例.md) · [下一章：I2C总线示例](P435_I2C总线示例.md) · [返回大纲](大纲.md)
