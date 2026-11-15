---
id: learning.zephyr-docs.api-file-network-device-reference.page-9
title: zephyr__dt-bindings__sensor__pac194x.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2sensor_2pac194x_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_zephyr\_\_dt-bindings\_\_sensor\_\_pac194x.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2sensor_2pac194x_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

the Microchip PAC194x power monitor的设备树绑定常量（Devicetree Binding Constants）。

查看此文件的源码。

<a id="details"></a>

the Microchip PAC194x power monitor的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 9.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 满量程范围模式（Full-scale Range Mode）

设备树（Devicetree）属性 `microchip,vbus-mode` 和 `microchip,vsense-mode` 的取值。

<a id="r_ga69132e5c34fa02a6bfa36ae4bf1ecd27"></a>

```c
#define PAC_UNIPOLAR_FSR 0
```

相关声明：[PAC_UNIPOLAR_FSR](../api_update_memory_topic_reference/P013_PAC194X API主题.md#ga69132e5c34fa02a6bfa36ae4bf1ecd27)。

单极性满量程范围（Unipolar Full-scale Range）。

<a id="r_gafdc80d9ece34bd9a2d39d649b7971ec1"></a>

```c
#define PAC_BIPOLAR_FSR 1
```

相关声明：[PAC_BIPOLAR_FSR](../api_update_memory_topic_reference/P013_PAC194X API主题.md#gafdc80d9ece34bd9a2d39d649b7971ec1)。

双极性满量程范围（Bipolar Full-scale Range）。

<a id="r_ga4db614817516296166b2524ab78c447f"></a>

```c
#define PAC_BIPOLAR_HALF_FSR 2
```

相关声明：[PAC_BIPOLAR_HALF_FSR](../api_update_memory_topic_reference/P013_PAC194X API主题.md#ga4db614817516296166b2524ab78c447f)。

双极性半量程范围（Bipolar Half Range），即 `FSR / 2`。

<a id="define-members-1"></a>

### 累积数据源（Accumulation Source）

设备树（Devicetree）属性 `microchip,accumulation-mode` 的取值。

<a id="r_ga3090e6340cf34c043924b3a30fea4c79"></a>

```c
#define PAC_ACCUM_VPOWER 0
```

相关声明：[PAC_ACCUM_VPOWER](../api_update_memory_topic_reference/P013_PAC194X API主题.md#ga3090e6340cf34c043924b3a30fea4c79)。

累积功率数据（Power Data）。

<a id="r_ga264aab83fe304ab142ac139a9de53396"></a>

```c
#define PAC_ACCUM_VSENSE 1
```

相关声明：[PAC_ACCUM_VSENSE](../api_update_memory_topic_reference/P013_PAC194X API主题.md#ga264aab83fe304ab142ac139a9de53396)。

累积电流数据，即检测电压（Sense Voltage）数据。

<a id="r_ga12f7026116719fbcdb0ed959ca165025"></a>

```c
#define PAC_ACCUM_VBUS 2
```

相关声明：[PAC_ACCUM_VBUS](../api_update_memory_topic_reference/P013_PAC194X API主题.md#ga12f7026116719fbcdb0ed959ca165025)。

累积总线电压数据（Bus Voltage Data）。

<a id="define-members-2"></a>

### 刷新模式（Refresh Mode）

设备树（Devicetree）属性 `microchip,refresh-mode` 的取值。

<a id="r_ga11c894871e498d98606f96469700fd11"></a>

```c
#define PAC_REFRESH_MANUAL 0
```

相关声明：[PAC_REFRESH_MANUAL](../api_update_memory_topic_reference/P013_PAC194X API主题.md#ga11c894871e498d98606f96469700fd11)。

手动刷新（Manual Refresh）。

<a id="r_ga06fe36ad6ef61554bd1a46d7f0fefe3b"></a>

```c
#define PAC_REFRESH_AUTO_WAIT 1
```

相关声明：[PAC_REFRESH_AUTO_WAIT](../api_update_memory_topic_reference/P013_PAC194X API主题.md#ga06fe36ad6ef61554bd1a46d7f0fefe3b)。

自动刷新（Automatic Refresh），等待有效数据。

<a id="r_ga753b24688d14a0ccac99da1ba7abd308"></a>

```c
#define PAC_REFRESH_AUTO_NOWAIT 2
```

相关声明：[PAC_REFRESH_AUTO_NOWAIT](../api_update_memory_topic_reference/P013_PAC194X API主题.md#ga753b24688d14a0ccac99da1ba7abd308)。

自动刷新（Automatic Refresh），不等待。


## 9.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P211_pac194x.h_源码浏览.md)
- [PAC_UNIPOLAR_FSR](../api_update_memory_topic_reference/P013_PAC194X API主题.md#ga69132e5c34fa02a6bfa36ae4bf1ecd27)
- [PAC_BIPOLAR_FSR](../api_update_memory_topic_reference/P013_PAC194X API主题.md#gafdc80d9ece34bd9a2d39d649b7971ec1)
- [PAC_BIPOLAR_HALF_FSR](../api_update_memory_topic_reference/P013_PAC194X API主题.md#ga4db614817516296166b2524ab78c447f)
- [PAC_ACCUM_VPOWER](../api_update_memory_topic_reference/P013_PAC194X API主题.md#ga3090e6340cf34c043924b3a30fea4c79)
- [PAC_ACCUM_VSENSE](../api_update_memory_topic_reference/P013_PAC194X API主题.md#ga264aab83fe304ab142ac139a9de53396)
- [PAC_ACCUM_VBUS](../api_update_memory_topic_reference/P013_PAC194X API主题.md#ga12f7026116719fbcdb0ed959ca165025)
- [PAC_REFRESH_MANUAL](../api_update_memory_topic_reference/P013_PAC194X API主题.md#ga11c894871e498d98606f96469700fd11)
- [PAC_REFRESH_AUTO_WAIT](../api_update_memory_topic_reference/P013_PAC194X API主题.md#ga06fe36ad6ef61554bd1a46d7f0fefe3b)
- [PAC_REFRESH_AUTO_NOWAIT](../api_update_memory_topic_reference/P013_PAC194X API主题.md#ga753b24688d14a0ccac99da1ba7abd308)

<a id="header-details"></a>

---

[上一章](P008_zephyr__drivers__misc__nxp_rtxxx_dsp_ctrl__nxp_rtxxx_dsp_ctrl.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P010_zephyr__dt-bindings__sensor__tmp11x.h_文件参考.md)
