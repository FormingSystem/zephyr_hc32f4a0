---
id: learning.zephyr-docs.api-file-interface-reference.page-7
title: zephyr__bluetooth__audio__ccid.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ccid_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_zephyr\_\_bluetooth\_\_audio\_\_ccid.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ccid_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙音频内容控制标识符（Audio Content Control Identifier）的头文件。

<a id="details"></a>

```c
#include <stdint.h>
#include <zephyr/bluetooth/gatt.h>
```

查看此文件的源码。

蓝牙音频内容控制标识符（Bluetooth Audio Content Control Identifier，CCID）头文件。版权（Copyright）© 2020 Bose Corporation；© 2021–2024 Nordic Semiconductor ASA。SPDX 许可证标识（License Identifier）：`Apache-2.0`。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 7.1\_宏定义（Macros）

<a id="r_ga1be6ef63b32f44100a77e48c88a9c126"></a>

```c
#define BT_CCID_MIN 0U
```

相关声明：[BT_CCID_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccid.html#ga1be6ef63b32f44100a77e48c88a9c126)。

CCID 的最小值。

<a id="r_gaae664247d3537ab473c2f533602b2afa"></a>

```c
#define BT_CCID_MAX 255U
```

相关声明：[BT_CCID_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccid.html#gaae664247d3537ab473c2f533602b2afa)。

CCID 的最大值。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 7.2\_函数（Functions）

<a id="r_gad621dd750e4b1c23791afc72785990fc"></a>

```c
int bt_ccid_alloc_value (void)
```

相关声明：[bt_ccid_alloc_value](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccid.html#gad621dd750e4b1c23791afc72785990fc)。

分配一个 CCID 值。

<a id="r_ga07845fe5cc445a35448881430f528609"></a>

```c
const struct bt_gatt_attr * bt_ccid_find_attr (uint8_t ccid)
```

相关声明：[bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)、[bt_ccid_find_attr](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccid.html#ga07845fe5cc445a35448881430f528609)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取 CCID 值对应的通用属性配置文件（GATT）属性。


## 7.3\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/bluetooth/gatt.h](../api_source_runtime_reference/P021_gatt.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P085_ccid.h_源码浏览.md)
- [BT_CCID_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccid.html#ga1be6ef63b32f44100a77e48c88a9c126)
- [BT_CCID_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccid.html#gaae664247d3537ab473c2f533602b2afa)
- [bt_ccid_alloc_value](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccid.html#gad621dd750e4b1c23791afc72785990fc)
- [bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)
- [bt_ccid_find_attr](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccid.html#ga07845fe5cc445a35448881430f528609)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>

---

[上一章](P006_zephyr__mgmt__mcumgr__mgmt__callback_defines.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P008_zephyr__drivers__clock_control__clock_control_ifx.h_文件参考.md)
