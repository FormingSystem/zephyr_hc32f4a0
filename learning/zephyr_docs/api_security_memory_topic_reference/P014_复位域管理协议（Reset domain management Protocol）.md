---
id: learning.zephyr-docs.api-security-memory-topic-reference.page-14
title: 复位域管理协议（Reset domain management Protocol）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__reset.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_复位域管理协议（Reset domain management Protocol）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__reset.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

通过 SCMI 进行复位域管理。

<a id="details"></a>

通过 SCMI 进行复位域管理。

<a id="header-files"></a>
<a id="files"></a>

## 14.1\_文件（Files）

<a id="r_reset_2Eh"></a>

```c
file reset.h
```

相关声明：[reset.h](../api_file_network_device_reference/P007_zephyr__drivers__firmware__scmi__reset.h_文件参考.md)。

系统控制与管理接口（SCMI）复位协议（Reset Protocol）的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 14.2\_数据结构（Data Structures）

<a id="r_scmi_5Freset_5Fdomain_5Fattr"></a>

```c
struct scmi_reset_domain_attr
```

相关声明：[scmi_reset_domain_attr](../platform_security_model_reference/P050_scmi_reset_domain_attr_结构体.md)。

系统控制与管理接口（SCMI）的复位域（Reset Domain）属性。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 14.3\_宏定义（Macros）

<a id="r_ga37c2d2e445ca154408714ac33a744026"></a>

```c
#define SCMI_RESET_ATTR_NUM_DOMAINS GENMASK(15, 0)
```

