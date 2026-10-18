---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-20
title: bt_avrcp_change_path_cmd_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__change__path__cmd.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_bt\_avrcp\_change\_path\_cmd\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__change__path__cmd.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

更改路径（ChangePath）命令请求。

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

<a id="details"></a>

更改路径（ChangePath）命令请求。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 20.1\_数据成员（Data Fields）

<a id="r_ac575ced16bc5e61043b035b406f732a4"></a>

```c
uint16_t uid_counter
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uid_counter](#ac575ced16bc5e61043b035b406f732a4)。

UID 计数器（UID Counter）。

<a id="r_a1ced4e12dd7d1c3b31213dce355cf165"></a>

```c
uint8_t direction
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[direction](#a1ced4e12dd7d1c3b31213dce355cf165)。

更改路径的方向，类型为 `bt_avrcp_change_path_t`。

<a id="r_a026e337b5bcf6f827f32314eabd19832"></a>

```c
uint8_t folder_uid [8]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[folder_uid](#a026e337b5bcf6f827f32314eabd19832)。

64 位文件夹 UID。

## 20.2\_详细说明（Detailed Documentation）

<a id="a1ced4e12dd7d1c3b31213dce355cf165"></a>

### `direction`

```c
uint8_t bt_avrcp_change_path_cmd::direction
```

更改路径的方向，类型为 `bt_avrcp_change_path_t`。

<a id="a026e337b5bcf6f827f32314eabd19832"></a>

### `folder_uid`

```c
uint8_t bt_avrcp_change_path_cmd::folder_uid[8]
```

64 位文件夹 UID。

<a id="ac575ced16bc5e61043b035b406f732a4"></a>

### `uid_counter`

```c
uint16_t bt_avrcp_change_path_cmd::uid_counter
```

UID 计数器（UID Counter）。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/avrcp.h`

## 20.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/avrcp.h](https://docs.zephyrproject.org/latest/doxygen/html/avrcp_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_avrcp_change_path_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga02d67e84b4a48ebecf3b307cbd4bb61c)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P019_bt_avrcp_app_setting_val_text_结构体.md) · [返回大纲](大纲.md) · [下一章](P021_bt_avrcp_change_path_rsp_结构体.md)
