---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-23
title: bt_conn_le_info_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__le__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第23章\_bt\_conn\_le\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__le__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

LE 连接信息结构体。

```c
#include <zephyr/bluetooth/conn.h>
```

<a id="details"></a>

LE 连接信息结构体。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 23.1\_数据成员（Data Fields）

<a id="r_a5f1eacec82f31182460d6d5359a8b295"></a>

```c
const bt_addr_le_t * src
```

相关声明：[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[src](#a5f1eacec82f31182460d6d5359a8b295)。

源端，即本地身份地址（Source／Local Identity Address）。

<a id="r_a1f78e1c0ed3482ce6eec9ce6eeda4769"></a>

```c
const bt_addr_le_t * dst
```

相关声明：[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[dst](#a1f78e1c0ed3482ce6eec9ce6eeda4769)。

目的端，即远端身份地址（Destination／Remote Identity Address）；在身份解析完成前，为远端可解析私有地址（Resolvable Private Address，RPA）。

<a id="r_a3be5df0deb0af08f84843eb3c6a5e5ae"></a>

```c
const bt_addr_le_t * local
```

相关声明：[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[local](#a3be5df0deb0af08f84843eb3c6a5e5ae)。

建立连接时使用的本地设备地址（Local device address）。

<a id="r_a236d1c97c735c7cfaead0b1a3672d512"></a>

```c
const bt_addr_le_t * remote
```

相关声明：[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[remote](#a236d1c97c735c7cfaead0b1a3672d512)。

建立连接时使用的远端设备地址（Remote device address）。

<a id="r_a3bede29a6a5df282bde6a26f50ea9aee"></a>

```c
uint32_t interval_us
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[interval_us](#a3bede29a6a5df282bde6a26f50ea9aee)。

连接间隔（Connection interval），单位为微秒。

```c
union {
```

<a id="r_ab1dd14de238f3edc9269ce059b355971"></a>

```c
uint16_t interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[interval](#a95a1f635e53f16d5839cdd58f4bda962)。

连接间隔（Connection interval），以 1.25 毫秒为单位。

<a id="r_ac54576bd1722433ace425a4488aa7e77"></a>

```c
};
```

<a id="r_acd83835fe5ec0878fd653b87cb570a49"></a>

```c
uint16_t latency
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[latency](#acd83835fe5ec0878fd653b87cb570a49)。

连接外设延迟（Connection peripheral latency）。

<a id="r_afb4dc594d063fbbad2bcd4acf047f716"></a>

```c
uint16_t timeout
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[timeout](#afb4dc594d063fbbad2bcd4acf047f716)。

连接监督超时（Connection supervision timeout）。

<a id="r_a215d39c6cd7da1ac033529b5541cbfc1"></a>

```c
const struct bt_conn_le_phy_info * phy
```

相关声明：[bt_conn_le_phy_info](P028_bt_conn_le_phy_info_结构体.md)、[phy](#a215d39c6cd7da1ac033529b5541cbfc1)。

连接物理层信息（Connection PHY info）。

<a id="r_ae309f390c8d7b33a4de55791af235ab0"></a>

```c
const struct bt_conn_le_data_len_info * data_len
```

相关声明：[bt_conn_le_data_len_info](P019_bt_conn_le_data_len_info_结构体.md)、[data_len](#ae309f390c8d7b33a4de55791af235ab0)。

连接的最大单片段参数（Maximum single fragment parameters）。

<a id="r_a5d97a2eb4aa880abe857f19adeea425d"></a>

```c
const struct bt_conn_le_subrating_info * subrate
```

相关声明：[bt_conn_le_subrating_info](P034_bt_conn_le_subrating_info_结构体.md)、[subrate](#a5d97a2eb4aa880abe857f19adeea425d)。

连接子速率参数（Connection subrating parameters）。

## 23.2\_详细说明（Detailed Documentation）

<a id="ac54576bd1722433ace425a4488aa7e77"></a>

### `[union]`

```c
union { ... } bt_conn_le_info
```

<a id="ae309f390c8d7b33a4de55791af235ab0"></a>

### `data_len`

```c
const struct bt_conn_le_data_len_info* bt_conn_le_info::data_len
```

连接的最大单片段参数（Maximum single fragment parameters）。

<a id="a1f78e1c0ed3482ce6eec9ce6eeda4769"></a>

### `dst`

```c
const bt_addr_le_t* bt_conn_le_info::dst
```

目的端，即远端身份地址（Destination／Remote Identity Address）；在身份解析完成前，为远端可解析私有地址（Resolvable Private Address，RPA）。

<a id="a95a1f635e53f16d5839cdd58f4bda962"></a>

### `interval`

```c
uint16_t bt_conn_le_info::interval
```

连接间隔（Connection interval），以 1.25 毫秒为单位。

**已弃用（Deprecated）**：已弃用（Deprecated）：改用 `bt_conn_le_info::interval_us`。

<a id="a3bede29a6a5df282bde6a26f50ea9aee"></a>

### `interval_us`

```c
uint32_t bt_conn_le_info::interval_us
```

连接间隔（Connection interval），单位为微秒。

<a id="acd83835fe5ec0878fd653b87cb570a49"></a>

### `latency`

```c
uint16_t bt_conn_le_info::latency
```

连接外设延迟（Connection peripheral latency）。

<a id="a3be5df0deb0af08f84843eb3c6a5e5ae"></a>

### `local`

```c
const bt_addr_le_t* bt_conn_le_info::local
```

建立连接时使用的本地设备地址（Local device address）。

<a id="a215d39c6cd7da1ac033529b5541cbfc1"></a>

### `phy`

```c
const struct bt_conn_le_phy_info* bt_conn_le_info::phy
```

连接物理层信息（Connection PHY info）。

<a id="a236d1c97c735c7cfaead0b1a3672d512"></a>

### `remote`

```c
const bt_addr_le_t* bt_conn_le_info::remote
```

建立连接时使用的远端设备地址（Remote device address）。

<a id="a5f1eacec82f31182460d6d5359a8b295"></a>

### `src`

```c
const bt_addr_le_t* bt_conn_le_info::src
```

源端，即本地身份地址（Source／Local Identity Address）。

<a id="a5d97a2eb4aa880abe857f19adeea425d"></a>

### `subrate`

```c
const struct bt_conn_le_subrating_info* bt_conn_le_info::subrate
```

连接子速率参数（Connection subrating parameters）。

<a id="afb4dc594d063fbbad2bcd4acf047f716"></a>

### `timeout`

```c
uint16_t bt_conn_le_info::timeout
```

连接监督超时（Connection supervision timeout）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/conn.h`

## 23.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h_source.html)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_conn_le_phy_info](P028_bt_conn_le_phy_info_结构体.md)
- [bt_conn_le_data_len_info](P019_bt_conn_le_data_len_info_结构体.md)
- [bt_conn_le_subrating_info](P034_bt_conn_le_subrating_info_结构体.md)
- [bt_conn_le_info](P023_bt_conn_le_info_结构体.md)
- [Deprecated](https://docs.zephyrproject.org/latest/doxygen/html/deprecated.html#_deprecated000134)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P022_bt_conn_le_frame_space_updated_结构体.md) · [返回大纲](大纲.md) · [下一章](P024_bt_conn_le_min_conn_interval_group_结构体.md)
