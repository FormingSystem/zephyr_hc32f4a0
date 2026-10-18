---
id: learning.zephyr-docs.api-file-system-power-reference.page-32
title: zephyr__bluetooth__audio__pacs.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pacs_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第32章\_zephyr\_\_bluetooth\_\_audio\_\_pacs.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/pacs_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙已发布音频能力服务（Published Audio Capabilities Service，PACS）的API。

<a id="details"></a>

```c
#include <stdbool.h>
#include <zephyr/bluetooth/assigned_numbers.h>
#include <zephyr/bluetooth/audio/audio.h>
#include <zephyr/bluetooth/conn.h>
#include <zephyr/sys/slist.h>
```

查看此文件的源码。

蓝牙已发布音频能力服务（Published Audio Capabilities Service，PACS）的API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 32.1\_数据结构（Data Structures）

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

## 32.2\_类型定义（Typedefs）

<a id="r_ga452591f80b6be5d79609b25ade2154a9"></a>

```c
typedef bool(* bt_pacs_cap_foreach_func_t) (const struct bt_pacs_cap *cap, void *user_data)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_pacs_cap_foreach_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pacs.html#ga452591f80b6be5d79609b25ade2154a9)、[bt_pacs_cap](../bluetooth_service_model_reference/P147_bt_pacs_cap_结构体.md)。

已发布音频能力（Published Audio Capability）迭代器回调（Iterator Callback）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 32.3\_函数（Functions）

<a id="r_ga31e2c7e9a4b5b6a291b96832c1218a49"></a>

```c
void bt_pacs_cap_foreach (enum bt_audio_dir dir, bt_pacs_cap_foreach_func_t func, void *user_data)
```

相关声明：[bt_pacs_cap_foreach](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pacs.html#ga31e2c7e9a4b5b6a291b96832c1218a49)、[bt_audio_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#ga5bd899fb5e4d844058184913866e462f)、[bt_pacs_cap_foreach_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pacs.html#ga452591f80b6be5d79609b25ade2154a9)。

已发布音频能力（Published Audio Capability）迭代器（Iterator）。

<a id="r_gac77a3dd5015058145b51db5fef2c9485"></a>

```c
int bt_pacs_register (const struct bt_pacs_register_param *param)
```

相关声明：[bt_pacs_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pacs.html#gac77a3dd5015058145b51db5fef2c9485)、[bt_pacs_register_param](../bluetooth_service_model_reference/P148_bt_pacs_register_param_结构体.md)。

注册已发布音频能力服务（Published Audio Capability Service）实例。

<a id="r_gac23d3c4e850394194871e8daaa44545b"></a>

```c
int bt_pacs_unregister (void)
```

相关声明：[bt_pacs_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pacs.html#gac23d3c4e850394194871e8daaa44545b)。

注销已发布音频能力服务（Published Audio Capability Service）实例。

<a id="r_ga251b36d4f5775eea1f69873709f847cc"></a>

```c
int bt_pacs_cap_register (enum bt_audio_dir dir, struct bt_pacs_cap *cap)
```

相关声明：[bt_pacs_cap_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pacs.html#ga251b36d4f5775eea1f69873709f847cc)、[bt_audio_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#ga5bd899fb5e4d844058184913866e462f)、[bt_pacs_cap](../bluetooth_service_model_reference/P147_bt_pacs_cap_结构体.md)。

注册已发布音频能力（Published Audio Capability）。

<a id="r_ga4f6015eba63ffc7a9377afe54a290da1"></a>

```c
int bt_pacs_cap_unregister (enum bt_audio_dir dir, struct bt_pacs_cap *cap)
```

相关声明：[bt_pacs_cap_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pacs.html#ga4f6015eba63ffc7a9377afe54a290da1)、[bt_audio_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#ga5bd899fb5e4d844058184913866e462f)、[bt_pacs_cap](../bluetooth_service_model_reference/P147_bt_pacs_cap_结构体.md)。

注销已发布音频能力（Published Audio Capability）。

<a id="r_gaff290fd59bb05012abcf405dbdc72884"></a>

```c
int bt_pacs_set_location (enum bt_audio_dir dir, enum bt_audio_location location)
```

相关声明：[bt_pacs_set_location](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pacs.html#gaff290fd59bb05012abcf405dbdc72884)、[bt_audio_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#ga5bd899fb5e4d844058184913866e462f)、[bt_audio_location](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga61230848c02098352320fe751332c4e8)。

设置某个端点类型（Endpoint Type）的位置（Location）。

<a id="r_ga29a1ec26c1e5e82e02eac39e1088332c"></a>

```c
int bt_pacs_set_available_contexts (enum bt_audio_dir dir, enum bt_audio_context contexts)
```

相关声明：[bt_pacs_set_available_contexts](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pacs.html#ga29a1ec26c1e5e82e02eac39e1088332c)、[bt_audio_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#ga5bd899fb5e4d844058184913866e462f)、[bt_audio_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gafb379ffa88388cc1397960155bbb2ab3)。

设置某个端点类型（Endpoint Type）的可用上下文（Available Contexts）。

<a id="r_ga437d824d0a944b6c30db492dbe28514f"></a>

```c
enum bt_audio_context bt_pacs_get_available_contexts (enum bt_audio_dir dir)
```

相关声明：[bt_audio_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gafb379ffa88388cc1397960155bbb2ab3)、[bt_pacs_get_available_contexts](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pacs.html#ga437d824d0a944b6c30db492dbe28514f)、[bt_audio_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#ga5bd899fb5e4d844058184913866e462f)。

获取某个端点类型（Endpoint Type）的可用上下文（Available Contexts）。

<a id="r_ga12f283d2daf72302a01cefb4a4a8fc70"></a>

```c
int bt_pacs_conn_set_available_contexts_for_conn (struct bt_conn *conn, enum bt_audio_dir dir, enum bt_audio_context *contexts)
```

相关声明：[bt_pacs_conn_set_available_contexts_for_conn](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pacs.html#ga12f283d2daf72302a01cefb4a4a8fc70)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_audio_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#ga5bd899fb5e4d844058184913866e462f)、[bt_audio_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gafb379ffa88388cc1397960155bbb2ab3)。

设置给定连接（Connection）的可用上下文（Available Contexts）。

<a id="r_ga7b28aa42525344445b20bb90a19441aa"></a>

```c
enum bt_audio_context bt_pacs_get_available_contexts_for_conn (struct bt_conn *conn, enum bt_audio_dir dir)
```

相关声明：[bt_audio_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gafb379ffa88388cc1397960155bbb2ab3)、[bt_pacs_get_available_contexts_for_conn](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pacs.html#ga7b28aa42525344445b20bb90a19441aa)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_audio_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#ga5bd899fb5e4d844058184913866e462f)。

获取给定连接（Connection）的可用上下文（Available Contexts）。

<a id="r_gabae9cf025f32ce80b660ebd7f95241b2"></a>

```c
int bt_pacs_set_supported_contexts (enum bt_audio_dir dir, enum bt_audio_context contexts)
```

相关声明：[bt_pacs_set_supported_contexts](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pacs.html#gabae9cf025f32ce80b660ebd7f95241b2)、[bt_audio_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#ga5bd899fb5e4d844058184913866e462f)、[bt_audio_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gafb379ffa88388cc1397960155bbb2ab3)。

设置某个端点类型（Endpoint Type）支持的上下文（Supported Contexts）。


## 32.4\_原页交叉引用（Cross References）

- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [zephyr/bluetooth/assigned_numbers.h](../api_source_socket_ethernet_reference/P001_assigned_numbers.h_源码浏览.md)
- [zephyr/bluetooth/audio/audio.h](../api_source_compiler_device_reference/P002_audio.h_源码浏览.md)
- [zephyr/bluetooth/conn.h](../api_source_register_time_reference/P002_conn.h_源码浏览.md)
- [zephyr/sys/slist.h](../slist_reference/P003_单向链表头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P641_pacs.h_源码浏览.md)
- [bt_pacs_cap](../bluetooth_service_model_reference/P147_bt_pacs_cap_结构体.md)
- [bt_pacs_register_param](../bluetooth_service_model_reference/P148_bt_pacs_register_param_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [bt_pacs_cap_foreach_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pacs.html#ga452591f80b6be5d79609b25ade2154a9)
- [bt_pacs_cap_foreach](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pacs.html#ga31e2c7e9a4b5b6a291b96832c1218a49)
- [bt_audio_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html#ga5bd899fb5e4d844058184913866e462f)
- [bt_pacs_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pacs.html#gac77a3dd5015058145b51db5fef2c9485)
- [bt_pacs_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pacs.html#gac23d3c4e850394194871e8daaa44545b)
- [bt_pacs_cap_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pacs.html#ga251b36d4f5775eea1f69873709f847cc)
- [bt_pacs_cap_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pacs.html#ga4f6015eba63ffc7a9377afe54a290da1)
- [bt_pacs_set_location](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pacs.html#gaff290fd59bb05012abcf405dbdc72884)
- [bt_audio_location](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga61230848c02098352320fe751332c4e8)
- [bt_pacs_set_available_contexts](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pacs.html#ga29a1ec26c1e5e82e02eac39e1088332c)
- [bt_audio_context](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#gafb379ffa88388cc1397960155bbb2ab3)
- [bt_pacs_get_available_contexts](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pacs.html#ga437d824d0a944b6c30db492dbe28514f)
- [bt_pacs_conn_set_available_contexts_for_conn](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pacs.html#ga12f283d2daf72302a01cefb4a4a8fc70)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_pacs_get_available_contexts_for_conn](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pacs.html#ga7b28aa42525344445b20bb90a19441aa)
- [bt_pacs_set_supported_contexts](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pacs.html#gabae9cf025f32ce80b660ebd7f95241b2)

<a id="header-details"></a>

---

[上一章](P031_zephyr__mgmt__mcumgr__grp__os_mgmt__os_mgmt.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P033_zephyr__dt-bindings__usb-c__pd.h_文件参考.md)
