---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-82
title: bt_has_preset_register_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__has__preset__register__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第82章\_bt\_has\_preset\_register\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__has__preset__register__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

预设（Preset）的注册结构。

```c
#include <zephyr/bluetooth/audio/has.h>
```

<a id="details"></a>

预设（Preset）的注册结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 82.1\_数据成员（Data Fields）

<a id="r_a9a3ade943b4f7569577c092df3ec467c"></a>

```c
uint8_t index
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[index](#a9a3ade943b4f7569577c092df3ec467c)。

预设索引（Preset index）。

<a id="r_a8273bbec14040a7dd67aeac14188b86b"></a>

```c
enum bt_has_properties properties
```

相关声明：[bt_has_properties](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga7b8913a9f9bc4d5c066582780adcf274)、[properties](#a8273bbec14040a7dd67aeac14188b86b)。

预设属性（Preset properties）。

<a id="r_a35b8d2e9a01198cc34350595c786f1ae"></a>

```c
const char * name
```

相关声明：[name](#a35b8d2e9a01198cc34350595c786f1ae)。

预设名称（Preset name）。

<a id="r_a6e480fb6337d363353ca7ba6f716cd71"></a>

```c
const struct bt_has_preset_ops * ops
```

相关声明：[bt_has_preset_ops](P080_bt_has_preset_ops_结构体.md)、[ops](#a6e480fb6337d363353ca7ba6f716cd71)。

预设操作（Preset Operations）结构。

## 82.2\_详细说明（Detailed Documentation）

<a id="a9a3ade943b4f7569577c092df3ec467c"></a>

### `index`

```c
uint8_t bt_has_preset_register_param::index
```

预设索引（Preset index）。

唯一预设标识符（Unique preset identifier），不得为 `BT_HAS_PRESET_INDEX_NONE`。

<a id="a35b8d2e9a01198cc34350595c786f1ae"></a>

### `name`

```c
const char* bt_has_preset_register_param::name
```

预设名称（Preset name）。

预设名称（Preset name）。若启用 `CONFIG_BT_HAS_PRESET_NAME_DYNAMIC`，服务器或客户端之后可以修改此名称。其长度必须大于 `BT_HAS_PRESET_NAME_MIN`；若超过 `BT_HAS_PRESET_NAME_MAX`，名称会被截断。

<a id="a6e480fb6337d363353ca7ba6f716cd71"></a>

### `ops`

```c
const struct bt_has_preset_ops* bt_has_preset_register_param::ops
```

预设操作（Preset Operations）结构。

<a id="a8273bbec14040a7dd67aeac14188b86b"></a>

### `properties`

```c
enum bt_has_properties bt_has_preset_register_param::properties
```

预设属性（Preset properties）。

预设属性位域（Preset properties bitfield）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/has.h`

## 82.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/has.h](https://docs.zephyrproject.org/latest/doxygen/html/has_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_has_properties](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga7b8913a9f9bc4d5c066582780adcf274)
- [bt_has_preset_ops](P080_bt_has_preset_ops_结构体.md)
- [BT_HAS_PRESET_INDEX_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga462679b8b5c91762c6d1daf03c5675d0)
- [CONFIG_BT_HAS_PRESET_NAME_DYNAMIC](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HAS_PRESET_NAME_DYNAMIC)
- [BT_HAS_PRESET_NAME_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#gacbc29958c09b26a81e02893cd5914074)
- [BT_HAS_PRESET_NAME_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#gae133807f12d0d7a1ecd1f8dda24c7f09)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P081_bt_has_preset_record_结构体.md) · [返回大纲](大纲.md) · [下一章](P083_bt_hfp_ag_结构体.md)
