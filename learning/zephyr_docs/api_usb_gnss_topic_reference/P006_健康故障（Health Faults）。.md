---
id: learning.zephyr-docs.api-usb-gnss-topic-reference.page-6
title: 健康故障（Health Faults）。
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__faults.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_健康故障（Health Faults）。

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__health__faults.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

规范定义的健康故障值（Health fault values）列表。

<a id="details"></a>

规范定义的健康故障值（Health fault values）列表。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 6.1\_宏定义（Macros）

<a id="r_ga5fe6993bb219f6547b67e6720f7bf526"></a>

```c
#define BT_MESH_HEALTH_FAULT_NO_FAULT 0x00
```

相关声明：[BT_MESH_HEALTH_FAULT_NO_FAULT](#ga5fe6993bb219f6547b67e6720f7bf526)。

未发生故障（No Fault）。

<a id="r_gaa75f0a4d758476e2fdeaa94b1ad98b55"></a>

```c
#define BT_MESH_HEALTH_FAULT_BATTERY_LOW_WARNING 0x01
```

相关声明：[BT_MESH_HEALTH_FAULT_BATTERY_LOW_WARNING](#gaa75f0a4d758476e2fdeaa94b1ad98b55)。

电池电量低警告（Battery Low Warning）。

<a id="r_gaaa682f49f35e6764af0429690aebf20e"></a>

```c
#define BT_MESH_HEALTH_FAULT_BATTERY_LOW_ERROR 0x02
```

相关声明：[BT_MESH_HEALTH_FAULT_BATTERY_LOW_ERROR](#gaaa682f49f35e6764af0429690aebf20e)。

电池电量低错误（Battery Low Error）。

<a id="r_ga0a77dbd3aa3bddeab0cbcf434d36f791"></a>

```c
#define BT_MESH_HEALTH_FAULT_SUPPLY_VOLTAGE_TOO_LOW_WARNING 0x03
```

相关声明：[BT_MESH_HEALTH_FAULT_SUPPLY_VOLTAGE_TOO_LOW_WARNING](#ga0a77dbd3aa3bddeab0cbcf434d36f791)。

供电电压过低警告（Supply Voltage Too Low Warning）。

<a id="r_gab64bbf32cda9d9cd8e82a05f7c9924a1"></a>

```c
#define BT_MESH_HEALTH_FAULT_SUPPLY_VOLTAGE_TOO_LOW_ERROR 0x04
```

相关声明：[BT_MESH_HEALTH_FAULT_SUPPLY_VOLTAGE_TOO_LOW_ERROR](#gab64bbf32cda9d9cd8e82a05f7c9924a1)。

供电电压过低错误（Supply Voltage Too Low Error）。

<a id="r_ga7838991d14a19ef401a41d96bec76287"></a>

```c
#define BT_MESH_HEALTH_FAULT_SUPPLY_VOLTAGE_TOO_HIGH_WARNING 0x05
```

相关声明：[BT_MESH_HEALTH_FAULT_SUPPLY_VOLTAGE_TOO_HIGH_WARNING](#ga7838991d14a19ef401a41d96bec76287)。

供电电压过高警告（Supply Voltage Too High Warning）。

<a id="r_ga86d34960a167c0c3f8a1f320d1843702"></a>

```c
#define BT_MESH_HEALTH_FAULT_SUPPLY_VOLTAGE_TOO_HIGH_ERROR 0x06
```

相关声明：[BT_MESH_HEALTH_FAULT_SUPPLY_VOLTAGE_TOO_HIGH_ERROR](#ga86d34960a167c0c3f8a1f320d1843702)。

供电电压过高错误（Supply Voltage Too High Error）。

<a id="r_ga326ce2242e409c9577d324388509b7b7"></a>

```c
#define BT_MESH_HEALTH_FAULT_POWER_SUPPLY_INTERRUPTED_WARNING 0x07
```

相关声明：[BT_MESH_HEALTH_FAULT_POWER_SUPPLY_INTERRUPTED_WARNING](#ga326ce2242e409c9577d324388509b7b7)。

供电中断警告（Power Supply Interrupted Warning）。

<a id="r_gaf1fff982760290c80424b87a60bff822"></a>

```c
#define BT_MESH_HEALTH_FAULT_POWER_SUPPLY_INTERRUPTED_ERROR 0x08
```

相关声明：[BT_MESH_HEALTH_FAULT_POWER_SUPPLY_INTERRUPTED_ERROR](#gaf1fff982760290c80424b87a60bff822)。

供电中断错误（Power Supply Interrupted Error）。

<a id="r_gab92ab13dbc9799476e6e627a81080e14"></a>

```c
#define BT_MESH_HEALTH_FAULT_NO_LOAD_WARNING 0x09
```

相关声明：[BT_MESH_HEALTH_FAULT_NO_LOAD_WARNING](#gab92ab13dbc9799476e6e627a81080e14)。

无负载警告（No Load Warning）。

<a id="r_ga29b5e94269715a8301bc363cb66db370"></a>

```c
#define BT_MESH_HEALTH_FAULT_NO_LOAD_ERROR 0x0A
```

相关声明：[BT_MESH_HEALTH_FAULT_NO_LOAD_ERROR](#ga29b5e94269715a8301bc363cb66db370)。

无负载错误（No Load Error）。

<a id="r_gacd14cc12794077cc517d5fefa748c9c6"></a>

```c
#define BT_MESH_HEALTH_FAULT_OVERLOAD_WARNING 0x0B
```

相关声明：[BT_MESH_HEALTH_FAULT_OVERLOAD_WARNING](#gacd14cc12794077cc517d5fefa748c9c6)。

过载警告（Overload Warning）。

<a id="r_gafafa715a04011e80944199d93ee6c51b"></a>

```c
#define BT_MESH_HEALTH_FAULT_OVERLOAD_ERROR 0x0C
```

相关声明：[BT_MESH_HEALTH_FAULT_OVERLOAD_ERROR](#gafafa715a04011e80944199d93ee6c51b)。

过载错误（Overload Error）。

<a id="r_gac737fc53f2184bd1664f0da5388148ac"></a>

```c
#define BT_MESH_HEALTH_FAULT_OVERHEAT_WARNING 0x0D
```

相关声明：[BT_MESH_HEALTH_FAULT_OVERHEAT_WARNING](#gac737fc53f2184bd1664f0da5388148ac)。

过热警告（Overheat Warning）。

<a id="r_ga1c47ccb73f94cee4db7d300679972300"></a>

```c
#define BT_MESH_HEALTH_FAULT_OVERHEAT_ERROR 0x0E
```

相关声明：[BT_MESH_HEALTH_FAULT_OVERHEAT_ERROR](#ga1c47ccb73f94cee4db7d300679972300)。

过热错误（Overheat Error）。

<a id="r_ga95fd40c6066a37417ebfc9916b06db7c"></a>

```c
#define BT_MESH_HEALTH_FAULT_CONDENSATION_WARNING 0x0F
```

相关声明：[BT_MESH_HEALTH_FAULT_CONDENSATION_WARNING](#ga95fd40c6066a37417ebfc9916b06db7c)。

凝露警告（Condensation Warning）。

<a id="r_ga3da2c495908e3b4aac524e5d91c58189"></a>

```c
#define BT_MESH_HEALTH_FAULT_CONDENSATION_ERROR 0x10
```

相关声明：[BT_MESH_HEALTH_FAULT_CONDENSATION_ERROR](#ga3da2c495908e3b4aac524e5d91c58189)。

凝露错误（Condensation Error）。

<a id="r_ga7fb07118fea783803bfa8f419441740f"></a>

```c
#define BT_MESH_HEALTH_FAULT_VIBRATION_WARNING 0x11
```

相关声明：[BT_MESH_HEALTH_FAULT_VIBRATION_WARNING](#ga7fb07118fea783803bfa8f419441740f)。

振动警告（Vibration Warning）。

<a id="r_ga1b9f51d2760530bc170a81ff29435cf3"></a>

```c
#define BT_MESH_HEALTH_FAULT_VIBRATION_ERROR 0x12
```

相关声明：[BT_MESH_HEALTH_FAULT_VIBRATION_ERROR](#ga1b9f51d2760530bc170a81ff29435cf3)。

振动错误（Vibration Error）。

<a id="r_ga4e46ae0ebd52722c1600f2025a2fb190"></a>

```c
#define BT_MESH_HEALTH_FAULT_CONFIGURATION_WARNING 0x13
```

相关声明：[BT_MESH_HEALTH_FAULT_CONFIGURATION_WARNING](#ga4e46ae0ebd52722c1600f2025a2fb190)。

配置警告（Configuration Warning）。

<a id="r_ga03ee761cb0a2d5cbf3509a719e658621"></a>

```c
#define BT_MESH_HEALTH_FAULT_CONFIGURATION_ERROR 0x14
```

相关声明：[BT_MESH_HEALTH_FAULT_CONFIGURATION_ERROR](#ga03ee761cb0a2d5cbf3509a719e658621)。

配置错误（Configuration Error）。

<a id="r_ga0e50ab22bffb357f02acf4860664d535"></a>

```c
#define BT_MESH_HEALTH_FAULT_ELEMENT_NOT_CALIBRATED_WARNING 0x15
```

相关声明：[BT_MESH_HEALTH_FAULT_ELEMENT_NOT_CALIBRATED_WARNING](#ga0e50ab22bffb357f02acf4860664d535)。

元素未校准警告（Element Not Calibrated Warning）。

<a id="r_gaa612dbc60cc9ab0fe4978a0992499009"></a>

```c
#define BT_MESH_HEALTH_FAULT_ELEMENT_NOT_CALIBRATED_ERROR 0x16
```

相关声明：[BT_MESH_HEALTH_FAULT_ELEMENT_NOT_CALIBRATED_ERROR](#gaa612dbc60cc9ab0fe4978a0992499009)。

元素未校准错误（Element Not Calibrated Error）。

<a id="r_gabf766439091f937438a0e736ddc892b4"></a>

```c
#define BT_MESH_HEALTH_FAULT_MEMORY_WARNING 0x17
```

相关声明：[BT_MESH_HEALTH_FAULT_MEMORY_WARNING](#gabf766439091f937438a0e736ddc892b4)。

内存警告（Memory Warning）。

<a id="r_ga358d3351b1935b3a4c259060902033db"></a>

```c
#define BT_MESH_HEALTH_FAULT_MEMORY_ERROR 0x18
```

相关声明：[BT_MESH_HEALTH_FAULT_MEMORY_ERROR](#ga358d3351b1935b3a4c259060902033db)。

内存错误（Memory Error）。

<a id="r_ga8d60f38c1560c269fdfd18de35daf5d6"></a>

```c
#define BT_MESH_HEALTH_FAULT_SELF_TEST_WARNING 0x19
```

相关声明：[BT_MESH_HEALTH_FAULT_SELF_TEST_WARNING](#ga8d60f38c1560c269fdfd18de35daf5d6)。

自测试警告（Self-Test Warning）。

<a id="r_ga75214891137e1045bcc83c4c54458e77"></a>

```c
#define BT_MESH_HEALTH_FAULT_SELF_TEST_ERROR 0x1A
```

相关声明：[BT_MESH_HEALTH_FAULT_SELF_TEST_ERROR](#ga75214891137e1045bcc83c4c54458e77)。

自测试错误（Self-Test Error）。

<a id="r_ga124bb981c3ab2c41eda2ddf3bc85b5f2"></a>

```c
#define BT_MESH_HEALTH_FAULT_INPUT_TOO_LOW_WARNING 0x1B
```

相关声明：[BT_MESH_HEALTH_FAULT_INPUT_TOO_LOW_WARNING](#ga124bb981c3ab2c41eda2ddf3bc85b5f2)。

输入过低警告（Input Too Low Warning）。

<a id="r_ga33c5b4f773c6afe73f64a14411033b3f"></a>

```c
#define BT_MESH_HEALTH_FAULT_INPUT_TOO_LOW_ERROR 0x1C
```

相关声明：[BT_MESH_HEALTH_FAULT_INPUT_TOO_LOW_ERROR](#ga33c5b4f773c6afe73f64a14411033b3f)。

输入过低错误（Input Too Low Error）。

<a id="r_gae3c188075202eeff7292ab56e03e31a9"></a>

```c
#define BT_MESH_HEALTH_FAULT_INPUT_TOO_HIGH_WARNING 0x1D
```

相关声明：[BT_MESH_HEALTH_FAULT_INPUT_TOO_HIGH_WARNING](#gae3c188075202eeff7292ab56e03e31a9)。

输入过高警告（Input Too High Warning）。

<a id="r_gad42b0f690836deae1dcbb4757e885c02"></a>

```c
#define BT_MESH_HEALTH_FAULT_INPUT_TOO_HIGH_ERROR 0x1E
```

相关声明：[BT_MESH_HEALTH_FAULT_INPUT_TOO_HIGH_ERROR](#gad42b0f690836deae1dcbb4757e885c02)。

输入过高错误（Input Too High Error）。

<a id="r_ga5a1ba1561e93574e0d4598bd90c386b8"></a>

```c
#define BT_MESH_HEALTH_FAULT_INPUT_NO_CHANGE_WARNING 0x1F
```

相关声明：[BT_MESH_HEALTH_FAULT_INPUT_NO_CHANGE_WARNING](#ga5a1ba1561e93574e0d4598bd90c386b8)。

输入无变化警告（Input No Change Warning）。

<a id="r_ga3789605186fe9c172d3320a22a21ead6"></a>

```c
#define BT_MESH_HEALTH_FAULT_INPUT_NO_CHANGE_ERROR 0x20
```

相关声明：[BT_MESH_HEALTH_FAULT_INPUT_NO_CHANGE_ERROR](#ga3789605186fe9c172d3320a22a21ead6)。

输入无变化错误（Input No Change Error）。

<a id="r_gaf51ad764a78b425cda29720c4e063221"></a>

```c
#define BT_MESH_HEALTH_FAULT_ACTUATOR_BLOCKED_WARNING 0x21
```

相关声明：[BT_MESH_HEALTH_FAULT_ACTUATOR_BLOCKED_WARNING](#gaf51ad764a78b425cda29720c4e063221)。

执行器受阻警告（Actuator Blocked Warning）。

<a id="r_ga0493f52939a375fcebe33d45451b618c"></a>

```c
#define BT_MESH_HEALTH_FAULT_ACTUATOR_BLOCKED_ERROR 0x22
```

相关声明：[BT_MESH_HEALTH_FAULT_ACTUATOR_BLOCKED_ERROR](#ga0493f52939a375fcebe33d45451b618c)。

执行器受阻错误（Actuator Blocked Error）。

<a id="r_ga03cfae918863f10dd5aaab6fd3a82b07"></a>

```c
#define BT_MESH_HEALTH_FAULT_HOUSING_OPENED_WARNING 0x23
```

相关声明：[BT_MESH_HEALTH_FAULT_HOUSING_OPENED_WARNING](#ga03cfae918863f10dd5aaab6fd3a82b07)。

外壳打开警告（Housing Opened Warning）。

<a id="r_ga7308395342cc226ef17584aebfa78d2c"></a>

```c
#define BT_MESH_HEALTH_FAULT_HOUSING_OPENED_ERROR 0x24
```

相关声明：[BT_MESH_HEALTH_FAULT_HOUSING_OPENED_ERROR](#ga7308395342cc226ef17584aebfa78d2c)。

外壳打开错误（Housing Opened Error）。

<a id="r_ga66d4e92380a42b0491848a261a36246b"></a>

```c
#define BT_MESH_HEALTH_FAULT_TAMPER_WARNING 0x25
```

相关声明：[BT_MESH_HEALTH_FAULT_TAMPER_WARNING](#ga66d4e92380a42b0491848a261a36246b)。

篡改警告（Tamper Warning）。

<a id="r_ga69b7755dd511f30864272ad1465f2965"></a>

```c
#define BT_MESH_HEALTH_FAULT_TAMPER_ERROR 0x26
```

相关声明：[BT_MESH_HEALTH_FAULT_TAMPER_ERROR](#ga69b7755dd511f30864272ad1465f2965)。

篡改错误（Tamper Error）。

<a id="r_ga1494db7b9a0fbab15119a65da0b6b0d0"></a>

```c
#define BT_MESH_HEALTH_FAULT_DEVICE_MOVED_WARNING 0x27
```

相关声明：[BT_MESH_HEALTH_FAULT_DEVICE_MOVED_WARNING](#ga1494db7b9a0fbab15119a65da0b6b0d0)。

设备被移动警告（Device Moved Warning）。

<a id="r_ga482eb25cfcfd943342f8d30ed976bc24"></a>

```c
#define BT_MESH_HEALTH_FAULT_DEVICE_MOVED_ERROR 0x28
```

相关声明：[BT_MESH_HEALTH_FAULT_DEVICE_MOVED_ERROR](#ga482eb25cfcfd943342f8d30ed976bc24)。

设备被移动错误（Device Moved Error）。

<a id="r_ga7f158981cf1282acaca0839244e3c6cb"></a>

```c
#define BT_MESH_HEALTH_FAULT_DEVICE_DROPPED_WARNING 0x29
```

相关声明：[BT_MESH_HEALTH_FAULT_DEVICE_DROPPED_WARNING](#ga7f158981cf1282acaca0839244e3c6cb)。

设备跌落警告（Device Dropped Warning）。

<a id="r_ga2d0909640905067168ba45bea0523618"></a>

```c
#define BT_MESH_HEALTH_FAULT_DEVICE_DROPPED_ERROR 0x2A
```

相关声明：[BT_MESH_HEALTH_FAULT_DEVICE_DROPPED_ERROR](#ga2d0909640905067168ba45bea0523618)。

设备跌落错误（Device Dropped Error）。

<a id="r_ga95d30649750b543650c3a21cc8719c3e"></a>

```c
#define BT_MESH_HEALTH_FAULT_OVERFLOW_WARNING 0x2B
```

相关声明：[BT_MESH_HEALTH_FAULT_OVERFLOW_WARNING](#ga95d30649750b543650c3a21cc8719c3e)。

溢出警告（Overflow Warning）。

<a id="r_ga63b9b85427e0efa31e8a1496065b3dc9"></a>

```c
#define BT_MESH_HEALTH_FAULT_OVERFLOW_ERROR 0x2C
```

相关声明：[BT_MESH_HEALTH_FAULT_OVERFLOW_ERROR](#ga63b9b85427e0efa31e8a1496065b3dc9)。

溢出错误（Overflow Error）。

<a id="r_gada2400efbf70229ce8328a9ace7fcccf"></a>

```c
#define BT_MESH_HEALTH_FAULT_EMPTY_WARNING 0x2D
```

相关声明：[BT_MESH_HEALTH_FAULT_EMPTY_WARNING](#gada2400efbf70229ce8328a9ace7fcccf)。

空状态警告（Empty Warning）。

<a id="r_ga0b0414621784d1a3c872077e0b578d0d"></a>

```c
#define BT_MESH_HEALTH_FAULT_EMPTY_ERROR 0x2E
```

相关声明：[BT_MESH_HEALTH_FAULT_EMPTY_ERROR](#ga0b0414621784d1a3c872077e0b578d0d)。

空状态错误（Empty Error）。

<a id="r_ga534b85b4f805b585c4c4d29e6abe782a"></a>

```c
#define BT_MESH_HEALTH_FAULT_INTERNAL_BUS_WARNING 0x2F
```

相关声明：[BT_MESH_HEALTH_FAULT_INTERNAL_BUS_WARNING](#ga534b85b4f805b585c4c4d29e6abe782a)。

内部总线警告（Internal Bus Warning）。

<a id="r_ga54b4657666c01dca9417d58e302ff738"></a>

```c
#define BT_MESH_HEALTH_FAULT_INTERNAL_BUS_ERROR 0x30
```

相关声明：[BT_MESH_HEALTH_FAULT_INTERNAL_BUS_ERROR](#ga54b4657666c01dca9417d58e302ff738)。

内部总线错误（Internal Bus Error）。

<a id="r_gae1113f6fcaae95b1a7cfe2dd95c287ab"></a>

```c
#define BT_MESH_HEALTH_FAULT_MECHANISM_JAMMED_WARNING 0x31
```

相关声明：[BT_MESH_HEALTH_FAULT_MECHANISM_JAMMED_WARNING](#gae1113f6fcaae95b1a7cfe2dd95c287ab)。

机械机构卡住警告（Mechanism Jammed Warning）。

<a id="r_gaa6ccb4569d63b6eb0dc53ec7211f2f98"></a>

```c
#define BT_MESH_HEALTH_FAULT_MECHANISM_JAMMED_ERROR 0x32
```

相关声明：[BT_MESH_HEALTH_FAULT_MECHANISM_JAMMED_ERROR](#gaa6ccb4569d63b6eb0dc53ec7211f2f98)。

机械机构卡住错误（Mechanism Jammed Error）。

<a id="r_gae0b8ecef9c11e17a02ede6a4b416c3b8"></a>

```c
#define BT_MESH_HEALTH_FAULT_VENDOR_SPECIFIC_START 0x80
```

相关声明：[BT_MESH_HEALTH_FAULT_VENDOR_SPECIFIC_START](#gae0b8ecef9c11e17a02ede6a4b416c3b8)。

厂商特定故障值（Vendor-specific Fault Values）的起始值。

## 6.2\_详细说明（Detailed Documentation）

<a id="ga0493f52939a375fcebe33d45451b618c"></a>

### `BT_MESH_HEALTH_FAULT_ACTUATOR_BLOCKED_ERROR`

```c
#define BT_MESH_HEALTH_FAULT_ACTUATOR_BLOCKED_ERROR 0x22
```

```c
#include <zephyr/bluetooth/mesh/health_faults.h>
```

执行器受阻错误（Actuator Blocked Error）。

<a id="gaf51ad764a78b425cda29720c4e063221"></a>

### `BT_MESH_HEALTH_FAULT_ACTUATOR_BLOCKED_WARNING`

```c
#define BT_MESH_HEALTH_FAULT_ACTUATOR_BLOCKED_WARNING 0x21
```

```c
#include <zephyr/bluetooth/mesh/health_faults.h>
```

执行器受阻警告（Actuator Blocked Warning）。

<a id="gaaa682f49f35e6764af0429690aebf20e"></a>

### `BT_MESH_HEALTH_FAULT_BATTERY_LOW_ERROR`

```c
#define BT_MESH_HEALTH_FAULT_BATTERY_LOW_ERROR 0x02
```

```c
#include <zephyr/bluetooth/mesh/health_faults.h>
```

电池电量低错误（Battery Low Error）。

<a id="gaa75f0a4d758476e2fdeaa94b1ad98b55"></a>

### `BT_MESH_HEALTH_FAULT_BATTERY_LOW_WARNING`

```c
#define BT_MESH_HEALTH_FAULT_BATTERY_LOW_WARNING 0x01
```

```c
#include <zephyr/bluetooth/mesh/health_faults.h>
```

电池电量低警告（Battery Low Warning）。

<a id="ga3da2c495908e3b4aac524e5d91c58189"></a>

### `BT_MESH_HEALTH_FAULT_CONDENSATION_ERROR`

```c
#define BT_MESH_HEALTH_FAULT_CONDENSATION_ERROR 0x10
```

```c
#include <zephyr/bluetooth/mesh/health_faults.h>
```

凝露错误（Condensation Error）。

<a id="ga95fd40c6066a37417ebfc9916b06db7c"></a>

### `BT_MESH_HEALTH_FAULT_CONDENSATION_WARNING`

```c
#define BT_MESH_HEALTH_FAULT_CONDENSATION_WARNING 0x0F
```

```c
#include <zephyr/bluetooth/mesh/health_faults.h>
```

凝露警告（Condensation Warning）。

<a id="ga03ee761cb0a2d5cbf3509a719e658621"></a>

### `BT_MESH_HEALTH_FAULT_CONFIGURATION_ERROR`

```c
#define BT_MESH_HEALTH_FAULT_CONFIGURATION_ERROR 0x14
```

```c
#include <zephyr/bluetooth/mesh/health_faults.h>
```

配置错误（Configuration Error）。

<a id="ga4e46ae0ebd52722c1600f2025a2fb190"></a>

### `BT_MESH_HEALTH_FAULT_CONFIGURATION_WARNING`

```c
#define BT_MESH_HEALTH_FAULT_CONFIGURATION_WARNING 0x13
```

```c
#include <zephyr/bluetooth/mesh/health_faults.h>
```

配置警告（Configuration Warning）。

<a id="ga2d0909640905067168ba45bea0523618"></a>

### `BT_MESH_HEALTH_FAULT_DEVICE_DROPPED_ERROR`

```c
#define BT_MESH_HEALTH_FAULT_DEVICE_DROPPED_ERROR 0x2A
```

```c
#include <zephyr/bluetooth/mesh/health_faults.h>
```

设备跌落错误（Device Dropped Error）。

<a id="ga7f158981cf1282acaca0839244e3c6cb"></a>

### `BT_MESH_HEALTH_FAULT_DEVICE_DROPPED_WARNING`

```c
#define BT_MESH_HEALTH_FAULT_DEVICE_DROPPED_WARNING 0x29
```

```c
#include <zephyr/bluetooth/mesh/health_faults.h>
```

设备跌落警告（Device Dropped Warning）。

<a id="ga482eb25cfcfd943342f8d30ed976bc24"></a>

### `BT_MESH_HEALTH_FAULT_DEVICE_MOVED_ERROR`

```c
#define BT_MESH_HEALTH_FAULT_DEVICE_MOVED_ERROR 0x28
```

```c
#include <zephyr/bluetooth/mesh/health_faults.h>
```

设备被移动错误（Device Moved Error）。

<a id="ga1494db7b9a0fbab15119a65da0b6b0d0"></a>

### `BT_MESH_HEALTH_FAULT_DEVICE_MOVED_WARNING`

```c
#define BT_MESH_HEALTH_FAULT_DEVICE_MOVED_WARNING 0x27
```

```c
#include <zephyr/bluetooth/mesh/health_faults.h>
```

设备被移动警告（Device Moved Warning）。

<a id="gaa612dbc60cc9ab0fe4978a0992499009"></a>

### `BT_MESH_HEALTH_FAULT_ELEMENT_NOT_CALIBRATED_ERROR`

```c
#define BT_MESH_HEALTH_FAULT_ELEMENT_NOT_CALIBRATED_ERROR 0x16
```

```c
#include <zephyr/bluetooth/mesh/health_faults.h>
```

元素未校准错误（Element Not Calibrated Error）。

<a id="ga0e50ab22bffb357f02acf4860664d535"></a>

### `BT_MESH_HEALTH_FAULT_ELEMENT_NOT_CALIBRATED_WARNING`

```c
#define BT_MESH_HEALTH_FAULT_ELEMENT_NOT_CALIBRATED_WARNING 0x15
```

```c
#include <zephyr/bluetooth/mesh/health_faults.h>
```

元素未校准警告（Element Not Calibrated Warning）。

<a id="ga0b0414621784d1a3c872077e0b578d0d"></a>

### `BT_MESH_HEALTH_FAULT_EMPTY_ERROR`

```c
#define BT_MESH_HEALTH_FAULT_EMPTY_ERROR 0x2E
```

```c
#include <zephyr/bluetooth/mesh/health_faults.h>
```

空状态错误（Empty Error）。

<a id="gada2400efbf70229ce8328a9ace7fcccf"></a>

### `BT_MESH_HEALTH_FAULT_EMPTY_WARNING`

```c
#define BT_MESH_HEALTH_FAULT_EMPTY_WARNING 0x2D
```

```c
#include <zephyr/bluetooth/mesh/health_faults.h>
```

空状态警告（Empty Warning）。

<a id="ga7308395342cc226ef17584aebfa78d2c"></a>

### `BT_MESH_HEALTH_FAULT_HOUSING_OPENED_ERROR`

```c
#define BT_MESH_HEALTH_FAULT_HOUSING_OPENED_ERROR 0x24
```

```c
#include <zephyr/bluetooth/mesh/health_faults.h>
```

外壳打开错误（Housing Opened Error）。

<a id="ga03cfae918863f10dd5aaab6fd3a82b07"></a>

### `BT_MESH_HEALTH_FAULT_HOUSING_OPENED_WARNING`

```c
#define BT_MESH_HEALTH_FAULT_HOUSING_OPENED_WARNING 0x23
```

```c
#include <zephyr/bluetooth/mesh/health_faults.h>
```

外壳打开警告（Housing Opened Warning）。

<a id="ga3789605186fe9c172d3320a22a21ead6"></a>

### `BT_MESH_HEALTH_FAULT_INPUT_NO_CHANGE_ERROR`

```c
#define BT_MESH_HEALTH_FAULT_INPUT_NO_CHANGE_ERROR 0x20
```

```c
#include <zephyr/bluetooth/mesh/health_faults.h>
```

输入无变化错误（Input No Change Error）。

<a id="ga5a1ba1561e93574e0d4598bd90c386b8"></a>

### `BT_MESH_HEALTH_FAULT_INPUT_NO_CHANGE_WARNING`

```c
#define BT_MESH_HEALTH_FAULT_INPUT_NO_CHANGE_WARNING 0x1F
```

```c
#include <zephyr/bluetooth/mesh/health_faults.h>
```

输入无变化警告（Input No Change Warning）。

<a id="gad42b0f690836deae1dcbb4757e885c02"></a>

### `BT_MESH_HEALTH_FAULT_INPUT_TOO_HIGH_ERROR`

```c
#define BT_MESH_HEALTH_FAULT_INPUT_TOO_HIGH_ERROR 0x1E
```

```c
#include <zephyr/bluetooth/mesh/health_faults.h>
```

输入过高错误（Input Too High Error）。

<a id="gae3c188075202eeff7292ab56e03e31a9"></a>

### `BT_MESH_HEALTH_FAULT_INPUT_TOO_HIGH_WARNING`

```c
#define BT_MESH_HEALTH_FAULT_INPUT_TOO_HIGH_WARNING 0x1D
```

```c
#include <zephyr/bluetooth/mesh/health_faults.h>
```

输入过高警告（Input Too High Warning）。

<a id="ga33c5b4f773c6afe73f64a14411033b3f"></a>

### `BT_MESH_HEALTH_FAULT_INPUT_TOO_LOW_ERROR`

```c
#define BT_MESH_HEALTH_FAULT_INPUT_TOO_LOW_ERROR 0x1C
```

```c
#include <zephyr/bluetooth/mesh/health_faults.h>
```

输入过低错误（Input Too Low Error）。

<a id="ga124bb981c3ab2c41eda2ddf3bc85b5f2"></a>

### `BT_MESH_HEALTH_FAULT_INPUT_TOO_LOW_WARNING`

```c
#define BT_MESH_HEALTH_FAULT_INPUT_TOO_LOW_WARNING 0x1B
```

```c
#include <zephyr/bluetooth/mesh/health_faults.h>
```

输入过低警告（Input Too Low Warning）。

<a id="ga54b4657666c01dca9417d58e302ff738"></a>

### `BT_MESH_HEALTH_FAULT_INTERNAL_BUS_ERROR`

```c
#define BT_MESH_HEALTH_FAULT_INTERNAL_BUS_ERROR 0x30
```

```c
#include <zephyr/bluetooth/mesh/health_faults.h>
```

内部总线错误（Internal Bus Error）。

<a id="ga534b85b4f805b585c4c4d29e6abe782a"></a>

### `BT_MESH_HEALTH_FAULT_INTERNAL_BUS_WARNING`

```c
#define BT_MESH_HEALTH_FAULT_INTERNAL_BUS_WARNING 0x2F
```

```c
#include <zephyr/bluetooth/mesh/health_faults.h>
```

内部总线警告（Internal Bus Warning）。

<a id="gaa6ccb4569d63b6eb0dc53ec7211f2f98"></a>

### `BT_MESH_HEALTH_FAULT_MECHANISM_JAMMED_ERROR`

```c
#define BT_MESH_HEALTH_FAULT_MECHANISM_JAMMED_ERROR 0x32
```

```c
#include <zephyr/bluetooth/mesh/health_faults.h>
```

机械机构卡住错误（Mechanism Jammed Error）。

<a id="gae1113f6fcaae95b1a7cfe2dd95c287ab"></a>

### `BT_MESH_HEALTH_FAULT_MECHANISM_JAMMED_WARNING`

```c
#define BT_MESH_HEALTH_FAULT_MECHANISM_JAMMED_WARNING 0x31
```

```c
#include <zephyr/bluetooth/mesh/health_faults.h>
```

机械机构卡住警告（Mechanism Jammed Warning）。

<a id="ga358d3351b1935b3a4c259060902033db"></a>

### `BT_MESH_HEALTH_FAULT_MEMORY_ERROR`

```c
#define BT_MESH_HEALTH_FAULT_MEMORY_ERROR 0x18
```

```c
#include <zephyr/bluetooth/mesh/health_faults.h>
```

内存错误（Memory Error）。

<a id="gabf766439091f937438a0e736ddc892b4"></a>

### `BT_MESH_HEALTH_FAULT_MEMORY_WARNING`

```c
#define BT_MESH_HEALTH_FAULT_MEMORY_WARNING 0x17
```

```c
#include <zephyr/bluetooth/mesh/health_faults.h>
```

内存警告（Memory Warning）。

<a id="ga5fe6993bb219f6547b67e6720f7bf526"></a>

### `BT_MESH_HEALTH_FAULT_NO_FAULT`

```c
#define BT_MESH_HEALTH_FAULT_NO_FAULT 0x00
```

```c
#include <zephyr/bluetooth/mesh/health_faults.h>
```

未发生故障（No Fault）。

<a id="ga29b5e94269715a8301bc363cb66db370"></a>

### `BT_MESH_HEALTH_FAULT_NO_LOAD_ERROR`

```c
#define BT_MESH_HEALTH_FAULT_NO_LOAD_ERROR 0x0A
```

```c
#include <zephyr/bluetooth/mesh/health_faults.h>
```

无负载错误（No Load Error）。

<a id="gab92ab13dbc9799476e6e627a81080e14"></a>

### `BT_MESH_HEALTH_FAULT_NO_LOAD_WARNING`

```c
#define BT_MESH_HEALTH_FAULT_NO_LOAD_WARNING 0x09
```

```c
#include <zephyr/bluetooth/mesh/health_faults.h>
```

无负载警告（No Load Warning）。

<a id="ga63b9b85427e0efa31e8a1496065b3dc9"></a>

### `BT_MESH_HEALTH_FAULT_OVERFLOW_ERROR`

```c
#define BT_MESH_HEALTH_FAULT_OVERFLOW_ERROR 0x2C
```

```c
#include <zephyr/bluetooth/mesh/health_faults.h>
```

溢出错误（Overflow Error）。

<a id="ga95d30649750b543650c3a21cc8719c3e"></a>

### `BT_MESH_HEALTH_FAULT_OVERFLOW_WARNING`

```c
#define BT_MESH_HEALTH_FAULT_OVERFLOW_WARNING 0x2B
```

```c
#include <zephyr/bluetooth/mesh/health_faults.h>
```

溢出警告（Overflow Warning）。

<a id="ga1c47ccb73f94cee4db7d300679972300"></a>

### `BT_MESH_HEALTH_FAULT_OVERHEAT_ERROR`

```c
#define BT_MESH_HEALTH_FAULT_OVERHEAT_ERROR 0x0E
```

```c
#include <zephyr/bluetooth/mesh/health_faults.h>
```

过热错误（Overheat Error）。

<a id="gac737fc53f2184bd1664f0da5388148ac"></a>

### `BT_MESH_HEALTH_FAULT_OVERHEAT_WARNING`

```c
#define BT_MESH_HEALTH_FAULT_OVERHEAT_WARNING 0x0D
```

```c
#include <zephyr/bluetooth/mesh/health_faults.h>
```

过热警告（Overheat Warning）。

<a id="gafafa715a04011e80944199d93ee6c51b"></a>

### `BT_MESH_HEALTH_FAULT_OVERLOAD_ERROR`

```c
#define BT_MESH_HEALTH_FAULT_OVERLOAD_ERROR 0x0C
```

```c
#include <zephyr/bluetooth/mesh/health_faults.h>
```

过载错误（Overload Error）。

<a id="gacd14cc12794077cc517d5fefa748c9c6"></a>

### `BT_MESH_HEALTH_FAULT_OVERLOAD_WARNING`

```c
#define BT_MESH_HEALTH_FAULT_OVERLOAD_WARNING 0x0B
```

```c
#include <zephyr/bluetooth/mesh/health_faults.h>
```

过载警告（Overload Warning）。

<a id="gaf1fff982760290c80424b87a60bff822"></a>

### `BT_MESH_HEALTH_FAULT_POWER_SUPPLY_INTERRUPTED_ERROR`

```c
#define BT_MESH_HEALTH_FAULT_POWER_SUPPLY_INTERRUPTED_ERROR 0x08
```

```c
#include <zephyr/bluetooth/mesh/health_faults.h>
```

供电中断错误（Power Supply Interrupted Error）。

<a id="ga326ce2242e409c9577d324388509b7b7"></a>

### `BT_MESH_HEALTH_FAULT_POWER_SUPPLY_INTERRUPTED_WARNING`

```c
#define BT_MESH_HEALTH_FAULT_POWER_SUPPLY_INTERRUPTED_WARNING 0x07
```

```c
#include <zephyr/bluetooth/mesh/health_faults.h>
```

供电中断警告（Power Supply Interrupted Warning）。

<a id="ga75214891137e1045bcc83c4c54458e77"></a>

### `BT_MESH_HEALTH_FAULT_SELF_TEST_ERROR`

```c
#define BT_MESH_HEALTH_FAULT_SELF_TEST_ERROR 0x1A
```

```c
#include <zephyr/bluetooth/mesh/health_faults.h>
```

自测试错误（Self-Test Error）。

<a id="ga8d60f38c1560c269fdfd18de35daf5d6"></a>

### `BT_MESH_HEALTH_FAULT_SELF_TEST_WARNING`

```c
#define BT_MESH_HEALTH_FAULT_SELF_TEST_WARNING 0x19
```

```c
#include <zephyr/bluetooth/mesh/health_faults.h>
```

自测试警告（Self-Test Warning）。

<a id="ga86d34960a167c0c3f8a1f320d1843702"></a>

### `BT_MESH_HEALTH_FAULT_SUPPLY_VOLTAGE_TOO_HIGH_ERROR`

```c
#define BT_MESH_HEALTH_FAULT_SUPPLY_VOLTAGE_TOO_HIGH_ERROR 0x06
```

```c
#include <zephyr/bluetooth/mesh/health_faults.h>
```

供电电压过高错误（Supply Voltage Too High Error）。

<a id="ga7838991d14a19ef401a41d96bec76287"></a>

### `BT_MESH_HEALTH_FAULT_SUPPLY_VOLTAGE_TOO_HIGH_WARNING`

```c
#define BT_MESH_HEALTH_FAULT_SUPPLY_VOLTAGE_TOO_HIGH_WARNING 0x05
```

```c
#include <zephyr/bluetooth/mesh/health_faults.h>
```

供电电压过高警告（Supply Voltage Too High Warning）。

<a id="gab64bbf32cda9d9cd8e82a05f7c9924a1"></a>

### `BT_MESH_HEALTH_FAULT_SUPPLY_VOLTAGE_TOO_LOW_ERROR`

```c
#define BT_MESH_HEALTH_FAULT_SUPPLY_VOLTAGE_TOO_LOW_ERROR 0x04
```

```c
#include <zephyr/bluetooth/mesh/health_faults.h>
```

供电电压过低错误（Supply Voltage Too Low Error）。

<a id="ga0a77dbd3aa3bddeab0cbcf434d36f791"></a>

### `BT_MESH_HEALTH_FAULT_SUPPLY_VOLTAGE_TOO_LOW_WARNING`

```c
#define BT_MESH_HEALTH_FAULT_SUPPLY_VOLTAGE_TOO_LOW_WARNING 0x03
```

```c
#include <zephyr/bluetooth/mesh/health_faults.h>
```

供电电压过低警告（Supply Voltage Too Low Warning）。

<a id="ga69b7755dd511f30864272ad1465f2965"></a>

### `BT_MESH_HEALTH_FAULT_TAMPER_ERROR`

```c
#define BT_MESH_HEALTH_FAULT_TAMPER_ERROR 0x26
```

```c
#include <zephyr/bluetooth/mesh/health_faults.h>
```

篡改错误（Tamper Error）。

<a id="ga66d4e92380a42b0491848a261a36246b"></a>

### `BT_MESH_HEALTH_FAULT_TAMPER_WARNING`

```c
#define BT_MESH_HEALTH_FAULT_TAMPER_WARNING 0x25
```

```c
#include <zephyr/bluetooth/mesh/health_faults.h>
```

篡改警告（Tamper Warning）。

<a id="gae0b8ecef9c11e17a02ede6a4b416c3b8"></a>

### `BT_MESH_HEALTH_FAULT_VENDOR_SPECIFIC_START`

```c
#define BT_MESH_HEALTH_FAULT_VENDOR_SPECIFIC_START 0x80
```

```c
#include <zephyr/bluetooth/mesh/health_faults.h>
```

厂商特定故障值（Vendor-specific Fault Values）的起始值。

低于此值的所有取值均保留供蓝牙规范（Bluetooth Specification）使用。

<a id="ga1b9f51d2760530bc170a81ff29435cf3"></a>

### `BT_MESH_HEALTH_FAULT_VIBRATION_ERROR`

```c
#define BT_MESH_HEALTH_FAULT_VIBRATION_ERROR 0x12
```

```c
#include <zephyr/bluetooth/mesh/health_faults.h>
```

振动错误（Vibration Error）。

<a id="ga7fb07118fea783803bfa8f419441740f"></a>

### `BT_MESH_HEALTH_FAULT_VIBRATION_WARNING`

```c
#define BT_MESH_HEALTH_FAULT_VIBRATION_WARNING 0x11
```

```c
#include <zephyr/bluetooth/mesh/health_faults.h>
```

振动警告（Vibration Warning）。


## 6.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/health_faults.h](../api_file_usb_network_reference/P010_zephyr__bluetooth__mesh__health_faults.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P005_运行时配置（Runtime Configuration）.md) · [返回大纲](大纲.md) · [下一章](P007_瑞萨 RA 时钟分频生成器（Clock Divider Generators）.md)
