---
id: learning.zephyr-docs.platform-security-model-reference.page-68
title: tisci_msg_fwl_region_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structtisci__msg__fwl__region.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第68章\_tisci\_msg\_fwl\_region\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structtisci__msg__fwl__region.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/drivers/firmware/tisci/tisci.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 68.1\_数据成员（Data Fields）

<a id="r_ab3b3ae28613a3ef9e7c83b9d2af9f4ce"></a>

```c
uint16_t fwl_id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[fwl_id](#ab3b3ae28613a3ef9e7c83b9d2af9f4ce)。

<a id="r_a2cb0672482a7859294a1c95b7f42d265"></a>

```c
uint16_t region
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[region](#a2cb0672482a7859294a1c95b7f42d265)。

<a id="r_aae2b9a8670d5e799347606d48408980f"></a>

```c
uint32_t n_permission_regs
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[n_permission_regs](#aae2b9a8670d5e799347606d48408980f)。

<a id="r_a4e5c3b596b1e60524ac386c8506c3870"></a>

```c
uint32_t control
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[control](#a4e5c3b596b1e60524ac386c8506c3870)。

<a id="r_a4c091b340c1dc21f866d623489ab8451"></a>

```c
uint32_t permissions [3]
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[permissions](#a4c091b340c1dc21f866d623489ab8451)。

<a id="r_a4378cc7f160a86af3708284a7cb068a6"></a>

```c
uint64_t start_address
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[start_address](#a4378cc7f160a86af3708284a7cb068a6)。

<a id="r_a789bcad9536d23d0cca4e8791f01c95c"></a>

```c
uint64_t end_address
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[end_address](#a789bcad9536d23d0cca4e8791f01c95c)。

## 68.2\_详细说明（Detailed Documentation）

<a id="a4e5c3b596b1e60524ac386c8506c3870"></a>

### `control`

```c
uint32_t tisci_msg_fwl_region::control
```

<a id="a789bcad9536d23d0cca4e8791f01c95c"></a>

### `end_address`

```c
uint64_t tisci_msg_fwl_region::end_address
```

<a id="ab3b3ae28613a3ef9e7c83b9d2af9f4ce"></a>

### `fwl_id`

```c
uint16_t tisci_msg_fwl_region::fwl_id
```

<a id="aae2b9a8670d5e799347606d48408980f"></a>

### `n_permission_regs`

```c
uint32_t tisci_msg_fwl_region::n_permission_regs
```

<a id="a4c091b340c1dc21f866d623489ab8451"></a>

### `permissions`

```c
uint32_t tisci_msg_fwl_region::permissions[3]
```

<a id="a2cb0672482a7859294a1c95b7f42d265"></a>

### `region`

```c
uint16_t tisci_msg_fwl_region::region
```

<a id="a4378cc7f160a86af3708284a7cb068a6"></a>

### `start_address`

```c
uint64_t tisci_msg_fwl_region::start_address
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/firmware/tisci/tisci.h`

## 68.3\_原页交叉引用（Cross References）

- [zephyr/drivers/firmware/tisci/tisci.h](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P067_tisci_msg_fwl_owner_结构体.md) · [返回大纲](大纲.md) · [下一章](P069_tisci_msg_fwl_region_cfg_结构体.md)
