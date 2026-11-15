---
id: learning.zephyr-docs.api-file-reference.page-88
title: zephyr__dt-bindings__input__esp32-touch-sensor-input.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/esp32-touch-sensor-input_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第88章\_zephyr\_\_dt-bindings\_\_input\_\_esp32-touch-sensor-input.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/esp32-touch-sensor-input_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/dt-bindings/dt-util.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 88.1\_宏定义（Macros）

<a id="r_ae2a0cd54094572c8656231a5838cb66a"></a>

```c
#define ESP32_TOUCH_FILTER_MODE_IIR_4 0
```

相关声明：[ESP32_TOUCH_FILTER_MODE_IIR_4](#ae2a0cd54094572c8656231a5838cb66a)。

<a id="r_aaa4e199eb00344994a8f1545122bec4f"></a>

```c
#define ESP32_TOUCH_FILTER_MODE_IIR_8 1
```

相关声明：[ESP32_TOUCH_FILTER_MODE_IIR_8](#aaa4e199eb00344994a8f1545122bec4f)。

<a id="r_a2d049eb351a0d74411c267495a838c43"></a>

```c
#define ESP32_TOUCH_FILTER_MODE_IIR_16 2
```

相关声明：[ESP32_TOUCH_FILTER_MODE_IIR_16](#a2d049eb351a0d74411c267495a838c43)。

<a id="r_a734fd0678fa616ba49888e073ce2867e"></a>

```c
#define ESP32_TOUCH_FILTER_MODE_IIR_32 3
```

相关声明：[ESP32_TOUCH_FILTER_MODE_IIR_32](#a734fd0678fa616ba49888e073ce2867e)。

<a id="r_a79399dd378771854335172d42bec75ff"></a>

```c
#define ESP32_TOUCH_FILTER_MODE_IIR_64 4
```

相关声明：[ESP32_TOUCH_FILTER_MODE_IIR_64](#a79399dd378771854335172d42bec75ff)。

<a id="r_a34af295d6874b7a48bea0a33b775bf5b"></a>

```c
#define ESP32_TOUCH_FILTER_MODE_IIR_128 5
```

相关声明：[ESP32_TOUCH_FILTER_MODE_IIR_128](#a34af295d6874b7a48bea0a33b775bf5b)。

<a id="r_af80cda7abfcf1d87383b0857eb3d2b7d"></a>

```c
#define ESP32_TOUCH_FILTER_MODE_IIR_256 6
```

相关声明：[ESP32_TOUCH_FILTER_MODE_IIR_256](#af80cda7abfcf1d87383b0857eb3d2b7d)。

<a id="r_a0191397c82bd5b2e178b39192d197a5a"></a>

```c
#define ESP32_TOUCH_FILTER_MODE_JITTER 7
```

相关声明：[ESP32_TOUCH_FILTER_MODE_JITTER](#a0191397c82bd5b2e178b39192d197a5a)。

<a id="r_ab7600d5876774079f3ed910eccdecfef"></a>

```c
#define ESP32_TOUCH_FILTER_NOISE_THR_4_8TH 0
```

相关声明：[ESP32_TOUCH_FILTER_NOISE_THR_4_8TH](#ab7600d5876774079f3ed910eccdecfef)。

<a id="r_a69c5b8f22ee5c81d4994690f2d033dac"></a>

```c
#define ESP32_TOUCH_FILTER_NOISE_THR_3_8TH 1
```

相关声明：[ESP32_TOUCH_FILTER_NOISE_THR_3_8TH](#a69c5b8f22ee5c81d4994690f2d033dac)。

<a id="r_a9b9e8a6dc207ce34f2feecb833e272a4"></a>

```c
#define ESP32_TOUCH_FILTER_NOISE_THR_2_8TH 2
```

相关声明：[ESP32_TOUCH_FILTER_NOISE_THR_2_8TH](#a9b9e8a6dc207ce34f2feecb833e272a4)。

<a id="r_ac2d469b684700c9936ffb60da244d124"></a>

```c
#define ESP32_TOUCH_FILTER_NOISE_THR_8_8TH 3
```

相关声明：[ESP32_TOUCH_FILTER_NOISE_THR_8_8TH](#ac2d469b684700c9936ffb60da244d124)。

<a id="r_a800b1f8f2f1c7b6e0dc10b8421487b91"></a>

```c
#define ESP32_TOUCH_FILTER_SMOOTH_MODE_OFF 0
```

相关声明：[ESP32_TOUCH_FILTER_SMOOTH_MODE_OFF](#a800b1f8f2f1c7b6e0dc10b8421487b91)。

<a id="r_a708831f2ca6d7bbf92dda0903aa9eab7"></a>

```c
#define ESP32_TOUCH_FILTER_SMOOTH_MODE_IIR_2 1
```

相关声明：[ESP32_TOUCH_FILTER_SMOOTH_MODE_IIR_2](#a708831f2ca6d7bbf92dda0903aa9eab7)。

<a id="r_aadcde8afbbb880f9ae297cfe01d437bd"></a>

```c
#define ESP32_TOUCH_FILTER_SMOOTH_MODE_IIR_4 2
```

相关声明：[ESP32_TOUCH_FILTER_SMOOTH_MODE_IIR_4](#aadcde8afbbb880f9ae297cfe01d437bd)。

<a id="r_a11620309c1ce775346fa6eb9c6ac4c77"></a>

```c
#define ESP32_TOUCH_FILTER_SMOOTH_MODE_IIR_8 3
```

相关声明：[ESP32_TOUCH_FILTER_SMOOTH_MODE_IIR_8](#a11620309c1ce775346fa6eb9c6ac4c77)。

## 88.2\_详细说明（Detailed Documentation）

<a id="a34af295d6874b7a48bea0a33b775bf5b"></a>

### `ESP32_TOUCH_FILTER_MODE_IIR_128`

```c
#define ESP32_TOUCH_FILTER_MODE_IIR_128 5
```

<a id="a2d049eb351a0d74411c267495a838c43"></a>

### `ESP32_TOUCH_FILTER_MODE_IIR_16`

```c
#define ESP32_TOUCH_FILTER_MODE_IIR_16 2
```

<a id="af80cda7abfcf1d87383b0857eb3d2b7d"></a>

### `ESP32_TOUCH_FILTER_MODE_IIR_256`

```c
#define ESP32_TOUCH_FILTER_MODE_IIR_256 6
```

<a id="a734fd0678fa616ba49888e073ce2867e"></a>

### `ESP32_TOUCH_FILTER_MODE_IIR_32`

```c
#define ESP32_TOUCH_FILTER_MODE_IIR_32 3
```

<a id="ae2a0cd54094572c8656231a5838cb66a"></a>

### `ESP32_TOUCH_FILTER_MODE_IIR_4`

```c
#define ESP32_TOUCH_FILTER_MODE_IIR_4 0
```

<a id="a79399dd378771854335172d42bec75ff"></a>

### `ESP32_TOUCH_FILTER_MODE_IIR_64`

```c
#define ESP32_TOUCH_FILTER_MODE_IIR_64 4
```

<a id="aaa4e199eb00344994a8f1545122bec4f"></a>

### `ESP32_TOUCH_FILTER_MODE_IIR_8`

```c
#define ESP32_TOUCH_FILTER_MODE_IIR_8 1
```

<a id="a0191397c82bd5b2e178b39192d197a5a"></a>

### `ESP32_TOUCH_FILTER_MODE_JITTER`

```c
#define ESP32_TOUCH_FILTER_MODE_JITTER 7
```

<a id="a9b9e8a6dc207ce34f2feecb833e272a4"></a>

### `ESP32_TOUCH_FILTER_NOISE_THR_2_8TH`

```c
#define ESP32_TOUCH_FILTER_NOISE_THR_2_8TH 2
```

<a id="a69c5b8f22ee5c81d4994690f2d033dac"></a>

### `ESP32_TOUCH_FILTER_NOISE_THR_3_8TH`

```c
#define ESP32_TOUCH_FILTER_NOISE_THR_3_8TH 1
```

<a id="ab7600d5876774079f3ed910eccdecfef"></a>

### `ESP32_TOUCH_FILTER_NOISE_THR_4_8TH`

```c
#define ESP32_TOUCH_FILTER_NOISE_THR_4_8TH 0
```

<a id="ac2d469b684700c9936ffb60da244d124"></a>

### `ESP32_TOUCH_FILTER_NOISE_THR_8_8TH`

```c
#define ESP32_TOUCH_FILTER_NOISE_THR_8_8TH 3
```

<a id="a708831f2ca6d7bbf92dda0903aa9eab7"></a>

### `ESP32_TOUCH_FILTER_SMOOTH_MODE_IIR_2`

```c
#define ESP32_TOUCH_FILTER_SMOOTH_MODE_IIR_2 1
```

<a id="aadcde8afbbb880f9ae297cfe01d437bd"></a>

### `ESP32_TOUCH_FILTER_SMOOTH_MODE_IIR_4`

```c
#define ESP32_TOUCH_FILTER_SMOOTH_MODE_IIR_4 2
```

<a id="a11620309c1ce775346fa6eb9c6ac4c77"></a>

### `ESP32_TOUCH_FILTER_SMOOTH_MODE_IIR_8`

```c
#define ESP32_TOUCH_FILTER_SMOOTH_MODE_IIR_8 3
```

<a id="a800b1f8f2f1c7b6e0dc10b8421487b91"></a>

### `ESP32_TOUCH_FILTER_SMOOTH_MODE_OFF`

```c
#define ESP32_TOUCH_FILTER_SMOOTH_MODE_OFF 0
```


## 88.3\_原页交叉引用（Cross References）

- [zephyr/dt-bindings/dt-util.h](../dt_bus_binding_reference/P006_设备树绑定工具头文件源码.md)
- [查看此文件的源码。](../api_source_runtime_reference/P017_esp32-touch-sensor-input.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P087_zephyr__dt-bindings__pinctrl__esp32-pinctrl.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P089_zephyr__dt-bindings__pinctrl__esp32c2-gpio-sigmap.h_文件参考.md)
