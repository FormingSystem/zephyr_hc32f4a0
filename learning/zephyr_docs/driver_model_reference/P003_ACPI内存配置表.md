---
id: learning.zephyr-docs.driver-model-reference.page-3
title: ACPI内存配置表
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structacpi__mcfg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_ACPI内存配置表

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structacpi__mcfg.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/acpi/acpi.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 3.1\_数据成员（Data Fields）

<a id="r_ac3745fb726a32a57992556b9dbaa1365"></a>

```c
ACPI_TABLE_HEADER header
```

相关声明：[header](#ac3745fb726a32a57992556b9dbaa1365)。

<a id="r_a8d6bc322dcb14c2892382067275f2426"></a>

```c
ACPI_MCFG_ALLOCATION pci_segs []
```

相关声明：[pci_segs](#a8d6bc322dcb14c2892382067275f2426)。

## 3.2\_详细说明（Detailed Documentation）

<a id="ac3745fb726a32a57992556b9dbaa1365"></a>

### `header`

```c
ACPI_TABLE_HEADER acpi_mcfg::header
```

<a id="a8d6bc322dcb14c2892382067275f2426"></a>

### `pci_segs`

```c
ACPI_MCFG_ALLOCATION acpi_mcfg::pci_segs[]
```

本结构体文档由以下文件生成：

- `zephyr/acpi/acpi.h`

## 3.3\_原页交叉引用（Cross References）

- [zephyr/acpi/acpi.h](https://docs.zephyrproject.org/latest/doxygen/html/acpi_2acpi_8h_source.html)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P002_ACPI中断资源.md) · [返回大纲](大纲.md) · [下一章](P004_ACPI内存映射资源.md)
