---
id: learning.zephyr-docs.system-service-model-reference.page-48
title: img_mgmt_state_slot_encode_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structimg__mgmt__state__slot__encode.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第48章\_img\_mgmt\_state\_slot\_encode\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structimg__mgmt__state__slot__encode.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MGMT_EVT_OP_IMG_MGMT_IMAGE_SLOT_STATE通知回调中提供的结构。该回调允许应用或模块向映像槽位状态（Image Slot State）响应追加自定义字段。

```c
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt_callbacks.h>
```

<a id="details"></a>

MGMT_EVT_OP_IMG_MGMT_IMAGE_SLOT_STATE通知回调中提供的结构。该回调允许应用或模块向映像槽位状态（Image Slot State）响应追加自定义字段。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 48.1\_数据成员（Data Fields）

<a id="r_a9279018722b20380da6e48046787d220"></a>

```c
bool * ok
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[ok](#a9279018722b20380da6e48046787d220)。

<a id="r_a62157cb9a3288806f4ec11e5c2ef20ac"></a>

```c
zcbor_state_t * zse
```

相关声明：[zse](#a62157cb9a3288806f4ec11e5c2ef20ac)。

<a id="r_ad669d8c2062f90d008f715dee206c687"></a>

```c
const uint32_t slot
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[slot](#ad669d8c2062f90d008f715dee206c687)。

<a id="r_aa4bf77897519408786c1ee28029342dd"></a>

```c
const char * version
```

相关声明：[version](#aa4bf77897519408786c1ee28029342dd)。

<a id="r_a5c2486f75743eb44133819b5f35d97cb"></a>

```c
const uint8_t * hash
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[hash](#a5c2486f75743eb44133819b5f35d97cb)。

<a id="r_a9e53ce9a8a88b76e035b02cd2289fb07"></a>

```c
const int flags
```

相关声明：[flags](#a9e53ce9a8a88b76e035b02cd2289fb07)。

## 48.2\_详细说明（Detailed Documentation）

<a id="a9e53ce9a8a88b76e035b02cd2289fb07"></a>

### `flags`

```c
const int img_mgmt_state_slot_encode::flags
```

<a id="a5c2486f75743eb44133819b5f35d97cb"></a>

### `hash`

```c
const uint8_t* img_mgmt_state_slot_encode::hash
```

<a id="a9279018722b20380da6e48046787d220"></a>

### `ok`

```c
bool* img_mgmt_state_slot_encode::ok
```

<a id="ad669d8c2062f90d008f715dee206c687"></a>

### `slot`

```c
const uint32_t img_mgmt_state_slot_encode::slot
```

<a id="aa4bf77897519408786c1ee28029342dd"></a>

### `version`

```c
const char* img_mgmt_state_slot_encode::version
```

<a id="a62157cb9a3288806f4ec11e5c2ef20ac"></a>

### `zse`

```c
zcbor_state_t* img_mgmt_state_slot_encode::zse
```

本数据类型文档由以下文件生成：

- `zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt_callbacks.h`

## 48.3\_原页交叉引用（Cross References）

- [MGMT_EVT_OP_IMG_MGMT_IMAGE_SLOT_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__img__mgmt.html#gga3fa2c42bade08cca1122e32f6315f107a52a1b8f3d4dae7bab74fd6187500acc7)
- [zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt_callbacks.h](https://docs.zephyrproject.org/latest/doxygen/html/img__mgmt__callbacks_8h_source.html)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P047_img_mgmt_state_结构体.md) · [返回大纲](大纲.md) · [下一章](P049_img_mgmt_upload_action_结构体.md)
