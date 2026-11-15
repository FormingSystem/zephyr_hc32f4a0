---
id: learning.zephyr-docs.api-file-network-device-reference.page-10
title: zephyr__dt-bindings__sensor__tmp11x.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2sensor_2tmp11x_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_zephyr\_\_dt-bindings\_\_sensor\_\_tmp11x.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2sensor_2tmp11x_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

the TI TMP11x temperature sensors的设备树绑定常量（Devicetree Binding Constants）。

查看此文件的源码。

<a id="details"></a>

the TI TMP11x temperature sensors的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 10.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 输出数据率选项（Output data rate options）

设备树 `odr` 属性的取值。

<a id="r_ga4693b7e433f4dc51f95e11a8934643a9"></a>

```c
#define TMP11X_DT_ODR_15_5_MS 0
```

相关声明：[TMP11X_DT_ODR_15_5_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html#ga4693b7e433f4dc51f95e11a8934643a9)。

15.5 毫秒（ms）。

<a id="r_ga17cb6c1c3e49a8da2196ae938368ecfb"></a>

```c
#define TMP11X_DT_ODR_125_MS 0x80
```

相关声明：[TMP11X_DT_ODR_125_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html#ga17cb6c1c3e49a8da2196ae938368ecfb)。

时间：125 ms。

<a id="r_ga1a842507ebce470f3a380e1140021925"></a>

```c
#define TMP11X_DT_ODR_250_MS 0x100
```

相关声明：[TMP11X_DT_ODR_250_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html#ga1a842507ebce470f3a380e1140021925)。

时间：250 ms。

<a id="r_gaa071b4ad7ac75ed781015b1674bf5edd"></a>

```c
#define TMP11X_DT_ODR_500_MS 0x180
```

相关声明：[TMP11X_DT_ODR_500_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html#gaa071b4ad7ac75ed781015b1674bf5edd)。

时间：500 ms。

<a id="r_ga7e2ad50b9864468c6f00cccdab608658"></a>

```c
#define TMP11X_DT_ODR_1000_MS 0x200
```

相关声明：[TMP11X_DT_ODR_1000_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html#ga7e2ad50b9864468c6f00cccdab608658)。

时间：1000 ms。

<a id="r_ga0f64f79e1dbbcb29ae6871380a446ca4"></a>

```c
#define TMP11X_DT_ODR_4000_MS 0x280
```

相关声明：[TMP11X_DT_ODR_4000_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html#ga0f64f79e1dbbcb29ae6871380a446ca4)。

4000 毫秒（ms）。

<a id="r_ga29b10bb8a1070968983b72627ed4a2b3"></a>

```c
#define TMP11X_DT_ODR_8000_MS 0x300
```

相关声明：[TMP11X_DT_ODR_8000_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html#ga29b10bb8a1070968983b72627ed4a2b3)。

8000 毫秒（ms）。

<a id="r_ga4f7689b5d4a5b72da402c3edb85f14d8"></a>

```c
#define TMP11X_DT_ODR_16000_MS 0x380
```

相关声明：[TMP11X_DT_ODR_16000_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html#ga4f7689b5d4a5b72da402c3edb85f14d8)。

16000 毫秒（ms）。

<a id="define-members-1"></a>

### 平均处理／过采样选项（Averaging/Oversampling Options）

设备树（Devicetree）属性 `oversampling` 的取值。

<a id="r_gad0340558552e92935044952ba5d1c2ac"></a>

```c
#define TMP11X_DT_OVERSAMPLING_1 0
```

相关声明：[TMP11X_DT_OVERSAMPLING_1](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html#gad0340558552e92935044952ba5d1c2ac)。

对 1 次转换取平均（Conversions Averaged）。

<a id="r_ga5f7db14f47703ae89bd066c71d0f8267"></a>

```c
#define TMP11X_DT_OVERSAMPLING_8 0x20
```

相关声明：[TMP11X_DT_OVERSAMPLING_8](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html#ga5f7db14f47703ae89bd066c71d0f8267)。

对 8 次转换取平均（Conversions Averaged）。

<a id="r_ga74cf0d96ee648e9278e241c9052c868d"></a>

```c
#define TMP11X_DT_OVERSAMPLING_32 0x40
```

相关声明：[TMP11X_DT_OVERSAMPLING_32](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html#ga74cf0d96ee648e9278e241c9052c868d)。

对 32 次转换取平均（Conversions Averaged）。

<a id="r_ga5736162b8a82a591c95bc40d48c96339"></a>

```c
#define TMP11X_DT_OVERSAMPLING_64 0x60
```

相关声明：[TMP11X_DT_OVERSAMPLING_64](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html#ga5736162b8a82a591c95bc40d48c96339)。

对 64 次转换取平均（Conversions Averaged）。


## 10.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P213_tmp11x.h_源码浏览.md)
- [TMP11X_DT_ODR_15_5_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html#ga4693b7e433f4dc51f95e11a8934643a9)
- [TMP11X_DT_ODR_125_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html#ga17cb6c1c3e49a8da2196ae938368ecfb)
- [TMP11X_DT_ODR_250_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html#ga1a842507ebce470f3a380e1140021925)
- [TMP11X_DT_ODR_500_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html#gaa071b4ad7ac75ed781015b1674bf5edd)
- [TMP11X_DT_ODR_1000_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html#ga7e2ad50b9864468c6f00cccdab608658)
- [TMP11X_DT_ODR_4000_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html#ga0f64f79e1dbbcb29ae6871380a446ca4)
- [TMP11X_DT_ODR_8000_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html#ga29b10bb8a1070968983b72627ed4a2b3)
- [TMP11X_DT_ODR_16000_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html#ga4f7689b5d4a5b72da402c3edb85f14d8)
- [TMP11X_DT_OVERSAMPLING_1](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html#gad0340558552e92935044952ba5d1c2ac)
- [TMP11X_DT_OVERSAMPLING_8](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html#ga5f7db14f47703ae89bd066c71d0f8267)
- [TMP11X_DT_OVERSAMPLING_32](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html#ga74cf0d96ee648e9278e241c9052c868d)
- [TMP11X_DT_OVERSAMPLING_64](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html#ga5736162b8a82a591c95bc40d48c96339)

<a id="header-details"></a>

---

[上一章](P009_zephyr__dt-bindings__sensor__pac194x.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P011_zephyr__net__ethernet_vlan.h_文件参考.md)
