---
id: learning.zephyr-docs.platform-security-model-reference.page-35
title: scmi_clock_config_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structscmi__clock__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第35章\_scmi\_clock\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structscmi__clock__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

描述CLOCK_CONFIG_SET命令的参数。

```c
#include <zephyr/drivers/firmware/scmi/clk.h>
```

<a id="details"></a>

描述CLOCK_CONFIG_SET命令的参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 35.1\_数据成员（Data Fields）

<a id="r_a1f4acfb41d1b75448f96acad6cfd3498"></a>

```c
uint32_t clk_id
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[clk_id](#a1f4acfb41d1b75448f96acad6cfd3498)。

待配置时钟的 ID。

<a id="r_ae21186dde1af79f55bdce325d08cdc06"></a>

```c
uint32_t attributes
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[attributes](#ae21186dde1af79f55bdce325d08cdc06)。

配置属性（例如：

<a id="r_ae180ad04a48558130e26a268ec444297"></a>

```c
uint32_t extended_cfg_val
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[extended_cfg_val](#ae180ad04a48558130e26a268ec444297)。

扩展配置值；具体含义由属性决定。

## 35.2\_详细说明（Detailed Documentation）

<a id="ae21186dde1af79f55bdce325d08cdc06"></a>

### `attributes`

```c
uint32_t scmi_clock_config::attributes
```

配置属性（例如：

使能/禁用，参见 `SCMI_CLK_CONFIG_*`）。

<a id="a1f4acfb41d1b75448f96acad6cfd3498"></a>

### `clk_id`

```c
uint32_t scmi_clock_config::clk_id
```

待配置时钟的 ID。

<a id="ae180ad04a48558130e26a268ec444297"></a>

### `extended_cfg_val`

```c
uint32_t scmi_clock_config::extended_cfg_val
```

扩展配置值；具体含义由属性决定。

本数据类型文档由以下文件生成：

- `zephyr/drivers/firmware/scmi/clk.h`

## 35.3\_原页交叉引用（Cross References）

- [zephyr/drivers/firmware/scmi/clk.h](https://docs.zephyrproject.org/latest/doxygen/html/clk_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P034_scmi_clock_attributes_结构体.md) · [返回大纲](大纲.md) · [下一章](P036_scmi_clock_rate_config_结构体.md)
