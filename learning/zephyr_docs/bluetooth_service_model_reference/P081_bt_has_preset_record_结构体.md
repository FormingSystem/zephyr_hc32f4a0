---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-81
title: bt_has_preset_record_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__has__preset__record.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第81章\_bt\_has\_preset\_record\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__has__preset__record.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

预设记录（Preset Record）定义。

```c
#include <zephyr/bluetooth/audio/has.h>
```

<a id="details"></a>

预设记录（Preset Record）定义。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 81.1\_数据成员（Data Fields）

<a id="r_a68484827708a19a75f2cdf922f01e677"></a>

```c
uint8_t index
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[index](#a68484827708a19a75f2cdf922f01e677)。

唯一预设索引（Unique preset index）。

<a id="r_ad3fc652d24a8b625b97abb02f0fb66bb"></a>

```c
enum bt_has_properties properties
```

相关声明：[bt_has_properties](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga7b8913a9f9bc4d5c066582780adcf274)、[properties](#ad3fc652d24a8b625b97abb02f0fb66bb)。

预设属性位域（Preset properties bitfield）。

<a id="r_ac064f0ae2841627930fb3ca0370ef5ec"></a>

```c
const char * name
```

相关声明：[name](#ac064f0ae2841627930fb3ca0370ef5ec)。

预设名称（Preset name）。

## 81.2\_详细说明（Detailed Documentation）

<a id="a68484827708a19a75f2cdf922f01e677"></a>

### `index`

```c
uint8_t bt_has_preset_record::index
```

唯一预设索引（Unique preset index）。

<a id="ac064f0ae2841627930fb3ca0370ef5ec"></a>

### `name`

```c
const char* bt_has_preset_record::name
```

预设名称（Preset name）。

<a id="ad3fc652d24a8b625b97abb02f0fb66bb"></a>

### `properties`

```c
enum bt_has_properties bt_has_preset_record::properties
```

预设属性位域（Preset properties bitfield）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/has.h`

## 81.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/has.h](https://docs.zephyrproject.org/latest/doxygen/html/has_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_has_properties](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html#ga7b8913a9f9bc4d5c066582780adcf274)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P080_bt_has_preset_ops_结构体.md) · [返回大纲](大纲.md) · [下一章](P082_bt_has_preset_register_param_结构体.md)
