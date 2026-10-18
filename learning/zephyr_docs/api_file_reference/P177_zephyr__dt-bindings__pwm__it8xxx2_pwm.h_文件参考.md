---
id: learning.zephyr-docs.api-file-reference.page-177
title: zephyr__dt-bindings__pwm__it8xxx2_pwm.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/it8xxx2__pwm_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第177章\_zephyr\_\_dt-bindings\_\_pwm\_\_it8xxx2\_pwm.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/it8xxx2__pwm_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/dt-bindings/dt-util.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 177.1\_宏定义（Macros）

<a id="r_a98aaba2e733ce20cd59eeadc33663965"></a>

```c
#define PWM_PRESCALER_C4 1
```

相关声明：[PWM_PRESCALER_C4](#a98aaba2e733ce20cd59eeadc33663965)。

<a id="r_a15fa229af614107078c43d887c985520"></a>

```c
#define PWM_PRESCALER_C6 2
```

相关声明：[PWM_PRESCALER_C6](#a15fa229af614107078c43d887c985520)。

<a id="r_a784a4aa1339416ac435615ec74742ca9"></a>

```c
#define PWM_PRESCALER_C7 3
```

相关声明：[PWM_PRESCALER_C7](#a784a4aa1339416ac435615ec74742ca9)。

<a id="r_a9b43cbcd1d148602c21fa850bebefbdc"></a>

```c
#define PWM_CHANNEL_0 0
```

相关声明：[PWM_CHANNEL_0](#a9b43cbcd1d148602c21fa850bebefbdc)。

<a id="r_a1da821e350e2e57c46bb73d60256e537"></a>

```c
#define PWM_CHANNEL_1 1
```

相关声明：[PWM_CHANNEL_1](#a1da821e350e2e57c46bb73d60256e537)。

<a id="r_a90a3351d5ed724d6970eb50970e12df3"></a>

```c
#define PWM_CHANNEL_2 2
```

相关声明：[PWM_CHANNEL_2](#a90a3351d5ed724d6970eb50970e12df3)。

<a id="r_ad7ecaad6ade54bca69bac60bb39b3d23"></a>

```c
#define PWM_CHANNEL_3 3
```

相关声明：[PWM_CHANNEL_3](#ad7ecaad6ade54bca69bac60bb39b3d23)。

<a id="r_a7695e0811561c98657a24fb828b7dd80"></a>

```c
#define PWM_CHANNEL_4 4
```

相关声明：[PWM_CHANNEL_4](#a7695e0811561c98657a24fb828b7dd80)。

<a id="r_a45c3365cad7dbd63b7db5881a287ca78"></a>

```c
#define PWM_CHANNEL_5 5
```

相关声明：[PWM_CHANNEL_5](#a45c3365cad7dbd63b7db5881a287ca78)。

<a id="r_abbce1e1eeae1747443dcea1259f99384"></a>

```c
#define PWM_CHANNEL_6 6
```

相关声明：[PWM_CHANNEL_6](#abbce1e1eeae1747443dcea1259f99384)。

<a id="r_aefd382e2874b5ecac051e5f0129199b0"></a>

```c
#define PWM_CHANNEL_7 7
```

相关声明：[PWM_CHANNEL_7](#aefd382e2874b5ecac051e5f0129199b0)。

<a id="r_a32b90fa9162659b3eb7ac54091093887"></a>

```c
#define PWM_IT8XXX2_OPEN_DRAIN BIT(8)
```

相关声明：[PWM_IT8XXX2_OPEN_DRAIN](#a32b90fa9162659b3eb7ac54091093887)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

## 177.2\_详细说明（Detailed Documentation）

<a id="a9b43cbcd1d148602c21fa850bebefbdc"></a>

### `PWM_CHANNEL_0`

```c
#define PWM_CHANNEL_0 0
```

<a id="a1da821e350e2e57c46bb73d60256e537"></a>

### `PWM_CHANNEL_1`

```c
#define PWM_CHANNEL_1 1
```

<a id="a90a3351d5ed724d6970eb50970e12df3"></a>

### `PWM_CHANNEL_2`

```c
#define PWM_CHANNEL_2 2
```

<a id="ad7ecaad6ade54bca69bac60bb39b3d23"></a>

### `PWM_CHANNEL_3`

```c
#define PWM_CHANNEL_3 3
```

<a id="a7695e0811561c98657a24fb828b7dd80"></a>

### `PWM_CHANNEL_4`

```c
#define PWM_CHANNEL_4 4
```

<a id="a45c3365cad7dbd63b7db5881a287ca78"></a>

### `PWM_CHANNEL_5`

```c
#define PWM_CHANNEL_5 5
```

<a id="abbce1e1eeae1747443dcea1259f99384"></a>

### `PWM_CHANNEL_6`

```c
#define PWM_CHANNEL_6 6
```

<a id="aefd382e2874b5ecac051e5f0129199b0"></a>

### `PWM_CHANNEL_7`

```c
#define PWM_CHANNEL_7 7
```

<a id="a32b90fa9162659b3eb7ac54091093887"></a>

### `PWM_IT8XXX2_OPEN_DRAIN`

```c
#define PWM_IT8XXX2_OPEN_DRAIN BIT(8)
```

<a id="a98aaba2e733ce20cd59eeadc33663965"></a>

### `PWM_PRESCALER_C4`

```c
#define PWM_PRESCALER_C4 1
```

<a id="a15fa229af614107078c43d887c985520"></a>

### `PWM_PRESCALER_C6`

```c
#define PWM_PRESCALER_C6 2
```

<a id="a784a4aa1339416ac435615ec74742ca9"></a>

### `PWM_PRESCALER_C7`

```c
#define PWM_PRESCALER_C7 3
```


## 177.3\_原页交叉引用（Cross References）

- [zephyr/dt-bindings/dt-util.h](../dt_bus_binding_reference/P006_设备树绑定工具头文件源码.md)
- [查看此文件的源码。](../api_source_runtime_reference/P035_it8xxx2_pwm.h_源码浏览.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P176_zephyr__dt-bindings__i2c__it8xxx2-i2c.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P178_zephyr__kernel__stats.h_文件参考.md)
