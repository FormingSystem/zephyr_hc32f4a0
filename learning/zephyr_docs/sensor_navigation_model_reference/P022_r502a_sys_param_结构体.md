---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-22
title: r502a_sys_param_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structr502a__sys__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第22章\_r502a\_sys\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structr502a__sys__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

系统参数（System Parameter）。

```c
#include <zephyr/drivers/sensor/grow_r502a.h>
```

<a id="details"></a>

系统参数（System parameter）。此结构体保存传感器状态寄存器及系统参数的值。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 22.1\_数据成员（Data Fields）

<a id="r_adb966712020f826ecc646c04a93edd5f"></a>

```c
uint16_t status_reg
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[status_reg](#adb966712020f826ecc646c04a93edd5f)。

状态寄存器（Status register）。

<a id="r_aaa11e04312322afa3f406f872763d8be"></a>

```c
uint16_t system_id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[system_id](#aaa11e04312322afa3f406f872763d8be)。

系统标识代码（System identifier code）。

<a id="r_a4cc85b5b8ec7a511f9fc5dd3912c0a39"></a>

```c
uint16_t lib_size
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[lib_size](#a4cc85b5b8ec7a511f9fc5dd3912c0a39)。

指纹库大小。

<a id="r_a076a36d66a6908eee2131a8f652fefa4"></a>

```c
uint16_t sec_level
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[sec_level](#a076a36d66a6908eee2131a8f652fefa4)。

安全级别（Security level），范围为 1 至 5。

<a id="r_ac3f2dc2456a29eeda55417ba91a29f62"></a>

```c
uint32_t addr
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[addr](#ac3f2dc2456a29eeda55417ba91a29f62)。

设备地址。

<a id="r_a8c3470762665d940a3ec2dc214150bf8"></a>

```c
uint16_t data_pkt_size
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[data_pkt_size](#a8c3470762665d940a3ec2dc214150bf8)。

数据包长度。

<a id="r_adf5a91c5972af06d1bf9beb6a9040bac"></a>

```c
uint32_t baud
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[baud](#adf5a91c5972af06d1bf9beb6a9040bac)。

波特率（Baud rate）。

## 22.2\_详细说明（Detailed Documentation）

<a id="ac3f2dc2456a29eeda55417ba91a29f62"></a>

### `addr`

```c
uint32_t r502a_sys_param::addr
```

设备地址。

<a id="adf5a91c5972af06d1bf9beb6a9040bac"></a>

### `baud`

```c
uint32_t r502a_sys_param::baud
```

波特率（Baud rate）。

<a id="a8c3470762665d940a3ec2dc214150bf8"></a>

### `data_pkt_size`

```c
uint16_t r502a_sys_param::data_pkt_size
```

数据包长度。

<a id="a4cc85b5b8ec7a511f9fc5dd3912c0a39"></a>

### `lib_size`

```c
uint16_t r502a_sys_param::lib_size
```

指纹库大小。

<a id="a076a36d66a6908eee2131a8f652fefa4"></a>

### `sec_level`

```c
uint16_t r502a_sys_param::sec_level
```

安全级别（Security level），范围为 1 至 5。

<a id="adb966712020f826ecc646c04a93edd5f"></a>

### `status_reg`

```c
uint16_t r502a_sys_param::status_reg
```

状态寄存器（Status register）。

<a id="aaa11e04312322afa3f406f872763d8be"></a>

### `system_id`

```c
uint16_t r502a_sys_param::system_id
```

系统标识代码（System identifier code）。

本数据类型文档由以下文件生成：

- `zephyr/drivers/sensor/grow_r502a.h`

## 22.3\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor/grow_r502a.h](https://docs.zephyrproject.org/latest/doxygen/html/grow__r502a_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P021_nmea_match_gst_data_结构体.md) · [返回大纲](大纲.md) · [下一章](P023_r502a_template_结构体.md)
