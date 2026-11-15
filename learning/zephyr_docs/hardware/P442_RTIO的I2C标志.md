---
id: learning.zephyr-docs.hardware.adcsamples-3
title: RTIO的I2C标志
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__rtio__i2c__flags.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第442章\_RTIO的I2C标志

原文：[group__rtio__i2c__flags](https://docs.zephyrproject.org/latest/doxygen/html/group__rtio__i2c__flags.html)。读取日期：2026-10-13，`latest`。

## 442.1\_用途与头文件

本页列出**实时输入输出（Real-Time Input/Output，RTIO）**中 **I2C（Inter-Integrated Circuit，集成电路互连）**输入输出设备（I/O Device，IODEV）的标志。

```c
#include <zephyr/rtio/sqe.h>
```

## 442.2\_标志定义与等价关系

以下三个宏分别与对应的 I2C 消息标志等价；`BIT(n)` 表示第 n 位。

| RTIO 标志 | 定义值 | 等价的 I2C 消息标志 | 含义 |
| --- | --- | --- | --- |
| <a id="gaf923e862d2c6a3fbce5eb96781cf86d8"></a>[`RTIO_IODEV_I2C_STOP`](https://docs.zephyrproject.org/latest/doxygen/html/group__rtio__i2c__flags.html#gaf923e862d2c6a3fbce5eb96781cf86d8) | `BIT(1)` | `I2C_MSG_STOP` | 停止条件（Stop Condition） |
| <a id="gadba1c5eddeecc431000bd92054f55c3a"></a>[`RTIO_IODEV_I2C_RESTART`](https://docs.zephyrproject.org/latest/doxygen/html/group__rtio__i2c__flags.html#gadba1c5eddeecc431000bd92054f55c3a) | `BIT(2)` | `I2C_MSG_RESTART` | 重复起始条件（Repeated Start Condition） |
| <a id="gaa0c3b047c7205d12775d8d38907119b9"></a>[`RTIO_IODEV_I2C_10_BITS`](https://docs.zephyrproject.org/latest/doxygen/html/group__rtio__i2c__flags.html#gaa0c3b047c7205d12775d8d38907119b9) | `BIT(3)` | `I2C_MSG_ADDR_10_BITS` | 使用 10 位地址（10-bit Address） |

```c
#define RTIO_IODEV_I2C_STOP BIT(1)
#define RTIO_IODEV_I2C_RESTART BIT(2)
#define RTIO_IODEV_I2C_10_BITS BIT(3)
```

---

[上一章：ADC通用流示例](P441_ADC通用流示例.md) · [下一章：ADC通道配置结构](P443_ADC通道配置结构.md) · [返回大纲](大纲.md)
