---
id: learning.zephyr-docs.platform-security-model-reference.page-46
title: scmi_power_state_config_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structscmi__power__state__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第46章\_scmi\_power\_state\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structscmi__power__state__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

描述POWER_STATE_SET命令的参数。

```c
#include <zephyr/drivers/firmware/scmi/power.h>
```

<a id="details"></a>

描述POWER_STATE_SET命令的参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 46.1\_数据成员（Data Fields）

<a id="r_a83743ab1270c319ab62148e2cf89741f"></a>

```c
uint32_t flags
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[flags](#a83743ab1270c319ab62148e2cf89741f)。

请求标志，参见 `SCMI_POWER_STATE_SET_FLAGS_*`。

<a id="r_ae246faf5674e4d885d84e8ee782cccae"></a>

```c
uint32_t domain_id
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[domain_id](#ae246faf5674e4d885d84e8ee782cccae)。

待配置电源域的 ID。

<a id="r_a742409967c5487aecbccf89347dd7ae4"></a>

```c
uint32_t power_state
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[power_state](#a742409967c5487aecbccf89347dd7ae4)。

要设置的电源状态，参见 `SCMI_POWER_STATE_PARAM`。

## 46.2\_详细说明（Detailed Documentation）

<a id="ae246faf5674e4d885d84e8ee782cccae"></a>

### `domain_id`

```c
uint32_t scmi_power_state_config::domain_id
```

待配置电源域的 ID。

<a id="a83743ab1270c319ab62148e2cf89741f"></a>

### `flags`

```c
uint32_t scmi_power_state_config::flags
```

请求标志，参见 `SCMI_POWER_STATE_SET_FLAGS_*`。

<a id="a742409967c5487aecbccf89347dd7ae4"></a>

### `power_state`

```c
uint32_t scmi_power_state_config::power_state
```

要设置的电源状态，参见 `SCMI_POWER_STATE_PARAM`。

本数据类型文档由以下文件生成：

- `zephyr/drivers/firmware/scmi/power.h`

## 46.3\_原页交叉引用（Cross References）

- [zephyr/drivers/firmware/scmi/power.h](https://docs.zephyrproject.org/latest/doxygen/html/power_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [SCMI_POWER_STATE_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__power.html#ga9765bcc859e9f4f550d6f4974d154eab)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P045_scmi_platform_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P047_scmi_protocol_结构体.md)
