---
id: learning.zephyr-docs.network-core-model-reference.page-42
title: ieee802154_req_params_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__req__params.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第42章\_ieee802154\_req\_params\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__req__params.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

扫描参数（Scanning Parameters）。

```c
#include <zephyr/net/ieee802154_mgmt.h>
```

<a id="details"></a>

扫描参数（Scanning Parameters）。用于请求扫描并获取结果，见第8.2.11.2节。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 42.1\_数据成员（Data Fields）

<a id="r_ad49071ae3c35a548f6894d32be017ad7"></a>

```c
uint32_t channel_set
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[channel_set](#ad49071ae3c35a548f6894d32be017ad7)。

要扫描的信道集合（Channel Set），使用上述宏进行管理。

<a id="r_a75b3e1658829dfa4970cef7267250c9b"></a>

```c
uint32_t duration
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[duration](#a75b3e1658829dfa4970cef7267250c9b)。

每个信道的扫描持续时间（Scan Duration），单位为毫秒。

<a id="r_a78c9f6b62c7cfc51f514df09a2719441"></a>

```c
uint16_t channel
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[channel](#a78c9f6b62c7cfc51f514df09a2719441)。

作为结果返回的当前使用信道（Channel）。

<a id="r_abde2cf05ea51cd0e024552aaf2414c86"></a>

```c
uint16_t pan_id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[pan_id](#abde2cf05ea51cd0e024552aaf2414c86)。

作为结果返回的当前使用pan_id。

```c
union {
```

<a id="r_aba54aac5e287fe09e22a32057a522477"></a>

```c
uint16_t short_addr
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[short_addr](#a9cafc55c59dc4eff07bdf03e60da07ec)。

采用CPU字节序（CPU Byte Order）。

<a id="r_a718daa1b38dffaecfe20a4d62dfbf516"></a>

```c
uint8_t addr [8]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[addr](#aa1b2ea9ffb009a1b6255a9e57ddef9f7)。

采用大端序（Big Endian）。

<a id="r_a591ec123b8009042260d51a6c134a11d"></a>

```c
};
```

结果地址（Result Address）。

<a id="r_a8c63caa3ae260f4c6f9bebe71677673b"></a>

```c
uint8_t len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[len](#a8c63caa3ae260f4c6f9bebe71677673b)。

地址长度（Address Length）。

<a id="r_af08c2fa32367340c54c8d8bf9c46f34a"></a>

```c
uint8_t lqi
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[lqi](#af08c2fa32367340c54c8d8bf9c46f34a)。

链路质量信息（Link Quality Information），范围为0至255。

<a id="r_af3243c160c8746cfd2e97fcf1218a80b"></a>

```c
bool association_permitted
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[association_permitted](#af3243c160c8746cfd2e97fcf1218a80b)。

表示协调器（Coordinator）是否允许关联的标志。

<a id="r_a74d1d4fc3dbff188f0fddcf091da3723"></a>

```c
uint8_t * beacon_payload
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[beacon_payload](#a74d1d4fc3dbff188f0fddcf091da3723)。

信标（Beacon）的附加载荷，如有。

<a id="r_a05bf6f9356b375ed9706bd1a8cdc497c"></a>

```c
size_t beacon_payload_len
```

相关声明：[beacon_payload_len](#a05bf6f9356b375ed9706bd1a8cdc497c)。

附加载荷（Additional Payload）的长度。

## 42.2\_详细说明（Detailed Documentation）

<a id="a591ec123b8009042260d51a6c134a11d"></a>

### `[union]`

```c
union { ... } ieee802154_req_params
```

结果地址（Result Address）。

<a id="aa1b2ea9ffb009a1b6255a9e57ddef9f7"></a>

### `addr`

```c
uint8_t ieee802154_req_params::addr[8]
```

采用大端序（Big Endian）。

<a id="af3243c160c8746cfd2e97fcf1218a80b"></a>

### `association_permitted`

```c
bool ieee802154_req_params::association_permitted
```

表示协调器（Coordinator）是否允许关联的标志。

<a id="a74d1d4fc3dbff188f0fddcf091da3723"></a>

### `beacon_payload`

```c
uint8_t* ieee802154_req_params::beacon_payload
```

信标（Beacon）的附加载荷，如有。

<a id="a05bf6f9356b375ed9706bd1a8cdc497c"></a>

### `beacon_payload_len`

```c
size_t ieee802154_req_params::beacon_payload_len
```

附加载荷（Additional Payload）的长度。

<a id="a78c9f6b62c7cfc51f514df09a2719441"></a>

### `channel`

```c
uint16_t ieee802154_req_params::channel
```

作为结果返回的当前使用信道（Channel）。

<a id="ad49071ae3c35a548f6894d32be017ad7"></a>

### `channel_set`

```c
uint32_t ieee802154_req_params::channel_set
```

要扫描的信道集合（Channel Set），使用上述宏进行管理。

<a id="a75b3e1658829dfa4970cef7267250c9b"></a>

### `duration`

```c
uint32_t ieee802154_req_params::duration
```

每个信道的扫描持续时间（Scan Duration），单位为毫秒。

<a id="a8c63caa3ae260f4c6f9bebe71677673b"></a>

### `len`

```c
uint8_t ieee802154_req_params::len
```

地址长度（Address Length）。

<a id="af08c2fa32367340c54c8d8bf9c46f34a"></a>

### `lqi`

```c
uint8_t ieee802154_req_params::lqi
```

链路质量信息（Link Quality Information），范围为0至255。

<a id="abde2cf05ea51cd0e024552aaf2414c86"></a>

### `pan_id`

```c
uint16_t ieee802154_req_params::pan_id
```

作为结果返回的当前使用pan_id。

<a id="a9cafc55c59dc4eff07bdf03e60da07ec"></a>

### `short_addr`

```c
uint16_t ieee802154_req_params::short_addr
```

采用CPU字节序（CPU Byte Order）。

本数据类型文档由以下文件生成：

- `zephyr/net/ieee802154_mgmt.h`

## 42.3\_原页交叉引用（Cross References）

- [zephyr/net/ieee802154_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__mgmt_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [ieee802154_req_params](P042_ieee802154_req_params_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P041_ieee802154_radio_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P043_ieee802154_security_control_field_结构体.md)
