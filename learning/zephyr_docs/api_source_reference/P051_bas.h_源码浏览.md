---
id: learning.zephyr-docs.api-source-reference.page-51
title: bas.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/bas_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第51章\_bas.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/bas_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/bas_8h.html)。

## 51.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="foldopen00035"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="foldopen00049"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="foldopen00064"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="foldopen00076"></a>
<a id="l00076"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="foldopen00091"></a>
<a id="l00091"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="foldopen00106"></a>
<a id="l00106"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="foldopen00124"></a>
<a id="l00124"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="foldopen00142"></a>
<a id="l00142"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="foldopen00163"></a>
<a id="l00163"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="foldopen00181"></a>
<a id="l00181"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="foldopen00196"></a>
<a id="l00196"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00297"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="l00302"></a>
<a id="l00306"></a>
<a id="l00307"></a>
<a id="agroup__bt__bas_html_ga31d5d4a7184243ffe9d925714de4367f"></a>
<a id="agroup__bt__bas_html_ga3584a3e7b7194bf244f414d6860b1313"></a>
<a id="agroup__bt__bas_html_ga3cea34f717f2df01b6f49bed80f27f44"></a>
<a id="agroup__bt__bas_html_ga4e3f58a5f7c8715f3f8f24b96229b71c"></a>
<a id="agroup__bt__bas_html_ga56d26a8cde072959e8d8b75ee4fb2819"></a>
<a id="agroup__bt__bas_html_ga5e0325af9dcd362dd3c1691832be5677"></a>
<a id="agroup__bt__bas_html_ga60b153c4d291ed4b16ce1f9d2dc1b45d"></a>
<a id="agroup__bt__bas_html_ga6976a11ffe2c9a9b2fff82763be2edee"></a>
<a id="agroup__bt__bas_html_ga7996edb35bcca878062360b24036b6f8"></a>
<a id="agroup__bt__bas_html_ga7bf36a53494e2ecfbb5ccd218f29f51f"></a>
<a id="agroup__bt__bas_html_ga7c425f7fd9e908e327810f89d7645745"></a>
<a id="agroup__bt__bas_html_ga9c50ed6a493adee208a59b17c48702f8"></a>
<a id="agroup__bt__bas_html_ga9f09b045f9db8aa2f2e21adb0a65c3aa"></a>
<a id="agroup__bt__bas_html_gaa94f308b6e135a3957191499778275ec"></a>
<a id="agroup__bt__bas_html_gac8d519830c34b9c8370366e2593dbeba"></a>
<a id="agroup__bt__bas_html_gac8e32530f966c7699d3c28e6685bcee5"></a>
<a id="agroup__bt__bas_html_gad374826ce9465bbf344b1f25b16c574c"></a>
<a id="agroup__bt__bas_html_gad410bdd972f09f0314b696ce31e6d82d"></a>
<a id="agroup__bt__bas_html_gad981cab4d2a285ee72481b54836cf35b"></a>
<a id="agroup__bt__bas_html_gadbe0f52d04d90372d603af66b693e980"></a>
<a id="agroup__bt__bas_html_gae1cbafd30e1d78437c78d44df25aa005"></a>
<a id="agroup__bt__bas_html_gaf76a1eea78e9ff5c35977c41b00fb64d"></a>
<a id="agroup__bt__bas_html_gafd74ef933734960a64f1ee1e80e9e335"></a>
<a id="agroup__bt__bas_html_gga31d5d4a7184243ffe9d925714de4367fa63b460de845ef9cb7423c82008b2ed49"></a>
<a id="agroup__bt__bas_html_gga31d5d4a7184243ffe9d925714de4367fae373a1d0f3875bafbdcab7c1cca0f522"></a>
<a id="agroup__bt__bas_html_gga3584a3e7b7194bf244f414d6860b1313a23a496ecd4b7e7d33ee7a2f0021c4f1a"></a>
<a id="agroup__bt__bas_html_gga3584a3e7b7194bf244f414d6860b1313a35249a218c5c15a24e9b529991282ab9"></a>
<a id="agroup__bt__bas_html_gga3584a3e7b7194bf244f414d6860b1313a663b3a9a4490600c56f2784246bbe58c"></a>
<a id="agroup__bt__bas_html_gga3584a3e7b7194bf244f414d6860b1313aba3c8d0d791dae18b6aa3149619e4e02"></a>
<a id="agroup__bt__bas_html_gga4e3f58a5f7c8715f3f8f24b96229b71ca2064d10fa9b52c40142eb4f8a9ef2799"></a>
<a id="agroup__bt__bas_html_gga4e3f58a5f7c8715f3f8f24b96229b71ca98d72b37dce3b29dcc901bb58d3e6acf"></a>
<a id="agroup__bt__bas_html_gga4e3f58a5f7c8715f3f8f24b96229b71cadabb6df4477b9483e18cd3bd77ef8adc"></a>
<a id="agroup__bt__bas_html_gga56d26a8cde072959e8d8b75ee4fb2819ad45c2b537f66cc7118357616120fa8a5"></a>
<a id="agroup__bt__bas_html_gga56d26a8cde072959e8d8b75ee4fb2819af82ae1d0e53efa882ff21d4e67b9ba7a"></a>
<a id="agroup__bt__bas_html_gga6976a11ffe2c9a9b2fff82763be2edeea6af59b287c252dbb04d6ab6cdbbf6d6f"></a>
<a id="agroup__bt__bas_html_gga6976a11ffe2c9a9b2fff82763be2edeeab119e2a0a3600269f752dfc7f271edee"></a>
<a id="agroup__bt__bas_html_gga7c425f7fd9e908e327810f89d7645745a69d60021c1d1772f461f0e90eadd9b46"></a>
<a id="agroup__bt__bas_html_gga7c425f7fd9e908e327810f89d7645745a74cb90028ebf42119c8c69a3801591ba"></a>
<a id="agroup__bt__bas_html_gga7c425f7fd9e908e327810f89d7645745add93cefc8c583aa0edd71ed66edbea3d"></a>
<a id="agroup__bt__bas_html_gga9f09b045f9db8aa2f2e21adb0a65c3aaa0c681a700639a1ba8b3cf3e5afc70e64"></a>
<a id="agroup__bt__bas_html_gga9f09b045f9db8aa2f2e21adb0a65c3aaa5a9f93290d6b11596771e7e9bbc357af"></a>
<a id="agroup__bt__bas_html_gga9f09b045f9db8aa2f2e21adb0a65c3aaa5dc3c38414be857fd5d2cf98a0edc730"></a>
<a id="agroup__bt__bas_html_gga9f09b045f9db8aa2f2e21adb0a65c3aaabbf719d116ec24bbf327c8e7a2eb50c0"></a>
<a id="agroup__bt__bas_html_gga9f09b045f9db8aa2f2e21adb0a65c3aaade1f3bc7dab9c768feb8d70c149ffbda"></a>
<a id="agroup__bt__bas_html_ggad374826ce9465bbf344b1f25b16c574ca27d8f485ee4ee50bb8d9c02049b9679e"></a>
<a id="agroup__bt__bas_html_ggad374826ce9465bbf344b1f25b16c574ca46fa5393ea4acefae2d2ffdfaef2a31d"></a>
<a id="agroup__bt__bas_html_ggad374826ce9465bbf344b1f25b16c574cabdd600d10005a09cbce4f5584cb3bb58"></a>
<a id="agroup__bt__bas_html_ggad374826ce9465bbf344b1f25b16c574cae08b7620b5babb731a6c8e8bf12b1387"></a>
<a id="agroup__bt__bas_html_ggad410bdd972f09f0314b696ce31e6d82da683bc2d562e99ae0c691eb3611206f00"></a>
<a id="agroup__bt__bas_html_ggad410bdd972f09f0314b696ce31e6d82daa50e305c82d8081877576953e07241db"></a>
<a id="agroup__bt__bas_html_ggad410bdd972f09f0314b696ce31e6d82dae36621eac964d7f2b8b5959de11ba870"></a>
<a id="agroup__bt__bas_html_ggad981cab4d2a285ee72481b54836cf35ba527c9490662f70b789ecb0d37f90df3b"></a>
<a id="agroup__bt__bas_html_ggad981cab4d2a285ee72481b54836cf35ba7bea7165cbba98284b9941cf8809787f"></a>
<a id="agroup__bt__bas_html_ggad981cab4d2a285ee72481b54836cf35ba8c70a47828ed3b90c08e742dff3c0ab7"></a>
<a id="agroup__bt__bas_html_ggad981cab4d2a285ee72481b54836cf35bab8d7bcea2ab1d76a66727e11a520654a"></a>
<a id="agroup__bt__bas_html_ggaf76a1eea78e9ff5c35977c41b00fb64da3f2f11b307bb6e641792e4e85fe3a363"></a>
<a id="agroup__bt__bas_html_ggaf76a1eea78e9ff5c35977c41b00fb64daafeab5f57d1a12770bc9ac95161e1af8"></a>
<a id="agroup__bt__bas_html_ggaf76a1eea78e9ff5c35977c41b00fb64dab90caed6b5b1fef37f79176ae6221383"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="asys_2util_8h_html"></a>

