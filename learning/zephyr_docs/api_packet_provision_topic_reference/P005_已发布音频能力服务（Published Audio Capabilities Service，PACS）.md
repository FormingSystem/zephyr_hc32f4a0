---
id: learning.zephyr-docs.api-packet-provision-topic-reference.page-5
title: 已发布音频能力服务（Published Audio Capabilities Service，PACS）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pacs.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_已发布音频能力服务（Published Audio Capabilities Service，PACS）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pacs.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

已发布音频能力服务（Published Audio Capabilities Service，PACS）

<a id="details"></a>

已发布音频能力服务（Published Audio Capabilities Service，PACS）。自 3.0 起提供，版本 0.8.0。PACS 用于向远端设备公开能力（Capabilities）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 5.1\_数据结构（Data Structures）

<a id="r_bt_5Fpacs_5Fcap"></a>

```c
struct bt_pacs_cap
```

相关声明：[bt_pacs_cap](../bluetooth_service_model_reference/P147_bt_pacs_cap_结构体.md)。

已发布音频能力（Published Audio Capability）结构。

<a id="r_bt_5Fpacs_5Fregister_5Fparam"></a>

```c
struct bt_pacs_register_param
```

相关声明：[bt_pacs_register_param](../bluetooth_service_model_reference/P148_bt_pacs_register_param_结构体.md)。

用于注册已发布音频能力服务（PACS）的结构。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 5.2\_类型定义（Typedefs）

<a id="r_ga452591f80b6be5d79609b25ade2154a9"></a>

