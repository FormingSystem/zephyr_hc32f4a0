---
id: learning.zephyr-docs.device-power-control-model-reference.page-79
title: sam_pmc_cfg_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsam__pmc__cfg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第79章\_sam\_pmc\_cfg\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsam__pmc__cfg.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

电源管理控制器（PMC）设备的恒定配置参数。

```c
#include <zephyr/drivers/clock_control/mchp_sam_pmc.h>
```

<a id="details"></a>

电源管理控制器（PMC）设备的恒定配置参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 79.1\_数据成员（Data Fields）

<a id="r_aa2584519cb128e96715a6a01140f609c"></a>

```c
uint32_t *const reg
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[reg](#aa2584519cb128e96715a6a01140f609c)。

电源管理控制器（PMC）寄存器基地址。

<a id="r_a0fc5ba6ce43a1f7b91d854ace83f59df"></a>

```c
const struct device * td_slck
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[td_slck](#a0fc5ba6ce43a1f7b91d854ace83f59df)。

时序域（Timing-domain）慢时钟设备。

<a id="r_abd4cbbd2082fe579bc6edd3d4548f390"></a>

```c
const struct device * md_slck
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[md_slck](#abd4cbbd2082fe579bc6edd3d4548f390)。

主域（Main-domain）慢时钟设备。

<a id="r_a8459cfb8ca7a99416e0c2e5e9a680481"></a>

```c
const struct device * main_xtal
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[main_xtal](#a8459cfb8ca7a99416e0c2e5e9a680481)。

主晶体振荡器（Main crystal oscillator）设备。

<a id="r_a3029662f9fa5ca96c142a9564c44f4d2"></a>

```c
const struct sam_sckc_config td_slck_cfg
```

相关声明：[sam_sckc_config](P081_sam_sckc_config_结构体.md)、[td_slck_cfg](#a3029662f9fa5ca96c142a9564c44f4d2)。

时序域慢时钟配置。

<a id="r_a149d058d1170af8eb75628dfd6b9cc92"></a>

```c
const struct sam_sckc_config md_slck_cfg
```

相关声明：[sam_sckc_config](P081_sam_sckc_config_结构体.md)、[md_slck_cfg](#a149d058d1170af8eb75628dfd6b9cc92)。

主域慢时钟配置。

## 79.2\_详细说明（Detailed Documentation）

<a id="a8459cfb8ca7a99416e0c2e5e9a680481"></a>

### `main_xtal`

```c
const struct device* sam_pmc_cfg::main_xtal
```

主晶体振荡器（Main crystal oscillator）设备。

<a id="abd4cbbd2082fe579bc6edd3d4548f390"></a>

### `md_slck`

```c
const struct device* sam_pmc_cfg::md_slck
```

主域（Main-domain）慢时钟设备。

<a id="a149d058d1170af8eb75628dfd6b9cc92"></a>

### `md_slck_cfg`

```c
const struct sam_sckc_config sam_pmc_cfg::md_slck_cfg
```

主域慢时钟配置。

<a id="aa2584519cb128e96715a6a01140f609c"></a>

### `reg`

```c
uint32_t* const sam_pmc_cfg::reg
```

电源管理控制器（PMC）寄存器基地址。

<a id="a0fc5ba6ce43a1f7b91d854ace83f59df"></a>

### `td_slck`

```c
const struct device* sam_pmc_cfg::td_slck
```

时序域（Timing-domain）慢时钟设备。

<a id="a3029662f9fa5ca96c142a9564c44f4d2"></a>

### `td_slck_cfg`

```c
const struct sam_sckc_config sam_pmc_cfg::td_slck_cfg
```

时序域慢时钟配置。

本数据类型文档由以下文件生成：

- `zephyr/drivers/clock_control/mchp_sam_pmc.h`

## 79.3\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control/mchp_sam_pmc.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__sam__pmc_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [device](../device_reference/P002_设备对象结构.md)
- [sam_sckc_config](P081_sam_sckc_config_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P078_sam_clk_cfg_结构体.md) · [返回大纲](大纲.md) · [下一章](P080_sam_pmc_data_结构体.md)
