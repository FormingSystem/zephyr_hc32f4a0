---
id: learning.zephyr-docs.api-power-policy-topic-reference.page-6
title: IT51XXX API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__it51xxx__flash__ex__op.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_IT51XXX API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__it51xxx__flash__ex__op.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

IT51XXX 闪存控制器的扩展操作。

<a id="details"></a>

IT51XXX 闪存控制器的扩展操作。

<a id="header-files"></a>
<a id="files"></a>

## 6.1\_文件（Files）

<a id="r_it51xxx_5Fflash_5Fapi_5Fex_2Eh"></a>

```c
file it51xxx_flash_api_ex.h
```

相关声明：[it51xxx_flash_api_ex.h](../api_file_management_reference/P024_zephyr__drivers__flash__it51xxx_flash_api_ex.h_文件参考.md)。

IT51XXX扩展操作（Extended Operations）的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 6.2\_数据结构（Data Structures）

<a id="r_flash_5Fit51xxx_5Fex_5Fop_5Faddr_5Fprotection"></a>

```c
struct flash_it51xxx_ex_op_addr_protection
```

相关声明：[flash_it51xxx_ex_op_addr_protection](../system_service_model_reference/P030_flash_it51xxx_ex_op_addr_protection_结构体.md)。

闪存地址保护（Flash Address Protection）的请求/结果。

<a id="r_flash_5Fit51xxx_5Fex_5Fop_5Fwr_5Fprotect_5Flock"></a>

```c
struct flash_it51xxx_ex_op_wr_protect_lock
```

相关声明：[flash_it51xxx_ex_op_wr_protect_lock](../system_service_model_reference/P031_flash_it51xxx_ex_op_wr_protect_lock_结构体.md)。

嵌入式闪存（EFlash）写入/读取保护锁定的请求/结果。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 6.3\_宏定义（Macros）

<a id="r_gab8bf4e9c5cc81bf131038de3b465c85f"></a>

```c
#define IT51XXX_PROTECT_PATH_COUNT 3
```

