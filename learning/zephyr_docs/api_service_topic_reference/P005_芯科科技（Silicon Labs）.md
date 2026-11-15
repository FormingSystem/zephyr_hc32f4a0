---
id: learning.zephyr-docs.api-service-topic-reference.page-5
title: 芯科科技（Silicon Labs）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__silabs.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_芯科科技（Silicon Labs）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__silabs.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-files"></a>
<a id="files"></a>

## 5.1\_文件（Files）

<a id="r_clock_5Fcontrol_5Fsilabs_2Eh"></a>

```c
file clock_control_silabs.h
```

相关声明：[clock_control_silabs.h](../api_file_service_reference/P003_zephyr__drivers__clock_control__clock_control_silabs.h_文件参考.md)。

Silicon Labs设备的时钟控制定义（Clock Control Definitions）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 5.2\_数据结构（Data Structures）

<a id="r_silabs_5Fclock_5Fcontrol_5Fcmu_5Fconfig"></a>

```c
struct silabs_clock_control_cmu_config
```

相关声明：[silabs_clock_control_cmu_config](../device_power_control_model_reference/P087_silabs_clock_control_cmu_config_结构体.md)。

外设的时钟管理单元（Clock Management Unit，CMU）时钟配置。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 5.3\_宏定义（Macros）

<a id="r_ga2238842842469b06a3cb0d0cf187583c"></a>

```c
#define SILABS_DT_CLOCK_CFG(node_id)
```

