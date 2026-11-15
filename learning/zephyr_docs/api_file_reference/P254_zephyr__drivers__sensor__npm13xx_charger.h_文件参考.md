---
id: learning.zephyr-docs.api-file-reference.page-254
title: zephyr__drivers__sensor__npm13xx_charger.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/npm13xx__charger_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第254章\_zephyr\_\_drivers\_\_sensor\_\_npm13xx\_charger.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/npm13xx__charger_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/drivers/sensor.h>
```

查看此文件的源码。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 254.1\_枚举（Enumerations）

<a id="r_a3b5c9edfeb25c77685d67babdc4c5299"></a>

```c
enum sensor_channel_npm13xx_charger { SENSOR_CHAN_NPM13XX_CHARGER_STATUS = SENSOR_CHAN_PRIV_START , SENSOR_CHAN_NPM13XX_CHARGER_ERROR , SENSOR_CHAN_NPM13XX_CHARGER_VBUS_STATUS }
```

相关声明：[sensor_channel_npm13xx_charger](#a3b5c9edfeb25c77685d67babdc4c5299)、[SENSOR_CHAN_NPM13XX_CHARGER_STATUS](#a3b5c9edfeb25c77685d67babdc4c5299abb7d0a263602d5a4e7fddf5b7fa44946)、[SENSOR_CHAN_NPM13XX_CHARGER_ERROR](#a3b5c9edfeb25c77685d67babdc4c5299a68daf03ea54b12dba3bd2cac5d5f142b)、[SENSOR_CHAN_NPM13XX_CHARGER_VBUS_STATUS](#a3b5c9edfeb25c77685d67babdc4c5299aa070958a66af182e1db9c49a6a41c8c2)。

<a id="r_add553da0fb80ee2cfb6a5b009a1d6058"></a>

```c
enum sensor_attribute_npm13xx_charger { SENSOR_ATTR_NPM13XX_CHARGER_VBUS_PRESENT = SENSOR_ATTR_PRIV_START , SENSOR_ATTR_NPM13XX_CHARGER_VBUS_CUR_LIMIT , SENSOR_ATTR_NPM13XX_CHARGER_VBUS_OVERVLT_PROT , SENSOR_ATTR_NPM13XX_CHARGER_VBUS_UNDERVLT , SENSOR_ATTR_NPM13XX_CHARGER_VBUS_SUSPENDED , SENSOR_ATTR_NPM13XX_CHARGER_VBUS_BUSOUT }
```

相关声明：[sensor_attribute_npm13xx_charger](#add553da0fb80ee2cfb6a5b009a1d6058)、[SENSOR_ATTR_NPM13XX_CHARGER_VBUS_PRESENT](#add553da0fb80ee2cfb6a5b009a1d6058ac65dd6d01c5995c1f0514daaded1c283)、[SENSOR_ATTR_NPM13XX_CHARGER_VBUS_CUR_LIMIT](#add553da0fb80ee2cfb6a5b009a1d6058a3faad43b78763a2520e9a87baf38265b)、[SENSOR_ATTR_NPM13XX_CHARGER_VBUS_OVERVLT_PROT](#add553da0fb80ee2cfb6a5b009a1d6058a5674d4ecc2377640a42fc78fef60c0ab)、[SENSOR_ATTR_NPM13XX_CHARGER_VBUS_UNDERVLT](#add553da0fb80ee2cfb6a5b009a1d6058addc2f6fbe32fd3bdadeb6c5d3aa00a08)、[SENSOR_ATTR_NPM13XX_CHARGER_VBUS_SUSPENDED](#add553da0fb80ee2cfb6a5b009a1d6058a7e1153a7eeb8e02925d0ee57c79b8a31)、[SENSOR_ATTR_NPM13XX_CHARGER_VBUS_BUSOUT](#add553da0fb80ee2cfb6a5b009a1d6058abb429313846ec7adbf09d84b5385e2bc)。

## 254.2\_详细说明（Detailed Documentation）

<a id="add553da0fb80ee2cfb6a5b009a1d6058"></a>

### `sensor_attribute_npm13xx_charger`

```c
enum sensor_attribute_npm13xx_charger
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_ATTR_NPM13XX_CHARGER_VBUS_PRESENT` |  |
| `SENSOR_ATTR_NPM13XX_CHARGER_VBUS_CUR_LIMIT` |  |
| `SENSOR_ATTR_NPM13XX_CHARGER_VBUS_OVERVLT_PROT` |  |
| `SENSOR_ATTR_NPM13XX_CHARGER_VBUS_UNDERVLT` |  |
| `SENSOR_ATTR_NPM13XX_CHARGER_VBUS_SUSPENDED` |  |
| `SENSOR_ATTR_NPM13XX_CHARGER_VBUS_BUSOUT` |  |

<a id="a3b5c9edfeb25c77685d67babdc4c5299"></a>

### `sensor_channel_npm13xx_charger`

```c
enum sensor_channel_npm13xx_charger
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_CHAN_NPM13XX_CHARGER_STATUS` |  |
| `SENSOR_CHAN_NPM13XX_CHARGER_ERROR` |  |
| `SENSOR_CHAN_NPM13XX_CHARGER_VBUS_STATUS` |  |


## 254.3\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h_source.html)
- [查看此文件的源码。](../api_source_configuration_reference/P060_npm13xx_charger.h_源码浏览.md)

<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="add553da0fb80ee2cfb6a5b009a1d6058ac65dd6d01c5995c1f0514daaded1c283"></a>
<a id="add553da0fb80ee2cfb6a5b009a1d6058a3faad43b78763a2520e9a87baf38265b"></a>
<a id="add553da0fb80ee2cfb6a5b009a1d6058a5674d4ecc2377640a42fc78fef60c0ab"></a>
<a id="add553da0fb80ee2cfb6a5b009a1d6058addc2f6fbe32fd3bdadeb6c5d3aa00a08"></a>
<a id="add553da0fb80ee2cfb6a5b009a1d6058a7e1153a7eeb8e02925d0ee57c79b8a31"></a>
<a id="add553da0fb80ee2cfb6a5b009a1d6058abb429313846ec7adbf09d84b5385e2bc"></a>
<a id="a3b5c9edfeb25c77685d67babdc4c5299abb7d0a263602d5a4e7fddf5b7fa44946"></a>
<a id="a3b5c9edfeb25c77685d67babdc4c5299a68daf03ea54b12dba3bd2cac5d5f142b"></a>
<a id="a3b5c9edfeb25c77685d67babdc4c5299aa070958a66af182e1db9c49a6a41c8c2"></a>

---

[上一章](P253_zephyr__dt-bindings__flash_controller__npcx_fiu_qspi.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P255_zephyr__drivers__sensor__npm2100_vbat.h_文件参考.md)
