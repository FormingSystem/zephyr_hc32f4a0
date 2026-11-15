---
id: learning.zephyr-docs.platform-security-model-reference.page-76
title: acpi_dmar_id_联合体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/unionacpi__dmar__id.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第76章\_acpi\_dmar\_id\_联合体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/unionacpi__dmar__id.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/acpi/acpi.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 76.1\_数据成员（Data Fields）

```c
struct {
```

<a id="r_a02cb825a2772ee8d738266321c292ba3"></a>

```c
uint16_t function: 3
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[function](#a8fe219b9f4f5871cf14d01079af79614)。

<a id="r_a3300682ad606a81e71baac4f50a0d7ae"></a>

```c
uint16_t device: 5
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[device](#a03e48f74dae90bbbeba96c4d9f274020)。

<a id="r_a8445da4d5064de9fd04c7a755f235224"></a>

```c
uint16_t bus: 8
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[bus](#a3e9194555004762db83d9853594ffca1)。

<a id="r_a0fffa1ca831591b42f732acfd1d86aa6"></a>

```c
} bits
```

相关声明：[bits](#a0fffa1ca831591b42f732acfd1d86aa6)。

<a id="r_a700729e862c40298e4ebe05b7881f009"></a>

```c
uint16_t raw
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[raw](#a700729e862c40298e4ebe05b7881f009)。

## 76.2\_详细说明（Detailed Documentation）

<a id="a0fffa1ca831591b42f732acfd1d86aa6"></a>

### `[struct]`

```c
struct { ... } acpi_dmar_id::bits
```

<a id="a3e9194555004762db83d9853594ffca1"></a>

### `bus`

```c
uint16_t acpi_dmar_id::bus
```

<a id="a03e48f74dae90bbbeba96c4d9f274020"></a>

### `device`

```c
uint16_t acpi_dmar_id::device
```

<a id="a8fe219b9f4f5871cf14d01079af79614"></a>

### `function`

```c
uint16_t acpi_dmar_id::function
```

<a id="a700729e862c40298e4ebe05b7881f009"></a>

### `raw`

```c
uint16_t acpi_dmar_id::raw
```

本数据类型文档由以下文件生成：

- `zephyr/acpi/acpi.h`

## 76.3\_原页交叉引用（Cross References）

- [zephyr/acpi/acpi.h](https://docs.zephyrproject.org/latest/doxygen/html/acpi_2acpi_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P075_xen_domctl_pt_irq_结构体.md) · [返回大纲](大纲.md)
