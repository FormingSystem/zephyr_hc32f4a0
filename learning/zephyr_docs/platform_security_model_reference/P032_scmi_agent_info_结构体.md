---
id: learning.zephyr-docs.platform-security-model-reference.page-32
title: scmi_agent_info_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structscmi__agent__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第32章\_scmi\_agent\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structscmi__agent__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

系统控制与管理接口（SCMI）基础协议的代理信息。

```c
#include <zephyr/drivers/firmware/scmi/base.h>
```

<a id="details"></a>

系统控制与管理接口（SCMI）基础协议的代理信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 32.1\_数据成员（Data Fields）

<a id="r_a137145e77dd29b54815295d0951a5263"></a>

```c
uint32_t agent_id
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[agent_id](#a137145e77dd29b54815295d0951a5263)。

代理（agent）的标识符。

<a id="r_aed61e021c94d0a5efb05f14daf47077b"></a>

```c
char name [16]
```

相关声明：[name](#aed61e021c94d0a5efb05f14daf47077b)。

以空字符结尾的 ASCII 字符串，长度最多为 16 字节。

## 32.2\_详细说明（Detailed Documentation）

<a id="a137145e77dd29b54815295d0951a5263"></a>

### `agent_id`

```c
uint32_t scmi_agent_info::agent_id
```

代理（agent）的标识符。

<a id="aed61e021c94d0a5efb05f14daf47077b"></a>

### `name`

```c
char scmi_agent_info::name[16]
```

以空字符结尾的 ASCII 字符串，长度最多为 16 字节。

本数据类型文档由以下文件生成：

- `zephyr/drivers/firmware/scmi/base.h`

## 32.3\_原页交叉引用（Cross References）

- [zephyr/drivers/firmware/scmi/base.h](https://docs.zephyrproject.org/latest/doxygen/html/base_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P031_pcie_vctc_map_结构体.md) · [返回大纲](大纲.md) · [下一章](P033_scmi_channel_结构体.md)
