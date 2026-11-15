---
id: learning.zephyr-docs.network-core-model-reference.page-43
title: ieee802154_security_control_field_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__security__control__field.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第43章\_ieee802154\_security\_control\_field\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__security__control__field.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

安全控制（Security Control）字段，即辅助安全头的第一个八位组。

```c
#include <zephyr/net/ieee802154_frame.h>
```

<a id="details"></a>

安全控制字段（Security Control Field），即辅助安全头的第一个八位组。见第9.4.2节及图9-5。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 43.1\_数据成员（Data Fields）

<a id="r_a7e497bc409cf73cea2b374418eeeb7cd"></a>

```c
uint8_t reserved: 3
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[reserved](#a7e497bc409cf73cea2b374418eeeb7cd)。

保留字段（Reserved），应为0。

<a id="r_ab4063e2e9715ef131e585ddaaea42090"></a>

```c
uint8_t key_id_mode: 2
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[key_id_mode](#ab4063e2e9715ef131e585ddaaea42090)。

密钥标识符模式（Key Identifier Mode），见ieee802154_key_id_mode。

<a id="r_af57b19d0851fbda4c91c8cbaf79b0722"></a>

```c
uint8_t security_level: 3
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[security_level](#af57b19d0851fbda4c91c8cbaf79b0722)。

安全等级（Security Level），见ieee802154_security_level。

## 43.2\_详细说明（Detailed Documentation）

<a id="ab4063e2e9715ef131e585ddaaea42090"></a>

### `key_id_mode`

```c
uint8_t ieee802154_security_control_field::key_id_mode
```

密钥标识符模式（Key Identifier Mode），见ieee802154_key_id_mode。

<a id="a7e497bc409cf73cea2b374418eeeb7cd"></a>

### `reserved`

```c
uint8_t ieee802154_security_control_field::reserved
```

保留字段（Reserved），应为0。

<a id="af57b19d0851fbda4c91c8cbaf79b0722"></a>

### `security_level`

```c
uint8_t ieee802154_security_control_field::security_level
```

安全等级（Security Level），见ieee802154_security_level。

本数据类型文档由以下文件生成：

- `zephyr/net/ieee802154_frame.h`

## 43.3\_原页交叉引用（Cross References）

- [zephyr/net/ieee802154_frame.h](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [ieee802154_key_id_mode](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#ac5819ed25fa7b56756e8e7962f579ec7)
- [ieee802154_security_level](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#aaf5ffabf140bf36c9076662e4b46e4a2)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P042_ieee802154_req_params_结构体.md) · [返回大纲](大纲.md) · [下一章](P044_ieee802154_security_ctx_结构体.md)
