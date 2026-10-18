---
id: learning.zephyr-docs.device-power-control-model-reference.page-49
title: numaker_scc_subsys_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnumaker__scc__subsys.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第49章\_numaker\_scc\_subsys\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnumaker__scc__subsys.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

NuMaker时钟子系统选择器（Clock Subsystem Selector）。

```c
#include <zephyr/drivers/clock_control/clock_control_numaker.h>
```

<a id="details"></a>

NuMaker时钟子系统选择器（Clock Subsystem Selector）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 49.1\_数据成员（Data Fields）

<a id="r_af8e2099977ecba2c53808fe8db4e041a"></a>

```c
uint32_t subsys_id
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[subsys_id](#af8e2099977ecba2c53808fe8db4e041a)。

SCC 子系统 ID，参见 `NUMAKER_SCC_SUBSYS_ID_PCC`。

```c
union {
```

<a id="r_ad2792f8ad57ee0e620a3c8157808aa73"></a>

```c
struct numaker_scc_subsys_pcc pcc
```

相关声明：[numaker_scc_subsys_pcc](P050_numaker_scc_subsys_pcc_结构体.md)、[pcc](#af8e8bc8bd9236ed245d56ef57b6e9082)。

外设时钟配置（Peripheral Clock Configuration）。

<a id="r_a7f5b37288c4551f317fbd8fbb6afa069"></a>

```c
};
```

## 49.2\_详细说明（Detailed Documentation）

<a id="a7f5b37288c4551f317fbd8fbb6afa069"></a>

### `[union]`

```c
union { ... } numaker_scc_subsys
```

<a id="af8e8bc8bd9236ed245d56ef57b6e9082"></a>

### `pcc`

```c
struct numaker_scc_subsys_pcc numaker_scc_subsys::pcc
```

外设时钟配置（Peripheral Clock Configuration）。

<a id="af8e2099977ecba2c53808fe8db4e041a"></a>

### `subsys_id`

```c
uint32_t numaker_scc_subsys::subsys_id
```

SCC 子系统 ID，参见 `NUMAKER_SCC_SUBSYS_ID_PCC`。

本数据类型文档由以下文件生成：

- `zephyr/drivers/clock_control/clock_control_numaker.h`

## 49.3\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control/clock_control_numaker.h](https://docs.zephyrproject.org/latest/doxygen/html/clock__control__numaker_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [NUMAKER_SCC_SUBSYS_ID_PCC](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__numaker.html#ga276ba4e34017fda5c4b77f4abb82a7af)
- [numaker_scc_subsys_pcc](P050_numaker_scc_subsys_pcc_结构体.md)
- [numaker_scc_subsys](P049_numaker_scc_subsys_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P048_npcx_ex_ops_uma_out_结构体.md) · [返回大纲](大纲.md) · [下一章](P050_numaker_scc_subsys_pcc_结构体.md)
