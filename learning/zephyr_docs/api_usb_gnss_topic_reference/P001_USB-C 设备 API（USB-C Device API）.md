---
id: learning.zephyr-docs.api-usb-gnss-topic-reference.page-1
title: USB-C 设备 API（USB-C Device API）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_USB-C 设备 API（USB-C Device API）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

USB-C设备（Device）API。

<a id="details"></a>

USB-C 设备 API（USB-C Device APIs）。起始版本（Since）：3.3。接口版本（Version）：0.1.0。

<a id="header-groups"></a>
<a id="groups"></a>

## 1.1\_主题（Topics）

<a id="r_sink_5Fcallbacks"></a>

相关声明：[受电端回调（Sink Callbacks）](../api_power_policy_topic_reference/P010_受电端回调（Sink Callbacks）.md)。

<a id="r_source_5Fcallbacks"></a>

相关声明：[供电端回调（Source Callbacks）](../api_input_runtime_topic_reference/P018_供电端回调（Source Callbacks）.md)。

<a id="header-files"></a>
<a id="files"></a>

## 1.2\_文件（Files）

<a id="r_usbc_2Eh"></a>

```c
file usbc.h
```

相关声明：[usbc.h](../api_file_clock_network_reference/P027_zephyr__usb_c__usbc.h_文件参考.md)。

USB-C设备（Device）API。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.3\_宏定义（Macros）

<a id="r_gaaa5c1f6278a7ca6d589c9c80695ca746"></a>

```c
#define FIXED_5V_100MA_RDO 0x1100280a
```

