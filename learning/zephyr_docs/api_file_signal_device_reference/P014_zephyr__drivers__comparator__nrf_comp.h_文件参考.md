---
id: learning.zephyr-docs.api-file-signal-device-reference.page-14
title: zephyr__drivers__comparator__nrf_comp.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nrf__comp_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_zephyr\_\_drivers\_\_comparator\_\_nrf\_comp.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/nrf__comp_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/dt-bindings/comparator/nrf-comp.h>
#include <zephyr/drivers/comparator.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 14.1\_数据结构（Data Structures）

<a id="r_comp_5Fnrf_5Fcomp_5Fse_5Fconfig"></a>

```c
struct comp_nrf_comp_se_config
```

相关声明：[comp_nrf_comp_se_config](../device_power_control_model_reference/P004_comp_nrf_comp_se_config_结构体.md)。

单端模式（Single-Ended Mode）的配置结构。

<a id="r_comp_5Fnrf_5Fcomp_5Fdiff_5Fconfig"></a>

```c
struct comp_nrf_comp_diff_config
```

相关声明：[comp_nrf_comp_diff_config](../device_power_control_model_reference/P003_comp_nrf_comp_diff_config_结构体.md)。

差分模式（Differential Mode）的配置结构。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 14.2\_枚举（Enumerations）

<a id="r_a661d2e37c4acd5551b77e5bf2437b553"></a>

```c
enum comp_nrf_comp_refsel { COMP_NRF_COMP_REFSEL_INT_1V2 , COMP_NRF_COMP_REFSEL_INT_1V8 , COMP_NRF_COMP_REFSEL_INT_2V4 , COMP_NRF_COMP_REFSEL_AVDDAO1V8 , COMP_NRF_COMP_REFSEL_VDD , COMP_NRF_COMP_REFSEL_AREF }
```

