---
id: learning.zephyr-docs.hardware.ops-0
title: CRC驱动操作结构
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcrc__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第52章\_CRC驱动操作结构

原文：[structcrc__driver__api](https://docs.zephyrproject.org/latest/doxygen/html/structcrc__driver__api.html)。读取日期：2026-10-13，`latest`。

## 52.1\_驱动操作结构

`struct crc_driver_api` 是**循环冗余校验（Cyclic Redundancy Check，CRC）**驱动必须定义的 **应用程序编程接口（Application Programming Interface，API）**结构。它保存指向驱动已实现操作的函数指针，以及驱动特定的其他常量数据。官方声明所在头文件为 `zephyr/drivers/crc.h`，本页参考由该文件生成。

原文以 **必需项（Required，REQ）**与 **可选项（Optional，OPT）**标记字段。标为REQ的成员**必须由驱动设置**；标为OPT的成员可以不实现。下表保留每个字段实际标记，而非把所有操作统一视为可选。

## 52.2\_操作字段

| 字段 | 函数指针类型 | 要求 | 作用 |
| --- | --- | --- | --- |
| [`begin`](https://docs.zephyrproject.org/latest/doxygen/html/structcrc__driver__api.html#abf45e92362c5cb1d3c2e6503eea0a974) | [`crc_api_begin`](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface__backend.html#ga8babc96e0e656e3974c5e3df32f59107) | OPT | 为计算配置CRC单元。 |
| [`update`](https://docs.zephyrproject.org/latest/doxygen/html/structcrc__driver__api.html#a82cb49e5025deedbc80159e5d5817a89) | [`crc_api_update`](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface__backend.html#ga7d6a2a6b119a8fb51d91e6f5f6269af7) | OPT | 对所给数据缓冲区执行CRC计算并取得结果。 |
| [`finish`](https://docs.zephyrproject.org/latest/doxygen/html/structcrc__driver__api.html#a644cf87e1a1f1105dd0bbbcbe66be32b) | [`crc_api_finish`](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface__backend.html#gadaec1299bbc8b5a03e4b724b32064abc) | OPT | 完成CRC计算。 |

原页把三个操作均标为可选。这是操作结构的标注，不表示省略任一计算阶段后仍能得到同样结果；应用需要处理公共接口报告的未实现错误，详见[CRC驱动接口参考](P038_CRC驱动接口参考.md)。

这些字段的参数签名与公共接口的对应关系，见[驱动后端接口](P047_CRC驱动后端接口.md)。原页的逐字段参考与上表一致，没有另外给出字段默认值。

## 52.3\_相关设备定义入口

原页还指向 [`DEVICE_DT_INST_DEFINE()`](../device_reference/P001_设备模型公共接口.md#gada5ba4aca9e0662ccebb2232c7256419)、[`DEVICE_DT_DEFINE()`](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1) 与 [`DEVICE_API()`](../device_reference/P007_设备模型头文件参考.md#aa0cdc799fc0b9c80eb29f989eec86707)。前两个宏用于依据设备树定义设备实例，后一个宏用于定义驱动API对象；它们把设备实例与操作结构关联起来。这里保留官方精确链接，具体参数以对应宏参考为准。

[上一章：伪EEPROM接口](P051_伪EEPROM接口.md) · [下一章：熵源驱动操作结构](P053_熵源驱动操作结构.md) · [返回大纲](大纲.md)
