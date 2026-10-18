---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-325
title: bt_hci_le_read_min_supported_conn_interval_group_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__le__read__min__supported__conn__interval__group.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第325章\_bt\_hci\_le\_read\_min\_supported\_conn\_interval\_group\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__le__read__min__supported__conn__interval__group.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 325.1\_数据成员（Data Fields）

<a id="r_a5cfd002c4dc82faa692ed1afa50692b5"></a>

```c
uint16_t group_min
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[group_min](#a5cfd002c4dc82faa692ed1afa50692b5)。

<a id="r_abcd7d0eadf485b82993d421072cc8ba4"></a>

```c
uint16_t group_max
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[group_max](#abcd7d0eadf485b82993d421072cc8ba4)。

<a id="r_a43ef933e3f445ac1366a3707b52ceffd"></a>

```c
uint16_t group_stride
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[group_stride](#a43ef933e3f445ac1366a3707b52ceffd)。

## 325.2\_详细说明（Detailed Documentation）

<a id="abcd7d0eadf485b82993d421072cc8ba4"></a>

### `group_max`

```c
uint16_t bt_hci_le_read_min_supported_conn_interval_group::group_max
```

<a id="a5cfd002c4dc82faa692ed1afa50692b5"></a>

### `group_min`

```c
uint16_t bt_hci_le_read_min_supported_conn_interval_group::group_min
```

<a id="a43ef933e3f445ac1366a3707b52ceffd"></a>

### `group_stride`

```c
uint16_t bt_hci_le_read_min_supported_conn_interval_group::group_stride
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 325.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P324_bt_hci_le_iq_sample16_结构体.md) · [返回大纲](大纲.md) · [下一章](P326_bt_hci_lockstep_结构体.md)
