---
id: learning.zephyr-docs.api-file-system-device-reference.page-24
title: zephyr__dt-bindings__sensor__lps22hh.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/lps22hh_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第24章\_zephyr\_\_dt-bindings\_\_sensor\_\_lps22hh.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/lps22hh_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

the ST LPS22HH pressure sensor的设备树绑定常量（Devicetree Binding Constants）。

查看此文件的源码。

<a id="details"></a>

the ST LPS22HH pressure sensor的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 24.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 输出数据率选项（Output data rate options）

设备树 `odr` 属性的取值。

<a id="r_ga8c40f6451b73b5dab3af90c026589aa5"></a>

```c
#define LPS22HH_DT_ODR_POWER_DOWN 0
```

相关声明：[LPS22HH_DT_ODR_POWER_DOWN](../api_connection_topic_reference/P012_LPS22HH API主题.md#ga8c40f6451b73b5dab3af90c026589aa5)。

掉电（Power-down）。

<a id="r_ga0417e7a3bb172d181ec4d2d9285469e8"></a>

```c
#define LPS22HH_DT_ODR_1HZ 1
```

相关声明：[LPS22HH_DT_ODR_1HZ](../api_connection_topic_reference/P012_LPS22HH API主题.md#ga0417e7a3bb172d181ec4d2d9285469e8)。

频率：1 Hz。

<a id="r_ga1c332941d39229a715862e187181287b"></a>

```c
#define LPS22HH_DT_ODR_10HZ 2
```

相关声明：[LPS22HH_DT_ODR_10HZ](../api_connection_topic_reference/P012_LPS22HH API主题.md#ga1c332941d39229a715862e187181287b)。

频率：10 Hz。

<a id="r_gaa4ac2ccf60d30bd61225ff184c58f62f"></a>

```c
#define LPS22HH_DT_ODR_25HZ 3
```

相关声明：[LPS22HH_DT_ODR_25HZ](../api_connection_topic_reference/P012_LPS22HH API主题.md#gaa4ac2ccf60d30bd61225ff184c58f62f)。

频率：25 Hz。

<a id="r_ga523f313a2ec38dd59e48ad77e2361056"></a>

```c
#define LPS22HH_DT_ODR_50HZ 4
```

相关声明：[LPS22HH_DT_ODR_50HZ](../api_connection_topic_reference/P012_LPS22HH API主题.md#ga523f313a2ec38dd59e48ad77e2361056)。

频率：50 Hz。

<a id="r_ga11a0a1ab6cacd7c5dbd0c151242fba53"></a>

```c
#define LPS22HH_DT_ODR_75HZ 5
```

相关声明：[LPS22HH_DT_ODR_75HZ](../api_connection_topic_reference/P012_LPS22HH API主题.md#ga11a0a1ab6cacd7c5dbd0c151242fba53)。

频率：75 Hz。

<a id="r_ga6b2f19c118c9d519c6cc6219b041762c"></a>

```c
#define LPS22HH_DT_ODR_100HZ 6
```

相关声明：[LPS22HH_DT_ODR_100HZ](../api_connection_topic_reference/P012_LPS22HH API主题.md#ga6b2f19c118c9d519c6cc6219b041762c)。

频率：100 Hz。

<a id="r_ga53feaea4e3e20b1a95cad0007d1b3262"></a>

```c
#define LPS22HH_DT_ODR_200HZ 7
```

相关声明：[LPS22HH_DT_ODR_200HZ](../api_connection_topic_reference/P012_LPS22HH API主题.md#ga53feaea4e3e20b1a95cad0007d1b3262)。

频率：200 Hz。


## 24.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P457_lps22hh.h_源码浏览.md)
- [LPS22HH_DT_ODR_POWER_DOWN](../api_connection_topic_reference/P012_LPS22HH API主题.md#ga8c40f6451b73b5dab3af90c026589aa5)
- [LPS22HH_DT_ODR_1HZ](../api_connection_topic_reference/P012_LPS22HH API主题.md#ga0417e7a3bb172d181ec4d2d9285469e8)
- [LPS22HH_DT_ODR_10HZ](../api_connection_topic_reference/P012_LPS22HH API主题.md#ga1c332941d39229a715862e187181287b)
- [LPS22HH_DT_ODR_25HZ](../api_connection_topic_reference/P012_LPS22HH API主题.md#gaa4ac2ccf60d30bd61225ff184c58f62f)
- [LPS22HH_DT_ODR_50HZ](../api_connection_topic_reference/P012_LPS22HH API主题.md#ga523f313a2ec38dd59e48ad77e2361056)
- [LPS22HH_DT_ODR_75HZ](../api_connection_topic_reference/P012_LPS22HH API主题.md#ga11a0a1ab6cacd7c5dbd0c151242fba53)
- [LPS22HH_DT_ODR_100HZ](../api_connection_topic_reference/P012_LPS22HH API主题.md#ga6b2f19c118c9d519c6cc6219b041762c)
- [LPS22HH_DT_ODR_200HZ](../api_connection_topic_reference/P012_LPS22HH API主题.md#ga53feaea4e3e20b1a95cad0007d1b3262)

<a id="header-details"></a>

---

[上一章](P023_zephyr__drivers__led_strip.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P025_zephyr__pmci__mctp__mctp_memory.h_文件参考.md)
