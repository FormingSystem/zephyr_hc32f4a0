---
id: learning.zephyr-docs.hardware.dacapi-6
title: DAC通道配置结构
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structdac__channel__cfg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第825章\_DAC通道配置结构

原文：[structdac__channel__cfg](https://docs.zephyrproject.org/latest/doxygen/html/structdac__channel__cfg.html)。读取日期：2026-10-13，`latest`。

`struct dac_channel_cfg` 指定数模转换器（Digital-to-Analog Converter，DAC）通道配置（Channel Configuration）。定义来自 `zephyr/drivers/dac.h`：

```c
#include <zephyr/drivers/dac.h>
```

## 825.1\_全部字段

| 字段 | 声明类型 | 中文说明 |
| --- | --- | --- |
| [`channel_id`](https://docs.zephyrproject.org/latest/doxygen/html/structdac__channel__cfg.html#a41a1708aa81b2a808556ec976ce303f3) | [`uint8_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | 要配置的DAC通道标识（Channel Identifier） |
| [`resolution`](https://docs.zephyrproject.org/latest/doxygen/html/structdac__channel__cfg.html#a4ba4f6dde3e4525e0a0e71fea5aeaef3) | [`uint8_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | 所需DAC分辨率（Resolution），受设备能力限制 |
| [`buffered`](https://docs.zephyrproject.org/latest/doxygen/html/structdac__channel__cfg.html#a31df5ad55f40cb89819fac3acd6b4d96) | [`bool`](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)，位域宽度1 | 为此通道启用输出缓冲器（Output Buffer） |
| [`internal`](https://docs.zephyrproject.org/latest/doxygen/html/structdac__channel__cfg.html#ac0557d8d726842d480ecea04b115ff74) | [`bool`](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)，位域宽度1 | 为此通道启用内部输出路径（Internal Output Path） |

[`uint8_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) 为8位无符号整数；[`bool`](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b) 为布尔类型，位域（Bit Field）宽度保留为1。

## 825.2\_缓冲器与内部路径

`buffered` 例如适用于输出直接连接负载（Load）、中间没有放大器（Amplifier）的情况，具体行为取决于硬件。

`internal` 适用于支持通过内部路径直接连接片上外设（On-Chip Peripheral）的通道，具体行为同样取决于硬件。

该结构由[通道配置接口](P822_数模转换器接口.md)使用；字段文档由 `zephyr/drivers/dac.h` 生成。

---

[上一章：DAC驱动扩展入口](P824_DAC驱动扩展入口.md) · [下一章：DAC设备树规格结构](P826_DAC设备树规格结构.md) · [返回大纲](大纲.md)
