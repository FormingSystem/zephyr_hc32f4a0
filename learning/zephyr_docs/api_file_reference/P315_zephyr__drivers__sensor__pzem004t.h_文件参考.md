---
id: learning.zephyr-docs.api-file-reference.page-315
title: zephyr__drivers__sensor__pzem004t.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pzem004t_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第315章\_zephyr\_\_drivers\_\_sensor\_\_pzem004t.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/pzem004t_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/drivers/sensor.h>
```

查看此文件的源码。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 315.1\_枚举（Enumerations）

<a id="r_ae89669c0c9353578730abddbf89317c8"></a>

```c
enum sensor_channel_pzem004t { SENSOR_CHAN_PZEM004T_ENERGY = SENSOR_CHAN_PRIV_START , SENSOR_CHAN_PZEM004T_POWER_FACTOR , SENSOR_CHAN_PZEM004T_ALARM_STATUS , SENSOR_CHAN_PZEM004T_POWER_ALARM_THRESHOLD , SENSOR_CHAN_PZEM004T_MODBUS_RTU_ADDRESS , SENSOR_CHAN_PZEM004T_ADDRESS_INST_SET , SENSOR_CHAN_PZEM004T_RESET_ENERGY }
```

相关声明：[sensor_channel_pzem004t](#ae89669c0c9353578730abddbf89317c8)、[SENSOR_CHAN_PZEM004T_ENERGY](#ae89669c0c9353578730abddbf89317c8a93ae8e1b50fd213580f3542f8af8d678)、[SENSOR_CHAN_PZEM004T_POWER_FACTOR](#ae89669c0c9353578730abddbf89317c8af4816399cbd0a3498dccd171a74895d2)、[SENSOR_CHAN_PZEM004T_ALARM_STATUS](#ae89669c0c9353578730abddbf89317c8ac71d41aebb26977781fd9dca39b43352)、[SENSOR_CHAN_PZEM004T_POWER_ALARM_THRESHOLD](#ae89669c0c9353578730abddbf89317c8a268e403bacb31a68888ad5a527a87f4b)、[SENSOR_CHAN_PZEM004T_MODBUS_RTU_ADDRESS](#ae89669c0c9353578730abddbf89317c8ab45e14abf577f9913f6d2c62b8c42efc)、[SENSOR_CHAN_PZEM004T_ADDRESS_INST_SET](#ae89669c0c9353578730abddbf89317c8a416600d86b5821fa0d0b7980327193ee)、[SENSOR_CHAN_PZEM004T_RESET_ENERGY](#ae89669c0c9353578730abddbf89317c8a2c4c10ab296093f4422261ec7df12902)。

<a id="r_a33c78de1fb354c14fc0438a06f494a79"></a>

```c
enum sensor_attribute_pzem004t { SENSOR_ATTR_PZEM004T_POWER_ALARM_THRESHOLD = SENSOR_ATTR_PRIV_START , SENSOR_ATTR_PZEM004T_MODBUS_RTU_ADDRESS , SENSOR_ATTR_PZEM004T_ADDRESS_INST_SET , SENSOR_ATTR_PZEM004T_RESET_ENERGY }
```

相关声明：[sensor_attribute_pzem004t](#a33c78de1fb354c14fc0438a06f494a79)、[SENSOR_ATTR_PZEM004T_POWER_ALARM_THRESHOLD](#a33c78de1fb354c14fc0438a06f494a79ae295849a8604ce5dbf1b69a5aa72108b)、[SENSOR_ATTR_PZEM004T_MODBUS_RTU_ADDRESS](#a33c78de1fb354c14fc0438a06f494a79ad785a07dc2bfcb54ca672d6f8a09c7e7)、[SENSOR_ATTR_PZEM004T_ADDRESS_INST_SET](#a33c78de1fb354c14fc0438a06f494a79a4653bc9656221e9359c820d618acd937)、[SENSOR_ATTR_PZEM004T_RESET_ENERGY](#a33c78de1fb354c14fc0438a06f494a79a674c0ad21c9adcc62f078f69b36fea01)。

## 315.2\_详细说明（Detailed Documentation）

<a id="a33c78de1fb354c14fc0438a06f494a79"></a>

### `sensor_attribute_pzem004t`

```c
enum sensor_attribute_pzem004t
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_ATTR_PZEM004T_POWER_ALARM_THRESHOLD` |  |
| `SENSOR_ATTR_PZEM004T_MODBUS_RTU_ADDRESS` |  |
| `SENSOR_ATTR_PZEM004T_ADDRESS_INST_SET` |  |
| `SENSOR_ATTR_PZEM004T_RESET_ENERGY` |  |

<a id="ae89669c0c9353578730abddbf89317c8"></a>

### `sensor_channel_pzem004t`

```c
enum sensor_channel_pzem004t
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_CHAN_PZEM004T_ENERGY` |  |
| `SENSOR_CHAN_PZEM004T_POWER_FACTOR` |  |
| `SENSOR_CHAN_PZEM004T_ALARM_STATUS` |  |
| `SENSOR_CHAN_PZEM004T_POWER_ALARM_THRESHOLD` |  |
| `SENSOR_CHAN_PZEM004T_MODBUS_RTU_ADDRESS` |  |
| `SENSOR_CHAN_PZEM004T_ADDRESS_INST_SET` |  |
| `SENSOR_CHAN_PZEM004T_RESET_ENERGY` |  |


## 315.3\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h_source.html)
- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/pzem004t_8h_source.html)

<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="a33c78de1fb354c14fc0438a06f494a79ae295849a8604ce5dbf1b69a5aa72108b"></a>
<a id="a33c78de1fb354c14fc0438a06f494a79ad785a07dc2bfcb54ca672d6f8a09c7e7"></a>
<a id="a33c78de1fb354c14fc0438a06f494a79a4653bc9656221e9359c820d618acd937"></a>
<a id="a33c78de1fb354c14fc0438a06f494a79a674c0ad21c9adcc62f078f69b36fea01"></a>
<a id="ae89669c0c9353578730abddbf89317c8a93ae8e1b50fd213580f3542f8af8d678"></a>
<a id="ae89669c0c9353578730abddbf89317c8af4816399cbd0a3498dccd171a74895d2"></a>
<a id="ae89669c0c9353578730abddbf89317c8ac71d41aebb26977781fd9dca39b43352"></a>
<a id="ae89669c0c9353578730abddbf89317c8a268e403bacb31a68888ad5a527a87f4b"></a>
<a id="ae89669c0c9353578730abddbf89317c8ab45e14abf577f9913f6d2c62b8c42efc"></a>
<a id="ae89669c0c9353578730abddbf89317c8a416600d86b5821fa0d0b7980327193ee"></a>
<a id="ae89669c0c9353578730abddbf89317c8a2c4c10ab296093f4422261ec7df12902"></a>

---

[上一章](P314_zephyr__drivers__pwm__pwm_mchp_pwm_g1.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P316_zephyr__drivers__sensor__qdec_nxp_tpm.h_文件参考.md)
