---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-79
title: bt_has_features_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__has__features__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第79章\_bt\_has\_features\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__has__features__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于注册助听接入服务（Hearing Access Service）实例特性的结构。

```c
#include <zephyr/bluetooth/audio/has.h>
```

<a id="details"></a>

用于注册助听接入服务（Hearing Access Service）实例特性的结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 79.1\_数据成员（Data Fields）

<a id="r_abcaf8630309bcae1a8184095c1eca656"></a>

```c
enum bt_has_hearing_aid_type type
```

相关声明：[bt_has_hearing_aid_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#gaa9572a32f912c8fe529b510aa23f4540)、[type](#abcaf8630309bcae1a8184095c1eca656)。

助听器类型值（Hearing Aid Type value）。

<a id="r_ada946ee62547349bc01054db5cafa279"></a>

```c
bool preset_sync_support
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[preset_sync_support](#ada946ee62547349bc01054db5cafa279)。

预设同步支持（Preset Synchronization Support）。

<a id="r_a5ff95f2633bf577fc0f4c3d714d53bb1"></a>

```c
bool independent_presets
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[independent_presets](#a5ff95f2633bf577fc0f4c3d714d53bb1)。

独立预设（Independent Presets）。

## 79.2\_详细说明（Detailed Documentation）

<a id="a5ff95f2633bf577fc0f4c3d714d53bb1"></a>

### `independent_presets`

```c
bool bt_has_features_param::independent_presets
```

独立预设（Independent Presets）。

仅在 `type` 为 `BT_HAS_HEARING_AID_TYPE_BINAURAL` 且 `CONFIG_BT_HAS_PRESET_COUNT` 非零时适用。

<a id="ada946ee62547349bc01054db5cafa279"></a>

### `preset_sync_support`

```c
bool bt_has_features_param::preset_sync_support
```

预设同步支持（Preset Synchronization Support）。

仅在 `type` 为 `BT_HAS_HEARING_AID_TYPE_BINAURAL` 且 `CONFIG_BT_HAS_PRESET_COUNT` 非零时适用。

<a id="abcaf8630309bcae1a8184095c1eca656"></a>

### `type`

```c
enum bt_has_hearing_aid_type bt_has_features_param::type
```

助听器类型值（Hearing Aid Type value）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/has.h`

## 79.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/has.h](https://docs.zephyrproject.org/latest/doxygen/html/has_8h_source.html)
- [bt_has_hearing_aid_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#gaa9572a32f912c8fe529b510aa23f4540)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [BT_HAS_HEARING_AID_TYPE_BINAURAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ggaa9572a32f912c8fe529b510aa23f4540a5bc91d6bcba7e140cc642715ccc9879c)
- [CONFIG_BT_HAS_PRESET_COUNT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HAS_PRESET_COUNT)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P078_bt_has_client_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P080_bt_has_preset_ops_结构体.md)
