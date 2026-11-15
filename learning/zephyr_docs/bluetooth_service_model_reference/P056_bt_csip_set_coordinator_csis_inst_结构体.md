---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-56
title: bt_csip_set_coordinator_csis_inst_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__csip__set__coordinator__csis__inst.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第56章\_bt\_csip\_set\_coordinator\_csis\_inst\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__csip__set__coordinator__csis__inst.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

表示远端设备上协调集合（Coordinated Set）实例的结构体。

```c
#include <zephyr/bluetooth/audio/csip.h>
```

<a id="details"></a>

表示远端设备上的协调集合实例（Coordinated set instance）的结构。在通过 `bt_csip_set_coordinator_discover()` 发现集合期间，填充此结构中的值。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 56.1\_数据成员（Data Fields）

<a id="r_a0c407932ad1fb5e36cd19daf28bac96d"></a>

```c
struct bt_csip_set_coordinator_set_info info
```

相关声明：[bt_csip_set_coordinator_set_info](P057_bt_csip_set_coordinator_set_info_结构体.md)、[info](#a0c407932ad1fb5e36cd19daf28bac96d)。

协调集合信息（Coordinated set information）。

<a id="r_a7e7210dded5a084c5d45f9209895e37f"></a>

```c
void * svc_inst
```

相关声明：[svc_inst](#a7e7210dded5a084c5d45f9209895e37f)。

内部使用的指针值（Internal pointer value）。

## 56.2\_详细说明（Detailed Documentation）

<a id="a0c407932ad1fb5e36cd19daf28bac96d"></a>

### `info`

```c
struct bt_csip_set_coordinator_set_info bt_csip_set_coordinator_csis_inst::info
```

协调集合信息（Coordinated set information）。

<a id="a7e7210dded5a084c5d45f9209895e37f"></a>

### `svc_inst`

```c
void* bt_csip_set_coordinator_csis_inst::svc_inst
```

内部使用的指针值（Internal pointer value）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/csip.h`

## 56.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/csip.h](https://docs.zephyrproject.org/latest/doxygen/html/csip_8h_source.html)
- [bt_csip_set_coordinator_set_info](P057_bt_csip_set_coordinator_set_info_结构体.md)
- [bt_csip_set_coordinator_discover()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html#ga7e7ea4a92bb76aded86807571a2cbb73)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P055_bt_csip_set_coordinator_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P057_bt_csip_set_coordinator_set_info_结构体.md)
