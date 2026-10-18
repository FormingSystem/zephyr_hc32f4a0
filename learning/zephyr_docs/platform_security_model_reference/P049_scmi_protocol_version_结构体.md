---
id: learning.zephyr-docs.platform-security-model-reference.page-49
title: scmi_protocol_version_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structscmi__protocol__version.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第49章\_scmi\_protocol\_version\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structscmi__protocol__version.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

系统控制与管理接口（SCMI）的协议版本。

```c
#include <zephyr/drivers/firmware/scmi/protocol.h>
```

<a id="details"></a>

SCMI 协议版本。协议版本使用一个 32 位无符号整数表示，其中高 16 位为主版本号（Major revision），低 16 位为次版本号（Minor revision）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 49.1\_数据成员（Data Fields）

```c
union {
```

<a id="r_add9bee7dd1a69869d1c1d4d0208c58ba"></a>

```c
uint32_t raw
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[raw](#a978b1c6f10fd87e5f538e840e4e71470)。

原始的 32 位协议版本值。

```c
struct {
```

<a id="r_a3955ea0f9c3e72f142598b7c134cc4a7"></a>

```c
uint16_t minor
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[minor](#a602f109457cb0e481a0446cb40f81fab)。

协议次版本号（Minor revision）。

<a id="r_a4e75bf1267f674e1616d1e6f8f1caea8"></a>

```c
uint16_t major
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[major](#a03bf7fd19968bd6e976c948d29f83326)。

协议主版本号（Major revision）。

<a id="r_abbe789aac678a371c7c959f67b5cd267"></a>

```c
}
```

<a id="r_ade3ddead1c5047d93002db086ace35ef"></a>

```c
};
```

访问协议版本位域。

## 49.2\_详细说明（Detailed Documentation）

<a id="ade3ddead1c5047d93002db086ace35ef"></a>

### `[union]`

```c
union { ... } scmi_protocol_version
```

访问协议版本位域。

<a id="a03bf7fd19968bd6e976c948d29f83326"></a>

### `major`

```c
uint16_t scmi_protocol_version::major
```

协议主版本号（Major revision）。

<a id="a602f109457cb0e481a0446cb40f81fab"></a>

### `minor`

```c
uint16_t scmi_protocol_version::minor
```

协议次版本号（Minor revision）。

<a id="a978b1c6f10fd87e5f538e840e4e71470"></a>

### `raw`

```c
uint32_t scmi_protocol_version::raw
```

原始的 32 位协议版本值。

本数据类型文档由以下文件生成：

- `zephyr/drivers/firmware/scmi/protocol.h`

## 49.3\_原页交叉引用（Cross References）

- [zephyr/drivers/firmware/scmi/protocol.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2firmware_2scmi_2protocol_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [scmi_protocol_version](P049_scmi_protocol_version_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P048_scmi_protocol_events_结构体.md) · [返回大纲](大纲.md) · [下一章](P050_scmi_reset_domain_attr_结构体.md)
