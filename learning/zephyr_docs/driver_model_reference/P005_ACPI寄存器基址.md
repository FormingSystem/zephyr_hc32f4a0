---
id: learning.zephyr-docs.driver-model-reference.page-5
title: ACPI寄存器基址
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structacpi__reg__base.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_ACPI寄存器基址

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structacpi__reg__base.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/acpi/acpi.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 5.1\_数据成员（Data Fields）

<a id="r_a416f2ff166b33add65eba5e7787c3ef5"></a>

```c
enum acpi_res_type type
```

相关声明：[acpi_res_type](https://docs.zephyrproject.org/latest/doxygen/html/acpi_2acpi_8h.html#a225bfac5f9770bd826ae98d2bbbbfc5b)、[type](#a416f2ff166b33add65eba5e7787c3ef5)。

```c
union {
```

<a id="r_a56bd66dd12d16408fe62231c071da3d0"></a>

```c
uintptr_t mmio
```

相关声明：[uintptr_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a4788399d1d0b37ccf098a7da82254808)、[mmio](#ada6ffb943e406068271d56b5a129b717)。

<a id="r_a3c69902b505542554efbbde2cde7275f"></a>

```c
uintptr_t port
```

相关声明：[uintptr_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a4788399d1d0b37ccf098a7da82254808)、[port](#ab845df09e3b4b9734103605ea7c65d1e)。

<a id="r_ad56cc48ac58fbc87410fe2960192cbac"></a>

```c
};
```

<a id="r_aaca25908e4e16a71627c48208c55d0ef"></a>

```c
uint32_t length
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[length](#aaca25908e4e16a71627c48208c55d0ef)。

## 5.2\_详细说明（Detailed Documentation）

<a id="ad56cc48ac58fbc87410fe2960192cbac"></a>

### `[union]`

```c
union { ... } acpi_reg_base
```

<a id="aaca25908e4e16a71627c48208c55d0ef"></a>

### `length`

```c
uint32_t acpi_reg_base::length
```

<a id="ada6ffb943e406068271d56b5a129b717"></a>

### `mmio`

```c
uintptr_t acpi_reg_base::mmio
```

<a id="ab845df09e3b4b9734103605ea7c65d1e"></a>

### `port`

```c
uintptr_t acpi_reg_base::port
```

<a id="a416f2ff166b33add65eba5e7787c3ef5"></a>

### `type`

```c
enum acpi_res_type acpi_reg_base::type
```

本结构体文档由以下文件生成：

- `zephyr/acpi/acpi.h`

## 5.3\_原页交叉引用（Cross References）

- [zephyr/acpi/acpi.h](https://docs.zephyrproject.org/latest/doxygen/html/acpi_2acpi_8h_source.html)
- [acpi_res_type](https://docs.zephyrproject.org/latest/doxygen/html/acpi_2acpi_8h.html#a225bfac5f9770bd826ae98d2bbbbfc5b)
- [uintptr_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a4788399d1d0b37ccf098a7da82254808)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [acpi_reg_base](P005_ACPI寄存器基址.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P004_ACPI内存映射资源.md) · [返回大纲](大纲.md) · [下一章](P006_地址转换区域配置.md)
