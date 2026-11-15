---
id: learning.zephyr-docs.api-file-service-interface-reference.page-29
title: zephyr__dt-bindings__sensor__ism330dhcx.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ism330dhcx_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第29章\_zephyr\_\_dt-bindings\_\_sensor\_\_ism330dhcx.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ism330dhcx_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

the ST ISM330DHCX IMU的设备树绑定常量（Devicetree Binding Constants）。

查看此文件的源码。

<a id="details"></a>

the ST ISM330DHCX IMU的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 29.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 加速度计与陀螺仪输出数据率（Accelerometer and Gyroscope Output Data Rate）

设备树（Devicetree）属性 `accel-odr` 和 `gyro-odr` 的取值。

<a id="r_ga87a5e66db94487da96dfc641d1f361b7"></a>

```c
#define ISM330DHCX_DT_ODR_OFF 0x0
```

相关声明：[ISM330DHCX_DT_ODR_OFF](../api_vector_pipeline_topic_reference/P010_ISM330DHCX API主题.md#ga87a5e66db94487da96dfc641d1f361b7)。

掉电（Power-down）。

<a id="r_gabf89ada8b9ccb619405ae5a6b85b25c8"></a>

```c
#define ISM330DHCX_DT_ODR_12Hz5 0x1
```

相关声明：[ISM330DHCX_DT_ODR_12Hz5](../api_vector_pipeline_topic_reference/P010_ISM330DHCX API主题.md#gabf89ada8b9ccb619405ae5a6b85b25c8)。

频率：12.5 Hz。

<a id="r_ga8a13ead73def96a1eeadd80e36c24ec9"></a>

```c
#define ISM330DHCX_DT_ODR_26H 0x2
```

相关声明：[ISM330DHCX_DT_ODR_26H](../api_vector_pipeline_topic_reference/P010_ISM330DHCX API主题.md#ga8a13ead73def96a1eeadd80e36c24ec9)。

频率：26 Hz。

<a id="r_ga8e867da0f5762b9d92528e83da164d52"></a>

```c
#define ISM330DHCX_DT_ODR_52Hz 0x3
```

相关声明：[ISM330DHCX_DT_ODR_52Hz](../api_vector_pipeline_topic_reference/P010_ISM330DHCX API主题.md#ga8e867da0f5762b9d92528e83da164d52)。

频率：52 Hz。

<a id="r_ga7af183f35760d8e5846f27ba6772a8de"></a>

```c
#define ISM330DHCX_DT_ODR_104Hz 0x4
```

相关声明：[ISM330DHCX_DT_ODR_104Hz](../api_vector_pipeline_topic_reference/P010_ISM330DHCX API主题.md#ga7af183f35760d8e5846f27ba6772a8de)。

频率：104 Hz。

<a id="r_ga3ebda7f972a93b3983e6b999424a101c"></a>

```c
#define ISM330DHCX_DT_ODR_208Hz 0x5
```

相关声明：[ISM330DHCX_DT_ODR_208Hz](../api_vector_pipeline_topic_reference/P010_ISM330DHCX API主题.md#ga3ebda7f972a93b3983e6b999424a101c)。

频率：208 Hz。

<a id="r_ga841dc019b9d82260918954574732f2e2"></a>

```c
#define ISM330DHCX_DT_ODR_416Hz 0x6
```

相关声明：[ISM330DHCX_DT_ODR_416Hz](../api_vector_pipeline_topic_reference/P010_ISM330DHCX API主题.md#ga841dc019b9d82260918954574732f2e2)。

频率：416 Hz。

<a id="r_ga04c641e9e5d6ab3623dad897bf354885"></a>

```c
#define ISM330DHCX_DT_ODR_833Hz 0x7
```

相关声明：[ISM330DHCX_DT_ODR_833Hz](../api_vector_pipeline_topic_reference/P010_ISM330DHCX API主题.md#ga04c641e9e5d6ab3623dad897bf354885)。

频率：833 Hz。

<a id="r_gaeabe6f4e3818189feadb07b24a7094ca"></a>

```c
#define ISM330DHCX_DT_ODR_1666Hz 0x8
```

相关声明：[ISM330DHCX_DT_ODR_1666Hz](../api_vector_pipeline_topic_reference/P010_ISM330DHCX API主题.md#gaeabe6f4e3818189feadb07b24a7094ca)。

1666 Hz（赫兹）。

<a id="r_ga1b177f90f4b9fb03303891a604374ead"></a>

```c
#define ISM330DHCX_DT_ODR_3332Hz 0x9
```

相关声明：[ISM330DHCX_DT_ODR_3332Hz](../api_vector_pipeline_topic_reference/P010_ISM330DHCX API主题.md#ga1b177f90f4b9fb03303891a604374ead)。

3332 Hz（赫兹）。

<a id="r_gacdeff79efe2eb01d76f1db32bc99ee94"></a>

```c
#define ISM330DHCX_DT_ODR_6667Hz 0xa
```

相关声明：[ISM330DHCX_DT_ODR_6667Hz](../api_vector_pipeline_topic_reference/P010_ISM330DHCX API主题.md#gacdeff79efe2eb01d76f1db32bc99ee94)。

6667 Hz（赫兹）。

<a id="r_ga67a0d381f9856c2b13de67c2e75393d9"></a>

```c
#define ISM330DHCX_DT_ODR_1Hz6 0xb
```

相关声明：[ISM330DHCX_DT_ODR_1Hz6](../api_vector_pipeline_topic_reference/P010_ISM330DHCX API主题.md#ga67a0d381f9856c2b13de67c2e75393d9)。

1.6 Hz，低功耗（Low-power）模式。


## 29.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P413_ism330dhcx.h_源码浏览.md)
- [ISM330DHCX_DT_ODR_OFF](../api_vector_pipeline_topic_reference/P010_ISM330DHCX API主题.md#ga87a5e66db94487da96dfc641d1f361b7)
- [ISM330DHCX_DT_ODR_12Hz5](../api_vector_pipeline_topic_reference/P010_ISM330DHCX API主题.md#gabf89ada8b9ccb619405ae5a6b85b25c8)
- [ISM330DHCX_DT_ODR_26H](../api_vector_pipeline_topic_reference/P010_ISM330DHCX API主题.md#ga8a13ead73def96a1eeadd80e36c24ec9)
- [ISM330DHCX_DT_ODR_52Hz](../api_vector_pipeline_topic_reference/P010_ISM330DHCX API主题.md#ga8e867da0f5762b9d92528e83da164d52)
- [ISM330DHCX_DT_ODR_104Hz](../api_vector_pipeline_topic_reference/P010_ISM330DHCX API主题.md#ga7af183f35760d8e5846f27ba6772a8de)
- [ISM330DHCX_DT_ODR_208Hz](../api_vector_pipeline_topic_reference/P010_ISM330DHCX API主题.md#ga3ebda7f972a93b3983e6b999424a101c)
- [ISM330DHCX_DT_ODR_416Hz](../api_vector_pipeline_topic_reference/P010_ISM330DHCX API主题.md#ga841dc019b9d82260918954574732f2e2)
- [ISM330DHCX_DT_ODR_833Hz](../api_vector_pipeline_topic_reference/P010_ISM330DHCX API主题.md#ga04c641e9e5d6ab3623dad897bf354885)
- [ISM330DHCX_DT_ODR_1666Hz](../api_vector_pipeline_topic_reference/P010_ISM330DHCX API主题.md#gaeabe6f4e3818189feadb07b24a7094ca)
- [ISM330DHCX_DT_ODR_3332Hz](../api_vector_pipeline_topic_reference/P010_ISM330DHCX API主题.md#ga1b177f90f4b9fb03303891a604374ead)
- [ISM330DHCX_DT_ODR_6667Hz](../api_vector_pipeline_topic_reference/P010_ISM330DHCX API主题.md#gacdeff79efe2eb01d76f1db32bc99ee94)
- [ISM330DHCX_DT_ODR_1Hz6](../api_vector_pipeline_topic_reference/P010_ISM330DHCX API主题.md#ga67a0d381f9856c2b13de67c2e75393d9)

<a id="header-details"></a>

---

[上一章](P028_zephyr__drivers__interrupt_controller__intc_rz_ext_irq.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P030_zephyr__dt-bindings__sensor__ism6hg256x.h_文件参考.md)
