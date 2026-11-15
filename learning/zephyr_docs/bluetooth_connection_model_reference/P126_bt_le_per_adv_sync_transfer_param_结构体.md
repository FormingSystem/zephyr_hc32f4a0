---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-126
title: bt_le_per_adv_sync_transfer_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__per__adv__sync__transfer__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第126章\_bt\_le\_per\_adv\_sync\_transfer\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__per__adv__sync__transfer__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

周期广播同步传递（Periodic Advertising Sync Transfer）的参数。

```c
#include <zephyr/bluetooth/bluetooth.h>
```

<a id="details"></a>

周期广播同步传递参数（Periodic Advertising Sync Transfer，PAST parameters）。此结构定义配置同步传递所需的参数，包括最大事件跳过数、同步超时及同步传递选项。注意（Note）：用于 `bt_le_per_adv_sync_transfer_subscribe` 函数，配置同步传递设置。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 126.1\_数据成员（Data Fields）

<a id="r_a840e7cfac3a2947e5128d704067aaf7e"></a>

```c
uint16_t skip
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[skip](#a840e7cfac3a2947e5128d704067aaf7e)。

最大事件跳过数（Maximum event skip）。

<a id="r_a5bfa84c6bdacdf8893a0951a5ce71fc6"></a>

```c
uint16_t timeout
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[timeout](#a5bfa84c6bdacdf8893a0951a5ce71fc6)。

同步超时（Synchronization timeout），为 N × 10 毫秒。

<a id="r_a0b3ee6df1b409e64a064ffb6ac632cce"></a>

```c
uint32_t options
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[options](#a0b3ee6df1b409e64a064ffb6ac632cce)。

周期广播同步传递选项（Periodic Advertising Sync Transfer options），参见 `bt_le_per_adv_sync_transfer_opt`。

## 126.2\_详细说明（Detailed Documentation）

<a id="a0b3ee6df1b409e64a064ffb6ac632cce"></a>

### `options`

```c
uint32_t bt_le_per_adv_sync_transfer_param::options
```

周期广播同步传递选项（Periodic Advertising Sync Transfer options），参见 `bt_le_per_adv_sync_transfer_opt`。

<a id="a840e7cfac3a2947e5128d704067aaf7e"></a>

### `skip`

```c
uint16_t bt_le_per_adv_sync_transfer_param::skip
```

最大事件跳过数（Maximum event skip）。

成功接收后可以跳过的周期广播数据包数量（Periodic advertising packets）。

<a id="a5bfa84c6bdacdf8893a0951a5ce71fc6"></a>

### `timeout`

```c
uint16_t bt_le_per_adv_sync_transfer_param::timeout
```

同步超时（Synchronization timeout），为 N × 10 毫秒。

周期广播同步的同步超时（Synchronization timeout），范围为 `0x000A`–`0x4000`，即 100–163840 毫秒。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/bluetooth.h`

## 126.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [bt_le_per_adv_sync_transfer_opt](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga820c5f3721e72662e558cc4576b6111b)
- [bt_le_per_adv_sync_transfer_subscribe](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaa0658bd53df1d5e8e89e13330e4fd0ae)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P125_bt_le_per_adv_sync_term_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P127_bt_le_scan_cb_结构体.md)
