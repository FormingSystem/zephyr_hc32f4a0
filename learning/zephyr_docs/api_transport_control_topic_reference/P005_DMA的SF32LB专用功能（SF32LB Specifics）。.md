---
id: learning.zephyr-docs.api-transport-control-topic-reference.page-5
title: DMA的SF32LB专用功能（SF32LB Specifics）。
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__dma__sf32lb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_DMA的SF32LB专用功能（SF32LB Specifics）。

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__sf32lb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

DMA的SF32LB专用功能（SF32LB Specifics）。

<a id="details"></a>

DMA的SF32LB专用功能（SF32LB Specifics）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 5.1\_数据结构（Data Structures）

<a id="r_sf32lb_5Fdma_5Fdt_5Fspec"></a>

```c
struct sf32lb_dma_dt_spec
```

相关声明：[sf32lb_dma_dt_spec](../device_power_control_model_reference/P086_sf32lb_dma_dt_spec_结构体.md)。

SF32LB直接内存访问的设备树规格（DMA DT Spec）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 5.2\_宏定义（Macros）

<a id="r_gafe8cf86b36b9741dd069b296bf2dfbdf"></a>

```c
#define SF32LB_DMA_DT_SPEC_GET(node_id)
```

相关声明：[SF32LB_DMA_DT_SPEC_GET](#gafe8cf86b36b9741dd069b296bf2dfbdf)。

根据设备树节点（DT Node）初始化 `sf32lb_dma_dt_spec` 结构体。

<a id="r_gaf9f8a7a13b1c806aa182e917c99cacaf"></a>

```c
#define SF32LB_DMA_DT_SPEC_GET_BY_NAME(node_id, name)
```

相关声明：[SF32LB_DMA_DT_SPEC_GET_BY_NAME](#gaf9f8a7a13b1c806aa182e917c99cacaf)。

根据设备树节点（DT Node）初始化 `sf32lb_dma_dt_spec` 结构体。

<a id="r_gacb66db47cfc3b7bf06ca1323de291611"></a>

```c
#define SF32LB_DMA_DT_SPEC_GET_BY_NAME_OR(node_id, name, default_value)
```

相关声明：[SF32LB_DMA_DT_SPEC_GET_BY_NAME_OR](#gacb66db47cfc3b7bf06ca1323de291611)。

根据设备树节点（DT Node）初始化 `sf32lb_dma_dt_spec` 结构体，必要时回退到默认值（Default Values）。

<a id="r_gafac07cb5115b1e38d3894a9d63267b94"></a>

```c
#define SF32LB_DMA_DT_INST_SPEC_GET(index)
```

相关声明：[SF32LB_DMA_DT_INST_SPEC_GET](#gafac07cb5115b1e38d3894a9d63267b94)。

根据设备树实例（DT Instance）初始化 `sf32lb_dma_dt_spec` 结构体。

<a id="r_ga81ecab737bf1dbe44c4ec49dc7a42cb4"></a>

```c
#define SF32LB_DMA_DT_INST_SPEC_GET_BY_NAME(index, name)
```

相关声明：[SF32LB_DMA_DT_INST_SPEC_GET_BY_NAME](#ga81ecab737bf1dbe44c4ec49dc7a42cb4)。

根据设备树实例（DT Instance）初始化 `sf32lb_dma_dt_spec` 结构体。

<a id="r_ga0acc6ba43d7b7e77218110b0e3fb5777"></a>

```c
#define SF32LB_DMA_DT_INST_SPEC_GET_BY_NAME_OR(index, name, default_value)
```

相关声明：[SF32LB_DMA_DT_INST_SPEC_GET_BY_NAME_OR](#ga0acc6ba43d7b7e77218110b0e3fb5777)。

根据设备树实例（DT Instance）初始化 `sf32lb_dma_dt_spec` 结构体。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 5.3\_函数（Functions）

<a id="r_ga6a55283d1c080695e9b6130bd86da8b2"></a>

```c
static bool sf32lb_dma_is_ready_dt (const struct sf32lb_dma_dt_spec *spec)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[sf32lb_dma_is_ready_dt](#ga6a55283d1c080695e9b6130bd86da8b2)、[sf32lb_dma_dt_spec](../device_power_control_model_reference/P086_sf32lb_dma_dt_spec_结构体.md)。

检查 DMA 控制器（Controller）是否就绪。

<a id="r_ga15960e506ac44ea925a84b29730f94dd"></a>

```c
static void sf32lb_dma_config_init_dt (const struct sf32lb_dma_dt_spec *spec, struct dma_config *config)
```

相关声明：[sf32lb_dma_config_init_dt](#ga15960e506ac44ea925a84b29730f94dd)、[sf32lb_dma_dt_spec](../device_power_control_model_reference/P086_sf32lb_dma_dt_spec_结构体.md)、[dma_config](../dma_reference/P004_DMA通道配置.md)。

根据设备树规格（DT Spec）初始化 DMA 配置结构体。

<a id="r_ga4e70429d274e376e6152291aa6815e56"></a>

```c
static int sf32lb_dma_config_dt (const struct sf32lb_dma_dt_spec *spec, struct dma_config *config)
```

相关声明：[sf32lb_dma_config_dt](#ga4e70429d274e376e6152291aa6815e56)、[sf32lb_dma_dt_spec](../device_power_control_model_reference/P086_sf32lb_dma_dt_spec_结构体.md)、[dma_config](../dma_reference/P004_DMA通道配置.md)。

根据设备树规格（DT Spec）配置 DMA 通道（Channel）。

<a id="r_ga4aac7edfd591224b08956a1aab6e4c7c"></a>

```c
static int sf32lb_dma_start_dt (const struct sf32lb_dma_dt_spec *spec)
```

相关声明：[sf32lb_dma_start_dt](#ga4aac7edfd591224b08956a1aab6e4c7c)、[sf32lb_dma_dt_spec](../device_power_control_model_reference/P086_sf32lb_dma_dt_spec_结构体.md)。

根据设备树规格（DT Spec）启动 DMA 传输（Transfer）。

<a id="r_ga7d9763ae4042d855718a855955faef78"></a>

```c
static int sf32lb_dma_stop_dt (const struct sf32lb_dma_dt_spec *spec)
```

相关声明：[sf32lb_dma_stop_dt](#ga7d9763ae4042d855718a855955faef78)、[sf32lb_dma_dt_spec](../device_power_control_model_reference/P086_sf32lb_dma_dt_spec_结构体.md)。

根据设备树规格（DT Spec）停止 DMA 传输（Transfer）。

<a id="r_gab6dd22ab9a477e8fb450d8197c15a280"></a>

```c
static int sf32lb_dma_reload_dt (const struct sf32lb_dma_dt_spec *spec, uintptr_t src, uintptr_t dst, size_t size)
```

相关声明：[sf32lb_dma_reload_dt](#gab6dd22ab9a477e8fb450d8197c15a280)、[sf32lb_dma_dt_spec](../device_power_control_model_reference/P086_sf32lb_dma_dt_spec_结构体.md)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)。

根据设备树规格（DT Spec）重新装载 DMA 传输（Reload Transfer）。

<a id="r_ga6ca2f3a9b69b930552d0704bc562f01f"></a>

```c
static int sf32lb_dma_get_status_dt (const struct sf32lb_dma_dt_spec *spec, struct dma_status *status)
```

相关声明：[sf32lb_dma_get_status_dt](#ga6ca2f3a9b69b930552d0704bc562f01f)、[sf32lb_dma_dt_spec](../device_power_control_model_reference/P086_sf32lb_dma_dt_spec_结构体.md)、[dma_status](../dma_reference/P005_DMA运行状态.md)。

根据设备树规格（DT Spec）获取 DMA 传输状态（Transfer Status）。

## 5.4\_详细说明（Detailed Documentation）

<a id="gafac07cb5115b1e38d3894a9d63267b94"></a>

### `SF32LB_DMA_DT_INST_SPEC_GET`

```c
#define SF32LB_DMA_DT_INST_SPEC_GET ( index)
```

```c
#include <zephyr/drivers/dma/sf32lb.h>
```

展开值（Value）：

```c
SF32LB_DMA_DT_SPEC_GET(DT_DRV_INST(index))
```

根据设备树实例（DT Instance）初始化 `sf32lb_dma_dt_spec` 结构体。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `index` | 设备树实例索引（DT Instance Index）。 |

<a id="ga81ecab737bf1dbe44c4ec49dc7a42cb4"></a>

### `SF32LB_DMA_DT_INST_SPEC_GET_BY_NAME`

```c
#define SF32LB_DMA_DT_INST_SPEC_GET_BY_NAME ( index, name )
```

```c
#include <zephyr/drivers/dma/sf32lb.h>
```

展开值（Value）：

```c
SF32LB_DMA_DT_SPEC_GET_BY_NAME(DT_DRV_INST(index), name)
```

根据设备树实例（DT Instance）初始化 `sf32lb_dma_dt_spec` 结构体。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `index` | 设备树实例索引（DT Instance Index）。 |
| `name` | DMA 名称（Name）。 |

<a id="ga0acc6ba43d7b7e77218110b0e3fb5777"></a>

### `SF32LB_DMA_DT_INST_SPEC_GET_BY_NAME_OR`

```c
#define SF32LB_DMA_DT_INST_SPEC_GET_BY_NAME_OR ( index, name, default_value )
```

```c
#include <zephyr/drivers/dma/sf32lb.h>
```

展开值（Value）：

```c
SF32LB_DMA_DT_SPEC_GET_BY_NAME_OR(DT_DRV_INST(index), name, default_value)
```

根据设备树实例（DT Instance）初始化 `sf32lb_dma_dt_spec` 结构体。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `index` | 设备树实例索引（DT Instance Index）。 |
| `name` | DMA 名称（Name）。 |
| `default_value` | 缺失单元（Cells）的默认值。 |

<a id="gafe8cf86b36b9741dd069b296bf2dfbdf"></a>

### `SF32LB_DMA_DT_SPEC_GET`

```c
#define SF32LB_DMA_DT_SPEC_GET ( node_id)
```

```c
#include <zephyr/drivers/dma/sf32lb.h>
```

展开值（Value）：

```c
{                                                                                          \
        .dev = DEVICE_DT_GET(DT_DMAS_CTLR(node_id)),                                       \
        .channel = DT_DMAS_CELL_BY_IDX(node_id, 0, channel),                               \
        .request = DT_DMAS_CELL_BY_IDX(node_id, 0, request),                               \
        .config = DT_DMAS_CELL_BY_IDX(node_id, 0, config),                                 \
}
```

根据设备树节点（DT Node）初始化 `sf32lb_dma_dt_spec` 结构体。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 设备树节点标识符（DT Node Identifier）。 |

<a id="gaf9f8a7a13b1c806aa182e917c99cacaf"></a>

### `SF32LB_DMA_DT_SPEC_GET_BY_NAME`

```c
#define SF32LB_DMA_DT_SPEC_GET_BY_NAME ( node_id, name )
```

```c
#include <zephyr/drivers/dma/sf32lb.h>
```

展开值（Value）：

```c
{                                                                                          \
        .dev = DEVICE_DT_GET(DT_DMAS_CTLR_BY_NAME(node_id, name)),                         \
        .channel = DT_DMAS_CELL_BY_NAME(node_id, name, channel),                           \
        .request = DT_DMAS_CELL_BY_NAME(node_id, name, request),                           \
        .config = DT_DMAS_CELL_BY_NAME(node_id, name, config),                             \
}
```

根据设备树节点（DT Node）初始化 `sf32lb_dma_dt_spec` 结构体。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 设备树节点标识符（DT Node Identifier）。 |

<a id="gacb66db47cfc3b7bf06ca1323de291611"></a>

### `SF32LB_DMA_DT_SPEC_GET_BY_NAME_OR`

```c
#define SF32LB_DMA_DT_SPEC_GET_BY_NAME_OR ( node_id, name, default_value )
```

```c
#include <zephyr/drivers/dma/sf32lb.h>
```

展开值（Value）：

```c
COND_CODE_1(DT_DMAS_HAS_NAME(node_id, name),                                               \
        (SF32LB_DMA_DT_SPEC_GET_BY_NAME(node_id, name)), (default_value))
```

根据设备树节点（DT Node）初始化 `sf32lb_dma_dt_spec` 结构体，必要时回退到默认值（Default Values）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 设备树节点标识符（DT Node Identifier）。 |
| `name` | dmas元素的名称，由节点的dma-names属性定义，以小写字母与下划线形式传入。 |
| `default_value` | 要展开成的回退值。 |

<a id="ga4e70429d274e376e6152291aa6815e56"></a>

### `sf32lb_dma_config_dt()`

```c
int sf32lb_dma_config_dt ( const struct sf32lb_dma_dt_spec * spec, struct dma_config * config )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/dma/sf32lb.h>
```

根据设备树规格（DT Spec）配置 DMA 通道（Channel）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `spec` | SF32LB直接内存访问的设备树规格（DMA DT Spec）。 |
| `config` | DMA 配置。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOTSUP` | 不支持该配置（Configuration）。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga15960e506ac44ea925a84b29730f94dd"></a>

### `sf32lb_dma_config_init_dt()`

```c
void sf32lb_dma_config_init_dt ( const struct sf32lb_dma_dt_spec * spec, struct dma_config * config )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/dma/sf32lb.h>
```

根据设备树规格（DT Spec）初始化 DMA 配置结构体。

本函数设置 `dma_config` 结构体中的以下字段（Fields）：

- `dma_slot`（DMA 槽位）。
- `channel_priority`（通道优先级）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` spec` | SF32LB直接内存访问的设备树规格（DMA DT Spec）。 |
| `[out] config` | DMA 配置。 |

<a id="ga6ca2f3a9b69b930552d0704bc562f01f"></a>

### `sf32lb_dma_get_status_dt()`

```c
int sf32lb_dma_get_status_dt ( const struct sf32lb_dma_dt_spec * spec, struct dma_status * status )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/dma/sf32lb.h>
```

根据设备树规格（DT Spec）获取 DMA 传输状态（Transfer Status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` spec` | SF32LB直接内存访问的设备树规格（DMA DT Spec）。 |
| `[out] status` | 状态输出（Status Output）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负 `errno`；参见 `dma_get_status()`。

<a id="ga6a55283d1c080695e9b6130bd86da8b2"></a>

### `sf32lb_dma_is_ready_dt()`

```c
bool sf32lb_dma_is_ready_dt ( const struct sf32lb_dma_dt_spec * spec)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/dma/sf32lb.h>
```

检查 DMA 控制器（Controller）是否就绪。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `spec` | SF32LB直接内存访问的设备树规格（DMA DT Spec）。 |

**返回（Returns）**：**返回值（Returns）：**DMA 控制器就绪（Ready）返回 `true`，未就绪返回 `false`。

<a id="gab6dd22ab9a477e8fb450d8197c15a280"></a>

### `sf32lb_dma_reload_dt()`

```c
int sf32lb_dma_reload_dt ( const struct sf32lb_dma_dt_spec * spec, uintptr_t src, uintptr_t dst, size_t size )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/dma/sf32lb.h>
```

根据设备树规格（DT Spec）重新装载 DMA 传输（Reload Transfer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `spec` | SF32LB直接内存访问的设备树规格（DMA DT Spec）。 |
| `src` | 源地址。 |
| `dst` | 目的地址（Destination Address）。 |
| `size` | 传输大小（Transfer Size）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负 `errno`；参见 `dma_reload()`。

<a id="ga4aac7edfd591224b08956a1aab6e4c7c"></a>

### `sf32lb_dma_start_dt()`

```c
int sf32lb_dma_start_dt ( const struct sf32lb_dma_dt_spec * spec)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/dma/sf32lb.h>
```

根据设备树规格（DT Spec）启动 DMA 传输（Transfer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `spec` | SF32LB直接内存访问的设备树规格（DMA DT Spec）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负 `errno`；参见 `dma_start()`。

<a id="ga7d9763ae4042d855718a855955faef78"></a>

### `sf32lb_dma_stop_dt()`

```c
int sf32lb_dma_stop_dt ( const struct sf32lb_dma_dt_spec * spec)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/dma/sf32lb.h>
```

根据设备树规格（DT Spec）停止 DMA 传输（Transfer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `spec` | SF32LB直接内存访问的设备树规格（DMA DT Spec）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负 `errno`；参见 `dma_stop()`。


## 5.5\_原页交叉引用（Cross References）

- [sf32lb_dma_dt_spec](../device_power_control_model_reference/P086_sf32lb_dma_dt_spec_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [dma_config](../dma_reference/P004_DMA通道配置.md)
- [uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)
- [dma_status](../dma_reference/P005_DMA运行状态.md)
- [zephyr/drivers/dma/sf32lb.h](../api_file_transfer_device_reference/P004_zephyr__drivers__dma__sf32lb.h_文件参考.md)
- [DT_DRV_INST](../dt_instance_reference/P001_设备树驱动实例宏.md#ga219f413efba2f4c0151468b9a25a8dc1)
- [DEVICE_DT_GET](../device_reference/P001_设备模型公共接口.md#ga9a65996ce21f43acb7db061e23b48ec7)
- [DT_DMAS_CTLR](../dma_reference/P008_DMA设备树宏.md#ga09a22a0e5133dc7514680c16373f6ad3)
- [DT_DMAS_CELL_BY_IDX](../dma_reference/P008_DMA设备树宏.md#ga8aff7a91d19482964b8b56cb558c1b59)
- [DT_DMAS_CTLR_BY_NAME](../dma_reference/P008_DMA设备树宏.md#ga8c148fc826dee34f5e4601f4a7aa9f55)
- [DT_DMAS_CELL_BY_NAME](../dma_reference/P008_DMA设备树宏.md#ga1b80ae7fee6bcc9aa2ad03435e70dd14)
- [COND_CODE_1](../util_reference/P001_通用工具公共接口.md#ga358bc3e7669c860a98839a51cd526b20)
- [DT_DMAS_HAS_NAME](../dma_reference/P008_DMA设备树宏.md#ga865adb5b82c63e7f63451b96cd5a6404)
- [dma_get_status()](../dma_reference/P001_DMA公共接口.md#ga2cae500f1f9ed42ad338a40ec8655544)
- [dma_reload()](../dma_reference/P001_DMA公共接口.md#ga55bd5d550349c11c63ef47c2ed861f36)
- [dma_start()](../dma_reference/P001_DMA公共接口.md#gaf1184de07811702ffe89737b79e4a338)
- [dma_stop()](../dma_reference/P001_DMA公共接口.md#gafd602ee8386e10bb9ac7d386b3dc6a83)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__devicetree-inst_html_ga219f413efba2f4c0151468b9a25a8dc1"></a>
<a id="agroup__dma__sf32lb_html_gafe8cf86b36b9741dd069b296bf2dfbdf"></a>
<a id="agroup__dma__sf32lb_html_gaf9f8a7a13b1c806aa182e917c99cacaf"></a>
<a id="agroup__dma__sf32lb_html_gacb66db47cfc3b7bf06ca1323de291611"></a>
<a id="agroup__device__model_html_ga9a65996ce21f43acb7db061e23b48ec7"></a>
<a id="agroup__devicetree-dmas_html_ga09a22a0e5133dc7514680c16373f6ad3"></a>
<a id="agroup__devicetree-dmas_html_ga8aff7a91d19482964b8b56cb558c1b59"></a>
<a id="agroup__devicetree-dmas_html_ga1b80ae7fee6bcc9aa2ad03435e70dd14"></a>
<a id="agroup__devicetree-dmas_html_ga8c148fc826dee34f5e4601f4a7aa9f55"></a>
<a id="agroup__devicetree-dmas_html_ga865adb5b82c63e7f63451b96cd5a6404"></a>
<a id="agroup__sys-util_html_ga358bc3e7669c860a98839a51cd526b20"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P004_Core Devices SF32LB API主题.md) · [返回大纲](大纲.md) · [下一章](P006_eSPI 驱动后端 API（Driver Backend API）.md)
