---
id: learning.zephyr-docs.api-file-reference.page-255
title: zephyr__drivers__sensor__npm2100_vbat.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/npm2100__vbat_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第255章\_zephyr\_\_drivers\_\_sensor\_\_npm2100\_vbat.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/npm2100__vbat_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/drivers/sensor.h>
```

查看此文件的源码。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 255.1\_枚举（Enumerations）

<a id="r_ad07cbdadaca3c654f3a27a54f74b30e7"></a>

```c
enum sensor_channel_npm2100_vbat { SENSOR_CHAN_NPM2100_VBAT_STATUS = SENSOR_CHAN_PRIV_START , SENSOR_CHAN_NPM2100_VOLT_DROOP , SENSOR_CHAN_NPM2100_DPS_COUNT , SENSOR_CHAN_NPM2100_DPS_TIMER , SENSOR_CHAN_NPM2100_DPS_DURATION }
```

相关声明：[sensor_channel_npm2100_vbat](#ad07cbdadaca3c654f3a27a54f74b30e7)、[SENSOR_CHAN_NPM2100_VBAT_STATUS](#ad07cbdadaca3c654f3a27a54f74b30e7ab2556cfe11bce37125a1b2c734acc368)、[SENSOR_CHAN_NPM2100_VOLT_DROOP](#ad07cbdadaca3c654f3a27a54f74b30e7a5b291484fb7cf4978bd7607081ccbd4a)、[SENSOR_CHAN_NPM2100_DPS_COUNT](#ad07cbdadaca3c654f3a27a54f74b30e7afa85e0dbca574d95493578cac8bff834)、[SENSOR_CHAN_NPM2100_DPS_TIMER](#ad07cbdadaca3c654f3a27a54f74b30e7a95abddd9aabcf283728d0fbd32834623)、[SENSOR_CHAN_NPM2100_DPS_DURATION](#ad07cbdadaca3c654f3a27a54f74b30e7ae722a338b422b8310d0c999ef510cb49)。

<a id="r_a0c9921cfee8de69b35666e1ab276196e"></a>

```c
enum sensor_attr_npm2100_vbat { SENSOR_ATTR_NPM2100_ADC_DELAY = SENSOR_ATTR_PRIV_START }
```

相关声明：[sensor_attr_npm2100_vbat](#a0c9921cfee8de69b35666e1ab276196e)、[SENSOR_ATTR_NPM2100_ADC_DELAY](#a0c9921cfee8de69b35666e1ab276196ea6523499d40a42c85a2d316b74859ba1d)。

## 255.2\_详细说明（Detailed Documentation）

<a id="a0c9921cfee8de69b35666e1ab276196e"></a>

### `sensor_attr_npm2100_vbat`

```c
enum sensor_attr_npm2100_vbat
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_ATTR_NPM2100_ADC_DELAY` |  |

<a id="ad07cbdadaca3c654f3a27a54f74b30e7"></a>

### `sensor_channel_npm2100_vbat`

```c
enum sensor_channel_npm2100_vbat
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_CHAN_NPM2100_VBAT_STATUS` |  |
| `SENSOR_CHAN_NPM2100_VOLT_DROOP` |  |
| `SENSOR_CHAN_NPM2100_DPS_COUNT` |  |
| `SENSOR_CHAN_NPM2100_DPS_TIMER` |  |
| `SENSOR_CHAN_NPM2100_DPS_DURATION` |  |


## 255.3\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h_source.html)
- [查看此文件的源码。](../api_source_configuration_reference/P061_npm2100_vbat.h_源码浏览.md)

<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="a0c9921cfee8de69b35666e1ab276196ea6523499d40a42c85a2d316b74859ba1d"></a>
<a id="ad07cbdadaca3c654f3a27a54f74b30e7ab2556cfe11bce37125a1b2c734acc368"></a>
<a id="ad07cbdadaca3c654f3a27a54f74b30e7a5b291484fb7cf4978bd7607081ccbd4a"></a>
<a id="ad07cbdadaca3c654f3a27a54f74b30e7afa85e0dbca574d95493578cac8bff834"></a>
<a id="ad07cbdadaca3c654f3a27a54f74b30e7a95abddd9aabcf283728d0fbd32834623"></a>
<a id="ad07cbdadaca3c654f3a27a54f74b30e7ae722a338b422b8310d0c999ef510cb49"></a>

---

[上一章](P254_zephyr__drivers__sensor__npm13xx_charger.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P256_zephyr__dt-bindings__clock__nrf-auxpll.h_文件参考.md)
