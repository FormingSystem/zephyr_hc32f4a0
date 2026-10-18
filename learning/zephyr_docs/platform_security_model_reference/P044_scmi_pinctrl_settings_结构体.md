---
id: learning.zephyr-docs.platform-security-model-reference.page-44
title: scmi_pinctrl_settings_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structscmi__pinctrl__settings.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第44章\_scmi\_pinctrl\_settings\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structscmi__pinctrl__settings.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

描述PINCTRL_SETTINGS_CONFIGURE命令的参数。

```c
#include <zephyr/drivers/firmware/scmi/pinctrl.h>
```

<a id="details"></a>

描述PINCTRL_SETTINGS_CONFIGURE命令的参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 44.1\_数据成员（Data Fields）

<a id="r_a36c8e49a42cb89d4117b9e90fe1a044e"></a>

```c
uint32_t id
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[id](#a36c8e49a42cb89d4117b9e90fe1a044e)。

待配置引脚或引脚组的标识符。

<a id="r_ade79b6c3efc5b069f74ad6e12088d6c2"></a>

```c
uint32_t function
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[function](#ade79b6c3efc5b069f74ad6e12088d6c2)。

要复用的功能，或 `SCMI_PINCTRL_NO_FUNCTION`。

<a id="r_a7c206eaf1a88e0d1e54d0d19c79e25c6"></a>

```c
uint32_t attributes
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[attributes](#a7c206eaf1a88e0d1e54d0d19c79e25c6)。

属性字（Attributes word），参见 `SCMI_PINCTRL_CONFIG_ATTRIBUTES`。

<a id="r_a5e92a3755d6dc8ccfecf696ca5eb8bd1"></a>

```c
uint32_t config [(10 *2)]
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[config](#a5e92a3755d6dc8ccfecf696ca5eb8bd1)。

由 `{type, value}` 配置对组成的数组。

## 44.2\_详细说明（Detailed Documentation）

<a id="a7c206eaf1a88e0d1e54d0d19c79e25c6"></a>

### `attributes`

```c
uint32_t scmi_pinctrl_settings::attributes
```

属性字（Attributes word），参见 `SCMI_PINCTRL_CONFIG_ATTRIBUTES`。

<a id="a5e92a3755d6dc8ccfecf696ca5eb8bd1"></a>

### `config`

```c
uint32_t scmi_pinctrl_settings::config[(10 *2)]
```

由 `{type, value}` 配置对组成的数组。

<a id="ade79b6c3efc5b069f74ad6e12088d6c2"></a>

### `function`

```c
uint32_t scmi_pinctrl_settings::function
```

要复用的功能，或 `SCMI_PINCTRL_NO_FUNCTION`。

<a id="a36c8e49a42cb89d4117b9e90fe1a044e"></a>

### `id`

```c
uint32_t scmi_pinctrl_settings::id
```

待配置引脚或引脚组的标识符。

本数据类型文档由以下文件生成：

- `zephyr/drivers/firmware/scmi/pinctrl.h`

## 44.3\_原页交叉引用（Cross References）

- [zephyr/drivers/firmware/scmi/pinctrl.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2firmware_2scmi_2pinctrl_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [SCMI_PINCTRL_NO_FUNCTION](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#gad3e2c57ca0d05f266c13ad5efda5f822)
- [SCMI_PINCTRL_CONFIG_ATTRIBUTES](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__pinctrl.html#ga8a504f804ca89f1fc7c7c2f8298f5b9e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P043_scmi_pd_lpm_settings_结构体.md) · [返回大纲](大纲.md) · [下一章](P045_scmi_platform_info_结构体.md)