相关声明：[SCMI_RESET_ATTR_NUM_DOMAINS](#ga37c2d2e445ca154408714ac33a744026)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

`PROTOCOL_ATTRIBUTES` 报告中复位域数量（Number of Reset Domains）的掩码。

<a id="r_ga1f3645b121c17f59af4bbf65c58a5d3a"></a>

```c
#define SCMI_RESET_ATTR_GET_NUM_DOMAINS(attr)
```

相关声明：[SCMI_RESET_ATTR_GET_NUM_DOMAINS](#ga1f3645b121c17f59af4bbf65c58a5d3a)。

从协议属性（Protocol Attributes）中提取复位域数量。

<a id="r_ga07d62d1b8ca250b0e501486768b17ac0"></a>

```c
#define SCMI_RESET_AUTONOMOUS BIT(0)
```

相关声明：[SCMI_RESET_AUTONOMOUS](#ga07d62d1b8ca250b0e501486768b17ac0)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

自主复位标志（Autonomous Reset Flag）：必须由平台自主执行复位。

<a id="r_ga5ff99722e090ce5aeadc15150646e2cd"></a>

```c
#define SCMI_RESET_EXPLICIT_ASSERT BIT(1)
```

相关声明：[SCMI_RESET_EXPLICIT_ASSERT](#ga5ff99722e090ce5aeadc15150646e2cd)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

显式置位／解除标志（Explicit Assert/Deassert Flag）：显式置位复位信号。

<a id="r_gaf250227757a532df03f49c7be35aad2e"></a>

```c
#define SCMI_RESET_ASYNCHRONOUS_RESET BIT(2)
```

相关声明：[SCMI_RESET_ASYNCHRONOUS_RESET](#gaf250227757a532df03f49c7be35aad2e)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

异步复位标志（Asynchronous Reset Flag）：复位必须异步完成。

<a id="r_ga52224187c48e05e2f3ce6e40cbfdf748"></a>

```c
#define SCMI_RESET_ARCH_COLD_RESET 0
```

相关声明：[SCMI_RESET_ARCH_COLD_RESET](#ga52224187c48e05e2f3ce6e40cbfdf748)。

体系结构冷复位类型（Architectural Cold Reset Type）。

<a id="r_gace0e9bc4de3c67488e631370c76a1337"></a>

```c
#define SCMI_RESET_PROTOCOL_SUPPORTED_VERSION 0x30001
```

相关声明：[SCMI_RESET_PROTOCOL_SUPPORTED_VERSION](#gace0e9bc4de3c67488e631370c76a1337)。

支持的 SCMI 复位协议（Reset Protocol）版本。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 14.4\_函数（Functions）

<a id="r_gaa0d948bb949e0ef8066bccd243948044"></a>

```c
int scmi_reset_domain_get_attr (struct scmi_protocol *proto, uint32_t id, struct scmi_reset_domain_attr *dom_attr)
```

相关声明：[scmi_reset_domain_get_attr](#gaa0d948bb949e0ef8066bccd243948044)、[scmi_protocol](../platform_security_model_reference/P047_scmi_protocol_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[scmi_reset_domain_attr](../platform_security_model_reference/P050_scmi_reset_domain_attr_结构体.md)。

通过 SCMI 复位域协议获取复位域属性（Reset Domain Attributes）。

<a id="r_gab79cf3b45fec93a8eba5dd0d6377b21e"></a>

```c
int scmi_reset_domain (struct scmi_protocol *proto, uint32_t id, uint32_t flags, uint32_t reset_state)
```

相关声明：[scmi_reset_domain](#gab79cf3b45fec93a8eba5dd0d6377b21e)、[scmi_protocol](../platform_security_model_reference/P047_scmi_protocol_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

通过 SCMI 复位域协议复位指定域（Reset Domain）。

## 14.5\_详细说明（Detailed Documentation）

<a id="ga52224187c48e05e2f3ce6e40cbfdf748"></a>

### `SCMI_RESET_ARCH_COLD_RESET`

```c
#define SCMI_RESET_ARCH_COLD_RESET 0
```

```c
#include <zephyr/drivers/firmware/scmi/reset.h>
```

体系结构冷复位类型（Architectural Cold Reset Type）。

<a id="gaf250227757a532df03f49c7be35aad2e"></a>

### `SCMI_RESET_ASYNCHRONOUS_RESET`

```c
#define SCMI_RESET_ASYNCHRONOUS_RESET BIT(2)
```

```c
#include <zephyr/drivers/firmware/scmi/reset.h>
```

异步复位标志（Asynchronous Reset Flag）：复位必须异步完成。

<a id="ga1f3645b121c17f59af4bbf65c58a5d3a"></a>

### `SCMI_RESET_ATTR_GET_NUM_DOMAINS`

```c
#define SCMI_RESET_ATTR_GET_NUM_DOMAINS ( attr)
```

```c
#include <zephyr/drivers/firmware/scmi/reset.h>
```

展开值（Value）：

```c
FIELD_GET(SCMI_RESET_ATTR_NUM_DOMAINS, (attr))
```

从协议属性（Protocol Attributes）中提取复位域数量。

<a id="ga37c2d2e445ca154408714ac33a744026"></a>

### `SCMI_RESET_ATTR_NUM_DOMAINS`

```c
#define SCMI_RESET_ATTR_NUM_DOMAINS GENMASK(15, 0)
```

```c
#include <zephyr/drivers/firmware/scmi/reset.h>
```

`PROTOCOL_ATTRIBUTES` 报告中复位域数量（Number of Reset Domains）的掩码。

<a id="ga07d62d1b8ca250b0e501486768b17ac0"></a>

### `SCMI_RESET_AUTONOMOUS`

```c
#define SCMI_RESET_AUTONOMOUS BIT(0)
```

```c
#include <zephyr/drivers/firmware/scmi/reset.h>
```

自主复位标志（Autonomous Reset Flag）：必须由平台自主执行复位。

<a id="ga5ff99722e090ce5aeadc15150646e2cd"></a>

### `SCMI_RESET_EXPLICIT_ASSERT`

```c
#define SCMI_RESET_EXPLICIT_ASSERT BIT(1)
```

```c
#include <zephyr/drivers/firmware/scmi/reset.h>
```

显式置位／解除标志（Explicit Assert/Deassert Flag）：显式置位复位信号。

<a id="gace0e9bc4de3c67488e631370c76a1337"></a>

### `SCMI_RESET_PROTOCOL_SUPPORTED_VERSION`

```c
#define SCMI_RESET_PROTOCOL_SUPPORTED_VERSION 0x30001
```

```c
#include <zephyr/drivers/firmware/scmi/reset.h>
```

支持的 SCMI 复位协议（Reset Protocol）版本。

<a id="gab79cf3b45fec93a8eba5dd0d6377b21e"></a>

### `scmi_reset_domain()`

```c
int scmi_reset_domain ( struct scmi_protocol * proto, uint32_t id, uint32_t flags, uint32_t reset_state )
```

```c
#include <zephyr/drivers/firmware/scmi/reset.h>
```

通过 SCMI 复位域协议复位指定域（Reset Domain）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `proto` | 指向 SCMI 时钟协议（Clock Protocol）数据的指针。 |
| `id` | 本次查询所针对的复位域标识（Reset Domain ID）。 |
| `flags` | 本次请求专用的附加条件和要求。 |
| `reset_state` | 请求的复位状态（Reset State）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。

<a id="gaa0d948bb949e0ef8066bccd243948044"></a>

### `scmi_reset_domain_get_attr()`

```c
int scmi_reset_domain_get_attr ( struct scmi_protocol * proto, uint32_t id, struct scmi_reset_domain_attr * dom_attr )
```

```c
#include <zephyr/drivers/firmware/scmi/reset.h>
```

通过 SCMI 复位域协议获取复位域属性（Reset Domain Attributes）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `proto` | 指向 SCMI 时钟协议（Clock Protocol）数据的指针。 |
| `id` | 本次查询所针对的复位域标识（Reset Domain ID）。 |
| `dom_attr` | 用于返回复位域标识属性（Reset Domain ID Attributes）的指针。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负值 `errno`。


## 14.6\_原页交叉引用（Cross References）

- [reset.h](../api_file_network_device_reference/P007_zephyr__drivers__firmware__scmi__reset.h_文件参考.md)
- [scmi_reset_domain_attr](../platform_security_model_reference/P050_scmi_reset_domain_attr_结构体.md)
- [GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [scmi_protocol](../platform_security_model_reference/P047_scmi_protocol_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [FIELD_GET](../api_file_reference/P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa49a456f06f7bdbedfcf3517e461947e)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__scmi__reset_html_ga37c2d2e445ca154408714ac33a744026"></a>
<a id="asilabs-pinctrl-siwx91x_8h_html_aa49a456f06f7bdbedfcf3517e461947e"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P013_电源域协议（Power Domain Protocol）.md) · [返回大纲](大纲.md) · [下一章](P015_SocketCAN 库.md)
