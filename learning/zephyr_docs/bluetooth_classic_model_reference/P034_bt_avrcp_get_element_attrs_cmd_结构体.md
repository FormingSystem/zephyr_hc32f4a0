---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-34
title: bt_avrcp_get_element_attrs_cmd_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__get__element__attrs__cmd.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第34章\_bt\_avrcp\_get\_element\_attrs\_cmd\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__get__element__attrs__cmd.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

获取元素属性（GetElementAttributes）命令请求结构体。

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

<a id="details"></a>

获取元素属性（GetElementAttributes）命令请求结构体。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 34.1\_数据成员（Data Fields）

<a id="r_a82826b71e51eb7ccc296c753c9d855f3"></a>

```c
uint8_t identifier [8]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[identifier](#a82826b71e51eb7ccc296c753c9d855f3)。

元素标识符，`0x0` 表示当前播放的元素。

<a id="r_a1404b06ec564c9ae57f3fc6a920b6407"></a>

```c
uint8_t num_attrs
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_attrs](#a1404b06ec564c9ae57f3fc6a920b6407)。

请求的属性数量，0 表示全部属性。

<a id="r_a02c96f2e1a1b747a041b663b4532fdc2"></a>

```c
uint32_t attr_ids []
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[attr_ids](#a02c96f2e1a1b747a041b663b4532fdc2)。

属性 ID 数组，类型为 `bt_avrcp_media_attr_id_t`。

## 34.2\_详细说明（Detailed Documentation）

<a id="a02c96f2e1a1b747a041b663b4532fdc2"></a>

### `attr_ids`

```c
uint32_t bt_avrcp_get_element_attrs_cmd::attr_ids[]
```

属性 ID 数组，类型为 `bt_avrcp_media_attr_id_t`。

<a id="a82826b71e51eb7ccc296c753c9d855f3"></a>

### `identifier`

```c
uint8_t bt_avrcp_get_element_attrs_cmd::identifier[8]
```

元素标识符，`0x0` 表示当前播放的元素。

<a id="a1404b06ec564c9ae57f3fc6a920b6407"></a>

### `num_attrs`

```c
uint8_t bt_avrcp_get_element_attrs_cmd::num_attrs
```

请求的属性数量，0 表示全部属性。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/avrcp.h`

## 34.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/avrcp.h](https://docs.zephyrproject.org/latest/doxygen/html/avrcp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [bt_avrcp_media_attr_id_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga0ebc5d2657688b70119e11ac20d24592)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P033_bt_avrcp_get_curr_player_app_setting_val_rsp_结构体.md) · [返回大纲](大纲.md) · [下一章](P035_bt_avrcp_get_element_attrs_rsp_结构体.md)