相关声明：[SILABS_DT_CLOCK_CFG](#ga2238842842469b06a3cb0d0cf187583c)。

根据设备树节点（DT Node）初始化 `silabs_clock_control_cmu_config`。

<a id="r_ga109d85a9e8fe8ec3730927a91d885721"></a>

```c
#define SILABS_DT_INST_CLOCK_CFG(inst)
```

相关声明：[SILABS_DT_INST_CLOCK_CFG](#ga109d85a9e8fe8ec3730927a91d885721)。

对设备树实例（DT Instance）执行与 `SILABS_DT_CLOCK_CFG()` 等效的操作。

<a id="r_ga6aee6d89bb6d61cc82f43bf9d2c0f35b"></a>

```c
#define SILABS_DT_CLOCK_CFG_BY_NAME(node_id, name)
```

相关声明：[SILABS_DT_CLOCK_CFG_BY_NAME](#ga6aee6d89bb6d61cc82f43bf9d2c0f35b)。

根据设备树节点（DT Node），按名称（By Name）初始化 `silabs_clock_control_cmu_config`。

<a id="r_ga558497745851c6074caebc726c243333"></a>

```c
#define SILABS_DT_INST_CLOCK_CFG_BY_NAME(inst, name)
```

相关声明：[SILABS_DT_INST_CLOCK_CFG_BY_NAME](#ga558497745851c6074caebc726c243333)。

对设备树实例（DT Instance）执行与 `SILABS_DT_CLOCK_CFG_BY_NAME()` 等效的操作。

## 5.4\_详细说明（Detailed Documentation）

<a id="ga2238842842469b06a3cb0d0cf187583c"></a>

### `SILABS_DT_CLOCK_CFG`

```c
#define SILABS_DT_CLOCK_CFG ( node_id)
```

```c
#include <zephyr/drivers/clock_control/clock_control_silabs.h>
```

展开值（Value）：

```c
{                                                                                          \
        .bus_clock = DT_CLOCKS_CELL(node_id, enable),                                      \
        .branch = DT_CLOCKS_CELL(node_id, branch),                                         \
}
```

根据设备树节点（DT Node）初始化 `silabs_clock_control_cmu_config`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 具有 `clocks` 属性的设备树节点标识（Devicetree Node Identifier）。 |

<a id="ga6aee6d89bb6d61cc82f43bf9d2c0f35b"></a>

### `SILABS_DT_CLOCK_CFG_BY_NAME`

```c
#define SILABS_DT_CLOCK_CFG_BY_NAME ( node_id, name )
```

```c
#include <zephyr/drivers/clock_control/clock_control_silabs.h>
```

展开值（Value）：

```c
{                                                                                          \
        .bus_clock = DT_CLOCKS_CELL_BY_NAME(node_id, name, enable),                        \
        .branch = DT_CLOCKS_CELL_BY_NAME(node_id, name, branch),                           \
}
```

根据设备树节点（DT Node），按名称（By Name）初始化 `silabs_clock_control_cmu_config`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 具有 `clocks` 属性的设备树节点标识（Devicetree Node Identifier）。 |
| `name` | 由节点 `clock-names` 属性定义的 `clocks` 元素名称，使用小写字母和下划线（Lowercase-and-Underscores）形式。 |

<a id="ga109d85a9e8fe8ec3730927a91d885721"></a>

### `SILABS_DT_INST_CLOCK_CFG`

```c
#define SILABS_DT_INST_CLOCK_CFG ( inst)
```

```c
#include <zephyr/drivers/clock_control/clock_control_silabs.h>
```

展开值（Value）：

```c
{                                                                                          \
        .bus_clock = DT_INST_CLOCKS_CELL(inst, enable),                                    \
        .branch = DT_INST_CLOCKS_CELL(inst, branch),                                       \
}
```

对设备树实例（DT Instance）执行与 `SILABS_DT_CLOCK_CFG()` 等效的操作。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 设备树实例编号（DT Instance Number）。 |

<a id="ga558497745851c6074caebc726c243333"></a>

### `SILABS_DT_INST_CLOCK_CFG_BY_NAME`

```c
#define SILABS_DT_INST_CLOCK_CFG_BY_NAME ( inst, name )
```

```c
#include <zephyr/drivers/clock_control/clock_control_silabs.h>
```

展开值（Value）：

```c
{                                                                                          \
        .bus_clock = DT_INST_CLOCKS_CELL_BY_NAME(inst, name, enable),                      \
        .branch = DT_INST_CLOCKS_CELL_BY_NAME(inst, name, branch),                         \
}
```

对设备树实例（DT Instance）执行与 `SILABS_DT_CLOCK_CFG_BY_NAME()` 等效的操作。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 设备树实例编号（DT Instance Number）。 |
| `name` | 由节点 `clock-names` 属性定义的 `clocks` 元素名称，使用小写字母和下划线（Lowercase-and-Underscores）形式。 |


## 5.5\_原页交叉引用（Cross References）

- [clock_control_silabs.h](../api_file_service_reference/P003_zephyr__drivers__clock_control__clock_control_silabs.h_文件参考.md)
- [silabs_clock_control_cmu_config](../device_power_control_model_reference/P087_silabs_clock_control_cmu_config_结构体.md)
- [DT_CLOCKS_CELL](https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-clocks.html#ga211bc385cbbb1d8b8fa52e2e0a52d23d)
- [DT_CLOCKS_CELL_BY_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-clocks.html#gaca32bfb478ac92e6a760ad0761328d5a)
- [DT_INST_CLOCKS_CELL](https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-clocks.html#gad6a9584690066548b8d61489ad615a45)
- [DT_INST_CLOCKS_CELL_BY_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-clocks.html#ga976ab2adb237e5f1e0ba3496e9322d14)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__devicetree-clocks_html_ga211bc385cbbb1d8b8fa52e2e0a52d23d"></a>
<a id="agroup__devicetree-clocks_html_gaca32bfb478ac92e6a760ad0761328d5a"></a>
<a id="agroup__devicetree-clocks_html_gad6a9584690066548b8d61489ad615a45"></a>
<a id="agroup__devicetree-clocks_html_ga976ab2adb237e5f1e0ba3496e9322d14"></a>

---

[上一章](P004_微芯（Microchip）SAM 电源管理控制器（PMC）.md) · [返回大纲](大纲.md) · [下一章](P006_德州仪器（Texas Instruments）TI SCI.md)
