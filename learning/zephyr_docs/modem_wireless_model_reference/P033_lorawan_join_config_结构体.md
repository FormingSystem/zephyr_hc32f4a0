---
id: learning.zephyr-docs.modem-wireless-model-reference.page-33
title: lorawan_join_config_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structlorawan__join__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第33章\_lorawan\_join\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structlorawan__join__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

LoRaWAN入网参数（Join Parameters）。

```c
#include <zephyr/lorawan/lorawan.h>
```

<a id="details"></a>

LoRaWAN入网参数（Join Parameters）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 33.1\_数据成员（Data Fields）

```c
union {
```

<a id="r_a4f5c89a2395b8c16875120e45a44209f"></a>

```c
struct lorawan_join_otaa otaa
```

相关声明：[lorawan_join_otaa](P034_lorawan_join_otaa_结构体.md)、[otaa](#a7e2db9310308b59f652d72a3d7b3f7ff)。

空中激活（OTAA）入网参数。

<a id="r_ae655789e4e02bb9bb7f04dc1aa80038c"></a>

```c
struct lorawan_join_abp abp
```

相关声明：[lorawan_join_abp](P032_lorawan_join_abp_结构体.md)、[abp](#a0b44703df9ebe466ccf1d7744138daee)。

个性化激活（ABP）入网参数。

<a id="r_ab359c2a358c27c620d40ed92559d13da"></a>

```c
};
```

入网参数（Join parameters）。

<a id="r_af5c973ed774255858b2219f737a3fe0a"></a>

```c
uint8_t * dev_eui
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[dev_eui](#af5c973ed774255858b2219f737a3fe0a)。

设备扩展唯一标识符（Device EUI）。

<a id="r_a9dbe39641f878e4c997a16711fdb5585"></a>

```c
enum lorawan_act_type mode
```

相关声明：[lorawan_act_type](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga2bf50442214ecdc717f1a24dc058a338)、[mode](#a9dbe39641f878e4c997a16711fdb5585)。

激活模式（Activation mode）。

## 33.2\_详细说明（Detailed Documentation）

<a id="ab359c2a358c27c620d40ed92559d13da"></a>

### `[union]`

```c
union { ... } lorawan_join_config
```

入网参数（Join parameters）。

<a id="a0b44703df9ebe466ccf1d7744138daee"></a>

### `abp`

```c
struct lorawan_join_abp lorawan_join_config::abp
```

个性化激活（ABP）入网参数。

<a id="af5c973ed774255858b2219f737a3fe0a"></a>

### `dev_eui`

```c
uint8_t* lorawan_join_config::dev_eui
```

设备扩展唯一标识符（Device EUI）。

存在安全元件（secure element）时为可选项。

<a id="a9dbe39641f878e4c997a16711fdb5585"></a>

### `mode`

```c
enum lorawan_act_type lorawan_join_config::mode
```

激活模式（Activation mode）。

<a id="a7e2db9310308b59f652d72a3d7b3f7ff"></a>

### `otaa`

```c
struct lorawan_join_otaa lorawan_join_config::otaa
```

空中激活（OTAA）入网参数。

本数据类型文档由以下文件生成：

- `zephyr/lorawan/lorawan.h`

## 33.3\_原页交叉引用（Cross References）

- [zephyr/lorawan/lorawan.h](https://docs.zephyrproject.org/latest/doxygen/html/lorawan_8h_source.html)
- [lorawan_join_otaa](P034_lorawan_join_otaa_结构体.md)
- [lorawan_join_abp](P032_lorawan_join_abp_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [lorawan_act_type](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga2bf50442214ecdc717f1a24dc058a338)
- [lorawan_join_config](P033_lorawan_join_config_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P032_lorawan_join_abp_结构体.md) · [返回大纲](大纲.md) · [下一章](P034_lorawan_join_otaa_结构体.md)
