---
id: learning.zephyr-docs.hardware.dacapi-7
title: DAC设备树规格结构
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structdac__dt__spec.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第826章\_DAC设备树规格结构

原文：[structdac__dt__spec](https://docs.zephyrproject.org/latest/doxygen/html/structdac__dt__spec.html)。读取日期：2026-10-13，`latest`。

`struct dac_dt_spec` 保存设备树（Devicetree）中指定的数模转换器（Digital-to-Analog Converter，DAC）通道信息。定义来自 `zephyr/drivers/dac.h`：

```c
#include <zephyr/drivers/dac.h>
```

## 826.1\_全部字段与有效性

| 字段 | 声明类型 | 中文说明 |
| --- | --- | --- |
| [`dev`](https://docs.zephyrproject.org/latest/doxygen/html/structdac__dt__spec.html#a9e779040c75a1a0fbea138285682c05f) | `const struct device *` | 此输入输出通道（I/O Channel）使用的DAC驱动实例的设备结构指针 |
| [`channel_id`](https://docs.zephyrproject.org/latest/doxygen/html/structdac__dt__spec.html#a27e188e8c4aefe79ff7331883eb53549) | [`uint8_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | 此I/O通道使用的DAC通道标识（Channel Identifier） |
| [`channel_cfg_dt_node_exists`](https://docs.zephyrproject.org/latest/doxygen/html/structdac__dt__spec.html#a00dde7f3907771edcc07fdc060e9e944) | [`bool`](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b) | 标志设备树中是否通过相应DAC控制器的子节点提供了此通道的配置 |
| [`channel_cfg`](https://docs.zephyrproject.org/latest/doxygen/html/structdac__dt__spec.html#a142c21713aa8d5b081e840f8c99a6e66) | `struct dac_channel_cfg` | 设备树指定的关联通道配置；**仅在 `channel_cfg_dt_node_exists` 为true时有效** |
| [`vref_mv`](https://docs.zephyrproject.org/latest/doxygen/html/structdac__dt__spec.html#adc5df5c5d99704753daad5ebd38d3fee) | [`uint16_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e) | 此通道选择的参考电压（Reference Voltage），设备树未提供该值时为0；**仅在 `channel_cfg_dt_node_exists` 为true时有效** |

[`uint8_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)／[`uint16_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e) 分别为8／16位无符号整数，[`bool`](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b) 为布尔类型；I/O指输入输出（Input/Output）。`vref_mv` 的毫伏单位与头文件电压换算接口的参考电压参数一致。

## 826.2\_关联宏与配置结构

[DAC_DT_SPEC_GET_BY_IDX和DAC_DT_SPEC_GET](P822_数模转换器接口.md)可以生成此结构的静态初始化器（Static Initializer）。`channel_cfg` 的成员含义见[DAC通道配置结构](P825_DAC通道配置结构.md)。

本结构字段文档由 `zephyr/drivers/dac.h` 生成。

---

[上一章：DAC通道配置结构](P825_DAC通道配置结构.md) · [下一章：DAC驱动接口结构](P827_DAC驱动接口结构.md) · [返回大纲](大纲.md)
