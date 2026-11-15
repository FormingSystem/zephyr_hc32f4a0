---
id: learning.zephyr-docs.platform-security-model-reference.page-51
title: scmi_system_power_state_config_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structscmi__system__power__state__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第51章\_scmi\_system\_power\_state\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structscmi__system__power__state__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

系统电源状态（System Power State）的配置。

```c
#include <zephyr/drivers/firmware/scmi/system.h>
```

<a id="details"></a>

系统电源状态（System Power State）的配置。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 51.1\_数据成员（Data Fields）

<a id="r_a28e0594daa49055401a0ecb82a614464"></a>

```c
uint32_t flags
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[flags](#a28e0594daa49055401a0ecb82a614464)。

请求标志，参见 `SCMI_SYSTEM_POWER_FLAG_*`。

<a id="r_a451cdd0751819ab189173723de742b63"></a>

```c
uint32_t system_state
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[system_state](#a451cdd0751819ab189173723de742b63)。

目标系统电源状态，参见 `SCMI_SYSTEM_POWER_STATE_*`。

## 51.2\_详细说明（Detailed Documentation）

<a id="a28e0594daa49055401a0ecb82a614464"></a>

### `flags`

```c
uint32_t scmi_system_power_state_config::flags
```

请求标志，参见 `SCMI_SYSTEM_POWER_FLAG_*`。

<a id="a451cdd0751819ab189173723de742b63"></a>

### `system_state`

```c
uint32_t scmi_system_power_state_config::system_state
```

目标系统电源状态，参见 `SCMI_SYSTEM_POWER_STATE_*`。

本数据类型文档由以下文件生成：

- `zephyr/drivers/firmware/scmi/system.h`

## 51.3\_原页交叉引用（Cross References）

- [zephyr/drivers/firmware/scmi/system.h](https://docs.zephyrproject.org/latest/doxygen/html/system_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P050_scmi_reset_domain_attr_结构体.md) · [返回大纲](大纲.md) · [下一章](P052_scmi_transport_api_结构体.md)
