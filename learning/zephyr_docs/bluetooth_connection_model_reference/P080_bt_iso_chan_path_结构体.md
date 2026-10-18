---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-80
title: bt_iso_chan_path_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__iso__chan__path.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第80章\_bt\_iso\_chan\_path\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__iso__chan__path.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

等时信道（ISO Channel）的数据路径（Data Path）结构。

```c
#include <zephyr/bluetooth/iso.h>
```

<a id="details"></a>

等时信道（ISO Channel）的数据路径（Data Path）结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 80.1\_数据成员（Data Fields）

<a id="r_a5e4fb798376489a38a87e4052ff85550"></a>

```c
uint8_t pid
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[pid](#a5e4fb798376489a38a87e4052ff85550)。

默认路径标识符（Default path ID）。

<a id="r_a519c884281207d1165a61ccfb7fbcdf4"></a>

```c
uint8_t format
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[format](#a519c884281207d1165a61ccfb7fbcdf4)。

编码格式（Coding Format）。

<a id="r_a95db7917f7b9e90a33f494233c3266eb"></a>

```c
uint16_t cid
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[cid](#a95db7917f7b9e90a33f494233c3266eb)。

公司标识符（Company ID）。

<a id="r_aebc12293ba0b10a87f1852e2a3e53a23"></a>

```c
uint16_t vid
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[vid](#aebc12293ba0b10a87f1852e2a3e53a23)。

厂商定义的编解码器标识符（Vendor-defined Codec ID）。

<a id="r_adaed07de7e09263e3e941817eeb44258"></a>

```c
uint32_t delay
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[delay](#adaed07de7e09263e3e941817eeb44258)。

控制器延迟（Controller Delay），单位为微秒。

<a id="r_a0da75c4911a197fed7fd7f17c76dddae"></a>

```c
uint8_t cc_len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cc_len](#a0da75c4911a197fed7fd7f17c76dddae)。

编解码器配置长度（Codec Configuration length）。

<a id="r_ac370bfca109153db02a747120c227104"></a>

```c
const uint8_t * cc
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cc](#ac370bfca109153db02a747120c227104)。

指向包含编解码器配置（Codec Configuration）的数组的指针。

## 80.2\_详细说明（Detailed Documentation）

<a id="ac370bfca109153db02a747120c227104"></a>

### `cc`

```c
const uint8_t* bt_iso_chan_path::cc
```

指向包含编解码器配置（Codec Configuration）的数组的指针。

当 `bt_iso_chan_path.cc_len` 非零时，不得为 `NULL`。

<a id="a0da75c4911a197fed7fd7f17c76dddae"></a>

### `cc_len`

```c
uint8_t bt_iso_chan_path::cc_len
```

编解码器配置长度（Codec Configuration length）。

<a id="a95db7917f7b9e90a33f494233c3266eb"></a>

### `cid`

```c
uint16_t bt_iso_chan_path::cid
```

公司标识符（Company ID）。

<a id="adaed07de7e09263e3e941817eeb44258"></a>

### `delay`

```c
uint32_t bt_iso_chan_path::delay
```

控制器延迟（Controller Delay），单位为微秒。

取值范围为 `BT_ISO_CONTROLLER_DELAY_MIN` 至 `BT_ISO_CONTROLLER_DELAY_MAX`。

<a id="a519c884281207d1165a61ccfb7fbcdf4"></a>

### `format`

```c
uint8_t bt_iso_chan_path::format
```

编码格式（Coding Format）。

有效值参见 `BT_HCI_CODING_FORMAT_*`。

<a id="a5e4fb798376489a38a87e4052ff85550"></a>

### `pid`

```c
uint8_t bt_iso_chan_path::pid
```

默认路径标识符（Default path ID）。

使用通过主机控制器接口传输的等时数据（ISO over HCI）时，设为 `BT_ISO_DATA_PATH_HCI`；使用厂商专用数据路径（Vendor specific data paths）时，取值在 `BT_ISO_DATA_PATH_VS_ID_MIN` 与 `BT_ISO_DATA_PATH_VS_ID_MAX` 之间。

<a id="aebc12293ba0b10a87f1852e2a3e53a23"></a>

### `vid`

```c
uint16_t bt_iso_chan_path::vid
```

厂商定义的编解码器标识符（Vendor-defined Codec ID）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/iso.h`

## 80.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/iso.h](https://docs.zephyrproject.org/latest/doxygen/html/iso_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [BT_ISO_CONTROLLER_DELAY_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga29bf2b36a4ab4e1325f626bbcf52a9a6)
- [BT_ISO_CONTROLLER_DELAY_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gae6ba7c8ea447112bcd7798d0351a9a91)
- [BT_ISO_DATA_PATH_HCI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gadd421c69edccfd695d728ded5feb6862)
- [BT_ISO_DATA_PATH_VS_ID_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ga9f26e30d05e571d3fc33dec8ae693e45)
- [BT_ISO_DATA_PATH_VS_ID_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gae5e1f7c86165b26fc6d93bc922676f9a)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P079_bt_iso_chan_ops_结构体.md) · [返回大纲](大纲.md) · [下一章](P081_bt_iso_chan_qos_结构体.md)