相关声明：[FIXED_5V_100MA_RDO](#gaaa5c1f6278a7ca6d589c9c80695ca746)。

若带有下述选项的 5 V、100 mA 供电足以让受电方（Sink）工作，则 policy_cb_get_rdo 可以返回此请求数据对象（Request Data Object，RDO）值。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 1.4\_枚举（Enumerations）

<a id="r_ga38a301a97a5e1a85e9836bbf083859f3"></a>

```c
enum usbc_policy_request_t { REQUEST_NOP , REQUEST_TC_DISABLED , REQUEST_TC_ERROR_RECOVERY , REQUEST_TC_END , REQUEST_PE_DR_SWAP , REQUEST_PE_HARD_RESET_SEND , REQUEST_PE_SOFT_RESET_SEND , REQUEST_PE_GET_SRC_CAPS , REQUEST_GET_SNK_CAPS , REQUEST_PE_GOTO_MIN }
```

相关声明：[usbc_policy_request_t](#ga38a301a97a5e1a85e9836bbf083859f3)、[REQUEST_NOP](#gga38a301a97a5e1a85e9836bbf083859f3a2274197ac367b3da6358cac8dd781134)、[REQUEST_TC_DISABLED](#gga38a301a97a5e1a85e9836bbf083859f3a899633a1b63b1c3a826b5556f0f23d8b)、[REQUEST_TC_ERROR_RECOVERY](#gga38a301a97a5e1a85e9836bbf083859f3a8a7b77d81428f0c4784af3204f33b290)、[REQUEST_TC_END](#gga38a301a97a5e1a85e9836bbf083859f3a0c5ff3bc4c0d6f636663fd3911ed85d5)、[REQUEST_PE_DR_SWAP](#gga38a301a97a5e1a85e9836bbf083859f3a1fe9f57fac7f5149fe5f0f7c42523536)、[REQUEST_PE_HARD_RESET_SEND](#gga38a301a97a5e1a85e9836bbf083859f3a7c3c9c959439ee73539cff13e561c403)、[REQUEST_PE_SOFT_RESET_SEND](#gga38a301a97a5e1a85e9836bbf083859f3ad45120b1ceabeb054c2c2273b8431894)、[REQUEST_PE_GET_SRC_CAPS](#gga38a301a97a5e1a85e9836bbf083859f3a8c6083028ee8655cd0bebb6d9aab2e1e)、[REQUEST_GET_SNK_CAPS](#gga38a301a97a5e1a85e9836bbf083859f3ade1edc3aef0e4d563934edbc9ce784bc)、[REQUEST_PE_GOTO_MIN](#gga38a301a97a5e1a85e9836bbf083859f3ae5b4eb0db00e81a98cfe2436b64a7018)。

设备策略管理器请求（Device Policy Manager Requests）。

<a id="r_ga66f934a5c5cd88b574c71d1f18fbda23"></a>

```c
enum usbc_policy_notify_t { MSG_ACCEPT_RECEIVED , MSG_REJECTED_RECEIVED , MSG_DISCARDED , MSG_NOT_SUPPORTED_RECEIVED , DATA_ROLE_IS_UFP , DATA_ROLE_IS_DFP , POWER_ROLE_IS_SOURCE , POWER_ROLE_IS_SINK , PD_CONNECTED , NOT_PD_CONNECTED , TRANSITION_PS , PORT_PARTNER_NOT_RESPONSIVE , PROTOCOL_ERROR , SNK_TRANSITION_TO_DEFAULT , HARD_RESET_RECEIVED , POWER_CHANGE_0A0 , POWER_CHANGE_DEF , POWER_CHANGE_1A5 , POWER_CHANGE_3A0 , SENDER_RESPONSE_TIMEOUT , SOURCE_CAPABILITIES_RECEIVED }
```

相关声明：[usbc_policy_notify_t](#ga66f934a5c5cd88b574c71d1f18fbda23)、[MSG_ACCEPT_RECEIVED](#gga66f934a5c5cd88b574c71d1f18fbda23a43bc56906b5dc4767d3297400053d286)、[MSG_REJECTED_RECEIVED](#gga66f934a5c5cd88b574c71d1f18fbda23a4ad0620e76c694004d3a1b43458a14b2)、[MSG_DISCARDED](#gga66f934a5c5cd88b574c71d1f18fbda23aa316636e8353dad1a9d5dec8b85a67e4)、[MSG_NOT_SUPPORTED_RECEIVED](#gga66f934a5c5cd88b574c71d1f18fbda23ab2f97ffaa13c84e656f7ac0004ec86ae)、[DATA_ROLE_IS_UFP](#gga66f934a5c5cd88b574c71d1f18fbda23a4020203569dcb95ab1b3d2946efced19)、[DATA_ROLE_IS_DFP](#gga66f934a5c5cd88b574c71d1f18fbda23a791604f4f0b2a2c3ccea4e98d1659a61)、[POWER_ROLE_IS_SOURCE](#gga66f934a5c5cd88b574c71d1f18fbda23a75abb66ae57bb7ad946b8c3c2734f445)、[POWER_ROLE_IS_SINK](#gga66f934a5c5cd88b574c71d1f18fbda23ae0372eb6238d86c3cfb2a10764180451)、[PD_CONNECTED](#gga66f934a5c5cd88b574c71d1f18fbda23adbefad204068244fdf75ba1ff211fbfc)、[NOT_PD_CONNECTED](#gga66f934a5c5cd88b574c71d1f18fbda23adebcbf5155b43ce562127d4077d46d7d)、[TRANSITION_PS](#gga66f934a5c5cd88b574c71d1f18fbda23a3a27b8e70ffe5788aa3ffea1bf61cae9)、[PORT_PARTNER_NOT_RESPONSIVE](#gga66f934a5c5cd88b574c71d1f18fbda23ad52e1c4f949bb64fef1d996ac2f4e0de)、[PROTOCOL_ERROR](#gga66f934a5c5cd88b574c71d1f18fbda23a8cb937247ec21f791706f4f426496a8c)、[SNK_TRANSITION_TO_DEFAULT](#gga66f934a5c5cd88b574c71d1f18fbda23aa02158d0afdd60c755453977200dfb28)、[HARD_RESET_RECEIVED](#gga66f934a5c5cd88b574c71d1f18fbda23ab74f5bcaa94a5fb1e46cdd7c6a5d822f)、[POWER_CHANGE_0A0](#gga66f934a5c5cd88b574c71d1f18fbda23a0fb0676a11ad8bad2d5249031ba5fd19)、[POWER_CHANGE_DEF](#gga66f934a5c5cd88b574c71d1f18fbda23a3a50be6f70c1a7abd724ab447491c46a)、[POWER_CHANGE_1A5](#gga66f934a5c5cd88b574c71d1f18fbda23a336bfb983c4d07684d67d4d9ef6c1489)、[POWER_CHANGE_3A0](#gga66f934a5c5cd88b574c71d1f18fbda23a3477c1c6ad8885c3ab7a9c58b7399dcf)、[SENDER_RESPONSE_TIMEOUT](#gga66f934a5c5cd88b574c71d1f18fbda23ac22b0026881f65c574d0bf7454321745)、[SOURCE_CAPABILITIES_RECEIVED](#gga66f934a5c5cd88b574c71d1f18fbda23a0266a21d8c836cf281c30542eb6badd4)。

设备策略管理器通知（Device Policy Manager Notifications）。

<a id="r_gafea882f4f3cc96c502d53a24a3e5aec5"></a>

```c
enum usbc_policy_check_t { CHECK_POWER_ROLE_SWAP , CHECK_DATA_ROLE_SWAP_TO_DFP , CHECK_DATA_ROLE_SWAP_TO_UFP , CHECK_SNK_AT_DEFAULT_LEVEL , CHECK_VCONN_CONTROL , CHECK_SRC_PS_AT_DEFAULT_LEVEL }
```

相关声明：[usbc_policy_check_t](#gafea882f4f3cc96c502d53a24a3e5aec5)、[CHECK_POWER_ROLE_SWAP](#ggafea882f4f3cc96c502d53a24a3e5aec5a1181a470497b797136cf0eb204394106)、[CHECK_DATA_ROLE_SWAP_TO_DFP](#ggafea882f4f3cc96c502d53a24a3e5aec5afa602e00bf418656e365baa4d9ff6cef)、[CHECK_DATA_ROLE_SWAP_TO_UFP](#ggafea882f4f3cc96c502d53a24a3e5aec5a7c97208a8a12f70e7ffa43bb406b9ebd)、[CHECK_SNK_AT_DEFAULT_LEVEL](#ggafea882f4f3cc96c502d53a24a3e5aec5a17f7f4fc9aa4178f0358769dedd29ade)、[CHECK_VCONN_CONTROL](#ggafea882f4f3cc96c502d53a24a3e5aec5a655e913c86db5caa961083dad9f6b7a1)、[CHECK_SRC_PS_AT_DEFAULT_LEVEL](#ggafea882f4f3cc96c502d53a24a3e5aec5a42b660bb630edcca5ae8b031033d0718)。

设备策略管理器检查（Device Policy Manager Checks）。

<a id="r_gadf5d2934b5dc8e2b01d20bb904988784"></a>

```c
enum usbc_policy_wait_t { WAIT_SINK_REQUEST , WAIT_POWER_ROLE_SWAP , WAIT_DATA_ROLE_SWAP , WAIT_VCONN_SWAP }
```

相关声明：[usbc_policy_wait_t](#gadf5d2934b5dc8e2b01d20bb904988784)、[WAIT_SINK_REQUEST](#ggadf5d2934b5dc8e2b01d20bb904988784a009ce2ceacd92db88d9a6beb01f84a28)、[WAIT_POWER_ROLE_SWAP](#ggadf5d2934b5dc8e2b01d20bb904988784a91f1f41bf9318e06c02c1957a39a762a)、[WAIT_DATA_ROLE_SWAP](#ggadf5d2934b5dc8e2b01d20bb904988784ae5ef03f78d78a7014404c581bad77c18)、[WAIT_VCONN_SWAP](#ggadf5d2934b5dc8e2b01d20bb904988784aa982aed81f39e35cde74399c6d74e601)。

设备策略管理器等待消息通知（Device Policy Manager Wait Message Notifications）。

<a id="r_ga4c4f0592a034b4e49eee85e95af33f94"></a>

```c
enum usbc_snk_req_reply_t { SNK_REQUEST_VALID , SNK_REQUEST_REJECT , SNK_REQUEST_WAIT }
```

相关声明：[usbc_snk_req_reply_t](#ga4c4f0592a034b4e49eee85e95af33f94)、[SNK_REQUEST_VALID](#gga4c4f0592a034b4e49eee85e95af33f94a7922edb67afe83596819994a71de76dd)、[SNK_REQUEST_REJECT](#gga4c4f0592a034b4e49eee85e95af33f94a714f82e830f9528a8200c2c14795b282)、[SNK_REQUEST_WAIT](#gga4c4f0592a034b4e49eee85e95af33f94a7ae46f6deb593eedd0564d30cb4c75fb)。

设备策略管理器对受电方请求（Sink Request）的响应。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.5\_函数（Functions）

<a id="r_ga1535f7f53b3cc859ff536883fd631830"></a>

```c
int usbc_start (const struct device *dev)
```

相关声明：[usbc_start](#ga1535f7f53b3cc859ff536883fd631830)、[device](../device_reference/P002_设备对象结构.md)。

启动 USB-C 子系统（Subsystem）。

<a id="r_ga68b73c03a5098a21260b5c3638edc973"></a>

```c
int usbc_suspend (const struct device *dev)
```

相关声明：[usbc_suspend](#ga68b73c03a5098a21260b5c3638edc973)、[device](../device_reference/P002_设备对象结构.md)。

挂起 USB-C 子系统（Suspend Subsystem）。

<a id="r_ga42691b0bb2b4be50147ac655e2cd9761"></a>

```c
int usbc_request (const struct device *dev, const enum usbc_policy_request_t req)
```

相关声明：[usbc_request](#ga42691b0bb2b4be50147ac655e2cd9761)、[device](../device_reference/P002_设备对象结构.md)、[usbc_policy_request_t](#ga38a301a97a5e1a85e9836bbf083859f3)。

向 USB-C 子系统（Subsystem）提出请求。

<a id="r_ga997007cab2e54ad53b774b4215d0f593"></a>

```c
void usbc_set_dpm_data (const struct device *dev, void *dpm_data)
```

相关声明：[usbc_set_dpm_data](#ga997007cab2e54ad53b774b4215d0f593)、[device](../device_reference/P002_设备对象结构.md)。

设置设备策略管理器（Device Policy Manager，DPM）数据的指针。

<a id="r_gabd99b6926baf67212d65c4a4d147ce5b"></a>

```c
void * usbc_get_dpm_data (const struct device *dev)
```

相关声明：[usbc_get_dpm_data](#gabd99b6926baf67212d65c4a4d147ce5b)、[device](../device_reference/P002_设备对象结构.md)。

获取设备策略管理器（Device Policy Manager，DPM）数据的指针。

<a id="r_ga9846b36061453023e16c160f5f120159"></a>

```c
void usbc_set_vconn_control_cb (const struct device *dev, const tcpc_vconn_control_cb_t cb)
```

相关声明：[usbc_set_vconn_control_cb](#ga9846b36061453023e16c160f5f120159)、[device](../device_reference/P002_设备对象结构.md)、[tcpc_vconn_control_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga073ad4a46a5ea1f9e5cad45488d672f0)。

设置用于配置 VCONN 控制（Control）的回调。

<a id="r_ga8741df33b5432d9c7d5902af9bd67084"></a>

```c
void usbc_set_vconn_discharge_cb (const struct device *dev, const tcpc_vconn_discharge_cb_t cb)
```

相关声明：[usbc_set_vconn_discharge_cb](#ga8741df33b5432d9c7d5902af9bd67084)、[device](../device_reference/P002_设备对象结构.md)、[tcpc_vconn_discharge_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga4d2b77f6ee685d1bff1117843150e664)。

设置用于 VCONN 放电（Discharge）的回调。

<a id="r_ga67a046b411134d7c631942ae6ba73fc5"></a>

```c
void usbc_set_policy_cb_check (const struct device *dev, const policy_cb_check_t cb)
```

相关声明：[usbc_set_policy_cb_check](#ga67a046b411134d7c631942ae6ba73fc5)、[device](../device_reference/P002_设备对象结构.md)、[policy_cb_check_t](../api_power_policy_topic_reference/P010_受电端回调（Sink Callbacks）.md#ga2aacd704d08a8cecbf818150e8ec51b6)。

设置用于检查策略（Policy）的回调。

<a id="r_gaedec1b4ad7b028ad18e1bcbe5396f1ee"></a>

```c
void usbc_set_policy_cb_notify (const struct device *dev, const policy_cb_notify_t cb)
```

相关声明：[usbc_set_policy_cb_notify](#gaedec1b4ad7b028ad18e1bcbe5396f1ee)、[device](../device_reference/P002_设备对象结构.md)、[policy_cb_notify_t](../api_power_policy_topic_reference/P010_受电端回调（Sink Callbacks）.md#ga44af668d9c22e757983c803d7b8ff82e)。

设置用于向设备策略管理器通知策略变化（Policy Change）的回调。

<a id="r_gaa295593c7d5ede31328efaaab38b5880"></a>

```c
void usbc_set_policy_cb_wait_notify (const struct device *dev, const policy_cb_wait_notify_t cb)
```

相关声明：[usbc_set_policy_cb_wait_notify](#gaa295593c7d5ede31328efaaab38b5880)、[device](../device_reference/P002_设备对象结构.md)、[policy_cb_wait_notify_t](../api_power_policy_topic_reference/P010_受电端回调（Sink Callbacks）.md#gaea62016b263dfaf5f869dd6ea036fdad)。

设置用于向设备策略管理器通知已收到 WAIT 消息的回调。

<a id="r_gafbd2885d758aa869635041fa89750596"></a>

```c
void usbc_set_policy_cb_get_snk_cap (const struct device *dev, const policy_cb_get_snk_cap_t cb)
```

相关声明：[usbc_set_policy_cb_get_snk_cap](#gafbd2885d758aa869635041fa89750596)、[device](../device_reference/P002_设备对象结构.md)、[policy_cb_get_snk_cap_t](../api_power_policy_topic_reference/P010_受电端回调（Sink Callbacks）.md#gaaed0161142c3481ce9180015b6968357)。

设置用于获取受电方能力（Sink Capabilities）的回调。

<a id="r_ga4536f47082f58f49d492de6f2b00dd17"></a>

```c
void usbc_set_policy_cb_set_src_cap (const struct device *dev, const policy_cb_set_src_cap_t cb)
```

相关声明：[usbc_set_policy_cb_set_src_cap](#ga4536f47082f58f49d492de6f2b00dd17)、[device](../device_reference/P002_设备对象结构.md)、[policy_cb_set_src_cap_t](../api_power_policy_topic_reference/P010_受电端回调（Sink Callbacks）.md#ga6096d6909698f1b86a1a9cbd1f8d4097)。

设置用于存储已接收的端口伙伴供电能力（Port Partner's Source Capabilities）的回调。

<a id="r_ga7c1ffea81f71416ab2942fc5a5b67d41"></a>

```c
void usbc_set_policy_cb_get_rdo (const struct device *dev, const policy_cb_get_rdo_t cb)
```

相关声明：[usbc_set_policy_cb_get_rdo](#ga7c1ffea81f71416ab2942fc5a5b67d41)、[device](../device_reference/P002_设备对象结构.md)、[policy_cb_get_rdo_t](../api_power_policy_topic_reference/P010_受电端回调（Sink Callbacks）.md#gae0448c6b271273c5db59775c3a6260dc)。

设置用于获取请求数据对象（Request Data Object，RDO）的回调。

<a id="r_gaffa045ee6e2fbc07fde7e84e44d3853f"></a>

```c
void usbc_set_policy_cb_is_snk_at_default (const struct device *dev, const policy_cb_is_snk_at_default_t cb)
```

相关声明：[usbc_set_policy_cb_is_snk_at_default](#gaffa045ee6e2fbc07fde7e84e44d3853f)、[device](../device_reference/P002_设备对象结构.md)、[policy_cb_is_snk_at_default_t](../api_power_policy_topic_reference/P010_受电端回调（Sink Callbacks）.md#ga1a3da6faad509213f607893fef16b673)。

设置用于检查受电方电源是否处于默认级别（Default Level）的回调。

<a id="r_ga8974f9661dfebf8f686d677f999d5957"></a>

```c
void usbc_set_policy_cb_get_src_rp (const struct device *dev, const policy_cb_get_src_rp_t cb)
```

相关声明：[usbc_set_policy_cb_get_src_rp](#ga8974f9661dfebf8f686d677f999d5957)、[device](../device_reference/P002_设备对象结构.md)、[policy_cb_get_src_rp_t](../api_input_runtime_topic_reference/P018_供电端回调（Source Callbacks）.md#ga7c75f8192001179f20bf1fe48316f3c6)。

设置用于获取应施加在配置通道（CC）线上的 Rp 值的回调。

<a id="r_gaf5332ba0c87ff737e1c476d7be071fec"></a>

```c
void usbc_set_policy_cb_src_en (const struct device *dev, const policy_cb_src_en_t cb)
```

相关声明：[usbc_set_policy_cb_src_en](#gaf5332ba0c87ff737e1c476d7be071fec)、[device](../device_reference/P002_设备对象结构.md)、[policy_cb_src_en_t](../api_input_runtime_topic_reference/P018_供电端回调（Source Callbacks）.md#gaaecac7683d7092c0a477e8d9ca0e5a33)。

设置用于启用 VBUS 的回调。

<a id="r_ga7800c065ae5cfb7a95b58865d47c7f04"></a>

```c
void usbc_set_policy_cb_get_src_caps (const struct device *dev, const policy_cb_get_src_caps_t cb)
```

相关声明：[usbc_set_policy_cb_get_src_caps](#ga7800c065ae5cfb7a95b58865d47c7f04)、[device](../device_reference/P002_设备对象结构.md)、[policy_cb_get_src_caps_t](../api_input_runtime_topic_reference/P018_供电端回调（Source Callbacks）.md#ga4bbf78bd752d38d915412dd942d3aab8)。

设置用于从设备策略管理器获取供电方能力（Source Capabilities）的回调。

<a id="r_ga7f85188cc4f1a95350195abd0d736ada"></a>

```c
void usbc_set_policy_cb_check_sink_request (const struct device *dev, const policy_cb_check_sink_request_t cb)
```

相关声明：[usbc_set_policy_cb_check_sink_request](#ga7f85188cc4f1a95350195abd0d736ada)、[device](../device_reference/P002_设备对象结构.md)、[policy_cb_check_sink_request_t](../api_input_runtime_topic_reference/P018_供电端回调（Source Callbacks）.md#gaeeda677224456f685137e4b345c0e173)。

设置用于检查受电方请求（Sink Request）是否有效的回调。

<a id="r_gaf25c9cc2b6c514b9dcddc8129a76ccee"></a>

```c
void usbc_set_policy_cb_is_ps_ready (const struct device *dev, const policy_cb_is_ps_ready_t cb)
```

相关声明：[usbc_set_policy_cb_is_ps_ready](#gaf25c9cc2b6c514b9dcddc8129a76ccee)、[device](../device_reference/P002_设备对象结构.md)、[policy_cb_is_ps_ready_t](../api_input_runtime_topic_reference/P018_供电端回调（Source Callbacks）.md#gae7391e858485e44a74e5fcdbb7931ca7)。

设置用于检查供电方电源（Source Power Supply）是否就绪的回调。

<a id="r_ga5b4adb4330dfadf127d0a01253d722bb"></a>

```c
void usbc_set_policy_cb_present_contract_is_valid (const struct device *dev, const policy_cb_present_contract_is_valid_t cb)
```

相关声明：[usbc_set_policy_cb_present_contract_is_valid](#ga5b4adb4330dfadf127d0a01253d722bb)、[device](../device_reference/P002_设备对象结构.md)、[policy_cb_present_contract_is_valid_t](../api_input_runtime_topic_reference/P018_供电端回调（Source Callbacks）.md#ga2925e462140a700920251d92ae5a3aa4)。

设置用于检查当前供电协定（Contract）是否仍有效的回调。

<a id="r_gaa8f89bfb1e9a1840b2d61ebaa13aeb2f"></a>

```c
void usbc_set_policy_cb_change_src_caps (const struct device *dev, const policy_cb_change_src_caps_t cb)
```

相关声明：[usbc_set_policy_cb_change_src_caps](#gaa8f89bfb1e9a1840b2d61ebaa13aeb2f)、[device](../device_reference/P002_设备对象结构.md)、[policy_cb_change_src_caps_t](../api_input_runtime_topic_reference/P018_供电端回调（Source Callbacks）.md#ga699811c862990b31ec0126dd3a4c3e4d)。

设置用于请求向受电方发送另一组供电能力（Source Caps）的回调。

<a id="r_gafd0a407558bb92dc8b7007d9d717b940"></a>

```c
void usbc_set_policy_cb_set_port_partner_snk_cap (const struct device *dev, const policy_cb_set_port_partner_snk_cap_t cb)
```

相关声明：[usbc_set_policy_cb_set_port_partner_snk_cap](#gafd0a407558bb92dc8b7007d9d717b940)、[device](../device_reference/P002_设备对象结构.md)、[policy_cb_set_port_partner_snk_cap_t](../api_input_runtime_topic_reference/P018_供电端回调（Source Callbacks）.md#gae903c8108e8d1563cb0b1ccdd901c925)。

设置用于存储从受电端口伙伴（Sink Port Partner）收到的能力（Capabilities）的回调。

## 1.6\_详细说明（Detailed Documentation）

<a id="gaaa5c1f6278a7ca6d589c9c80695ca746"></a>

### `FIXED_5V_100MA_RDO`

```c
#define FIXED_5V_100MA_RDO 0x1100280a
```

```c
#include <zephyr/usb_c/usbc.h>
```

若带有下述选项的 5 V、100 mA 供电足以让受电方（Sink）工作，则 policy_cb_get_rdo 可以返回此请求数据对象（Request Data Object，RDO）值。

请求数据对象（RDO）采用以下配置：

- 最大工作电流（Maximum Operating Current）：100 mA。
- 工作电流（Operating Current）：100 mA。
- 不支持非分块扩展消息（Unchunked Extended Messages）。
- 不允许 USB 挂起（No USB Suspend）。
- 不具备 USB 通信能力（USB Communications Capable）。
- 无能力不匹配（Capability Mismatch）。
- 不执行功率回退（GiveBack）。
- 对象位置（Object Position）：1，即 5 V 电源数据对象（PDO）。

<a id="gafea882f4f3cc96c502d53a24a3e5aec5"></a>

### `usbc_policy_check_t`

```c
enum usbc_policy_check_t
```

```c
#include <zephyr/usb_c/usbc.h>
```

设备策略管理器检查（Device Policy Manager Checks）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `CHECK_POWER_ROLE_SWAP` | 检查是否允许电源角色交换（Power Role Swap）。 |
| `CHECK_DATA_ROLE_SWAP_TO_DFP` | 检查是否允许将数据角色交换（Data Role Swap）为下行端口（DFP）。 |
| `CHECK_DATA_ROLE_SWAP_TO_UFP` | 检查是否允许将数据角色交换（Data Role Swap）为上行端口（UFP）。 |
| `CHECK_SNK_AT_DEFAULT_LEVEL` | 检查受电端（Sink）是否处于默认电平（Default Level）。 |
| `CHECK_VCONN_CONTROL` | 检查是否应控制 VCONN。 |
| `CHECK_SRC_PS_AT_DEFAULT_LEVEL` | 检查供电端电源（Source Power Supply）是否处于默认电平（Default Level）。 |

<a id="ga66f934a5c5cd88b574c71d1f18fbda23"></a>

### `usbc_policy_notify_t`

```c
enum usbc_policy_notify_t
```

```c
#include <zephyr/usb_c/usbc.h>
```

设备策略管理器通知（Device Policy Manager Notifications）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MSG_ACCEPT_RECEIVED` | 收到电力传输接受消息（Power Delivery Accept Message）。 |
| `MSG_REJECTED_RECEIVED` | 收到电力传输拒绝消息（Power Delivery Reject Message）。 |
| `MSG_DISCARDED` | 电力传输（Power Delivery）丢弃了正在发送的消息。 |
| `MSG_NOT_SUPPORTED_RECEIVED` | 收到电力传输不支持消息（Power Delivery Not Supported Message）。 |
| `DATA_ROLE_IS_UFP` | 数据角色（Data Role）已设为上行端口（Upstream Facing Port，UFP）。 |
| `DATA_ROLE_IS_DFP` | 数据角色（Data Role）已设为下行端口（Downstream Facing Port，DFP）。 |
| `POWER_ROLE_IS_SOURCE` | 电源角色（Power Role）已设为供电端（Source）。 |
| `POWER_ROLE_IS_SINK` | 电源角色（Power Role）已设为受电端（Sink）。 |
| `PD_CONNECTED` | 已建立 PD 显式契约（PD Explicit Contract）。 |
| `NOT_PD_CONNECTED` | 尚未建立 PD 显式契约（PD Explicit Contract）。 |
| `TRANSITION_PS` | 切换电源供电状态（Transition the Power Supply）。 |
| `PORT_PARTNER_NOT_RESPONSIVE` | 端口伙伴（Port Partner）未响应。 |
| `PROTOCOL_ERROR` | 发生协议错误（Protocol Error）。 |
| `SNK_TRANSITION_TO_DEFAULT` | 将受电端（Sink）切换到默认状态。 |
| `HARD_RESET_RECEIVED` | 收到硬复位（Hard Reset）。 |
| `POWER_CHANGE_0A0` | 受电端子电源状态（Sink SubPower State）：0 V。 |
| `POWER_CHANGE_DEF` | 受电端子电源状态（Sink SubPower State）：5 V／500 mA。 |
| `POWER_CHANGE_1A5` | 受电端子电源状态（Sink SubPower State）：5 V／1.5 A。 |
| `POWER_CHANGE_3A0` | 受电端子电源状态（Sink SubPower State）：5 V／3 A。 |
| `SENDER_RESPONSE_TIMEOUT` | 发送方响应超时（Sender Response Timeout）。 |
| `SOURCE_CAPABILITIES_RECEIVED` | 收到供电端能力（Source Capabilities）。 |

<a id="ga38a301a97a5e1a85e9836bbf083859f3"></a>

### `usbc_policy_request_t`

```c
enum usbc_policy_request_t
```

```c
#include <zephyr/usb_c/usbc.h>
```

设备策略管理器请求（Device Policy Manager Requests）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `REQUEST_NOP` | 无请求（No Request）。 |
| `REQUEST_TC_DISABLED` | 请求 Type-C 层切换到禁用状态（Disabled State）。 |
| `REQUEST_TC_ERROR_RECOVERY` | 请求 Type-C 层切换到错误恢复状态（Error Recovery State）。 |
| `REQUEST_TC_END` | Type-C 请求（Requests）的结束标记。 |
| `REQUEST_PE_DR_SWAP` | 请求策略引擎层（Policy Engine Layer）执行数据角色交换（Data Role Swap）。 |
| `REQUEST_PE_HARD_RESET_SEND` | 请求策略引擎层（Policy Engine Layer）发送硬复位（Hard Reset）。 |
| `REQUEST_PE_SOFT_RESET_SEND` | 请求策略引擎层（Policy Engine Layer）发送软复位（Soft Reset）。 |
| `REQUEST_PE_GET_SRC_CAPS` | 请求策略引擎层（Policy Engine Layer）从端口伙伴（Port Partner）获取供电端能力（Source Capabilities）。 |
| `REQUEST_GET_SNK_CAPS` | 请求策略引擎（Policy Engine）从端口伙伴（Port Partner）获取受电端能力（Sink Capabilities）。 |
| `REQUEST_PE_GOTO_MIN` | 请求策略引擎（Policy Engine）要求端口伙伴（Port Partner）提供最小功率（Minimum Power）。 |

<a id="gadf5d2934b5dc8e2b01d20bb904988784"></a>

### `usbc_policy_wait_t`

```c
enum usbc_policy_wait_t
```

```c
#include <zephyr/usb_c/usbc.h>
```

设备策略管理器等待消息通知（Device Policy Manager Wait Message Notifications）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `WAIT_SINK_REQUEST` | 端口伙伴（Port Partner）当前无法满足受电端请求（Sink Request）。 |
| `WAIT_POWER_ROLE_SWAP` | 端口伙伴（Port Partner）当前无法执行电源角色交换（Power Role Swap）。 |
| `WAIT_DATA_ROLE_SWAP` | 端口伙伴（Port Partner）当前无法执行数据角色交换（Data Role Swap）。 |
| `WAIT_VCONN_SWAP` | 端口伙伴（Port Partner）当前无法执行 VCONN 交换（VCONN Swap）。 |

<a id="ga4c4f0592a034b4e49eee85e95af33f94"></a>

### `usbc_snk_req_reply_t`

```c
enum usbc_snk_req_reply_t
```

```c
#include <zephyr/usb_c/usbc.h>
```

设备策略管理器对受电方请求（Sink Request）的响应。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SNK_REQUEST_VALID` | 能够满足受电端端口伙伴（Sink Port Partner）的请求。 |
| `SNK_REQUEST_REJECT` | 无法满足受电端端口伙伴（Sink Port Partner）的请求。 |
| `SNK_REQUEST_WAIT` | 稍后能够满足受电端端口伙伴（Sink Port Partner）的请求。 |

<a id="gabd99b6926baf67212d65c4a4d147ce5b"></a>

### `usbc_get_dpm_data()`

```c
void * usbc_get_dpm_data ( const struct device * dev)
```

```c
#include <zephyr/usb_c/usbc.h>
```

获取设备策略管理器（Device Policy Manager，DPM）数据的指针。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 运行时设备结构体（runtime device structure）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `NULL` | 尚未设置设备策略管理器数据（DPM Data）时。 |

**返回（Returns）**：返回值（Returns）：指向通过 `usbc_set_dpm_data` 设置的设备策略管理器数据（DPM Data）的指针。

<a id="ga42691b0bb2b4be50147ac655e2cd9761"></a>

### `usbc_request()`

```c
int usbc_request ( const struct device * dev, const enum usbc_policy_request_t req )
```

```c
#include <zephyr/usb_c/usbc.h>
```

向 USB-C 子系统（Subsystem）提出请求。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 运行时设备结构体（runtime device structure）。 |
| `req` | 请求（Request）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |

<a id="ga997007cab2e54ad53b774b4215d0f593"></a>

### `usbc_set_dpm_data()`

```c
void usbc_set_dpm_data ( const struct device * dev, void * dpm_data )
```

```c
#include <zephyr/usb_c/usbc.h>
```

设置设备策略管理器（Device Policy Manager，DPM）数据的指针。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 运行时设备结构体（runtime device structure）。 |
| `dpm_data` | 指向设备策略管理器数据（DPM Data）的指针。 |

<a id="gaa8f89bfb1e9a1840b2d61ebaa13aeb2f"></a>

### `usbc_set_policy_cb_change_src_caps()`

```c
void usbc_set_policy_cb_change_src_caps ( const struct device * dev, const policy_cb_change_src_caps_t cb )
```

```c
#include <zephyr/usb_c/usbc.h>
```

设置用于请求向受电方发送另一组供电能力（Source Caps）的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | USB-C 连接器实例（Connector Instance）。 |
| `cb` | 回调（Callback）。 |

<a id="ga67a046b411134d7c631942ae6ba73fc5"></a>

### `usbc_set_policy_cb_check()`

```c
void usbc_set_policy_cb_check ( const struct device * dev, const policy_cb_check_t cb )
```

```c
#include <zephyr/usb_c/usbc.h>
```

设置用于检查策略（Policy）的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 运行时设备结构体（runtime device structure）。 |
| `cb` | 回调（Callback）。 |

<a id="ga7f85188cc4f1a95350195abd0d736ada"></a>

### `usbc_set_policy_cb_check_sink_request()`

```c
void usbc_set_policy_cb_check_sink_request ( const struct device * dev, const policy_cb_check_sink_request_t cb )
```

```c
#include <zephyr/usb_c/usbc.h>
```

设置用于检查受电方请求（Sink Request）是否有效的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | USB-C 连接器实例（Connector Instance）。 |
| `cb` | 回调（Callback）。 |

<a id="ga7c1ffea81f71416ab2942fc5a5b67d41"></a>

### `usbc_set_policy_cb_get_rdo()`

```c
void usbc_set_policy_cb_get_rdo ( const struct device * dev, const policy_cb_get_rdo_t cb )
```

```c
#include <zephyr/usb_c/usbc.h>
```

设置用于获取请求数据对象（Request Data Object，RDO）的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 运行时设备结构体（runtime device structure）。 |
| `cb` | 回调（Callback）。 |

<a id="gafbd2885d758aa869635041fa89750596"></a>

### `usbc_set_policy_cb_get_snk_cap()`

```c
void usbc_set_policy_cb_get_snk_cap ( const struct device * dev, const policy_cb_get_snk_cap_t cb )
```

```c
#include <zephyr/usb_c/usbc.h>
```

设置用于获取受电方能力（Sink Capabilities）的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 运行时设备结构体（runtime device structure）。 |
| `cb` | 回调（Callback）。 |

<a id="ga7800c065ae5cfb7a95b58865d47c7f04"></a>

### `usbc_set_policy_cb_get_src_caps()`

```c
void usbc_set_policy_cb_get_src_caps ( const struct device * dev, const policy_cb_get_src_caps_t cb )
```

```c
#include <zephyr/usb_c/usbc.h>
```

设置用于从设备策略管理器获取供电方能力（Source Capabilities）的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | USB-C 连接器实例（Connector Instance）。 |
| `cb` | 回调（Callback）。 |

<a id="ga8974f9661dfebf8f686d677f999d5957"></a>

### `usbc_set_policy_cb_get_src_rp()`

```c
void usbc_set_policy_cb_get_src_rp ( const struct device * dev, const policy_cb_get_src_rp_t cb )
```

```c
#include <zephyr/usb_c/usbc.h>
```

设置用于获取应施加在配置通道（CC）线上的 Rp 值的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | USB-C 连接器实例（Connector Instance）。 |
| `cb` | 回调（Callback）。 |

<a id="gaf25c9cc2b6c514b9dcddc8129a76ccee"></a>

### `usbc_set_policy_cb_is_ps_ready()`

```c
void usbc_set_policy_cb_is_ps_ready ( const struct device * dev, const policy_cb_is_ps_ready_t cb )
```

```c
#include <zephyr/usb_c/usbc.h>
```

设置用于检查供电方电源（Source Power Supply）是否就绪的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | USB-C 连接器实例（Connector Instance）。 |
| `cb` | 回调（Callback）。 |

<a id="gaffa045ee6e2fbc07fde7e84e44d3853f"></a>

### `usbc_set_policy_cb_is_snk_at_default()`

```c
void usbc_set_policy_cb_is_snk_at_default ( const struct device * dev, const policy_cb_is_snk_at_default_t cb )
```

```c
#include <zephyr/usb_c/usbc.h>
```

设置用于检查受电方电源是否处于默认级别（Default Level）的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 运行时设备结构体（runtime device structure）。 |
| `cb` | 回调（Callback）。 |

<a id="gaedec1b4ad7b028ad18e1bcbe5396f1ee"></a>

### `usbc_set_policy_cb_notify()`

```c
void usbc_set_policy_cb_notify ( const struct device * dev, const policy_cb_notify_t cb )
```

```c
#include <zephyr/usb_c/usbc.h>
```

设置用于向设备策略管理器通知策略变化（Policy Change）的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 运行时设备结构体（runtime device structure）。 |
| `cb` | 回调（Callback）。 |

<a id="ga5b4adb4330dfadf127d0a01253d722bb"></a>

### `usbc_set_policy_cb_present_contract_is_valid()`

```c
void usbc_set_policy_cb_present_contract_is_valid ( const struct device * dev, const policy_cb_present_contract_is_valid_t cb )
```

```c
#include <zephyr/usb_c/usbc.h>
```

设置用于检查当前供电协定（Contract）是否仍有效的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | USB-C 连接器实例（Connector Instance）。 |
| `cb` | 回调（Callback）。 |

<a id="gafd0a407558bb92dc8b7007d9d717b940"></a>

### `usbc_set_policy_cb_set_port_partner_snk_cap()`

```c
void usbc_set_policy_cb_set_port_partner_snk_cap ( const struct device * dev, const policy_cb_set_port_partner_snk_cap_t cb )
```

```c
#include <zephyr/usb_c/usbc.h>
```

设置用于存储从受电端口伙伴（Sink Port Partner）收到的能力（Capabilities）的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | USB-C 连接器实例（Connector Instance）。 |
| `cb` | 回调（Callback）。 |

<a id="ga4536f47082f58f49d492de6f2b00dd17"></a>

### `usbc_set_policy_cb_set_src_cap()`

```c
void usbc_set_policy_cb_set_src_cap ( const struct device * dev, const policy_cb_set_src_cap_t cb )
```

```c
#include <zephyr/usb_c/usbc.h>
```

设置用于存储已接收的端口伙伴供电能力（Port Partner's Source Capabilities）的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 运行时设备结构体（runtime device structure）。 |
| `cb` | 回调（Callback）。 |

<a id="gaf5332ba0c87ff737e1c476d7be071fec"></a>

### `usbc_set_policy_cb_src_en()`

```c
void usbc_set_policy_cb_src_en ( const struct device * dev, const policy_cb_src_en_t cb )
```

```c
#include <zephyr/usb_c/usbc.h>
```

设置用于启用 VBUS 的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | USB-C 连接器实例（Connector Instance）。 |
| `cb` | 回调（Callback）。 |

<a id="gaa295593c7d5ede31328efaaab38b5880"></a>

### `usbc_set_policy_cb_wait_notify()`

```c
void usbc_set_policy_cb_wait_notify ( const struct device * dev, const policy_cb_wait_notify_t cb )
```

```c
#include <zephyr/usb_c/usbc.h>
```

设置用于向设备策略管理器通知已收到 WAIT 消息的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 运行时设备结构体（runtime device structure）。 |
| `cb` | 回调（Callback）。 |

<a id="ga9846b36061453023e16c160f5f120159"></a>

### `usbc_set_vconn_control_cb()`

```c
void usbc_set_vconn_control_cb ( const struct device * dev, const tcpc_vconn_control_cb_t cb )
```

```c
#include <zephyr/usb_c/usbc.h>
```

设置用于配置 VCONN 控制（Control）的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 运行时设备结构体（runtime device structure）。 |
| `cb` | VCONN 控制回调（VCONN Control Callback）。 |

<a id="ga8741df33b5432d9c7d5902af9bd67084"></a>

### `usbc_set_vconn_discharge_cb()`

```c
void usbc_set_vconn_discharge_cb ( const struct device * dev, const tcpc_vconn_discharge_cb_t cb )
```

```c
#include <zephyr/usb_c/usbc.h>
```

设置用于 VCONN 放电（Discharge）的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 运行时设备结构体（runtime device structure）。 |
| `cb` | VCONN 放电回调（VCONN Discharge Callback）。 |

<a id="ga1535f7f53b3cc859ff536883fd631830"></a>

### `usbc_start()`

```c
int usbc_start ( const struct device * dev)
```

```c
#include <zephyr/usb_c/usbc.h>
```

启动 USB-C 子系统（Subsystem）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 运行时设备结构体（runtime device structure）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |

<a id="ga68b73c03a5098a21260b5c3638edc973"></a>

### `usbc_suspend()`

```c
int usbc_suspend ( const struct device * dev)
```

```c
#include <zephyr/usb_c/usbc.h>
```

挂起 USB-C 子系统（Suspend Subsystem）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 运行时设备结构体（runtime device structure）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |


## 1.7\_原页交叉引用（Cross References）

- [受电端回调（Sink Callbacks）](../api_power_policy_topic_reference/P010_受电端回调（Sink Callbacks）.md)
- [供电端回调（Source Callbacks）](../api_input_runtime_topic_reference/P018_供电端回调（Source Callbacks）.md)
- [usbc.h](../api_file_clock_network_reference/P027_zephyr__usb_c__usbc.h_文件参考.md)
- [device](../device_reference/P002_设备对象结构.md)
- [tcpc_vconn_control_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga073ad4a46a5ea1f9e5cad45488d672f0)
- [tcpc_vconn_discharge_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga4d2b77f6ee685d1bff1117843150e664)
- [policy_cb_check_t](../api_power_policy_topic_reference/P010_受电端回调（Sink Callbacks）.md#ga2aacd704d08a8cecbf818150e8ec51b6)
- [policy_cb_notify_t](../api_power_policy_topic_reference/P010_受电端回调（Sink Callbacks）.md#ga44af668d9c22e757983c803d7b8ff82e)
- [policy_cb_wait_notify_t](../api_power_policy_topic_reference/P010_受电端回调（Sink Callbacks）.md#gaea62016b263dfaf5f869dd6ea036fdad)
- [policy_cb_get_snk_cap_t](../api_power_policy_topic_reference/P010_受电端回调（Sink Callbacks）.md#gaaed0161142c3481ce9180015b6968357)
- [policy_cb_set_src_cap_t](../api_power_policy_topic_reference/P010_受电端回调（Sink Callbacks）.md#ga6096d6909698f1b86a1a9cbd1f8d4097)
- [policy_cb_get_rdo_t](../api_power_policy_topic_reference/P010_受电端回调（Sink Callbacks）.md#gae0448c6b271273c5db59775c3a6260dc)
- [policy_cb_is_snk_at_default_t](../api_power_policy_topic_reference/P010_受电端回调（Sink Callbacks）.md#ga1a3da6faad509213f607893fef16b673)
- [policy_cb_get_src_rp_t](../api_input_runtime_topic_reference/P018_供电端回调（Source Callbacks）.md#ga7c75f8192001179f20bf1fe48316f3c6)
- [policy_cb_src_en_t](../api_input_runtime_topic_reference/P018_供电端回调（Source Callbacks）.md#gaaecac7683d7092c0a477e8d9ca0e5a33)
- [policy_cb_get_src_caps_t](../api_input_runtime_topic_reference/P018_供电端回调（Source Callbacks）.md#ga4bbf78bd752d38d915412dd942d3aab8)
- [policy_cb_check_sink_request_t](../api_input_runtime_topic_reference/P018_供电端回调（Source Callbacks）.md#gaeeda677224456f685137e4b345c0e173)
- [policy_cb_is_ps_ready_t](../api_input_runtime_topic_reference/P018_供电端回调（Source Callbacks）.md#gae7391e858485e44a74e5fcdbb7931ca7)
- [policy_cb_present_contract_is_valid_t](../api_input_runtime_topic_reference/P018_供电端回调（Source Callbacks）.md#ga2925e462140a700920251d92ae5a3aa4)
- [policy_cb_change_src_caps_t](../api_input_runtime_topic_reference/P018_供电端回调（Source Callbacks）.md#ga699811c862990b31ec0126dd3a4c3e4d)
- [policy_cb_set_port_partner_snk_cap_t](../api_input_runtime_topic_reference/P018_供电端回调（Source Callbacks）.md#gae903c8108e8d1563cb0b1ccdd901c925)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggafea882f4f3cc96c502d53a24a3e5aec5a1181a470497b797136cf0eb204394106"></a>
<a id="ggafea882f4f3cc96c502d53a24a3e5aec5afa602e00bf418656e365baa4d9ff6cef"></a>
<a id="ggafea882f4f3cc96c502d53a24a3e5aec5a7c97208a8a12f70e7ffa43bb406b9ebd"></a>
<a id="ggafea882f4f3cc96c502d53a24a3e5aec5a17f7f4fc9aa4178f0358769dedd29ade"></a>
<a id="ggafea882f4f3cc96c502d53a24a3e5aec5a655e913c86db5caa961083dad9f6b7a1"></a>
<a id="ggafea882f4f3cc96c502d53a24a3e5aec5a42b660bb630edcca5ae8b031033d0718"></a>
<a id="gga66f934a5c5cd88b574c71d1f18fbda23a43bc56906b5dc4767d3297400053d286"></a>
<a id="gga66f934a5c5cd88b574c71d1f18fbda23a4ad0620e76c694004d3a1b43458a14b2"></a>
<a id="gga66f934a5c5cd88b574c71d1f18fbda23aa316636e8353dad1a9d5dec8b85a67e4"></a>
<a id="gga66f934a5c5cd88b574c71d1f18fbda23ab2f97ffaa13c84e656f7ac0004ec86ae"></a>
<a id="gga66f934a5c5cd88b574c71d1f18fbda23a4020203569dcb95ab1b3d2946efced19"></a>
<a id="gga66f934a5c5cd88b574c71d1f18fbda23a791604f4f0b2a2c3ccea4e98d1659a61"></a>
<a id="gga66f934a5c5cd88b574c71d1f18fbda23a75abb66ae57bb7ad946b8c3c2734f445"></a>
<a id="gga66f934a5c5cd88b574c71d1f18fbda23ae0372eb6238d86c3cfb2a10764180451"></a>
<a id="gga66f934a5c5cd88b574c71d1f18fbda23adbefad204068244fdf75ba1ff211fbfc"></a>
<a id="gga66f934a5c5cd88b574c71d1f18fbda23adebcbf5155b43ce562127d4077d46d7d"></a>
<a id="gga66f934a5c5cd88b574c71d1f18fbda23a3a27b8e70ffe5788aa3ffea1bf61cae9"></a>
<a id="gga66f934a5c5cd88b574c71d1f18fbda23ad52e1c4f949bb64fef1d996ac2f4e0de"></a>
<a id="gga66f934a5c5cd88b574c71d1f18fbda23a8cb937247ec21f791706f4f426496a8c"></a>
<a id="gga66f934a5c5cd88b574c71d1f18fbda23aa02158d0afdd60c755453977200dfb28"></a>
<a id="gga66f934a5c5cd88b574c71d1f18fbda23ab74f5bcaa94a5fb1e46cdd7c6a5d822f"></a>
<a id="gga66f934a5c5cd88b574c71d1f18fbda23a0fb0676a11ad8bad2d5249031ba5fd19"></a>
<a id="gga66f934a5c5cd88b574c71d1f18fbda23a3a50be6f70c1a7abd724ab447491c46a"></a>
<a id="gga66f934a5c5cd88b574c71d1f18fbda23a336bfb983c4d07684d67d4d9ef6c1489"></a>
<a id="gga66f934a5c5cd88b574c71d1f18fbda23a3477c1c6ad8885c3ab7a9c58b7399dcf"></a>
<a id="gga66f934a5c5cd88b574c71d1f18fbda23ac22b0026881f65c574d0bf7454321745"></a>
<a id="gga66f934a5c5cd88b574c71d1f18fbda23a0266a21d8c836cf281c30542eb6badd4"></a>
<a id="gga38a301a97a5e1a85e9836bbf083859f3a2274197ac367b3da6358cac8dd781134"></a>
<a id="gga38a301a97a5e1a85e9836bbf083859f3a899633a1b63b1c3a826b5556f0f23d8b"></a>
<a id="gga38a301a97a5e1a85e9836bbf083859f3a8a7b77d81428f0c4784af3204f33b290"></a>
<a id="gga38a301a97a5e1a85e9836bbf083859f3a0c5ff3bc4c0d6f636663fd3911ed85d5"></a>
<a id="gga38a301a97a5e1a85e9836bbf083859f3a1fe9f57fac7f5149fe5f0f7c42523536"></a>
<a id="gga38a301a97a5e1a85e9836bbf083859f3a7c3c9c959439ee73539cff13e561c403"></a>
<a id="gga38a301a97a5e1a85e9836bbf083859f3ad45120b1ceabeb054c2c2273b8431894"></a>
<a id="gga38a301a97a5e1a85e9836bbf083859f3a8c6083028ee8655cd0bebb6d9aab2e1e"></a>
<a id="gga38a301a97a5e1a85e9836bbf083859f3ade1edc3aef0e4d563934edbc9ce784bc"></a>
<a id="gga38a301a97a5e1a85e9836bbf083859f3ae5b4eb0db00e81a98cfe2436b64a7018"></a>
<a id="ggadf5d2934b5dc8e2b01d20bb904988784a009ce2ceacd92db88d9a6beb01f84a28"></a>
<a id="ggadf5d2934b5dc8e2b01d20bb904988784a91f1f41bf9318e06c02c1957a39a762a"></a>
<a id="ggadf5d2934b5dc8e2b01d20bb904988784ae5ef03f78d78a7014404c581bad77c18"></a>
<a id="ggadf5d2934b5dc8e2b01d20bb904988784aa982aed81f39e35cde74399c6d74e601"></a>
<a id="gga4c4f0592a034b4e49eee85e95af33f94a7922edb67afe83596819994a71de76dd"></a>
<a id="gga4c4f0592a034b4e49eee85e95af33f94a714f82e830f9528a8200c2c14795b282"></a>
<a id="gga4c4f0592a034b4e49eee85e95af33f94a7ae46f6deb593eedd0564d30cb4c75fb"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_设备地址（Device Address）.md)
