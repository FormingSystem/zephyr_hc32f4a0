---
id: learning.zephyr-docs.device-power-control-model-reference.page-53
title: numicro_scc_subsys_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnumicro__scc__subsys.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第53章\_numicro\_scc\_subsys\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnumicro__scc__subsys.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Numicro外设时钟子系统配置（Peripheral Clock Subsystem Configuration）。

```c
#include <zephyr/drivers/clock_control/clock_control_numicro.h>
```

<a id="details"></a>

Numicro外设时钟子系统配置（Peripheral Clock Subsystem Configuration）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 53.1\_数据成员（Data Fields）

<a id="r_a58dd936369388d486bb93cc9c0d5eba7"></a>

```c
uint32_t subsys_id
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[subsys_id](#a58dd936369388d486bb93cc9c0d5eba7)。

子系统 ID，目前硬编码为 PCC。

```c
union {
```

<a id="r_ae8346aa626f8a2bd320591a214fe3eae"></a>

```c
struct numicro_scc_subsys_pcc pcc
```

相关声明：[numicro_scc_subsys_pcc](P054_numicro_scc_subsys_pcc_结构体.md)、[pcc](#a2bc16b33c42e4f3b8997a8bd50be7657)。

外设子系统配置。

<a id="r_aab66c6739d2228b66d7c9a8935e47aca"></a>

```c
};
```

子系统配置。

## 53.2\_详细说明（Detailed Documentation）

<a id="aab66c6739d2228b66d7c9a8935e47aca"></a>

### `[union]`

```c
union { ... } numicro_scc_subsys
```

子系统配置。

<a id="a2bc16b33c42e4f3b8997a8bd50be7657"></a>

### `pcc`

```c
struct numicro_scc_subsys_pcc numicro_scc_subsys::pcc
```

外设子系统配置。

<a id="a58dd936369388d486bb93cc9c0d5eba7"></a>

### `subsys_id`

```c
uint32_t numicro_scc_subsys::subsys_id
```

子系统 ID，目前硬编码为 PCC。

本数据类型文档由以下文件生成：

- `zephyr/drivers/clock_control/clock_control_numicro.h`

## 53.3\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control/clock_control_numicro.h](https://docs.zephyrproject.org/latest/doxygen/html/clock__control__numicro_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [numicro_scc_subsys_pcc](P054_numicro_scc_subsys_pcc_结构体.md)
- [numicro_scc_subsys](P053_numicro_scc_subsys_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P052_numaker_scc_subsys_rate_结构体.md) · [返回大纲](大纲.md) · [下一章](P054_numicro_scc_subsys_pcc_结构体.md)
