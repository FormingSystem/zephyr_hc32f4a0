---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-32
title: mctp_usb_class_inst_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmctp__usb__class__inst.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第32章\_mctp\_usb\_class\_inst\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmctp__usb__class__inst.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

管理组件传输协议（MCTP）的USB类实例配置。

```c
#include <zephyr/pmci/mctp/mctp_usb.h>
```

<a id="details"></a>

MCTP USB 类实例配置（Class instance configuration）。保存单个 MCTP USB 类实例的 USB 接口描述符参数，以及关联的 MCTP 总线绑定。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 32.1\_数据成员（Data Fields）

<a id="r_a72a792cb05ef8d7ebdf0c97a6f371828"></a>

```c
uint8_t subclass
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[subclass](#a72a792cb05ef8d7ebdf0c97a6f371828)。

USB 接口描述符中使用的 MCTP 子类（Subclass）。

<a id="r_a8c93e48357b67467b729f111d7dc484d"></a>

```c
uint8_t mctp_protocol
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mctp_protocol](#a8c93e48357b67467b729f111d7dc484d)。

USB 接口描述符中使用的 MCTP 协议版本。

<a id="r_aa436a766a2d3c4a29b64bed4fc86a099"></a>

```c
struct mctp_binding_usb * mctp_binding
```

相关声明：[mctp_binding_usb](P031_mctp_binding_usb_结构体.md)、[mctp_binding](#aa436a766a2d3c4a29b64bed4fc86a099)。

指向关联 MCTP USB 总线绑定的指针。

## 32.2\_详细说明（Detailed Documentation）

<a id="aa436a766a2d3c4a29b64bed4fc86a099"></a>

### `mctp_binding`

```c
struct mctp_binding_usb* mctp_usb_class_inst::mctp_binding
```

指向关联 MCTP USB 总线绑定的指针。

<a id="a8c93e48357b67467b729f111d7dc484d"></a>

### `mctp_protocol`

```c
uint8_t mctp_usb_class_inst::mctp_protocol
```

USB 接口描述符中使用的 MCTP 协议版本。

<a id="a72a792cb05ef8d7ebdf0c97a6f371828"></a>

### `subclass`

```c
uint8_t mctp_usb_class_inst::subclass
```

USB 接口描述符中使用的 MCTP 子类（Subclass）。

本数据类型文档由以下文件生成：

- `zephyr/pmci/mctp/mctp_usb.h`

## 32.3\_原页交叉引用（Cross References）

- [zephyr/pmci/mctp/mctp_usb.h](https://docs.zephyrproject.org/latest/doxygen/html/mctp__usb_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mctp_binding_usb](P031_mctp_binding_usb_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P031_mctp_binding_usb_结构体.md) · [返回大纲](大纲.md) · [下一章](P033_memc_driver_api_结构体.md)
