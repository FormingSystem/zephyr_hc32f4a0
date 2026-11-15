---
id: learning.zephyr-docs.api-bridge-paging-topic-reference.page-14
title: 唤醒控制器（WUC）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_唤醒控制器（WUC）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

唤醒控制器（Wakeup Controller，WUC）驱动 API。

<a id="details"></a>

唤醒控制器（Wakeup Controller，WUC）驱动 API。自 4.4 起提供，版本 0.1.0。

<a id="header-groups"></a>
<a id="groups"></a>

## 14.1\_主题（Topics）

<a id="r_devicetree-wakeup-controller"></a>

相关声明：[设备树唤醒控制器接口（Devicetree WUC Controller API）](../dt_irq_reference/P005_设备树唤醒控制器宏.md)。

<a id="r_wuc_5Finterface_5Fbackend"></a>

相关声明：[WUC 驱动后端 API](../api_connection_topic_reference/P023_WUC 驱动后端 API.md)。

<a id="header-files"></a>
<a id="files"></a>

## 14.2\_文件（Files）

<a id="r_wuc_2Eh"></a>

```c
file wuc.h
```

相关声明：[wuc.h](../api_file_paging_wakeup_reference/P003_zephyr__drivers__wuc.h_文件参考.md)。

唤醒控制器（Wakeup Controller，WUC）驱动API的主头文件。

<a id="r_wuc_5Fnxp_5Fllwu_2Eh"></a>

```c
file wuc_nxp_llwu.h
```

