---
id: learning.zephyr-docs.api-file-mesh-interrupt-reference.page-18
title: zephyr__drivers__comparator__nrf_lpcomp.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nrf__lpcomp_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_zephyr\_\_drivers\_\_comparator\_\_nrf\_lpcomp.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/nrf__lpcomp_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/dt-bindings/comparator/nrf-comp.h>
#include <zephyr/drivers/comparator.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 18.1\_数据结构（Data Structures）

<a id="r_comp_5Fnrf_5Flpcomp_5Fconfig"></a>

```c
struct comp_nrf_lpcomp_config
```

相关声明：[comp_nrf_lpcomp_config](../device_power_control_model_reference/P005_comp_nrf_lpcomp_config_结构体.md)。

配置结构（Configuration Structure）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 18.2\_枚举（Enumerations）

<a id="r_ae42326afcd4f5435480f80d382266a04"></a>

```c
enum comp_nrf_lpcomp_refsel { COMP_NRF_LPCOMP_REFSEL_VDD_1_8 , COMP_NRF_LPCOMP_REFSEL_VDD_2_8 , COMP_NRF_LPCOMP_REFSEL_VDD_3_8 , COMP_NRF_LPCOMP_REFSEL_VDD_4_8 , COMP_NRF_LPCOMP_REFSEL_VDD_5_8 , COMP_NRF_LPCOMP_REFSEL_VDD_6_8 , COMP_NRF_LPCOMP_REFSEL_VDD_7_8 , COMP_NRF_LPCOMP_REFSEL_VDD_1_16 , COMP_NRF_LPCOMP_REFSEL_VDD_3_16 , COMP_NRF_LPCOMP_REFSEL_VDD_5_16 , COMP_NRF_LPCOMP_REFSEL_VDD_7_16 , COMP_NRF_LPCOMP_REFSEL_VDD_9_16 , COMP_NRF_LPCOMP_REFSEL_VDD_11_16 , COMP_NRF_LPCOMP_REFSEL_VDD_13_16 , COMP_NRF_LPCOMP_REFSEL_VDD_15_16 , COMP_NRF_LPCOMP_REFSEL_AREF }
```

