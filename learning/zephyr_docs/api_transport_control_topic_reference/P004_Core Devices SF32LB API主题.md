---
id: learning.zephyr-docs.api-transport-control-topic-reference.page-4
title: Core Devices SF32LB API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__sf32lb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_Core Devices SF32LB API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__sf32lb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-files"></a>
<a id="files"></a>

## 4.1\_文件（Files）

<a id="r_sf32lb_2Eh"></a>

```c
file sf32lb.h
```

相关声明：[sf32lb.h](../api_file_transfer_device_reference/P002_zephyr__drivers__clock_control__sf32lb.h_文件参考.md)。

Core Devices SF32LB设备的时钟控制辅助接口（Clock Control Helpers）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 4.2\_数据结构（Data Structures）

<a id="r_sf32lb_5Fclock_5Fdt_5Fspec"></a>

```c
struct sf32lb_clock_dt_spec
```

相关声明：[sf32lb_clock_dt_spec](../device_power_control_model_reference/P085_sf32lb_clock_dt_spec_结构体.md)。

SF32LB时钟的设备树规格（Clock DT Spec）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 4.3\_宏定义（Macros）

<a id="r_ga918cb283440e5ddf0ced958f55477b34"></a>

```c
#define SF32LB_CLOCK_DT_SPEC_GET(node_id)
```

