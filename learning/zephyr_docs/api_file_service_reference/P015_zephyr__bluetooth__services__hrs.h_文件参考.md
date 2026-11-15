---
id: learning.zephyr-docs.api-file-service-reference.page-15
title: zephyr__bluetooth__services__hrs.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/hrs_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_zephyr\_\_bluetooth\_\_services\_\_hrs.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/hrs_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <stdint.h>
#include <zephyr/sys/slist.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 15.1\_数据结构（Data Structures）

<a id="r_bt_5Fhrs_5Fcb"></a>

```c
struct bt_hrs_cb
```

相关声明：[bt_hrs_cb](../bluetooth_service_model_reference/P093_bt_hrs_cb_结构体.md)。

心率服务（Heart Rate Service）的回调结构。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 15.2\_宏定义（Macros）

<a id="r_ga4ff20fff68b19602a8857d29f8dd822d"></a>

```c
#define BT_HRS_CONTROL_POINT_RESET_ENERGY_EXPANDED_REQ 0x01
```

相关声明：[BT_HRS_CONTROL_POINT_RESET_ENERGY_EXPANDED_REQ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hrs.html#ga4ff20fff68b19602a8857d29f8dd822d)。

服务器（Server）应从零开始重新累计能量消耗（Energy Expended）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 15.3\_函数（Functions）

<a id="r_ga4b250a12dc6e975589f21ca1391c5b38"></a>

```c
int bt_hrs_cb_register (struct bt_hrs_cb *cb)
```

相关声明：[bt_hrs_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hrs.html#ga4b250a12dc6e975589f21ca1391c5b38)、[bt_hrs_cb](../bluetooth_service_model_reference/P093_bt_hrs_cb_结构体.md)。

注册心率服务回调（Heart Rate Service Callback）。

<a id="r_gad725bf460319ca796c166a5f91e38bb6"></a>

```c
int bt_hrs_cb_unregister (struct bt_hrs_cb *cb)
```

相关声明：[bt_hrs_cb_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hrs.html#gad725bf460319ca796c166a5f91e38bb6)、[bt_hrs_cb](../bluetooth_service_model_reference/P093_bt_hrs_cb_结构体.md)。

注销心率服务回调（Heart Rate Service Callback）。

<a id="r_ga0e3d298d984e2504957ca655f142e45b"></a>

```c
int bt_hrs_notify (uint16_t heartrate)
```

相关声明：[bt_hrs_notify](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hrs.html#ga0e3d298d984e2504957ca655f142e45b)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

通知心率测量值（Heart Rate Measurement）。


## 15.4\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/sys/slist.h](../slist_reference/P003_单向链表头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P323_hrs.h_源码浏览.md)
- [bt_hrs_cb](../bluetooth_service_model_reference/P093_bt_hrs_cb_结构体.md)
- [BT_HRS_CONTROL_POINT_RESET_ENERGY_EXPANDED_REQ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hrs.html#ga4ff20fff68b19602a8857d29f8dd822d)
- [bt_hrs_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hrs.html#ga4b250a12dc6e975589f21ca1391c5b38)
- [bt_hrs_cb_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hrs.html#gad725bf460319ca796c166a5f91e38bb6)
- [bt_hrs_notify](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hrs.html#ga0e3d298d984e2504957ca655f142e45b)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)

---

[上一章](P014_zephyr__drivers__misc__ft8xx__ft8xx_memory.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P016_zephyr__input__input_nunchuk.h_文件参考.md)
