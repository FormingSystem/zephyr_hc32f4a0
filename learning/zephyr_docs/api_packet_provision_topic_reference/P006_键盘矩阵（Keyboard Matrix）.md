---
id: learning.zephyr-docs.api-packet-provision-topic-reference.page-6
title: 键盘矩阵（Keyboard Matrix）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_键盘矩阵（Keyboard Matrix）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-files"></a>
<a id="files"></a>

## 6.1\_文件（Files）

<a id="r_input_5Fkbd_5Fmatrix_2Eh"></a>

```c
file input_kbd_matrix.h
```

相关声明：[input_kbd_matrix.h](../api_file_serial_motion_reference/P005_zephyr__input__input_kbd_matrix.h_文件参考.md)。

键盘矩阵输入设备（Keyboard Matrix Input Devices）的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 6.2\_数据结构（Data Structures）

<a id="r_input_5Fkbd_5Fmatrix_5Fapi"></a>

```c
struct input_kbd_matrix_api
```

相关声明：[input_kbd_matrix_api](../system_service_model_reference/P054_input_kbd_matrix_api_结构体.md)。

键盘矩阵（Keyboard Matrix）的内部API。

<a id="r_input_5Fkbd_5Fmatrix_5Fcommon_5Fconfig"></a>

```c
struct input_kbd_matrix_common_config
```

相关声明：[input_kbd_matrix_common_config](../system_service_model_reference/P055_input_kbd_matrix_common_config_结构体.md)。

通用键盘矩阵（Keyboard Matrix）配置。

<a id="r_input_5Fkbd_5Fmatrix_5Fcommon_5Fdata"></a>

```c
struct input_kbd_matrix_common_data
```

相关声明：[input_kbd_matrix_common_data](../system_service_model_reference/P056_input_kbd_matrix_common_data_结构体.md)。

通用键盘矩阵（Keyboard Matrix）数据。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 6.3\_宏定义（Macros）

<a id="r_ga2f35f23d426f93f71057a31f612a88de"></a>

```c
#define INPUT_KBD_MATRIX_COLUMN_DRIVE_NONE -1
```

