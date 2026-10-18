---
id: learning.zephyr-docs.api-file-serial-motion-reference.page-5
title: zephyr__input__input_kbd_matrix.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/input__kbd__matrix_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_zephyr\_\_input\_\_input\_kbd\_matrix.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/input__kbd__matrix_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

键盘矩阵输入设备（Keyboard Matrix Input Devices）的主头文件。

<a id="details"></a>

```c
#include <zephyr/device.h>
#include <zephyr/kernel.h>
#include <zephyr/pm/device.h>
#include <zephyr/sys/atomic.h>
#include <zephyr/sys/util.h>
#include <zephyr/sys/clock.h>
#include <zephyr/toolchain.h>
```

查看此文件的源码。

键盘矩阵输入设备（Keyboard Matrix Input Devices）的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 5.1\_数据结构（Data Structures）

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

## 5.2\_宏定义（Macros）

<a id="r_ga2f35f23d426f93f71057a31f612a88de"></a>

```c
#define INPUT_KBD_MATRIX_COLUMN_DRIVE_NONE -1
```

相关声明：[INPUT_KBD_MATRIX_COLUMN_DRIVE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#ga2f35f23d426f93f71057a31f612a88de)。

`drive_column` 的特殊参数，表示不驱动任何列（Column）。

<a id="r_ga6d27ba5612c09d80087e854b21fb9e65"></a>

```c
#define INPUT_KBD_MATRIX_COLUMN_DRIVE_ALL -2
```

相关声明：[INPUT_KBD_MATRIX_COLUMN_DRIVE_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#ga6d27ba5612c09d80087e854b21fb9e65)。

`drive_column` 的特殊参数，表示驱动全部列（Columns）。

<a id="r_ga80a384d2041dcee27d7940a1e408d82a"></a>

```c
#define INPUT_KBD_MATRIX_SCAN_OCURRENCES 30U
```

相关声明：[INPUT_KBD_MATRIX_SCAN_OCURRENCES](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#ga80a384d2041dcee27d7940a1e408d82a)。

跟踪的扫描周期数（Scan Cycles）。

<a id="r_ga1343b97a8b072f8ed362e8a4f242bdd1"></a>

```c
#define PRIkbdrow "02" PRIx8
```

相关声明：[PRIkbdrow](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#ga1343b97a8b072f8ed362e8a4f242bdd1)、[PRIx8](../api_file_reference/P171_____w__zephyr__zephyr__lib__libc__minimal__include__inttypes.h_文件参考.md#adac1acc1d24060aeee7791a99d1a3a8c)。

<a id="r_gaec0209680e18da8584bdf41e5229aaae"></a>

```c
#define INPUT_KBD_ACTUAL_KEY_MASK_CONST
```

相关声明：[INPUT_KBD_ACTUAL_KEY_MASK_CONST](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#gaec0209680e18da8584bdf41e5229aaae)。

<a id="r_gae395cd03c295673dc9563c252ba7e022"></a>

```c
#define INPUT_KBD_MATRIX_ROW_BITS NUM_BITS(kbd_row_t)
```

相关声明：[INPUT_KBD_MATRIX_ROW_BITS](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#gae395cd03c295673dc9563c252ba7e022)、[NUM_BITS](../util_reference/P002_通用工具头文件参考.md#afa27c06d0ad6b949289431ad75f104ab)、[kbd_row_t](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#gac7d5c811da0c9ab2660be3c3f2fcfe86)。

最大行数（Maximum Number of Rows）。

<a id="r_gac7cc0314fa201b1efbcac37cf5f90576"></a>

```c
#define INPUT_KBD_MATRIX_DATA_NAME(node_id, name)
```

相关声明：[INPUT_KBD_MATRIX_DATA_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#gac7cc0314fa201b1efbcac37cf5f90576)。

<a id="r_gac1a4389b1afeab9c48a15c024bfb0cac"></a>

```c
#define INPUT_KBD_MATRIX_DT_DEFINE_ROW_COL(node_id, _row_size, _col_size)
```

相关声明：[INPUT_KBD_MATRIX_DT_DEFINE_ROW_COL](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#gac1a4389b1afeab9c48a15c024bfb0cac)。

根据设备树（Devicetree）定义通用键盘矩阵支持数据（Keyboard Matrix Support Data），并指定行数和列数。

<a id="r_ga512bea2ca97569f465074ca8f231a0a3"></a>

```c
#define INPUT_KBD_MATRIX_DT_DEFINE(node_id)
```

相关声明：[INPUT_KBD_MATRIX_DT_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#ga512bea2ca97569f465074ca8f231a0a3)。

根据设备树（Devicetree）定义通用键盘矩阵支持数据（Keyboard Matrix Support Data）。

<a id="r_ga1d3fe52f10c75dc4c32c8583c05fb2a2"></a>

```c
#define INPUT_KBD_MATRIX_DT_INST_DEFINE_ROW_COL(inst, row_size, col_size)
```

相关声明：[INPUT_KBD_MATRIX_DT_INST_DEFINE_ROW_COL](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#ga1d3fe52f10c75dc4c32c8583c05fb2a2)。

根据设备树实例（Devicetree Instance）定义通用键盘矩阵支持数据，并指定行数和列数。

<a id="r_gab3ea5b7d597574b32ced16604648a6d2"></a>

```c
#define INPUT_KBD_MATRIX_DT_INST_DEFINE(inst)
```

相关声明：[INPUT_KBD_MATRIX_DT_INST_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#gab3ea5b7d597574b32ced16604648a6d2)。

根据设备树实例（Devicetree Instance）定义通用键盘矩阵支持数据。

<a id="r_ga5ad9141616b4a63068bfbe8004bba67d"></a>

```c
#define INPUT_KBD_MATRIX_DT_COMMON_CONFIG_INIT_ROW_COL(node_id, _api, _row_size, _col_size)
```

相关声明：[INPUT_KBD_MATRIX_DT_COMMON_CONFIG_INIT_ROW_COL](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#ga5ad9141616b4a63068bfbe8004bba67d)。

根据设备树（Devicetree）初始化通用键盘矩阵配置（Keyboard Matrix Config），并指定行数和列数。

<a id="r_ga3281b4e5909a1c07d8190092bc31cb12"></a>

```c
#define INPUT_KBD_MATRIX_DT_COMMON_CONFIG_INIT(node_id, api)
```

相关声明：[INPUT_KBD_MATRIX_DT_COMMON_CONFIG_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#ga3281b4e5909a1c07d8190092bc31cb12)。

根据设备树（Devicetree）初始化通用键盘矩阵配置（Keyboard Matrix Config）。

<a id="r_gac6baf9b284f0796cdd5dbcef338f9588"></a>

```c
#define INPUT_KBD_MATRIX_DT_INST_COMMON_CONFIG_INIT_ROW_COL(inst, api, row_size, col_size)
```

相关声明：[INPUT_KBD_MATRIX_DT_INST_COMMON_CONFIG_INIT_ROW_COL](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#gac6baf9b284f0796cdd5dbcef338f9588)。

根据设备树实例（Devicetree Instance）初始化通用键盘矩阵配置，并指定行数和列数。

<a id="r_gab19b4a8c66c5540b4e690459655f92fd"></a>

```c
#define INPUT_KBD_MATRIX_DT_INST_COMMON_CONFIG_INIT(inst, api)
```

相关声明：[INPUT_KBD_MATRIX_DT_INST_COMMON_CONFIG_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#gab19b4a8c66c5540b4e690459655f92fd)。

根据设备树实例（Devicetree Instance）初始化通用键盘矩阵配置。

<a id="r_ga352d484344c93c30f5cad75551793377"></a>

```c
#define INPUT_KBD_STRUCT_CHECK(config, data)
```

相关声明：[INPUT_KBD_STRUCT_CHECK](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#ga352d484344c93c30f5cad75551793377)。

验证通用数据结构的偏移量（Offset）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 5.3\_类型定义（Typedefs）

<a id="r_gac7d5c811da0c9ab2660be3c3f2fcfe86"></a>

```c
typedef uint8_t kbd_row_t
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[kbd_row_t](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#gac7d5c811da0c9ab2660be3c3f2fcfe86)。

行条目数据类型（Row Entry Data Type）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 5.4\_函数（Functions）

<a id="r_gab35f4bf523760933294242ccc8226490"></a>

```c
int input_kbd_matrix_actual_key_mask_set (const struct device *dev, uint8_t row, uint8_t col, bool enabled)
```

相关声明：[input_kbd_matrix_actual_key_mask_set](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#gab35f4bf523760933294242ccc8226490)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

在实际按键掩码（Actual Key Mask）中启用或禁用特定的行列组合。

<a id="r_gaf97b6ff410631f111d7c3a7aa7f64171"></a>

```c
void input_kbd_matrix_poll_start (const struct device *dev)
```

相关声明：[input_kbd_matrix_poll_start](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#gaf97b6ff410631f111d7c3a7aa7f64171)、[device](../device_reference/P002_设备对象结构.md)。

开始扫描键盘矩阵（Keyboard Matrix）。

<a id="r_ga6d843c7213bf5c0af9003c165a5f3e03"></a>

```c
void input_kbd_matrix_drive_column_hook (const struct device *dev, int col)
```

相关声明：[input_kbd_matrix_drive_column_hook](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#ga6d843c7213bf5c0af9003c165a5f3e03)、[device](../device_reference/P002_设备对象结构.md)。

驱动列的钩子（Drive Column Hook）。

<a id="r_ga938dc38da7e81e5a68b8b9dc585c4bab"></a>

```c
int input_kbd_matrix_common_init (const struct device *dev)
```

相关声明：[input_kbd_matrix_common_init](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#ga938dc38da7e81e5a68b8b9dc585c4bab)、[device](../device_reference/P002_设备对象结构.md)。

在初始化时初始化键盘矩阵设备（Keyboard Matrix Device）的公共函数。

<a id="r_ga8e72535859abe307b4409dc4177b5721"></a>

```c
bool input_kbd_matrix_ghosting (const struct device *dev)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[input_kbd_matrix_ghosting](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#ga8e72535859abe307b4409dc4177b5721)、[device](../device_reference/P002_设备对象结构.md)。

检查当前键盘矩阵状态是否存在鬼键（Ghost Keys）。

<a id="r_ga45a596e00af6ebf547f44a01cd07d539"></a>

```c
void input_kbd_matrix_update_state (const struct device *dev)
```

相关声明：[input_kbd_matrix_update_state](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#ga45a596e00af6ebf547f44a01cd07d539)、[device](../device_reference/P002_设备对象结构.md)。

更新键盘矩阵状态并执行去抖（Debouncing）。

<a id="r_ga90ec50249d8e561d69f550fcaa6bd969"></a>

```c
bool input_kbd_matrix_active (const struct device *dev)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[input_kbd_matrix_active](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#ga90ec50249d8e561d69f550fcaa6bd969)、[device](../device_reference/P002_设备对象结构.md)。

矩阵被视为活动状态（Active）时返回 `true`。


## 5.5\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [zephyr/pm/device.h](../api_source_configuration_reference/P071_device.h_源码浏览.md)
- [zephyr/sys/atomic.h](../atomic_reference/P003_原子操作公共头文件源码.md)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [zephyr/sys/clock.h](../timer_reference/P091_系统时钟头文件源码.md)
- [zephyr/toolchain.h](../api_source_compiler_device_reference/P023_toolchain.h_源码浏览.md)
- [查看此文件的源码。](../api_source_configuration_reference/P037_input_kbd_matrix.h_源码浏览.md)
- [input_kbd_matrix_api](../system_service_model_reference/P054_input_kbd_matrix_api_结构体.md)
- [input_kbd_matrix_common_config](../system_service_model_reference/P055_input_kbd_matrix_common_config_结构体.md)
- [input_kbd_matrix_common_data](../system_service_model_reference/P056_input_kbd_matrix_common_data_结构体.md)
- [INPUT_KBD_MATRIX_COLUMN_DRIVE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#ga2f35f23d426f93f71057a31f612a88de)
- [INPUT_KBD_MATRIX_COLUMN_DRIVE_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#ga6d27ba5612c09d80087e854b21fb9e65)
- [INPUT_KBD_MATRIX_SCAN_OCURRENCES](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#ga80a384d2041dcee27d7940a1e408d82a)
- [PRIkbdrow](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#ga1343b97a8b072f8ed362e8a4f242bdd1)
- [PRIx8](../api_file_reference/P171_____w__zephyr__zephyr__lib__libc__minimal__include__inttypes.h_文件参考.md#adac1acc1d24060aeee7791a99d1a3a8c)
- [INPUT_KBD_ACTUAL_KEY_MASK_CONST](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#gaec0209680e18da8584bdf41e5229aaae)
- [INPUT_KBD_MATRIX_ROW_BITS](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#gae395cd03c295673dc9563c252ba7e022)
- [NUM_BITS](../util_reference/P002_通用工具头文件参考.md#afa27c06d0ad6b949289431ad75f104ab)
- [kbd_row_t](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#gac7d5c811da0c9ab2660be3c3f2fcfe86)
- [INPUT_KBD_MATRIX_DATA_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#gac7cc0314fa201b1efbcac37cf5f90576)
- [INPUT_KBD_MATRIX_DT_DEFINE_ROW_COL](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#gac1a4389b1afeab9c48a15c024bfb0cac)
- [INPUT_KBD_MATRIX_DT_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#ga512bea2ca97569f465074ca8f231a0a3)
- [INPUT_KBD_MATRIX_DT_INST_DEFINE_ROW_COL](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#ga1d3fe52f10c75dc4c32c8583c05fb2a2)
- [INPUT_KBD_MATRIX_DT_INST_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#gab3ea5b7d597574b32ced16604648a6d2)
- [INPUT_KBD_MATRIX_DT_COMMON_CONFIG_INIT_ROW_COL](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#ga5ad9141616b4a63068bfbe8004bba67d)
- [INPUT_KBD_MATRIX_DT_COMMON_CONFIG_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#ga3281b4e5909a1c07d8190092bc31cb12)
- [INPUT_KBD_MATRIX_DT_INST_COMMON_CONFIG_INIT_ROW_COL](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#gac6baf9b284f0796cdd5dbcef338f9588)
- [INPUT_KBD_MATRIX_DT_INST_COMMON_CONFIG_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#gab19b4a8c66c5540b4e690459655f92fd)
- [INPUT_KBD_STRUCT_CHECK](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#ga352d484344c93c30f5cad75551793377)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [input_kbd_matrix_actual_key_mask_set](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#gab35f4bf523760933294242ccc8226490)
- [device](../device_reference/P002_设备对象结构.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [input_kbd_matrix_poll_start](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#gaf97b6ff410631f111d7c3a7aa7f64171)
- [input_kbd_matrix_drive_column_hook](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#ga6d843c7213bf5c0af9003c165a5f3e03)
- [input_kbd_matrix_common_init](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#ga938dc38da7e81e5a68b8b9dc585c4bab)
- [input_kbd_matrix_ghosting](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#ga8e72535859abe307b4409dc4177b5721)
- [input_kbd_matrix_update_state](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#ga45a596e00af6ebf547f44a01cd07d539)
- [input_kbd_matrix_active](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#ga90ec50249d8e561d69f550fcaa6bd969)

<a id="header-details"></a>

---

[上一章](P004_zephyr__net__ssh__common.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P006_zephyr__drivers__sensor__mcux_lpcmp.h_文件参考.md)