相关声明：[IT51XXX_PROTECT_PATH_COUNT](#gab8bf4e9c5cc81bf131038de3b465c85f)。

支持的保护路径（protection paths）数量。

<a id="r_ga9aca094dbb96b053e4ae3278e154e024"></a>

```c
#define PROTECT_PATH_EC BIT(0)
```

相关声明：[PROTECT_PATH_EC](#ga9aca094dbb96b053e4ae3278e154e024)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

嵌入式控制器（EC）保护路径。

<a id="r_ga36c72a15e7249f7f10b804c5c6032a63"></a>

```c
#define PROTECT_PATH_HOST BIT(1)
```

相关声明：[PROTECT_PATH_HOST](#ga36c72a15e7249f7f10b804c5c6032a63)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

主机（Host）保护路径。

<a id="r_gae9029006b0dd37d903f42aa46996348a"></a>

```c
#define PROTECT_PATH_DBGR BIT(2)
```

相关声明：[PROTECT_PATH_DBGR](#gae9029006b0dd37d903f42aa46996348a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

调试器（DBGR）保护路径。

<a id="r_ga568a023173e973e827a0a0cb52ea43da"></a>

```c
#define PROTECT_PATH_ALL (PROTECT_PATH_EC | PROTECT_PATH_HOST | PROTECT_PATH_DBGR)
```

相关声明：[PROTECT_PATH_ALL](#ga568a023173e973e827a0a0cb52ea43da)、[PROTECT_PATH_EC](#ga9aca094dbb96b053e4ae3278e154e024)、[PROTECT_PATH_HOST](#ga36c72a15e7249f7f10b804c5c6032a63)、[PROTECT_PATH_DBGR](#gae9029006b0dd37d903f42aa46996348a)。

所有保护路径。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 6.4\_枚举（Enumerations）

<a id="r_ga202c4883f6d1108844399f52f7f8a650"></a>

```c
enum flash_it51xxx_ex_op { FLASH_IT51XXX_INTERNAL , FLASH_IT51XXX_EXTERNAL_FSPI_CS0 , FLASH_IT51XXX_EXTERNAL_FSPI_CS1 , FLASH_IT51XXX_ADDR_3B , FLASH_IT51XXX_ADDR_4B , FLASH_IT51XXX_WRITE_PROTECT , FLASH_IT51XXX_READ_PROTECT , FLASH_IT51XXX_WR_PROTECT_LOCK }
```

相关声明：[flash_it51xxx_ex_op](#ga202c4883f6d1108844399f52f7f8a650)、[FLASH_IT51XXX_INTERNAL](#gga202c4883f6d1108844399f52f7f8a650ae732fbd6292ab7dc340c15510a5e5cc4)、[FLASH_IT51XXX_EXTERNAL_FSPI_CS0](#gga202c4883f6d1108844399f52f7f8a650a2eaa44cde3aea200ab0cf3e09d92b492)、[FLASH_IT51XXX_EXTERNAL_FSPI_CS1](#gga202c4883f6d1108844399f52f7f8a650abceab43c2f5880c68d1307ba3b4a640d)、[FLASH_IT51XXX_ADDR_3B](#gga202c4883f6d1108844399f52f7f8a650aaf3619f6f55e8b4ecc11bce418ed042e)、[FLASH_IT51XXX_ADDR_4B](#gga202c4883f6d1108844399f52f7f8a650a1e6bb921cb7ef22edeb2e6a241a98526)、[FLASH_IT51XXX_WRITE_PROTECT](#gga202c4883f6d1108844399f52f7f8a650a3aac745c29f6fe7def99e2bfb1f92150)、[FLASH_IT51XXX_READ_PROTECT](#gga202c4883f6d1108844399f52f7f8a650a47a857da09d2086cbcec1b87cfcfab83)、[FLASH_IT51XXX_WR_PROTECT_LOCK](#gga202c4883f6d1108844399f52f7f8a650ae447c52cb768677fe02af6fc51e90e3c)。

IT51XXX 闪存扩展操作（flash extended operations）的枚举。

## 6.5\_详细说明（Detailed Documentation）

<a id="gab8bf4e9c5cc81bf131038de3b465c85f"></a>

### `IT51XXX_PROTECT_PATH_COUNT`

```c
#define IT51XXX_PROTECT_PATH_COUNT 3
```

```c
#include <zephyr/drivers/flash/it51xxx_flash_api_ex.h>
```

支持的保护路径（protection paths）数量。

<a id="ga568a023173e973e827a0a0cb52ea43da"></a>

### `PROTECT_PATH_ALL`

```c
#define PROTECT_PATH_ALL (PROTECT_PATH_EC | PROTECT_PATH_HOST | PROTECT_PATH_DBGR)
```

```c
#include <zephyr/drivers/flash/it51xxx_flash_api_ex.h>
```

所有保护路径。

<a id="gae9029006b0dd37d903f42aa46996348a"></a>

### `PROTECT_PATH_DBGR`

```c
#define PROTECT_PATH_DBGR BIT(2)
```

```c
#include <zephyr/drivers/flash/it51xxx_flash_api_ex.h>
```

调试器（DBGR）保护路径。

<a id="ga9aca094dbb96b053e4ae3278e154e024"></a>

### `PROTECT_PATH_EC`

```c
#define PROTECT_PATH_EC BIT(0)
```

```c
#include <zephyr/drivers/flash/it51xxx_flash_api_ex.h>
```

嵌入式控制器（EC）保护路径。

<a id="ga36c72a15e7249f7f10b804c5c6032a63"></a>

### `PROTECT_PATH_HOST`

```c
#define PROTECT_PATH_HOST BIT(1)
```

```c
#include <zephyr/drivers/flash/it51xxx_flash_api_ex.h>
```

主机（Host）保护路径。

<a id="ga202c4883f6d1108844399f52f7f8a650"></a>

### `flash_it51xxx_ex_op`

```c
enum flash_it51xxx_ex_op
```

```c
#include <zephyr/drivers/flash/it51xxx_flash_api_ex.h>
```

IT51XXX 闪存扩展操作（flash extended operations）的枚举。

定义 IT51XXX 闪存控制器访问的闪存设备（Flash Device），以及闪存操作所用的寻址模式（Addressing Mode）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `FLASH_IT51XXX_INTERNAL` | 访问内部 SPI 嵌入式闪存（E-flash），即集成在 IT51XXX SoC 内部的片上嵌入式 SPI 闪存。 |
| `FLASH_IT51XXX_EXTERNAL_FSPI_CS0` | 访问连接到 FSPI `CS0#` 的外部 SPI 闪存，操作对象为 IT51XXX FSPI 控制器片选 0（Chip Select 0）连接的外部闪存设备。 |
| `FLASH_IT51XXX_EXTERNAL_FSPI_CS1` | 访问连接到 FSPI `CS1#` 的外部 SPI 闪存，操作对象为 IT51XXX FSPI 控制器片选 1（Chip Select 1）连接的外部闪存设备。 |
| `FLASH_IT51XXX_ADDR_3B` | 3 字节（24 位）寻址模式（Addressing Mode）。使用 24 位地址周期，支持容量最大为 16 MB 的闪存设备。 |
| `FLASH_IT51XXX_ADDR_4B` | 4 字节（32 位）寻址模式（Addressing Mode）。支持容量大于 16 MB 的闪存设备，需要 32 位地址周期。 |
| `FLASH_IT51XXX_WRITE_PROTECT` | 写保护（Write Protection）。 |
| `FLASH_IT51XXX_READ_PROTECT` | 读保护（Read Protection）。 |
| `FLASH_IT51XXX_WR_PROTECT_LOCK` | eFlash 读／写保护锁（Write/Read Protection Lock）。 |


## 6.6\_原页交叉引用（Cross References）

- [it51xxx_flash_api_ex.h](../api_file_management_reference/P024_zephyr__drivers__flash__it51xxx_flash_api_ex.h_文件参考.md)
- [flash_it51xxx_ex_op_addr_protection](../system_service_model_reference/P030_flash_it51xxx_ex_op_addr_protection_结构体.md)
- [flash_it51xxx_ex_op_wr_protect_lock](../system_service_model_reference/P031_flash_it51xxx_ex_op_wr_protect_lock_结构体.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga202c4883f6d1108844399f52f7f8a650ae732fbd6292ab7dc340c15510a5e5cc4"></a>
<a id="gga202c4883f6d1108844399f52f7f8a650a2eaa44cde3aea200ab0cf3e09d92b492"></a>
<a id="gga202c4883f6d1108844399f52f7f8a650abceab43c2f5880c68d1307ba3b4a640d"></a>
<a id="gga202c4883f6d1108844399f52f7f8a650aaf3619f6f55e8b4ecc11bce418ed042e"></a>
<a id="gga202c4883f6d1108844399f52f7f8a650a1e6bb921cb7ef22edeb2e6a241a98526"></a>
<a id="gga202c4883f6d1108844399f52f7f8a650a3aac745c29f6fe7def99e2bfb1f92150"></a>
<a id="gga202c4883f6d1108844399f52f7f8a650a47a857da09d2086cbcec1b87cfcfab83"></a>
<a id="gga202c4883f6d1108844399f52f7f8a650ae447c52cb768677fe02af6fc51e90e3c"></a>

---

[上一章](P005_HTU31D API主题.md) · [返回大纲](大纲.md) · [下一章](P007_LPS2xDF API主题.md)
