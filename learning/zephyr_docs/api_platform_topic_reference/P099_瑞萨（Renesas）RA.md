---
id: learning.zephyr-docs.api-platform-topic-reference.page-99
title: 瑞萨（Renesas）RA
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__ra__flash__ex__op.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第99章\_瑞萨（Renesas）RA

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__ra__flash__ex__op.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Renesas RA 闪存控制器的扩展操作。

<a id="details"></a>

Renesas RA 闪存控制器的扩展操作。

<a id="header-files"></a>
<a id="files"></a>

## 99.1\_文件（Files）

<a id="r_ra_5Fflash_5Fapi_5Fextensions_2Eh"></a>

```c
file ra_flash_api_extensions.h
```

相关声明：[ra_flash_api_extensions.h](../api_file_supplement_reference/P097_zephyr__drivers__flash__ra_flash_api_extensions.h_文件参考.md)。

Renesas RA闪存扩展操作（Flash Extended Operations）的头文件。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 99.2\_枚举（Enumerations）

<a id="r_ga00ad044f5928882300e87ff9a13c1f74"></a>

```c
enum ra_ex_ops { QSPI_FLASH_EX_OP_EXIT_QPI = 1 }
```

相关声明：[ra_ex_ops](#ga00ad044f5928882300e87ff9a13c1f74)、[QSPI_FLASH_EX_OP_EXIT_QPI](#gga00ad044f5928882300e87ff9a13c1f74ab955683b469ec4f2d77f202896ccad3b)。

Renesas RA 闪存扩展操作（Flash Extended Operations）的枚举（Enumeration）。

## 99.3\_详细说明（Detailed Documentation）

<a id="ga00ad044f5928882300e87ff9a13c1f74"></a>

### `ra_ex_ops`

```c
enum ra_ex_ops
```

```c
#include <zephyr/drivers/flash/ra_flash_api_extensions.h>
```

Renesas RA 闪存扩展操作（Flash Extended Operations）的枚举（Enumeration）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `QSPI_FLASH_EX_OP_EXIT_QPI` | 在四线外设接口模式（QPI，4-4-4）下复位闪存设备（Flash Device）。 |


## 99.4\_原页交叉引用（Cross References）

- [ra_flash_api_extensions.h](../api_file_supplement_reference/P097_zephyr__drivers__flash__ra_flash_api_extensions.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga00ad044f5928882300e87ff9a13c1f74ab955683b469ec4f2d77f202896ccad3b"></a>

---

[上一章](P098_PSI5 驱动后端 API.md) · [返回大纲](大纲.md) · [下一章](P100_FocalTech FT9001 复位控制器辅助工具（Reset controller helpers）.md)
