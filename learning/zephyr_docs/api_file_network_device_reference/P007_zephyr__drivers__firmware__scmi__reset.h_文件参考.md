---
id: learning.zephyr-docs.api-file-network-device-reference.page-7
title: zephyr__drivers__firmware__scmi__reset.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2firmware_2scmi_2reset_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_zephyr\_\_drivers\_\_firmware\_\_scmi\_\_reset.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2firmware_2scmi_2reset_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

系统控制与管理接口（SCMI）复位协议（Reset Protocol）的头文件。

<a id="details"></a>

```c
#include <zephyr/drivers/firmware/scmi/protocol.h>
```

查看此文件的源码。

系统控制与管理接口（SCMI）复位协议（Reset Protocol）的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 7.1\_数据结构（Data Structures）

<a id="r_scmi_5Freset_5Fdomain_5Fattr"></a>

```c
struct scmi_reset_domain_attr
```

相关声明：[scmi_reset_domain_attr](../platform_security_model_reference/P050_scmi_reset_domain_attr_结构体.md)。

系统控制与管理接口（SCMI）的复位域（Reset Domain）属性。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 7.2\_宏定义（Macros）

<a id="r_ga37c2d2e445ca154408714ac33a744026"></a>

```c
#define SCMI_RESET_ATTR_NUM_DOMAINS GENMASK(15, 0)
```

相关声明：[SCMI_RESET_ATTR_NUM_DOMAINS](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__reset.html#ga37c2d2e445ca154408714ac33a744026)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

`PROTOCOL_ATTRIBUTES` 报告中复位域数量（Number of Reset Domains）的掩码。

<a id="r_ga1f3645b121c17f59af4bbf65c58a5d3a"></a>

```c
#define SCMI_RESET_ATTR_GET_NUM_DOMAINS(attr)
```

相关声明：[SCMI_RESET_ATTR_GET_NUM_DOMAINS](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__reset.html#ga1f3645b121c17f59af4bbf65c58a5d3a)。

从协议属性（Protocol Attributes）中提取复位域数量。

<a id="r_ga07d62d1b8ca250b0e501486768b17ac0"></a>

```c
#define SCMI_RESET_AUTONOMOUS BIT(0)
```

相关声明：[SCMI_RESET_AUTONOMOUS](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__reset.html#ga07d62d1b8ca250b0e501486768b17ac0)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

自主复位标志（Autonomous Reset Flag）：必须由平台自主执行复位。

<a id="r_ga5ff99722e090ce5aeadc15150646e2cd"></a>

```c
#define SCMI_RESET_EXPLICIT_ASSERT BIT(1)
```

相关声明：[SCMI_RESET_EXPLICIT_ASSERT](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__reset.html#ga5ff99722e090ce5aeadc15150646e2cd)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

显式置位／解除标志（Explicit Assert/Deassert Flag）：显式置位复位信号。

<a id="r_gaf250227757a532df03f49c7be35aad2e"></a>

```c
#define SCMI_RESET_ASYNCHRONOUS_RESET BIT(2)
```

相关声明：[SCMI_RESET_ASYNCHRONOUS_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__reset.html#gaf250227757a532df03f49c7be35aad2e)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

异步复位标志（Asynchronous Reset Flag）：复位必须异步完成。

<a id="r_ga52224187c48e05e2f3ce6e40cbfdf748"></a>

```c
#define SCMI_RESET_ARCH_COLD_RESET 0
```

相关声明：[SCMI_RESET_ARCH_COLD_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__reset.html#ga52224187c48e05e2f3ce6e40cbfdf748)。

体系结构冷复位类型（Architectural Cold Reset Type）。

<a id="r_gace0e9bc4de3c67488e631370c76a1337"></a>

```c
#define SCMI_RESET_PROTOCOL_SUPPORTED_VERSION 0x30001
```

相关声明：[SCMI_RESET_PROTOCOL_SUPPORTED_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__reset.html#gace0e9bc4de3c67488e631370c76a1337)。

支持的 SCMI 复位协议（Reset Protocol）版本。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 7.3\_函数（Functions）

<a id="r_gaa0d948bb949e0ef8066bccd243948044"></a>

```c
int scmi_reset_domain_get_attr (struct scmi_protocol *proto, uint32_t id, struct scmi_reset_domain_attr *dom_attr)
```

相关声明：[scmi_reset_domain_get_attr](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__reset.html#gaa0d948bb949e0ef8066bccd243948044)、[scmi_protocol](../platform_security_model_reference/P047_scmi_protocol_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[scmi_reset_domain_attr](../platform_security_model_reference/P050_scmi_reset_domain_attr_结构体.md)。

通过 SCMI 复位域协议获取复位域属性（Reset Domain Attributes）。

<a id="r_gab79cf3b45fec93a8eba5dd0d6377b21e"></a>

```c
int scmi_reset_domain (struct scmi_protocol *proto, uint32_t id, uint32_t flags, uint32_t reset_state)
```

相关声明：[scmi_reset_domain](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__reset.html#gab79cf3b45fec93a8eba5dd0d6377b21e)、[scmi_protocol](../platform_security_model_reference/P047_scmi_protocol_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

通过 SCMI 复位域协议复位指定域（Reset Domain）。


## 7.4\_原页交叉引用（Cross References）

- [zephyr/drivers/firmware/scmi/protocol.h](../api_source_reference/P156_protocol.h_源码浏览.md)
- [查看此文件的源码。](../api_source_configuration_reference/P019_reset.h_源码浏览.md)
- [scmi_reset_domain_attr](../platform_security_model_reference/P050_scmi_reset_domain_attr_结构体.md)
- [SCMI_RESET_ATTR_NUM_DOMAINS](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__reset.html#ga37c2d2e445ca154408714ac33a744026)
- [GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)
- [SCMI_RESET_ATTR_GET_NUM_DOMAINS](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__reset.html#ga1f3645b121c17f59af4bbf65c58a5d3a)
- [SCMI_RESET_AUTONOMOUS](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__reset.html#ga07d62d1b8ca250b0e501486768b17ac0)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [SCMI_RESET_EXPLICIT_ASSERT](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__reset.html#ga5ff99722e090ce5aeadc15150646e2cd)
- [SCMI_RESET_ASYNCHRONOUS_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__reset.html#gaf250227757a532df03f49c7be35aad2e)
- [SCMI_RESET_ARCH_COLD_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__reset.html#ga52224187c48e05e2f3ce6e40cbfdf748)
- [SCMI_RESET_PROTOCOL_SUPPORTED_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__reset.html#gace0e9bc4de3c67488e631370c76a1337)
- [scmi_reset_domain_get_attr](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__reset.html#gaa0d948bb949e0ef8066bccd243948044)
- [scmi_protocol](../platform_security_model_reference/P047_scmi_protocol_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [scmi_reset_domain](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__reset.html#gab79cf3b45fec93a8eba5dd0d6377b21e)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

<a id="header-details"></a>

---

[上一章](P006_zephyr__drivers__emul.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P008_zephyr__drivers__misc__nxp_rtxxx_dsp_ctrl__nxp_rtxxx_dsp_ctrl.h_文件参考.md)
