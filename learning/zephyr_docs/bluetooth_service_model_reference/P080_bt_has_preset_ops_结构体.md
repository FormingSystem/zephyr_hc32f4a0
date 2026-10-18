---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-80
title: bt_has_preset_ops_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__has__preset__ops.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第80章\_bt\_has\_preset\_ops\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__has__preset__ops.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

预设操作（Preset Operations）结构。

```c
#include <zephyr/bluetooth/audio/has.h>
```

<a id="details"></a>

预设操作（Preset Operations）结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 80.1\_数据成员（Data Fields）

<a id="r_aec9d0f01c03f02f0a6f124527b72235e"></a>

```c
int(* select )(uint8_t index, bool sync)
```

相关声明：[select](#aec9d0f01c03f02f0a6f124527b72235e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

预设选择回调（Preset select callback）。

<a id="r_a7f0069639eb3b1f8b0d290a752b68770"></a>

```c
void(* name_changed )(uint8_t index, const char *name)
```

相关声明：[name_changed](#a7f0069639eb3b1f8b0d290a752b68770)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

预设名称变化回调（Preset name changed callback）。

## 80.2\_详细说明（Detailed Documentation）

<a id="a7f0069639eb3b1f8b0d290a752b68770"></a>

### `name_changed`

```c
void(* bt_has_preset_ops::name_changed) (uint8_t index, const char *name)
```

预设名称变化回调（Preset name changed callback）。

`index` 标识的预设名称（Preset name）变化时调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `index` | 名称已变化的预设索引（Preset index）。 |
| `name` | 预设当前名称（Preset current name）。 |

<a id="aec9d0f01c03f02f0a6f124527b72235e"></a>

### `select`

```c
int(* bt_has_preset_ops::select) (uint8_t index, bool sync)
```

预设选择回调（Preset select callback）。

客户端请求选择 `index` 标识的预设（Preset）时调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `index` | 请求激活的预设索引（Preset index）。 |
| `sync` | 服务器是否必须将此变化转发给双耳助听器集合（Binaural Hearing Aid Set）的另一成员。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，错误时为负值。当前无法执行操作时为 `-EBUSY`；若需要用户在请求的预设变为活动预设后，通过调用 `bt_has_preset_active_set` 确认，则返回 `-EINPROGRESS`。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/has.h`

## 80.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/has.h](https://docs.zephyrproject.org/latest/doxygen/html/has_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [bt_has_preset_active_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga2c0fe62baa63b72703d6f553f1de072b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P079_bt_has_features_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P081_bt_has_preset_record_结构体.md)
