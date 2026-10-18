---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-12
title: bt_conn_le_create_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__le__create__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_bt\_conn\_le\_create\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__le__create__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/conn.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 12.1\_数据成员（Data Fields）

<a id="r_a4b1e26c0976d9c900b831c886c77b055"></a>

```c
uint32_t options
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[options](#a4b1e26c0976d9c900b831c886c77b055)。

创建连接选项的位域（Create connection options bit-field）。

<a id="r_a5cfae677f924534dc5bc7b38c457a7af"></a>

```c
uint16_t interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[interval](#a5cfae677f924534dc5bc7b38c457a7af)。

扫描间隔（Scan interval），为 N × 0.625 毫秒。

<a id="r_a339b99f65c5029ada6cdf453ab1f258e"></a>

```c
uint16_t window
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[window](#a339b99f65c5029ada6cdf453ab1f258e)。

扫描窗口（Scan window），为 N × 0.625 毫秒。

<a id="r_a2bc978ac97435fe5f87c6e01692f2910"></a>

```c
uint16_t interval_coded
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[interval_coded](#a2bc978ac97435fe5f87c6e01692f2910)。

低功耗编码物理层扫描间隔（LE Coded PHY scan interval），为 N × 0.625 毫秒。

<a id="r_ae62491837d35d95e32016b793edf8c96"></a>

```c
uint16_t window_coded
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[window_coded](#ae62491837d35d95e32016b793edf8c96)。

低功耗编码物理层扫描窗口（LE Coded PHY scan window），为 N × 0.625 毫秒。

<a id="r_a59f05bfb9468779d02f8d0beeb7a35c1"></a>

```c
uint16_t timeout
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[timeout](#a59f05bfb9468779d02f8d0beeb7a35c1)。

连接发起超时（Connection initiation timeout），为 N × 10 毫秒。

## 12.2\_详细说明（Detailed Documentation）

<a id="a5cfae677f924534dc5bc7b38c457a7af"></a>

### `interval`

```c
uint16_t bt_conn_le_create_param::interval
```

扫描间隔（Scan interval），为 N × 0.625 毫秒。

**说明（Note）**：注意（Note）：启用 `CONFIG_BT_SCAN_AND_INITIATE_IN_PARALLEL` 且应用希望并行扫描与连接时，为获得最佳性能，蓝牙控制器（Bluetooth Controller）可能要求扫描与连接建立使用相同的扫描间隔（Scan interval）。

<a id="a2bc978ac97435fe5f87c6e01692f2910"></a>

### `interval_coded`

```c
uint16_t bt_conn_le_create_param::interval_coded
```

低功耗编码物理层扫描间隔（LE Coded PHY scan interval），为 N × 0.625 毫秒。

设为零时，使用与低功耗 1M 物理层（LE 1M PHY）相同的扫描间隔。

<a id="a4b1e26c0976d9c900b831c886c77b055"></a>

### `options`

```c
uint32_t bt_conn_le_create_param::options
```

创建连接选项的位域（Create connection options bit-field）。

<a id="a59f05bfb9468779d02f8d0beeb7a35c1"></a>

### `timeout`

```c
uint16_t bt_conn_le_create_param::timeout
```

连接发起超时（Connection initiation timeout），为 N × 10 毫秒。

设为零时，使用默认超时 `CONFIG_BT_CREATE_CONN_TIMEOUT`。

**说明（Note）**：注意（Note）：`bt_conn_le_create_auto` 不使用此项。

<a id="a339b99f65c5029ada6cdf453ab1f258e"></a>

### `window`

```c
uint16_t bt_conn_le_create_param::window
```

扫描窗口（Scan window），为 N × 0.625 毫秒。

**说明（Note）**：注意（Note）：启用 `CONFIG_BT_SCAN_AND_INITIATE_IN_PARALLEL` 且应用希望并行扫描与连接时，为获得最佳性能，蓝牙控制器（Bluetooth Controller）可能要求扫描与连接建立使用相同的扫描窗口（Scan window）。

<a id="ae62491837d35d95e32016b793edf8c96"></a>

### `window_coded`

```c
uint16_t bt_conn_le_create_param::window_coded
```

低功耗编码物理层扫描窗口（LE Coded PHY scan window），为 N × 0.625 毫秒。

设为零时，使用与低功耗 1M 物理层（LE 1M PHY）相同的扫描窗口。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/conn.h`

## 12.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [CONFIG_BT_SCAN_AND_INITIATE_IN_PARALLEL](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SCAN_AND_INITIATE_IN_PARALLEL)
- [CONFIG_BT_CREATE_CONN_TIMEOUT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CREATE_CONN_TIMEOUT)
- [bt_conn_le_create_auto](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaecfaf2cb44772511dbb585de8f76f09b)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P011_bt_conn_le_conn_rate_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P013_bt_conn_le_create_synced_param_结构体.md)
