---
id: learning.zephyr-docs.hardware.ops-2
title: EEPROM驱动操作结构
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structeeprom__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第54章\_EEPROM驱动操作结构

原文：[structeeprom__driver__api](https://docs.zephyrproject.org/latest/doxygen/html/structeeprom__driver__api.html)。读取日期：2026-10-13，`latest`。

<a id="details"></a>
<a id="doc-variable-members"></a>
<a id="header-details"></a>
<a id="header-doc-variable-members"></a>
<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 54.1\_驱动操作结构

`struct eeprom_driver_api` 是**电可擦可编程只读存储器（Electrically Erasable Programmable Read-Only Memory，EEPROM）**驱动必须定义的 **应用程序编程接口（Application Programming Interface，API）**结构。它保存指向驱动已实现操作的函数指针，以及驱动特定的其他常量数据。官方声明所在头文件为 `zephyr/drivers/eeprom.h`，本页参考由该文件生成。

原文以 **必需项（Required，REQ）**与 **可选项（Optional，OPT）**标记字段。标为REQ的成员**必须由驱动设置**；标为OPT的成员可以不实现。下表保留每个字段实际标记，而非把所有操作统一视为可选。

## 54.2\_操作字段

<a id="a821724b35926882a1a732f1fb541b965"></a>
<a id="r_a821724b35926882a1a732f1fb541b965"></a>
<a id="a82ef001ad60f95fabb37235a40974854"></a>
<a id="r_a82ef001ad60f95fabb37235a40974854"></a>
<a id="ade546770dc302ecb149a8631bbf5b5cb"></a>
<a id="r_ade546770dc302ecb149a8631bbf5b5cb"></a>

| 字段 | 函数指针类型 | 要求 | 作用 |
| --- | --- | --- | --- |
| [`read`](https://docs.zephyrproject.org/latest/doxygen/html/structeeprom__driver__api.html#a821724b35926882a1a732f1fb541b965) | [`eeprom_api_read`](https://docs.zephyrproject.org/latest/doxygen/html/group__eeprom__interface__backend.html#gaa12f5fdb02e73a608d5fdf128b14b4be) | REQ | 从EEPROM读取数据。 |
| [`write`](https://docs.zephyrproject.org/latest/doxygen/html/structeeprom__driver__api.html#ade546770dc302ecb149a8631bbf5b5cb) | [`eeprom_api_write`](https://docs.zephyrproject.org/latest/doxygen/html/group__eeprom__interface__backend.html#gaee46582bce50cf50cc0293d006ca2ba8) | REQ | 向EEPROM写入数据。 |
| [`size`](https://docs.zephyrproject.org/latest/doxygen/html/structeeprom__driver__api.html#a82ef001ad60f95fabb37235a40974854) | [`eeprom_api_size`](https://docs.zephyrproject.org/latest/doxygen/html/group__eeprom__interface__backend.html#gabbf1d1f66944f2297c68686a7db080ac) | REQ | 取得EEPROM容量，单位为字节。 |

三个操作在原文中均标为必需。读写返回操作状态，容量查询返回字节数，不能因为字段同属一个操作表就使用相同的返回值判断。公共调用约束见[EEPROM接口参考](P040_EEPROM接口参考.md)。

这些字段的参数签名与公共接口的对应关系，见[驱动后端接口](P049_EEPROM驱动后端接口.md)。原页的逐字段参考与上表一致，没有另外给出字段默认值。

## 54.3\_相关设备定义入口

原页还指向 [`DEVICE_DT_INST_DEFINE()`](../device_reference/P001_设备模型公共接口.md#gada5ba4aca9e0662ccebb2232c7256419)、[`DEVICE_DT_DEFINE()`](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1) 与 [`DEVICE_API()`](../device_reference/P007_设备模型头文件参考.md#aa0cdc799fc0b9c80eb29f989eec86707)。前两个宏用于依据设备树定义设备实例，后一个宏用于定义驱动API对象；它们把设备实例与操作结构关联起来。这里保留官方精确链接，具体参数以对应宏参考为准。

对应的完整[头文件参考](../flash_reference/P021_EEPROM公共头文件参考.md)和[源码浏览译文](../flash_reference/P022_EEPROM公共头文件源码.md)已补齐，类型、条件声明和调用转发可继续对照。

[上一章：熵源驱动操作结构](P053_熵源驱动操作结构.md) · [下一章：CAN收发器操作结构](P055_CAN收发器操作结构.md) · [返回大纲](大纲.md)
