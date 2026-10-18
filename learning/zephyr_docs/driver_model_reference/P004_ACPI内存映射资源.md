---
id: learning.zephyr-docs.driver-model-reference.page-4
title: ACPI内存映射资源
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structacpi__mmio__resource.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_ACPI内存映射资源

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structacpi__mmio__resource.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/acpi/acpi.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 4.1\_数据成员（Data Fields）

<a id="r_a26d31589732a487adbe7b2ab862c4ff4"></a>

```c
uint8_t mmio_max
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mmio_max](#a26d31589732a487adbe7b2ab862c4ff4)。

<a id="r_ae4ab8715b8f13fa57bc983393c8bd5e6"></a>

```c
struct acpi_reg_base * reg_base
```

相关声明：[acpi_reg_base](P005_ACPI寄存器基址.md)、[reg_base](#ae4ab8715b8f13fa57bc983393c8bd5e6)。

## 4.2\_详细说明（Detailed Documentation）

<a id="a26d31589732a487adbe7b2ab862c4ff4"></a>

### `mmio_max`

```c
uint8_t acpi_mmio_resource::mmio_max
```

<a id="ae4ab8715b8f13fa57bc983393c8bd5e6"></a>

### `reg_base`

```c
struct acpi_reg_base* acpi_mmio_resource::reg_base
```

本结构体文档由以下文件生成：

- `zephyr/acpi/acpi.h`

## 4.3\_原页交叉引用（Cross References）

- [zephyr/acpi/acpi.h](https://docs.zephyrproject.org/latest/doxygen/html/acpi_2acpi_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [acpi_reg_base](P005_ACPI寄存器基址.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P003_ACPI内存配置表.md) · [返回大纲](大纲.md) · [下一章](P005_ACPI寄存器基址.md)