```c
typedef bool(* bt_pacs_cap_foreach_func_t) (const struct bt_pacs_cap *cap, void *user_data)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_pacs_cap_foreach_func_t](#ga452591f80b6be5d79609b25ade2154a9)、[bt_pacs_cap](../bluetooth_service_model_reference/P147_bt_pacs_cap_结构体.md)。

已发布音频能力（Published Audio Capability）迭代器回调（Iterator Callback）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 5.3\_函数（Functions）

<a id="r_ga31e2c7e9a4b5b6a291b96832c1218a49"></a>

```c
void bt_pacs_cap_foreach (enum bt_audio_dir dir, bt_pacs_cap_foreach_func_t func, void *user_data)
```

相关声明：[bt_pacs_cap_foreach](#ga31e2c7e9a4b5b6a291b96832c1218a49)、[bt_audio_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#ga5bd899fb5e4d844058184913866e462f)、[bt_pacs_cap_foreach_func_t](#ga452591f80b6be5d79609b25ade2154a9)。

已发布音频能力（Published Audio Capability）迭代器（Iterator）。

<a id="r_gac77a3dd5015058145b51db5fef2c9485"></a>

```c
int bt_pacs_register (const struct bt_pacs_register_param *param)
```

相关声明：[bt_pacs_register](#gac77a3dd5015058145b51db5fef2c9485)、[bt_pacs_register_param](../bluetooth_service_model_reference/P148_bt_pacs_register_param_结构体.md)。

注册已发布音频能力服务（Published Audio Capability Service）实例。

<a id="r_gac23d3c4e850394194871e8daaa44545b"></a>

```c
int bt_pacs_unregister (void)
```

相关声明：[bt_pacs_unregister](#gac23d3c4e850394194871e8daaa44545b)。

注销已发布音频能力服务（Published Audio Capability Service）实例。

<a id="r_ga251b36d4f5775eea1f69873709f847cc"></a>

```c
int bt_pacs_cap_register (enum bt_audio_dir dir, struct bt_pacs_cap *cap)
```

相关声明：[bt_pacs_cap_register](#ga251b36d4f5775eea1f69873709f847cc)、[bt_audio_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#ga5bd899fb5e4d844058184913866e462f)、[bt_pacs_cap](../bluetooth_service_model_reference/P147_bt_pacs_cap_结构体.md)。

注册已发布音频能力（Published Audio Capability）。

<a id="r_ga4f6015eba63ffc7a9377afe54a290da1"></a>

```c
int bt_pacs_cap_unregister (enum bt_audio_dir dir, struct bt_pacs_cap *cap)
```

相关声明：[bt_pacs_cap_unregister](#ga4f6015eba63ffc7a9377afe54a290da1)、[bt_audio_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#ga5bd899fb5e4d844058184913866e462f)、[bt_pacs_cap](../bluetooth_service_model_reference/P147_bt_pacs_cap_结构体.md)。

注销已发布音频能力（Published Audio Capability）。

<a id="r_gaff290fd59bb05012abcf405dbdc72884"></a>

```c
int bt_pacs_set_location (enum bt_audio_dir dir, enum bt_audio_location location)
```

相关声明：[bt_pacs_set_location](#gaff290fd59bb05012abcf405dbdc72884)、[bt_audio_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#ga5bd899fb5e4d844058184913866e462f)、[bt_audio_location](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga61230848c02098352320fe751332c4e8)。

设置某个端点类型（Endpoint Type）的位置（Location）。

<a id="r_ga29a1ec26c1e5e82e02eac39e1088332c"></a>

```c
int bt_pacs_set_available_contexts (enum bt_audio_dir dir, enum bt_audio_context contexts)
```

相关声明：[bt_pacs_set_available_contexts](#ga29a1ec26c1e5e82e02eac39e1088332c)、[bt_audio_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#ga5bd899fb5e4d844058184913866e462f)、[bt_audio_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gafb379ffa88388cc1397960155bbb2ab3)。

设置某个端点类型（Endpoint Type）的可用上下文（Available Contexts）。

<a id="r_ga437d824d0a944b6c30db492dbe28514f"></a>

```c
enum bt_audio_context bt_pacs_get_available_contexts (enum bt_audio_dir dir)
```

相关声明：[bt_audio_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gafb379ffa88388cc1397960155bbb2ab3)、[bt_pacs_get_available_contexts](#ga437d824d0a944b6c30db492dbe28514f)、[bt_audio_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#ga5bd899fb5e4d844058184913866e462f)。

获取某个端点类型（Endpoint Type）的可用上下文（Available Contexts）。

<a id="r_ga12f283d2daf72302a01cefb4a4a8fc70"></a>

```c
int bt_pacs_conn_set_available_contexts_for_conn (struct bt_conn *conn, enum bt_audio_dir dir, enum bt_audio_context *contexts)
```

相关声明：[bt_pacs_conn_set_available_contexts_for_conn](#ga12f283d2daf72302a01cefb4a4a8fc70)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_audio_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#ga5bd899fb5e4d844058184913866e462f)、[bt_audio_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gafb379ffa88388cc1397960155bbb2ab3)。

设置给定连接（Connection）的可用上下文（Available Contexts）。

<a id="r_ga7b28aa42525344445b20bb90a19441aa"></a>

```c
enum bt_audio_context bt_pacs_get_available_contexts_for_conn (struct bt_conn *conn, enum bt_audio_dir dir)
```

相关声明：[bt_audio_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gafb379ffa88388cc1397960155bbb2ab3)、[bt_pacs_get_available_contexts_for_conn](#ga7b28aa42525344445b20bb90a19441aa)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_audio_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#ga5bd899fb5e4d844058184913866e462f)。

获取给定连接（Connection）的可用上下文（Available Contexts）。

<a id="r_gabae9cf025f32ce80b660ebd7f95241b2"></a>

```c
int bt_pacs_set_supported_contexts (enum bt_audio_dir dir, enum bt_audio_context contexts)
```

相关声明：[bt_pacs_set_supported_contexts](#gabae9cf025f32ce80b660ebd7f95241b2)、[bt_audio_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#ga5bd899fb5e4d844058184913866e462f)、[bt_audio_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gafb379ffa88388cc1397960155bbb2ab3)。

设置某个端点类型（Endpoint Type）支持的上下文（Supported Contexts）。

## 5.4\_详细说明（Detailed Documentation）

<a id="ga452591f80b6be5d79609b25ade2154a9"></a>

### `bt_pacs_cap_foreach_func_t`

```c
typedef bool(* bt_pacs_cap_foreach_func_t) (const struct bt_pacs_cap *cap, void *user_data)
```

```c
#include <zephyr/bluetooth/audio/pacs.h>
```

已发布音频能力（Published Audio Capability）迭代器回调（Iterator Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cap` | 找到的能力（Capability）。 |
| `user_data` | 所给数据（Data）。 |

