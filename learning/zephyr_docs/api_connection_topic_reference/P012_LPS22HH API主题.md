---
id: learning.zephyr-docs.api-connection-topic-reference.page-12
title: LPS22HH API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__lps22hh__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_LPS22HH API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__lps22hh__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

STMicroelectronics LPS22HH 压力和温度传感器。

<a id="details"></a>

STMicroelectronics LPS22HH 压力和温度传感器。

<a id="header-files"></a>
<a id="files"></a>

## 12.1\_文件（Files）

<a id="r_lps22hh_2Eh"></a>

```c
file lps22hh.h
```

相关声明：[lps22hh.h](https://docs.zephyrproject.org/latest/doxygen/html/lps22hh_8h.html)。

the ST LPS22HH pressure sensor的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 12.2\_输出数据率选项（Output data rate options）

设备树 `odr` 属性的取值。

<a id="r_ga8c40f6451b73b5dab3af90c026589aa5"></a>

```c
#define LPS22HH_DT_ODR_POWER_DOWN 0
```

相关声明：[LPS22HH_DT_ODR_POWER_DOWN](#ga8c40f6451b73b5dab3af90c026589aa5)。

掉电（Power-down）。

<a id="r_ga0417e7a3bb172d181ec4d2d9285469e8"></a>

```c
#define LPS22HH_DT_ODR_1HZ 1
```

相关声明：[LPS22HH_DT_ODR_1HZ](#ga0417e7a3bb172d181ec4d2d9285469e8)。

频率：1 Hz。

<a id="r_ga1c332941d39229a715862e187181287b"></a>

```c
#define LPS22HH_DT_ODR_10HZ 2
```

相关声明：[LPS22HH_DT_ODR_10HZ](#ga1c332941d39229a715862e187181287b)。

频率：10 Hz。

<a id="r_gaa4ac2ccf60d30bd61225ff184c58f62f"></a>

```c
#define LPS22HH_DT_ODR_25HZ 3
```

相关声明：[LPS22HH_DT_ODR_25HZ](#gaa4ac2ccf60d30bd61225ff184c58f62f)。

频率：25 Hz。

<a id="r_ga523f313a2ec38dd59e48ad77e2361056"></a>

```c
#define LPS22HH_DT_ODR_50HZ 4
```

相关声明：[LPS22HH_DT_ODR_50HZ](#ga523f313a2ec38dd59e48ad77e2361056)。

频率：50 Hz。

<a id="r_ga11a0a1ab6cacd7c5dbd0c151242fba53"></a>

```c
#define LPS22HH_DT_ODR_75HZ 5
```

相关声明：[LPS22HH_DT_ODR_75HZ](#ga11a0a1ab6cacd7c5dbd0c151242fba53)。

频率：75 Hz。

<a id="r_ga6b2f19c118c9d519c6cc6219b041762c"></a>

```c
#define LPS22HH_DT_ODR_100HZ 6
```

相关声明：[LPS22HH_DT_ODR_100HZ](#ga6b2f19c118c9d519c6cc6219b041762c)。

频率：100 Hz。

<a id="r_ga53feaea4e3e20b1a95cad0007d1b3262"></a>

```c
#define LPS22HH_DT_ODR_200HZ 7
```

相关声明：[LPS22HH_DT_ODR_200HZ](#ga53feaea4e3e20b1a95cad0007d1b3262)。

频率：200 Hz。

## 12.3\_详细说明（Detailed Documentation）

<a id="ga6b2f19c118c9d519c6cc6219b041762c"></a>

### `LPS22HH_DT_ODR_100HZ`

```c
#define LPS22HH_DT_ODR_100HZ 6
```

```c
#include <zephyr/dt-bindings/sensor/lps22hh.h>
```

频率：100 Hz。

<a id="ga1c332941d39229a715862e187181287b"></a>

### `LPS22HH_DT_ODR_10HZ`

```c
#define LPS22HH_DT_ODR_10HZ 2
```

```c
#include <zephyr/dt-bindings/sensor/lps22hh.h>
```

频率：10 Hz。

<a id="ga0417e7a3bb172d181ec4d2d9285469e8"></a>

### `LPS22HH_DT_ODR_1HZ`

```c
#define LPS22HH_DT_ODR_1HZ 1
```

```c
#include <zephyr/dt-bindings/sensor/lps22hh.h>
```

频率：1 Hz。

<a id="ga53feaea4e3e20b1a95cad0007d1b3262"></a>

### `LPS22HH_DT_ODR_200HZ`

```c
#define LPS22HH_DT_ODR_200HZ 7
```

```c
#include <zephyr/dt-bindings/sensor/lps22hh.h>
```

频率：200 Hz。

<a id="gaa4ac2ccf60d30bd61225ff184c58f62f"></a>

### `LPS22HH_DT_ODR_25HZ`

```c
#define LPS22HH_DT_ODR_25HZ 3
```

```c
#include <zephyr/dt-bindings/sensor/lps22hh.h>
```

频率：25 Hz。

<a id="ga523f313a2ec38dd59e48ad77e2361056"></a>

### `LPS22HH_DT_ODR_50HZ`

```c
#define LPS22HH_DT_ODR_50HZ 4
```

```c
#include <zephyr/dt-bindings/sensor/lps22hh.h>
```

频率：50 Hz。

<a id="ga11a0a1ab6cacd7c5dbd0c151242fba53"></a>

### `LPS22HH_DT_ODR_75HZ`

```c
#define LPS22HH_DT_ODR_75HZ 5
```

```c
#include <zephyr/dt-bindings/sensor/lps22hh.h>
```

频率：75 Hz。

<a id="ga8c40f6451b73b5dab3af90c026589aa5"></a>

### `LPS22HH_DT_ODR_POWER_DOWN`

```c
#define LPS22HH_DT_ODR_POWER_DOWN 0
```

```c
#include <zephyr/dt-bindings/sensor/lps22hh.h>
```

掉电（Power-down）。


## 12.4\_原页交叉引用（Cross References）

- [lps22hh.h](https://docs.zephyrproject.org/latest/doxygen/html/lps22hh_8h.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P011_闪存映像 API（Flash image API）.md) · [返回大纲](大纲.md) · [下一章](P013_MDIO 驱动后端 API.md)
