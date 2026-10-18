---
id: learning.zephyr-docs.api-file-management-reference.page-24
title: zephyr__drivers__flash__it51xxx_flash_api_ex.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/it51xxx__flash__api__ex_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第24章\_zephyr\_\_drivers\_\_flash\_\_it51xxx\_flash\_api\_ex.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/it51xxx__flash__api__ex_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

IT51XXX扩展操作（Extended Operations）的头文件。

<a id="details"></a>

```c
#include <zephyr/drivers/flash.h>
```

查看此文件的源码。

IT51XXX扩展操作（Extended Operations）的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 24.1\_数据结构（Data Structures）

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

## 24.2\_宏定义（Macros）

<a id="r_gab8bf4e9c5cc81bf131038de3b465c85f"></a>

```c
#define IT51XXX_PROTECT_PATH_COUNT 3
```

相关声明：[IT51XXX_PROTECT_PATH_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__it51xxx__flash__ex__op.html#gab8bf4e9c5cc81bf131038de3b465c85f)。

支持的保护路径（protection paths）数量。

<a id="r_ga9aca094dbb96b053e4ae3278e154e024"></a>

```c
#define PROTECT_PATH_EC BIT(0)
```

相关声明：[PROTECT_PATH_EC](https://docs.zephyrproject.org/latest/doxygen/html/group__it51xxx__flash__ex__op.html#ga9aca094dbb96b053e4ae3278e154e024)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

嵌入式控制器（EC）保护路径。

<a id="r_ga36c72a15e7249f7f10b804c5c6032a63"></a>

```c
#define PROTECT_PATH_HOST BIT(1)
```

相关声明：[PROTECT_PATH_HOST](https://docs.zephyrproject.org/latest/doxygen/html/group__it51xxx__flash__ex__op.html#ga36c72a15e7249f7f10b804c5c6032a63)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

主机（Host）保护路径。

<a id="r_gae9029006b0dd37d903f42aa46996348a"></a>

```c
#define PROTECT_PATH_DBGR BIT(2)
```

相关声明：[PROTECT_PATH_DBGR](https://docs.zephyrproject.org/latest/doxygen/html/group__it51xxx__flash__ex__op.html#gae9029006b0dd37d903f42aa46996348a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

调试器（DBGR）保护路径。

<a id="r_ga568a023173e973e827a0a0cb52ea43da"></a>

```c
#define PROTECT_PATH_ALL (PROTECT_PATH_EC | PROTECT_PATH_HOST | PROTECT_PATH_DBGR)
```

相关声明：[PROTECT_PATH_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__it51xxx__flash__ex__op.html#ga568a023173e973e827a0a0cb52ea43da)、[PROTECT_PATH_EC](https://docs.zephyrproject.org/latest/doxygen/html/group__it51xxx__flash__ex__op.html#ga9aca094dbb96b053e4ae3278e154e024)、[PROTECT_PATH_HOST](https://docs.zephyrproject.org/latest/doxygen/html/group__it51xxx__flash__ex__op.html#ga36c72a15e7249f7f10b804c5c6032a63)、[PROTECT_PATH_DBGR](https://docs.zephyrproject.org/latest/doxygen/html/group__it51xxx__flash__ex__op.html#gae9029006b0dd37d903f42aa46996348a)。

所有保护路径。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 24.3\_枚举（Enumerations）

<a id="r_ga202c4883f6d1108844399f52f7f8a650"></a>

```c
enum flash_it51xxx_ex_op { FLASH_IT51XXX_INTERNAL , FLASH_IT51XXX_EXTERNAL_FSPI_CS0 , FLASH_IT51XXX_EXTERNAL_FSPI_CS1 , FLASH_IT51XXX_ADDR_3B , FLASH_IT51XXX_ADDR_4B , FLASH_IT51XXX_WRITE_PROTECT , FLASH_IT51XXX_READ_PROTECT , FLASH_IT51XXX_WR_PROTECT_LOCK }
```

相关声明：[flash_it51xxx_ex_op](https://docs.zephyrproject.org/latest/doxygen/html/group__it51xxx__flash__ex__op.html#ga202c4883f6d1108844399f52f7f8a650)、[FLASH_IT51XXX_INTERNAL](https://docs.zephyrproject.org/latest/doxygen/html/group__it51xxx__flash__ex__op.html#gga202c4883f6d1108844399f52f7f8a650ae732fbd6292ab7dc340c15510a5e5cc4)、[FLASH_IT51XXX_EXTERNAL_FSPI_CS0](https://docs.zephyrproject.org/latest/doxygen/html/group__it51xxx__flash__ex__op.html#gga202c4883f6d1108844399f52f7f8a650a2eaa44cde3aea200ab0cf3e09d92b492)、[FLASH_IT51XXX_EXTERNAL_FSPI_CS1](https://docs.zephyrproject.org/latest/doxygen/html/group__it51xxx__flash__ex__op.html#gga202c4883f6d1108844399f52f7f8a650abceab43c2f5880c68d1307ba3b4a640d)、[FLASH_IT51XXX_ADDR_3B](https://docs.zephyrproject.org/latest/doxygen/html/group__it51xxx__flash__ex__op.html#gga202c4883f6d1108844399f52f7f8a650aaf3619f6f55e8b4ecc11bce418ed042e)、[FLASH_IT51XXX_ADDR_4B](https://docs.zephyrproject.org/latest/doxygen/html/group__it51xxx__flash__ex__op.html#gga202c4883f6d1108844399f52f7f8a650a1e6bb921cb7ef22edeb2e6a241a98526)、[FLASH_IT51XXX_WRITE_PROTECT](https://docs.zephyrproject.org/latest/doxygen/html/group__it51xxx__flash__ex__op.html#gga202c4883f6d1108844399f52f7f8a650a3aac745c29f6fe7def99e2bfb1f92150)、[FLASH_IT51XXX_READ_PROTECT](https://docs.zephyrproject.org/latest/doxygen/html/group__it51xxx__flash__ex__op.html#gga202c4883f6d1108844399f52f7f8a650a47a857da09d2086cbcec1b87cfcfab83)、[FLASH_IT51XXX_WR_PROTECT_LOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__it51xxx__flash__ex__op.html#gga202c4883f6d1108844399f52f7f8a650ae447c52cb768677fe02af6fc51e90e3c)。

IT51XXX 闪存扩展操作（flash extended operations）的枚举。


## 24.4\_原页交叉引用（Cross References）

- [zephyr/drivers/flash.h](../flash_reference/P010_Flash公共头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P417_it51xxx_flash_api_ex.h_源码浏览.md)
- [flash_it51xxx_ex_op_addr_protection](../system_service_model_reference/P030_flash_it51xxx_ex_op_addr_protection_结构体.md)
- [flash_it51xxx_ex_op_wr_protect_lock](../system_service_model_reference/P031_flash_it51xxx_ex_op_wr_protect_lock_结构体.md)
- [IT51XXX_PROTECT_PATH_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__it51xxx__flash__ex__op.html#gab8bf4e9c5cc81bf131038de3b465c85f)
- [PROTECT_PATH_EC](https://docs.zephyrproject.org/latest/doxygen/html/group__it51xxx__flash__ex__op.html#ga9aca094dbb96b053e4ae3278e154e024)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [PROTECT_PATH_HOST](https://docs.zephyrproject.org/latest/doxygen/html/group__it51xxx__flash__ex__op.html#ga36c72a15e7249f7f10b804c5c6032a63)
- [PROTECT_PATH_DBGR](https://docs.zephyrproject.org/latest/doxygen/html/group__it51xxx__flash__ex__op.html#gae9029006b0dd37d903f42aa46996348a)
- [PROTECT_PATH_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__it51xxx__flash__ex__op.html#ga568a023173e973e827a0a0cb52ea43da)
- [flash_it51xxx_ex_op](https://docs.zephyrproject.org/latest/doxygen/html/group__it51xxx__flash__ex__op.html#ga202c4883f6d1108844399f52f7f8a650)
- [FLASH_IT51XXX_INTERNAL](https://docs.zephyrproject.org/latest/doxygen/html/group__it51xxx__flash__ex__op.html#gga202c4883f6d1108844399f52f7f8a650ae732fbd6292ab7dc340c15510a5e5cc4)
- [FLASH_IT51XXX_EXTERNAL_FSPI_CS0](https://docs.zephyrproject.org/latest/doxygen/html/group__it51xxx__flash__ex__op.html#gga202c4883f6d1108844399f52f7f8a650a2eaa44cde3aea200ab0cf3e09d92b492)
- [FLASH_IT51XXX_EXTERNAL_FSPI_CS1](https://docs.zephyrproject.org/latest/doxygen/html/group__it51xxx__flash__ex__op.html#gga202c4883f6d1108844399f52f7f8a650abceab43c2f5880c68d1307ba3b4a640d)
- [FLASH_IT51XXX_ADDR_3B](https://docs.zephyrproject.org/latest/doxygen/html/group__it51xxx__flash__ex__op.html#gga202c4883f6d1108844399f52f7f8a650aaf3619f6f55e8b4ecc11bce418ed042e)
- [FLASH_IT51XXX_ADDR_4B](https://docs.zephyrproject.org/latest/doxygen/html/group__it51xxx__flash__ex__op.html#gga202c4883f6d1108844399f52f7f8a650a1e6bb921cb7ef22edeb2e6a241a98526)
- [FLASH_IT51XXX_WRITE_PROTECT](https://docs.zephyrproject.org/latest/doxygen/html/group__it51xxx__flash__ex__op.html#gga202c4883f6d1108844399f52f7f8a650a3aac745c29f6fe7def99e2bfb1f92150)
- [FLASH_IT51XXX_READ_PROTECT](https://docs.zephyrproject.org/latest/doxygen/html/group__it51xxx__flash__ex__op.html#gga202c4883f6d1108844399f52f7f8a650a47a857da09d2086cbcec1b87cfcfab83)
- [FLASH_IT51XXX_WR_PROTECT_LOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__it51xxx__flash__ex__op.html#gga202c4883f6d1108844399f52f7f8a650ae447c52cb768677fe02af6fc51e90e3c)

<a id="header-details"></a>

---

[上一章](P023_zephyr__drivers__i2c__i2c_nrfx_twim.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P025_zephyr__net__ssh__keygen.h_文件参考.md)