```c
/*
 * Copyright (c) 2024 Demant A/S
 * Copyright (c) 2018 Nordic Semiconductor ASA
 * Copyright (c) 2016 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_BLUETOOTH_SERVICES_BAS_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_SERVICES_BAS_H_


#include <stdint.h>
#include <zephyr/sys/util.h>

#ifdef __cplusplus
extern "C" {
#endif

enum bt_bas_bcs_flags {
        BT_BAS_BCS_BATTERY_CRITICAL_STATE = BIT(0),

        BT_BAS_BCS_IMMEDIATE_SERVICE_REQUIRED = BIT(1),
};

enum bt_bas_bls_flags {
        BT_BAS_BLS_FLAG_IDENTIFIER_PRESENT = BIT(0),

        BT_BAS_BLS_FLAG_BATTERY_LEVEL_PRESENT = BIT(1),

        BT_BAS_BLS_FLAG_ADDITIONAL_STATUS_PRESENT = BIT(2),
};

enum bt_bas_bls_battery_present {
        BT_BAS_BLS_BATTERY_NOT_PRESENT = 0,

        BT_BAS_BLS_BATTERY_PRESENT = 1
};

enum bt_bas_bls_wired_power_source {
        BT_BAS_BLS_WIRED_POWER_NOT_CONNECTED = 0,

        BT_BAS_BLS_WIRED_POWER_CONNECTED = 1,

        BT_BAS_BLS_WIRED_POWER_UNKNOWN = 2
};

enum bt_bas_bls_wireless_power_source {
        BT_BAS_BLS_WIRELESS_POWER_NOT_CONNECTED = 0,

        BT_BAS_BLS_WIRELESS_POWER_CONNECTED = 1,

        BT_BAS_BLS_WIRELESS_POWER_UNKNOWN = 2
};

enum bt_bas_bls_battery_charge_state {
        BT_BAS_BLS_CHARGE_STATE_UNKNOWN = 0,

        BT_BAS_BLS_CHARGE_STATE_CHARGING = 1,

        BT_BAS_BLS_CHARGE_STATE_DISCHARGING_ACTIVE = 2,

        BT_BAS_BLS_CHARGE_STATE_DISCHARGING_INACTIVE = 3
};

enum bt_bas_bls_battery_charge_level {
        BT_BAS_BLS_CHARGE_LEVEL_UNKNOWN = 0,

        BT_BAS_BLS_CHARGE_LEVEL_GOOD = 1,

        BT_BAS_BLS_CHARGE_LEVEL_LOW = 2,

        BT_BAS_BLS_CHARGE_LEVEL_CRITICAL = 3
};

enum bt_bas_bls_battery_charge_type {
        BT_BAS_BLS_CHARGE_TYPE_UNKNOWN = 0,

        BT_BAS_BLS_CHARGE_TYPE_CONSTANT_CURRENT = 1,

        BT_BAS_BLS_CHARGE_TYPE_CONSTANT_VOLTAGE = 2,

        BT_BAS_BLS_CHARGE_TYPE_TRICKLE = 3,

        BT_BAS_BLS_CHARGE_TYPE_FLOAT = 4
};

enum bt_bas_bls_charging_fault_reason {
        BT_BAS_BLS_FAULT_REASON_NONE = 0,

        BT_BAS_BLS_FAULT_REASON_BATTERY = BIT(0),

        BT_BAS_BLS_FAULT_REASON_EXTERNAL_POWER = BIT(1),

        BT_BAS_BLS_FAULT_REASON_OTHER = BIT(2)
};

enum bt_bas_bls_service_required {
        BT_BAS_BLS_SERVICE_REQUIRED_FALSE = 0,

        BT_BAS_BLS_SERVICE_REQUIRED_TRUE = 1,

        BT_BAS_BLS_SERVICE_REQUIRED_UNKNOWN = 2
};

enum bt_bas_bls_battery_fault {
        BT_BAS_BLS_BATTERY_FAULT_NO = 0,

        BT_BAS_BLS_BATTERY_FAULT_YES = 1
};

uint8_t bt_bas_get_battery_level(void);

int bt_bas_set_battery_level(uint8_t level);

void bt_bas_bls_set_battery_present(enum bt_bas_bls_battery_present present);

void bt_bas_bls_set_wired_external_power_source(enum bt_bas_bls_wired_power_source source);

void bt_bas_bls_set_wireless_external_power_source(enum bt_bas_bls_wireless_power_source source);

void bt_bas_bls_set_battery_charge_state(enum bt_bas_bls_battery_charge_state state);

void bt_bas_bls_set_battery_charge_level(enum bt_bas_bls_battery_charge_level level);

void bt_bas_bls_set_battery_charge_type(enum bt_bas_bls_battery_charge_type type);

void bt_bas_bls_set_charging_fault_reason(enum bt_bas_bls_charging_fault_reason reason);

void bt_bas_bls_set_identifier(uint16_t identifier);

void bt_bas_bls_set_service_required(enum bt_bas_bls_service_required value);

void bt_bas_bls_set_battery_fault(enum bt_bas_bls_battery_fault value);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_BLUETOOTH_SERVICES_BAS_H_ */
```

