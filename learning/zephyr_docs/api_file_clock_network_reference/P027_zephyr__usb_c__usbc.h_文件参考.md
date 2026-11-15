---
id: learning.zephyr-docs.api-file-clock-network-reference.page-27
title: zephyr__usb_c__usbc.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/usbc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第27章\_zephyr\_\_usb\_c\_\_usbc.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/usbc_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

USB-C设备（Device）API。

<a id="details"></a>

```c
#include <zephyr/types.h>
#include <zephyr/device.h>
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
#include <zephyr/drivers/usb_c/usbc_vbus.h>
```

查看此文件的源码。

USB-C 设备 API（Device APIs）。本文件包含 USB-C 设备 API。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 27.1\_宏定义（Macros）

<a id="r_gaaa5c1f6278a7ca6d589c9c80695ca746"></a>

```c
#define FIXED_5V_100MA_RDO 0x1100280a
```

相关声明：[FIXED_5V_100MA_RDO](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gaaa5c1f6278a7ca6d589c9c80695ca746)。

若带有下述选项的 5 V、100 mA 供电足以让受电方（Sink）工作，则 policy_cb_get_rdo 可以返回此请求数据对象（Request Data Object，RDO）值。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 27.2\_类型定义（Typedefs）

<a id="r_gaaed0161142c3481ce9180015b6968357"></a>

```c
typedef int(* policy_cb_get_snk_cap_t) (const struct device *dev, uint32_t **pdos, int *num_pdos)
```

