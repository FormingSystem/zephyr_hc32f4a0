---
id: learning.zephyr-docs.device-power-control-model-reference.page-106
title: fuel_gauge_prop_val_联合体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/unionfuel__gauge__prop__val.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第106章\_fuel\_gauge\_prop\_val\_联合体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/unionfuel__gauge__prop__val.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

属性字段（Property Field）到值/类型联合体的映射。

```c
#include <zephyr/drivers/fuel_gauge.h>
```

<a id="details"></a>

属性字段（Property Field）到值/类型联合体的映射。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 106.1\_数据成员（Data Fields）

<a id="r_ad96f07db337c038466dd17401c076d38"></a>

```c
int avg_current
```

相关声明：[avg_current](#ad96f07db337c038466dd17401c076d38)。

对应属性（Property）：`FUEL_GAUGE_AVG_CURRENT`。

<a id="r_a8d349a8fe357fd30ba4d458dd8260f5a"></a>

```c
int32_t avg_current_ua
```

相关声明：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[avg_current_ua](#a8d349a8fe357fd30ba4d458dd8260f5a)。

对应属性（Property）：`FUEL_GAUGE_AVG_CURRENT_UA`。

<a id="r_ac8e8e74c2b1f2e0c1f4e65eecf5a745a"></a>

```c
bool cutoff
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[cutoff](#ac8e8e74c2b1f2e0c1f4e65eecf5a745a)。

对应属性（Property）：`FUEL_GAUGE_CHARGE_CUTOFF`。

<a id="r_a9bed3247063f069bb92b2902cc5ff468"></a>

```c
int current
```

相关声明：[current](#a9bed3247063f069bb92b2902cc5ff468)。

对应属性（Property）：`FUEL_GAUGE_CURRENT`。

<a id="r_ac8a4263fede43ebcd28cff1c66e413b1"></a>

```c
int32_t current_ua
```

相关声明：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[current_ua](#ac8a4263fede43ebcd28cff1c66e413b1)。

对应属性（Property）：`FUEL_GAUGE_CURRENT_UA`。

<a id="r_ac27ae67a315a7204cea6e88962758587"></a>

```c
uint32_t cycle_count
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[cycle_count](#ac27ae67a315a7204cea6e88962758587)。

对应属性（Property）：`FUEL_GAUGE_CYCLE_COUNT`。

<a id="r_a9f4653e270e93280bd6bed6022c135b0"></a>

```c
uint32_t connect_state
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[connect_state](#a9f4653e270e93280bd6bed6022c135b0)。

对应属性（Property）：`FUEL_GAUGE_CONNECT_STATE`。

<a id="r_adeb93ed2120e808aac815dcbdf69067f"></a>

```c
uint32_t flags
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[flags](#adeb93ed2120e808aac815dcbdf69067f)。

对应属性（Property）：`FUEL_GAUGE_FLAGS`。

<a id="r_aa29f7163a1637b6aa8cd6a15dc99d55b"></a>

```c
uint32_t full_charge_capacity
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[full_charge_capacity](#aa29f7163a1637b6aa8cd6a15dc99d55b)。

对应属性（Property）：`FUEL_GAUGE_FULL_CHARGE_CAPACITY`。

<a id="r_af421dee221486f53d71d0fb8e6c4df1c"></a>

```c
uint32_t full_charge_capacity_uah
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[full_charge_capacity_uah](#af421dee221486f53d71d0fb8e6c4df1c)。

对应属性（Property）：`FUEL_GAUGE_FULL_CHARGE_CAPACITY_UAH`。

<a id="r_a4916bb50489c5f70335da2f11ed9477e"></a>

```c
bool present_state
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[present_state](#a4916bb50489c5f70335da2f11ed9477e)。

对应属性（Property）：`FUEL_GAUGE_PRESENT_STATE`。

<a id="r_adecf57aa90e2b5d483cfd889ec512400"></a>

```c
uint32_t remaining_capacity
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[remaining_capacity](#adecf57aa90e2b5d483cfd889ec512400)。

对应属性（Property）：`FUEL_GAUGE_REMAINING_CAPACITY`。

<a id="r_ab19f11342d10502937595b535db09c7a"></a>

```c
uint32_t remaining_capacity_uah
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[remaining_capacity_uah](#ab19f11342d10502937595b535db09c7a)。

对应属性（Property）：`FUEL_GAUGE_REMAINING_CAPACITY_UAH`。

<a id="r_ae716bdf1346dc7767d98526db6083008"></a>

```c
uint32_t runtime_to_empty
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[runtime_to_empty](#ae716bdf1346dc7767d98526db6083008)。

对应属性（Property）：`FUEL_GAUGE_RUNTIME_TO_EMPTY`。

<a id="r_af40db6b3dba16b20097d0767e51a07c5"></a>

```c
uint32_t runtime_to_empty_mins
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[runtime_to_empty_mins](#af40db6b3dba16b20097d0767e51a07c5)。

对应属性（Property）：`FUEL_GAUGE_RUNTIME_TO_EMPTY_MINS`。

<a id="r_a2c77e8de7fa40fadfa13dfd4c94df804"></a>

```c
uint32_t runtime_to_full
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[runtime_to_full](#a2c77e8de7fa40fadfa13dfd4c94df804)。

对应属性（Property）：`FUEL_GAUGE_RUNTIME_TO_FULL`。

<a id="r_a600a90fd8d847bd29ffd9d96822abdb8"></a>

```c
uint32_t runtime_to_full_mins
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[runtime_to_full_mins](#a600a90fd8d847bd29ffd9d96822abdb8)。

对应属性（Property）：`FUEL_GAUGE_RUNTIME_TO_FULL_MINS`。

<a id="r_a957025a2a9fb7709e2bf478f15fd31a0"></a>

```c
uint16_t sbs_mfr_access_word
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[sbs_mfr_access_word](#a957025a2a9fb7709e2bf478f15fd31a0)。

对应属性（Property）：`FUEL_GAUGE_SBS_MFR_ACCESS`。

<a id="r_a33297ff5bf70b510272eddf77ced411e"></a>

```c
uint8_t absolute_state_of_charge
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[absolute_state_of_charge](#a33297ff5bf70b510272eddf77ced411e)。

对应属性（Property）：`FUEL_GAUGE_ABSOLUTE_STATE_OF_CHARGE`。

<a id="r_ae1d5c18887cb8dab5ad070801992be1a"></a>

```c
uint8_t absolute_state_of_charge_pct
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[absolute_state_of_charge_pct](#ae1d5c18887cb8dab5ad070801992be1a)。

对应属性（Property）：`FUEL_GAUGE_ABSOLUTE_STATE_OF_CHARGE_PCT`。

<a id="r_a45b20c5118f7ee408d507b94e6cae1dc"></a>

```c
uint8_t relative_state_of_charge
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[relative_state_of_charge](#a45b20c5118f7ee408d507b94e6cae1dc)。

对应属性（Property）：`FUEL_GAUGE_RELATIVE_STATE_OF_CHARGE`。

<a id="r_a94893761a1f77a9c0e746c34e5bb6e61"></a>

```c
uint8_t relative_state_of_charge_pct
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[relative_state_of_charge_pct](#a94893761a1f77a9c0e746c34e5bb6e61)。

对应属性（Property）：`FUEL_GAUGE_RELATIVE_STATE_OF_CHARGE_PCT`。

<a id="r_a36528b111568bd1c90859e454610fd9f"></a>

```c
uint16_t temperature
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[temperature](#a36528b111568bd1c90859e454610fd9f)。

对应属性（Property）：`FUEL_GAUGE_TEMPERATURE`。

<a id="r_a7d943c31ad7dd53d16bfded98e70b332"></a>

```c
uint16_t temperature_dk
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[temperature_dk](#a7d943c31ad7dd53d16bfded98e70b332)。

对应属性（Property）：`FUEL_GAUGE_TEMPERATURE_DK`。

<a id="r_abec5cadefa09e088620a9598dec9c473"></a>

```c
int voltage
```

相关声明：[voltage](#abec5cadefa09e088620a9598dec9c473)。

对应属性（Property）：`FUEL_GAUGE_VOLTAGE`。

<a id="r_aa52341a118d1445ee762ba1563406441"></a>

```c
int32_t voltage_uv
```

相关声明：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[voltage_uv](#aa52341a118d1445ee762ba1563406441)。

对应属性（Property）：`FUEL_GAUGE_VOLTAGE_UV`。

<a id="r_a7fc0551e303de56e0eb6bdac1ecaccd0"></a>

```c
uint16_t sbs_mode
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[sbs_mode](#a7fc0551e303de56e0eb6bdac1ecaccd0)。

对应属性（Property）：`FUEL_GAUGE_SBS_MODE`。

<a id="r_a6f74626deef4debbd8dfe6c188984d1b"></a>

```c
uint32_t chg_current
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[chg_current](#a6f74626deef4debbd8dfe6c188984d1b)。

对应属性（Property）：`FUEL_GAUGE_CHARGE_CURRENT`。

<a id="r_a740700d2c6c6db83617d8dfd964e34f7"></a>

```c
uint32_t chg_current_ua
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[chg_current_ua](#a740700d2c6c6db83617d8dfd964e34f7)。

对应属性（Property）：`FUEL_GAUGE_CHARGE_CURRENT_UA`。

<a id="r_a8743f7e7a05919b5469e39527b697e62"></a>

```c
uint32_t chg_voltage
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[chg_voltage](#a8743f7e7a05919b5469e39527b697e62)。

对应属性（Property）：`FUEL_GAUGE_CHARGE_VOLTAGE`。

<a id="r_ae40e0074599fa69ea5b9e9012c14452b"></a>

```c
uint32_t chg_voltage_uv
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[chg_voltage_uv](#ae40e0074599fa69ea5b9e9012c14452b)。

对应属性（Property）：`FUEL_GAUGE_CHARGE_VOLTAGE_UV`。

<a id="r_a65607bb9ba43022c9c566646d4763aac"></a>

```c
uint16_t fg_status
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[fg_status](#a65607bb9ba43022c9c566646d4763aac)。

对应属性（Property）：`FUEL_GAUGE_STATUS`。

<a id="r_a20aa5736b0ac3c5adda10152660de275"></a>

```c
uint16_t design_cap
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[design_cap](#a20aa5736b0ac3c5adda10152660de275)。

对应属性（Property）：`FUEL_GAUGE_DESIGN_CAPACITY`。

<a id="r_a11626713aef0445ad613a5976401d09e"></a>

```c
uint16_t design_volt
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[design_volt](#a11626713aef0445ad613a5976401d09e)。

对应属性（Property）：`FUEL_GAUGE_DESIGN_VOLTAGE`。

<a id="r_a06edf4e066a3b655cdfd4ab732e93b7a"></a>

```c
uint16_t design_volt_mv
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[design_volt_mv](#a06edf4e066a3b655cdfd4ab732e93b7a)。

对应属性（Property）：`FUEL_GAUGE_DESIGN_VOLTAGE_MV`。

<a id="r_aa5529fea5cfe765be9b66f5fad96ab2f"></a>

```c
int16_t sbs_at_rate
```

相关声明：[int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)、[sbs_at_rate](#aa5529fea5cfe765be9b66f5fad96ab2f)。

对应属性（Property）：`FUEL_GAUGE_SBS_ATRATE`。

<a id="r_aeeeddb48f22b54f90c603d58e9ffa9a5"></a>

```c
uint16_t sbs_at_rate_time_to_full
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[sbs_at_rate_time_to_full](#aeeeddb48f22b54f90c603d58e9ffa9a5)。

对应属性（Property）：`FUEL_GAUGE_SBS_ATRATE_TIME_TO_FULL`。

<a id="r_a8bc68c65571afb6856e7e1e6cb33a5e4"></a>

```c
uint16_t sbs_at_rate_time_to_full_mins
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[sbs_at_rate_time_to_full_mins](#a8bc68c65571afb6856e7e1e6cb33a5e4)。

对应属性（Property）：`FUEL_GAUGE_SBS_ATRATE_TIME_TO_FULL_MINS`。

<a id="r_a7c8b6f9ee98e5b97ddc85b7e72cea4a8"></a>

```c
uint16_t sbs_at_rate_time_to_empty
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[sbs_at_rate_time_to_empty](#a7c8b6f9ee98e5b97ddc85b7e72cea4a8)。

对应属性（Property）：`FUEL_GAUGE_SBS_ATRATE_TIME_TO_EMPTY`。

<a id="r_adbfa0be8653107875e91edd5db40265d"></a>

```c
uint16_t sbs_at_rate_time_to_empty_mins
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[sbs_at_rate_time_to_empty_mins](#adbfa0be8653107875e91edd5db40265d)。

对应属性（Property）：`FUEL_GAUGE_SBS_ATRATE_TIME_TO_EMPTY_MINS`。

<a id="r_a9b5015878c9a77d9c8330139f94843b7"></a>

```c
bool sbs_at_rate_ok
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[sbs_at_rate_ok](#a9b5015878c9a77d9c8330139f94843b7)。

对应属性（Property）：`FUEL_GAUGE_SBS_ATRATE_OK`。

<a id="r_a818ab7faf8f51d4d1a5c5f070d54b997"></a>

```c
uint16_t sbs_remaining_capacity_alarm
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[sbs_remaining_capacity_alarm](#a818ab7faf8f51d4d1a5c5f070d54b997)。

对应属性（Property）：`FUEL_GAUGE_SBS_REMAINING_CAPACITY_ALARM`。

<a id="r_aa0e46c727bb31acb5d41ce4bc6d5b106"></a>

```c
uint16_t sbs_remaining_time_alarm
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[sbs_remaining_time_alarm](#aa0e46c727bb31acb5d41ce4bc6d5b106)。

对应属性（Property）：`FUEL_GAUGE_SBS_REMAINING_TIME_ALARM`。

<a id="r_a0b6878d02d4d5a3865e8ca8d57951914"></a>

```c
uint16_t sbs_remaining_time_alarm_mins
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[sbs_remaining_time_alarm_mins](#a0b6878d02d4d5a3865e8ca8d57951914)。

对应属性（Property）：`FUEL_GAUGE_SBS_REMAINING_TIME_ALARM_MINS`。

<a id="r_a52b70375d15ed878d62d1390c3144cd8"></a>

```c
uint16_t current_direction
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[current_direction](#a52b70375d15ed878d62d1390c3144cd8)。

对应属性（Property）：`FUEL_GAUGE_CURRENT_DIRECTION`。

<a id="r_aa901ef363509234577d73958984862a4"></a>

```c
uint8_t state_of_charge_alarm
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[state_of_charge_alarm](#aa901ef363509234577d73958984862a4)。

对应属性（Property）：`FUEL_GAUGE_STATE_OF_CHARGE_ALARM`。

<a id="r_ab43ccbb0a1443e64d26e498d31d1a240"></a>

```c
uint8_t state_of_charge_alarm_pct
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[state_of_charge_alarm_pct](#ab43ccbb0a1443e64d26e498d31d1a240)。

对应属性（Property）：`FUEL_GAUGE_STATE_OF_CHARGE_ALARM_PCT`。

<a id="r_aff81db28e93cb70ebea6793e4493915f"></a>

```c
uint32_t low_voltage_alarm
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[low_voltage_alarm](#aff81db28e93cb70ebea6793e4493915f)。

对应属性（Property）：`FUEL_GAUGE_LOW_VOLTAGE_ALARM`。

<a id="r_aee04c49d39652837420039fb968ecea5"></a>

```c
uint32_t low_voltage_alarm_uv
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[low_voltage_alarm_uv](#aee04c49d39652837420039fb968ecea5)。

对应属性（Property）：`FUEL_GAUGE_LOW_VOLTAGE_ALARM_UV`。

<a id="r_a2b044d7e33e98fd0c0cead2a3de61431"></a>

```c
uint32_t high_voltage_alarm
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[high_voltage_alarm](#a2b044d7e33e98fd0c0cead2a3de61431)。

对应属性（Property）：`FUEL_GAUGE_HIGH_VOLTAGE_ALARM`。

<a id="r_acf5b8f9b1ff3b3c5b5547d4920dbd7f2"></a>

```c
uint32_t high_voltage_alarm_uv
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[high_voltage_alarm_uv](#acf5b8f9b1ff3b3c5b5547d4920dbd7f2)。

对应属性（Property）：`FUEL_GAUGE_HIGH_VOLTAGE_ALARM_UV`。

<a id="r_aaa55eae9e98203e5f1847d6162d1d28e"></a>

```c
int32_t low_current_alarm
```

相关声明：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[low_current_alarm](#aaa55eae9e98203e5f1847d6162d1d28e)。

对应属性（Property）：`FUEL_GAUGE_LOW_CURRENT_ALARM`。

<a id="r_a49e894ef1b0f7be9c5a1dba12a8cff41"></a>

```c
int32_t low_current_alarm_ua
```

相关声明：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[low_current_alarm_ua](#a49e894ef1b0f7be9c5a1dba12a8cff41)。

对应属性（Property）：`FUEL_GAUGE_LOW_CURRENT_ALARM_UA`。

<a id="r_ab4aafbc07557b2c15396b8bfc66d7e9b"></a>

```c
int32_t high_current_alarm
```

相关声明：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[high_current_alarm](#ab4aafbc07557b2c15396b8bfc66d7e9b)。

对应属性（Property）：`FUEL_GAUGE_HIGH_CURRENT_ALARM`。

<a id="r_adab6e7b86aea46fdb9f5bc99ae87e431"></a>

```c
int32_t high_current_alarm_ua
```

相关声明：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[high_current_alarm_ua](#adab6e7b86aea46fdb9f5bc99ae87e431)。

对应属性（Property）：`FUEL_GAUGE_HIGH_CURRENT_ALARM_UA`。

<a id="r_ad8d424fbbe3124cde5e82b74957a4885"></a>

```c
uint16_t low_temperature_alarm
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[low_temperature_alarm](#ad8d424fbbe3124cde5e82b74957a4885)。

对应属性（Property）：`FUEL_GAUGE_LOW_TEMPERATURE_ALARM`。

<a id="r_a163ecf351a2a538cac53757ad402dde0"></a>

```c
uint16_t low_temperature_alarm_dk
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[low_temperature_alarm_dk](#a163ecf351a2a538cac53757ad402dde0)。

对应属性（Property）：`FUEL_GAUGE_LOW_TEMPERATURE_ALARM_DK`。

<a id="r_a9dd892b613881fda89635046b3ef7942"></a>

```c
uint16_t high_temperature_alarm
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[high_temperature_alarm](#a9dd892b613881fda89635046b3ef7942)。

对应属性（Property）：`FUEL_GAUGE_HIGH_TEMPERATURE_ALARM`。

<a id="r_ac651ea27014b7e61fdf5e847d70a188c"></a>

```c
uint16_t high_temperature_alarm_dk
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[high_temperature_alarm_dk](#ac651ea27014b7e61fdf5e847d70a188c)。

对应属性（Property）：`FUEL_GAUGE_HIGH_TEMPERATURE_ALARM_DK`。

<a id="r_ad600545303f0fa6e2853396e83d87fdd"></a>

```c
int32_t gpio_voltage
```

相关声明：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[gpio_voltage](#ad600545303f0fa6e2853396e83d87fdd)。

对应属性（Property）：`FUEL_GAUGE_GPIO_VOLTAGE`。

<a id="r_ab969822a9d1bc32345d02805c6f9b204"></a>

```c
int32_t gpio_voltage_uv
```

相关声明：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[gpio_voltage_uv](#ab969822a9d1bc32345d02805c6f9b204)。

对应属性（Property）：`FUEL_GAUGE_GPIO_VOLTAGE_UV`。

<a id="r_aef3ced90ca261ec7501778a41f12963d"></a>

```c
int32_t low_gpio_alarm
```

相关声明：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[low_gpio_alarm](#aef3ced90ca261ec7501778a41f12963d)。

对应属性（Property）：`FUEL_GAUGE_LOW_GPIO_ALARM`。

<a id="r_a4ce4046d3284afa7fd2e37d510cf4fd2"></a>

```c
int32_t low_gpio_alarm_uv
```

相关声明：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[low_gpio_alarm_uv](#a4ce4046d3284afa7fd2e37d510cf4fd2)。

对应属性（Property）：`FUEL_GAUGE_LOW_GPIO_ALARM_UV`。

<a id="r_a0bf74ed2b92b7b0920cf90ef7119aa36"></a>

```c
int32_t high_gpio_alarm
```

相关声明：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[high_gpio_alarm](#a0bf74ed2b92b7b0920cf90ef7119aa36)。

对应属性（Property）：`FUEL_GAUGE_HIGH_GPIO_ALARM`。

<a id="r_ab553a7b8b86225bd6c13c7f0c0a5e658"></a>

```c
int32_t high_gpio_alarm_uv
```

相关声明：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[high_gpio_alarm_uv](#ab553a7b8b86225bd6c13c7f0c0a5e658)。

对应属性（Property）：`FUEL_GAUGE_HIGH_GPIO_ALARM_UV`。

<a id="r_a3b2dc6e92a6b4158115e76c78061fe16"></a>

```c
uint8_t adc_mode
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[adc_mode](#a3b2dc6e92a6b4158115e76c78061fe16)。

对应属性（Property）：`FUEL_GAUGE_ADC_MODE`。

<a id="r_aaee1a60dac0770780bd45c1549fbf819"></a>

```c
uint8_t cc_config
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cc_config](#aaee1a60dac0770780bd45c1549fbf819)。

对应属性（Property）：`FUEL_GAUGE_CC_CONFIG`。

<a id="r_a1638b4b54bf57af650832e53f9ce90a4"></a>

```c
uint8_t state_of_health
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[state_of_health](#a1638b4b54bf57af650832e53f9ce90a4)。

对应属性（Property）：`FUEL_GAUGE_STATE_OF_HEALTH`。

<a id="r_a9e12460af8ae1a0ba0d1838e977e7a59"></a>

```c
uint32_t therm_voltage_uv
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[therm_voltage_uv](#a9e12460af8ae1a0ba0d1838e977e7a59)。

对应属性（Property）：`FUEL_GAUGE_THERM_VOLTAGE_UV`。

<a id="r_a63ce57eb11373a7e899d6324f4335749"></a>

```c
fuel_gauge_custom_value_int_t custom_int
```

相关声明：[fuel_gauge_custom_value_int_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#gaf8c7f6c4f49dd420df6841c43c41d615)、[custom_int](#a63ce57eb11373a7e899d6324f4335749)。

供下游自定义属性使用的通用整数值。

<a id="r_a21fb17e3d083c0a26f592f38b07b797e"></a>

```c
fuel_gauge_custom_value_uint_t custom_uint
```

相关声明：[fuel_gauge_custom_value_uint_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ga08e4dae43d5169da58af32ec419ef9e8)、[custom_uint](#a21fb17e3d083c0a26f592f38b07b797e)。

供下游自定义属性使用的通用无符号值。

<a id="r_aec778f250686b960c7328c27b48d5a17"></a>

```c
fuel_gauge_custom_value_bool_t custom_bool
```

相关声明：[fuel_gauge_custom_value_bool_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ga44fd24de7d165388a87e6dd74f6547af)、[custom_bool](#aec778f250686b960c7328c27b48d5a17)。

供下游自定义属性使用的通用布尔值。

## 106.2\_详细说明（Detailed Documentation）

<a id="a33297ff5bf70b510272eddf77ced411e"></a>

### `absolute_state_of_charge`

```c
uint8_t fuel_gauge_prop_val::absolute_state_of_charge
```

对应属性（Property）：`FUEL_GAUGE_ABSOLUTE_STATE_OF_CHARGE`。

**已弃用（Deprecated）**：已弃用（Deprecated）：请改用 `fuel_gauge_prop_val::absolute_state_of_charge_pct`。

<a id="ae1d5c18887cb8dab5ad070801992be1a"></a>

### `absolute_state_of_charge_pct`

```c
uint8_t fuel_gauge_prop_val::absolute_state_of_charge_pct
```

对应属性（Property）：`FUEL_GAUGE_ABSOLUTE_STATE_OF_CHARGE_PCT`。

<a id="a3b2dc6e92a6b4158115e76c78061fe16"></a>

### `adc_mode`

```c
uint8_t fuel_gauge_prop_val::adc_mode
```

对应属性（Property）：`FUEL_GAUGE_ADC_MODE`。

<a id="ad96f07db337c038466dd17401c076d38"></a>

### `avg_current`

```c
int fuel_gauge_prop_val::avg_current
```

对应属性（Property）：`FUEL_GAUGE_AVG_CURRENT`。

**已弃用（Deprecated）**：已弃用（Deprecated）：请改用 `fuel_gauge_prop_val::avg_current_ua`。

<a id="a8d349a8fe357fd30ba4d458dd8260f5a"></a>

### `avg_current_ua`

```c
int32_t fuel_gauge_prop_val::avg_current_ua
```

对应属性（Property）：`FUEL_GAUGE_AVG_CURRENT_UA`。

<a id="aaee1a60dac0770780bd45c1549fbf819"></a>

### `cc_config`

```c
uint8_t fuel_gauge_prop_val::cc_config
```

对应属性（Property）：`FUEL_GAUGE_CC_CONFIG`。

<a id="a6f74626deef4debbd8dfe6c188984d1b"></a>

### `chg_current`

```c
uint32_t fuel_gauge_prop_val::chg_current
```

对应属性（Property）：`FUEL_GAUGE_CHARGE_CURRENT`。

**已弃用（Deprecated）**：已弃用（Deprecated）：请改用 `fuel_gauge_prop_val::chg_current_ua`。

<a id="a740700d2c6c6db83617d8dfd964e34f7"></a>

### `chg_current_ua`

```c
uint32_t fuel_gauge_prop_val::chg_current_ua
```

对应属性（Property）：`FUEL_GAUGE_CHARGE_CURRENT_UA`。

<a id="a8743f7e7a05919b5469e39527b697e62"></a>

### `chg_voltage`

```c
uint32_t fuel_gauge_prop_val::chg_voltage
```

对应属性（Property）：`FUEL_GAUGE_CHARGE_VOLTAGE`。

**已弃用（Deprecated）**：已弃用（Deprecated）：请改用 `fuel_gauge_prop_val::chg_voltage_uv`。

<a id="ae40e0074599fa69ea5b9e9012c14452b"></a>

### `chg_voltage_uv`

```c
uint32_t fuel_gauge_prop_val::chg_voltage_uv
```

对应属性（Property）：`FUEL_GAUGE_CHARGE_VOLTAGE_UV`。

<a id="a9f4653e270e93280bd6bed6022c135b0"></a>

### `connect_state`

```c
uint32_t fuel_gauge_prop_val::connect_state
```

对应属性（Property）：`FUEL_GAUGE_CONNECT_STATE`。

<a id="a9bed3247063f069bb92b2902cc5ff468"></a>

### `current`

```c
int fuel_gauge_prop_val::current
```

对应属性（Property）：`FUEL_GAUGE_CURRENT`。

**已弃用（Deprecated）**：已弃用（Deprecated）：请改用 `fuel_gauge_prop_val::current_ua`。

<a id="a52b70375d15ed878d62d1390c3144cd8"></a>

### `current_direction`

```c
uint16_t fuel_gauge_prop_val::current_direction
```

对应属性（Property）：`FUEL_GAUGE_CURRENT_DIRECTION`。

<a id="ac8a4263fede43ebcd28cff1c66e413b1"></a>

### `current_ua`

```c
int32_t fuel_gauge_prop_val::current_ua
```

对应属性（Property）：`FUEL_GAUGE_CURRENT_UA`。

<a id="aec778f250686b960c7328c27b48d5a17"></a>

### `custom_bool`

```c
fuel_gauge_custom_value_bool_t fuel_gauge_prop_val::custom_bool
```

供下游自定义属性使用的通用布尔值。

<a id="a63ce57eb11373a7e899d6324f4335749"></a>

### `custom_int`

```c
fuel_gauge_custom_value_int_t fuel_gauge_prop_val::custom_int
```

供下游自定义属性使用的通用整数值。

<a id="a21fb17e3d083c0a26f592f38b07b797e"></a>

### `custom_uint`

```c
fuel_gauge_custom_value_uint_t fuel_gauge_prop_val::custom_uint
```

供下游自定义属性使用的通用无符号值。

<a id="ac8e8e74c2b1f2e0c1f4e65eecf5a745a"></a>

### `cutoff`

```c
bool fuel_gauge_prop_val::cutoff
```

对应属性（Property）：`FUEL_GAUGE_CHARGE_CUTOFF`。

<a id="ac27ae67a315a7204cea6e88962758587"></a>

### `cycle_count`

```c
uint32_t fuel_gauge_prop_val::cycle_count
```

对应属性（Property）：`FUEL_GAUGE_CYCLE_COUNT`。

<a id="a20aa5736b0ac3c5adda10152660de275"></a>

### `design_cap`

```c
uint16_t fuel_gauge_prop_val::design_cap
```

对应属性（Property）：`FUEL_GAUGE_DESIGN_CAPACITY`。

<a id="a11626713aef0445ad613a5976401d09e"></a>

### `design_volt`

```c
uint16_t fuel_gauge_prop_val::design_volt
```

对应属性（Property）：`FUEL_GAUGE_DESIGN_VOLTAGE`。

**已弃用（Deprecated）**：已弃用（Deprecated）：请改用 `fuel_gauge_prop_val::design_volt_mv`。

<a id="a06edf4e066a3b655cdfd4ab732e93b7a"></a>

### `design_volt_mv`

```c
uint16_t fuel_gauge_prop_val::design_volt_mv
```

对应属性（Property）：`FUEL_GAUGE_DESIGN_VOLTAGE_MV`。

<a id="a65607bb9ba43022c9c566646d4763aac"></a>

### `fg_status`

```c
uint16_t fuel_gauge_prop_val::fg_status
```

对应属性（Property）：`FUEL_GAUGE_STATUS`。

<a id="adeb93ed2120e808aac815dcbdf69067f"></a>

### `flags`

```c
uint32_t fuel_gauge_prop_val::flags
```

对应属性（Property）：`FUEL_GAUGE_FLAGS`。

<a id="aa29f7163a1637b6aa8cd6a15dc99d55b"></a>

### `full_charge_capacity`

```c
uint32_t fuel_gauge_prop_val::full_charge_capacity
```

对应属性（Property）：`FUEL_GAUGE_FULL_CHARGE_CAPACITY`。

**已弃用（Deprecated）**：已弃用（Deprecated）：请改用 `fuel_gauge_prop_val::full_charge_capacity_uah`。

<a id="af421dee221486f53d71d0fb8e6c4df1c"></a>

### `full_charge_capacity_uah`

```c
uint32_t fuel_gauge_prop_val::full_charge_capacity_uah
```

对应属性（Property）：`FUEL_GAUGE_FULL_CHARGE_CAPACITY_UAH`。

<a id="ad600545303f0fa6e2853396e83d87fdd"></a>

### `gpio_voltage`

```c
int32_t fuel_gauge_prop_val::gpio_voltage
```

对应属性（Property）：`FUEL_GAUGE_GPIO_VOLTAGE`。

**已弃用（Deprecated）**：已弃用（Deprecated）：请改用 `fuel_gauge_prop_val::gpio_voltage_uv`。

<a id="ab969822a9d1bc32345d02805c6f9b204"></a>

### `gpio_voltage_uv`

```c
int32_t fuel_gauge_prop_val::gpio_voltage_uv
```

对应属性（Property）：`FUEL_GAUGE_GPIO_VOLTAGE_UV`。

<a id="ab4aafbc07557b2c15396b8bfc66d7e9b"></a>

### `high_current_alarm`

```c
int32_t fuel_gauge_prop_val::high_current_alarm
```

对应属性（Property）：`FUEL_GAUGE_HIGH_CURRENT_ALARM`。

**已弃用（Deprecated）**：已弃用（Deprecated）：请改用 `fuel_gauge_prop_val::high_current_alarm_ua`。

<a id="adab6e7b86aea46fdb9f5bc99ae87e431"></a>

### `high_current_alarm_ua`

```c
int32_t fuel_gauge_prop_val::high_current_alarm_ua
```

对应属性（Property）：`FUEL_GAUGE_HIGH_CURRENT_ALARM_UA`。

<a id="a0bf74ed2b92b7b0920cf90ef7119aa36"></a>

### `high_gpio_alarm`

```c
int32_t fuel_gauge_prop_val::high_gpio_alarm
```

对应属性（Property）：`FUEL_GAUGE_HIGH_GPIO_ALARM`。

**已弃用（Deprecated）**：已弃用（Deprecated）：请改用 `fuel_gauge_prop_val::high_gpio_alarm_uv`。

<a id="ab553a7b8b86225bd6c13c7f0c0a5e658"></a>

### `high_gpio_alarm_uv`

```c
int32_t fuel_gauge_prop_val::high_gpio_alarm_uv
```

对应属性（Property）：`FUEL_GAUGE_HIGH_GPIO_ALARM_UV`。

<a id="a9dd892b613881fda89635046b3ef7942"></a>

### `high_temperature_alarm`

```c
uint16_t fuel_gauge_prop_val::high_temperature_alarm
```

对应属性（Property）：`FUEL_GAUGE_HIGH_TEMPERATURE_ALARM`。

**已弃用（Deprecated）**：已弃用（Deprecated）：请改用 `fuel_gauge_prop_val::high_temperature_alarm_dk`。

<a id="ac651ea27014b7e61fdf5e847d70a188c"></a>

### `high_temperature_alarm_dk`

```c
uint16_t fuel_gauge_prop_val::high_temperature_alarm_dk
```

对应属性（Property）：`FUEL_GAUGE_HIGH_TEMPERATURE_ALARM_DK`。

<a id="a2b044d7e33e98fd0c0cead2a3de61431"></a>

### `high_voltage_alarm`

```c
uint32_t fuel_gauge_prop_val::high_voltage_alarm
```

对应属性（Property）：`FUEL_GAUGE_HIGH_VOLTAGE_ALARM`。

**已弃用（Deprecated）**：已弃用（Deprecated）：请改用 `fuel_gauge_prop_val::high_voltage_alarm_uv`。

<a id="acf5b8f9b1ff3b3c5b5547d4920dbd7f2"></a>

### `high_voltage_alarm_uv`

```c
uint32_t fuel_gauge_prop_val::high_voltage_alarm_uv
```

对应属性（Property）：`FUEL_GAUGE_HIGH_VOLTAGE_ALARM_UV`。

<a id="aaa55eae9e98203e5f1847d6162d1d28e"></a>

### `low_current_alarm`

```c
int32_t fuel_gauge_prop_val::low_current_alarm
```

对应属性（Property）：`FUEL_GAUGE_LOW_CURRENT_ALARM`。

**已弃用（Deprecated）**：已弃用（Deprecated）：请改用 `fuel_gauge_prop_val::low_current_alarm_ua`。

<a id="a49e894ef1b0f7be9c5a1dba12a8cff41"></a>

### `low_current_alarm_ua`

```c
int32_t fuel_gauge_prop_val::low_current_alarm_ua
```

对应属性（Property）：`FUEL_GAUGE_LOW_CURRENT_ALARM_UA`。

<a id="aef3ced90ca261ec7501778a41f12963d"></a>

### `low_gpio_alarm`

```c
int32_t fuel_gauge_prop_val::low_gpio_alarm
```

对应属性（Property）：`FUEL_GAUGE_LOW_GPIO_ALARM`。

**已弃用（Deprecated）**：已弃用（Deprecated）：请改用 `fuel_gauge_prop_val::low_gpio_alarm_uv`。

<a id="a4ce4046d3284afa7fd2e37d510cf4fd2"></a>

### `low_gpio_alarm_uv`

```c
int32_t fuel_gauge_prop_val::low_gpio_alarm_uv
```

对应属性（Property）：`FUEL_GAUGE_LOW_GPIO_ALARM_UV`。

<a id="ad8d424fbbe3124cde5e82b74957a4885"></a>

### `low_temperature_alarm`

```c
uint16_t fuel_gauge_prop_val::low_temperature_alarm
```

对应属性（Property）：`FUEL_GAUGE_LOW_TEMPERATURE_ALARM`。

**已弃用（Deprecated）**：已弃用（Deprecated）：请改用 `fuel_gauge_prop_val::low_temperature_alarm_dk`。

<a id="a163ecf351a2a538cac53757ad402dde0"></a>

### `low_temperature_alarm_dk`

```c
uint16_t fuel_gauge_prop_val::low_temperature_alarm_dk
```

对应属性（Property）：`FUEL_GAUGE_LOW_TEMPERATURE_ALARM_DK`。

<a id="aff81db28e93cb70ebea6793e4493915f"></a>

### `low_voltage_alarm`

```c
uint32_t fuel_gauge_prop_val::low_voltage_alarm
```

对应属性（Property）：`FUEL_GAUGE_LOW_VOLTAGE_ALARM`。

**已弃用（Deprecated）**：已弃用（Deprecated）：请改用 `fuel_gauge_prop_val::low_voltage_alarm_uv`。

<a id="aee04c49d39652837420039fb968ecea5"></a>

### `low_voltage_alarm_uv`

```c
uint32_t fuel_gauge_prop_val::low_voltage_alarm_uv
```

对应属性（Property）：`FUEL_GAUGE_LOW_VOLTAGE_ALARM_UV`。

<a id="a4916bb50489c5f70335da2f11ed9477e"></a>

### `present_state`

```c
bool fuel_gauge_prop_val::present_state
```

对应属性（Property）：`FUEL_GAUGE_PRESENT_STATE`。

<a id="a45b20c5118f7ee408d507b94e6cae1dc"></a>

### `relative_state_of_charge`

```c
uint8_t fuel_gauge_prop_val::relative_state_of_charge
```

对应属性（Property）：`FUEL_GAUGE_RELATIVE_STATE_OF_CHARGE`。

**已弃用（Deprecated）**：已弃用（Deprecated）：请改用 `fuel_gauge_prop_val::relative_state_of_charge_pct`。

<a id="a94893761a1f77a9c0e746c34e5bb6e61"></a>

### `relative_state_of_charge_pct`

```c
uint8_t fuel_gauge_prop_val::relative_state_of_charge_pct
```

对应属性（Property）：`FUEL_GAUGE_RELATIVE_STATE_OF_CHARGE_PCT`。

<a id="adecf57aa90e2b5d483cfd889ec512400"></a>

### `remaining_capacity`

```c
uint32_t fuel_gauge_prop_val::remaining_capacity
```

对应属性（Property）：`FUEL_GAUGE_REMAINING_CAPACITY`。

**已弃用（Deprecated）**：已弃用（Deprecated）：请改用 `fuel_gauge_prop_val::remaining_capacity_uah`。

<a id="ab19f11342d10502937595b535db09c7a"></a>

### `remaining_capacity_uah`

```c
uint32_t fuel_gauge_prop_val::remaining_capacity_uah
```

对应属性（Property）：`FUEL_GAUGE_REMAINING_CAPACITY_UAH`。

<a id="ae716bdf1346dc7767d98526db6083008"></a>

### `runtime_to_empty`

```c
uint32_t fuel_gauge_prop_val::runtime_to_empty
```

对应属性（Property）：`FUEL_GAUGE_RUNTIME_TO_EMPTY`。

**已弃用（Deprecated）**：已弃用（Deprecated）：请改用 `fuel_gauge_prop_val::runtime_to_empty_mins`。

<a id="af40db6b3dba16b20097d0767e51a07c5"></a>

### `runtime_to_empty_mins`

```c
uint32_t fuel_gauge_prop_val::runtime_to_empty_mins
```

对应属性（Property）：`FUEL_GAUGE_RUNTIME_TO_EMPTY_MINS`。

<a id="a2c77e8de7fa40fadfa13dfd4c94df804"></a>

### `runtime_to_full`

```c
uint32_t fuel_gauge_prop_val::runtime_to_full
```

对应属性（Property）：`FUEL_GAUGE_RUNTIME_TO_FULL`。

**已弃用（Deprecated）**：已弃用（Deprecated）：请改用 `fuel_gauge_prop_val::runtime_to_full_mins`。

<a id="a600a90fd8d847bd29ffd9d96822abdb8"></a>

### `runtime_to_full_mins`

```c
uint32_t fuel_gauge_prop_val::runtime_to_full_mins
```

对应属性（Property）：`FUEL_GAUGE_RUNTIME_TO_FULL_MINS`。

<a id="aa5529fea5cfe765be9b66f5fad96ab2f"></a>

### `sbs_at_rate`

```c
int16_t fuel_gauge_prop_val::sbs_at_rate
```

对应属性（Property）：`FUEL_GAUGE_SBS_ATRATE`。

<a id="a9b5015878c9a77d9c8330139f94843b7"></a>

### `sbs_at_rate_ok`

```c
bool fuel_gauge_prop_val::sbs_at_rate_ok
```

对应属性（Property）：`FUEL_GAUGE_SBS_ATRATE_OK`。

<a id="a7c8b6f9ee98e5b97ddc85b7e72cea4a8"></a>

### `sbs_at_rate_time_to_empty`

```c
uint16_t fuel_gauge_prop_val::sbs_at_rate_time_to_empty
```

对应属性（Property）：`FUEL_GAUGE_SBS_ATRATE_TIME_TO_EMPTY`。

**已弃用（Deprecated）**：已弃用（Deprecated）：请改用 `fuel_gauge_prop_val::sbs_at_rate_time_to_empty_mins`。

<a id="adbfa0be8653107875e91edd5db40265d"></a>

### `sbs_at_rate_time_to_empty_mins`

```c
uint16_t fuel_gauge_prop_val::sbs_at_rate_time_to_empty_mins
```

对应属性（Property）：`FUEL_GAUGE_SBS_ATRATE_TIME_TO_EMPTY_MINS`。

<a id="aeeeddb48f22b54f90c603d58e9ffa9a5"></a>

### `sbs_at_rate_time_to_full`

```c
uint16_t fuel_gauge_prop_val::sbs_at_rate_time_to_full
```

对应属性（Property）：`FUEL_GAUGE_SBS_ATRATE_TIME_TO_FULL`。

**已弃用（Deprecated）**：已弃用（Deprecated）：请改用 `fuel_gauge_prop_val::sbs_at_rate_time_to_full_mins`。

<a id="a8bc68c65571afb6856e7e1e6cb33a5e4"></a>

### `sbs_at_rate_time_to_full_mins`

```c
uint16_t fuel_gauge_prop_val::sbs_at_rate_time_to_full_mins
```

对应属性（Property）：`FUEL_GAUGE_SBS_ATRATE_TIME_TO_FULL_MINS`。

<a id="a957025a2a9fb7709e2bf478f15fd31a0"></a>

### `sbs_mfr_access_word`

```c
uint16_t fuel_gauge_prop_val::sbs_mfr_access_word
```

对应属性（Property）：`FUEL_GAUGE_SBS_MFR_ACCESS`。

<a id="a7fc0551e303de56e0eb6bdac1ecaccd0"></a>

### `sbs_mode`

```c
uint16_t fuel_gauge_prop_val::sbs_mode
```

对应属性（Property）：`FUEL_GAUGE_SBS_MODE`。

<a id="a818ab7faf8f51d4d1a5c5f070d54b997"></a>

### `sbs_remaining_capacity_alarm`

```c
uint16_t fuel_gauge_prop_val::sbs_remaining_capacity_alarm
```

对应属性（Property）：`FUEL_GAUGE_SBS_REMAINING_CAPACITY_ALARM`。

<a id="aa0e46c727bb31acb5d41ce4bc6d5b106"></a>

### `sbs_remaining_time_alarm`

```c
uint16_t fuel_gauge_prop_val::sbs_remaining_time_alarm
```

对应属性（Property）：`FUEL_GAUGE_SBS_REMAINING_TIME_ALARM`。

**已弃用（Deprecated）**：已弃用（Deprecated）：请改用 `fuel_gauge_prop_val::sbs_remaining_time_alarm_mins`。

<a id="a0b6878d02d4d5a3865e8ca8d57951914"></a>

### `sbs_remaining_time_alarm_mins`

```c
uint16_t fuel_gauge_prop_val::sbs_remaining_time_alarm_mins
```

对应属性（Property）：`FUEL_GAUGE_SBS_REMAINING_TIME_ALARM_MINS`。

<a id="aa901ef363509234577d73958984862a4"></a>

### `state_of_charge_alarm`

```c
uint8_t fuel_gauge_prop_val::state_of_charge_alarm
```

对应属性（Property）：`FUEL_GAUGE_STATE_OF_CHARGE_ALARM`。

**已弃用（Deprecated）**：已弃用（Deprecated）：请改用 `fuel_gauge_prop_val::state_of_charge_alarm_pct`。

<a id="ab43ccbb0a1443e64d26e498d31d1a240"></a>

### `state_of_charge_alarm_pct`

```c
uint8_t fuel_gauge_prop_val::state_of_charge_alarm_pct
```

对应属性（Property）：`FUEL_GAUGE_STATE_OF_CHARGE_ALARM_PCT`。

<a id="a1638b4b54bf57af650832e53f9ce90a4"></a>

### `state_of_health`

```c
uint8_t fuel_gauge_prop_val::state_of_health
```

对应属性（Property）：`FUEL_GAUGE_STATE_OF_HEALTH`。

<a id="a36528b111568bd1c90859e454610fd9f"></a>

### `temperature`

```c
uint16_t fuel_gauge_prop_val::temperature
```

对应属性（Property）：`FUEL_GAUGE_TEMPERATURE`。

**已弃用（Deprecated）**：已弃用（Deprecated）：请改用 `fuel_gauge_prop_val::temperature_dk`。

<a id="a7d943c31ad7dd53d16bfded98e70b332"></a>

### `temperature_dk`

```c
uint16_t fuel_gauge_prop_val::temperature_dk
```

对应属性（Property）：`FUEL_GAUGE_TEMPERATURE_DK`。

<a id="a9e12460af8ae1a0ba0d1838e977e7a59"></a>

### `therm_voltage_uv`

```c
uint32_t fuel_gauge_prop_val::therm_voltage_uv
```

对应属性（Property）：`FUEL_GAUGE_THERM_VOLTAGE_UV`。

<a id="abec5cadefa09e088620a9598dec9c473"></a>

### `voltage`

```c
int fuel_gauge_prop_val::voltage
```

对应属性（Property）：`FUEL_GAUGE_VOLTAGE`。

**已弃用（Deprecated）**：已弃用（Deprecated）：请改用 `fuel_gauge_prop_val::voltage_uv`。

<a id="aa52341a118d1445ee762ba1563406441"></a>

### `voltage_uv`

```c
int32_t fuel_gauge_prop_val::voltage_uv
```

对应属性（Property）：`FUEL_GAUGE_VOLTAGE_UV`。

本数据类型文档由以下文件生成：

- `zephyr/drivers/fuel_gauge.h`

## 106.3\_原页交叉引用（Cross References）

- [zephyr/drivers/fuel_gauge.h](https://docs.zephyrproject.org/latest/doxygen/html/fuel__gauge_8h_source.html)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)
- [fuel_gauge_custom_value_int_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#gaf8c7f6c4f49dd420df6841c43c41d615)
- [fuel_gauge_custom_value_uint_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ga08e4dae43d5169da58af32ec419ef9e8)
- [fuel_gauge_custom_value_bool_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ga44fd24de7d165388a87e6dd74f6547af)
- [Deprecated](https://docs.zephyrproject.org/latest/doxygen/html/deprecated.html#_deprecated000045)
- [Deprecated](https://docs.zephyrproject.org/latest/doxygen/html/deprecated.html#_deprecated000039)
- [Deprecated](https://docs.zephyrproject.org/latest/doxygen/html/deprecated.html#_deprecated000049)
- [Deprecated](https://docs.zephyrproject.org/latest/doxygen/html/deprecated.html#_deprecated000050)
- [Deprecated](https://docs.zephyrproject.org/latest/doxygen/html/deprecated.html#_deprecated000040)
- [Deprecated](https://docs.zephyrproject.org/latest/doxygen/html/deprecated.html#_deprecated000051)
- [Deprecated](https://docs.zephyrproject.org/latest/doxygen/html/deprecated.html#_deprecated000041)
- [Deprecated](https://docs.zephyrproject.org/latest/doxygen/html/deprecated.html#_deprecated000062)
- [Deprecated](https://docs.zephyrproject.org/latest/doxygen/html/deprecated.html#_deprecated000059)
- [Deprecated](https://docs.zephyrproject.org/latest/doxygen/html/deprecated.html#_deprecated000064)
- [Deprecated](https://docs.zephyrproject.org/latest/doxygen/html/deprecated.html#_deprecated000061)
- [Deprecated](https://docs.zephyrproject.org/latest/doxygen/html/deprecated.html#_deprecated000057)
- [Deprecated](https://docs.zephyrproject.org/latest/doxygen/html/deprecated.html#_deprecated000058)
- [Deprecated](https://docs.zephyrproject.org/latest/doxygen/html/deprecated.html#_deprecated000063)
- [Deprecated](https://docs.zephyrproject.org/latest/doxygen/html/deprecated.html#_deprecated000060)
- [Deprecated](https://docs.zephyrproject.org/latest/doxygen/html/deprecated.html#_deprecated000056)
- [Deprecated](https://docs.zephyrproject.org/latest/doxygen/html/deprecated.html#_deprecated000046)
- [Deprecated](https://docs.zephyrproject.org/latest/doxygen/html/deprecated.html#_deprecated000042)
- [Deprecated](https://docs.zephyrproject.org/latest/doxygen/html/deprecated.html#_deprecated000043)
- [Deprecated](https://docs.zephyrproject.org/latest/doxygen/html/deprecated.html#_deprecated000044)
- [Deprecated](https://docs.zephyrproject.org/latest/doxygen/html/deprecated.html#_deprecated000053)
- [Deprecated](https://docs.zephyrproject.org/latest/doxygen/html/deprecated.html#_deprecated000052)
- [Deprecated](https://docs.zephyrproject.org/latest/doxygen/html/deprecated.html#_deprecated000054)
- [Deprecated](https://docs.zephyrproject.org/latest/doxygen/html/deprecated.html#_deprecated000055)
- [Deprecated](https://docs.zephyrproject.org/latest/doxygen/html/deprecated.html#_deprecated000047)
- [Deprecated](https://docs.zephyrproject.org/latest/doxygen/html/deprecated.html#_deprecated000048)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P105_clock_mchp_xec_subsys_联合体.md) · [返回大纲](大纲.md) · [下一章](P107_pd_augmented_supply_pdo_sink_联合体.md)
