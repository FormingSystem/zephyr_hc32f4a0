---
id: learning.zephyr-docs.api-file-runtime-reference.page-46
title: zephyr__drivers__flash__nrf_qspi_nor.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nrf__qspi__nor_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第46章\_zephyr\_\_drivers\_\_flash\_\_nrf\_qspi\_nor.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/nrf__qspi__nor_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/syscalls/nrf_qspi_nor.h>
```

查看此文件的源码。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 46.1\_函数（Functions）

<a id="r_abfe75f149d6a54c7fefe9d3a2ed21ea3"></a>

```c
void nrf_qspi_nor_xip_enable (const struct device *dev, bool enable)
```

相关声明：[nrf_qspi_nor_xip_enable](#abfe75f149d6a54c7fefe9d3a2ed21ea3)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

指定是否允许就地执行操作（Execute in Place，XIP）。

## 46.2\_详细说明（Detailed Documentation）

<a id="abfe75f149d6a54c7fefe9d3a2ed21ea3"></a>

### `nrf_qspi_nor_xip_enable()`

```c
void nrf_qspi_nor_xip_enable ( const struct device * dev, bool enable )
```

指定是否允许就地执行操作（Execute in Place，XIP）。

通常，驱动会在不进行 QSPI 操作的期间停用 QSPI 外设（Peripheral），以避免外设空闲（Idle）时产生额外电流消耗。出于同样原因，nRF53 系列片上系统（SoCs）的基础时钟（Base Clock）`HFCLK192M` 在这些期间会配置为默认的四分频（/4 Divider），而在其他时候不能使用该分频设置。但是，使用就地执行访问（XIP Accesses）时，必须阻止驱动执行上述两种操作，否则 XIP 会失败。因此，应用程序应使用本函数通知驱动即将发生 XIP 访问，让驱动保持 QSPI 外设可工作（Operable）。不再需要 XIP 操作时，应使用本函数禁用它。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 闪存设备。 |
| `enable` | 若为 `true`，驱动启用就地执行操作（XIP Operation），并抑制会导致 XIP 失败的空闲操作（Idle Actions）。 |


## 46.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P601_nrf_qspi_nor.h_源码浏览.md)
- [device](../device_reference/P002_设备对象结构.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)

<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P045_zephyr__drivers__flash__npcx_flash_api_ex.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P047_zephyr__dt-bindings__gpio__numicro-gpio.h_文件参考.md)
