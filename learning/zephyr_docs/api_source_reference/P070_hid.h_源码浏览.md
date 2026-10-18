---
id: learning.zephyr-docs.api-source-reference.page-70
title: hid.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2classic_2hid_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第70章\_hid.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2classic_2hid_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2classic_2hid_8h.html)。

## 70.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00069"></a>
<a id="l00071"></a>
<a id="l00073"></a>
<a id="l00075"></a>
<a id="l00077"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00087"></a>
<a id="l00088"></a>

```c


/*
 * Copyright 2026 Xiaomi Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_HID_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_HID_H_


#ifdef __cplusplus
extern "C" {
#endif

#define BT_HID_PROTOCOL_BOOT_MODE   0x00U
#define BT_HID_PROTOCOL_REPORT_MODE 0x01U

#define BT_HID_REPORT_TYPE_OTHER   0x00U
#define BT_HID_REPORT_TYPE_INPUT   0x01U
#define BT_HID_REPORT_TYPE_OUTPUT  0x02U
#define BT_HID_REPORT_TYPE_FEATURE 0x03U

#define BT_HID_HS_RSP_SUCCESS               0x00U
#define BT_HID_HS_RSP_NOT_READY             0x01U
#define BT_HID_HS_RSP_ERR_INVALID_REPORT_ID 0x02U
#define BT_HID_HS_RSP_ERR_UNSUPPORTED_REQ   0x03U
#define BT_HID_HS_RSP_ERR_INVALID_PARAM     0x04U
#define BT_HID_HS_RSP_ERR_UNKNOWN           0x0eU
#define BT_HID_HS_RSP_ERR_FATAL             0x0fU

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_HID_H_ */
```

## 70.2\_可见注释译文（Comments）

### 注释 1：原第 5 行

版权（Copyright）：2026 Xiaomi Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 88 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_HID_H_`。

## 70.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2classic_2hid_8h.html)

---

[上一章](P069_cap.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P071_controller.h_源码浏览.md)
