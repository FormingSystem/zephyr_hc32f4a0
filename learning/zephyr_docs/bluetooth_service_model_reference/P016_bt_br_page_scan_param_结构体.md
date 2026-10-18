---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-16
title: bt_br_page_scan_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__br__page__scan__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_bt\_br\_page\_scan\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__br__page__scan__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

寻呼扫描（Page Scan）参数。

```c
#include <zephyr/bluetooth/classic/classic.h>
```

<a id="details"></a>

寻呼扫描（Page Scan）参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 16.1\_数据成员（Data Fields）

<a id="r_a670129c10bc0c57684e00ce7835b1648"></a>

```c
uint16_t interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[interval](#a670129c10bc0c57684e00ce7835b1648)。

寻呼扫描间隔（Page scan interval），以 0.625 毫秒为单位；范围为 `0x0012`–`0x1000`。

<a id="r_a0f0cb7a792d2ec2ff7cc1d7bc6b01dce"></a>

```c
uint16_t window
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[window](#a0f0cb7a792d2ec2ff7cc1d7bc6b01dce)。

寻呼扫描窗口（Page scan window），以 0.625 毫秒为单位；范围为 `0x0011`–`0x1000`。

<a id="r_aab7cc81841af5461825dfe19a45dab3e"></a>

```c
enum bt_br_scan_type type
```

相关声明：[bt_br_scan_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga03757f934de6f13f95f02316b098875d)、[type](#aab7cc81841af5461825dfe19a45dab3e)。

寻呼扫描类型（Page Scan Type）。

## 16.2\_详细说明（Detailed Documentation）

<a id="a670129c10bc0c57684e00ce7835b1648"></a>

### `interval`

```c
uint16_t bt_br_page_scan_param::interval
```

寻呼扫描间隔（Page scan interval），以 0.625 毫秒为单位；范围为 `0x0012`–`0x1000`。

根据蓝牙核心规范（Bluetooth Core Specification），控制器只使用偶数值；若提供奇数，控制器可能忽略最低有效位（LSB），或对该值取整。应用应使用偶数，以符合规范。

<a id="aab7cc81841af5461825dfe19a45dab3e"></a>

### `type`

```c
enum bt_br_scan_type bt_br_page_scan_param::type
```

寻呼扫描类型（Page Scan Type）。

<a id="a0f0cb7a792d2ec2ff7cc1d7bc6b01dce"></a>

### `window`

```c
uint16_t bt_br_page_scan_param::window
```

寻呼扫描窗口（Page scan window），以 0.625 毫秒为单位；范围为 `0x0011`–`0x1000`。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/classic.h`

## 16.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/classic.h](https://docs.zephyrproject.org/latest/doxygen/html/classic_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_br_scan_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga03757f934de6f13f95f02316b098875d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P015_bt_br_oob_结构体.md) · [返回大纲](大纲.md) · [下一章](P017_bt_cap_broadcast_source_结构体.md)
