---
id: learning.zephyr-docs.api-vector-pipeline-topic-reference.page-12
title: LIS2DE12 API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__lis2de12__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_LIS2DE12 API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2de12__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

STMicroelectronics LIS2DE12 三轴加速度计（3-axis accelerometer）。

<a id="details"></a>

STMicroelectronics LIS2DE12 三轴加速度计（3-axis accelerometer）。

<a id="header-files"></a>
<a id="files"></a>

## 12.1\_文件（Files）

<a id="r_lis2de12_2Eh"></a>

```c
file lis2de12.h
```

相关声明：[lis2de12.h](https://docs.zephyrproject.org/latest/doxygen/html/lis2de12_8h.html)。

the ST LIS2DE12 accelerometer的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 12.2\_加速度计满量程范围（Accelerometer full-scale range）

设备树 `accel-range` 属性的取值。

<a id="r_ga4d98a2437d4189112bf8de962a6427c5"></a>

```c
#define LIS2DE12_DT_FS_2G 0
```

相关声明：[LIS2DE12_DT_FS_2G](#ga4d98a2437d4189112bf8de962a6427c5)。

量程（range）：±2 g。

<a id="r_ga28ea756e9426fef814d34e8f8e416373"></a>

```c
#define LIS2DE12_DT_FS_4G 1
```

相关声明：[LIS2DE12_DT_FS_4G](#ga28ea756e9426fef814d34e8f8e416373)。

量程（range）：±4 g。

<a id="r_ga9e527343fd8f40e87698ab4f2095a09c"></a>

```c
#define LIS2DE12_DT_FS_8G 2
```

相关声明：[LIS2DE12_DT_FS_8G](#ga9e527343fd8f40e87698ab4f2095a09c)。

量程（range）：±8 g。

<a id="r_ga5a79ea2d22261f2cbff1a920165c3614"></a>

```c
#define LIS2DE12_DT_FS_16G 3
```

相关声明：[LIS2DE12_DT_FS_16G](#ga5a79ea2d22261f2cbff1a920165c3614)。

量程（range）：±16 g。

## 12.3\_加速度计输出数据率（Accelerometer output data rate）

设备树（Devicetree）属性 `accel-odr` 的取值。

<a id="r_ga6fbd76dfbed77dbb642f6174e41b4933"></a>

```c
#define LIS2DE12_DT_ODR_OFF 0x00
```

相关声明：[LIS2DE12_DT_ODR_OFF](#ga6fbd76dfbed77dbb642f6174e41b4933)。

掉电（Power-down）。

<a id="r_gaeb564c25b94d793c58cb0c54ce04acf5"></a>

```c
#define LIS2DE12_DT_ODR_AT_1Hz 0x01
```

相关声明：[LIS2DE12_DT_ODR_AT_1Hz](#gaeb564c25b94d793c58cb0c54ce04acf5)。

1 Hz，正常（Normal）模式。

<a id="r_gad0a75e097c965995ed8e46cf93585cf6"></a>

```c
#define LIS2DE12_DT_ODR_AT_10Hz 0x02
```

相关声明：[LIS2DE12_DT_ODR_AT_10Hz](#gad0a75e097c965995ed8e46cf93585cf6)。

10 Hz，正常（Normal）模式。

<a id="r_gab5e906715ed2c45f4794a9d069d56921"></a>

```c
#define LIS2DE12_DT_ODR_AT_25Hz 0x03
```

相关声明：[LIS2DE12_DT_ODR_AT_25Hz](#gab5e906715ed2c45f4794a9d069d56921)。

25 Hz，正常（Normal）模式。

<a id="r_gaa751bddcce56dba2fe8209bd919692ef"></a>

```c
#define LIS2DE12_DT_ODR_AT_50Hz 0x04
```

相关声明：[LIS2DE12_DT_ODR_AT_50Hz](#gaa751bddcce56dba2fe8209bd919692ef)。

50 Hz，正常（Normal）模式。

<a id="r_gab0d6486440d1a759bf86311237803814"></a>

```c
#define LIS2DE12_DT_ODR_AT_100Hz 0x05
```

相关声明：[LIS2DE12_DT_ODR_AT_100Hz](#gab0d6486440d1a759bf86311237803814)。

100 Hz，正常（Normal）模式。

<a id="r_gabb6ab746392ec390affcff0b63208fcd"></a>

```c
#define LIS2DE12_DT_ODR_AT_200Hz 0x06
```

相关声明：[LIS2DE12_DT_ODR_AT_200Hz](#gabb6ab746392ec390affcff0b63208fcd)。

200 Hz，正常（Normal）模式。

<a id="r_ga02142274ee4945c67385ff49b322ad66"></a>

```c
#define LIS2DE12_DT_ODR_AT_400Hz 0x07
```

相关声明：[LIS2DE12_DT_ODR_AT_400Hz](#ga02142274ee4945c67385ff49b322ad66)。

400 Hz，正常（Normal）模式。

<a id="r_gaa14ef617b90cb5f8453eab1837eeb5d7"></a>

```c
#define LIS2DE12_DT_ODR_AT_1kHz620 0x08
```

相关声明：[LIS2DE12_DT_ODR_AT_1kHz620](#gaa14ef617b90cb5f8453eab1837eeb5d7)。

1620 Hz，正常（Normal）模式。

<a id="r_ga817a85c45d4dfb94933715f2b1492ca2"></a>

```c
#define LIS2DE12_DT_ODR_AT_5kHz376 0x09
```

相关声明：[LIS2DE12_DT_ODR_AT_5kHz376](#ga817a85c45d4dfb94933715f2b1492ca2)。

5376 Hz，正常（Normal）模式。

## 12.4\_详细说明（Detailed Documentation）

<a id="ga5a79ea2d22261f2cbff1a920165c3614"></a>

### `LIS2DE12_DT_FS_16G`

```c
#define LIS2DE12_DT_FS_16G 3
```

```c
#include <zephyr/dt-bindings/sensor/lis2de12.h>
```

量程（range）：±16 g。

<a id="ga4d98a2437d4189112bf8de962a6427c5"></a>

### `LIS2DE12_DT_FS_2G`

```c
#define LIS2DE12_DT_FS_2G 0
```

```c
#include <zephyr/dt-bindings/sensor/lis2de12.h>
```

量程（range）：±2 g。

<a id="ga28ea756e9426fef814d34e8f8e416373"></a>

### `LIS2DE12_DT_FS_4G`

```c
#define LIS2DE12_DT_FS_4G 1
```

```c
#include <zephyr/dt-bindings/sensor/lis2de12.h>
```

量程（range）：±4 g。

<a id="ga9e527343fd8f40e87698ab4f2095a09c"></a>

### `LIS2DE12_DT_FS_8G`

```c
#define LIS2DE12_DT_FS_8G 2
```

```c
#include <zephyr/dt-bindings/sensor/lis2de12.h>
```

量程（range）：±8 g。

<a id="gab0d6486440d1a759bf86311237803814"></a>

### `LIS2DE12_DT_ODR_AT_100Hz`

```c
#define LIS2DE12_DT_ODR_AT_100Hz 0x05
```

```c
#include <zephyr/dt-bindings/sensor/lis2de12.h>
```

100 Hz，正常（Normal）模式。

<a id="gad0a75e097c965995ed8e46cf93585cf6"></a>

### `LIS2DE12_DT_ODR_AT_10Hz`

```c
#define LIS2DE12_DT_ODR_AT_10Hz 0x02
```

```c
#include <zephyr/dt-bindings/sensor/lis2de12.h>
```

10 Hz，正常（Normal）模式。

<a id="gaeb564c25b94d793c58cb0c54ce04acf5"></a>

### `LIS2DE12_DT_ODR_AT_1Hz`

```c
#define LIS2DE12_DT_ODR_AT_1Hz 0x01
```

```c
#include <zephyr/dt-bindings/sensor/lis2de12.h>
```

1 Hz，正常（Normal）模式。

<a id="gaa14ef617b90cb5f8453eab1837eeb5d7"></a>

### `LIS2DE12_DT_ODR_AT_1kHz620`

```c
#define LIS2DE12_DT_ODR_AT_1kHz620 0x08
```

```c
#include <zephyr/dt-bindings/sensor/lis2de12.h>
```

1620 Hz，正常（Normal）模式。

<a id="gabb6ab746392ec390affcff0b63208fcd"></a>

### `LIS2DE12_DT_ODR_AT_200Hz`

```c
#define LIS2DE12_DT_ODR_AT_200Hz 0x06
```

```c
#include <zephyr/dt-bindings/sensor/lis2de12.h>
```

200 Hz，正常（Normal）模式。

<a id="gab5e906715ed2c45f4794a9d069d56921"></a>

### `LIS2DE12_DT_ODR_AT_25Hz`

```c
#define LIS2DE12_DT_ODR_AT_25Hz 0x03
```

```c
#include <zephyr/dt-bindings/sensor/lis2de12.h>
```

25 Hz，正常（Normal）模式。

<a id="ga02142274ee4945c67385ff49b322ad66"></a>

### `LIS2DE12_DT_ODR_AT_400Hz`

```c
#define LIS2DE12_DT_ODR_AT_400Hz 0x07
```

```c
#include <zephyr/dt-bindings/sensor/lis2de12.h>
```

400 Hz，正常（Normal）模式。

<a id="gaa751bddcce56dba2fe8209bd919692ef"></a>

### `LIS2DE12_DT_ODR_AT_50Hz`

```c
#define LIS2DE12_DT_ODR_AT_50Hz 0x04
```

```c
#include <zephyr/dt-bindings/sensor/lis2de12.h>
```

50 Hz，正常（Normal）模式。

<a id="ga817a85c45d4dfb94933715f2b1492ca2"></a>

### `LIS2DE12_DT_ODR_AT_5kHz376`

```c
#define LIS2DE12_DT_ODR_AT_5kHz376 0x09
```

```c
#include <zephyr/dt-bindings/sensor/lis2de12.h>
```

5376 Hz，正常（Normal）模式。

<a id="ga6fbd76dfbed77dbb642f6174e41b4933"></a>

### `LIS2DE12_DT_ODR_OFF`

```c
#define LIS2DE12_DT_ODR_OFF 0x00
```

```c
#include <zephyr/dt-bindings/sensor/lis2de12.h>
```

掉电（Power-down）。


## 12.5\_原页交叉引用（Cross References）

- [lis2de12.h](https://docs.zephyrproject.org/latest/doxygen/html/lis2de12_8h.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P011_ISM6HG256X API主题.md) · [返回大纲](大纲.md) · [下一章](P013_LSM6DSV320X API主题.md)