相关声明：[INPUT_KBD_MATRIX_COLUMN_DRIVE_NONE](#ga2f35f23d426f93f71057a31f612a88de)。

`drive_column` 的特殊参数，表示不驱动任何列（Column）。

<a id="r_ga6d27ba5612c09d80087e854b21fb9e65"></a>

```c
#define INPUT_KBD_MATRIX_COLUMN_DRIVE_ALL -2
```

相关声明：[INPUT_KBD_MATRIX_COLUMN_DRIVE_ALL](#ga6d27ba5612c09d80087e854b21fb9e65)。

`drive_column` 的特殊参数，表示驱动全部列（Columns）。

<a id="r_ga80a384d2041dcee27d7940a1e408d82a"></a>

```c
#define INPUT_KBD_MATRIX_SCAN_OCURRENCES 30U
```

相关声明：[INPUT_KBD_MATRIX_SCAN_OCURRENCES](#ga80a384d2041dcee27d7940a1e408d82a)。

跟踪的扫描周期数（Scan Cycles）。

<a id="r_ga1343b97a8b072f8ed362e8a4f242bdd1"></a>

```c
#define PRIkbdrow "02" PRIx8
```

相关声明：[PRIkbdrow](#ga1343b97a8b072f8ed362e8a4f242bdd1)、[PRIx8](../api_file_reference/P171_____w__zephyr__zephyr__lib__libc__minimal__include__inttypes.h_文件参考.md#adac1acc1d24060aeee7791a99d1a3a8c)。

<a id="r_gaec0209680e18da8584bdf41e5229aaae"></a>

```c
#define INPUT_KBD_ACTUAL_KEY_MASK_CONST
```

相关声明：[INPUT_KBD_ACTUAL_KEY_MASK_CONST](#gaec0209680e18da8584bdf41e5229aaae)。

<a id="r_gae395cd03c295673dc9563c252ba7e022"></a>

```c
#define INPUT_KBD_MATRIX_ROW_BITS NUM_BITS(kbd_row_t)
```

相关声明：[INPUT_KBD_MATRIX_ROW_BITS](#gae395cd03c295673dc9563c252ba7e022)、[NUM_BITS](../util_reference/P002_通用工具头文件参考.md#afa27c06d0ad6b949289431ad75f104ab)、[kbd_row_t](#gac7d5c811da0c9ab2660be3c3f2fcfe86)。

最大行数（Maximum Number of Rows）。

<a id="r_gac7cc0314fa201b1efbcac37cf5f90576"></a>

```c
#define INPUT_KBD_MATRIX_DATA_NAME(node_id, name)
```

相关声明：[INPUT_KBD_MATRIX_DATA_NAME](#gac7cc0314fa201b1efbcac37cf5f90576)。

<a id="r_gac1a4389b1afeab9c48a15c024bfb0cac"></a>

```c
#define INPUT_KBD_MATRIX_DT_DEFINE_ROW_COL(node_id, _row_size, _col_size)
```

相关声明：[INPUT_KBD_MATRIX_DT_DEFINE_ROW_COL](#gac1a4389b1afeab9c48a15c024bfb0cac)。

根据设备树（Devicetree）定义通用键盘矩阵支持数据（Keyboard Matrix Support Data），并指定行数和列数。

<a id="r_ga512bea2ca97569f465074ca8f231a0a3"></a>

```c
#define INPUT_KBD_MATRIX_DT_DEFINE(node_id)
```

相关声明：[INPUT_KBD_MATRIX_DT_DEFINE](#ga512bea2ca97569f465074ca8f231a0a3)。

根据设备树（Devicetree）定义通用键盘矩阵支持数据（Keyboard Matrix Support Data）。

<a id="r_ga1d3fe52f10c75dc4c32c8583c05fb2a2"></a>

```c
#define INPUT_KBD_MATRIX_DT_INST_DEFINE_ROW_COL(inst, row_size, col_size)
```

相关声明：[INPUT_KBD_MATRIX_DT_INST_DEFINE_ROW_COL](#ga1d3fe52f10c75dc4c32c8583c05fb2a2)。

根据设备树实例（Devicetree Instance）定义通用键盘矩阵支持数据，并指定行数和列数。

<a id="r_gab3ea5b7d597574b32ced16604648a6d2"></a>

```c
#define INPUT_KBD_MATRIX_DT_INST_DEFINE(inst)
```

相关声明：[INPUT_KBD_MATRIX_DT_INST_DEFINE](#gab3ea5b7d597574b32ced16604648a6d2)。

根据设备树实例（Devicetree Instance）定义通用键盘矩阵支持数据。

<a id="r_ga5ad9141616b4a63068bfbe8004bba67d"></a>

```c
#define INPUT_KBD_MATRIX_DT_COMMON_CONFIG_INIT_ROW_COL(node_id, _api, _row_size, _col_size)
```

相关声明：[INPUT_KBD_MATRIX_DT_COMMON_CONFIG_INIT_ROW_COL](#ga5ad9141616b4a63068bfbe8004bba67d)。

根据设备树（Devicetree）初始化通用键盘矩阵配置（Keyboard Matrix Config），并指定行数和列数。

<a id="r_ga3281b4e5909a1c07d8190092bc31cb12"></a>

```c
#define INPUT_KBD_MATRIX_DT_COMMON_CONFIG_INIT(node_id, api)
```

相关声明：[INPUT_KBD_MATRIX_DT_COMMON_CONFIG_INIT](#ga3281b4e5909a1c07d8190092bc31cb12)。

根据设备树（Devicetree）初始化通用键盘矩阵配置（Keyboard Matrix Config）。

<a id="r_gac6baf9b284f0796cdd5dbcef338f9588"></a>

```c
#define INPUT_KBD_MATRIX_DT_INST_COMMON_CONFIG_INIT_ROW_COL(inst, api, row_size, col_size)
```

相关声明：[INPUT_KBD_MATRIX_DT_INST_COMMON_CONFIG_INIT_ROW_COL](#gac6baf9b284f0796cdd5dbcef338f9588)。

根据设备树实例（Devicetree Instance）初始化通用键盘矩阵配置，并指定行数和列数。

<a id="r_gab19b4a8c66c5540b4e690459655f92fd"></a>

```c
#define INPUT_KBD_MATRIX_DT_INST_COMMON_CONFIG_INIT(inst, api)
```

相关声明：[INPUT_KBD_MATRIX_DT_INST_COMMON_CONFIG_INIT](#gab19b4a8c66c5540b4e690459655f92fd)。

根据设备树实例（Devicetree Instance）初始化通用键盘矩阵配置。

<a id="r_ga352d484344c93c30f5cad75551793377"></a>

```c
#define INPUT_KBD_STRUCT_CHECK(config, data)
```

相关声明：[INPUT_KBD_STRUCT_CHECK](#ga352d484344c93c30f5cad75551793377)。

验证通用数据结构的偏移量（Offset）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 6.4\_类型定义（Typedefs）

<a id="r_gac7d5c811da0c9ab2660be3c3f2fcfe86"></a>

```c
typedef uint8_t kbd_row_t
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[kbd_row_t](#gac7d5c811da0c9ab2660be3c3f2fcfe86)。

行条目数据类型（Row Entry Data Type）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 6.5\_函数（Functions）

<a id="r_gab35f4bf523760933294242ccc8226490"></a>

```c
int input_kbd_matrix_actual_key_mask_set (const struct device *dev, uint8_t row, uint8_t col, bool enabled)
```

相关声明：[input_kbd_matrix_actual_key_mask_set](#gab35f4bf523760933294242ccc8226490)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

在实际按键掩码（Actual Key Mask）中启用或禁用特定的行列组合。

<a id="r_gaf97b6ff410631f111d7c3a7aa7f64171"></a>

```c
void input_kbd_matrix_poll_start (const struct device *dev)
```

相关声明：[input_kbd_matrix_poll_start](#gaf97b6ff410631f111d7c3a7aa7f64171)、[device](../device_reference/P002_设备对象结构.md)。

开始扫描键盘矩阵（Keyboard Matrix）。

<a id="r_ga6d843c7213bf5c0af9003c165a5f3e03"></a>

```c
void input_kbd_matrix_drive_column_hook (const struct device *dev, int col)
```

相关声明：[input_kbd_matrix_drive_column_hook](#ga6d843c7213bf5c0af9003c165a5f3e03)、[device](../device_reference/P002_设备对象结构.md)。

驱动列的钩子（Drive Column Hook）。

<a id="r_ga938dc38da7e81e5a68b8b9dc585c4bab"></a>

```c
int input_kbd_matrix_common_init (const struct device *dev)
```

相关声明：[input_kbd_matrix_common_init](#ga938dc38da7e81e5a68b8b9dc585c4bab)、[device](../device_reference/P002_设备对象结构.md)。

在初始化时初始化键盘矩阵设备（Keyboard Matrix Device）的公共函数。

<a id="r_ga8e72535859abe307b4409dc4177b5721"></a>

```c
bool input_kbd_matrix_ghosting (const struct device *dev)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[input_kbd_matrix_ghosting](#ga8e72535859abe307b4409dc4177b5721)、[device](../device_reference/P002_设备对象结构.md)。

检查当前键盘矩阵状态是否存在鬼键（Ghost Keys）。

<a id="r_ga45a596e00af6ebf547f44a01cd07d539"></a>

```c
void input_kbd_matrix_update_state (const struct device *dev)
```

相关声明：[input_kbd_matrix_update_state](#ga45a596e00af6ebf547f44a01cd07d539)、[device](../device_reference/P002_设备对象结构.md)。

更新键盘矩阵状态并执行去抖（Debouncing）。

<a id="r_ga90ec50249d8e561d69f550fcaa6bd969"></a>

```c
bool input_kbd_matrix_active (const struct device *dev)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[input_kbd_matrix_active](#ga90ec50249d8e561d69f550fcaa6bd969)、[device](../device_reference/P002_设备对象结构.md)。

矩阵被视为活动状态（Active）时返回 `true`。

## 6.6\_详细说明（Detailed Documentation）

<a id="gaec0209680e18da8584bdf41e5229aaae"></a>

### `INPUT_KBD_ACTUAL_KEY_MASK_CONST`

```c
#define INPUT_KBD_ACTUAL_KEY_MASK_CONST
```

```c
#include <zephyr/input/input_kbd_matrix.h>
```

<a id="ga6d27ba5612c09d80087e854b21fb9e65"></a>

### `INPUT_KBD_MATRIX_COLUMN_DRIVE_ALL`

```c
#define INPUT_KBD_MATRIX_COLUMN_DRIVE_ALL -2
```

```c
#include <zephyr/input/input_kbd_matrix.h>
```

`drive_column` 的特殊参数，表示驱动全部列（Columns）。

<a id="ga2f35f23d426f93f71057a31f612a88de"></a>

### `INPUT_KBD_MATRIX_COLUMN_DRIVE_NONE`

```c
#define INPUT_KBD_MATRIX_COLUMN_DRIVE_NONE -1
```

```c
#include <zephyr/input/input_kbd_matrix.h>
```

`drive_column` 的特殊参数，表示不驱动任何列（Column）。

<a id="gac7cc0314fa201b1efbcac37cf5f90576"></a>

### `INPUT_KBD_MATRIX_DATA_NAME`

```c
#define INPUT_KBD_MATRIX_DATA_NAME ( node_id, name )
```

```c
#include <zephyr/input/input_kbd_matrix.h>
```

展开值（Value）：

```c
_CONCAT(__input_kbd_matrix_, \
        _CONCAT(name, DEVICE_DT_NAME_GET(node_id)))
```

<a id="ga3281b4e5909a1c07d8190092bc31cb12"></a>

### `INPUT_KBD_MATRIX_DT_COMMON_CONFIG_INIT`

```c
#define INPUT_KBD_MATRIX_DT_COMMON_CONFIG_INIT ( node_id, api )
```

```c
#include <zephyr/input/input_kbd_matrix.h>
```

展开值（Value）：

```c
INPUT_KBD_MATRIX_DT_COMMON_CONFIG_INIT_ROW_COL( \
        node_id, api, DT_PROP(node_id, row_size), DT_PROP(node_id, col_size))
```

根据设备树（Devicetree）初始化通用键盘矩阵配置（Keyboard Matrix Config）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 设备树节点标识符。 |
| `api` | 指向 `input_kbd_matrix_api` 结构体的指针。 |

<a id="ga5ad9141616b4a63068bfbe8004bba67d"></a>

### `INPUT_KBD_MATRIX_DT_COMMON_CONFIG_INIT_ROW_COL`

```c
#define INPUT_KBD_MATRIX_DT_COMMON_CONFIG_INIT_ROW_COL ( node_id, _api, _row_size, _col_size )
```

```c
#include <zephyr/input/input_kbd_matrix.h>
```

展开值（Value）：

```c
{ \
        .api = _api, \
        .row_size = _row_size, \
        .col_size = _col_size, \
        .poll_period_us = DT_PROP(node_id, poll_period_us), \
        .stable_poll_period_us = DT_PROP_OR(node_id, stable_poll_period_us, \
                                            DT_PROP(node_id, poll_period_us)), \
        .poll_timeout_ms = DT_PROP(node_id, poll_timeout_ms), \
        .debounce_down_us = DT_PROP(node_id, debounce_down_ms) * USEC_PER_MSEC, \
        .debounce_up_us = DT_PROP(node_id, debounce_up_ms) * USEC_PER_MSEC, \
        .settle_time_us = DT_PROP(node_id, settle_time_us), \
        .ghostkey_check = !DT_PROP(node_id, no_ghostkey_check), \
        IF_ENABLED(DT_NODE_HAS_PROP(node_id, actual_key_mask), ( \
        .actual_key_mask = INPUT_KBD_MATRIX_DATA_NAME(node_id, actual_key_mask), \
        )) \
        \
        .matrix_stable_state = INPUT_KBD_MATRIX_DATA_NAME(node_id, stable_state), \
        .matrix_unstable_state = INPUT_KBD_MATRIX_DATA_NAME(node_id, unstable_state), \
        .matrix_previous_state = INPUT_KBD_MATRIX_DATA_NAME(node_id, previous_state), \
        .matrix_new_state = INPUT_KBD_MATRIX_DATA_NAME(node_id, new_state), \
        .scan_cycle_idx = INPUT_KBD_MATRIX_DATA_NAME(node_id, scan_cycle_idx), \
}
```

根据设备树（Devicetree）初始化通用键盘矩阵配置（Keyboard Matrix Config），并指定行数和列数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 设备树节点标识符。 |
| `_api` | 指向 `input_kbd_matrix_api` 结构体的指针。 |
| `_row_size` | 矩阵行数（Matrix Row Count）。 |
| `_col_size` | 矩阵列数（Matrix Column Count）。 |

<a id="ga512bea2ca97569f465074ca8f231a0a3"></a>

### `INPUT_KBD_MATRIX_DT_DEFINE`

```c
#define INPUT_KBD_MATRIX_DT_DEFINE ( node_id)
```

```c
#include <zephyr/input/input_kbd_matrix.h>
```

展开值（Value）：

```c
INPUT_KBD_MATRIX_DT_DEFINE_ROW_COL( \
        node_id, DT_PROP(node_id, row_size), DT_PROP(node_id, col_size))
```

根据设备树（Devicetree）定义通用键盘矩阵支持数据（Keyboard Matrix Support Data）。

<a id="gac1a4389b1afeab9c48a15c024bfb0cac"></a>

### `INPUT_KBD_MATRIX_DT_DEFINE_ROW_COL`

```c
#define INPUT_KBD_MATRIX_DT_DEFINE_ROW_COL ( node_id, _row_size, _col_size )
```

```c
#include <zephyr/input/input_kbd_matrix.h>
```

展开值（Value）：

```c
BUILD_ASSERT(IN_RANGE(_row_size, 1, INPUT_KBD_MATRIX_ROW_BITS), "invalid row-size"); \
BUILD_ASSERT(IN_RANGE(_col_size, 1, UINT8_MAX), "invalid col-size"); \
IF_ENABLED(DT_NODE_HAS_PROP(node_id, actual_key_mask), ( \
BUILD_ASSERT(DT_PROP_LEN(node_id, actual_key_mask) == _col_size, \
             "actual-key-mask size does not match the number of columns"); \
static INPUT_KBD_ACTUAL_KEY_MASK_CONST kbd_row_t \
        INPUT_KBD_MATRIX_DATA_NAME(node_id, actual_key_mask)[_col_size] = \
                DT_PROP(node_id, actual_key_mask); \
)) \
static kbd_row_t INPUT_KBD_MATRIX_DATA_NAME(node_id, stable_state)[_col_size]; \
static kbd_row_t INPUT_KBD_MATRIX_DATA_NAME(node_id, unstable_state)[_col_size]; \
static kbd_row_t INPUT_KBD_MATRIX_DATA_NAME(node_id, previous_state)[_col_size]; \
static kbd_row_t INPUT_KBD_MATRIX_DATA_NAME(node_id, new_state)[_col_size]; \
static uint8_t INPUT_KBD_MATRIX_DATA_NAME(node_id, scan_cycle_idx)[_row_size * _col_size];
```

根据设备树（Devicetree）定义通用键盘矩阵支持数据（Keyboard Matrix Support Data），并指定行数和列数。

<a id="gab19b4a8c66c5540b4e690459655f92fd"></a>

### `INPUT_KBD_MATRIX_DT_INST_COMMON_CONFIG_INIT`

```c
#define INPUT_KBD_MATRIX_DT_INST_COMMON_CONFIG_INIT ( inst, api )
```

```c
#include <zephyr/input/input_kbd_matrix.h>
```

展开值（Value）：

```c
INPUT_KBD_MATRIX_DT_COMMON_CONFIG_INIT(DT_DRV_INST(inst), api)
```

根据设备树实例（Devicetree Instance）初始化通用键盘矩阵配置。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 实例（instance）。 |
| `api` | 指向 `input_kbd_matrix_api` 结构体的指针。 |

<a id="gac6baf9b284f0796cdd5dbcef338f9588"></a>

### `INPUT_KBD_MATRIX_DT_INST_COMMON_CONFIG_INIT_ROW_COL`

```c
#define INPUT_KBD_MATRIX_DT_INST_COMMON_CONFIG_INIT_ROW_COL ( inst, api, row_size, col_size )
```

```c
#include <zephyr/input/input_kbd_matrix.h>
```

展开值（Value）：

```c
INPUT_KBD_MATRIX_DT_COMMON_CONFIG_INIT_ROW_COL(DT_DRV_INST(inst), api, row_size, col_size)
```

根据设备树实例（Devicetree Instance）初始化通用键盘矩阵配置，并指定行数和列数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 实例（instance）。 |
| `api` | 指向 `input_kbd_matrix_api` 结构体的指针。 |
| `row_size` | 矩阵行数（Matrix Row Count）。 |
| `col_size` | 矩阵列数（Matrix Column Count）。 |

<a id="gab3ea5b7d597574b32ced16604648a6d2"></a>

### `INPUT_KBD_MATRIX_DT_INST_DEFINE`

```c
#define INPUT_KBD_MATRIX_DT_INST_DEFINE ( inst)
```

```c
#include <zephyr/input/input_kbd_matrix.h>
```

展开值（Value）：

```c
INPUT_KBD_MATRIX_DT_DEFINE(DT_DRV_INST(inst))
```

根据设备树实例（Devicetree Instance）定义通用键盘矩阵支持数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 实例（instance）。 |

<a id="ga1d3fe52f10c75dc4c32c8583c05fb2a2"></a>

### `INPUT_KBD_MATRIX_DT_INST_DEFINE_ROW_COL`

```c
#define INPUT_KBD_MATRIX_DT_INST_DEFINE_ROW_COL ( inst, row_size, col_size )
```

```c
#include <zephyr/input/input_kbd_matrix.h>
```

展开值（Value）：

```c
INPUT_KBD_MATRIX_DT_DEFINE_ROW_COL(DT_DRV_INST(inst), row_size, col_size)
```

根据设备树实例（Devicetree Instance）定义通用键盘矩阵支持数据，并指定行数和列数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 实例（instance）。 |
| `row_size` | 矩阵行数（Matrix Row Count）。 |
| `col_size` | 矩阵列数（Matrix Column Count）。 |

<a id="gae395cd03c295673dc9563c252ba7e022"></a>

### `INPUT_KBD_MATRIX_ROW_BITS`

```c
#define INPUT_KBD_MATRIX_ROW_BITS NUM_BITS(kbd_row_t)
```

```c
#include <zephyr/input/input_kbd_matrix.h>
```

最大行数（Maximum Number of Rows）。

<a id="ga80a384d2041dcee27d7940a1e408d82a"></a>

### `INPUT_KBD_MATRIX_SCAN_OCURRENCES`

```c
#define INPUT_KBD_MATRIX_SCAN_OCURRENCES 30U
```

```c
#include <zephyr/input/input_kbd_matrix.h>
```

跟踪的扫描周期数（Scan Cycles）。

<a id="ga352d484344c93c30f5cad75551793377"></a>

### `INPUT_KBD_STRUCT_CHECK`

```c
#define INPUT_KBD_STRUCT_CHECK ( config, data )
```

```c
#include <zephyr/input/input_kbd_matrix.h>
```

展开值（Value）：

```c
BUILD_ASSERT(offsetof(config, common) == 0, \
             "struct input_kbd_matrix_common_config must be placed first"); \
BUILD_ASSERT(offsetof(data, common) == 0, \
             "struct input_kbd_matrix_common_data must be placed first")
```

验证通用数据结构的偏移量（Offset）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `config` | 配置结构体（config structure）的名称。 |
| `data` | 数据结构名称（Data Structure Name）。 |

<a id="ga1343b97a8b072f8ed362e8a4f242bdd1"></a>

### `PRIkbdrow`

```c
#define PRIkbdrow "02" PRIx8
```

```c
#include <zephyr/input/input_kbd_matrix.h>
```

<a id="gac7d5c811da0c9ab2660be3c3f2fcfe86"></a>

### `kbd_row_t`

```c
typedef uint8_t kbd_row_t
```

```c
#include <zephyr/input/input_kbd_matrix.h>
```

行条目数据类型（Row Entry Data Type）。

<a id="ga90ec50249d8e561d69f550fcaa6bd969"></a>

### `input_kbd_matrix_active()`

```c
bool input_kbd_matrix_active ( const struct device * dev)
```

```c
#include <zephyr/input/input_kbd_matrix.h>
```

矩阵被视为活动状态（Active）时返回 `true`。

矩阵被视为活动状态（Active）时返回 `true`，即有按键按下，或有按键正在等待去抖（Debounce）或释放。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 键盘矩阵设备实例（Keyboard Matrix Device Instance）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | 矩阵处于活动状态（Active）。 |
| `false` | 矩阵处于空闲状态（Idle），所有按键均已释放。 |

<a id="gab35f4bf523760933294242ccc8226490"></a>

### `input_kbd_matrix_actual_key_mask_set()`

```c
int input_kbd_matrix_actual_key_mask_set ( const struct device * dev, uint8_t row, uint8_t col, bool enabled )
```

```c
#include <zephyr/input/input_kbd_matrix.h>
```

在实际按键掩码（Actual Key Mask）中启用或禁用特定的行列组合。

允许在运行时启用或禁用实际按键掩码（Actual Key Mask）中的特定行列组合。当某种配置缺少部分按键，且具体配置在运行时确定时，这会很有用。要求启用 `CONFIG_INPUT_KBD_ACTUAL_KEY_MASK_DYNAMIC`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向键盘矩阵（keyboard matrix）设备的指针。 |
| `row` | 要启用或禁用的矩阵行（Row）。 |
| `col` | 要启用或禁用的矩阵列（Column）。 |
| `enabled` | 指定的行列位置要启用还是禁用（Enable/Disable）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 更改成功时。 |
| `-errno` | 若行或列超出设备范围，则返回负 errno 值。 |

<a id="ga938dc38da7e81e5a68b8b9dc585c4bab"></a>

### `input_kbd_matrix_common_init()`

```c
int input_kbd_matrix_common_init ( const struct device * dev)
```

```c
#include <zephyr/input/input_kbd_matrix.h>
```

在初始化时初始化键盘矩阵设备（Keyboard Matrix Device）的公共函数。

必须在设备初始化函数（Init Function）的末尾调用此函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 键盘矩阵设备实例（Keyboard Matrix Device Instance）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 初始化成功时。 |
| `-errno` | 失败时返回负 errno 值。 |

<a id="ga6d843c7213bf5c0af9003c165a5f3e03"></a>

### `input_kbd_matrix_drive_column_hook()`

```c
void input_kbd_matrix_drive_column_hook ( const struct device * dev, int col )
```

```c
#include <zephyr/input/input_kbd_matrix.h>
```

驱动列的钩子（Drive Column Hook）。

应用可实现此钩子，以处理列选择的特殊行为（Column Selection Quirks）。在驱动专用 `drive_column` 函数之后调用。要求启用 `CONFIG_INPUT_KBD_DRIVE_COLUMN_HOOK`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 键盘矩阵设备实例（Keyboard Matrix Device Instance）。 |
| `col` | 要驱动的列，或者 `INPUT_KBD_MATRIX_COLUMN_DRIVE_NONE`、`INPUT_KBD_MATRIX_COLUMN_DRIVE_ALL`。 |

<a id="ga8e72535859abe307b4409dc4177b5721"></a>

### `input_kbd_matrix_ghosting()`

```c
bool input_kbd_matrix_ghosting ( const struct device * dev)
```

```c
#include <zephyr/input/input_kbd_matrix.h>
```

检查当前键盘矩阵状态是否存在鬼键（Ghost Keys）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 键盘矩阵设备实例（Keyboard Matrix Device Instance）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | 检测到鬼键（Ghosting Key）。 |
| `false` | 未检测到鬼键（Ghosting Key）。 |

<a id="gaf97b6ff410631f111d7c3a7aa7f64171"></a>

### `input_kbd_matrix_poll_start()`

```c
void input_kbd_matrix_poll_start ( const struct device * dev)
```

```c
#include <zephyr/input/input_kbd_matrix.h>
```

开始扫描键盘矩阵（Keyboard Matrix）。

启动键盘矩阵扫描周期（Scanning Cycle）。设备进入检测模式（Detect Mode）后，应响应按下事件调用此函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 键盘矩阵设备实例（Keyboard Matrix Device Instance）。 |

<a id="ga45a596e00af6ebf547f44a01cd07d539"></a>

### `input_kbd_matrix_update_state()`

```c
void input_kbd_matrix_update_state ( const struct device * dev)
```

```c
#include <zephyr/input/input_kbd_matrix.h>
```

更新键盘矩阵状态并执行去抖（Debouncing）。

驱动必须先为键盘矩阵填充 `input_kbd_matrix_common_config` 和 `input_kbd_matrix_common_data`。此函数随后更新稳定与不稳定状态，对各按键执行去抖（Per-key Debouncing），并向输入子系统（Input Subsystem）报告按键事件。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 键盘矩阵设备实例（Keyboard Matrix Device Instance）。 |


## 6.7\_原页交叉引用（Cross References）

- [input_kbd_matrix.h](../api_file_serial_motion_reference/P005_zephyr__input__input_kbd_matrix.h_文件参考.md)
- [input_kbd_matrix_api](../system_service_model_reference/P054_input_kbd_matrix_api_结构体.md)
- [input_kbd_matrix_common_config](../system_service_model_reference/P055_input_kbd_matrix_common_config_结构体.md)
- [input_kbd_matrix_common_data](../system_service_model_reference/P056_input_kbd_matrix_common_data_结构体.md)
- [PRIx8](../api_file_reference/P171_____w__zephyr__zephyr__lib__libc__minimal__include__inttypes.h_文件参考.md#adac1acc1d24060aeee7791a99d1a3a8c)
- [NUM_BITS](../util_reference/P002_通用工具头文件参考.md#afa27c06d0ad6b949289431ad75f104ab)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [device](../device_reference/P002_设备对象结构.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [DEVICE_DT_NAME_GET](../device_reference/P001_设备模型公共接口.md#ga8ebbf17ef805817aa638f36f177a1a0e)
- [DT_PROP](../dt_property_reference/P001_设备树属性读取宏.md#ga8e1fd9ebacd85d2013df027d041d506b)
- [DT_PROP_OR](../dt_property_reference/P001_设备树属性读取宏.md#ga5e5bfc9b1a6627b3f73014329e96340f)
- [USEC_PER_MSEC](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#ga2d66311052e2bddf914610fb7345ff27)
- [DT_NODE_HAS_PROP](../dt_identity_reference/P002_设备树存在性与状态宏.md#gacce67bf20541cd2d07d8540058964692)
- [IN_RANGE](../util_reference/P001_通用工具公共接口.md#gaea00fb0c11b73f77da8884374e2121b4)
- [UINT8_MAX](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#aeb4e270a084ee26fe73e799861bd0252)
- [DT_PROP_LEN](../dt_property_reference/P001_设备树属性读取宏.md#gaa7f5afcedd1f54be79a5337e8e28a5b6)
- [DT_DRV_INST](../dt_instance_reference/P001_设备树驱动实例宏.md#ga219f413efba2f4c0151468b9a25a8dc1)
- [true](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7)
- [false](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a65e9886d74aaee76545e83dd09011727)
- [CONFIG_INPUT_KBD_ACTUAL_KEY_MASK_DYNAMIC](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT_KBD_ACTUAL_KEY_MASK_DYNAMIC)
- [CONFIG_INPUT_KBD_DRIVE_COLUMN_HOOK](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT_KBD_DRIVE_COLUMN_HOOK)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__device__model_html_ga8ebbf17ef805817aa638f36f177a1a0e"></a>
<a id="agroup__devicetree-generic-prop_html_ga8e1fd9ebacd85d2013df027d041d506b"></a>
<a id="agroup__input__kbd__matrix_html_ga5ad9141616b4a63068bfbe8004bba67d"></a>
<a id="agroup__clock__apis_html_ga2d66311052e2bddf914610fb7345ff27"></a>
<a id="agroup__devicetree-generic-exist_html_gacce67bf20541cd2d07d8540058964692"></a>
<a id="agroup__devicetree-generic-prop_html_ga5e5bfc9b1a6627b3f73014329e96340f"></a>
<a id="agroup__input__kbd__matrix_html_gac7cc0314fa201b1efbcac37cf5f90576"></a>
<a id="agroup__input__kbd__matrix_html_gac1a4389b1afeab9c48a15c024bfb0cac"></a>
<a id="agroup__devicetree-generic-prop_html_gaa7f5afcedd1f54be79a5337e8e28a5b6"></a>
<a id="agroup__input__kbd__matrix_html_gac7d5c811da0c9ab2660be3c3f2fcfe86"></a>
<a id="agroup__input__kbd__matrix_html_gae395cd03c295673dc9563c252ba7e022"></a>
<a id="agroup__input__kbd__matrix_html_gaec0209680e18da8584bdf41e5229aaae"></a>
<a id="agroup__sys-util_html_gaea00fb0c11b73f77da8884374e2121b4"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_aeb4e270a084ee26fe73e799861bd0252"></a>
<a id="agroup__devicetree-inst_html_ga219f413efba2f4c0151468b9a25a8dc1"></a>
<a id="agroup__input__kbd__matrix_html_ga3281b4e5909a1c07d8190092bc31cb12"></a>
<a id="agroup__input__kbd__matrix_html_ga512bea2ca97569f465074ca8f231a0a3"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P005_已发布音频能力服务（Published Audio Capabilities Service，PACS）.md) · [返回大纲](大纲.md) · [下一章](P007_网络分组过滤器 API（Network Packet Filter API）.md)