## 51.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Demant A/S。

版权（Copyright）：© 2018 Nordic Semiconductor ASA。

版权（Copyright）：© 2016 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 307 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_SERVICES_BAS_H_`。

## 51.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/bas_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [bt_bas_bcs_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html#ga56d26a8cde072959e8d8b75ee4fb2819)
- [BT_BAS_BCS_BATTERY_CRITICAL_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html#gga56d26a8cde072959e8d8b75ee4fb2819ad45c2b537f66cc7118357616120fa8a5)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [BT_BAS_BCS_IMMEDIATE_SERVICE_REQUIRED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html#gga56d26a8cde072959e8d8b75ee4fb2819af82ae1d0e53efa882ff21d4e67b9ba7a)
- [bt_bas_bls_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html#ga7c425f7fd9e908e327810f89d7645745)
- [BT_BAS_BLS_FLAG_IDENTIFIER_PRESENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html#gga7c425f7fd9e908e327810f89d7645745a69d60021c1d1772f461f0e90eadd9b46)
- [BT_BAS_BLS_FLAG_BATTERY_LEVEL_PRESENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html#gga7c425f7fd9e908e327810f89d7645745a74cb90028ebf42119c8c69a3801591ba)
- [BT_BAS_BLS_FLAG_ADDITIONAL_STATUS_PRESENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html#gga7c425f7fd9e908e327810f89d7645745add93cefc8c583aa0edd71ed66edbea3d)
- [bt_bas_bls_battery_present](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html#ga31d5d4a7184243ffe9d925714de4367f)
- [BT_BAS_BLS_BATTERY_NOT_PRESENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html#gga31d5d4a7184243ffe9d925714de4367fae373a1d0f3875bafbdcab7c1cca0f522)
- [BT_BAS_BLS_BATTERY_PRESENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html#gga31d5d4a7184243ffe9d925714de4367fa63b460de845ef9cb7423c82008b2ed49)
- [bt_bas_bls_wired_power_source](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html#ga4e3f58a5f7c8715f3f8f24b96229b71c)
- [BT_BAS_BLS_WIRED_POWER_NOT_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html#gga4e3f58a5f7c8715f3f8f24b96229b71ca98d72b37dce3b29dcc901bb58d3e6acf)
- [BT_BAS_BLS_WIRED_POWER_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html#gga4e3f58a5f7c8715f3f8f24b96229b71cadabb6df4477b9483e18cd3bd77ef8adc)
- [BT_BAS_BLS_WIRED_POWER_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html#gga4e3f58a5f7c8715f3f8f24b96229b71ca2064d10fa9b52c40142eb4f8a9ef2799)
- [bt_bas_bls_wireless_power_source](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html#gaf76a1eea78e9ff5c35977c41b00fb64d)
- [BT_BAS_BLS_WIRELESS_POWER_NOT_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html#ggaf76a1eea78e9ff5c35977c41b00fb64dab90caed6b5b1fef37f79176ae6221383)
- [BT_BAS_BLS_WIRELESS_POWER_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html#ggaf76a1eea78e9ff5c35977c41b00fb64da3f2f11b307bb6e641792e4e85fe3a363)
- [BT_BAS_BLS_WIRELESS_POWER_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html#ggaf76a1eea78e9ff5c35977c41b00fb64daafeab5f57d1a12770bc9ac95161e1af8)
- [bt_bas_bls_battery_charge_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html#ga3584a3e7b7194bf244f414d6860b1313)
- [BT_BAS_BLS_CHARGE_STATE_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html#gga3584a3e7b7194bf244f414d6860b1313a663b3a9a4490600c56f2784246bbe58c)
- [BT_BAS_BLS_CHARGE_STATE_CHARGING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html#gga3584a3e7b7194bf244f414d6860b1313a35249a218c5c15a24e9b529991282ab9)
- [BT_BAS_BLS_CHARGE_STATE_DISCHARGING_ACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html#gga3584a3e7b7194bf244f414d6860b1313aba3c8d0d791dae18b6aa3149619e4e02)
- [BT_BAS_BLS_CHARGE_STATE_DISCHARGING_INACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html#gga3584a3e7b7194bf244f414d6860b1313a23a496ecd4b7e7d33ee7a2f0021c4f1a)
- [bt_bas_bls_battery_charge_level](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html#gad374826ce9465bbf344b1f25b16c574c)
- [BT_BAS_BLS_CHARGE_LEVEL_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html#ggad374826ce9465bbf344b1f25b16c574cabdd600d10005a09cbce4f5584cb3bb58)
- [BT_BAS_BLS_CHARGE_LEVEL_GOOD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html#ggad374826ce9465bbf344b1f25b16c574cae08b7620b5babb731a6c8e8bf12b1387)
- [BT_BAS_BLS_CHARGE_LEVEL_LOW](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html#ggad374826ce9465bbf344b1f25b16c574ca27d8f485ee4ee50bb8d9c02049b9679e)
- [BT_BAS_BLS_CHARGE_LEVEL_CRITICAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html#ggad374826ce9465bbf344b1f25b16c574ca46fa5393ea4acefae2d2ffdfaef2a31d)
- [bt_bas_bls_battery_charge_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html#ga9f09b045f9db8aa2f2e21adb0a65c3aa)
- [BT_BAS_BLS_CHARGE_TYPE_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html#gga9f09b045f9db8aa2f2e21adb0a65c3aaa0c681a700639a1ba8b3cf3e5afc70e64)
- [BT_BAS_BLS_CHARGE_TYPE_CONSTANT_CURRENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html#gga9f09b045f9db8aa2f2e21adb0a65c3aaa5a9f93290d6b11596771e7e9bbc357af)
- [BT_BAS_BLS_CHARGE_TYPE_CONSTANT_VOLTAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html#gga9f09b045f9db8aa2f2e21adb0a65c3aaa5dc3c38414be857fd5d2cf98a0edc730)
- [BT_BAS_BLS_CHARGE_TYPE_TRICKLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html#gga9f09b045f9db8aa2f2e21adb0a65c3aaade1f3bc7dab9c768feb8d70c149ffbda)
- [BT_BAS_BLS_CHARGE_TYPE_FLOAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html#gga9f09b045f9db8aa2f2e21adb0a65c3aaabbf719d116ec24bbf327c8e7a2eb50c0)
- [bt_bas_bls_charging_fault_reason](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html#gad981cab4d2a285ee72481b54836cf35b)
- [BT_BAS_BLS_FAULT_REASON_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html#ggad981cab4d2a285ee72481b54836cf35bab8d7bcea2ab1d76a66727e11a520654a)
- [BT_BAS_BLS_FAULT_REASON_BATTERY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html#ggad981cab4d2a285ee72481b54836cf35ba7bea7165cbba98284b9941cf8809787f)
- [BT_BAS_BLS_FAULT_REASON_EXTERNAL_POWER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html#ggad981cab4d2a285ee72481b54836cf35ba527c9490662f70b789ecb0d37f90df3b)
- [BT_BAS_BLS_FAULT_REASON_OTHER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html#ggad981cab4d2a285ee72481b54836cf35ba8c70a47828ed3b90c08e742dff3c0ab7)
- [bt_bas_bls_service_required](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html#gad410bdd972f09f0314b696ce31e6d82d)
- [BT_BAS_BLS_SERVICE_REQUIRED_FALSE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html#ggad410bdd972f09f0314b696ce31e6d82daa50e305c82d8081877576953e07241db)
- [BT_BAS_BLS_SERVICE_REQUIRED_TRUE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html#ggad410bdd972f09f0314b696ce31e6d82da683bc2d562e99ae0c691eb3611206f00)
- [BT_BAS_BLS_SERVICE_REQUIRED_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html#ggad410bdd972f09f0314b696ce31e6d82dae36621eac964d7f2b8b5959de11ba870)
- [bt_bas_bls_battery_fault](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html#ga6976a11ffe2c9a9b2fff82763be2edee)
- [BT_BAS_BLS_BATTERY_FAULT_NO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html#gga6976a11ffe2c9a9b2fff82763be2edeeab119e2a0a3600269f752dfc7f271edee)
- [BT_BAS_BLS_BATTERY_FAULT_YES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html#gga6976a11ffe2c9a9b2fff82763be2edeea6af59b287c252dbb04d6ab6cdbbf6d6f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_bas_get_battery_level](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html#gadbe0f52d04d90372d603af66b693e980)
- [bt_bas_set_battery_level](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html#gac8d519830c34b9c8370366e2593dbeba)
- [bt_bas_bls_set_battery_present](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html#ga5e0325af9dcd362dd3c1691832be5677)
- [bt_bas_bls_set_wired_external_power_source](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html#ga7bf36a53494e2ecfbb5ccd218f29f51f)
- [bt_bas_bls_set_wireless_external_power_source](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html#gae1cbafd30e1d78437c78d44df25aa005)
- [bt_bas_bls_set_battery_charge_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html#ga60b153c4d291ed4b16ce1f9d2dc1b45d)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)
- [bt_bas_bls_set_battery_charge_level](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html#gac8e32530f966c7699d3c28e6685bcee5)
- [bt_bas_bls_set_battery_charge_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html#ga3cea34f717f2df01b6f49bed80f27f44)
- [bt_bas_bls_set_charging_fault_reason](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html#ga7996edb35bcca878062360b24036b6f8)
- [bt_bas_bls_set_identifier](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html#gafd74ef933734960a64f1ee1e80e9e335)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_bas_bls_set_service_required](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html#gaa94f308b6e135a3957191499778275ec)
- [bt_bas_bls_set_battery_fault](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html#ga9c50ed6a493adee208a59b17c48702f8)
- [util.h](../util_reference/P002_通用工具头文件参考.md)

---

[上一章](P050_backend.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P052_base.h_源码浏览.md)