相关声明：[wuc_nxp_llwu.h](https://docs.zephyrproject.org/latest/doxygen/html/wuc__nxp__llwu_8h.html)。

NXP低漏电唤醒单元（LLWU）的唤醒源编码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 14.3\_数据结构（Data Structures）

<a id="r_wuc_5Fdt_5Fspec"></a>

```c
struct wuc_dt_spec
```

相关声明：[wuc_dt_spec](../device_power_control_model_reference/P103_wuc_dt_spec_结构体.md)。

唤醒控制器（Wakeup Controller）的设备配置。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 14.4\_宏定义（Macros）

<a id="r_gab16abb3ef7b60f6aeb2ada2f426a396b"></a>

```c
#define WUC_DT_SPEC_GET_BY_IDX(node_id, idx)
```

相关声明：[WUC_DT_SPEC_GET_BY_IDX](#gab16abb3ef7b60f6aeb2ada2f426a396b)。

`wuc_dt_spec` 的静态初始化器（Static Initializer）。

<a id="r_gaea86f159bca2896a315c4909e4755abb"></a>

```c
#define WUC_DT_SPEC_GET_BY_IDX_OR(node_id, idx, default_value)
```

相关声明：[WUC_DT_SPEC_GET_BY_IDX_OR](#gaea86f159bca2896a315c4909e4755abb)。

类似 `WUC_DT_SPEC_GET_BY_IDX()`，但可回退到默认值（Default Value）。

<a id="r_ga83d434b9c2b26dcd448d0b53c63ff295"></a>

```c
#define WUC_DT_SPEC_GET(node_id)
```

相关声明：[WUC_DT_SPEC_GET](#ga83d434b9c2b26dcd448d0b53c63ff295)。

等价于 `WUC_DT_SPEC_GET_BY_IDX(node_id, 0)`。

<a id="r_ga78290ca0574db5ac06eba7d0218d4de9"></a>

```c
#define WUC_DT_SPEC_GET_OR(node_id, default_value)
```

相关声明：[WUC_DT_SPEC_GET_OR](#ga78290ca0574db5ac06eba7d0218d4de9)。

等价于 `WUC_DT_SPEC_GET_BY_IDX_OR(node_id, 0, default_value)`。

<a id="r_ga7605bb886d41618ae57768cfc5f356a1"></a>

```c
#define WUC_DT_SPEC_INST_GET_BY_IDX(inst, idx)
```

相关声明：[WUC_DT_SPEC_INST_GET_BY_IDX](#ga7605bb886d41618ae57768cfc5f356a1)。

根据 `DT_DRV_COMPAT` 实例的唤醒控制器属性（Wakeup Controller Property）中指定索引处的条目，构造 `wuc_dt_spec` 静态初始化器。

<a id="r_ga73532298336d56886a2d23d67144c9cb"></a>

```c
#define WUC_DT_SPEC_INST_GET_BY_IDX_OR(inst, idx, default_value)
```

相关声明：[WUC_DT_SPEC_INST_GET_BY_IDX_OR](#ga73532298336d56886a2d23d67144c9cb)。

根据 `DT_DRV_COMPAT` 实例的 `wakeup-ctrls` 属性中指定索引处的条目，构造 `wuc_dt_spec` 静态初始化器，并提供回退值（Fallback）。

<a id="r_gaa461bbeb02ca0f795104705916a33d76"></a>

```c
#define WUC_DT_SPEC_INST_GET(inst)
```

相关声明：[WUC_DT_SPEC_INST_GET](#gaa461bbeb02ca0f795104705916a33d76)。

等价于 `WUC_DT_SPEC_INST_GET_BY_IDX(inst, 0)`。

<a id="r_gaa3897de51a6f6d2d94b2beeec6cacb6d"></a>

```c
#define WUC_DT_SPEC_INST_GET_OR(inst, default_value)
```

相关声明：[WUC_DT_SPEC_INST_GET_OR](#gaa3897de51a6f6d2d94b2beeec6cacb6d)。

等价于 `WUC_DT_SPEC_INST_GET_BY_IDX_OR(node_id, 0, default_value)`。参数名 `node_id` 按原文保留。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 14.5\_函数（Functions）

<a id="r_ga28999754c6980fcfdae275adb0e811be"></a>

```c
static int wuc_enable_wakeup_source (const struct device *dev, uint32_t id)
```

相关声明：[wuc_enable_wakeup_source](#ga28999754c6980fcfdae275adb0e811be)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

启用唤醒源（Wakeup Source）。

<a id="r_gac3747f4707d490e620963d1c46a19af8"></a>

```c
static int wuc_enable_wakeup_source_dt (const struct wuc_dt_spec *spec)
```

相关声明：[wuc_enable_wakeup_source_dt](#gac3747f4707d490e620963d1c46a19af8)、[wuc_dt_spec](../device_power_control_model_reference/P103_wuc_dt_spec_结构体.md)。

使用 `wuc_dt_spec` 启用唤醒源（Wakeup Source）。

<a id="r_gacac1135652beabd7858f3b01683a973b"></a>

```c
static int wuc_disable_wakeup_source (const struct device *dev, uint32_t id)
```

相关声明：[wuc_disable_wakeup_source](#gacac1135652beabd7858f3b01683a973b)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

禁用唤醒源（Wakeup Source）。

<a id="r_ga7c7d2cc85a6b88cf01ce214f4f8e2904"></a>

```c
static int wuc_disable_wakeup_source_dt (const struct wuc_dt_spec *spec)
```

相关声明：[wuc_disable_wakeup_source_dt](#ga7c7d2cc85a6b88cf01ce214f4f8e2904)、[wuc_dt_spec](../device_power_control_model_reference/P103_wuc_dt_spec_结构体.md)。

使用 `wuc_dt_spec` 禁用唤醒源（Wakeup Source）。

<a id="r_gac03165353edf5e3a5273b60d7e1a1c8e"></a>

```c
static int wuc_check_wakeup_source_triggered (const struct device *dev, uint32_t id)
```

相关声明：[wuc_check_wakeup_source_triggered](#gac03165353edf5e3a5273b60d7e1a1c8e)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

检查唤醒源（Wakeup Source）是否已触发。

<a id="r_gab4a363a52e46b5d28fc8fb946ea7a29a"></a>

```c
static int wuc_check_wakeup_source_triggered_dt (const struct wuc_dt_spec *spec)
```

相关声明：[wuc_check_wakeup_source_triggered_dt](#gab4a363a52e46b5d28fc8fb946ea7a29a)、[wuc_dt_spec](../device_power_control_model_reference/P103_wuc_dt_spec_结构体.md)。

使用 `wuc_dt_spec` 检查唤醒源（Wakeup Source）是否已触发。

<a id="r_ga4f280e6dc432be25c6a542abcf927b60"></a>

```c
static int wuc_clear_wakeup_source_triggered (const struct device *dev, uint32_t id)
```

相关声明：[wuc_clear_wakeup_source_triggered](#ga4f280e6dc432be25c6a542abcf927b60)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

清除唤醒源的已触发状态（Triggered Status）。

<a id="r_gafce93565e572eaddc98006f33f127ef5"></a>

```c
static int wuc_clear_wakeup_source_triggered_dt (const struct wuc_dt_spec *spec)
```

相关声明：[wuc_clear_wakeup_source_triggered_dt](#gafce93565e572eaddc98006f33f127ef5)、[wuc_dt_spec](../device_power_control_model_reference/P103_wuc_dt_spec_结构体.md)。

使用 `wuc_dt_spec` 清除唤醒源的已触发状态（Triggered Status）。

## 14.6\_详细说明（Detailed Documentation）

<a id="ga83d434b9c2b26dcd448d0b53c63ff295"></a>

### `WUC_DT_SPEC_GET`

```c
#define WUC_DT_SPEC_GET ( node_id)
```

```c
#include <zephyr/drivers/wuc.h>
```

展开值（Value）：

```c
WUC_DT_SPEC_GET_BY_IDX(node_id, 0)
```

等价于 `WUC_DT_SPEC_GET_BY_IDX(node_id, 0)`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 设备树节点标识符（Devicetree Node Identifier）。 |

**返回（Returns）**：返回值：对应此属性的 `struct wuc_dt_spec` 静态初始化器（Static Initializer）。

**参阅（See Also）**：另请参见：`WUC_DT_SPEC_GET_BY_IDX()`。

<a id="gab16abb3ef7b60f6aeb2ada2f426a396b"></a>

### `WUC_DT_SPEC_GET_BY_IDX`

```c
#define WUC_DT_SPEC_GET_BY_IDX ( node_id, idx )
```

```c
#include <zephyr/drivers/wuc.h>
```

展开值（Value）：

```c
{.dev = DEVICE_DT_GET(DT_WUC_BY_IDX(node_id, idx)), .id = DT_WUC_ID_BY_IDX(node_id, idx)}
```

`wuc_dt_spec` 的静态初始化器（Static Initializer）。

根据设备树节点标识符（Devicetree Node Identifier）、指定唤醒控制器（Wakeup Controller）的属性及索引，返回 `wuc_dt_spec` 结构体的静态初始化器（Static Initializer）。

设备树片段示例：

原始示例（Example）：

```c
 n: node {
    wakeup-ctrls = <&wuc 10>;
 }
```

使用示例：

原始示例（Example）：

```c
 const struct wuc_dt_spec spec = WUC_DT_SPEC_GET_BY_IDX(DT_NODELABEL(n), 0);
 Initializes 'spec' to:
  {
          .dev = DEVICE_DT_GET(DT_NODELABEL(wuc)),
          .id = 10
  }
```

仍须检查 `dev` 字段指向的设备是否就绪，例如使用 `device_is_ready()`。仅当节点存在、具有所给属性，且该属性如上所示指定了唤醒控制器的唤醒源 ID（Wakeup Source ID）时，才可使用此宏；否则就是错误用法。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 设备树节点标识符（Devicetree Node Identifier）。 |
| `idx` | `wakeup-ctrls` 中的逻辑索引（Logical Index）。 |

**返回（Returns）**：返回值：对应此属性的 `struct wuc_dt_spec` 静态初始化器（Static Initializer）。

<a id="gaea86f159bca2896a315c4909e4755abb"></a>

### `WUC_DT_SPEC_GET_BY_IDX_OR`

```c
#define WUC_DT_SPEC_GET_BY_IDX_OR ( node_id, idx, default_value )
```

```c
#include <zephyr/drivers/wuc.h>
```

展开值（Value）：

```c
COND_CODE_1(DT_NODE_HAS_PROP(node_id, wakeup_ctrls),                    \
            (WUC_DT_SPEC_GET_BY_IDX(node_id, idx)),             \
            (default_value))
```

类似 `WUC_DT_SPEC_GET_BY_IDX()`，但可回退到默认值（Default Value）。

若设备树节点标识符（Devicetree Node Identifier）`node_id` 指向的节点具有 `wakeup-ctrls` 属性，则展开为 `WUC_DT_SPEC_GET_BY_IDX(node_id, idx)`。在此情况下，不会展开 `default_value` 参数。

否则展开为default_value。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 设备树节点标识符（Devicetree Node Identifier）。 |
| `idx` | `wakeup-ctrls` 属性中的逻辑索引（Logical Index）。 |
| `default_value` | 要展开为的回退值（Fallback Value）。 |

**返回（Returns）**：返回值：对应此属性的 `struct wuc_dt_spec` 静态初始化器（Static Initializer）；若节点或属性不存在，则返回 `default_value`。

<a id="ga78290ca0574db5ac06eba7d0218d4de9"></a>

### `WUC_DT_SPEC_GET_OR`

```c
#define WUC_DT_SPEC_GET_OR ( node_id, default_value )
```

```c
#include <zephyr/drivers/wuc.h>
```

展开值（Value）：

```c
WUC_DT_SPEC_GET_BY_IDX_OR(node_id, 0, default_value)
```

等价于 `WUC_DT_SPEC_GET_BY_IDX_OR(node_id, 0, default_value)`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 设备树节点标识符（Devicetree Node Identifier）。 |
| `default_value` | 要展开为的回退值（Fallback Value）。 |

**返回（Returns）**：返回值：对应此属性的 `struct wuc_dt_spec` 静态初始化器（Static Initializer）；若节点或属性不存在，则返回 `default_value`。

<a id="gaa461bbeb02ca0f795104705916a33d76"></a>

### `WUC_DT_SPEC_INST_GET`

```c
#define WUC_DT_SPEC_INST_GET ( inst)
```

```c
#include <zephyr/drivers/wuc.h>
```

展开值（Value）：

```c
WUC_DT_SPEC_INST_GET_BY_IDX(inst, 0)
```

等价于 `WUC_DT_SPEC_INST_GET_BY_IDX(inst, 0)`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | DT_DRV_COMPAT实例编号（Instance Number）。 |

**返回（Returns）**：返回值：对应此属性的 `struct wuc_dt_spec` 静态初始化器（Static Initializer）。

**参阅（See Also）**：另请参见：`WUC_DT_SPEC_INST_GET_BY_IDX()`。

<a id="ga7605bb886d41618ae57768cfc5f356a1"></a>

### `WUC_DT_SPEC_INST_GET_BY_IDX`

```c
#define WUC_DT_SPEC_INST_GET_BY_IDX ( inst, idx )
```

```c
#include <zephyr/drivers/wuc.h>
```

展开值（Value）：

```c
WUC_DT_SPEC_GET_BY_IDX(DT_DRV_INST(inst), idx)
```

根据 `DT_DRV_COMPAT` 实例的唤醒控制器属性（Wakeup Controller Property）中指定索引处的条目，构造 `wuc_dt_spec` 静态初始化器。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | DT_DRV_COMPAT实例编号（Instance Number）。 |
| `idx` | `wakeup-ctrls` 中的逻辑索引（Logical Index）。 |

**返回（Returns）**：返回值：对应此属性的 `struct wuc_dt_spec` 静态初始化器（Static Initializer）。

**参阅（See Also）**：另请参见：`WUC_DT_SPEC_GET_BY_IDX()`。

<a id="ga73532298336d56886a2d23d67144c9cb"></a>

### `WUC_DT_SPEC_INST_GET_BY_IDX_OR`

```c
#define WUC_DT_SPEC_INST_GET_BY_IDX_OR ( inst, idx, default_value )
```

```c
#include <zephyr/drivers/wuc.h>
```

展开值（Value）：

```c
COND_CODE_1(DT_PROP_HAS_IDX(DT_DRV_INST(inst), wakeup_ctrls, idx), \
        (WUC_DT_SPEC_GET_BY_IDX(DT_DRV_INST(inst), idx)),       \
        (default_value))
```

根据 `DT_DRV_COMPAT` 实例的 `wakeup-ctrls` 属性中指定索引处的条目，构造 `wuc_dt_spec` 静态初始化器，并提供回退值（Fallback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | DT_DRV_COMPAT实例编号（Instance Number）。 |
| `idx` | `wakeup-ctrls` 属性中的逻辑索引（Logical Index）。 |
| `default_value` | 要展开为的回退值（Fallback Value）。 |

**返回（Returns）**：返回值：对应此属性的 `struct wuc_dt_spec` 静态初始化器（Static Initializer）；若节点或属性不存在，则返回 `default_value`。

<a id="gaa3897de51a6f6d2d94b2beeec6cacb6d"></a>

### `WUC_DT_SPEC_INST_GET_OR`

```c
#define WUC_DT_SPEC_INST_GET_OR ( inst, default_value )
```

```c
#include <zephyr/drivers/wuc.h>
```

展开值（Value）：

```c
WUC_DT_SPEC_INST_GET_BY_IDX_OR(inst, 0, default_value)
```

等价于 `WUC_DT_SPEC_INST_GET_BY_IDX_OR(node_id, 0, default_value)`。参数名 `node_id` 按原文保留。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | DT_DRV_COMPAT实例编号（Instance Number）。 |
| `default_value` | 要展开为的回退值（Fallback Value）。 |

**返回（Returns）**：返回值：对应此属性的 `struct wuc_dt_spec` 静态初始化器（Static Initializer）；若节点或属性不存在，则返回 `default_value`。

<a id="gac03165353edf5e3a5273b60d7e1a1c8e"></a>

### `wuc_check_wakeup_source_triggered()`

```c
int wuc_check_wakeup_source_triggered ( const struct device * dev, uint32_t id )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/wuc.h>
```

检查唤醒源（Wakeup Source）是否已触发。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 WUC 设备结构体（Device Structure）的指针。 |
| `id` | 唤醒源标识符。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOSYS` | 未实现此接口（Interface）。 |

**返回（Returns）**：返回值：由此源触发唤醒时返回 1，未触发时返回 0；失败时返回负 errno 错误码。

<a id="gab4a363a52e46b5d28fc8fb946ea7a29a"></a>

### `wuc_check_wakeup_source_triggered_dt()`

```c
int wuc_check_wakeup_source_triggered_dt ( const struct wuc_dt_spec * spec)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/wuc.h>
```

使用 `wuc_dt_spec` 检查唤醒源（Wakeup Source）是否已触发。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `spec` | 指向 WUC 设备树规格结构体（Devicetree Spec Structure）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOSYS` | 未实现此接口（Interface）。 |

**返回（Returns）**：返回值：由此源触发唤醒时返回 1，未触发时返回 0；失败时返回负 errno 错误码。

<a id="ga4f280e6dc432be25c6a542abcf927b60"></a>

### `wuc_clear_wakeup_source_triggered()`

```c
int wuc_clear_wakeup_source_triggered ( const struct device * dev, uint32_t id )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/wuc.h>
```

清除唤醒源的已触发状态（Triggered Status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 WUC 设备结构体（Device Structure）的指针。 |
| `id` | 唤醒源标识符。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOSYS` | 未实现此接口（Interface）。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="gafce93565e572eaddc98006f33f127ef5"></a>

### `wuc_clear_wakeup_source_triggered_dt()`

```c
int wuc_clear_wakeup_source_triggered_dt ( const struct wuc_dt_spec * spec)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/wuc.h>
```

使用 `wuc_dt_spec` 清除唤醒源的已触发状态（Triggered Status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `spec` | 指向 WUC 设备树规格结构体（Devicetree Spec Structure）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOSYS` | 未实现此接口（Interface）。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="gacac1135652beabd7858f3b01683a973b"></a>

### `wuc_disable_wakeup_source()`

```c
int wuc_disable_wakeup_source ( const struct device * dev, uint32_t id )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/wuc.h>
```

禁用唤醒源（Wakeup Source）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 WUC 设备结构体（Device Structure）的指针。 |
| `id` | 唤醒源标识符。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga7c7d2cc85a6b88cf01ce214f4f8e2904"></a>

### `wuc_disable_wakeup_source_dt()`

```c
int wuc_disable_wakeup_source_dt ( const struct wuc_dt_spec * spec)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/wuc.h>
```

使用 `wuc_dt_spec` 禁用唤醒源（Wakeup Source）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `spec` | 指向 WUC 设备树规格结构体（Devicetree Spec Structure）的指针。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga28999754c6980fcfdae275adb0e811be"></a>

### `wuc_enable_wakeup_source()`

```c
int wuc_enable_wakeup_source ( const struct device * dev, uint32_t id )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/wuc.h>
```

启用唤醒源（Wakeup Source）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 WUC 设备结构体（Device Structure）的指针。 |
| `id` | 唤醒源标识符。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="gac3747f4707d490e620963d1c46a19af8"></a>

### `wuc_enable_wakeup_source_dt()`

```c
int wuc_enable_wakeup_source_dt ( const struct wuc_dt_spec * spec)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/wuc.h>
```

使用 `wuc_dt_spec` 启用唤醒源（Wakeup Source）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `spec` | 指向 WUC 设备树规格结构体（Devicetree Spec Structure）的指针。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。


## 14.7\_原页交叉引用（Cross References）

- [设备树唤醒控制器接口（Devicetree WUC Controller API）](../dt_irq_reference/P005_设备树唤醒控制器宏.md)
- [WUC 驱动后端 API](../api_connection_topic_reference/P023_WUC 驱动后端 API.md)
- [wuc.h](../api_file_paging_wakeup_reference/P003_zephyr__drivers__wuc.h_文件参考.md)
- [wuc_nxp_llwu.h](https://docs.zephyrproject.org/latest/doxygen/html/wuc__nxp__llwu_8h.html)
- [wuc_dt_spec](../device_power_control_model_reference/P103_wuc_dt_spec_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [DEVICE_DT_GET](../device_reference/P001_设备模型公共接口.md#ga9a65996ce21f43acb7db061e23b48ec7)
- [DT_WUC_BY_IDX](../dt_irq_reference/P005_设备树唤醒控制器宏.md#gaff37ae7c6bd1c35d5e2db27dee748002)
- [DT_WUC_ID_BY_IDX](../dt_irq_reference/P005_设备树唤醒控制器宏.md#ga3cc552613fd5100a06fa83dc19fa8e29)
- [device_is_ready()](../device_reference/P001_设备模型公共接口.md#gaa4944bd850e90cbd52b0489f9b12edfb)
- [COND_CODE_1](../util_reference/P001_通用工具公共接口.md#ga358bc3e7669c860a98839a51cd526b20)
- [DT_NODE_HAS_PROP](../dt_identity_reference/P002_设备树存在性与状态宏.md#gacce67bf20541cd2d07d8540058964692)
- [DT_DRV_INST](../dt_instance_reference/P001_设备树驱动实例宏.md#ga219f413efba2f4c0151468b9a25a8dc1)
- [DT_PROP_HAS_IDX](../dt_property_reference/P001_设备树属性读取宏.md#ga479dfc704087eea7e7c5af42ae98576c)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__wuc__interface_html_gab16abb3ef7b60f6aeb2ada2f426a396b"></a>
<a id="agroup__device__model_html_ga9a65996ce21f43acb7db061e23b48ec7"></a>
<a id="agroup__devicetree-wakeup-controller_html_ga3cc552613fd5100a06fa83dc19fa8e29"></a>
<a id="agroup__devicetree-wakeup-controller_html_gaff37ae7c6bd1c35d5e2db27dee748002"></a>
<a id="agroup__devicetree-generic-exist_html_gacce67bf20541cd2d07d8540058964692"></a>
<a id="agroup__sys-util_html_ga358bc3e7669c860a98839a51cd526b20"></a>
<a id="agroup__wuc__interface_html_gaea86f159bca2896a315c4909e4755abb"></a>
<a id="agroup__wuc__interface_html_ga7605bb886d41618ae57768cfc5f356a1"></a>
<a id="agroup__devicetree-inst_html_ga219f413efba2f4c0151468b9a25a8dc1"></a>
<a id="agroup__devicetree-generic-prop_html_ga479dfc704087eea7e7c5af42ae98576c"></a>
<a id="agroup__wuc__interface_html_ga73532298336d56886a2d23d67144c9cb"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P013_MSPI 配置 API（MSPI Configure API）.md) · [返回大纲](大纲.md)
