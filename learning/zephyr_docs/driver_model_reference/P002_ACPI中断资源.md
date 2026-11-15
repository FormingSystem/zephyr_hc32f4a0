---
id: learning.zephyr-docs.driver-model-reference.page-2
title: ACPI中断资源
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structacpi__irq__resource.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_ACPI中断资源

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structacpi__irq__resource.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/acpi/acpi.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 2.1\_数据成员（Data Fields）

<a id="r_ac79f9ccd199de7fa52208dee857e7e8f"></a>

```c
uint32_t flags
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[flags](#ac79f9ccd199de7fa52208dee857e7e8f)。

<a id="r_a8d5d5ddb21f52e432862cd0fb16f5f0a"></a>

```c
uint8_t irq_vector_max
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[irq_vector_max](#a8d5d5ddb21f52e432862cd0fb16f5f0a)。

<a id="r_a261bdfee8d5a1137a30bd498e1c5b3c4"></a>

```c
uint16_t * irqs
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[irqs](#a261bdfee8d5a1137a30bd498e1c5b3c4)。

## 2.2\_详细说明（Detailed Documentation）

<a id="ac79f9ccd199de7fa52208dee857e7e8f"></a>

### `flags`

```c
uint32_t acpi_irq_resource::flags
```

<a id="a8d5d5ddb21f52e432862cd0fb16f5f0a"></a>

### `irq_vector_max`

```c
uint8_t acpi_irq_resource::irq_vector_max
```

<a id="a261bdfee8d5a1137a30bd498e1c5b3c4"></a>

### `irqs`

```c
uint16_t* acpi_irq_resource::irqs
```

本结构体文档由以下文件生成：

- `zephyr/acpi/acpi.h`

## 2.3\_原页交叉引用（Cross References）

- [zephyr/acpi/acpi.h](https://docs.zephyrproject.org/latest/doxygen/html/acpi_2acpi_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P001_ACPI设备.md) · [返回大纲](大纲.md) · [下一章](P003_ACPI内存配置表.md)
