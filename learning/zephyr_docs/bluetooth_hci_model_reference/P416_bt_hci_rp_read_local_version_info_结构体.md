---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-416
title: bt_hci_rp_read_local_version_info_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__read__local__version__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第416章\_bt\_hci\_rp\_read\_local\_version\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__read__local__version__info.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 416.1\_数据成员（Data Fields）

<a id="r_a935f990f7c28f7c89660c2b8ab975f43"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a935f990f7c28f7c89660c2b8ab975f43)。

<a id="r_a1cc521426e530344a328e935152dd488"></a>

```c
uint8_t hci_version
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[hci_version](#a1cc521426e530344a328e935152dd488)。

<a id="r_a04161ed3cc0b9c3c442e3464501ce118"></a>

```c
uint16_t hci_revision
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[hci_revision](#a04161ed3cc0b9c3c442e3464501ce118)。

<a id="r_a634641751852f66aabb408bf1b4d0cd2"></a>

```c
uint8_t lmp_version
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[lmp_version](#a634641751852f66aabb408bf1b4d0cd2)。

<a id="r_a7cd6ba190137eaf7c4eb9c2d7e5b36ce"></a>

```c
uint16_t manufacturer
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[manufacturer](#a7cd6ba190137eaf7c4eb9c2d7e5b36ce)。

<a id="r_a43f29cf08a2399e818bfa441c6b7a1f3"></a>

```c
uint16_t lmp_subversion
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[lmp_subversion](#a43f29cf08a2399e818bfa441c6b7a1f3)。

## 416.2\_详细说明（Detailed Documentation）

<a id="a04161ed3cc0b9c3c442e3464501ce118"></a>

### `hci_revision`

```c
uint16_t bt_hci_rp_read_local_version_info::hci_revision
```

<a id="a1cc521426e530344a328e935152dd488"></a>

### `hci_version`

```c
uint8_t bt_hci_rp_read_local_version_info::hci_version
```

<a id="a43f29cf08a2399e818bfa441c6b7a1f3"></a>

### `lmp_subversion`

```c
uint16_t bt_hci_rp_read_local_version_info::lmp_subversion
```

<a id="a634641751852f66aabb408bf1b4d0cd2"></a>

### `lmp_version`

```c
uint8_t bt_hci_rp_read_local_version_info::lmp_version
```

<a id="a7cd6ba190137eaf7c4eb9c2d7e5b36ce"></a>

### `manufacturer`

```c
uint16_t bt_hci_rp_read_local_version_info::manufacturer
```

<a id="a935f990f7c28f7c89660c2b8ab975f43"></a>

### `status`

```c
uint8_t bt_hci_rp_read_local_version_info::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 416.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P415_bt_hci_rp_read_local_features_结构体.md) · [返回大纲](大纲.md) · [下一章](P417_bt_hci_rp_read_rssi_结构体.md)
