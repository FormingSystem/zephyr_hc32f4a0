---
id: learning.zephyr-docs.api-file-system-device-reference.page-49
title: zephyr__dt-bindings__sensor__stts22h.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stts22h_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第49章\_zephyr\_\_dt-bindings\_\_sensor\_\_stts22h.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/stts22h_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

the ST STTS22H temperature sensor的设备树绑定常量（Devicetree Binding Constants）。

查看此文件的源码。

<a id="details"></a>

the ST STTS22H temperature sensor的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 49.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 输出数据率选项（Output data rate options）

设备树 `sampling-rate` 属性的取值。

<a id="r_ga2c2da98606a8b88b279d0138be13cb76"></a>

```c
#define STTS22H_POWER_DOWN 0x00
```

相关声明：[STTS22H_POWER_DOWN](../api_auxiliary_topic_reference/P016_STTS22H API主题.md#ga2c2da98606a8b88b279d0138be13cb76)。

掉电（Power-down）。

<a id="r_ga7c93186f94872a54a8ee97b154aa13ab"></a>

```c
#define STTS22H_ONE_SHOT 0x01
```

相关声明：[STTS22H_ONE_SHOT](../api_auxiliary_topic_reference/P016_STTS22H API主题.md#ga7c93186f94872a54a8ee97b154aa13ab)。

单次转换（one-shot conversion）。

<a id="r_gaa152218e7bf6be16cbee2f7e480d8e4d"></a>

```c
#define STTS22H_1Hz 0x04
```

相关声明：[STTS22H_1Hz](../api_auxiliary_topic_reference/P016_STTS22H API主题.md#gaa152218e7bf6be16cbee2f7e480d8e4d)。

频率：1 Hz。

<a id="r_ga2cefaa04bb4d8e855301088b3e9ed327"></a>

```c
#define STTS22H_25Hz 0x02
```

相关声明：[STTS22H_25Hz](../api_auxiliary_topic_reference/P016_STTS22H API主题.md#ga2cefaa04bb4d8e855301088b3e9ed327)。

频率：25 Hz。

<a id="r_ga43a2f447c68beab340f39b10f9a6df7b"></a>

```c
#define STTS22H_50Hz 0x12
```

相关声明：[STTS22H_50Hz](../api_auxiliary_topic_reference/P016_STTS22H API主题.md#ga43a2f447c68beab340f39b10f9a6df7b)。

频率：50 Hz。

<a id="r_ga9a6ff258f66017556825cad883744594"></a>

```c
#define STTS22H_100Hz 0x22
```

相关声明：[STTS22H_100Hz](../api_auxiliary_topic_reference/P016_STTS22H API主题.md#ga9a6ff258f66017556825cad883744594)。

频率：100 Hz。

<a id="r_ga572f26908bc83a3bb7b9f4daf165f855"></a>

```c
#define STTS22H_200Hz 0x32
```

相关声明：[STTS22H_200Hz](../api_auxiliary_topic_reference/P016_STTS22H API主题.md#ga572f26908bc83a3bb7b9f4daf165f855)。

频率：200 Hz。


## 49.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P842_stts22h.h_源码浏览.md)
- [STTS22H_POWER_DOWN](../api_auxiliary_topic_reference/P016_STTS22H API主题.md#ga2c2da98606a8b88b279d0138be13cb76)
- [STTS22H_ONE_SHOT](../api_auxiliary_topic_reference/P016_STTS22H API主题.md#ga7c93186f94872a54a8ee97b154aa13ab)
- [STTS22H_1Hz](../api_auxiliary_topic_reference/P016_STTS22H API主题.md#gaa152218e7bf6be16cbee2f7e480d8e4d)
- [STTS22H_25Hz](../api_auxiliary_topic_reference/P016_STTS22H API主题.md#ga2cefaa04bb4d8e855301088b3e9ed327)
- [STTS22H_50Hz](../api_auxiliary_topic_reference/P016_STTS22H API主题.md#ga43a2f447c68beab340f39b10f9a6df7b)
- [STTS22H_100Hz](../api_auxiliary_topic_reference/P016_STTS22H API主题.md#ga9a6ff258f66017556825cad883744594)
- [STTS22H_200Hz](../api_auxiliary_topic_reference/P016_STTS22H API主题.md#ga572f26908bc83a3bb7b9f4daf165f855)

<a id="header-details"></a>

---

[上一章](P048_zephyr__drivers__stepper__stepper_trinamic.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P050_zephyr__llext__symbol.h_文件参考.md)
