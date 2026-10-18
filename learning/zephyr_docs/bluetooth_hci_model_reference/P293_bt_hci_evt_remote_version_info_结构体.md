---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-293
title: bt_hci_evt_remote_version_info_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__remote__version__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第293章\_bt\_hci\_evt\_remote\_version\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__remote__version__info.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 293.1\_数据成员（Data Fields）

<a id="r_a196f9489183d6e0116ff687df66c60c0"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a196f9489183d6e0116ff687df66c60c0)。

<a id="r_a1703a9ac9a5e1ba3ed396fe5799f9f51"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#a1703a9ac9a5e1ba3ed396fe5799f9f51)。

<a id="r_a8442b9f2bdc6cbce564c9bcec4169a20"></a>

```c
uint8_t version
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[version](#a8442b9f2bdc6cbce564c9bcec4169a20)。

<a id="r_aaa9c3875143700b6ed013715cb3c7107"></a>

```c
uint16_t manufacturer
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[manufacturer](#aaa9c3875143700b6ed013715cb3c7107)。

<a id="r_a02188119418a5a6dd8a4d0c37f5a060d"></a>

```c
uint16_t subversion
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[subversion](#a02188119418a5a6dd8a4d0c37f5a060d)。

## 293.2\_详细说明（Detailed Documentation）

<a id="a1703a9ac9a5e1ba3ed396fe5799f9f51"></a>

### `handle`

```c
uint16_t bt_hci_evt_remote_version_info::handle
```

<a id="aaa9c3875143700b6ed013715cb3c7107"></a>

### `manufacturer`

```c
uint16_t bt_hci_evt_remote_version_info::manufacturer
```

<a id="a196f9489183d6e0116ff687df66c60c0"></a>

### `status`

```c
uint8_t bt_hci_evt_remote_version_info::status
```

<a id="a02188119418a5a6dd8a4d0c37f5a060d"></a>

### `subversion`

```c
uint16_t bt_hci_evt_remote_version_info::subversion
```

<a id="a8442b9f2bdc6cbce564c9bcec4169a20"></a>

### `version`

```c
uint8_t bt_hci_evt_remote_version_info::version
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 293.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P292_bt_hci_evt_remote_name_req_complete_结构体.md) · [返回大纲](大纲.md) · [下一章](P294_bt_hci_evt_role_change_结构体.md)
