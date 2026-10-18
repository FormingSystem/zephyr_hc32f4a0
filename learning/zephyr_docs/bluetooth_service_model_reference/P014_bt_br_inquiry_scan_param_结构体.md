---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-14
title: bt_br_inquiry_scan_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__br__inquiry__scan__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_bt\_br\_inquiry\_scan\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__br__inquiry__scan__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

BR/EDR 查询扫描（Inquiry Scan）参数。

```c
#include <zephyr/bluetooth/classic/classic.h>
```

<a id="details"></a>

基本速率／增强数据率查询扫描参数（BR/EDR inquiry scan parameters）。注意（Note）：这些参数用于配置本地 BR/EDR 控制器的查询扫描行为。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 14.1\_数据成员（Data Fields）

<a id="r_a6a04891451c372f91b1c670f2a642b15"></a>

```c
uint16_t interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[interval](#a6a04891451c372f91b1c670f2a642b15)。

查询扫描间隔（Inquiry scan interval），以 0.625 毫秒为单位；范围为 `0x0012`–`0x1000`。

<a id="r_adc90daed4bfa1bc40a8b179f02eaab46"></a>

```c
uint16_t window
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[window](#adc90daed4bfa1bc40a8b179f02eaab46)。

查询扫描窗口（Inquiry scan window），以 0.625 毫秒为单位；范围为 `0x0011`–`0x1000`。

<a id="r_a23c55eeca21406ad038d2ff361405d2b"></a>

```c
enum bt_br_scan_type type
```

相关声明：[bt_br_scan_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga03757f934de6f13f95f02316b098875d)、[type](#a23c55eeca21406ad038d2ff361405d2b)。

查询扫描类型（Inquiry Scan Type）。

## 14.2\_详细说明（Detailed Documentation）

<a id="a6a04891451c372f91b1c670f2a642b15"></a>

### `interval`

```c
uint16_t bt_br_inquiry_scan_param::interval
```

查询扫描间隔（Inquiry scan interval），以 0.625 毫秒为单位；范围为 `0x0012`–`0x1000`。

根据蓝牙核心规范（Bluetooth Core Specification），控制器只使用偶数值；若提供奇数，控制器可能忽略最低有效位（LSB），或对该值取整。应用应使用偶数，以符合规范。

<a id="a23c55eeca21406ad038d2ff361405d2b"></a>

### `type`

```c
enum bt_br_scan_type bt_br_inquiry_scan_param::type
```

查询扫描类型（Inquiry Scan Type）。

<a id="adc90daed4bfa1bc40a8b179f02eaab46"></a>

### `window`

```c
uint16_t bt_br_inquiry_scan_param::window
```

查询扫描窗口（Inquiry scan window），以 0.625 毫秒为单位；范围为 `0x0011`–`0x1000`。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/classic.h`

## 14.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/classic.h](https://docs.zephyrproject.org/latest/doxygen/html/classic_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_br_scan_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga03757f934de6f13f95f02316b098875d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P013_bt_br_discovery_result_结构体.md) · [返回大纲](大纲.md) · [下一章](P015_bt_br_oob_结构体.md)
