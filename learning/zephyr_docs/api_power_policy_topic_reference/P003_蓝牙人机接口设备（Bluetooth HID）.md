---
id: learning.zephyr-docs.api-power-policy-topic-reference.page-3
title: 蓝牙人机接口设备（Bluetooth HID）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_蓝牙人机接口设备（Bluetooth HID）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙人机接口设备（Bluetooth HID）

<a id="details"></a>

蓝牙人机接口设备（Bluetooth HID）

<a id="header-member-group"></a>
<a id="member-group"></a>

## 3.1\_HID 协议模式值（Protocol Mode Values）

定义于 HID v1.1.2 规范 2.1.2 节，其中规定报告协议模式（Report Protocol Mode）为默认模式。

双向 `GET_PROTOCOL` 和 `SET_PROTOCOL` 都携带相同取值，因此设备（Device）与主机（Host）角色共用这些值。

<a id="r_gac9f6cb6981d548e3db9e6a0a99bc6fc9"></a>

```c
#define BT_HID_PROTOCOL_BOOT_MODE 0x00U
```

相关声明：[BT_HID_PROTOCOL_BOOT_MODE](#gac9f6cb6981d548e3db9e6a0a99bc6fc9)。

引导协议模式（Boot Protocol Mode），旧式模式（Legacy）。

<a id="r_gad4f973c2bdd628e0d6b09884a83219c7"></a>

```c
#define BT_HID_PROTOCOL_REPORT_MODE 0x01U
```

相关声明：[BT_HID_PROTOCOL_REPORT_MODE](#gad4f973c2bdd628e0d6b09884a83219c7)。

报告协议模式（Report Protocol Mode），默认模式（Default）。

## 3.2\_HID 报告类型值（Report Type Values）

`GET_REPORT`、`SET_REPORT` 和 `DATA` 传输携带的报告类型（Report Type）。

定义于 HID v1.1.2 规范表 3.4。

<a id="r_ga70b5259d0204510cd225b3de6c3d0361"></a>

```c
#define BT_HID_REPORT_TYPE_OTHER 0x00U
```

相关声明：[BT_HID_REPORT_TYPE_OTHER](#ga70b5259d0204510cd225b3de6c3d0361)。

保留报告类型（Reserved Report Type），用于不适用任何类型的场合。

<a id="r_gafb92c081d13c6084fbd51a3df28b42dc"></a>

```c
#define BT_HID_REPORT_TYPE_INPUT 0x01U
```

相关声明：[BT_HID_REPORT_TYPE_INPUT](#gafb92c081d13c6084fbd51a3df28b42dc)。

输入报告（Input Report），从设备到主机。

<a id="r_gadfca183266ec397319b3242bbcea6c3e"></a>

```c
#define BT_HID_REPORT_TYPE_OUTPUT 0x02U
```

相关声明：[BT_HID_REPORT_TYPE_OUTPUT](#gadfca183266ec397319b3242bbcea6c3e)。

输出报告（Output Report），从主机到设备。

<a id="r_gac4cab3c0de498e45609c945780386353"></a>

```c
#define BT_HID_REPORT_TYPE_FEATURE 0x03U
```

相关声明：[BT_HID_REPORT_TYPE_FEATURE](#gac4cab3c0de498e45609c945780386353)。

特性报告（Feature Report）。

## 3.3\_HID 握手结果码（HANDSHAKE Result Codes）

控制通道（Control Channel）上所发请求的结果（Result）。

定义于 HID v1.1.2 规范 3.1.2.1 节。主机（Host）将这些结果报告给应用，设备（Device）使用它们作答，因此两种角色共用这些值。

<a id="r_ga19706f1a5e6fa8e112a3610aa8e8821f"></a>

```c
#define BT_HID_HS_RSP_SUCCESS 0x00U
```

相关声明：[BT_HID_HS_RSP_SUCCESS](#ga19706f1a5e6fa8e112a3610aa8e8821f)。

请求已成功完成（Completed Successfully）。

<a id="r_gae156f477153c8aac8bd033b5c695183f"></a>

```c
#define BT_HID_HS_RSP_NOT_READY 0x01U
```

相关声明：[BT_HID_HS_RSP_NOT_READY](#gae156f477153c8aac8bd033b5c695183f)。

对端（Peer）过忙，无法接受请求；发送方可以重试。

<a id="r_ga5907f25b03338cd30fe5595fd90fcfb3"></a>

```c
#define BT_HID_HS_RSP_ERR_INVALID_REPORT_ID 0x02U
```

相关声明：[BT_HID_HS_RSP_ERR_INVALID_REPORT_ID](#ga5907f25b03338cd30fe5595fd90fcfb3)。

请求引用了不支持的报告 ID（Report ID）。

<a id="r_ga5f50003a9615d2183a577cf99cc295b9"></a>

```c
#define BT_HID_HS_RSP_ERR_UNSUPPORTED_REQ 0x03U
```

相关声明：[BT_HID_HS_RSP_ERR_UNSUPPORTED_REQ](#ga5f50003a9615d2183a577cf99cc295b9)。

对端（Peer）不支持此请求。

<a id="r_ga2703efb41d6834e2681bba09b6cce648"></a>

```c
#define BT_HID_HS_RSP_ERR_INVALID_PARAM 0x04U
```

相关声明：[BT_HID_HS_RSP_ERR_INVALID_PARAM](#ga2703efb41d6834e2681bba09b6cce648)。

请求携带无效参数（Invalid Parameter）。

<a id="r_ga46ab8c7af038b5fb8e2e6baa0032f4d9"></a>

```c
#define BT_HID_HS_RSP_ERR_UNKNOWN 0x0eU
```

相关声明：[BT_HID_HS_RSP_ERR_UNKNOWN](#ga46ab8c7af038b5fb8e2e6baa0032f4d9)。

对端（Peer）无法确定错误情况（Error Condition）。

<a id="r_ga29aaf9e0914f0226d2ac741c32cdfe3b"></a>

```c
#define BT_HID_HS_RSP_ERR_FATAL 0x0fU
```

相关声明：[BT_HID_HS_RSP_ERR_FATAL](#ga29aaf9e0914f0226d2ac741c32cdfe3b)。

对端（Peer）遇到致命错误（Fatal Error），需要重启。

## 3.4\_详细说明（Detailed Documentation）

<a id="ga29aaf9e0914f0226d2ac741c32cdfe3b"></a>

### `BT_HID_HS_RSP_ERR_FATAL`

```c
#define BT_HID_HS_RSP_ERR_FATAL 0x0fU
```

```c
#include <zephyr/bluetooth/classic/hid.h>
```

对端（Peer）遇到致命错误（Fatal Error），需要重启。

<a id="ga2703efb41d6834e2681bba09b6cce648"></a>

### `BT_HID_HS_RSP_ERR_INVALID_PARAM`

```c
#define BT_HID_HS_RSP_ERR_INVALID_PARAM 0x04U
```

```c
#include <zephyr/bluetooth/classic/hid.h>
```

请求携带无效参数（Invalid Parameter）。

<a id="ga5907f25b03338cd30fe5595fd90fcfb3"></a>

### `BT_HID_HS_RSP_ERR_INVALID_REPORT_ID`

```c
#define BT_HID_HS_RSP_ERR_INVALID_REPORT_ID 0x02U
```

```c
#include <zephyr/bluetooth/classic/hid.h>
```

请求引用了不支持的报告 ID（Report ID）。

<a id="ga46ab8c7af038b5fb8e2e6baa0032f4d9"></a>

### `BT_HID_HS_RSP_ERR_UNKNOWN`

```c
#define BT_HID_HS_RSP_ERR_UNKNOWN 0x0eU
```

```c
#include <zephyr/bluetooth/classic/hid.h>
```

对端（Peer）无法确定错误情况（Error Condition）。

<a id="ga5f50003a9615d2183a577cf99cc295b9"></a>

### `BT_HID_HS_RSP_ERR_UNSUPPORTED_REQ`

```c
#define BT_HID_HS_RSP_ERR_UNSUPPORTED_REQ 0x03U
```

```c
#include <zephyr/bluetooth/classic/hid.h>
```

对端（Peer）不支持此请求。

<a id="gae156f477153c8aac8bd033b5c695183f"></a>

### `BT_HID_HS_RSP_NOT_READY`

```c
#define BT_HID_HS_RSP_NOT_READY 0x01U
```

```c
#include <zephyr/bluetooth/classic/hid.h>
```

对端（Peer）过忙，无法接受请求；发送方可以重试。

<a id="ga19706f1a5e6fa8e112a3610aa8e8821f"></a>

### `BT_HID_HS_RSP_SUCCESS`

```c
#define BT_HID_HS_RSP_SUCCESS 0x00U
```

```c
#include <zephyr/bluetooth/classic/hid.h>
```

请求已成功完成（Completed Successfully）。

<a id="gac9f6cb6981d548e3db9e6a0a99bc6fc9"></a>

### `BT_HID_PROTOCOL_BOOT_MODE`

```c
#define BT_HID_PROTOCOL_BOOT_MODE 0x00U
```

```c
#include <zephyr/bluetooth/classic/hid.h>
```

引导协议模式（Boot Protocol Mode），旧式模式（Legacy）。

<a id="gad4f973c2bdd628e0d6b09884a83219c7"></a>

### `BT_HID_PROTOCOL_REPORT_MODE`

```c
#define BT_HID_PROTOCOL_REPORT_MODE 0x01U
```

```c
#include <zephyr/bluetooth/classic/hid.h>
```

报告协议模式（Report Protocol Mode），默认模式（Default）。

<a id="gac4cab3c0de498e45609c945780386353"></a>

### `BT_HID_REPORT_TYPE_FEATURE`

```c
#define BT_HID_REPORT_TYPE_FEATURE 0x03U
```

```c
#include <zephyr/bluetooth/classic/hid.h>
```

特性报告（Feature Report）。

<a id="gafb92c081d13c6084fbd51a3df28b42dc"></a>

### `BT_HID_REPORT_TYPE_INPUT`

```c
#define BT_HID_REPORT_TYPE_INPUT 0x01U
```

```c
#include <zephyr/bluetooth/classic/hid.h>
```

输入报告（Input Report），从设备到主机。

<a id="ga70b5259d0204510cd225b3de6c3d0361"></a>

### `BT_HID_REPORT_TYPE_OTHER`

```c
#define BT_HID_REPORT_TYPE_OTHER 0x00U
```

```c
#include <zephyr/bluetooth/classic/hid.h>
```

保留报告类型（Reserved Report Type），用于不适用任何类型的场合。

<a id="gadfca183266ec397319b3242bbcea6c3e"></a>

### `BT_HID_REPORT_TYPE_OUTPUT`

```c
#define BT_HID_REPORT_TYPE_OUTPUT 0x02U
```

```c
#include <zephyr/bluetooth/classic/hid.h>
```

输出报告（Output Report），从主机到设备。


## 3.5\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/hid.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2classic_2hid_8h.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P002_游戏音频配置文件（Gaming Audio Profile，GMAP）的 LC3 预设.md) · [返回大纲](大纲.md) · [下一章](P004_主机命令驱动后端 API（Host Command Driver Backend API）.md)