**返回（Returns）**：返回值：返回 `true` 继续遍历下一项能力，返回 `false` 停止遍历。

<a id="ga31e2c7e9a4b5b6a291b96832c1218a49"></a>

### `bt_pacs_cap_foreach()`

```c
void bt_pacs_cap_foreach ( enum bt_audio_dir dir, bt_pacs_cap_foreach_func_t func, void * user_data )
```

```c
#include <zephyr/bluetooth/audio/pacs.h>
```

已发布音频能力（Published Audio Capability）迭代器（Iterator）。

按指定端点方向（Endpoint Direction）遍历能力。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dir` | 要查找其能力的端点方向（Endpoint Direction）。 |
| `func` | 回调函数（Callback function）。 |
| `user_data` | 传给回调（Callback）的数据。 |

<a id="ga251b36d4f5775eea1f69873709f847cc"></a>

### `bt_pacs_cap_register()`

```c
int bt_pacs_cap_register ( enum bt_audio_dir dir, struct bt_pacs_cap * cap )
```

```c
#include <zephyr/bluetooth/audio/pacs.h>
```

注册已发布音频能力（Published Audio Capability）。

注册音频本地能力（Audio Local Capability）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dir` | 要注册能力的端点方向（Endpoint Direction）。 |
| `cap` | 能力结构体（Capability Structure）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga4f6015eba63ffc7a9377afe54a290da1"></a>

### `bt_pacs_cap_unregister()`

```c
int bt_pacs_cap_unregister ( enum bt_audio_dir dir, struct bt_pacs_cap * cap )
```

```c
#include <zephyr/bluetooth/audio/pacs.h>
```

注销已发布音频能力（Published Audio Capability）。

注销音频本地能力（Audio Local Capability）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dir` | 要注销能力的端点方向（Endpoint Direction）。 |
| `cap` | 能力结构体（Capability Structure）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga12f283d2daf72302a01cefb4a4a8fc70"></a>

### `bt_pacs_conn_set_available_contexts_for_conn()`

```c
int bt_pacs_conn_set_available_contexts_for_conn ( struct bt_conn * conn, enum bt_audio_dir dir, enum bt_audio_context * contexts )
```

```c
#include <zephyr/bluetooth/audio/pacs.h>
```

设置给定连接（Connection）的可用上下文（Available Contexts）。

设置所给 `conn` 连接对象的可用上下文值（Available Contexts Value）。若 `contexts` 参数为 `NULL`，将其重置为默认值。默认可用上下文值通过 `bt_pacs_set_available_contexts` 设置。ACL 连接断开时，可用上下文值会重置为默认值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `dir` | 要更改可用上下文（Available Contexts）的端点方向。 |
| `contexts` | 要设置的上下文（Contexts）；为 `NULL` 时重置为默认值。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga437d824d0a944b6c30db492dbe28514f"></a>

### `bt_pacs_get_available_contexts()`

```c
enum bt_audio_context bt_pacs_get_available_contexts ( enum bt_audio_dir dir)
```

```c
#include <zephyr/bluetooth/audio/pacs.h>
```

获取某个端点类型（Endpoint Type）的可用上下文（Available Contexts）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dir` | 要获取上下文（Contexts）的端点方向。 |

**返回（Returns）**：返回值：可用上下文位掩码（Available Contexts Bitmask）。

<a id="ga7b28aa42525344445b20bb90a19441aa"></a>

### `bt_pacs_get_available_contexts_for_conn()`

```c
enum bt_audio_context bt_pacs_get_available_contexts_for_conn ( struct bt_conn * conn, enum bt_audio_dir dir )
```

```c
#include <zephyr/bluetooth/audio/pacs.h>
```

获取给定连接（Connection）的可用上下文（Available Contexts）。

