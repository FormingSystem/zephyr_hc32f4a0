---
id: learning.zephyr-docs.platform-security-model-reference.page-16
title: its_driver_api_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structits__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_its\_driver\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structits__driver__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/drivers/interrupt_controller/gicv3_its.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 16.1\_数据成员（Data Fields）

<a id="r_affc7190b95d16fa0223f6fd7b1ae9c14"></a>

```c
its_api_alloc_intid_t alloc_intid
```

相关声明：[its_api_alloc_intid_t](https://docs.zephyrproject.org/latest/doxygen/html/gicv3__its_8h.html#a49dff2553cbd48edc7057157d2ecb45d)、[alloc_intid](#affc7190b95d16fa0223f6fd7b1ae9c14)。

<a id="r_aa853404a1105b0cc4d1b6c976579ae4a"></a>

```c
its_api_setup_deviceid_t setup_deviceid
```

相关声明：[its_api_setup_deviceid_t](https://docs.zephyrproject.org/latest/doxygen/html/gicv3__its_8h.html#a39f4a213de953b77615b270f3ff13832)、[setup_deviceid](#aa853404a1105b0cc4d1b6c976579ae4a)。

<a id="r_a0a71be1a078b6e1a82624e0ef9a619ac"></a>

```c
its_api_map_intid_t map_intid
```

相关声明：[its_api_map_intid_t](https://docs.zephyrproject.org/latest/doxygen/html/gicv3__its_8h.html#a2642c1f7ecf45d404c17cdbcd824bb45)、[map_intid](#a0a71be1a078b6e1a82624e0ef9a619ac)。

<a id="r_aec4b32cea8d6c5fa2a59d2d25e6053cf"></a>

```c
its_api_send_int_t send_int
```

相关声明：[its_api_send_int_t](https://docs.zephyrproject.org/latest/doxygen/html/gicv3__its_8h.html#a26bf8d071e3cb856fc81d8911e942f5a)、[send_int](#aec4b32cea8d6c5fa2a59d2d25e6053cf)。

<a id="r_aa87bb10ac8f165c2acbc6033591b9aa8"></a>

```c
its_api_get_msi_addr_t get_msi_addr
```

相关声明：[its_api_get_msi_addr_t](https://docs.zephyrproject.org/latest/doxygen/html/gicv3__its_8h.html#add616700e3aeee952187ef96cb2d19c9)、[get_msi_addr](#aa87bb10ac8f165c2acbc6033591b9aa8)。

## 16.2\_详细说明（Detailed Documentation）

<a id="affc7190b95d16fa0223f6fd7b1ae9c14"></a>

### `alloc_intid`

```c
its_api_alloc_intid_t its_driver_api::alloc_intid
```

<a id="aa87bb10ac8f165c2acbc6033591b9aa8"></a>

### `get_msi_addr`

```c
its_api_get_msi_addr_t its_driver_api::get_msi_addr
```

<a id="a0a71be1a078b6e1a82624e0ef9a619ac"></a>

### `map_intid`

```c
its_api_map_intid_t its_driver_api::map_intid
```

<a id="aec4b32cea8d6c5fa2a59d2d25e6053cf"></a>

### `send_int`

```c
its_api_send_int_t its_driver_api::send_int
```

<a id="aa853404a1105b0cc4d1b6c976579ae4a"></a>

### `setup_deviceid`

```c
its_api_setup_deviceid_t its_driver_api::setup_deviceid
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/interrupt_controller/gicv3_its.h`

## 16.3\_原页交叉引用（Cross References）

- [zephyr/drivers/interrupt_controller/gicv3_its.h](https://docs.zephyrproject.org/latest/doxygen/html/gicv3__its_8h_source.html)
- [its_api_alloc_intid_t](https://docs.zephyrproject.org/latest/doxygen/html/gicv3__its_8h.html#a49dff2553cbd48edc7057157d2ecb45d)
- [its_api_setup_deviceid_t](https://docs.zephyrproject.org/latest/doxygen/html/gicv3__its_8h.html#a39f4a213de953b77615b270f3ff13832)
- [its_api_map_intid_t](https://docs.zephyrproject.org/latest/doxygen/html/gicv3__its_8h.html#a2642c1f7ecf45d404c17cdbcd824bb45)
- [its_api_send_int_t](https://docs.zephyrproject.org/latest/doxygen/html/gicv3__its_8h.html#a26bf8d071e3cb856fc81d8911e942f5a)
- [its_api_get_msi_addr_t](https://docs.zephyrproject.org/latest/doxygen/html/gicv3__its_8h.html#add616700e3aeee952187ef96cb2d19c9)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P015_intr_handle_data_t_结构体.md) · [返回大纲](大纲.md) · [下一章](P017_mcontext_t_结构体.md)
