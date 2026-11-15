---
id: learning.zephyr-docs.api-file-service-reference.page-35
title: zephyr__bluetooth__audio__pbp.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pbp_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第35章\_zephyr\_\_bluetooth\_\_audio\_\_pbp.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/pbp_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

公共广播配置文件（Public Broadcast Profile，PBP）的API。

<a id="details"></a>

```c
#include <stddef.h>
#include <stdint.h>
#include <zephyr/bluetooth/audio/audio.h>
#include <zephyr/bluetooth/bluetooth.h>
#include <zephyr/bluetooth/data.h>
#include <zephyr/bluetooth/uuid.h>
#include <zephyr/net_buf.h>
#include <zephyr/sys/util.h>
#include <zephyr/sys/util_macro.h>
```

查看此文件的源码。

公共广播配置文件（Public Broadcast Profile，PBP）的API。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 35.1\_宏定义（Macros）

<a id="r_ga5a334cfc19404a9d9f361b3b2424051a"></a>

```c
#define BT_PBP_MIN_PBA_SIZE (BT_UUID_SIZE_16 + 1 + 1)
```

相关声明：[BT_PBP_MIN_PBA_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbp.html#ga5a334cfc19404a9d9f361b3b2424051a)、[BT_UUID_SIZE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9d3506fd135b5cd8763446f572c161da)。

公共广播公告（Public Broadcast Announcement）的最小大小（Minimum Size）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 35.2\_枚举（Enumerations）

<a id="r_ga2685c082fb56bfece540c9f43bf5ba47"></a>

```c
enum bt_pbp_announcement_feature { BT_PBP_ANNOUNCEMENT_FEATURE_ENCRYPTION = (1UL << (0U)) , BT_PBP_ANNOUNCEMENT_FEATURE_STANDARD_QUALITY = (1UL << (1U)) , BT_PBP_ANNOUNCEMENT_FEATURE_HIGH_QUALITY = (1UL << (2U)) }
```

相关声明：[bt_pbp_announcement_feature](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbp.html#ga2685c082fb56bfece540c9f43bf5ba47)、[BT_PBP_ANNOUNCEMENT_FEATURE_ENCRYPTION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbp.html#gga2685c082fb56bfece540c9f43bf5ba47aeda548305ece142429bfa97fd9f612df)、[BT_PBP_ANNOUNCEMENT_FEATURE_STANDARD_QUALITY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbp.html#gga2685c082fb56bfece540c9f43bf5ba47a20aff6780e8f5ec5aaf0ea5500331638)、[BT_PBP_ANNOUNCEMENT_FEATURE_HIGH_QUALITY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbp.html#gga2685c082fb56bfece540c9f43bf5ba47a6d059892e294eec6a097d8e2813a352e)。

公共广播公告特性（Public Broadcast Announcement Features）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 35.3\_函数（Functions）

<a id="r_gaa496ac2a3ec9dd5fc013a1f4a804b11b"></a>

```c
int bt_pbp_get_announcement (const uint8_t meta[], size_t meta_len, enum bt_pbp_announcement_feature features, struct net_buf_simple *pba_data_buf)
```

相关声明：[bt_pbp_get_announcement](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbp.html#gaa496ac2a3ec9dd5fc013a1f4a804b11b)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_pbp_announcement_feature](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbp.html#ga2685c082fb56bfece540c9f43bf5ba47)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

根据 `features` 参数中收到的信息，创建公共广播公告（Public Broadcast Announcement）。

<a id="r_ga311b1fdb0a2aa24a09e8d3b3566693ff"></a>

```c
int bt_pbp_parse_announcement (struct bt_data *data, enum bt_pbp_announcement_feature *features, uint8_t **meta)
```

相关声明：[bt_pbp_parse_announcement](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbp.html#ga311b1fdb0a2aa24a09e8d3b3566693ff)、[bt_data](../bluetooth_connection_model_reference/P041_bt_data_结构体.md)、[bt_pbp_announcement_feature](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbp.html#ga2685c082fb56bfece540c9f43bf5ba47)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

解析收到的、对应于公共广播公告（Public Broadcast Announcement）的广播数据（Advertising Data）。


## 35.4\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/bluetooth/audio/audio.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2audio_8h_source.html)
- [zephyr/bluetooth/bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h_source.html)
- [zephyr/bluetooth/data.h](../api_source_reference/P121_data.h_源码浏览.md)
- [zephyr/bluetooth/uuid.h](../api_source_supplement_reference/P020_uuid.h_源码浏览.md)
- [zephyr/net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h_source.html)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [zephyr/sys/util_macro.h](../util_reference/P005_宏工具头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P645_pbp.h_源码浏览.md)
- [BT_PBP_MIN_PBA_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbp.html#ga5a334cfc19404a9d9f361b3b2424051a)
- [BT_UUID_SIZE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9d3506fd135b5cd8763446f572c161da)
- [bt_pbp_announcement_feature](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbp.html#ga2685c082fb56bfece540c9f43bf5ba47)
- [BT_PBP_ANNOUNCEMENT_FEATURE_ENCRYPTION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbp.html#gga2685c082fb56bfece540c9f43bf5ba47aeda548305ece142429bfa97fd9f612df)
- [BT_PBP_ANNOUNCEMENT_FEATURE_STANDARD_QUALITY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbp.html#gga2685c082fb56bfece540c9f43bf5ba47a20aff6780e8f5ec5aaf0ea5500331638)
- [BT_PBP_ANNOUNCEMENT_FEATURE_HIGH_QUALITY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbp.html#gga2685c082fb56bfece540c9f43bf5ba47a6d059892e294eec6a097d8e2813a352e)
- [bt_pbp_get_announcement](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbp.html#gaa496ac2a3ec9dd5fc013a1f4a804b11b)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)
- [bt_pbp_parse_announcement](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbp.html#ga311b1fdb0a2aa24a09e8d3b3566693ff)
- [bt_data](../bluetooth_connection_model_reference/P041_bt_data_结构体.md)

<a id="header-details"></a>

---

[上一章](P034_zephyr__drivers__otp.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P036_zephyr__drivers__regulator__pca9420.h_文件参考.md)