此服务器函数返回所给 `conn` 连接对象的可用上下文值（Available Contexts Value）。返回值是通过 `bt_pacs_conn_set_available_contexts_for_conn` 设置的值，或者通过 `bt_pacs_set_available_contexts` 设置的默认值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `dir` | 要获取上下文（Contexts）的端点方向。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_AUDIO_CONTEXT_TYPE_NONE` | `conn` 或 `dir` 无效时。 |

**返回（Returns）**：返回值：可用上下文位掩码（Available Contexts Bitmask）。

<a id="gac77a3dd5015058145b51db5fef2c9485"></a>

### `bt_pacs_register()`

```c
int bt_pacs_register ( const struct bt_pacs_register_param * param)
```

```c
#include <zephyr/bluetooth/audio/pacs.h>
```

注册已发布音频能力服务（Published Audio Capability Service）实例。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `param` | PACS 注册参数（Registration Parameters）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | `param` 为 `NULL`，或其中的取值组合不正确。 |
| `-EALREADY` | 已经注册（Already Registered）。 |
| `-ENOEXEC` | 请求被通用属性配置文件（GATT）拒绝。 |

<a id="ga29a1ec26c1e5e82e02eac39e1088332c"></a>

### `bt_pacs_set_available_contexts()`

```c
int bt_pacs_set_available_contexts ( enum bt_audio_dir dir, enum bt_audio_context contexts )
```

```c
#include <zephyr/bluetooth/audio/pacs.h>
```

设置某个端点类型（Endpoint Type）的可用上下文（Available Contexts）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dir` | 要更改可用上下文（Available Contexts）的端点方向。 |
| `contexts` | 要设置的上下文（Contexts）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gaff290fd59bb05012abcf405dbdc72884"></a>

### `bt_pacs_set_location()`

```c
int bt_pacs_set_location ( enum bt_audio_dir dir, enum bt_audio_location location )
```

```c
#include <zephyr/bluetooth/audio/pacs.h>
```

设置某个端点类型（Endpoint Type）的位置（Location）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dir` | 要更改位置（Location）的端点方向。 |
| `location` | 要设置的位置（Location）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gabae9cf025f32ce80b660ebd7f95241b2"></a>

### `bt_pacs_set_supported_contexts()`

```c
int bt_pacs_set_supported_contexts ( enum bt_audio_dir dir, enum bt_audio_context contexts )
```

```c
#include <zephyr/bluetooth/audio/pacs.h>
```

设置某个端点类型（Endpoint Type）支持的上下文（Supported Contexts）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dir` | 要更改可用上下文（Available Contexts）的端点方向。 |
| `contexts` | 要设置的上下文（Contexts）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="gac23d3c4e850394194871e8daaa44545b"></a>

### `bt_pacs_unregister()`

```c
int bt_pacs_unregister ( void )
```

```c
#include <zephyr/bluetooth/audio/pacs.h>
```

注销已发布音频能力服务（Published Audio Capability Service）实例。

**返回（Returns）**：成功返回 0，出错时返回负值。


## 5.5\_原页交叉引用（Cross References）

- [bt_pacs_cap](../bluetooth_service_model_reference/P147_bt_pacs_cap_结构体.md)
- [bt_pacs_register_param](../bluetooth_service_model_reference/P148_bt_pacs_register_param_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [bt_audio_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#ga5bd899fb5e4d844058184913866e462f)
- [bt_audio_location](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga61230848c02098352320fe751332c4e8)
- [bt_audio_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gafb379ffa88388cc1397960155bbb2ab3)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [zephyr/bluetooth/audio/pacs.h](../api_file_system_power_reference/P032_zephyr__bluetooth__audio__pacs.h_文件参考.md)
- [BT_AUDIO_CONTEXT_TYPE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ggafb379ffa88388cc1397960155bbb2ab3a890d2723c8b23127ab4a1cb8b6b1118d)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P004_远程配网客户端模型（Remote Provisioning Client model）.md) · [返回大纲](大纲.md) · [下一章](P006_键盘矩阵（Keyboard Matrix）.md)