相关声明：[SF32LB_CLOCK_DT_SPEC_GET](#ga918cb283440e5ddf0ced958f55477b34)。

根据设备树节点（DT Node）初始化 `sf32lb_clock_dt_spec` 结构体。

<a id="r_ga0f499e84570bfc26292d37a955b66d65"></a>

```c
#define SF32LB_CLOCK_DT_SPEC_GET_OR(node_id, default_spec)
```

相关声明：[SF32LB_CLOCK_DT_SPEC_GET_OR](#ga0f499e84570bfc26292d37a955b66d65)。

与 `SF32LB_CLOCK_DT_SPEC_GET` 相同，但提供默认值（Default Value）。

<a id="r_gad3b3a613c2fa2606dfaf725d437d3b04"></a>

```c
#define SF32LB_CLOCK_DT_INST_SPEC_GET(index)
```

相关声明：[SF32LB_CLOCK_DT_INST_SPEC_GET](#gad3b3a613c2fa2606dfaf725d437d3b04)。

根据设备树实例（DT Instance）初始化 `sf32lb_clock_dt_spec` 结构体。

<a id="r_ga7dfb5fb6a26ecf5785a83ce97cbf72dd"></a>

```c
#define SF32LB_CLOCK_DT_INST_PARENT_SPEC_GET(index)
```

相关声明：[SF32LB_CLOCK_DT_INST_PARENT_SPEC_GET](#ga7dfb5fb6a26ecf5785a83ce97cbf72dd)。

根据父设备树实例（Parent DT Instance）初始化 `sf32lb_clock_dt_spec` 结构体。

<a id="r_gaa1ff407097f3bec82c389c128317503b"></a>

```c
#define SF32LB_CLOCK_DT_INST_SPEC_GET_OR(index, default_spec)
```

相关声明：[SF32LB_CLOCK_DT_INST_SPEC_GET_OR](#gaa1ff407097f3bec82c389c128317503b)。

与 `SF32LB_CLOCK_DT_INST_SPEC_GET` 相同，但提供默认值（Default Value）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 4.4\_函数（Functions）

<a id="r_gafb7a2391a9bb9b4a3e0f5bb528195358"></a>

```c
static bool sf32lb_clock_is_ready_dt (const struct sf32lb_clock_dt_spec *spec)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[sf32lb_clock_is_ready_dt](#gafb7a2391a9bb9b4a3e0f5bb528195358)、[sf32lb_clock_dt_spec](../device_power_control_model_reference/P085_sf32lb_clock_dt_spec_结构体.md)。

检查时钟设备（Clock Device）是否就绪。

<a id="r_ga4eed096f4161bce08fa721a762834edf"></a>

```c
static int sf32lb_clock_control_on_dt (const struct sf32lb_clock_dt_spec *spec)
```

相关声明：[sf32lb_clock_control_on_dt](#ga4eed096f4161bce08fa721a762834edf)、[sf32lb_clock_dt_spec](../device_power_control_model_reference/P085_sf32lb_clock_dt_spec_结构体.md)。

使用 `sf32lb_clock_dt_spec` 结构体开启时钟（Clock）。

<a id="r_ga25d996cf39360f4d51a79856d9498247"></a>

```c
static int sf32lb_clock_control_off_dt (const struct sf32lb_clock_dt_spec *spec)
```

相关声明：[sf32lb_clock_control_off_dt](#ga25d996cf39360f4d51a79856d9498247)、[sf32lb_clock_dt_spec](../device_power_control_model_reference/P085_sf32lb_clock_dt_spec_结构体.md)。

使用 `sf32lb_clock_dt_spec` 结构体关闭时钟（Clock）。

<a id="r_ga6287285db98a2df028a761742896bbd3"></a>

```c
static enum clock_control_status sf32lb_clock_control_get_status_dt (const struct sf32lb_clock_dt_spec *spec)
```

相关声明：[clock_control_status](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__interface.html#gad12829335f0c954ab6d586549db45e09)、[sf32lb_clock_control_get_status_dt](#ga6287285db98a2df028a761742896bbd3)、[sf32lb_clock_dt_spec](../device_power_control_model_reference/P085_sf32lb_clock_dt_spec_结构体.md)。

使用 `sf32lb_clock_dt_spec` 结构体获取时钟状态（Clock Status）。

<a id="r_gaa15f0fb2a5304a9782b9dfb5ff1ddb93"></a>

```c
static uint32_t sf32lb_clock_control_get_rate_dt (const struct sf32lb_clock_dt_spec *spec, uint32_t *rate)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[sf32lb_clock_control_get_rate_dt](#gaa15f0fb2a5304a9782b9dfb5ff1ddb93)、[sf32lb_clock_dt_spec](../device_power_control_model_reference/P085_sf32lb_clock_dt_spec_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

使用 `sf32lb_clock_dt_spec` 结构体获取时钟速率（Clock Rate）。

## 4.5\_详细说明（Detailed Documentation）

<a id="ga7dfb5fb6a26ecf5785a83ce97cbf72dd"></a>

### `SF32LB_CLOCK_DT_INST_PARENT_SPEC_GET`

```c
#define SF32LB_CLOCK_DT_INST_PARENT_SPEC_GET ( index)
```

```c
#include <zephyr/drivers/clock_control/sf32lb.h>
```

展开值（Value）：

```c
{                                                                                          \
        .dev = DEVICE_DT_GET(DT_CLOCKS_CTLR(DT_INST_PARENT(index))),                       \
        .id = DT_CLOCKS_CELL(DT_INST_PARENT(index), id),                                   \
}
```

根据父设备树实例（Parent DT Instance）初始化 `sf32lb_clock_dt_spec` 结构体。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `index` | 设备树实例索引（DT Instance Index）。 |

<a id="gad3b3a613c2fa2606dfaf725d437d3b04"></a>

### `SF32LB_CLOCK_DT_INST_SPEC_GET`

```c
#define SF32LB_CLOCK_DT_INST_SPEC_GET ( index)
```

```c
#include <zephyr/drivers/clock_control/sf32lb.h>
```

展开值（Value）：

```c
SF32LB_CLOCK_DT_SPEC_GET(DT_DRV_INST(index))
```

根据设备树实例（DT Instance）初始化 `sf32lb_clock_dt_spec` 结构体。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `index` | 设备树实例索引（DT Instance Index）。 |

<a id="gaa1ff407097f3bec82c389c128317503b"></a>

### `SF32LB_CLOCK_DT_INST_SPEC_GET_OR`

```c
#define SF32LB_CLOCK_DT_INST_SPEC_GET_OR ( index, default_spec )
```

```c
#include <zephyr/drivers/clock_control/sf32lb.h>
```

展开值（Value）：

```c
SF32LB_CLOCK_DT_SPEC_GET_OR(DT_DRV_INST(index), default_spec)
```

与 `SF32LB_CLOCK_DT_INST_SPEC_GET` 相同，但提供默认值（Default Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `index` | 设备树实例索引（DT Instance Index）。 |
| `default_spec` | 节点没有 `clocks` 属性（Property）时使用的默认值。 |

<a id="ga918cb283440e5ddf0ced958f55477b34"></a>

### `SF32LB_CLOCK_DT_SPEC_GET`

```c
#define SF32LB_CLOCK_DT_SPEC_GET ( node_id)
```

```c
#include <zephyr/drivers/clock_control/sf32lb.h>
```

展开值（Value）：

```c
{                                                                                          \
        .dev = DEVICE_DT_GET(DT_CLOCKS_CTLR(node_id)),                                     \
        .id = DT_CLOCKS_CELL(node_id, id),                                                 \
}
```

根据设备树节点（DT Node）初始化 `sf32lb_clock_dt_spec` 结构体。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 设备树节点标识符（DT Node Identifier）。 |

<a id="ga0f499e84570bfc26292d37a955b66d65"></a>

### `SF32LB_CLOCK_DT_SPEC_GET_OR`

```c
#define SF32LB_CLOCK_DT_SPEC_GET_OR ( node_id, default_spec )
```

```c
#include <zephyr/drivers/clock_control/sf32lb.h>
```

展开值（Value）：

```c
COND_CODE_1(DT_CLOCKS_HAS_IDX(node_id, 0),                                                 \
            (SF32LB_CLOCK_DT_SPEC_GET(node_id)), (default_spec))
```

与 `SF32LB_CLOCK_DT_SPEC_GET` 相同，但提供默认值（Default Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 设备树节点标识符（DT Node Identifier）。 |
| `default_spec` | 节点没有 `clocks` 属性（Property）时使用的默认值。 |

<a id="gaa15f0fb2a5304a9782b9dfb5ff1ddb93"></a>

### `sf32lb_clock_control_get_rate_dt()`

```c
uint32_t sf32lb_clock_control_get_rate_dt ( const struct sf32lb_clock_dt_spec * spec, uint32_t * rate )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/clock_control/sf32lb.h>
```

使用 `sf32lb_clock_dt_spec` 结构体获取时钟速率（Clock Rate）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` spec` | SF32LB 时钟设备树规格（Clock DT Spec）。 |
| `[out] rate` | 存储的时钟速率（Clock Rate），单位为 Hz。 |

**返回（Returns）**：**返回值（Returns）：**参见 `clock_control_get_rate()`。

<a id="ga6287285db98a2df028a761742896bbd3"></a>

### `sf32lb_clock_control_get_status_dt()`

```c
enum clock_control_status sf32lb_clock_control_get_status_dt ( const struct sf32lb_clock_dt_spec * spec)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/clock_control/sf32lb.h>
```

使用 `sf32lb_clock_dt_spec` 结构体获取时钟状态（Clock Status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `spec` | SF32LB 时钟设备树规格（Clock DT Spec）。 |

**返回（Returns）**：**返回值（Returns）：**参见 `clock_control_get_status()`。

<a id="ga25d996cf39360f4d51a79856d9498247"></a>

### `sf32lb_clock_control_off_dt()`

```c
int sf32lb_clock_control_off_dt ( const struct sf32lb_clock_dt_spec * spec)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/clock_control/sf32lb.h>
```

使用 `sf32lb_clock_dt_spec` 结构体关闭时钟（Clock）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `spec` | SF32LB 时钟设备树规格（Clock DT Spec）。 |

**返回（Returns）**：**返回值（Returns）：**参见 `clock_control_off()`。

<a id="ga4eed096f4161bce08fa721a762834edf"></a>

### `sf32lb_clock_control_on_dt()`

```c
int sf32lb_clock_control_on_dt ( const struct sf32lb_clock_dt_spec * spec)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/clock_control/sf32lb.h>
```

使用 `sf32lb_clock_dt_spec` 结构体开启时钟（Clock）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `spec` | SF32LB 时钟设备树规格（Clock DT Spec）。 |

**返回（Returns）**：**返回值（Returns）：**参见 `clock_control_on()`。

<a id="gafb7a2391a9bb9b4a3e0f5bb528195358"></a>

### `sf32lb_clock_is_ready_dt()`

```c
bool sf32lb_clock_is_ready_dt ( const struct sf32lb_clock_dt_spec * spec)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/clock_control/sf32lb.h>
```

检查时钟设备（Clock Device）是否就绪。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `spec` | SF32LB 时钟设备树规格（Clock DT Spec）。 |

**返回（Returns）**：**返回值（Returns）：**时钟设备就绪（Ready）返回 `true`，未就绪返回 `false`。


## 4.6\_原页交叉引用（Cross References）

- [sf32lb.h](../api_file_transfer_device_reference/P002_zephyr__drivers__clock_control__sf32lb.h_文件参考.md)
- [sf32lb_clock_dt_spec](../device_power_control_model_reference/P085_sf32lb_clock_dt_spec_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [clock_control_status](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__interface.html#gad12829335f0c954ab6d586549db45e09)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [DEVICE_DT_GET](../device_reference/P001_设备模型公共接口.md#ga9a65996ce21f43acb7db061e23b48ec7)
- [DT_CLOCKS_CTLR](https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-clocks.html#ga69795ece1f4a46e2c26a8e2dbb452f23)
- [DT_INST_PARENT](../dt_instance_reference/P001_设备树驱动实例宏.md#ga176760ce1a019020b5465eebd4f44ff5)
- [DT_CLOCKS_CELL](https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-clocks.html#ga211bc385cbbb1d8b8fa52e2e0a52d23d)
- [DT_DRV_INST](../dt_instance_reference/P001_设备树驱动实例宏.md#ga219f413efba2f4c0151468b9a25a8dc1)
- [COND_CODE_1](../util_reference/P001_通用工具公共接口.md#ga358bc3e7669c860a98839a51cd526b20)
- [DT_CLOCKS_HAS_IDX](https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-clocks.html#gabfdf51e2b14c05e84366cff1bb056da0)
- [clock_control_get_rate()](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__interface.html#ga00f6af6d2668c2dfff0640fe176e89ff)
- [clock_control_get_status()](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__interface.html#ga35be64d09222f44aa00cd1371a39613e)
- [clock_control_off()](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__interface.html#gadbebc1c12937be561b761ef4a3b7d8a5)
- [clock_control_on()](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__interface.html#gaec69b0989cefad79ffd5c92f060150b9)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__device__model_html_ga9a65996ce21f43acb7db061e23b48ec7"></a>
<a id="agroup__devicetree-clocks_html_ga211bc385cbbb1d8b8fa52e2e0a52d23d"></a>
<a id="agroup__devicetree-clocks_html_ga69795ece1f4a46e2c26a8e2dbb452f23"></a>
<a id="agroup__devicetree-inst_html_ga176760ce1a019020b5465eebd4f44ff5"></a>
<a id="agroup__clock__control__sf32lb_html_ga918cb283440e5ddf0ced958f55477b34"></a>
<a id="agroup__devicetree-inst_html_ga219f413efba2f4c0151468b9a25a8dc1"></a>
<a id="agroup__clock__control__sf32lb_html_ga0f499e84570bfc26292d37a955b66d65"></a>
<a id="agroup__devicetree-clocks_html_gabfdf51e2b14c05e84366cff1bb056da0"></a>
<a id="agroup__sys-util_html_ga358bc3e7669c860a98839a51cd526b20"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P003_蓝牙 LC3 编解码器（Bluetooth LC3 codec）.md) · [返回大纲](大纲.md) · [下一章](P005_DMA的SF32LB专用功能（SF32LB Specifics）。.md)
