---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-58
title: bt_csip_set_coordinator_set_member_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__csip__set__coordinator__set__member.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第58章\_bt\_csip\_set\_coordinator\_set\_member\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__csip__set__coordinator__set__member.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

将远端设备表示为集合成员（Set Member）的结构体。

```c
#include <zephyr/bluetooth/audio/csip.h>
```

<a id="details"></a>

将远端设备表示为集合成员（Set Member）的结构体。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 58.1\_数据成员（Data Fields）

<a id="r_ac883b4348d5620b5315eeb4d32ea0260"></a>

```c
struct bt_csip_set_coordinator_csis_inst insts [0U]
```

相关声明：[bt_csip_set_coordinator_csis_inst](P056_bt_csip_set_coordinator_csis_inst_结构体.md)、[insts](#ac883b4348d5620b5315eeb4d32ea0260)。

远端设备的协调集合标识服务实例数组（Coordinated Set Identification Service instances）。

## 58.2\_详细说明（Detailed Documentation）

<a id="ac883b4348d5620b5315eeb4d32ea0260"></a>

### `insts`

```c
struct bt_csip_set_coordinator_csis_inst bt_csip_set_coordinator_set_member::insts[0U]
```

远端设备的协调集合标识服务实例数组（Coordinated Set Identification Service instances）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/csip.h`

## 58.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/csip.h](https://docs.zephyrproject.org/latest/doxygen/html/csip_8h_source.html)
- [bt_csip_set_coordinator_csis_inst](P056_bt_csip_set_coordinator_csis_inst_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P057_bt_csip_set_coordinator_set_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P059_bt_csip_set_member_cb_结构体.md)
