---
id: learning.zephyr-docs.api-file-storage-event-reference.page-1
title: zephyr__bluetooth__classic__hid.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2classic_2hid_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_zephyr\_\_bluetooth\_\_classic\_\_hid.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2classic_2hid_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

设备与主机角色共享的蓝牙人机接口设备（HID）协议值。

查看此文件的源码。

<a id="details"></a>

设备与主机角色共享的蓝牙人机接口设备（HID）协议值。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.1\_宏定义（Macros）

<a id="define-members-0"></a>

### HID 协议模式值（Protocol Mode Values）

定义于 HID v1.1.2 规范 2.1.2 节，其中规定报告协议模式（Report Protocol Mode）为默认模式。

双向 `GET_PROTOCOL` 和 `SET_PROTOCOL` 都携带相同取值，因此设备（Device）与主机（Host）角色共用这些值。

<a id="r_gac9f6cb6981d548e3db9e6a0a99bc6fc9"></a>

```c
#define BT_HID_PROTOCOL_BOOT_MODE 0x00U
```

相关声明：[BT_HID_PROTOCOL_BOOT_MODE](../api_power_policy_topic_reference/P003_蓝牙人机接口设备（Bluetooth HID）.md#gac9f6cb6981d548e3db9e6a0a99bc6fc9)。

引导协议模式（Boot Protocol Mode），旧式模式（Legacy）。

<a id="r_gad4f973c2bdd628e0d6b09884a83219c7"></a>

```c
#define BT_HID_PROTOCOL_REPORT_MODE 0x01U
```

相关声明：[BT_HID_PROTOCOL_REPORT_MODE](../api_power_policy_topic_reference/P003_蓝牙人机接口设备（Bluetooth HID）.md#gad4f973c2bdd628e0d6b09884a83219c7)。

报告协议模式（Report Protocol Mode），默认模式（Default）。

<a id="define-members-1"></a>

### HID 报告类型值（Report Type Values）

`GET_REPORT`、`SET_REPORT` 和 `DATA` 传输携带的报告类型（Report Type）。

定义于 HID v1.1.2 规范表 3.4。

<a id="r_ga70b5259d0204510cd225b3de6c3d0361"></a>

```c
#define BT_HID_REPORT_TYPE_OTHER 0x00U
```

相关声明：[BT_HID_REPORT_TYPE_OTHER](../api_power_policy_topic_reference/P003_蓝牙人机接口设备（Bluetooth HID）.md#ga70b5259d0204510cd225b3de6c3d0361)。

保留报告类型（Reserved Report Type），用于不适用任何类型的场合。

<a id="r_gafb92c081d13c6084fbd51a3df28b42dc"></a>

```c
#define BT_HID_REPORT_TYPE_INPUT 0x01U
```

相关声明：[BT_HID_REPORT_TYPE_INPUT](../api_power_policy_topic_reference/P003_蓝牙人机接口设备（Bluetooth HID）.md#gafb92c081d13c6084fbd51a3df28b42dc)。

输入报告（Input Report），从设备到主机。

<a id="r_gadfca183266ec397319b3242bbcea6c3e"></a>

```c
#define BT_HID_REPORT_TYPE_OUTPUT 0x02U
```

相关声明：[BT_HID_REPORT_TYPE_OUTPUT](../api_power_policy_topic_reference/P003_蓝牙人机接口设备（Bluetooth HID）.md#gadfca183266ec397319b3242bbcea6c3e)。

输出报告（Output Report），从主机到设备。

<a id="r_gac4cab3c0de498e45609c945780386353"></a>

```c
#define BT_HID_REPORT_TYPE_FEATURE 0x03U
```

相关声明：[BT_HID_REPORT_TYPE_FEATURE](../api_power_policy_topic_reference/P003_蓝牙人机接口设备（Bluetooth HID）.md#gac4cab3c0de498e45609c945780386353)。

特性报告（Feature Report）。

<a id="define-members-2"></a>

### HID 握手结果码（HANDSHAKE Result Codes）

控制通道（Control Channel）上所发请求的结果（Result）。

定义于 HID v1.1.2 规范 3.1.2.1 节。主机（Host）将这些结果报告给应用，设备（Device）使用它们作答，因此两种角色共用这些值。

<a id="r_ga19706f1a5e6fa8e112a3610aa8e8821f"></a>

```c
#define BT_HID_HS_RSP_SUCCESS 0x00U
```

相关声明：[BT_HID_HS_RSP_SUCCESS](../api_power_policy_topic_reference/P003_蓝牙人机接口设备（Bluetooth HID）.md#ga19706f1a5e6fa8e112a3610aa8e8821f)。

请求已成功完成（Completed Successfully）。

<a id="r_gae156f477153c8aac8bd033b5c695183f"></a>

```c
#define BT_HID_HS_RSP_NOT_READY 0x01U
```

相关声明：[BT_HID_HS_RSP_NOT_READY](../api_power_policy_topic_reference/P003_蓝牙人机接口设备（Bluetooth HID）.md#gae156f477153c8aac8bd033b5c695183f)。

对端（Peer）过忙，无法接受请求；发送方可以重试。

<a id="r_ga5907f25b03338cd30fe5595fd90fcfb3"></a>

```c
#define BT_HID_HS_RSP_ERR_INVALID_REPORT_ID 0x02U
```

相关声明：[BT_HID_HS_RSP_ERR_INVALID_REPORT_ID](../api_power_policy_topic_reference/P003_蓝牙人机接口设备（Bluetooth HID）.md#ga5907f25b03338cd30fe5595fd90fcfb3)。

请求引用了不支持的报告 ID（Report ID）。

<a id="r_ga5f50003a9615d2183a577cf99cc295b9"></a>

```c
#define BT_HID_HS_RSP_ERR_UNSUPPORTED_REQ 0x03U
```

相关声明：[BT_HID_HS_RSP_ERR_UNSUPPORTED_REQ](../api_power_policy_topic_reference/P003_蓝牙人机接口设备（Bluetooth HID）.md#ga5f50003a9615d2183a577cf99cc295b9)。

对端（Peer）不支持此请求。

<a id="r_ga2703efb41d6834e2681bba09b6cce648"></a>

```c
#define BT_HID_HS_RSP_ERR_INVALID_PARAM 0x04U
```

相关声明：[BT_HID_HS_RSP_ERR_INVALID_PARAM](../api_power_policy_topic_reference/P003_蓝牙人机接口设备（Bluetooth HID）.md#ga2703efb41d6834e2681bba09b6cce648)。

请求携带无效参数（Invalid Parameter）。

<a id="r_ga46ab8c7af038b5fb8e2e6baa0032f4d9"></a>

```c
#define BT_HID_HS_RSP_ERR_UNKNOWN 0x0eU
```

相关声明：[BT_HID_HS_RSP_ERR_UNKNOWN](../api_power_policy_topic_reference/P003_蓝牙人机接口设备（Bluetooth HID）.md#ga46ab8c7af038b5fb8e2e6baa0032f4d9)。

对端（Peer）无法确定错误情况（Error Condition）。

<a id="r_ga29aaf9e0914f0226d2ac741c32cdfe3b"></a>

```c
#define BT_HID_HS_RSP_ERR_FATAL 0x0fU
```

相关声明：[BT_HID_HS_RSP_ERR_FATAL](../api_power_policy_topic_reference/P003_蓝牙人机接口设备（Bluetooth HID）.md#ga29aaf9e0914f0226d2ac741c32cdfe3b)。

对端（Peer）遇到致命错误（Fatal Error），需要重启。


## 1.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P070_hid.h_源码浏览.md)
- [BT_HID_PROTOCOL_BOOT_MODE](../api_power_policy_topic_reference/P003_蓝牙人机接口设备（Bluetooth HID）.md#gac9f6cb6981d548e3db9e6a0a99bc6fc9)
- [BT_HID_PROTOCOL_REPORT_MODE](../api_power_policy_topic_reference/P003_蓝牙人机接口设备（Bluetooth HID）.md#gad4f973c2bdd628e0d6b09884a83219c7)
- [BT_HID_REPORT_TYPE_OTHER](../api_power_policy_topic_reference/P003_蓝牙人机接口设备（Bluetooth HID）.md#ga70b5259d0204510cd225b3de6c3d0361)
- [BT_HID_REPORT_TYPE_INPUT](../api_power_policy_topic_reference/P003_蓝牙人机接口设备（Bluetooth HID）.md#gafb92c081d13c6084fbd51a3df28b42dc)
- [BT_HID_REPORT_TYPE_OUTPUT](../api_power_policy_topic_reference/P003_蓝牙人机接口设备（Bluetooth HID）.md#gadfca183266ec397319b3242bbcea6c3e)
- [BT_HID_REPORT_TYPE_FEATURE](../api_power_policy_topic_reference/P003_蓝牙人机接口设备（Bluetooth HID）.md#gac4cab3c0de498e45609c945780386353)
- [BT_HID_HS_RSP_SUCCESS](../api_power_policy_topic_reference/P003_蓝牙人机接口设备（Bluetooth HID）.md#ga19706f1a5e6fa8e112a3610aa8e8821f)
- [BT_HID_HS_RSP_NOT_READY](../api_power_policy_topic_reference/P003_蓝牙人机接口设备（Bluetooth HID）.md#gae156f477153c8aac8bd033b5c695183f)
- [BT_HID_HS_RSP_ERR_INVALID_REPORT_ID](../api_power_policy_topic_reference/P003_蓝牙人机接口设备（Bluetooth HID）.md#ga5907f25b03338cd30fe5595fd90fcfb3)
- [BT_HID_HS_RSP_ERR_UNSUPPORTED_REQ](../api_power_policy_topic_reference/P003_蓝牙人机接口设备（Bluetooth HID）.md#ga5f50003a9615d2183a577cf99cc295b9)
- [BT_HID_HS_RSP_ERR_INVALID_PARAM](../api_power_policy_topic_reference/P003_蓝牙人机接口设备（Bluetooth HID）.md#ga2703efb41d6834e2681bba09b6cce648)
- [BT_HID_HS_RSP_ERR_UNKNOWN](../api_power_policy_topic_reference/P003_蓝牙人机接口设备（Bluetooth HID）.md#ga46ab8c7af038b5fb8e2e6baa0032f4d9)
- [BT_HID_HS_RSP_ERR_FATAL](../api_power_policy_topic_reference/P003_蓝牙人机接口设备（Bluetooth HID）.md#ga29aaf9e0914f0226d2ac741c32cdfe3b)

<a id="header-details"></a>

---

[返回大纲](大纲.md) · [下一章](P002_zephyr__drivers__can__can_fake.h_文件参考.md)
