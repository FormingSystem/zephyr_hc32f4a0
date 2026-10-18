---
id: learning.zephyr-docs.api-file-service-interface-reference.page-32
title: zephyr__dt-bindings__sensor__lis2de12.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/lis2de12_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第32章\_zephyr\_\_dt-bindings\_\_sensor\_\_lis2de12.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/lis2de12_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

the ST LIS2DE12 accelerometer的设备树绑定常量（Devicetree Binding Constants）。

查看此文件的源码。

<a id="details"></a>

the ST LIS2DE12 accelerometer的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 32.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 加速度计满量程范围（Accelerometer full-scale range）

设备树 `accel-range` 属性的取值。

<a id="r_ga4d98a2437d4189112bf8de962a6427c5"></a>

```c
#define LIS2DE12_DT_FS_2G 0
```

相关声明：[LIS2DE12_DT_FS_2G](../api_vector_pipeline_topic_reference/P012_LIS2DE12 API主题.md#ga4d98a2437d4189112bf8de962a6427c5)。

量程（range）：±2 g。

<a id="r_ga28ea756e9426fef814d34e8f8e416373"></a>

```c
#define LIS2DE12_DT_FS_4G 1
```

相关声明：[LIS2DE12_DT_FS_4G](../api_vector_pipeline_topic_reference/P012_LIS2DE12 API主题.md#ga28ea756e9426fef814d34e8f8e416373)。

量程（range）：±4 g。

<a id="r_ga9e527343fd8f40e87698ab4f2095a09c"></a>

```c
#define LIS2DE12_DT_FS_8G 2
```

相关声明：[LIS2DE12_DT_FS_8G](../api_vector_pipeline_topic_reference/P012_LIS2DE12 API主题.md#ga9e527343fd8f40e87698ab4f2095a09c)。

量程（range）：±8 g。

<a id="r_ga5a79ea2d22261f2cbff1a920165c3614"></a>

```c
#define LIS2DE12_DT_FS_16G 3
```

相关声明：[LIS2DE12_DT_FS_16G](../api_vector_pipeline_topic_reference/P012_LIS2DE12 API主题.md#ga5a79ea2d22261f2cbff1a920165c3614)。

量程（range）：±16 g。

<a id="define-members-1"></a>

### 加速度计输出数据率（Accelerometer output data rate）

设备树（Devicetree）属性 `accel-odr` 的取值。

<a id="r_ga6fbd76dfbed77dbb642f6174e41b4933"></a>

```c
#define LIS2DE12_DT_ODR_OFF 0x00
```

相关声明：[LIS2DE12_DT_ODR_OFF](../api_vector_pipeline_topic_reference/P012_LIS2DE12 API主题.md#ga6fbd76dfbed77dbb642f6174e41b4933)。

掉电（Power-down）。

<a id="r_gaeb564c25b94d793c58cb0c54ce04acf5"></a>

```c
#define LIS2DE12_DT_ODR_AT_1Hz 0x01
```

相关声明：[LIS2DE12_DT_ODR_AT_1Hz](../api_vector_pipeline_topic_reference/P012_LIS2DE12 API主题.md#gaeb564c25b94d793c58cb0c54ce04acf5)。

1 Hz，正常（Normal）模式。

<a id="r_gad0a75e097c965995ed8e46cf93585cf6"></a>

```c
#define LIS2DE12_DT_ODR_AT_10Hz 0x02
```

相关声明：[LIS2DE12_DT_ODR_AT_10Hz](../api_vector_pipeline_topic_reference/P012_LIS2DE12 API主题.md#gad0a75e097c965995ed8e46cf93585cf6)。

10 Hz，正常（Normal）模式。

<a id="r_gab5e906715ed2c45f4794a9d069d56921"></a>

```c
#define LIS2DE12_DT_ODR_AT_25Hz 0x03
```

相关声明：[LIS2DE12_DT_ODR_AT_25Hz](../api_vector_pipeline_topic_reference/P012_LIS2DE12 API主题.md#gab5e906715ed2c45f4794a9d069d56921)。

25 Hz，正常（Normal）模式。

<a id="r_gaa751bddcce56dba2fe8209bd919692ef"></a>

```c
#define LIS2DE12_DT_ODR_AT_50Hz 0x04
```

相关声明：[LIS2DE12_DT_ODR_AT_50Hz](../api_vector_pipeline_topic_reference/P012_LIS2DE12 API主题.md#gaa751bddcce56dba2fe8209bd919692ef)。

50 Hz，正常（Normal）模式。

<a id="r_gab0d6486440d1a759bf86311237803814"></a>

```c
#define LIS2DE12_DT_ODR_AT_100Hz 0x05
```

相关声明：[LIS2DE12_DT_ODR_AT_100Hz](../api_vector_pipeline_topic_reference/P012_LIS2DE12 API主题.md#gab0d6486440d1a759bf86311237803814)。

100 Hz，正常（Normal）模式。

<a id="r_gabb6ab746392ec390affcff0b63208fcd"></a>

```c
#define LIS2DE12_DT_ODR_AT_200Hz 0x06
```

相关声明：[LIS2DE12_DT_ODR_AT_200Hz](../api_vector_pipeline_topic_reference/P012_LIS2DE12 API主题.md#gabb6ab746392ec390affcff0b63208fcd)。

200 Hz，正常（Normal）模式。

<a id="r_ga02142274ee4945c67385ff49b322ad66"></a>

```c
#define LIS2DE12_DT_ODR_AT_400Hz 0x07
```

相关声明：[LIS2DE12_DT_ODR_AT_400Hz](../api_vector_pipeline_topic_reference/P012_LIS2DE12 API主题.md#ga02142274ee4945c67385ff49b322ad66)。

400 Hz，正常（Normal）模式。

<a id="r_gaa14ef617b90cb5f8453eab1837eeb5d7"></a>

```c
#define LIS2DE12_DT_ODR_AT_1kHz620 0x08
```

相关声明：[LIS2DE12_DT_ODR_AT_1kHz620](../api_vector_pipeline_topic_reference/P012_LIS2DE12 API主题.md#gaa14ef617b90cb5f8453eab1837eeb5d7)。

1620 Hz，正常（Normal）模式。

<a id="r_ga817a85c45d4dfb94933715f2b1492ca2"></a>

```c
#define LIS2DE12_DT_ODR_AT_5kHz376 0x09
```

相关声明：[LIS2DE12_DT_ODR_AT_5kHz376](../api_vector_pipeline_topic_reference/P012_LIS2DE12 API主题.md#ga817a85c45d4dfb94933715f2b1492ca2)。

5376 Hz，正常（Normal）模式。


## 32.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P441_lis2de12.h_源码浏览.md)
- [LIS2DE12_DT_FS_2G](../api_vector_pipeline_topic_reference/P012_LIS2DE12 API主题.md#ga4d98a2437d4189112bf8de962a6427c5)
- [LIS2DE12_DT_FS_4G](../api_vector_pipeline_topic_reference/P012_LIS2DE12 API主题.md#ga28ea756e9426fef814d34e8f8e416373)
- [LIS2DE12_DT_FS_8G](../api_vector_pipeline_topic_reference/P012_LIS2DE12 API主题.md#ga9e527343fd8f40e87698ab4f2095a09c)
- [LIS2DE12_DT_FS_16G](../api_vector_pipeline_topic_reference/P012_LIS2DE12 API主题.md#ga5a79ea2d22261f2cbff1a920165c3614)
- [LIS2DE12_DT_ODR_OFF](../api_vector_pipeline_topic_reference/P012_LIS2DE12 API主题.md#ga6fbd76dfbed77dbb642f6174e41b4933)
- [LIS2DE12_DT_ODR_AT_1Hz](../api_vector_pipeline_topic_reference/P012_LIS2DE12 API主题.md#gaeb564c25b94d793c58cb0c54ce04acf5)
- [LIS2DE12_DT_ODR_AT_10Hz](../api_vector_pipeline_topic_reference/P012_LIS2DE12 API主题.md#gad0a75e097c965995ed8e46cf93585cf6)
- [LIS2DE12_DT_ODR_AT_25Hz](../api_vector_pipeline_topic_reference/P012_LIS2DE12 API主题.md#gab5e906715ed2c45f4794a9d069d56921)
- [LIS2DE12_DT_ODR_AT_50Hz](../api_vector_pipeline_topic_reference/P012_LIS2DE12 API主题.md#gaa751bddcce56dba2fe8209bd919692ef)
- [LIS2DE12_DT_ODR_AT_100Hz](../api_vector_pipeline_topic_reference/P012_LIS2DE12 API主题.md#gab0d6486440d1a759bf86311237803814)
- [LIS2DE12_DT_ODR_AT_200Hz](../api_vector_pipeline_topic_reference/P012_LIS2DE12 API主题.md#gabb6ab746392ec390affcff0b63208fcd)
- [LIS2DE12_DT_ODR_AT_400Hz](../api_vector_pipeline_topic_reference/P012_LIS2DE12 API主题.md#ga02142274ee4945c67385ff49b322ad66)
- [LIS2DE12_DT_ODR_AT_1kHz620](../api_vector_pipeline_topic_reference/P012_LIS2DE12 API主题.md#gaa14ef617b90cb5f8453eab1837eeb5d7)
- [LIS2DE12_DT_ODR_AT_5kHz376](../api_vector_pipeline_topic_reference/P012_LIS2DE12 API主题.md#ga817a85c45d4dfb94933715f2b1492ca2)

<a id="header-details"></a>

---

[上一章](P031_____w__zephyr__zephyr__kernel__include__kernel_arch_interface.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P033_zephyr__net__lldp.h_文件参考.md)
