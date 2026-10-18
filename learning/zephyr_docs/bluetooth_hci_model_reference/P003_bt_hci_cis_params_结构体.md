---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-3
title: bt_hci_cis_params_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cis__params.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_bt\_hci\_cis\_params\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cis__params.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 3.1\_数据成员（Data Fields）

<a id="r_a6dcfca11d7f827b1b7a62b507620d4de"></a>

```c
uint8_t cis_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cis_id](#a6dcfca11d7f827b1b7a62b507620d4de)。

<a id="r_a8a85b914ba5585c6b362da3deb8d42d9"></a>

```c
uint16_t c_sdu
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[c_sdu](#a8a85b914ba5585c6b362da3deb8d42d9)。

<a id="r_ae2bffbaf0c4dde9144a7887177b3ffdb"></a>

```c
uint16_t p_sdu
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[p_sdu](#ae2bffbaf0c4dde9144a7887177b3ffdb)。

<a id="r_a5a5fcd9276d912446fe84d875ae74c2f"></a>

```c
uint8_t c_phy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[c_phy](#a5a5fcd9276d912446fe84d875ae74c2f)。

<a id="r_a18bc8e4b531d9fd16f18e10a0d931f6c"></a>

```c
uint8_t p_phy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[p_phy](#a18bc8e4b531d9fd16f18e10a0d931f6c)。

<a id="r_aa7fa628692f959db63788c6580cc5c66"></a>

```c
uint8_t c_rtn
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[c_rtn](#aa7fa628692f959db63788c6580cc5c66)。

<a id="r_ad55e197ccb70c83fcd4c1c6ba485f468"></a>

```c
uint8_t p_rtn
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[p_rtn](#ad55e197ccb70c83fcd4c1c6ba485f468)。

## 3.2\_详细说明（Detailed Documentation）

<a id="a5a5fcd9276d912446fe84d875ae74c2f"></a>

### `c_phy`

```c
uint8_t bt_hci_cis_params::c_phy
```

<a id="aa7fa628692f959db63788c6580cc5c66"></a>

### `c_rtn`

```c
uint8_t bt_hci_cis_params::c_rtn
```

<a id="a8a85b914ba5585c6b362da3deb8d42d9"></a>

### `c_sdu`

```c
uint16_t bt_hci_cis_params::c_sdu
```

<a id="a6dcfca11d7f827b1b7a62b507620d4de"></a>

### `cis_id`

```c
uint8_t bt_hci_cis_params::cis_id
```

<a id="a18bc8e4b531d9fd16f18e10a0d931f6c"></a>

### `p_phy`

```c
uint8_t bt_hci_cis_params::p_phy
```

<a id="ad55e197ccb70c83fcd4c1c6ba485f468"></a>

### `p_rtn`

```c
uint8_t bt_hci_cis_params::p_rtn
```

<a id="ae2bffbaf0c4dde9144a7887177b3ffdb"></a>

### `p_sdu`

```c
uint16_t bt_hci_cis_params::p_sdu
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 3.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P002_bt_hci_cis_结构体.md) · [返回大纲](大纲.md) · [下一章](P004_bt_hci_cis_params_test_结构体.md)
