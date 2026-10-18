---
id: learning.zephyr-docs.platform-security-model-reference.page-2
title: dw_ace_v1_ictl_driver_api_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structdw__ace__v1__ictl__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_dw\_ace\_v1\_ictl\_driver\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structdw__ace__v1__ictl__driver__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/drivers/interrupt_controller/dw_ace.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 2.1\_数据成员（Data Fields）

<a id="r_aa7984ba6960a07a33ae0746717bc45ac"></a>

```c
irq_enable_t intr_enable
```

相关声明：[irq_enable_t](https://docs.zephyrproject.org/latest/doxygen/html/dw__ace_8h.html#a99f66a0736502ea18deb13e0a5d9958e)、[intr_enable](#aa7984ba6960a07a33ae0746717bc45ac)。

<a id="r_a549b3e3c36f4bd632ab52ec4eee5fd80"></a>

```c
irq_disable_t intr_disable
```

相关声明：[irq_disable_t](https://docs.zephyrproject.org/latest/doxygen/html/dw__ace_8h.html#a1e71aa00761ed1a478f92de8a1342564)、[intr_disable](#a549b3e3c36f4bd632ab52ec4eee5fd80)。

<a id="r_ac2bbb8a07be14882b6763e58bf79be43"></a>

```c
irq_is_enabled_t intr_is_enabled
```

相关声明：[irq_is_enabled_t](https://docs.zephyrproject.org/latest/doxygen/html/dw__ace_8h.html#af94ebd4f440b084d94d42eed62e159cc)、[intr_is_enabled](#ac2bbb8a07be14882b6763e58bf79be43)。

## 2.2\_详细说明（Detailed Documentation）

<a id="a549b3e3c36f4bd632ab52ec4eee5fd80"></a>

### `intr_disable`

```c
irq_disable_t dw_ace_v1_ictl_driver_api::intr_disable
```

<a id="aa7984ba6960a07a33ae0746717bc45ac"></a>

### `intr_enable`

```c
irq_enable_t dw_ace_v1_ictl_driver_api::intr_enable
```

<a id="ac2bbb8a07be14882b6763e58bf79be43"></a>

### `intr_is_enabled`

```c
irq_is_enabled_t dw_ace_v1_ictl_driver_api::intr_is_enabled
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/interrupt_controller/dw_ace.h`

## 2.3\_原页交叉引用（Cross References）

- [zephyr/drivers/interrupt_controller/dw_ace.h](https://docs.zephyrproject.org/latest/doxygen/html/dw__ace_8h_source.html)
- [irq_enable_t](https://docs.zephyrproject.org/latest/doxygen/html/dw__ace_8h.html#a99f66a0736502ea18deb13e0a5d9958e)
- [irq_disable_t](https://docs.zephyrproject.org/latest/doxygen/html/dw__ace_8h.html#a1e71aa00761ed1a478f92de8a1342564)
- [irq_is_enabled_t](https://docs.zephyrproject.org/latest/doxygen/html/dw__ace_8h.html#af94ebd4f440b084d94d42eed62e159cc)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P001_child_interrupt_callback_结构体.md) · [返回大纲](大纲.md) · [下一章](P003_edac_nxp_callback_data_结构体.md)
