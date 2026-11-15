---
id: learning.zephyr-docs.api-file-system-power-reference.page-23
title: zephyr__dt-bindings__sensor__lis2ds12.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/lis2ds12_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第23章\_zephyr\_\_dt-bindings\_\_sensor\_\_lis2ds12.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/lis2ds12_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

the ST LIS2DS12 accelerometer的设备树绑定常量（Devicetree Binding Constants）。

查看此文件的源码。

<a id="details"></a>

the ST LIS2DS12 accelerometer的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 23.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 电源模式（Power Modes）

设备树属性（Devicetree Property）`power-mode` 的取值。

<a id="r_gaebfdbefbdc2f17440413ba44911e8f3c"></a>

```c
#define LIS2DS12_DT_POWER_DOWN 0
```

相关声明：[LIS2DS12_DT_POWER_DOWN](../api_transport_control_topic_reference/P010_LIS2DS12 API主题.md#gaebfdbefbdc2f17440413ba44911e8f3c)。

掉电（Power-down）。

<a id="r_ga93264cc6b09ef363a51a77d81e365083"></a>

```c
#define LIS2DS12_DT_LOW_POWER 1
```

相关声明：[LIS2DS12_DT_LOW_POWER](../api_transport_control_topic_reference/P010_LIS2DS12 API主题.md#ga93264cc6b09ef363a51a77d81e365083)。

低功耗模式（Low-power Mode）。

<a id="r_gaa94a782ff303956dbbc99dbcf59819f8"></a>

```c
#define LIS2DS12_DT_HIGH_RESOLUTION 2
```

相关声明：[LIS2DS12_DT_HIGH_RESOLUTION](../api_transport_control_topic_reference/P010_LIS2DS12 API主题.md#gaa94a782ff303956dbbc99dbcf59819f8)。

高分辨率模式（High-resolution Mode）。

<a id="r_gac66a29d7065bb2b94b471f704cd6ca58"></a>

```c
#define LIS2DS12_DT_HIGH_FREQUENCY 3
```

相关声明：[LIS2DS12_DT_HIGH_FREQUENCY](../api_transport_control_topic_reference/P010_LIS2DS12 API主题.md#gac66a29d7065bb2b94b471f704cd6ca58)。

高频模式（High-frequency Mode）。

<a id="define-members-1"></a>

### 输出数据率选项（Output data rate options）

设备树 `odr` 属性的取值。

LP：低功耗（Low-power）；HR：高分辨率（High-resolution）；HF：高频模式（High-frequency Mode）。

<a id="r_ga18ee240515cce324ee31ff7d8201a933"></a>

```c
#define LIS2DS12_DT_ODR_OFF 0
```

相关声明：[LIS2DS12_DT_ODR_OFF](../api_transport_control_topic_reference/P010_LIS2DS12 API主题.md#ga18ee240515cce324ee31ff7d8201a933)。

掉电（Power-down）。

<a id="r_gab222c78221c0a9d4ab1ce502c09103a5"></a>

```c
#define LIS2DS12_DT_ODR_1Hz_LP 1
```

相关声明：[LIS2DS12_DT_ODR_1Hz_LP](../api_transport_control_topic_reference/P010_LIS2DS12 API主题.md#gab222c78221c0a9d4ab1ce502c09103a5)。

1 Hz（仅适用于低功耗（LP）模式）。

<a id="r_ga304edbdda283cb5274988054c969ca43"></a>

```c
#define LIS2DS12_DT_ODR_12Hz5 2
```

相关声明：[LIS2DS12_DT_ODR_12Hz5](../api_transport_control_topic_reference/P010_LIS2DS12 API主题.md#ga304edbdda283cb5274988054c969ca43)。

12.5 Hz（适用于低功耗（LP）或高分辨率（HR）模式）。

<a id="r_gad37986618e794a9f7d59f521972ebc3b"></a>

```c
#define LIS2DS12_DT_ODR_25Hz 3
```

相关声明：[LIS2DS12_DT_ODR_25Hz](../api_transport_control_topic_reference/P010_LIS2DS12 API主题.md#gad37986618e794a9f7d59f521972ebc3b)。

25 Hz（适用于低功耗（LP）或高分辨率（HR）模式）。

<a id="r_ga428a9dea9f3bbd9e60ad533cdae334f8"></a>

```c
#define LIS2DS12_DT_ODR_50Hz 4
```

相关声明：[LIS2DS12_DT_ODR_50Hz](../api_transport_control_topic_reference/P010_LIS2DS12 API主题.md#ga428a9dea9f3bbd9e60ad533cdae334f8)。

50 Hz（适用于低功耗（LP）或高分辨率（HR）模式）。

<a id="r_ga07c6d9c6b044b749eed4db77d899d5ce"></a>

```c
#define LIS2DS12_DT_ODR_100Hz 5
```

相关声明：[LIS2DS12_DT_ODR_100Hz](../api_transport_control_topic_reference/P010_LIS2DS12 API主题.md#ga07c6d9c6b044b749eed4db77d899d5ce)。

100 Hz（适用于低功耗（LP）或高分辨率（HR）模式）。

<a id="r_gafc77b3b419461fa4744a83643ece77d4"></a>

```c
#define LIS2DS12_DT_ODR_200Hz 6
```

相关声明：[LIS2DS12_DT_ODR_200Hz](../api_transport_control_topic_reference/P010_LIS2DS12 API主题.md#gafc77b3b419461fa4744a83643ece77d4)。

200 Hz（适用于低功耗（LP）或高分辨率（HR）模式）。

<a id="r_ga97749570c84f44060280b17b1b42b19b"></a>

```c
#define LIS2DS12_DT_ODR_400Hz 7
```

相关声明：[LIS2DS12_DT_ODR_400Hz](../api_transport_control_topic_reference/P010_LIS2DS12 API主题.md#ga97749570c84f44060280b17b1b42b19b)。

400 Hz（适用于低功耗（LP）或高分辨率（HR）模式）。

<a id="r_gab7d0fb3bc0c15b714bda52d6e3435afc"></a>

```c
#define LIS2DS12_DT_ODR_800Hz 8
```

相关声明：[LIS2DS12_DT_ODR_800Hz](../api_transport_control_topic_reference/P010_LIS2DS12 API主题.md#gab7d0fb3bc0c15b714bda52d6e3435afc)。

800 Hz（适用于低功耗（LP）或高分辨率（HR）模式）。

<a id="r_ga11f5aede52debdbc639791b28777504a"></a>

```c
#define LIS2DS12_DT_ODR_1600Hz 9
```

相关声明：[LIS2DS12_DT_ODR_1600Hz](../api_transport_control_topic_reference/P010_LIS2DS12 API主题.md#ga11f5aede52debdbc639791b28777504a)。

1600 Hz（仅适用于高频（HF）模式）。

<a id="r_ga191a8680a6dff5ed459fbfd24aa04c2f"></a>

```c
#define LIS2DS12_DT_ODR_3200Hz_HF 10
```

相关声明：[LIS2DS12_DT_ODR_3200Hz_HF](../api_transport_control_topic_reference/P010_LIS2DS12 API主题.md#ga191a8680a6dff5ed459fbfd24aa04c2f)。

3200 Hz（仅适用于高频（HF）模式）。

<a id="r_ga3e06d2a0811d0aa1544e77eb5ee6a4a9"></a>

```c
#define LIS2DS12_DT_ODR_6400Hz_HF 11
```

相关声明：[LIS2DS12_DT_ODR_6400Hz_HF](../api_transport_control_topic_reference/P010_LIS2DS12 API主题.md#ga3e06d2a0811d0aa1544e77eb5ee6a4a9)。

6400 Hz（仅适用于高频（HF）模式）。


## 23.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P442_lis2ds12.h_源码浏览.md)
- [LIS2DS12_DT_POWER_DOWN](../api_transport_control_topic_reference/P010_LIS2DS12 API主题.md#gaebfdbefbdc2f17440413ba44911e8f3c)
- [LIS2DS12_DT_LOW_POWER](../api_transport_control_topic_reference/P010_LIS2DS12 API主题.md#ga93264cc6b09ef363a51a77d81e365083)
- [LIS2DS12_DT_HIGH_RESOLUTION](../api_transport_control_topic_reference/P010_LIS2DS12 API主题.md#gaa94a782ff303956dbbc99dbcf59819f8)
- [LIS2DS12_DT_HIGH_FREQUENCY](../api_transport_control_topic_reference/P010_LIS2DS12 API主题.md#gac66a29d7065bb2b94b471f704cd6ca58)
- [LIS2DS12_DT_ODR_OFF](../api_transport_control_topic_reference/P010_LIS2DS12 API主题.md#ga18ee240515cce324ee31ff7d8201a933)
- [LIS2DS12_DT_ODR_1Hz_LP](../api_transport_control_topic_reference/P010_LIS2DS12 API主题.md#gab222c78221c0a9d4ab1ce502c09103a5)
- [LIS2DS12_DT_ODR_12Hz5](../api_transport_control_topic_reference/P010_LIS2DS12 API主题.md#ga304edbdda283cb5274988054c969ca43)
- [LIS2DS12_DT_ODR_25Hz](../api_transport_control_topic_reference/P010_LIS2DS12 API主题.md#gad37986618e794a9f7d59f521972ebc3b)
- [LIS2DS12_DT_ODR_50Hz](../api_transport_control_topic_reference/P010_LIS2DS12 API主题.md#ga428a9dea9f3bbd9e60ad533cdae334f8)
- [LIS2DS12_DT_ODR_100Hz](../api_transport_control_topic_reference/P010_LIS2DS12 API主题.md#ga07c6d9c6b044b749eed4db77d899d5ce)
- [LIS2DS12_DT_ODR_200Hz](../api_transport_control_topic_reference/P010_LIS2DS12 API主题.md#gafc77b3b419461fa4744a83643ece77d4)
- [LIS2DS12_DT_ODR_400Hz](../api_transport_control_topic_reference/P010_LIS2DS12 API主题.md#ga97749570c84f44060280b17b1b42b19b)
- [LIS2DS12_DT_ODR_800Hz](../api_transport_control_topic_reference/P010_LIS2DS12 API主题.md#gab7d0fb3bc0c15b714bda52d6e3435afc)
- [LIS2DS12_DT_ODR_1600Hz](../api_transport_control_topic_reference/P010_LIS2DS12 API主题.md#ga11f5aede52debdbc639791b28777504a)
- [LIS2DS12_DT_ODR_3200Hz_HF](../api_transport_control_topic_reference/P010_LIS2DS12 API主题.md#ga191a8680a6dff5ed459fbfd24aa04c2f)
- [LIS2DS12_DT_ODR_6400Hz_HF](../api_transport_control_topic_reference/P010_LIS2DS12 API主题.md#ga3e06d2a0811d0aa1544e77eb5ee6a4a9)

<a id="header-details"></a>

---

[上一章](P022_zephyr__bluetooth__classic__l2cap_br.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P024_zephyr__drivers__interrupt_controller__loapic.h_文件参考.md)
