---
id: learning.zephyr-docs.peripheral-bus-storage-header-reference.page-18
title: zephyr__drivers__mspi__mspi_dw.h_头文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mspi__dw_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_zephyr\_\_drivers\_\_mspi\_\_mspi\_dw.h\_头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mspi__dw_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 18.1\_数据结构（Data Structures）

<a id="r_mspi_5Fdw_5Ftiming_5Fcfg"></a>

```c
struct mspi_dw_timing_cfg
```

相关声明：[mspi_dw_timing_cfg](../peripheral_bus_storage_model_reference/P044_mspi_dw_timing_cfg_结构体.md)。

Designware MSPI配置结构；调用mspi_timing_config时应将其传递给MSPI驱动。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 18.2\_宏定义（Macros）

<a id="r_af16490f55a7e32cf65bc76e8fff2ba95"></a>

```c
#define MSPI_DW_RX_TIMING_CFG BIT(0)
```

相关声明：[MSPI_DW_RX_TIMING_CFG](#af16490f55a7e32cf65bc76e8fff2ba95)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

## 18.3\_详细说明（Detailed Documentation）

<a id="af16490f55a7e32cf65bc76e8fff2ba95"></a>

### `MSPI_DW_RX_TIMING_CFG`

```c
#define MSPI_DW_RX_TIMING_CFG BIT(0)
```


## 18.4\_原页交叉引用（Cross References）

- [查看此文件的源码](https://docs.zephyrproject.org/latest/doxygen/html/mspi__dw_8h_source.html)
- [mspi_dw_timing_cfg](../peripheral_bus_storage_model_reference/P044_mspi_dw_timing_cfg_结构体.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P017_zephyr__drivers__mspi.h_头文件参考.md) · [返回大纲](大纲.md) · [下一章](P019_zephyr__drivers__mux.h_头文件参考.md)
