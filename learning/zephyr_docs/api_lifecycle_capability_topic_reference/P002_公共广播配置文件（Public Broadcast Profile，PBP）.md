---
id: learning.zephyr-docs.api-lifecycle-capability-topic-reference.page-2
title: 公共广播配置文件（Public Broadcast Profile，PBP）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_公共广播配置文件（Public Broadcast Profile，PBP）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbp.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

公共广播配置文件（Public Broadcast Profile，PBP）

<a id="details"></a>

公共广播配置文件（Public Broadcast Profile，PBP）。**引入版本（Since）：**3.5。**版本（Version）：**0.8.0。PBP 在广播数据（Advertising Data）中提供附加信息，用于公共广播（Public Broadcast）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 2.1\_宏定义（Macros）

<a id="r_ga5a334cfc19404a9d9f361b3b2424051a"></a>

```c
#define BT_PBP_MIN_PBA_SIZE (BT_UUID_SIZE_16 + 1 + 1)
```

相关声明：[BT_PBP_MIN_PBA_SIZE](#ga5a334cfc19404a9d9f361b3b2424051a)、[BT_UUID_SIZE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9d3506fd135b5cd8763446f572c161da)。

公共广播公告（Public Broadcast Announcement）的最小大小（Minimum Size）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 2.2\_枚举（Enumerations）

<a id="r_ga2685c082fb56bfece540c9f43bf5ba47"></a>

```c
enum bt_pbp_announcement_feature { BT_PBP_ANNOUNCEMENT_FEATURE_ENCRYPTION = (1UL << (0U)) , BT_PBP_ANNOUNCEMENT_FEATURE_STANDARD_QUALITY = (1UL << (1U)) , BT_PBP_ANNOUNCEMENT_FEATURE_HIGH_QUALITY = (1UL << (2U)) }
```

相关声明：[bt_pbp_announcement_feature](#ga2685c082fb56bfece540c9f43bf5ba47)、[BT_PBP_ANNOUNCEMENT_FEATURE_ENCRYPTION](#gga2685c082fb56bfece540c9f43bf5ba47aeda548305ece142429bfa97fd9f612df)、[BT_PBP_ANNOUNCEMENT_FEATURE_STANDARD_QUALITY](#gga2685c082fb56bfece540c9f43bf5ba47a20aff6780e8f5ec5aaf0ea5500331638)、[BT_PBP_ANNOUNCEMENT_FEATURE_HIGH_QUALITY](#gga2685c082fb56bfece540c9f43bf5ba47a6d059892e294eec6a097d8e2813a352e)。

公共广播公告特性（Public Broadcast Announcement Features）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 2.3\_函数（Functions）

<a id="r_gaa496ac2a3ec9dd5fc013a1f4a804b11b"></a>

```c
int bt_pbp_get_announcement (const uint8_t meta[], size_t meta_len, enum bt_pbp_announcement_feature features, struct net_buf_simple *pba_data_buf)
```

相关声明：[bt_pbp_get_announcement](#gaa496ac2a3ec9dd5fc013a1f4a804b11b)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_pbp_announcement_feature](#ga2685c082fb56bfece540c9f43bf5ba47)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

根据 `features` 参数中收到的信息，创建公共广播公告（Public Broadcast Announcement）。

<a id="r_ga311b1fdb0a2aa24a09e8d3b3566693ff"></a>

```c
int bt_pbp_parse_announcement (struct bt_data *data, enum bt_pbp_announcement_feature *features, uint8_t **meta)
```

相关声明：[bt_pbp_parse_announcement](#ga311b1fdb0a2aa24a09e8d3b3566693ff)、[bt_data](../bluetooth_connection_model_reference/P041_bt_data_结构体.md)、[bt_pbp_announcement_feature](#ga2685c082fb56bfece540c9f43bf5ba47)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

解析收到的、对应于公共广播公告（Public Broadcast Announcement）的广播数据（Advertising Data）。

## 2.4\_详细说明（Detailed Documentation）

<a id="ga5a334cfc19404a9d9f361b3b2424051a"></a>

### `BT_PBP_MIN_PBA_SIZE`

```c
#define BT_PBP_MIN_PBA_SIZE (BT_UUID_SIZE_16 + 1 + 1)
```

```c
#include <zephyr/bluetooth/audio/pbp.h>
```

公共广播公告（Public Broadcast Announcement）的最小大小（Minimum Size）。

它包含公共广播公告（Public Broadcast Announcement）的 UUID（2）、特性（Features，1）和元数据长度（Metadata Length，1）。

<a id="ga2685c082fb56bfece540c9f43bf5ba47"></a>

### `bt_pbp_announcement_feature`

```c
enum bt_pbp_announcement_feature
```

```c
#include <zephyr/bluetooth/audio/pbp.h>
```

公共广播公告特性（Public Broadcast Announcement Features）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_PBP_ANNOUNCEMENT_FEATURE_ENCRYPTION` | 广播流加密状态（Broadcast Streams Encryption Status）。 |
| `BT_PBP_ANNOUNCEMENT_FEATURE_STANDARD_QUALITY` | 标准质量公共广播音频配置（Standard Quality Public Broadcast Audio Configuration）。 |
| `BT_PBP_ANNOUNCEMENT_FEATURE_HIGH_QUALITY` | 高质量公共广播音频配置（High Quality Public Broadcast Audio Configuration）。 |

<a id="gaa496ac2a3ec9dd5fc013a1f4a804b11b"></a>

### `bt_pbp_get_announcement()`

```c
int bt_pbp_get_announcement ( const uint8_t meta[], size_t meta_len, enum bt_pbp_announcement_feature features, struct net_buf_simple * pba_data_buf )
```

```c
#include <zephyr/bluetooth/audio/pbp.h>
```

根据 `features` 参数中收到的信息，创建公共广播公告（Public Broadcast Announcement）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `meta` | 要包含在广播数据（Advertising Data）中的元数据（Metadata）。 |
| `meta_len` | 要包含在广播数据（Advertising Data）中的元数据字段大小（Metadata Fields Size）。 |
| `features` | 公共广播公告特性（Public Broadcast Announcement Features）。 |
| `pba_data_buf` | 用于存储公共广播公告（PBA）广播数据的指针。缓冲区大小必须为 `meta_len + BT_PBP_MIN_PBA_SIZE`。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，否则返回适当的错误码（Error Code）。

<a id="ga311b1fdb0a2aa24a09e8d3b3566693ff"></a>

### `bt_pbp_parse_announcement()`

```c
int bt_pbp_parse_announcement ( struct bt_data * data, enum bt_pbp_announcement_feature * features, uint8_t ** meta )
```

```c
#include <zephyr/bluetooth/audio/pbp.h>
```

解析收到的、对应于公共广播公告（Public Broadcast Announcement）的广播数据（Advertising Data）。

返回广播中的公共广播公告（Public Broadcast Announcement）特性和元数据（Features and Metadata）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] data` | 要检查的广播数据（Advertising Data）。 |
| `[out] features` | 指向公共广播源特性（Public Broadcast Source Features）的指针，用于存储解析得到的特性。 |
| `[out] meta` | 指向广播数据（Advertising Data）中元数据（Metadata）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | `data`、`features` 或 `meta` 为 `NULL` 时。 |
| `-ENOENT` | `data` 的类型不是 `BT_DATA_SVC_DATA16`，或服务数据中的 UUID 不是 `BT_UUID_PBA` 时。 |
| `-EMSGSIZE` | `data` 长度不足以容纳 PBP 公告（Announcement）时。 |
| `-EBADMSG` | `data` 包含无效数据（Invalid Data）时。 |

**返回（Returns）**：**返回值（Returns）：**成功时返回解析得到的元数据长度（Metadata Length）。


## 2.5\_原页交叉引用（Cross References）

- [BT_UUID_SIZE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga9d3506fd135b5cd8763446f572c161da)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)
- [bt_data](../bluetooth_connection_model_reference/P041_bt_data_结构体.md)
- [zephyr/bluetooth/audio/pbp.h](../api_file_service_reference/P035_zephyr__bluetooth__audio__pbp.h_文件参考.md)
- [BT_DATA_SVC_DATA16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga76990dda919688b369decaf9d3606b32)
- [BT_UUID_PBA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html#ga98f4f946c1bca483a7e81cad162ee0b1)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga2685c082fb56bfece540c9f43bf5ba47aeda548305ece142429bfa97fd9f612df"></a>
<a id="gga2685c082fb56bfece540c9f43bf5ba47a20aff6780e8f5ec5aaf0ea5500331638"></a>
<a id="gga2685c082fb56bfece540c9f43bf5ba47a6d059892e294eec6a097d8e2813a352e"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P001_APDS9253 API主题.md) · [返回大纲](大纲.md) · [下一章](P003_HTTP客户端（Client）API。.md)