相关声明：[policy_cb_get_snk_cap_t](../api_power_policy_topic_reference/P010_受电端回调（Sink Callbacks）.md#gaaed0161142c3481ce9180015b6968357)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取受电端能力（Sink Capabilities）的回调类型。

<a id="r_ga6096d6909698f1b86a1a9cbd1f8d4097"></a>

```c
typedef void(* policy_cb_set_src_cap_t) (const struct device *dev, const uint32_t *pdos, const int num_pdos)
```

相关声明：[policy_cb_set_src_cap_t](../api_power_policy_topic_reference/P010_受电端回调（Sink Callbacks）.md#ga6096d6909698f1b86a1a9cbd1f8d4097)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

报告收到的端口对端供电能力（Port Partner's Source Capabilities）的回调类型。

<a id="r_ga2aacd704d08a8cecbf818150e8ec51b6"></a>

```c
typedef bool(* policy_cb_check_t) (const struct device *dev, const enum usbc_policy_check_t policy_check)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[policy_cb_check_t](../api_power_policy_topic_reference/P010_受电端回调（Sink Callbacks）.md#ga2aacd704d08a8cecbf818150e8ec51b6)、[device](../device_reference/P002_设备对象结构.md)、[usbc_policy_check_t](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gafea882f4f3cc96c502d53a24a3e5aec5)。

检查策略（Policy）的回调类型。

<a id="r_gaea62016b263dfaf5f869dd6ea036fdad"></a>

```c
typedef bool(* policy_cb_wait_notify_t) (const struct device *dev, const enum usbc_policy_wait_t wait_notify)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[policy_cb_wait_notify_t](../api_power_policy_topic_reference/P010_受电端回调（Sink Callbacks）.md#gaea62016b263dfaf5f869dd6ea036fdad)、[device](../device_reference/P002_设备对象结构.md)、[usbc_policy_wait_t](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gadf5d2934b5dc8e2b01d20bb904988784)。

通知设备策略管理器（Device Policy Manager）收到 `WAIT` 消息的回调类型。

<a id="r_ga44af668d9c22e757983c803d7b8ff82e"></a>

```c
typedef void(* policy_cb_notify_t) (const struct device *dev, const enum usbc_policy_notify_t policy_notify)
```

相关声明：[policy_cb_notify_t](../api_power_policy_topic_reference/P010_受电端回调（Sink Callbacks）.md#ga44af668d9c22e757983c803d7b8ff82e)、[device](../device_reference/P002_设备对象结构.md)、[usbc_policy_notify_t](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ga66f934a5c5cd88b574c71d1f18fbda23)。

通知设备策略管理器（Device Policy Manager）策略发生变化的回调类型。

<a id="r_gae0448c6b271273c5db59775c3a6260dc"></a>

```c
typedef uint32_t(* policy_cb_get_rdo_t) (const struct device *dev)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[policy_cb_get_rdo_t](../api_power_policy_topic_reference/P010_受电端回调（Sink Callbacks）.md#gae0448c6b271273c5db59775c3a6260dc)、[device](../device_reference/P002_设备对象结构.md)。

获取请求数据对象（Request Data Object，RDO）的回调类型。

<a id="r_ga1a3da6faad509213f607893fef16b673"></a>

```c
typedef bool(* policy_cb_is_snk_at_default_t) (const struct device *dev)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[policy_cb_is_snk_at_default_t](../api_power_policy_topic_reference/P010_受电端回调（Sink Callbacks）.md#ga1a3da6faad509213f607893fef16b673)、[device](../device_reference/P002_设备对象结构.md)。

检查受电端供电（Sink Power Supply）是否处于默认级别的回调类型。

<a id="r_ga4bbf78bd752d38d915412dd942d3aab8"></a>

```c
typedef int(* policy_cb_get_src_caps_t) (const struct device *dev, const uint32_t **pdos, uint32_t *num_pdos)
```

相关声明：[policy_cb_get_src_caps_t](../api_input_runtime_topic_reference/P018_供电端回调（Source Callbacks）.md#ga4bbf78bd752d38d915412dd942d3aab8)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

从设备策略管理器（Device Policy Manager）获取供电端能力（Source Capabilities）的回调类型。

<a id="r_gaeeda677224456f685137e4b345c0e173"></a>

```c
typedef enum usbc_snk_req_reply_t(* policy_cb_check_sink_request_t) (const struct device *dev, const uint32_t request_msg)
```

相关声明：[usbc_snk_req_reply_t](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ga4c4f0592a034b4e49eee85e95af33f94)、[policy_cb_check_sink_request_t](../api_input_runtime_topic_reference/P018_供电端回调（Source Callbacks）.md#gaeeda677224456f685137e4b345c0e173)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

检查受电端请求（Sink Request）是否有效的回调类型。

<a id="r_gae7391e858485e44a74e5fcdbb7931ca7"></a>

```c
typedef bool(* policy_cb_is_ps_ready_t) (const struct device *dev)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[policy_cb_is_ps_ready_t](../api_input_runtime_topic_reference/P018_供电端回调（Source Callbacks）.md#gae7391e858485e44a74e5fcdbb7931ca7)、[device](../device_reference/P002_设备对象结构.md)。

检查供电端电源（Source Power Supply）是否就绪的回调类型。

<a id="r_ga2925e462140a700920251d92ae5a3aa4"></a>

```c
typedef bool(* policy_cb_present_contract_is_valid_t) (const struct device *dev, const uint32_t present_contract)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[policy_cb_present_contract_is_valid_t](../api_input_runtime_topic_reference/P018_供电端回调（Source Callbacks）.md#ga2925e462140a700920251d92ae5a3aa4)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

检查当前供电契约（Contract）是否仍有效的回调类型。

<a id="r_ga699811c862990b31ec0126dd3a4c3e4d"></a>

```c
typedef bool(* policy_cb_change_src_caps_t) (const struct device *dev)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[policy_cb_change_src_caps_t](../api_input_runtime_topic_reference/P018_供电端回调（Source Callbacks）.md#ga699811c862990b31ec0126dd3a4c3e4d)、[device](../device_reference/P002_设备对象结构.md)。

请求向受电端（Sink）发送另一组供电端能力（Source Caps）的回调类型。

<a id="r_gae903c8108e8d1563cb0b1ccdd901c925"></a>

```c
typedef void(* policy_cb_set_port_partner_snk_cap_t) (const struct device *dev, const uint32_t *pdos, const int num_pdos)
```

相关声明：[policy_cb_set_port_partner_snk_cap_t](../api_input_runtime_topic_reference/P018_供电端回调（Source Callbacks）.md#gae903c8108e8d1563cb0b1ccdd901c925)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

报告从受电端口对端（Sink Port Partner）收到的能力（Capabilities）的回调类型。

<a id="r_ga7c75f8192001179f20bf1fe48316f3c6"></a>

```c
typedef int(* policy_cb_get_src_rp_t) (const struct device *dev, enum tc_rp_value *rp)
```

相关声明：[policy_cb_get_src_rp_t](../api_input_runtime_topic_reference/P018_供电端回调（Source Callbacks）.md#ga7c75f8192001179f20bf1fe48316f3c6)、[device](../device_reference/P002_设备对象结构.md)、[tc_rp_value](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#ga4e0eec97f7c5c97b87eff9561deea2d5)。

获取应施加到配置通道（CC）线上的 Rp 值的回调类型。

<a id="r_gaaecac7683d7092c0a477e8d9ca0e5a33"></a>

```c
typedef int(* policy_cb_src_en_t) (const struct device *dev, bool en)
```

相关声明：[policy_cb_src_en_t](../api_input_runtime_topic_reference/P018_供电端回调（Source Callbacks）.md#gaaecac7683d7092c0a477e8d9ca0e5a33)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用 VBUS 的回调类型。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 27.3\_枚举（Enumerations）

<a id="r_ga38a301a97a5e1a85e9836bbf083859f3"></a>

```c
enum usbc_policy_request_t { REQUEST_NOP , REQUEST_TC_DISABLED , REQUEST_TC_ERROR_RECOVERY , REQUEST_TC_END , REQUEST_PE_DR_SWAP , REQUEST_PE_HARD_RESET_SEND , REQUEST_PE_SOFT_RESET_SEND , REQUEST_PE_GET_SRC_CAPS , REQUEST_GET_SNK_CAPS , REQUEST_PE_GOTO_MIN }
```

相关声明：[usbc_policy_request_t](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ga38a301a97a5e1a85e9836bbf083859f3)、[REQUEST_NOP](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga38a301a97a5e1a85e9836bbf083859f3a2274197ac367b3da6358cac8dd781134)、[REQUEST_TC_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga38a301a97a5e1a85e9836bbf083859f3a899633a1b63b1c3a826b5556f0f23d8b)、[REQUEST_TC_ERROR_RECOVERY](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga38a301a97a5e1a85e9836bbf083859f3a8a7b77d81428f0c4784af3204f33b290)、[REQUEST_TC_END](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga38a301a97a5e1a85e9836bbf083859f3a0c5ff3bc4c0d6f636663fd3911ed85d5)、[REQUEST_PE_DR_SWAP](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga38a301a97a5e1a85e9836bbf083859f3a1fe9f57fac7f5149fe5f0f7c42523536)、[REQUEST_PE_HARD_RESET_SEND](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga38a301a97a5e1a85e9836bbf083859f3a7c3c9c959439ee73539cff13e561c403)、[REQUEST_PE_SOFT_RESET_SEND](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga38a301a97a5e1a85e9836bbf083859f3ad45120b1ceabeb054c2c2273b8431894)、[REQUEST_PE_GET_SRC_CAPS](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga38a301a97a5e1a85e9836bbf083859f3a8c6083028ee8655cd0bebb6d9aab2e1e)、[REQUEST_GET_SNK_CAPS](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga38a301a97a5e1a85e9836bbf083859f3ade1edc3aef0e4d563934edbc9ce784bc)、[REQUEST_PE_GOTO_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga38a301a97a5e1a85e9836bbf083859f3ae5b4eb0db00e81a98cfe2436b64a7018)。

设备策略管理器请求（Device Policy Manager Requests）。

<a id="r_ga66f934a5c5cd88b574c71d1f18fbda23"></a>

```c
enum usbc_policy_notify_t { MSG_ACCEPT_RECEIVED , MSG_REJECTED_RECEIVED , MSG_DISCARDED , MSG_NOT_SUPPORTED_RECEIVED , DATA_ROLE_IS_UFP , DATA_ROLE_IS_DFP , POWER_ROLE_IS_SOURCE , POWER_ROLE_IS_SINK , PD_CONNECTED , NOT_PD_CONNECTED , TRANSITION_PS , PORT_PARTNER_NOT_RESPONSIVE , PROTOCOL_ERROR , SNK_TRANSITION_TO_DEFAULT , HARD_RESET_RECEIVED , POWER_CHANGE_0A0 , POWER_CHANGE_DEF , POWER_CHANGE_1A5 , POWER_CHANGE_3A0 , SENDER_RESPONSE_TIMEOUT , SOURCE_CAPABILITIES_RECEIVED }
```

相关声明：[usbc_policy_notify_t](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ga66f934a5c5cd88b574c71d1f18fbda23)、[MSG_ACCEPT_RECEIVED](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23a43bc56906b5dc4767d3297400053d286)、[MSG_REJECTED_RECEIVED](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23a4ad0620e76c694004d3a1b43458a14b2)、[MSG_DISCARDED](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23aa316636e8353dad1a9d5dec8b85a67e4)、[MSG_NOT_SUPPORTED_RECEIVED](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23ab2f97ffaa13c84e656f7ac0004ec86ae)、[DATA_ROLE_IS_UFP](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23a4020203569dcb95ab1b3d2946efced19)、[DATA_ROLE_IS_DFP](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23a791604f4f0b2a2c3ccea4e98d1659a61)、[POWER_ROLE_IS_SOURCE](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23a75abb66ae57bb7ad946b8c3c2734f445)、[POWER_ROLE_IS_SINK](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23ae0372eb6238d86c3cfb2a10764180451)、[PD_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23adbefad204068244fdf75ba1ff211fbfc)、[NOT_PD_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23adebcbf5155b43ce562127d4077d46d7d)、[TRANSITION_PS](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23a3a27b8e70ffe5788aa3ffea1bf61cae9)、[PORT_PARTNER_NOT_RESPONSIVE](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23ad52e1c4f949bb64fef1d996ac2f4e0de)、[PROTOCOL_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23a8cb937247ec21f791706f4f426496a8c)、[SNK_TRANSITION_TO_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23aa02158d0afdd60c755453977200dfb28)、[HARD_RESET_RECEIVED](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23ab74f5bcaa94a5fb1e46cdd7c6a5d822f)、[POWER_CHANGE_0A0](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23a0fb0676a11ad8bad2d5249031ba5fd19)、[POWER_CHANGE_DEF](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23a3a50be6f70c1a7abd724ab447491c46a)、[POWER_CHANGE_1A5](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23a336bfb983c4d07684d67d4d9ef6c1489)、[POWER_CHANGE_3A0](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23a3477c1c6ad8885c3ab7a9c58b7399dcf)、[SENDER_RESPONSE_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23ac22b0026881f65c574d0bf7454321745)、[SOURCE_CAPABILITIES_RECEIVED](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23a0266a21d8c836cf281c30542eb6badd4)。

设备策略管理器通知（Device Policy Manager Notifications）。

<a id="r_gafea882f4f3cc96c502d53a24a3e5aec5"></a>

```c
enum usbc_policy_check_t { CHECK_POWER_ROLE_SWAP , CHECK_DATA_ROLE_SWAP_TO_DFP , CHECK_DATA_ROLE_SWAP_TO_UFP , CHECK_SNK_AT_DEFAULT_LEVEL , CHECK_VCONN_CONTROL , CHECK_SRC_PS_AT_DEFAULT_LEVEL }
```

相关声明：[usbc_policy_check_t](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gafea882f4f3cc96c502d53a24a3e5aec5)、[CHECK_POWER_ROLE_SWAP](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ggafea882f4f3cc96c502d53a24a3e5aec5a1181a470497b797136cf0eb204394106)、[CHECK_DATA_ROLE_SWAP_TO_DFP](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ggafea882f4f3cc96c502d53a24a3e5aec5afa602e00bf418656e365baa4d9ff6cef)、[CHECK_DATA_ROLE_SWAP_TO_UFP](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ggafea882f4f3cc96c502d53a24a3e5aec5a7c97208a8a12f70e7ffa43bb406b9ebd)、[CHECK_SNK_AT_DEFAULT_LEVEL](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ggafea882f4f3cc96c502d53a24a3e5aec5a17f7f4fc9aa4178f0358769dedd29ade)、[CHECK_VCONN_CONTROL](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ggafea882f4f3cc96c502d53a24a3e5aec5a655e913c86db5caa961083dad9f6b7a1)、[CHECK_SRC_PS_AT_DEFAULT_LEVEL](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ggafea882f4f3cc96c502d53a24a3e5aec5a42b660bb630edcca5ae8b031033d0718)。

设备策略管理器检查（Device Policy Manager Checks）。

<a id="r_gadf5d2934b5dc8e2b01d20bb904988784"></a>

```c
enum usbc_policy_wait_t { WAIT_SINK_REQUEST , WAIT_POWER_ROLE_SWAP , WAIT_DATA_ROLE_SWAP , WAIT_VCONN_SWAP }
```

相关声明：[usbc_policy_wait_t](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gadf5d2934b5dc8e2b01d20bb904988784)、[WAIT_SINK_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ggadf5d2934b5dc8e2b01d20bb904988784a009ce2ceacd92db88d9a6beb01f84a28)、[WAIT_POWER_ROLE_SWAP](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ggadf5d2934b5dc8e2b01d20bb904988784a91f1f41bf9318e06c02c1957a39a762a)、[WAIT_DATA_ROLE_SWAP](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ggadf5d2934b5dc8e2b01d20bb904988784ae5ef03f78d78a7014404c581bad77c18)、[WAIT_VCONN_SWAP](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ggadf5d2934b5dc8e2b01d20bb904988784aa982aed81f39e35cde74399c6d74e601)。

设备策略管理器等待消息通知（Device Policy Manager Wait Message Notifications）。

<a id="r_ga4c4f0592a034b4e49eee85e95af33f94"></a>

```c
enum usbc_snk_req_reply_t { SNK_REQUEST_VALID , SNK_REQUEST_REJECT , SNK_REQUEST_WAIT }
```

相关声明：[usbc_snk_req_reply_t](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ga4c4f0592a034b4e49eee85e95af33f94)、[SNK_REQUEST_VALID](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga4c4f0592a034b4e49eee85e95af33f94a7922edb67afe83596819994a71de76dd)、[SNK_REQUEST_REJECT](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga4c4f0592a034b4e49eee85e95af33f94a714f82e830f9528a8200c2c14795b282)、[SNK_REQUEST_WAIT](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga4c4f0592a034b4e49eee85e95af33f94a7ae46f6deb593eedd0564d30cb4c75fb)。

设备策略管理器对受电方请求（Sink Request）的响应。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 27.4\_函数（Functions）

<a id="r_ga1535f7f53b3cc859ff536883fd631830"></a>

```c
int usbc_start (const struct device *dev)
```

相关声明：[usbc_start](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ga1535f7f53b3cc859ff536883fd631830)、[device](../device_reference/P002_设备对象结构.md)。

启动 USB-C 子系统（Subsystem）。

<a id="r_ga68b73c03a5098a21260b5c3638edc973"></a>

```c
int usbc_suspend (const struct device *dev)
```

相关声明：[usbc_suspend](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ga68b73c03a5098a21260b5c3638edc973)、[device](../device_reference/P002_设备对象结构.md)。

挂起 USB-C 子系统（Suspend Subsystem）。

<a id="r_ga42691b0bb2b4be50147ac655e2cd9761"></a>

```c
int usbc_request (const struct device *dev, const enum usbc_policy_request_t req)
```

相关声明：[usbc_request](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ga42691b0bb2b4be50147ac655e2cd9761)、[device](../device_reference/P002_设备对象结构.md)、[usbc_policy_request_t](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ga38a301a97a5e1a85e9836bbf083859f3)。

向 USB-C 子系统（Subsystem）提出请求。

<a id="r_ga997007cab2e54ad53b774b4215d0f593"></a>

```c
void usbc_set_dpm_data (const struct device *dev, void *dpm_data)
```

相关声明：[usbc_set_dpm_data](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ga997007cab2e54ad53b774b4215d0f593)、[device](../device_reference/P002_设备对象结构.md)。

设置设备策略管理器（Device Policy Manager，DPM）数据的指针。

<a id="r_gabd99b6926baf67212d65c4a4d147ce5b"></a>

```c
void * usbc_get_dpm_data (const struct device *dev)
```

相关声明：[usbc_get_dpm_data](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gabd99b6926baf67212d65c4a4d147ce5b)、[device](../device_reference/P002_设备对象结构.md)。

获取设备策略管理器（Device Policy Manager，DPM）数据的指针。

<a id="r_ga9846b36061453023e16c160f5f120159"></a>

```c
void usbc_set_vconn_control_cb (const struct device *dev, const tcpc_vconn_control_cb_t cb)
```

相关声明：[usbc_set_vconn_control_cb](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ga9846b36061453023e16c160f5f120159)、[device](../device_reference/P002_设备对象结构.md)、[tcpc_vconn_control_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga073ad4a46a5ea1f9e5cad45488d672f0)。

设置用于配置 VCONN 控制（Control）的回调。

<a id="r_ga8741df33b5432d9c7d5902af9bd67084"></a>

```c
void usbc_set_vconn_discharge_cb (const struct device *dev, const tcpc_vconn_discharge_cb_t cb)
```

相关声明：[usbc_set_vconn_discharge_cb](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ga8741df33b5432d9c7d5902af9bd67084)、[device](../device_reference/P002_设备对象结构.md)、[tcpc_vconn_discharge_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga4d2b77f6ee685d1bff1117843150e664)。

设置用于 VCONN 放电（Discharge）的回调。

<a id="r_ga67a046b411134d7c631942ae6ba73fc5"></a>

```c
void usbc_set_policy_cb_check (const struct device *dev, const policy_cb_check_t cb)
```

相关声明：[usbc_set_policy_cb_check](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ga67a046b411134d7c631942ae6ba73fc5)、[device](../device_reference/P002_设备对象结构.md)、[policy_cb_check_t](../api_power_policy_topic_reference/P010_受电端回调（Sink Callbacks）.md#ga2aacd704d08a8cecbf818150e8ec51b6)。

设置用于检查策略（Policy）的回调。

<a id="r_gaedec1b4ad7b028ad18e1bcbe5396f1ee"></a>

```c
void usbc_set_policy_cb_notify (const struct device *dev, const policy_cb_notify_t cb)
```

相关声明：[usbc_set_policy_cb_notify](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gaedec1b4ad7b028ad18e1bcbe5396f1ee)、[device](../device_reference/P002_设备对象结构.md)、[policy_cb_notify_t](../api_power_policy_topic_reference/P010_受电端回调（Sink Callbacks）.md#ga44af668d9c22e757983c803d7b8ff82e)。

设置用于向设备策略管理器通知策略变化（Policy Change）的回调。

<a id="r_gaa295593c7d5ede31328efaaab38b5880"></a>

```c
void usbc_set_policy_cb_wait_notify (const struct device *dev, const policy_cb_wait_notify_t cb)
```

相关声明：[usbc_set_policy_cb_wait_notify](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gaa295593c7d5ede31328efaaab38b5880)、[device](../device_reference/P002_设备对象结构.md)、[policy_cb_wait_notify_t](../api_power_policy_topic_reference/P010_受电端回调（Sink Callbacks）.md#gaea62016b263dfaf5f869dd6ea036fdad)。

设置用于向设备策略管理器通知已收到 WAIT 消息的回调。

<a id="r_gafbd2885d758aa869635041fa89750596"></a>

```c
void usbc_set_policy_cb_get_snk_cap (const struct device *dev, const policy_cb_get_snk_cap_t cb)
```

相关声明：[usbc_set_policy_cb_get_snk_cap](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gafbd2885d758aa869635041fa89750596)、[device](../device_reference/P002_设备对象结构.md)、[policy_cb_get_snk_cap_t](../api_power_policy_topic_reference/P010_受电端回调（Sink Callbacks）.md#gaaed0161142c3481ce9180015b6968357)。

设置用于获取受电方能力（Sink Capabilities）的回调。

<a id="r_ga4536f47082f58f49d492de6f2b00dd17"></a>

```c
void usbc_set_policy_cb_set_src_cap (const struct device *dev, const policy_cb_set_src_cap_t cb)
```

相关声明：[usbc_set_policy_cb_set_src_cap](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ga4536f47082f58f49d492de6f2b00dd17)、[device](../device_reference/P002_设备对象结构.md)、[policy_cb_set_src_cap_t](../api_power_policy_topic_reference/P010_受电端回调（Sink Callbacks）.md#ga6096d6909698f1b86a1a9cbd1f8d4097)。

设置用于存储已接收的端口伙伴供电能力（Port Partner's Source Capabilities）的回调。

<a id="r_ga7c1ffea81f71416ab2942fc5a5b67d41"></a>

```c
void usbc_set_policy_cb_get_rdo (const struct device *dev, const policy_cb_get_rdo_t cb)
```

相关声明：[usbc_set_policy_cb_get_rdo](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ga7c1ffea81f71416ab2942fc5a5b67d41)、[device](../device_reference/P002_设备对象结构.md)、[policy_cb_get_rdo_t](../api_power_policy_topic_reference/P010_受电端回调（Sink Callbacks）.md#gae0448c6b271273c5db59775c3a6260dc)。

设置用于获取请求数据对象（Request Data Object，RDO）的回调。

<a id="r_gaffa045ee6e2fbc07fde7e84e44d3853f"></a>

```c
void usbc_set_policy_cb_is_snk_at_default (const struct device *dev, const policy_cb_is_snk_at_default_t cb)
```

相关声明：[usbc_set_policy_cb_is_snk_at_default](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gaffa045ee6e2fbc07fde7e84e44d3853f)、[device](../device_reference/P002_设备对象结构.md)、[policy_cb_is_snk_at_default_t](../api_power_policy_topic_reference/P010_受电端回调（Sink Callbacks）.md#ga1a3da6faad509213f607893fef16b673)。

设置用于检查受电方电源是否处于默认级别（Default Level）的回调。

<a id="r_ga8974f9661dfebf8f686d677f999d5957"></a>

```c
void usbc_set_policy_cb_get_src_rp (const struct device *dev, const policy_cb_get_src_rp_t cb)
```

相关声明：[usbc_set_policy_cb_get_src_rp](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ga8974f9661dfebf8f686d677f999d5957)、[device](../device_reference/P002_设备对象结构.md)、[policy_cb_get_src_rp_t](../api_input_runtime_topic_reference/P018_供电端回调（Source Callbacks）.md#ga7c75f8192001179f20bf1fe48316f3c6)。

设置用于获取应施加在配置通道（CC）线上的 Rp 值的回调。

<a id="r_gaf5332ba0c87ff737e1c476d7be071fec"></a>

```c
void usbc_set_policy_cb_src_en (const struct device *dev, const policy_cb_src_en_t cb)
```

相关声明：[usbc_set_policy_cb_src_en](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gaf5332ba0c87ff737e1c476d7be071fec)、[device](../device_reference/P002_设备对象结构.md)、[policy_cb_src_en_t](../api_input_runtime_topic_reference/P018_供电端回调（Source Callbacks）.md#gaaecac7683d7092c0a477e8d9ca0e5a33)。

设置用于启用 VBUS 的回调。

<a id="r_ga7800c065ae5cfb7a95b58865d47c7f04"></a>

```c
void usbc_set_policy_cb_get_src_caps (const struct device *dev, const policy_cb_get_src_caps_t cb)
```

相关声明：[usbc_set_policy_cb_get_src_caps](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ga7800c065ae5cfb7a95b58865d47c7f04)、[device](../device_reference/P002_设备对象结构.md)、[policy_cb_get_src_caps_t](../api_input_runtime_topic_reference/P018_供电端回调（Source Callbacks）.md#ga4bbf78bd752d38d915412dd942d3aab8)。

设置用于从设备策略管理器获取供电方能力（Source Capabilities）的回调。

<a id="r_ga7f85188cc4f1a95350195abd0d736ada"></a>

```c
void usbc_set_policy_cb_check_sink_request (const struct device *dev, const policy_cb_check_sink_request_t cb)
```

相关声明：[usbc_set_policy_cb_check_sink_request](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ga7f85188cc4f1a95350195abd0d736ada)、[device](../device_reference/P002_设备对象结构.md)、[policy_cb_check_sink_request_t](../api_input_runtime_topic_reference/P018_供电端回调（Source Callbacks）.md#gaeeda677224456f685137e4b345c0e173)。

设置用于检查受电方请求（Sink Request）是否有效的回调。

<a id="r_gaf25c9cc2b6c514b9dcddc8129a76ccee"></a>

```c
void usbc_set_policy_cb_is_ps_ready (const struct device *dev, const policy_cb_is_ps_ready_t cb)
```

相关声明：[usbc_set_policy_cb_is_ps_ready](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gaf25c9cc2b6c514b9dcddc8129a76ccee)、[device](../device_reference/P002_设备对象结构.md)、[policy_cb_is_ps_ready_t](../api_input_runtime_topic_reference/P018_供电端回调（Source Callbacks）.md#gae7391e858485e44a74e5fcdbb7931ca7)。

设置用于检查供电方电源（Source Power Supply）是否就绪的回调。

<a id="r_ga5b4adb4330dfadf127d0a01253d722bb"></a>

```c
void usbc_set_policy_cb_present_contract_is_valid (const struct device *dev, const policy_cb_present_contract_is_valid_t cb)
```

相关声明：[usbc_set_policy_cb_present_contract_is_valid](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ga5b4adb4330dfadf127d0a01253d722bb)、[device](../device_reference/P002_设备对象结构.md)、[policy_cb_present_contract_is_valid_t](../api_input_runtime_topic_reference/P018_供电端回调（Source Callbacks）.md#ga2925e462140a700920251d92ae5a3aa4)。

设置用于检查当前供电协定（Contract）是否仍有效的回调。

<a id="r_gaa8f89bfb1e9a1840b2d61ebaa13aeb2f"></a>

```c
void usbc_set_policy_cb_change_src_caps (const struct device *dev, const policy_cb_change_src_caps_t cb)
```

相关声明：[usbc_set_policy_cb_change_src_caps](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gaa8f89bfb1e9a1840b2d61ebaa13aeb2f)、[device](../device_reference/P002_设备对象结构.md)、[policy_cb_change_src_caps_t](../api_input_runtime_topic_reference/P018_供电端回调（Source Callbacks）.md#ga699811c862990b31ec0126dd3a4c3e4d)。

设置用于请求向受电方发送另一组供电能力（Source Caps）的回调。

<a id="r_gafd0a407558bb92dc8b7007d9d717b940"></a>

```c
void usbc_set_policy_cb_set_port_partner_snk_cap (const struct device *dev, const policy_cb_set_port_partner_snk_cap_t cb)
```

相关声明：[usbc_set_policy_cb_set_port_partner_snk_cap](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gafd0a407558bb92dc8b7007d9d717b940)、[device](../device_reference/P002_设备对象结构.md)、[policy_cb_set_port_partner_snk_cap_t](../api_input_runtime_topic_reference/P018_供电端回调（Source Callbacks）.md#gae903c8108e8d1563cb0b1ccdd901c925)。

设置用于存储从受电端口伙伴（Sink Port Partner）收到的能力（Capabilities）的回调。


## 27.5\_原页交叉引用（Cross References）

- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/drivers/usb_c/usbc_tcpc.h](../api_source_reference/P892_usbc_tcpc.h_源码浏览.md)
- [zephyr/drivers/usb_c/usbc_vbus.h](../api_source_reference/P893_usbc_vbus.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P889_usbc.h_源码浏览.md)
- [FIXED_5V_100MA_RDO](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gaaa5c1f6278a7ca6d589c9c80695ca746)
- [policy_cb_get_snk_cap_t](../api_power_policy_topic_reference/P010_受电端回调（Sink Callbacks）.md#gaaed0161142c3481ce9180015b6968357)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [policy_cb_set_src_cap_t](../api_power_policy_topic_reference/P010_受电端回调（Sink Callbacks）.md#ga6096d6909698f1b86a1a9cbd1f8d4097)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [policy_cb_check_t](../api_power_policy_topic_reference/P010_受电端回调（Sink Callbacks）.md#ga2aacd704d08a8cecbf818150e8ec51b6)
- [usbc_policy_check_t](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gafea882f4f3cc96c502d53a24a3e5aec5)
- [policy_cb_wait_notify_t](../api_power_policy_topic_reference/P010_受电端回调（Sink Callbacks）.md#gaea62016b263dfaf5f869dd6ea036fdad)
- [usbc_policy_wait_t](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gadf5d2934b5dc8e2b01d20bb904988784)
- [policy_cb_notify_t](../api_power_policy_topic_reference/P010_受电端回调（Sink Callbacks）.md#ga44af668d9c22e757983c803d7b8ff82e)
- [usbc_policy_notify_t](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ga66f934a5c5cd88b574c71d1f18fbda23)
- [policy_cb_get_rdo_t](../api_power_policy_topic_reference/P010_受电端回调（Sink Callbacks）.md#gae0448c6b271273c5db59775c3a6260dc)
- [policy_cb_is_snk_at_default_t](../api_power_policy_topic_reference/P010_受电端回调（Sink Callbacks）.md#ga1a3da6faad509213f607893fef16b673)
- [policy_cb_get_src_caps_t](../api_input_runtime_topic_reference/P018_供电端回调（Source Callbacks）.md#ga4bbf78bd752d38d915412dd942d3aab8)
- [usbc_snk_req_reply_t](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ga4c4f0592a034b4e49eee85e95af33f94)
- [policy_cb_check_sink_request_t](../api_input_runtime_topic_reference/P018_供电端回调（Source Callbacks）.md#gaeeda677224456f685137e4b345c0e173)
- [policy_cb_is_ps_ready_t](../api_input_runtime_topic_reference/P018_供电端回调（Source Callbacks）.md#gae7391e858485e44a74e5fcdbb7931ca7)
- [policy_cb_present_contract_is_valid_t](../api_input_runtime_topic_reference/P018_供电端回调（Source Callbacks）.md#ga2925e462140a700920251d92ae5a3aa4)
- [policy_cb_change_src_caps_t](../api_input_runtime_topic_reference/P018_供电端回调（Source Callbacks）.md#ga699811c862990b31ec0126dd3a4c3e4d)
- [policy_cb_set_port_partner_snk_cap_t](../api_input_runtime_topic_reference/P018_供电端回调（Source Callbacks）.md#gae903c8108e8d1563cb0b1ccdd901c925)
- [policy_cb_get_src_rp_t](../api_input_runtime_topic_reference/P018_供电端回调（Source Callbacks）.md#ga7c75f8192001179f20bf1fe48316f3c6)
- [tc_rp_value](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#ga4e0eec97f7c5c97b87eff9561deea2d5)
- [policy_cb_src_en_t](../api_input_runtime_topic_reference/P018_供电端回调（Source Callbacks）.md#gaaecac7683d7092c0a477e8d9ca0e5a33)
- [usbc_policy_request_t](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ga38a301a97a5e1a85e9836bbf083859f3)
- [REQUEST_NOP](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga38a301a97a5e1a85e9836bbf083859f3a2274197ac367b3da6358cac8dd781134)
- [REQUEST_TC_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga38a301a97a5e1a85e9836bbf083859f3a899633a1b63b1c3a826b5556f0f23d8b)
- [REQUEST_TC_ERROR_RECOVERY](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga38a301a97a5e1a85e9836bbf083859f3a8a7b77d81428f0c4784af3204f33b290)
- [REQUEST_TC_END](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga38a301a97a5e1a85e9836bbf083859f3a0c5ff3bc4c0d6f636663fd3911ed85d5)
- [REQUEST_PE_DR_SWAP](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga38a301a97a5e1a85e9836bbf083859f3a1fe9f57fac7f5149fe5f0f7c42523536)
- [REQUEST_PE_HARD_RESET_SEND](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga38a301a97a5e1a85e9836bbf083859f3a7c3c9c959439ee73539cff13e561c403)
- [REQUEST_PE_SOFT_RESET_SEND](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga38a301a97a5e1a85e9836bbf083859f3ad45120b1ceabeb054c2c2273b8431894)
- [REQUEST_PE_GET_SRC_CAPS](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga38a301a97a5e1a85e9836bbf083859f3a8c6083028ee8655cd0bebb6d9aab2e1e)
- [REQUEST_GET_SNK_CAPS](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga38a301a97a5e1a85e9836bbf083859f3ade1edc3aef0e4d563934edbc9ce784bc)
- [REQUEST_PE_GOTO_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga38a301a97a5e1a85e9836bbf083859f3ae5b4eb0db00e81a98cfe2436b64a7018)
- [MSG_ACCEPT_RECEIVED](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23a43bc56906b5dc4767d3297400053d286)
- [MSG_REJECTED_RECEIVED](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23a4ad0620e76c694004d3a1b43458a14b2)
- [MSG_DISCARDED](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23aa316636e8353dad1a9d5dec8b85a67e4)
- [MSG_NOT_SUPPORTED_RECEIVED](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23ab2f97ffaa13c84e656f7ac0004ec86ae)
- [DATA_ROLE_IS_UFP](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23a4020203569dcb95ab1b3d2946efced19)
- [DATA_ROLE_IS_DFP](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23a791604f4f0b2a2c3ccea4e98d1659a61)
- [POWER_ROLE_IS_SOURCE](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23a75abb66ae57bb7ad946b8c3c2734f445)
- [POWER_ROLE_IS_SINK](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23ae0372eb6238d86c3cfb2a10764180451)
- [PD_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23adbefad204068244fdf75ba1ff211fbfc)
- [NOT_PD_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23adebcbf5155b43ce562127d4077d46d7d)
- [TRANSITION_PS](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23a3a27b8e70ffe5788aa3ffea1bf61cae9)
- [PORT_PARTNER_NOT_RESPONSIVE](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23ad52e1c4f949bb64fef1d996ac2f4e0de)
- [PROTOCOL_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23a8cb937247ec21f791706f4f426496a8c)
- [SNK_TRANSITION_TO_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23aa02158d0afdd60c755453977200dfb28)
- [HARD_RESET_RECEIVED](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23ab74f5bcaa94a5fb1e46cdd7c6a5d822f)
- [POWER_CHANGE_0A0](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23a0fb0676a11ad8bad2d5249031ba5fd19)
- [POWER_CHANGE_DEF](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23a3a50be6f70c1a7abd724ab447491c46a)
- [POWER_CHANGE_1A5](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23a336bfb983c4d07684d67d4d9ef6c1489)
- [POWER_CHANGE_3A0](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23a3477c1c6ad8885c3ab7a9c58b7399dcf)
- [SENDER_RESPONSE_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23ac22b0026881f65c574d0bf7454321745)
- [SOURCE_CAPABILITIES_RECEIVED](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23a0266a21d8c836cf281c30542eb6badd4)
- [CHECK_POWER_ROLE_SWAP](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ggafea882f4f3cc96c502d53a24a3e5aec5a1181a470497b797136cf0eb204394106)
- [CHECK_DATA_ROLE_SWAP_TO_DFP](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ggafea882f4f3cc96c502d53a24a3e5aec5afa602e00bf418656e365baa4d9ff6cef)
- [CHECK_DATA_ROLE_SWAP_TO_UFP](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ggafea882f4f3cc96c502d53a24a3e5aec5a7c97208a8a12f70e7ffa43bb406b9ebd)
- [CHECK_SNK_AT_DEFAULT_LEVEL](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ggafea882f4f3cc96c502d53a24a3e5aec5a17f7f4fc9aa4178f0358769dedd29ade)
- [CHECK_VCONN_CONTROL](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ggafea882f4f3cc96c502d53a24a3e5aec5a655e913c86db5caa961083dad9f6b7a1)
- [CHECK_SRC_PS_AT_DEFAULT_LEVEL](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ggafea882f4f3cc96c502d53a24a3e5aec5a42b660bb630edcca5ae8b031033d0718)
- [WAIT_SINK_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ggadf5d2934b5dc8e2b01d20bb904988784a009ce2ceacd92db88d9a6beb01f84a28)
- [WAIT_POWER_ROLE_SWAP](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ggadf5d2934b5dc8e2b01d20bb904988784a91f1f41bf9318e06c02c1957a39a762a)
- [WAIT_DATA_ROLE_SWAP](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ggadf5d2934b5dc8e2b01d20bb904988784ae5ef03f78d78a7014404c581bad77c18)
- [WAIT_VCONN_SWAP](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ggadf5d2934b5dc8e2b01d20bb904988784aa982aed81f39e35cde74399c6d74e601)
- [SNK_REQUEST_VALID](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga4c4f0592a034b4e49eee85e95af33f94a7922edb67afe83596819994a71de76dd)
- [SNK_REQUEST_REJECT](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga4c4f0592a034b4e49eee85e95af33f94a714f82e830f9528a8200c2c14795b282)
- [SNK_REQUEST_WAIT](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga4c4f0592a034b4e49eee85e95af33f94a7ae46f6deb593eedd0564d30cb4c75fb)
- [usbc_start](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ga1535f7f53b3cc859ff536883fd631830)
- [usbc_suspend](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ga68b73c03a5098a21260b5c3638edc973)
- [usbc_request](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ga42691b0bb2b4be50147ac655e2cd9761)
- [usbc_set_dpm_data](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ga997007cab2e54ad53b774b4215d0f593)
- [usbc_get_dpm_data](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gabd99b6926baf67212d65c4a4d147ce5b)
- [usbc_set_vconn_control_cb](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ga9846b36061453023e16c160f5f120159)
- [tcpc_vconn_control_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga073ad4a46a5ea1f9e5cad45488d672f0)
- [usbc_set_vconn_discharge_cb](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ga8741df33b5432d9c7d5902af9bd67084)
- [tcpc_vconn_discharge_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga4d2b77f6ee685d1bff1117843150e664)
- [usbc_set_policy_cb_check](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ga67a046b411134d7c631942ae6ba73fc5)
- [usbc_set_policy_cb_notify](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gaedec1b4ad7b028ad18e1bcbe5396f1ee)
- [usbc_set_policy_cb_wait_notify](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gaa295593c7d5ede31328efaaab38b5880)
- [usbc_set_policy_cb_get_snk_cap](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gafbd2885d758aa869635041fa89750596)
- [usbc_set_policy_cb_set_src_cap](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ga4536f47082f58f49d492de6f2b00dd17)
- [usbc_set_policy_cb_get_rdo](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ga7c1ffea81f71416ab2942fc5a5b67d41)
- [usbc_set_policy_cb_is_snk_at_default](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gaffa045ee6e2fbc07fde7e84e44d3853f)
- [usbc_set_policy_cb_get_src_rp](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ga8974f9661dfebf8f686d677f999d5957)
- [usbc_set_policy_cb_src_en](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gaf5332ba0c87ff737e1c476d7be071fec)
- [usbc_set_policy_cb_get_src_caps](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ga7800c065ae5cfb7a95b58865d47c7f04)
- [usbc_set_policy_cb_check_sink_request](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ga7f85188cc4f1a95350195abd0d736ada)
- [usbc_set_policy_cb_is_ps_ready](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gaf25c9cc2b6c514b9dcddc8129a76ccee)
- [usbc_set_policy_cb_present_contract_is_valid](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ga5b4adb4330dfadf127d0a01253d722bb)
- [usbc_set_policy_cb_change_src_caps](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gaa8f89bfb1e9a1840b2d61ebaa13aeb2f)
- [usbc_set_policy_cb_set_port_partner_snk_cap](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gafd0a407558bb92dc8b7007d9d717b940)

<a id="header-details"></a>

---

[上一章](P026_zephyr__drivers__usb__uhc.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P028_zephyr__bluetooth__audio__vcp.h_文件参考.md)