相关声明：[comp_nrf_lpcomp_refsel](#ae42326afcd4f5435480f80d382266a04)、[COMP_NRF_LPCOMP_REFSEL_VDD_1_8](#ae42326afcd4f5435480f80d382266a04a99627f00ae3182014da516333f64705f)、[COMP_NRF_LPCOMP_REFSEL_VDD_2_8](#ae42326afcd4f5435480f80d382266a04a3c10840415f3aed4d0b8414a6decf56d)、[COMP_NRF_LPCOMP_REFSEL_VDD_3_8](#ae42326afcd4f5435480f80d382266a04a25c009efcddd2e84417d115b5f4e346e)、[COMP_NRF_LPCOMP_REFSEL_VDD_4_8](#ae42326afcd4f5435480f80d382266a04a848e512c3223a019f6ec59612616fe33)、[COMP_NRF_LPCOMP_REFSEL_VDD_5_8](#ae42326afcd4f5435480f80d382266a04a295352a4ecb28f6288efe33fd0c49526)、[COMP_NRF_LPCOMP_REFSEL_VDD_6_8](#ae42326afcd4f5435480f80d382266a04a624b842d3ef6e8fa172412fc3a06dd1a)、[COMP_NRF_LPCOMP_REFSEL_VDD_7_8](#ae42326afcd4f5435480f80d382266a04a2b1cd929103b9af8ef372472078efb76)、[COMP_NRF_LPCOMP_REFSEL_VDD_1_16](#ae42326afcd4f5435480f80d382266a04acd4c60e604696b7d24028ad9e98d77f3)、[COMP_NRF_LPCOMP_REFSEL_VDD_3_16](#ae42326afcd4f5435480f80d382266a04a3b3760b0298de0fcb94812f98433ba16)、[COMP_NRF_LPCOMP_REFSEL_VDD_5_16](#ae42326afcd4f5435480f80d382266a04a94a97a641eaa3dc25b09d00dda8fb137)、[COMP_NRF_LPCOMP_REFSEL_VDD_7_16](#ae42326afcd4f5435480f80d382266a04a98def2c5d100c1c51c697203606b66dd)、[COMP_NRF_LPCOMP_REFSEL_VDD_9_16](#ae42326afcd4f5435480f80d382266a04aa62402dda42b69bd974de3f19aa4a509)、[COMP_NRF_LPCOMP_REFSEL_VDD_11_16](#ae42326afcd4f5435480f80d382266a04a9913bfd70d57767e295ced6e7287a7bb)、[COMP_NRF_LPCOMP_REFSEL_VDD_13_16](#ae42326afcd4f5435480f80d382266a04a930ce822163d6654cda439e43fbbaab1)、[COMP_NRF_LPCOMP_REFSEL_VDD_15_16](#ae42326afcd4f5435480f80d382266a04aade5263dc54bd126f9a761e0188b13f7)、[COMP_NRF_LPCOMP_REFSEL_AREF](#ae42326afcd4f5435480f80d382266a04abf717bfb0610352e60d4f4fc45a370b1)。

参考源选择（Reference selection）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 18.3\_函数（Functions）

<a id="r_aff748ac1a1a8c13796b81ef789b4c7f2"></a>

```c
int comp_nrf_lpcomp_configure (const struct device *dev, const struct comp_nrf_lpcomp_config *config)
```

相关声明：[comp_nrf_lpcomp_configure](#aff748ac1a1a8c13796b81ef789b4c7f2)、[device](../device_reference/P002_设备对象结构.md)、[comp_nrf_lpcomp_config](../device_power_control_model_reference/P005_comp_nrf_lpcomp_config_结构体.md)。

配置比较器（Comparator）。

## 18.4\_详细说明（Detailed Documentation）

<a id="ae42326afcd4f5435480f80d382266a04"></a>

### `comp_nrf_lpcomp_refsel`

```c
enum comp_nrf_lpcomp_refsel
```

参考源选择（Reference selection）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `COMP_NRF_LPCOMP_REFSEL_VDD_1_8` | 使用 `VDD * (1/8)` 作为参考电压（Reference）。 |
| `COMP_NRF_LPCOMP_REFSEL_VDD_2_8` | 使用 `VDD * (2/8)` 作为参考电压（Reference）。 |
| `COMP_NRF_LPCOMP_REFSEL_VDD_3_8` | 使用 `VDD * (3/8)` 作为参考电压（Reference）。 |
| `COMP_NRF_LPCOMP_REFSEL_VDD_4_8` | 使用 `VDD * (4/8)` 作为参考电压（Reference）。 |
| `COMP_NRF_LPCOMP_REFSEL_VDD_5_8` | 使用 `VDD * (5/8)` 作为参考电压（Reference）。 |
| `COMP_NRF_LPCOMP_REFSEL_VDD_6_8` | 使用 `VDD * (6/8)` 作为参考电压（Reference）。 |
| `COMP_NRF_LPCOMP_REFSEL_VDD_7_8` | 使用 `VDD * (7/8)` 作为参考电压（Reference）。 |
| `COMP_NRF_LPCOMP_REFSEL_VDD_1_16` | 使用 `VDD * (1/16)` 作为参考电压（Reference）。 |
| `COMP_NRF_LPCOMP_REFSEL_VDD_3_16` | 使用 `VDD * (3/16)` 作为参考电压（Reference）。 |
| `COMP_NRF_LPCOMP_REFSEL_VDD_5_16` | 使用 `VDD * (5/16)` 作为参考电压（Reference）。 |
| `COMP_NRF_LPCOMP_REFSEL_VDD_7_16` | 使用 `VDD * (7/16)` 作为参考电压（Reference）。 |
| `COMP_NRF_LPCOMP_REFSEL_VDD_9_16` | 使用 `VDD * (9/16)` 作为参考电压（Reference）。 |
| `COMP_NRF_LPCOMP_REFSEL_VDD_11_16` | 使用 `VDD * (11/16)` 作为参考电压（Reference）。 |
| `COMP_NRF_LPCOMP_REFSEL_VDD_13_16` | 使用 `VDD * (13/16)` 作为参考电压（Reference）。 |
| `COMP_NRF_LPCOMP_REFSEL_VDD_15_16` | 使用 `VDD * (15/16)` 作为参考电压（Reference）。 |
| `COMP_NRF_LPCOMP_REFSEL_AREF` | 使用外部模拟参考电压（External Analog Reference）。 |

<a id="aff748ac1a1a8c13796b81ef789b4c7f2"></a>

### `comp_nrf_lpcomp_configure()`

```c
int comp_nrf_lpcomp_configure ( const struct device * dev, const struct comp_nrf_lpcomp_config * config )
```

配置比较器（Comparator）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 比较器设备实例（Comparator Device Instance）。 |
| `config` | 配置（Configuration）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `negative` | 否则返回 errno 错误码（Error Code）。 |


## 18.5\_原页交叉引用（Cross References）

- [zephyr/dt-bindings/comparator/nrf-comp.h](../api_source_supplement_reference/P131_nrf-comp.h_源码浏览.md)
- [zephyr/drivers/comparator.h](../analog_reference/P002_比较器公共头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P600_nrf_lpcomp.h_源码浏览.md)
- [comp_nrf_lpcomp_config](../device_power_control_model_reference/P005_comp_nrf_lpcomp_config_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)

<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ae42326afcd4f5435480f80d382266a04a99627f00ae3182014da516333f64705f"></a>
<a id="ae42326afcd4f5435480f80d382266a04a3c10840415f3aed4d0b8414a6decf56d"></a>
<a id="ae42326afcd4f5435480f80d382266a04a25c009efcddd2e84417d115b5f4e346e"></a>
<a id="ae42326afcd4f5435480f80d382266a04a848e512c3223a019f6ec59612616fe33"></a>
<a id="ae42326afcd4f5435480f80d382266a04a295352a4ecb28f6288efe33fd0c49526"></a>
<a id="ae42326afcd4f5435480f80d382266a04a624b842d3ef6e8fa172412fc3a06dd1a"></a>
<a id="ae42326afcd4f5435480f80d382266a04a2b1cd929103b9af8ef372472078efb76"></a>
<a id="ae42326afcd4f5435480f80d382266a04acd4c60e604696b7d24028ad9e98d77f3"></a>
<a id="ae42326afcd4f5435480f80d382266a04a3b3760b0298de0fcb94812f98433ba16"></a>
<a id="ae42326afcd4f5435480f80d382266a04a94a97a641eaa3dc25b09d00dda8fb137"></a>
<a id="ae42326afcd4f5435480f80d382266a04a98def2c5d100c1c51c697203606b66dd"></a>
<a id="ae42326afcd4f5435480f80d382266a04aa62402dda42b69bd974de3f19aa4a509"></a>
<a id="ae42326afcd4f5435480f80d382266a04a9913bfd70d57767e295ced6e7287a7bb"></a>
<a id="ae42326afcd4f5435480f80d382266a04a930ce822163d6654cda439e43fbbaab1"></a>
<a id="ae42326afcd4f5435480f80d382266a04aade5263dc54bd126f9a761e0188b13f7"></a>
<a id="ae42326afcd4f5435480f80d382266a04abf717bfb0610352e60d4f4fc45a370b1"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P017_zephyr__bluetooth__mesh__msg.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P019_zephyr__bluetooth__services__nus.h_文件参考.md)
