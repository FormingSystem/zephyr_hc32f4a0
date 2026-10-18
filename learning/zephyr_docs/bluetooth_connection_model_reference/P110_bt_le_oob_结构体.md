---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-110
title: bt_le_oob_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__oob.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第110章\_bt\_le\_oob\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__oob.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

低功耗蓝牙带外（LE Out of Band，OOB）信息。

```c
#include <zephyr/bluetooth/bluetooth.h>
```

<a id="details"></a>

低功耗蓝牙带外（LE Out of Band，OOB）信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 110.1\_数据成员（Data Fields）

<a id="r_a17cfed7683efbf5b5954847d655d7424"></a>

```c
bt_addr_le_t addr
```

相关声明：[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[addr](#a17cfed7683efbf5b5954847d655d7424)。

低功耗地址（LE address）。

<a id="r_a80ccd4ab120a880adfff9aba3b19b4fd"></a>

```c
struct bt_le_oob_sc_data le_sc_data
```

相关声明：[bt_le_oob_sc_data](P111_bt_le_oob_sc_data_结构体.md)、[le_sc_data](#a80ccd4ab120a880adfff9aba3b19b4fd)。

低功耗蓝牙安全连接（LE Secure Connections）配对使用的带外（Out of Band，OOB）数据。

## 110.2\_详细说明（Detailed Documentation）

<a id="a17cfed7683efbf5b5954847d655d7424"></a>

### `addr`

```c
bt_addr_le_t bt_le_oob::addr
```

低功耗地址（LE address）。

若启用隐私（Privacy），则此地址为可解析私有地址（Resolvable Private Address）。

<a id="a80ccd4ab120a880adfff9aba3b19b4fd"></a>

### `le_sc_data`

```c
struct bt_le_oob_sc_data bt_le_oob::le_sc_data
```

低功耗蓝牙安全连接（LE Secure Connections）配对使用的带外（Out of Band，OOB）数据。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/bluetooth.h`

## 110.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h_source.html)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)
- [bt_le_oob_sc_data](P111_bt_le_oob_sc_data_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P109_bt_le_local_features_结构体.md) · [返回大纲](大纲.md) · [下一章](P111_bt_le_oob_sc_data_结构体.md)
