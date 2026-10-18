---
id: learning.zephyr-docs.api-fota-storage-topic-reference.page-1
title: 电池服务（Battery Service，BAS）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_电池服务（Battery Service，BAS）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

电池服务（Battery Service，BAS）

<a id="details"></a>

电池服务（Battery Service，BAS）。[实验性（Experimental）] 用户应注意，API 可能随持续开发而变更。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 1.1\_枚举（Enumerations）

<a id="r_ga56d26a8cde072959e8d8b75ee4fb2819"></a>

```c
enum bt_bas_bcs_flags { BT_BAS_BCS_BATTERY_CRITICAL_STATE = BIT(0) , BT_BAS_BCS_IMMEDIATE_SERVICE_REQUIRED = BIT(1) }
```

相关声明：[bt_bas_bcs_flags](#ga56d26a8cde072959e8d8b75ee4fb2819)、[BT_BAS_BCS_BATTERY_CRITICAL_STATE](#gga56d26a8cde072959e8d8b75ee4fb2819ad45c2b537f66cc7118357616120fa8a5)、[BT_BAS_BCS_IMMEDIATE_SERVICE_REQUIRED](#gga56d26a8cde072959e8d8b75ee4fb2819af82ae1d0e53efa882ff21d4e67b9ba7a)。

电池临界状态特征（Battery Critical Status Characteristic）的标志。

<a id="r_ga7c425f7fd9e908e327810f89d7645745"></a>

```c
enum bt_bas_bls_flags { BT_BAS_BLS_FLAG_IDENTIFIER_PRESENT = BIT(0) , BT_BAS_BLS_FLAG_BATTERY_LEVEL_PRESENT = BIT(1) , BT_BAS_BLS_FLAG_ADDITIONAL_STATUS_PRESENT = BIT(2) }
```

相关声明：[bt_bas_bls_flags](#ga7c425f7fd9e908e327810f89d7645745)、[BT_BAS_BLS_FLAG_IDENTIFIER_PRESENT](#gga7c425f7fd9e908e327810f89d7645745a69d60021c1d1772f461f0e90eadd9b46)、[BT_BAS_BLS_FLAG_BATTERY_LEVEL_PRESENT](#gga7c425f7fd9e908e327810f89d7645745a74cb90028ebf42119c8c69a3801591ba)、[BT_BAS_BLS_FLAG_ADDITIONAL_STATUS_PRESENT](#gga7c425f7fd9e908e327810f89d7645745add93cefc8c583aa0edd71ed66edbea3d)。

电池电量状态特征（Battery Level Status Characteristic）的标志。

<a id="r_ga31d5d4a7184243ffe9d925714de4367f"></a>

```c
enum bt_bas_bls_battery_present { BT_BAS_BLS_BATTERY_NOT_PRESENT = 0 , BT_BAS_BLS_BATTERY_PRESENT = 1 }
```

相关声明：[bt_bas_bls_battery_present](#ga31d5d4a7184243ffe9d925714de4367f)、[BT_BAS_BLS_BATTERY_NOT_PRESENT](#gga31d5d4a7184243ffe9d925714de4367fae373a1d0f3875bafbdcab7c1cca0f522)、[BT_BAS_BLS_BATTERY_PRESENT](#gga31d5d4a7184243ffe9d925714de4367fa63b460de845ef9cb7423c82008b2ed49)。

电池在位状态（Battery Present Status）。

<a id="r_ga4e3f58a5f7c8715f3f8f24b96229b71c"></a>

```c
enum bt_bas_bls_wired_power_source { BT_BAS_BLS_WIRED_POWER_NOT_CONNECTED = 0 , BT_BAS_BLS_WIRED_POWER_CONNECTED = 1 , BT_BAS_BLS_WIRED_POWER_UNKNOWN = 2 }
```

相关声明：[bt_bas_bls_wired_power_source](#ga4e3f58a5f7c8715f3f8f24b96229b71c)、[BT_BAS_BLS_WIRED_POWER_NOT_CONNECTED](#gga4e3f58a5f7c8715f3f8f24b96229b71ca98d72b37dce3b29dcc901bb58d3e6acf)、[BT_BAS_BLS_WIRED_POWER_CONNECTED](#gga4e3f58a5f7c8715f3f8f24b96229b71cadabb6df4477b9483e18cd3bd77ef8adc)、[BT_BAS_BLS_WIRED_POWER_UNKNOWN](#gga4e3f58a5f7c8715f3f8f24b96229b71ca2064d10fa9b52c40142eb4f8a9ef2799)。

有线外部电源状态（Wired External Power Source Status）。

<a id="r_gaf76a1eea78e9ff5c35977c41b00fb64d"></a>

```c
enum bt_bas_bls_wireless_power_source { BT_BAS_BLS_WIRELESS_POWER_NOT_CONNECTED = 0 , BT_BAS_BLS_WIRELESS_POWER_CONNECTED = 1 , BT_BAS_BLS_WIRELESS_POWER_UNKNOWN = 2 }
```

相关声明：[bt_bas_bls_wireless_power_source](#gaf76a1eea78e9ff5c35977c41b00fb64d)、[BT_BAS_BLS_WIRELESS_POWER_NOT_CONNECTED](#ggaf76a1eea78e9ff5c35977c41b00fb64dab90caed6b5b1fef37f79176ae6221383)、[BT_BAS_BLS_WIRELESS_POWER_CONNECTED](#ggaf76a1eea78e9ff5c35977c41b00fb64da3f2f11b307bb6e641792e4e85fe3a363)、[BT_BAS_BLS_WIRELESS_POWER_UNKNOWN](#ggaf76a1eea78e9ff5c35977c41b00fb64daafeab5f57d1a12770bc9ac95161e1af8)。

无线外部电源状态（Wireless External Power Source Status）。

<a id="r_ga3584a3e7b7194bf244f414d6860b1313"></a>

```c
enum bt_bas_bls_battery_charge_state { BT_BAS_BLS_CHARGE_STATE_UNKNOWN = 0 , BT_BAS_BLS_CHARGE_STATE_CHARGING = 1 , BT_BAS_BLS_CHARGE_STATE_DISCHARGING_ACTIVE = 2 , BT_BAS_BLS_CHARGE_STATE_DISCHARGING_INACTIVE = 3 }
```

相关声明：[bt_bas_bls_battery_charge_state](#ga3584a3e7b7194bf244f414d6860b1313)、[BT_BAS_BLS_CHARGE_STATE_UNKNOWN](#gga3584a3e7b7194bf244f414d6860b1313a663b3a9a4490600c56f2784246bbe58c)、[BT_BAS_BLS_CHARGE_STATE_CHARGING](#gga3584a3e7b7194bf244f414d6860b1313a35249a218c5c15a24e9b529991282ab9)、[BT_BAS_BLS_CHARGE_STATE_DISCHARGING_ACTIVE](#gga3584a3e7b7194bf244f414d6860b1313aba3c8d0d791dae18b6aa3149619e4e02)、[BT_BAS_BLS_CHARGE_STATE_DISCHARGING_INACTIVE](#gga3584a3e7b7194bf244f414d6860b1313a23a496ecd4b7e7d33ee7a2f0021c4f1a)。

电池充电状态（Battery Charge State）。

<a id="r_gad374826ce9465bbf344b1f25b16c574c"></a>

```c
enum bt_bas_bls_battery_charge_level { BT_BAS_BLS_CHARGE_LEVEL_UNKNOWN = 0 , BT_BAS_BLS_CHARGE_LEVEL_GOOD = 1 , BT_BAS_BLS_CHARGE_LEVEL_LOW = 2 , BT_BAS_BLS_CHARGE_LEVEL_CRITICAL = 3 }
```

相关声明：[bt_bas_bls_battery_charge_level](#gad374826ce9465bbf344b1f25b16c574c)、[BT_BAS_BLS_CHARGE_LEVEL_UNKNOWN](#ggad374826ce9465bbf344b1f25b16c574cabdd600d10005a09cbce4f5584cb3bb58)、[BT_BAS_BLS_CHARGE_LEVEL_GOOD](#ggad374826ce9465bbf344b1f25b16c574cae08b7620b5babb731a6c8e8bf12b1387)、[BT_BAS_BLS_CHARGE_LEVEL_LOW](#ggad374826ce9465bbf344b1f25b16c574ca27d8f485ee4ee50bb8d9c02049b9679e)、[BT_BAS_BLS_CHARGE_LEVEL_CRITICAL](#ggad374826ce9465bbf344b1f25b16c574ca46fa5393ea4acefae2d2ffdfaef2a31d)。

电池充电水平（Battery Charge Level）。

<a id="r_ga9f09b045f9db8aa2f2e21adb0a65c3aa"></a>

```c
enum bt_bas_bls_battery_charge_type { BT_BAS_BLS_CHARGE_TYPE_UNKNOWN = 0 , BT_BAS_BLS_CHARGE_TYPE_CONSTANT_CURRENT = 1 , BT_BAS_BLS_CHARGE_TYPE_CONSTANT_VOLTAGE = 2 , BT_BAS_BLS_CHARGE_TYPE_TRICKLE = 3 , BT_BAS_BLS_CHARGE_TYPE_FLOAT = 4 }
```

相关声明：[bt_bas_bls_battery_charge_type](#ga9f09b045f9db8aa2f2e21adb0a65c3aa)、[BT_BAS_BLS_CHARGE_TYPE_UNKNOWN](#gga9f09b045f9db8aa2f2e21adb0a65c3aaa0c681a700639a1ba8b3cf3e5afc70e64)、[BT_BAS_BLS_CHARGE_TYPE_CONSTANT_CURRENT](#gga9f09b045f9db8aa2f2e21adb0a65c3aaa5a9f93290d6b11596771e7e9bbc357af)、[BT_BAS_BLS_CHARGE_TYPE_CONSTANT_VOLTAGE](#gga9f09b045f9db8aa2f2e21adb0a65c3aaa5dc3c38414be857fd5d2cf98a0edc730)、[BT_BAS_BLS_CHARGE_TYPE_TRICKLE](#gga9f09b045f9db8aa2f2e21adb0a65c3aaade1f3bc7dab9c768feb8d70c149ffbda)、[BT_BAS_BLS_CHARGE_TYPE_FLOAT](#gga9f09b045f9db8aa2f2e21adb0a65c3aaabbf719d116ec24bbf327c8e7a2eb50c0)。

电池充电类型（Battery Charge Type）。

<a id="r_gad981cab4d2a285ee72481b54836cf35b"></a>

```c
enum bt_bas_bls_charging_fault_reason { BT_BAS_BLS_FAULT_REASON_NONE = 0 , BT_BAS_BLS_FAULT_REASON_BATTERY = BIT(0) , BT_BAS_BLS_FAULT_REASON_EXTERNAL_POWER = BIT(1) , BT_BAS_BLS_FAULT_REASON_OTHER = BIT(2) }
```

相关声明：[bt_bas_bls_charging_fault_reason](#gad981cab4d2a285ee72481b54836cf35b)、[BT_BAS_BLS_FAULT_REASON_NONE](#ggad981cab4d2a285ee72481b54836cf35bab8d7bcea2ab1d76a66727e11a520654a)、[BT_BAS_BLS_FAULT_REASON_BATTERY](#ggad981cab4d2a285ee72481b54836cf35ba7bea7165cbba98284b9941cf8809787f)、[BT_BAS_BLS_FAULT_REASON_EXTERNAL_POWER](#ggad981cab4d2a285ee72481b54836cf35ba527c9490662f70b789ecb0d37f90df3b)、[BT_BAS_BLS_FAULT_REASON_OTHER](#ggad981cab4d2a285ee72481b54836cf35ba8c70a47828ed3b90c08e742dff3c0ab7)。

充电故障原因（Charging Fault Reason）。

<a id="r_gad410bdd972f09f0314b696ce31e6d82d"></a>

```c
enum bt_bas_bls_service_required { BT_BAS_BLS_SERVICE_REQUIRED_FALSE = 0 , BT_BAS_BLS_SERVICE_REQUIRED_TRUE = 1 , BT_BAS_BLS_SERVICE_REQUIRED_UNKNOWN = 2 }
```

相关声明：[bt_bas_bls_service_required](#gad410bdd972f09f0314b696ce31e6d82d)、[BT_BAS_BLS_SERVICE_REQUIRED_FALSE](#ggad410bdd972f09f0314b696ce31e6d82daa50e305c82d8081877576953e07241db)、[BT_BAS_BLS_SERVICE_REQUIRED_TRUE](#ggad410bdd972f09f0314b696ce31e6d82da683bc2d562e99ae0c691eb3611206f00)、[BT_BAS_BLS_SERVICE_REQUIRED_UNKNOWN](#ggad410bdd972f09f0314b696ce31e6d82dae36621eac964d7f2b8b5959de11ba870)。

需要维护状态（Service Required Status）。

<a id="r_ga6976a11ffe2c9a9b2fff82763be2edee"></a>

```c
enum bt_bas_bls_battery_fault { BT_BAS_BLS_BATTERY_FAULT_NO = 0 , BT_BAS_BLS_BATTERY_FAULT_YES = 1 }
```

相关声明：[bt_bas_bls_battery_fault](#ga6976a11ffe2c9a9b2fff82763be2edee)、[BT_BAS_BLS_BATTERY_FAULT_NO](#gga6976a11ffe2c9a9b2fff82763be2edeeab119e2a0a3600269f752dfc7f271edee)、[BT_BAS_BLS_BATTERY_FAULT_YES](#gga6976a11ffe2c9a9b2fff82763be2edeea6af59b287c252dbb04d6ab6cdbbf6d6f)。

电池故障状态（Battery Fault Status）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.2\_函数（Functions）

<a id="r_gadbe0f52d04d90372d603af66b693e980"></a>

```c
uint8_t bt_bas_get_battery_level (void)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_bas_get_battery_level](#gadbe0f52d04d90372d603af66b693e980)。

读取电池电量值（Battery Level）。

<a id="r_gac8d519830c34b9c8370366e2593dbeba"></a>

```c
int bt_bas_set_battery_level (uint8_t level)
```

相关声明：[bt_bas_set_battery_level](#gac8d519830c34b9c8370366e2593dbeba)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

更新电池电量值（Battery Level）。

<a id="r_ga5e0325af9dcd362dd3c1691832be5677"></a>

```c
void bt_bas_bls_set_battery_present (enum bt_bas_bls_battery_present present)
```

相关声明：[bt_bas_bls_set_battery_present](#ga5e0325af9dcd362dd3c1691832be5677)、[bt_bas_bls_battery_present](#ga31d5d4a7184243ffe9d925714de4367f)。

设置电池在位状态（Battery Present Status）。

<a id="r_ga7bf36a53494e2ecfbb5ccd218f29f51f"></a>

```c
void bt_bas_bls_set_wired_external_power_source (enum bt_bas_bls_wired_power_source source)
```

相关声明：[bt_bas_bls_set_wired_external_power_source](#ga7bf36a53494e2ecfbb5ccd218f29f51f)、[bt_bas_bls_wired_power_source](#ga4e3f58a5f7c8715f3f8f24b96229b71c)。

设置有线外部电源状态（Wired External Power Source Status）。

<a id="r_gae1cbafd30e1d78437c78d44df25aa005"></a>

```c
void bt_bas_bls_set_wireless_external_power_source (enum bt_bas_bls_wireless_power_source source)
```

相关声明：[bt_bas_bls_set_wireless_external_power_source](#gae1cbafd30e1d78437c78d44df25aa005)、[bt_bas_bls_wireless_power_source](#gaf76a1eea78e9ff5c35977c41b00fb64d)。

设置无线外部电源状态（Wireless External Power Source Status）。

<a id="r_ga60b153c4d291ed4b16ce1f9d2dc1b45d"></a>

```c
void bt_bas_bls_set_battery_charge_state (enum bt_bas_bls_battery_charge_state state)
```

相关声明：[bt_bas_bls_set_battery_charge_state](#ga60b153c4d291ed4b16ce1f9d2dc1b45d)、[bt_bas_bls_battery_charge_state](#ga3584a3e7b7194bf244f414d6860b1313)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

设置电池充电状态（Battery Charge State）。

<a id="r_gac8e32530f966c7699d3c28e6685bcee5"></a>

```c
void bt_bas_bls_set_battery_charge_level (enum bt_bas_bls_battery_charge_level level)
```

相关声明：[bt_bas_bls_set_battery_charge_level](#gac8e32530f966c7699d3c28e6685bcee5)、[bt_bas_bls_battery_charge_level](#gad374826ce9465bbf344b1f25b16c574c)。

设置电池充电水平（Battery Charge Level）。

<a id="r_ga3cea34f717f2df01b6f49bed80f27f44"></a>

```c
void bt_bas_bls_set_battery_charge_type (enum bt_bas_bls_battery_charge_type type)
```

相关声明：[bt_bas_bls_set_battery_charge_type](#ga3cea34f717f2df01b6f49bed80f27f44)、[bt_bas_bls_battery_charge_type](#ga9f09b045f9db8aa2f2e21adb0a65c3aa)。

设置电池充电类型（Battery Charge Type）。

<a id="r_ga7996edb35bcca878062360b24036b6f8"></a>

```c
void bt_bas_bls_set_charging_fault_reason (enum bt_bas_bls_charging_fault_reason reason)
```

相关声明：[bt_bas_bls_set_charging_fault_reason](#ga7996edb35bcca878062360b24036b6f8)、[bt_bas_bls_charging_fault_reason](#gad981cab4d2a285ee72481b54836cf35b)。

设置充电故障原因（Charging Fault Reason）。

<a id="r_gafd74ef933734960a64f1ee1e80e9e335"></a>

```c
void bt_bas_bls_set_identifier (uint16_t identifier)
```

相关声明：[bt_bas_bls_set_identifier](#gafd74ef933734960a64f1ee1e80e9e335)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置电池标识符（Identifier）。

<a id="r_gaa94f308b6e135a3957191499778275ec"></a>

```c
void bt_bas_bls_set_service_required (enum bt_bas_bls_service_required value)
```

相关声明：[bt_bas_bls_set_service_required](#gaa94f308b6e135a3957191499778275ec)、[bt_bas_bls_service_required](#gad410bdd972f09f0314b696ce31e6d82d)。

设置需要维护状态（Service Required Status）。

<a id="r_ga9c50ed6a493adee208a59b17c48702f8"></a>

```c
void bt_bas_bls_set_battery_fault (enum bt_bas_bls_battery_fault value)
```

相关声明：[bt_bas_bls_set_battery_fault](#ga9c50ed6a493adee208a59b17c48702f8)、[bt_bas_bls_battery_fault](#ga6976a11ffe2c9a9b2fff82763be2edee)。

设置电池故障状态（Battery Fault Status）。

## 1.3\_详细说明（Detailed Documentation）

<a id="ga56d26a8cde072959e8d8b75ee4fb2819"></a>

### `bt_bas_bcs_flags`

```c
enum bt_bas_bcs_flags
```

```c
#include <zephyr/bluetooth/services/bas.h>
```

电池临界状态特征（Battery Critical Status Characteristic）的标志。

标识电池严重状态特征（Battery Critical Status Characteristic）中各字段是否存在的标志枚举。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_BAS_BCS_BATTERY_CRITICAL_STATE` | 电池严重状态（Battery Critical Status）位 0：严重电源状态（Critical Power State）。 |
| `BT_BAS_BCS_IMMEDIATE_SERVICE_REQUIRED` | 电池严重状态（Battery Critical Status）位 1：需要立即维护（Immediate Service Required）。 |

<a id="gad374826ce9465bbf344b1f25b16c574c"></a>

### `bt_bas_bls_battery_charge_level`

```c
enum bt_bas_bls_battery_charge_level
```

```c
#include <zephyr/bluetooth/services/bas.h>
```

电池充电水平（Battery Charge Level）。

电池电量等级（Battery Charge Level）枚举。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_BAS_BLS_CHARGE_LEVEL_UNKNOWN` | 电池电量等级未知（Unknown）。 |
| `BT_BAS_BLS_CHARGE_LEVEL_GOOD` | 电池电量充足（Good）。 |
| `BT_BAS_BLS_CHARGE_LEVEL_LOW` | 电池电量低（Low）。 |
| `BT_BAS_BLS_CHARGE_LEVEL_CRITICAL` | 电池电量严重不足（Critical）。 |

<a id="ga3584a3e7b7194bf244f414d6860b1313"></a>

### `bt_bas_bls_battery_charge_state`

```c
enum bt_bas_bls_battery_charge_state
```

```c
#include <zephyr/bluetooth/services/bas.h>
```

电池充电状态（Battery Charge State）。

电池充放电状态（Battery Charge State）枚举。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_BAS_BLS_CHARGE_STATE_UNKNOWN` | 电池充放电状态未知（Unknown）。 |
| `BT_BAS_BLS_CHARGE_STATE_CHARGING` | 电池正在充电（Charging）。 |
| `BT_BAS_BLS_CHARGE_STATE_DISCHARGING_ACTIVE` | 电池正在主动放电（Discharging Actively）。 |
| `BT_BAS_BLS_CHARGE_STATE_DISCHARGING_INACTIVE` | 电池处于放电状态但未活动（Discharging but Inactive）。 |

<a id="ga9f09b045f9db8aa2f2e21adb0a65c3aa"></a>

### `bt_bas_bls_battery_charge_type`

```c
enum bt_bas_bls_battery_charge_type
```

```c
#include <zephyr/bluetooth/services/bas.h>
```

电池充电类型（Battery Charge Type）。

电池所用充电类型（Charge Type）枚举。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_BAS_BLS_CHARGE_TYPE_UNKNOWN` | 电池充电类型未知，或未在充电（Unknown or Not Charging）。 |
| `BT_BAS_BLS_CHARGE_TYPE_CONSTANT_CURRENT` | 电池采用恒流充电（Constant Current）。 |
| `BT_BAS_BLS_CHARGE_TYPE_CONSTANT_VOLTAGE` | 电池采用恒压充电（Constant Voltage）。 |
| `BT_BAS_BLS_CHARGE_TYPE_TRICKLE` | 电池采用涓流充电（Trickle Charge）。 |
| `BT_BAS_BLS_CHARGE_TYPE_FLOAT` | 电池采用浮充（Float Charge）。 |

<a id="ga6976a11ffe2c9a9b2fff82763be2edee"></a>

### `bt_bas_bls_battery_fault`

```c
enum bt_bas_bls_battery_fault
```

```c
#include <zephyr/bluetooth/services/bas.h>
```

电池故障状态（Battery Fault Status）。

电池故障状态（Battery Fault Status）枚举。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_BAS_BLS_BATTERY_FAULT_NO` | 电池无故障（No Battery Fault）。 |
| `BT_BAS_BLS_BATTERY_FAULT_YES` | 电池存在故障（Battery Fault Present）。 |

<a id="ga31d5d4a7184243ffe9d925714de4367f"></a>

### `bt_bas_bls_battery_present`

```c
enum bt_bas_bls_battery_present
```

```c
#include <zephyr/bluetooth/services/bas.h>
```

电池在位状态（Battery Present Status）。

电池在位状态（Battery Presence）枚举。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_BAS_BLS_BATTERY_NOT_PRESENT` | 电池不在位（Not Present）。 |
| `BT_BAS_BLS_BATTERY_PRESENT` | 电池在位（Present）。 |

<a id="gad981cab4d2a285ee72481b54836cf35b"></a>

### `bt_bas_bls_charging_fault_reason`

```c
enum bt_bas_bls_charging_fault_reason
```

```c
#include <zephyr/bluetooth/services/bas.h>
```

充电故障原因（Charging Fault Reason）。

充电故障原因（Charging Fault Reason）枚举。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_BAS_BLS_FAULT_REASON_NONE` | 无充电故障（No Charging Fault）。 |
| `BT_BAS_BLS_FAULT_REASON_BATTERY` | 由电池问题引起的充电故障（Battery Issue）。 |
| `BT_BAS_BLS_FAULT_REASON_EXTERNAL_POWER` | 由外部电源问题引起的充电故障（External Power Source Issue）。 |
| `BT_BAS_BLS_FAULT_REASON_OTHER` | 其他原因引起的充电故障（Other Reasons）。 |

<a id="ga7c425f7fd9e908e327810f89d7645745"></a>

### `bt_bas_bls_flags`

```c
enum bt_bas_bls_flags
```

```c
#include <zephyr/bluetooth/services/bas.h>
```

电池电量状态特征（Battery Level Status Characteristic）的标志。

标识电池电量状态特征（Battery Level Status Characteristic）中各字段是否存在的标志枚举。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_BAS_BLS_FLAG_IDENTIFIER_PRESENT` | 指示存在电池电量状态标识符（Battery Level Status Identifier）的位。 |
| `BT_BAS_BLS_FLAG_BATTERY_LEVEL_PRESENT` | 指示存在电池电量（Battery Level）的位。 |
| `BT_BAS_BLS_FLAG_ADDITIONAL_STATUS_PRESENT` | 指示存在附加状态信息（Additional Status Information）的位。 |

<a id="gad410bdd972f09f0314b696ce31e6d82d"></a>

### `bt_bas_bls_service_required`

```c
enum bt_bas_bls_service_required
```

```c
#include <zephyr/bluetooth/services/bas.h>
```

需要维护状态（Service Required Status）。

是否需要维护（Service Required）的枚举。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_BAS_BLS_SERVICE_REQUIRED_FALSE` | 无需维护（Service Not Required）。 |
| `BT_BAS_BLS_SERVICE_REQUIRED_TRUE` | 需要维护（Service Required）。 |
| `BT_BAS_BLS_SERVICE_REQUIRED_UNKNOWN` | 维护需求未知（Unknown）。 |

<a id="ga4e3f58a5f7c8715f3f8f24b96229b71c"></a>

### `bt_bas_bls_wired_power_source`

```c
enum bt_bas_bls_wired_power_source
```

```c
#include <zephyr/bluetooth/services/bas.h>
```

有线外部电源状态（Wired External Power Source Status）。

有线外部电源状态（Wired External Power Source Status）枚举。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_BAS_BLS_WIRED_POWER_NOT_CONNECTED` | 有线外部电源未连接（Not Connected）。 |
| `BT_BAS_BLS_WIRED_POWER_CONNECTED` | 有线外部电源已连接（Connected）。 |
| `BT_BAS_BLS_WIRED_POWER_UNKNOWN` | 有线外部电源状态未知（Unknown）。 |

<a id="gaf76a1eea78e9ff5c35977c41b00fb64d"></a>

### `bt_bas_bls_wireless_power_source`

```c
enum bt_bas_bls_wireless_power_source
```

```c
#include <zephyr/bluetooth/services/bas.h>
```

无线外部电源状态（Wireless External Power Source Status）。

无线外部电源状态（Wireless External Power Source Status）枚举。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_BAS_BLS_WIRELESS_POWER_NOT_CONNECTED` | 无线外部电源未连接（Not Connected）。 |
| `BT_BAS_BLS_WIRELESS_POWER_CONNECTED` | 无线外部电源已连接（Connected）。 |
| `BT_BAS_BLS_WIRELESS_POWER_UNKNOWN` | 无线外部电源状态未知（Unknown）。 |

<a id="gac8e32530f966c7699d3c28e6685bcee5"></a>

### `bt_bas_bls_set_battery_charge_level()`

```c
void bt_bas_bls_set_battery_charge_level ( enum bt_bas_bls_battery_charge_level level)
```

```c
#include <zephyr/bluetooth/services/bas.h>
```

设置电池充电水平（Battery Charge Level）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `level` | 要设置的电池电量等级（Battery Charge Level）。 |

<a id="ga60b153c4d291ed4b16ce1f9d2dc1b45d"></a>

### `bt_bas_bls_set_battery_charge_state()`

```c
void bt_bas_bls_set_battery_charge_state ( enum bt_bas_bls_battery_charge_state state)
```

```c
#include <zephyr/bluetooth/services/bas.h>
```

设置电池充电状态（Battery Charge State）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `state` | 要设置的电池充放电状态（Battery Charge State）。 |

<a id="ga3cea34f717f2df01b6f49bed80f27f44"></a>

### `bt_bas_bls_set_battery_charge_type()`

```c
void bt_bas_bls_set_battery_charge_type ( enum bt_bas_bls_battery_charge_type type)
```

```c
#include <zephyr/bluetooth/services/bas.h>
```

设置电池充电类型（Battery Charge Type）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `type` | 要设置的电池充电类型（Battery Charge Type）。 |

<a id="ga9c50ed6a493adee208a59b17c48702f8"></a>

### `bt_bas_bls_set_battery_fault()`

```c
void bt_bas_bls_set_battery_fault ( enum bt_bas_bls_battery_fault value)
```

```c
#include <zephyr/bluetooth/services/bas.h>
```

设置电池故障状态（Battery Fault Status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `value` | 要设置的电池故障状态（Battery Fault Status）。 |

**注意（Attention）**：注意（Attention）：仅在启用以下 Kconfig 选项时可用：`CONFIG_BT_BAS_BLS_ADDITIONAL_STATUS_PRESENT`。

<a id="ga5e0325af9dcd362dd3c1691832be5677"></a>

### `bt_bas_bls_set_battery_present()`

```c
void bt_bas_bls_set_battery_present ( enum bt_bas_bls_battery_present present)
```

```c
#include <zephyr/bluetooth/services/bas.h>
```

设置电池在位状态（Battery Present Status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `present` | 要设置的电池在位状态（Battery Present Status）。 |

<a id="ga7996edb35bcca878062360b24036b6f8"></a>

### `bt_bas_bls_set_charging_fault_reason()`

```c
void bt_bas_bls_set_charging_fault_reason ( enum bt_bas_bls_charging_fault_reason reason)
```

```c
#include <zephyr/bluetooth/services/bas.h>
```

设置充电故障原因（Charging Fault Reason）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `reason` | 要设置的充电故障原因（Charging Fault Reason）。 |

<a id="gafd74ef933734960a64f1ee1e80e9e335"></a>

### `bt_bas_bls_set_identifier()`

```c
void bt_bas_bls_set_identifier ( uint16_t identifier)
```

```c
#include <zephyr/bluetooth/services/bas.h>
```

设置电池标识符（Identifier）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `identifier` | 要设置的标识符（Identifier）。 |

**注意（Attention）**：注意（Attention）：仅在启用以下 Kconfig 选项时可用：`CONFIG_BT_BAS_BLS_IDENTIFIER_PRESENT`。

<a id="gaa94f308b6e135a3957191499778275ec"></a>

### `bt_bas_bls_set_service_required()`

```c
void bt_bas_bls_set_service_required ( enum bt_bas_bls_service_required value)
```

```c
#include <zephyr/bluetooth/services/bas.h>
```

设置需要维护状态（Service Required Status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `value` | 要设置的维护需求状态（Service Required Status）。 |

**注意（Attention）**：注意（Attention）：仅在启用以下 Kconfig 选项时可用：`CONFIG_BT_BAS_BLS_ADDITIONAL_STATUS_PRESENT`。

<a id="ga7bf36a53494e2ecfbb5ccd218f29f51f"></a>

### `bt_bas_bls_set_wired_external_power_source()`

```c
void bt_bas_bls_set_wired_external_power_source ( enum bt_bas_bls_wired_power_source source)
```

```c
#include <zephyr/bluetooth/services/bas.h>
```

设置有线外部电源状态（Wired External Power Source Status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `source` | 要设置的有线外部电源状态（Wired External Power Source Status）。 |

<a id="gae1cbafd30e1d78437c78d44df25aa005"></a>

### `bt_bas_bls_set_wireless_external_power_source()`

```c
void bt_bas_bls_set_wireless_external_power_source ( enum bt_bas_bls_wireless_power_source source)
```

```c
#include <zephyr/bluetooth/services/bas.h>
```

设置无线外部电源状态（Wireless External Power Source Status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `source` | 要设置的无线外部电源状态（Wireless External Power Source Status）。 |

<a id="gadbe0f52d04d90372d603af66b693e980"></a>

### `bt_bas_get_battery_level()`

```c
uint8_t bt_bas_get_battery_level ( void )
```

```c
#include <zephyr/bluetooth/services/bas.h>
```

读取电池电量值（Battery Level）。

读取电池电量（Battery Level）的特征值（Characteristic Value）。

**返回（Returns）**：返回值（Returns）：以百分比表示的电池电量。

<a id="gac8d519830c34b9c8370366e2593dbeba"></a>

### `bt_bas_set_battery_level()`

```c
int bt_bas_set_battery_level ( uint8_t level)
```

```c
#include <zephyr/bluetooth/services/bas.h>
```

更新电池电量值（Battery Level）。

更新电池电量（Battery Level）的特征值。这会向所有当前订阅者发送 GATT 通知（Notification）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `level` | 以百分比表示的电池电量（Battery Level）。 |

**返回（Returns）**：返回值：成功时返回 0，出错时返回错误码。


## 1.4\_原页交叉引用（Cross References）

- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [zephyr/bluetooth/services/bas.h](../api_file_battery_interrupt_reference/P004_zephyr__bluetooth__services__bas.h_文件参考.md)
- [CONFIG_BT_BAS_BLS_ADDITIONAL_STATUS_PRESENT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_BAS_BLS_ADDITIONAL_STATUS_PRESENT)
- [CONFIG_BT_BAS_BLS_IDENTIFIER_PRESENT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_BAS_BLS_IDENTIFIER_PRESENT)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga56d26a8cde072959e8d8b75ee4fb2819ad45c2b537f66cc7118357616120fa8a5"></a>
<a id="gga56d26a8cde072959e8d8b75ee4fb2819af82ae1d0e53efa882ff21d4e67b9ba7a"></a>
<a id="ggad374826ce9465bbf344b1f25b16c574cabdd600d10005a09cbce4f5584cb3bb58"></a>
<a id="ggad374826ce9465bbf344b1f25b16c574cae08b7620b5babb731a6c8e8bf12b1387"></a>
<a id="ggad374826ce9465bbf344b1f25b16c574ca27d8f485ee4ee50bb8d9c02049b9679e"></a>
<a id="ggad374826ce9465bbf344b1f25b16c574ca46fa5393ea4acefae2d2ffdfaef2a31d"></a>
<a id="gga3584a3e7b7194bf244f414d6860b1313a663b3a9a4490600c56f2784246bbe58c"></a>
<a id="gga3584a3e7b7194bf244f414d6860b1313a35249a218c5c15a24e9b529991282ab9"></a>
<a id="gga3584a3e7b7194bf244f414d6860b1313aba3c8d0d791dae18b6aa3149619e4e02"></a>
<a id="gga3584a3e7b7194bf244f414d6860b1313a23a496ecd4b7e7d33ee7a2f0021c4f1a"></a>
<a id="gga9f09b045f9db8aa2f2e21adb0a65c3aaa0c681a700639a1ba8b3cf3e5afc70e64"></a>
<a id="gga9f09b045f9db8aa2f2e21adb0a65c3aaa5a9f93290d6b11596771e7e9bbc357af"></a>
<a id="gga9f09b045f9db8aa2f2e21adb0a65c3aaa5dc3c38414be857fd5d2cf98a0edc730"></a>
<a id="gga9f09b045f9db8aa2f2e21adb0a65c3aaade1f3bc7dab9c768feb8d70c149ffbda"></a>
<a id="gga9f09b045f9db8aa2f2e21adb0a65c3aaabbf719d116ec24bbf327c8e7a2eb50c0"></a>
<a id="gga6976a11ffe2c9a9b2fff82763be2edeeab119e2a0a3600269f752dfc7f271edee"></a>
<a id="gga6976a11ffe2c9a9b2fff82763be2edeea6af59b287c252dbb04d6ab6cdbbf6d6f"></a>
<a id="gga31d5d4a7184243ffe9d925714de4367fae373a1d0f3875bafbdcab7c1cca0f522"></a>
<a id="gga31d5d4a7184243ffe9d925714de4367fa63b460de845ef9cb7423c82008b2ed49"></a>
<a id="ggad981cab4d2a285ee72481b54836cf35bab8d7bcea2ab1d76a66727e11a520654a"></a>
<a id="ggad981cab4d2a285ee72481b54836cf35ba7bea7165cbba98284b9941cf8809787f"></a>
<a id="ggad981cab4d2a285ee72481b54836cf35ba527c9490662f70b789ecb0d37f90df3b"></a>
<a id="ggad981cab4d2a285ee72481b54836cf35ba8c70a47828ed3b90c08e742dff3c0ab7"></a>
<a id="gga7c425f7fd9e908e327810f89d7645745a69d60021c1d1772f461f0e90eadd9b46"></a>
<a id="gga7c425f7fd9e908e327810f89d7645745a74cb90028ebf42119c8c69a3801591ba"></a>
<a id="gga7c425f7fd9e908e327810f89d7645745add93cefc8c583aa0edd71ed66edbea3d"></a>
<a id="ggad410bdd972f09f0314b696ce31e6d82daa50e305c82d8081877576953e07241db"></a>
<a id="ggad410bdd972f09f0314b696ce31e6d82da683bc2d562e99ae0c691eb3611206f00"></a>
<a id="ggad410bdd972f09f0314b696ce31e6d82dae36621eac964d7f2b8b5959de11ba870"></a>
<a id="gga4e3f58a5f7c8715f3f8f24b96229b71ca98d72b37dce3b29dcc901bb58d3e6acf"></a>
<a id="gga4e3f58a5f7c8715f3f8f24b96229b71cadabb6df4477b9483e18cd3bd77ef8adc"></a>
<a id="gga4e3f58a5f7c8715f3f8f24b96229b71ca2064d10fa9b52c40142eb4f8a9ef2799"></a>
<a id="ggaf76a1eea78e9ff5c35977c41b00fb64dab90caed6b5b1fef37f79176ae6221383"></a>
<a id="ggaf76a1eea78e9ff5c35977c41b00fb64da3f2f11b307bb6e641792e4e85fe3a363"></a>
<a id="ggaf76a1eea78e9ff5c35977c41b00fb64daafeab5f57d1a12770bc9ac95161e1af8"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_协调集标识配置文件（Coordinated Set Identification Profile，CSIP）.md)
