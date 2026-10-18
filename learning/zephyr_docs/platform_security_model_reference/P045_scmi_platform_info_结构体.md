---
id: learning.zephyr-docs.platform-security-model-reference.page-45
title: scmi_platform_info_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structscmi__platform__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第45章\_scmi\_platform\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structscmi__platform__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

系统控制与管理接口（SCMI）基础协议的修订版本信息。

```c
#include <zephyr/drivers/firmware/scmi/base.h>
```

<a id="details"></a>

系统控制与管理接口（SCMI）基础协议的修订版本信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 45.1\_数据成员（Data Fields）

<a id="r_aa06c3dd53958c3cbe389f682b5ded16c"></a>

```c
uint8_t num_protocols
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_protocols](#aa06c3dd53958c3cbe389f682b5ded16c)。

已实现的协议数量，不包括基础协议（Base protocol）。

<a id="r_ade42f3a6c6e97bce2695072a39ec21bd"></a>

```c
uint8_t num_agents
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_agents](#ade42f3a6c6e97bce2695072a39ec21bd)。

系统中的代理（Agent）数量。

<a id="r_ae6327a38864e1247b382a76259562c92"></a>

```c
uint32_t impl_ver
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[impl_ver](#ae6327a38864e1247b382a76259562c92)。

供应商特定的实现版本。

<a id="r_a550fb1e5b313df82e7ad54741228abb6"></a>

```c
char vendor_id [16]
```

相关声明：[vendor_id](#a550fb1e5b313df82e7ad54741228abb6)。

供应商标识符（Vendor identifier）。

<a id="r_a050a3fb299aa893da67e32874b565d20"></a>

```c
char sub_vendor_id [16]
```

相关声明：[sub_vendor_id](#a050a3fb299aa893da67e32874b565d20)。

子供应商标识符（Sub-vendor identifier）。

## 45.2\_详细说明（Detailed Documentation）

<a id="ae6327a38864e1247b382a76259562c92"></a>

### `impl_ver`

```c
uint32_t scmi_platform_info::impl_ver
```

供应商特定的实现版本。

<a id="ade42f3a6c6e97bce2695072a39ec21bd"></a>

### `num_agents`

```c
uint8_t scmi_platform_info::num_agents
```

系统中的代理（Agent）数量。

<a id="aa06c3dd53958c3cbe389f682b5ded16c"></a>

### `num_protocols`

```c
uint8_t scmi_platform_info::num_protocols
```

已实现的协议数量，不包括基础协议（Base protocol）。

<a id="a050a3fb299aa893da67e32874b565d20"></a>

### `sub_vendor_id`

```c
char scmi_platform_info::sub_vendor_id[16]
```

子供应商标识符（Sub-vendor identifier）。

<a id="a550fb1e5b313df82e7ad54741228abb6"></a>

### `vendor_id`

```c
char scmi_platform_info::vendor_id[16]
```

供应商标识符（Vendor identifier）。

本数据类型文档由以下文件生成：

- `zephyr/drivers/firmware/scmi/base.h`

## 45.3\_原页交叉引用（Cross References）

- [zephyr/drivers/firmware/scmi/base.h](https://docs.zephyrproject.org/latest/doxygen/html/base_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P044_scmi_pinctrl_settings_结构体.md) · [返回大纲](大纲.md) · [下一章](P046_scmi_power_state_config_结构体.md)
