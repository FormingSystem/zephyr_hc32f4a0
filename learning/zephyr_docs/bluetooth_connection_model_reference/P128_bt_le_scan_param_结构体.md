---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-128
title: bt_le_scan_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__scan__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第128章\_bt\_le\_scan\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__scan__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

低功耗蓝牙（LE）的扫描参数。

```c
#include <zephyr/bluetooth/bluetooth.h>
```

<a id="details"></a>

低功耗蓝牙（LE）的扫描参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 128.1\_数据成员（Data Fields）

<a id="r_a02d75322390287c3fa754bf915660d0c"></a>

```c
uint8_t type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[type](#a02d75322390287c3fa754bf915660d0c)。

扫描类型（Scan type）。

<a id="r_ac815b05fee8ce0dd24228305b7596207"></a>

```c
uint8_t options
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[options](#ac815b05fee8ce0dd24228305b7596207)。

扫描选项位域（Scanning options bit-field）。

<a id="r_a2f4e053d97c62b6fdf42a245908607f8"></a>

```c
uint16_t interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[interval](#a2f4e053d97c62b6fdf42a245908607f8)。

扫描间隔（Scan interval），为 N × 0.625 毫秒。

<a id="r_a37a7ee82e86a91cf7a9c2adf60bb526a"></a>

```c
uint16_t window
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[window](#a37a7ee82e86a91cf7a9c2adf60bb526a)。

扫描窗口（Scan window），为 N × 0.625 毫秒。

<a id="r_a3e71ce551dcc7762c29e2316996e2912"></a>

```c
uint16_t timeout
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[timeout](#a3e71ce551dcc7762c29e2316996e2912)。

扫描超时（Scan timeout），为 N × 10 毫秒。

<a id="r_a67a20bc94a3d98fa10af7b5b42dde328"></a>

```c
uint16_t interval_coded
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[interval_coded](#a67a20bc94a3d98fa10af7b5b42dde328)。

低功耗编码物理层扫描间隔（LE Coded PHY scan interval），为 N × 0.625 毫秒。

<a id="r_a93166af55dca71393c60cb3f7ac6d809"></a>

```c
uint16_t window_coded
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[window_coded](#a93166af55dca71393c60cb3f7ac6d809)。

低功耗编码物理层扫描窗口（LE Coded PHY scan window），为 N × 0.625 毫秒。

## 128.2\_详细说明（Detailed Documentation）

<a id="a2f4e053d97c62b6fdf42a245908607f8"></a>

### `interval`

```c
uint16_t bt_le_scan_param::interval
```

扫描间隔（Scan interval），为 N × 0.625 毫秒。

**说明（Note）**：注意（Note）：启用 `CONFIG_BT_SCAN_AND_INITIATE_IN_PARALLEL` 且应用希望并行扫描与连接时，为获得最佳性能，蓝牙控制器（Bluetooth Controller）可能要求扫描与连接建立使用相同的扫描间隔（Scan interval）。

<a id="a67a20bc94a3d98fa10af7b5b42dde328"></a>

### `interval_coded`

```c
uint16_t bt_le_scan_param::interval_coded
```

低功耗编码物理层扫描间隔（LE Coded PHY scan interval），为 N × 0.625 毫秒。

设为零时，使用与低功耗 1M 物理层（LE 1M PHY）相同的扫描间隔。

<a id="ac815b05fee8ce0dd24228305b7596207"></a>

### `options`

```c
uint8_t bt_le_scan_param::options
```

扫描选项位域（Scanning options bit-field）。

<a id="a3e71ce551dcc7762c29e2316996e2912"></a>

### `timeout`

```c
uint16_t bt_le_scan_param::timeout
```

扫描超时（Scan timeout），为 N × 10 毫秒。

通过扫描超时回调（Scan timeout callback）通知应用。设为零时禁用超时。

<a id="a02d75322390287c3fa754bf915660d0c"></a>

### `type`

```c
uint8_t bt_le_scan_param::type
```

扫描类型（Scan type）。

`BT_LE_SCAN_TYPE_ACTIVE` 或 `BT_LE_SCAN_TYPE_PASSIVE`。

<a id="a37a7ee82e86a91cf7a9c2adf60bb526a"></a>

### `window`

```c
uint16_t bt_le_scan_param::window
```

扫描窗口（Scan window），为 N × 0.625 毫秒。

**说明（Note）**：注意（Note）：启用 `CONFIG_BT_SCAN_AND_INITIATE_IN_PARALLEL` 且应用希望并行扫描与连接时，为获得最佳性能，蓝牙控制器（Bluetooth Controller）可能要求扫描与连接建立使用相同的扫描窗口（Scan window）。

<a id="a93166af55dca71393c60cb3f7ac6d809"></a>

### `window_coded`

```c
uint16_t bt_le_scan_param::window_coded
```

低功耗编码物理层扫描窗口（LE Coded PHY scan window），为 N × 0.625 毫秒。

设为零时，使用与低功耗 1M 物理层（LE 1M PHY）相同的扫描窗口。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/bluetooth.h`

## 128.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [CONFIG_BT_SCAN_AND_INITIATE_IN_PARALLEL](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SCAN_AND_INITIATE_IN_PARALLEL)
- [BT_LE_SCAN_TYPE_ACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggaf980473379afa477c09e19912d40d29eaf202213813092ba298cd046aed687f22)
- [BT_LE_SCAN_TYPE_PASSIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggaf980473379afa477c09e19912d40d29ea731c507ed451eb6f8f8372849185b006)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P127_bt_le_scan_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P129_bt_le_scan_recv_info_结构体.md)
