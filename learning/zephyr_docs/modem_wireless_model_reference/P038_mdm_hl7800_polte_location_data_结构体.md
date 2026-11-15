---
id: learning.zephyr-docs.modem-wireless-model-reference.page-38
title: mdm_hl7800_polte_location_data_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmdm__hl7800__polte__location__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第38章\_mdm\_hl7800\_polte\_location\_data\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmdm__hl7800__polte__location__data.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

PoLTE定位响应（Location Response）。

```c
#include <zephyr/drivers/modem/hl7800.h>
```

<a id="details"></a>

PoLTE定位响应（Location Response）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 38.1\_数据成员（Data Fields）

<a id="r_aaae6d4f0ff600f595bad143166f5605c"></a>

```c
uint32_t timestamp
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[timestamp](#aaae6d4f0ff600f595bad143166f5605c)。

位置响应的时间戳。

<a id="r_a3a95fb87ddf47eb9d447b9dd0da92cf3"></a>

```c
int status
```

相关声明：[status](#a3a95fb87ddf47eb9d447b9dd0da92cf3)。

负值表示 `errno`，0 表示成功，正值表示服务器返回的错误码。

<a id="r_adc4a7aee1014c0290294240bd968e232"></a>

```c
char latitude [33]
```

相关声明：[latitude](#adc4a7aee1014c0290294240bd968e232)。

纬度（Latitude）。

<a id="r_a5114024090c7d039d63219495d9fd343"></a>

```c
char longitude [33]
```

相关声明：[longitude](#a5114024090c7d039d63219495d9fd343)。

经度（Longitude）。

<a id="r_a479ebd4268c0138138d62818b96a1593"></a>

```c
char confidence_in_meters [33]
```

相关声明：[confidence_in_meters](#a479ebd4268c0138138d62818b96a1593)。

位置置信范围（Location confidence），单位为米。

## 38.2\_详细说明（Detailed Documentation）

<a id="a479ebd4268c0138138d62818b96a1593"></a>

### `confidence_in_meters`

```c
char mdm_hl7800_polte_location_data::confidence_in_meters[33]
```

位置置信范围（Location confidence），单位为米。

<a id="adc4a7aee1014c0290294240bd968e232"></a>

### `latitude`

```c
char mdm_hl7800_polte_location_data::latitude[33]
```

纬度（Latitude）。

<a id="a5114024090c7d039d63219495d9fd343"></a>

### `longitude`

```c
char mdm_hl7800_polte_location_data::longitude[33]
```

经度（Longitude）。

<a id="a3a95fb87ddf47eb9d447b9dd0da92cf3"></a>

### `status`

```c
int mdm_hl7800_polte_location_data::status
```

负值表示 `errno`，0 表示成功，正值表示服务器返回的错误码。

`status` 非零时，其他成员无效。

<a id="aaae6d4f0ff600f595bad143166f5605c"></a>

### `timestamp`

```c
uint32_t mdm_hl7800_polte_location_data::timestamp
```

位置响应的时间戳。

本数据类型文档由以下文件生成：

- `zephyr/drivers/modem/hl7800.h`

## 38.3\_原页交叉引用（Cross References）

- [zephyr/drivers/modem/hl7800.h](https://docs.zephyrproject.org/latest/doxygen/html/hl7800_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P037_mdm_hl7800_compound_event_结构体.md) · [返回大纲](大纲.md) · [下一章](P039_mdm_hl7800_polte_registration_event_data_结构体.md)
