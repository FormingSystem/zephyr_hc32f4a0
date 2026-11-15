---
id: learning.zephyr-docs.driver-model-reference.page-1
title: ACPI设备
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structacpi__dev.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_ACPI设备

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structacpi__dev.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/acpi/acpi.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 1.1\_数据成员（Data Fields）

<a id="r_ace9e72f625889d0f84caa17ee6dc8e24"></a>

```c
ACPI_HANDLE handle
```

相关声明：[handle](#ace9e72f625889d0f84caa17ee6dc8e24)。

<a id="r_a181c2fdd63f316b1d69f3cdc0d924fe2"></a>

```c
char * path
```

相关声明：[path](#a181c2fdd63f316b1d69f3cdc0d924fe2)。

<a id="r_a54c5c7c33a425b565b0e1337063a1c1a"></a>

```c
ACPI_RESOURCE * res_lst
```

相关声明：[res_lst](#a54c5c7c33a425b565b0e1337063a1c1a)。

<a id="r_abc282bce7cdc3de32feb57bc4da790e8"></a>

```c
int res_type
```

相关声明：[res_type](#abc282bce7cdc3de32feb57bc4da790e8)。

<a id="r_a521452067b5751a2a59d156b13ff24f1"></a>

```c
ACPI_DEVICE_INFO * dev_info
```

相关声明：[dev_info](#a521452067b5751a2a59d156b13ff24f1)。

## 1.2\_详细说明（Detailed Documentation）

<a id="a521452067b5751a2a59d156b13ff24f1"></a>

### `dev_info`

```c
ACPI_DEVICE_INFO* acpi_dev::dev_info
```

<a id="ace9e72f625889d0f84caa17ee6dc8e24"></a>

### `handle`

```c
ACPI_HANDLE acpi_dev::handle
```

<a id="a181c2fdd63f316b1d69f3cdc0d924fe2"></a>

### `path`

```c
char* acpi_dev::path
```

<a id="a54c5c7c33a425b565b0e1337063a1c1a"></a>

### `res_lst`

```c
ACPI_RESOURCE* acpi_dev::res_lst
```

<a id="abc282bce7cdc3de32feb57bc4da790e8"></a>

### `res_type`

```c
int acpi_dev::res_type
```

本结构体文档由以下文件生成：

- `zephyr/acpi/acpi.h`

## 1.3\_原页交叉引用（Cross References）

- [zephyr/acpi/acpi.h](https://docs.zephyrproject.org/latest/doxygen/html/acpi_2acpi_8h_source.html)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_ACPI中断资源.md)
