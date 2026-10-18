---
id: learning.zephyr-docs.api-file-network-device-reference.page-8
title: zephyr__drivers__misc__nxp_rtxxx_dsp_ctrl__nxp_rtxxx_dsp_ctrl.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_zephyr\_\_drivers\_\_misc\_\_nxp\_rtxxx\_dsp\_ctrl\_\_nxp\_rtxxx\_dsp\_ctrl.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/device.h>
#include <zephyr/dt-bindings/misc/nxp_rtxxx_dsp_ctrl.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 8.1\_数据结构（Data Structures）

<a id="r_nxp_5Frtxxx_5Fdsp_5Fctrl_5Fapi"></a>

```c
struct nxp_rtxxx_dsp_ctrl_api
```

相关声明：[nxp_rtxxx_dsp_ctrl_api](../platform_security_model_reference/P023_nxp_rtxxx_dsp_ctrl_api_结构体.md)。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 8.2\_类型定义（Typedefs）

<a id="r_ab6ed31cfcaa45744f960bc19d89f642f"></a>

```c
typedef int(* nxp_rtxxx_dsp_ctrl_api_load_section) (const struct device *, const void *, size_t, enum nxp_rtxxx_dsp_ctrl_section_type)
```

相关声明：[nxp_rtxxx_dsp_ctrl_api_load_section](#ab6ed31cfcaa45744f960bc19d89f642f)、[device](../device_reference/P002_设备对象结构.md)、[nxp_rtxxx_dsp_ctrl_section_type](#a1230a21b6c11930f80fc5f12605de762)。

<a id="r_a561283f2992839e0191d2fcfef12d989"></a>

```c
typedef void(* nxp_rtxxx_dsp_ctrl_api_enable) (const struct device *dev)
```

相关声明：[nxp_rtxxx_dsp_ctrl_api_enable](#a561283f2992839e0191d2fcfef12d989)、[device](../device_reference/P002_设备对象结构.md)。

<a id="r_a17b3a647a7798b34c820366916b2a1c5"></a>

```c
typedef void(* nxp_rtxxx_dsp_ctrl_api_disable) (const struct device *dev)
```

相关声明：[nxp_rtxxx_dsp_ctrl_api_disable](#a17b3a647a7798b34c820366916b2a1c5)、[device](../device_reference/P002_设备对象结构.md)。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 8.3\_枚举（Enumerations）

<a id="r_a1230a21b6c11930f80fc5f12605de762"></a>

```c
enum nxp_rtxxx_dsp_ctrl_section_type { NXP_RTXXX_DSP_CTRL_SECTION_RESET = 0 , NXP_RTXXX_DSP_CTRL_SECTION_TEXT = 1 , NXP_RTXXX_DSP_CTRL_SECTION_DATA = 2 }
```

相关声明：[nxp_rtxxx_dsp_ctrl_section_type](#a1230a21b6c11930f80fc5f12605de762)、[NXP_RTXXX_DSP_CTRL_SECTION_RESET](#a1230a21b6c11930f80fc5f12605de762a8c63b3117b7c525e96be2b054395cfff)、[NXP_RTXXX_DSP_CTRL_SECTION_TEXT](#a1230a21b6c11930f80fc5f12605de762ab0c726ddfdf30c89075fcf9c7b4586e7)、[NXP_RTXXX_DSP_CTRL_SECTION_DATA](#a1230a21b6c11930f80fc5f12605de762aa43ff75c06ea161e322d77b8dede7791)。

描述镜像节类型选择（Image Section Type Selection）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 8.4\_函数（Functions）

<a id="r_af1bd0005fe3a6d46d559b249b3ff8ca8"></a>

```c
static int nxp_rtxxx_dsp_ctrl_load_section (const struct device *dev, const void *base, size_t length, enum nxp_rtxxx_dsp_ctrl_section_type section)
```

相关声明：[nxp_rtxxx_dsp_ctrl_load_section](#af1bd0005fe3a6d46d559b249b3ff8ca8)、[device](../device_reference/P002_设备对象结构.md)、[nxp_rtxxx_dsp_ctrl_section_type](#a1230a21b6c11930f80fc5f12605de762)。

将表示指定节（Section）的镜像加载到数字信号处理器（DSP）内存的特定区域。

<a id="r_a9cc6dd311f29f2e7c79fc74c39658041"></a>

```c
static void nxp_rtxxx_dsp_ctrl_enable (const struct device *dev)
```

相关声明：[nxp_rtxxx_dsp_ctrl_enable](#a9cc6dd311f29f2e7c79fc74c39658041)、[device](../device_reference/P002_设备对象结构.md)。

启动 DSP，即解除停顿（Unstall）。

<a id="r_a2efeac2828998f896f2e1bfb532700cd"></a>

```c
static void nxp_rtxxx_dsp_ctrl_disable (const struct device *dev)
```

相关声明：[nxp_rtxxx_dsp_ctrl_disable](#a2efeac2828998f896f2e1bfb532700cd)、[device](../device_reference/P002_设备对象结构.md)。

停止 DSP，即使其停顿（Stall）。

## 8.5\_详细说明（Detailed Documentation）

<a id="a17b3a647a7798b34c820366916b2a1c5"></a>

### `nxp_rtxxx_dsp_ctrl_api_disable`

```c
typedef void(* nxp_rtxxx_dsp_ctrl_api_disable) (const struct device *dev)
```

<a id="a561283f2992839e0191d2fcfef12d989"></a>

### `nxp_rtxxx_dsp_ctrl_api_enable`

```c
typedef void(* nxp_rtxxx_dsp_ctrl_api_enable) (const struct device *dev)
```

<a id="ab6ed31cfcaa45744f960bc19d89f642f"></a>

### `nxp_rtxxx_dsp_ctrl_api_load_section`

```c
typedef int(* nxp_rtxxx_dsp_ctrl_api_load_section) (const struct device *, const void *, size_t, enum nxp_rtxxx_dsp_ctrl_section_type)
```

<a id="a1230a21b6c11930f80fc5f12605de762"></a>

### `nxp_rtxxx_dsp_ctrl_section_type`

```c
enum nxp_rtxxx_dsp_ctrl_section_type
```

描述镜像节类型选择（Image Section Type Selection）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `NXP_RTXXX_DSP_CTRL_SECTION_RESET` |  |
| `NXP_RTXXX_DSP_CTRL_SECTION_TEXT` |  |
| `NXP_RTXXX_DSP_CTRL_SECTION_DATA` |  |

<a id="a2efeac2828998f896f2e1bfb532700cd"></a>

### `nxp_rtxxx_dsp_ctrl_disable()`

```c
void nxp_rtxxx_dsp_ctrl_disable ( const struct device * dev)
```

声明属性：`inline`、`static`。

停止 DSP，即使其停顿（Stall）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 数字信号处理器（DSP）设备。 |

<a id="a9cc6dd311f29f2e7c79fc74c39658041"></a>

### `nxp_rtxxx_dsp_ctrl_enable()`

```c
void nxp_rtxxx_dsp_ctrl_enable ( const struct device * dev)
```

声明属性：`inline`、`static`。

启动 DSP，即解除停顿（Unstall）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 数字信号处理器（DSP）设备。 |

<a id="af1bd0005fe3a6d46d559b249b3ff8ca8"></a>

### `nxp_rtxxx_dsp_ctrl_load_section()`

```c
int nxp_rtxxx_dsp_ctrl_load_section ( const struct device * dev, const void * base, size_t length, enum nxp_rtxxx_dsp_ctrl_section_type section )
```

声明属性：`inline`、`static`。

将表示指定节（Section）的镜像加载到数字信号处理器（DSP）内存的特定区域。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 数字信号处理器（DSP）设备。 |
| `base` | 待加载镜像（Image）的基址指针。 |
| `length` | 镜像长度（Image Length）。 |
| `section` | 指定镜像所表示的节类型（Section Type）。 |

**返回（Returns）**：**返回值（Returns）：**返回 `int`；成功为 0，参数无效为 `-EINVAL`，镜像大于目标区域为 `-ENOMEM`。


## 8.6\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/dt-bindings/misc/nxp_rtxxx_dsp_ctrl.h](../api_source_reference/P193_nxp_rtxxx_dsp_ctrl.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P165_nxp_rtxxx_dsp_ctrl.h_源码浏览.md)
- [nxp_rtxxx_dsp_ctrl_api](../platform_security_model_reference/P023_nxp_rtxxx_dsp_ctrl_api_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)

<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="a1230a21b6c11930f80fc5f12605de762a8c63b3117b7c525e96be2b054395cfff"></a>
<a id="a1230a21b6c11930f80fc5f12605de762ab0c726ddfdf30c89075fcf9c7b4586e7"></a>
<a id="a1230a21b6c11930f80fc5f12605de762aa43ff75c06ea161e322d77b8dede7791"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P007_zephyr__drivers__firmware__scmi__reset.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P009_zephyr__dt-bindings__sensor__pac194x.h_文件参考.md)
