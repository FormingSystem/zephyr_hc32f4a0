---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-106
title: bt_le_ext_adv_scanned_info_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__ext__adv__scanned__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第106章\_bt\_le\_ext\_adv\_scanned\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__ext__adv__scanned__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

广播被扫描事件（Advertising Scanned Event）的信息。

```c
#include <zephyr/bluetooth/bluetooth.h>
```

<a id="details"></a>

广播扫描事件信息（Advertising scanned event information）。注意（Note）：用于 `bt_le_ext_adv_cb`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 106.1\_数据成员（Data Fields）

<a id="r_a4431f157891d2c1a7d0e40f7e879ac3d"></a>

```c
bt_addr_le_t * addr
```

相关声明：[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[addr](#a4431f157891d2c1a7d0e40f7e879ac3d)。

主动扫描器的低功耗地址及类型（Active scanner LE address and type）。

## 106.2\_详细说明（Detailed Documentation）

<a id="a4431f157891d2c1a7d0e40f7e879ac3d"></a>

### `addr`

```c
bt_addr_le_t* bt_le_ext_adv_scanned_info::addr
```

主动扫描器的低功耗地址及类型（Active scanner LE address and type）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/bluetooth.h`

## 106.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h_source.html)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)
- [bt_le_ext_adv_cb](P103_bt_le_ext_adv_cb_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P105_bt_le_ext_adv_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P107_bt_le_ext_adv_sent_info_结构体.md)
