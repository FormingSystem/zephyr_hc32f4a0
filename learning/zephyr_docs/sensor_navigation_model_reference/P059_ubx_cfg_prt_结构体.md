---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-59
title: ubx_cfg_prt_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structubx__cfg__prt.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第59章\_ubx\_cfg\_prt\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structubx__cfg__prt.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/modem/ubx/protocol.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 59.1\_数据成员（Data Fields）

<a id="r_af5a445ab598a2b93e884c916fe13affc"></a>

```c
uint8_t port_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[port_id](#af5a445ab598a2b93e884c916fe13affc)。

<a id="r_aba6bef46b7818a2396b77a0b1245ecc5"></a>

```c
uint8_t reserved1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[reserved1](#aba6bef46b7818a2396b77a0b1245ecc5)。

<a id="r_a1d4df224a3a9e7e6031a418745ee4e95"></a>

```c
uint16_t rx_ready_pin
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[rx_ready_pin](#a1d4df224a3a9e7e6031a418745ee4e95)。

<a id="r_a571753eb8aba5610fb7bc3546b7bfce9"></a>

```c
uint32_t mode
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[mode](#a571753eb8aba5610fb7bc3546b7bfce9)。

<a id="r_ac83072a87e0b29b30e6406f4f61cf26d"></a>

```c
uint32_t baudrate
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[baudrate](#ac83072a87e0b29b30e6406f4f61cf26d)。

<a id="r_a960fd4543476b89b56f23dd29774b196"></a>

```c
uint16_t in_proto_mask
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[in_proto_mask](#a960fd4543476b89b56f23dd29774b196)。

<a id="r_a1f4f3ab473e80648043b792bc4d5022f"></a>

```c
uint16_t out_proto_mask
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[out_proto_mask](#a1f4f3ab473e80648043b792bc4d5022f)。

<a id="r_a836be3302c1e038fbc09712242a51e69"></a>

```c
uint16_t flags
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[flags](#a836be3302c1e038fbc09712242a51e69)。

<a id="r_ad2bf468b82cc86ae1ce99c2fa129c231"></a>

```c
uint16_t reserved2
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[reserved2](#ad2bf468b82cc86ae1ce99c2fa129c231)。

## 59.2\_详细说明（Detailed Documentation）

<a id="ac83072a87e0b29b30e6406f4f61cf26d"></a>

### `baudrate`

```c
uint32_t ubx_cfg_prt::baudrate
```

<a id="a836be3302c1e038fbc09712242a51e69"></a>

### `flags`

```c
uint16_t ubx_cfg_prt::flags
```

<a id="a960fd4543476b89b56f23dd29774b196"></a>

### `in_proto_mask`

```c
uint16_t ubx_cfg_prt::in_proto_mask
```

<a id="a571753eb8aba5610fb7bc3546b7bfce9"></a>

### `mode`

```c
uint32_t ubx_cfg_prt::mode
```

<a id="a1f4f3ab473e80648043b792bc4d5022f"></a>

### `out_proto_mask`

```c
uint16_t ubx_cfg_prt::out_proto_mask
```

<a id="af5a445ab598a2b93e884c916fe13affc"></a>

### `port_id`

```c
uint8_t ubx_cfg_prt::port_id
```

<a id="aba6bef46b7818a2396b77a0b1245ecc5"></a>

### `reserved1`

```c
uint8_t ubx_cfg_prt::reserved1
```

<a id="ad2bf468b82cc86ae1ce99c2fa129c231"></a>

### `reserved2`

```c
uint16_t ubx_cfg_prt::reserved2
```

<a id="a1d4df224a3a9e7e6031a418745ee4e95"></a>

### `rx_ready_pin`

```c
uint16_t ubx_cfg_prt::rx_ready_pin
```

本数据类型文档由以下文件生成：

- `zephyr/modem/ubx/protocol.h`

## 59.3\_原页交叉引用（Cross References）

- [zephyr/modem/ubx/protocol.h](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2protocol_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P058_ubx_cfg_nav5_结构体.md) · [返回大纲](大纲.md) · [下一章](P060_ubx_cfg_rate_结构体.md)