相关声明：[comp_nrf_comp_refsel](#a661d2e37c4acd5551b77e5bf2437b553)、[COMP_NRF_COMP_REFSEL_INT_1V2](#a661d2e37c4acd5551b77e5bf2437b553abfa40254064295fec8c5882402f7f0d2)、[COMP_NRF_COMP_REFSEL_INT_1V8](#a661d2e37c4acd5551b77e5bf2437b553abf7088360f68099140b06de7d3f4b4e7)、[COMP_NRF_COMP_REFSEL_INT_2V4](#a661d2e37c4acd5551b77e5bf2437b553a3670bac3f83f144ca1373a4ea6c0107c)、[COMP_NRF_COMP_REFSEL_AVDDAO1V8](#a661d2e37c4acd5551b77e5bf2437b553a87eba8036aea56146b734ee47a9cd6ca)、[COMP_NRF_COMP_REFSEL_VDD](#a661d2e37c4acd5551b77e5bf2437b553a0e8f3057261749e3a15333d42e49512f)、[COMP_NRF_COMP_REFSEL_AREF](#a661d2e37c4acd5551b77e5bf2437b553ab0ae8de9e72cf723645691166e9fbb2e)。

参考源选择（Reference selection）。

<a id="r_ad13baf7c262d5fb2321ea5140180b3b1"></a>

```c
enum comp_nrf_comp_sp_mode { COMP_NRF_COMP_SP_MODE_LOW , COMP_NRF_COMP_SP_MODE_NORMAL , COMP_NRF_COMP_SP_MODE_HIGH }
```

相关声明：[comp_nrf_comp_sp_mode](#ad13baf7c262d5fb2321ea5140180b3b1)、[COMP_NRF_COMP_SP_MODE_LOW](#ad13baf7c262d5fb2321ea5140180b3b1a108433aa9b89eeca9a706e67d5eb8826)、[COMP_NRF_COMP_SP_MODE_NORMAL](#ad13baf7c262d5fb2321ea5140180b3b1a1fb59dd0aa818e279c5e4d15b620fac5)、[COMP_NRF_COMP_SP_MODE_HIGH](#ad13baf7c262d5fb2321ea5140180b3b1aeb3aad272a4b6cd1269180306357bd98)。

速度模式选择。

<a id="r_a74444aeafb5a2bf633ffd706cc6b9010"></a>

```c
enum comp_nrf_comp_isource { COMP_NRF_COMP_ISOURCE_DISABLED , COMP_NRF_COMP_ISOURCE_2UA5 , COMP_NRF_COMP_ISOURCE_5UA , COMP_NRF_COMP_ISOURCE_10UA }
```

相关声明：[comp_nrf_comp_isource](#a74444aeafb5a2bf633ffd706cc6b9010)、[COMP_NRF_COMP_ISOURCE_DISABLED](#a74444aeafb5a2bf633ffd706cc6b9010a3d47ebd769b9d4b9668d7c6502294043)、[COMP_NRF_COMP_ISOURCE_2UA5](#a74444aeafb5a2bf633ffd706cc6b9010ab413c10f12cbfb5b2e550f8fa07992c2)、[COMP_NRF_COMP_ISOURCE_5UA](#a74444aeafb5a2bf633ffd706cc6b9010a1890799d7f32b44f1a870ed67a8707a0)、[COMP_NRF_COMP_ISOURCE_10UA](#a74444aeafb5a2bf633ffd706cc6b9010a16df414be65b65763e5938bc37bb392f)。

电流源（Current source）配置。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 14.3\_函数（Functions）

<a id="r_aca8ca4ea25fbfbe962f754ef79bcb356"></a>

```c
int comp_nrf_comp_configure_se (const struct device *dev, const struct comp_nrf_comp_se_config *config)
```

相关声明：[comp_nrf_comp_configure_se](#aca8ca4ea25fbfbe962f754ef79bcb356)、[device](../device_reference/P002_设备对象结构.md)、[comp_nrf_comp_se_config](../device_power_control_model_reference/P004_comp_nrf_comp_se_config_结构体.md)。

将比较器（Comparator）配置为单端模式（Single-ended Mode）。

<a id="r_a63ca5bf56504df5c9d0904609c433e11"></a>

```c
int comp_nrf_comp_configure_diff (const struct device *dev, const struct comp_nrf_comp_diff_config *config)
```

相关声明：[comp_nrf_comp_configure_diff](#a63ca5bf56504df5c9d0904609c433e11)、[device](../device_reference/P002_设备对象结构.md)、[comp_nrf_comp_diff_config](../device_power_control_model_reference/P003_comp_nrf_comp_diff_config_结构体.md)。

将比较器（Comparator）配置为差分模式（Differential Mode）。

## 14.4\_详细说明（Detailed Documentation）

<a id="a74444aeafb5a2bf633ffd706cc6b9010"></a>

### `comp_nrf_comp_isource`

```c
enum comp_nrf_comp_isource
```

电流源（Current source）配置。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `COMP_NRF_COMP_ISOURCE_DISABLED` | 禁用电流源（Current Source）。 |
| `COMP_NRF_COMP_ISOURCE_2UA5` | 使能 2.5 μA 电流源（Current Source）。 |
| `COMP_NRF_COMP_ISOURCE_5UA` | 使能 5 μA 电流源（Current Source）。 |
| `COMP_NRF_COMP_ISOURCE_10UA` | 使能 10 μA 电流源（Current Source）。 |

<a id="a661d2e37c4acd5551b77e5bf2437b553"></a>

### `comp_nrf_comp_refsel`

```c
enum comp_nrf_comp_refsel
```

参考源选择（Reference selection）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `COMP_NRF_COMP_REFSEL_INT_1V2` | 内部 1.2 V 参考电压（Reference）。 |
| `COMP_NRF_COMP_REFSEL_INT_1V8` | 内部 1.8 V 参考电压（Reference）。 |
| `COMP_NRF_COMP_REFSEL_INT_2V4` | 内部 2.4 V 参考电压（Reference）。 |
| `COMP_NRF_COMP_REFSEL_AVDDAO1V8` | AVDD 1.8 V 参考电压（Reference）。 |
| `COMP_NRF_COMP_REFSEL_VDD` | VDD 参考电压（Reference）。 |
| `COMP_NRF_COMP_REFSEL_AREF` | 使用外部模拟参考电压（External Analog Reference）。 |

<a id="ad13baf7c262d5fb2321ea5140180b3b1"></a>

### `comp_nrf_comp_sp_mode`

```c
enum comp_nrf_comp_sp_mode
```

速度模式选择。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `COMP_NRF_COMP_SP_MODE_LOW` | 低功耗模式（Low-power Mode）。 |
| `COMP_NRF_COMP_SP_MODE_NORMAL` | 正常模式（Normal Mode）。 |
| `COMP_NRF_COMP_SP_MODE_HIGH` | 高速模式（High-speed Mode）。 |

<a id="a63ca5bf56504df5c9d0904609c433e11"></a>

### `comp_nrf_comp_configure_diff()`

```c
int comp_nrf_comp_configure_diff ( const struct device * dev, const struct comp_nrf_comp_diff_config * config )
```

将比较器（Comparator）配置为差分模式（Differential Mode）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 比较器设备实例（Comparator Device Instance）。 |
| `config` | 差分模式配置（Differential Mode Configuration）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `negative` | 否则返回 errno 错误码（Error Code）。 |

<a id="aca8ca4ea25fbfbe962f754ef79bcb356"></a>

### `comp_nrf_comp_configure_se()`

```c
int comp_nrf_comp_configure_se ( const struct device * dev, const struct comp_nrf_comp_se_config * config )
```

将比较器（Comparator）配置为单端模式（Single-ended Mode）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 比较器设备实例（Comparator Device Instance）。 |
| `config` | 单端模式配置（Single-ended Mode Configuration）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `negative` | 否则返回 errno 错误码（Error Code）。 |


## 14.5\_原页交叉引用（Cross References）

- [zephyr/dt-bindings/comparator/nrf-comp.h](../api_source_supplement_reference/P131_nrf-comp.h_源码浏览.md)
- [zephyr/drivers/comparator.h](../analog_reference/P002_比较器公共头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P599_nrf_comp.h_源码浏览.md)
- [comp_nrf_comp_se_config](../device_power_control_model_reference/P004_comp_nrf_comp_se_config_结构体.md)
- [comp_nrf_comp_diff_config](../device_power_control_model_reference/P003_comp_nrf_comp_diff_config_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)

<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="a74444aeafb5a2bf633ffd706cc6b9010a3d47ebd769b9d4b9668d7c6502294043"></a>
<a id="a74444aeafb5a2bf633ffd706cc6b9010ab413c10f12cbfb5b2e550f8fa07992c2"></a>
<a id="a74444aeafb5a2bf633ffd706cc6b9010a1890799d7f32b44f1a870ed67a8707a0"></a>
<a id="a74444aeafb5a2bf633ffd706cc6b9010a16df414be65b65763e5938bc37bb392f"></a>
<a id="a661d2e37c4acd5551b77e5bf2437b553abfa40254064295fec8c5882402f7f0d2"></a>
<a id="a661d2e37c4acd5551b77e5bf2437b553abf7088360f68099140b06de7d3f4b4e7"></a>
<a id="a661d2e37c4acd5551b77e5bf2437b553a3670bac3f83f144ca1373a4ea6c0107c"></a>
<a id="a661d2e37c4acd5551b77e5bf2437b553a87eba8036aea56146b734ee47a9cd6ca"></a>
<a id="a661d2e37c4acd5551b77e5bf2437b553a0e8f3057261749e3a15333d42e49512f"></a>
<a id="a661d2e37c4acd5551b77e5bf2437b553ab0ae8de9e72cf723645691166e9fbb2e"></a>
<a id="ad13baf7c262d5fb2321ea5140180b3b1a108433aa9b89eeca9a706e67d5eb8826"></a>
<a id="ad13baf7c262d5fb2321ea5140180b3b1a1fb59dd0aa818e279c5e4d15b620fac5"></a>
<a id="ad13baf7c262d5fb2321ea5140180b3b1aeb3aad272a4b6cd1269180306357bd98"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P013_zephyr__drivers__interrupt_controller__intc_exti_stm32.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P015_zephyr__drivers__interrupt_controller__nxp_pint.h_文件参考.md)
