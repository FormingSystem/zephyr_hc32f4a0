---
id: learning.zephyr-docs.api-socket-lora-topic-reference.page-10
title: LoRaWAN API API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_LoRaWAN API API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

起始版本（Since）：2.5。版本（Version）：0.2.0。

<a id="header-files"></a>
<a id="files"></a>

## 10.1\_文件（Files）

<a id="r_emul_2Eh"></a>

```c
file emul.h
```

相关声明：[emul.h](../api_file_service_interface_reference/P034_zephyr__lorawan__emul.h_文件参考.md)。

LoRaWAN仿真器后端（Emulator Backend）API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 10.2\_数据结构（Data Structures）

<a id="r_lorawan_5Fjoin_5Fotaa"></a>

```c
struct lorawan_join_otaa
```

相关声明：[lorawan_join_otaa](../modem_wireless_model_reference/P034_lorawan_join_otaa_结构体.md)。

空中激活（Over-the-Air Activation，OTAA）方式的LoRaWAN入网参数。

<a id="r_lorawan_5Fjoin_5Fabp"></a>

```c
struct lorawan_join_abp
```

相关声明：[lorawan_join_abp](../modem_wireless_model_reference/P032_lorawan_join_abp_结构体.md)。

个性化激活（Activation by Personalization，ABP）方式的LoRaWAN入网参数。

<a id="r_lorawan_5Fjoin_5Fconfig"></a>

```c
struct lorawan_join_config
```

相关声明：[lorawan_join_config](../modem_wireless_model_reference/P033_lorawan_join_config_结构体.md)。

LoRaWAN入网参数（Join Parameters）。

<a id="r_lorawan_5Fdownlink_5Fcb"></a>

```c
struct lorawan_downlink_cb
```

相关声明：[lorawan_downlink_cb](../modem_wireless_model_reference/P031_lorawan_downlink_cb_结构体.md)。

LoRaWAN下行链路（Downlink）的回调参数。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 10.3\_宏定义（Macros）

<a id="r_ga83dbf2575eaae85f1837567e9fb729a4"></a>

```c
#define LW_RECV_PORT_ANY UINT16_MAX
```

相关声明：[LW_RECV_PORT_ANY](#ga83dbf2575eaae85f1837567e9fb729a4)、[UINT16_MAX](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3ea490c9b3617d4479bd80ef93cd5602)。

表示在任意端口接收（Receiving on Any Port）的标志。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 10.4\_类型定义（Typedefs）

<a id="r_ga17a7a2e1dbfa19b9f7e18a81be5514dd"></a>

```c
typedef uint8_t(* lorawan_battery_level_cb_t) (void)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[lorawan_battery_level_cb_t](#ga17a7a2e1dbfa19b9f7e18a81be5514dd)。

定义电池电量回调处理函数签名（Battery Level Callback Handler Function Signature）。

<a id="r_ga87a8d911f1c825bcf8c77ada568f3ed4"></a>

```c
typedef void(* lorawan_dr_changed_cb_t) (enum lorawan_datarate dr)
```

相关声明：[lorawan_dr_changed_cb_t](#ga87a8d911f1c825bcf8c77ada568f3ed4)、[lorawan_datarate](#ga276e66fb8ce88f853d1987686e31fc86)。

定义数据速率变化回调处理函数签名（Datarate Changed Callback Handler Function Signature）。

<a id="r_gaf9fad3b2bb93ab43751098f4b8dd31f9"></a>

```c
typedef void(* lorawan_link_check_ans_cb_t) (uint8_t demod_margin, uint8_t nb_gateways)
```

相关声明：[lorawan_link_check_ans_cb_t](#gaf9fad3b2bb93ab43751098f4b8dd31f9)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

定义链路检查应答处理函数签名（Link Check Answer Handler Function Signature）。

<a id="r_gade697fcc14a384420afc8817f72af410"></a>

```c
typedef int(* transport_descriptor_cb) (uint32_t descriptor)
```

相关声明：[transport_descriptor_cb](#gade697fcc14a384420afc8817f72af410)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

定义用户描述符回调处理函数签名（User's Descriptor Callback Handler Function Signature）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 10.5\_枚举（Enumerations）

<a id="r_ga88b65799c3f1d98fbce80927218c0837"></a>

```c
enum lorawan_class { LORAWAN_CLASS_A = 0x00 , LORAWAN_CLASS_B = 0x01 , LORAWAN_CLASS_C = 0x02 }
```

相关声明：[lorawan_class](#ga88b65799c3f1d98fbce80927218c0837)、[LORAWAN_CLASS_A](#gga88b65799c3f1d98fbce80927218c0837a538e56348e6d5b506e661e3af18aee6c)、[LORAWAN_CLASS_B](#gga88b65799c3f1d98fbce80927218c0837a79a9c205ac583051b2e072389491c7cb)、[LORAWAN_CLASS_C](#gga88b65799c3f1d98fbce80927218c0837ad158a1985688bbe54b20a8a808774547)。

LoRaWAN 设备类别类型（Class Types）。

<a id="r_ga2bf50442214ecdc717f1a24dc058a338"></a>

```c
enum lorawan_act_type { LORAWAN_ACT_OTAA = 0 , LORAWAN_ACT_ABP }
```

相关声明：[lorawan_act_type](#ga2bf50442214ecdc717f1a24dc058a338)、[LORAWAN_ACT_OTAA](#gga2bf50442214ecdc717f1a24dc058a338a5f262e334bc46278bec491cd022b612a)、[LORAWAN_ACT_ABP](#gga2bf50442214ecdc717f1a24dc058a338a13bb2a28232081844e36308977ec6701)。

LoRaWAN 激活类型（Activation Types）。

<a id="r_ga0635d19612db9009775eae8e527d4897"></a>

```c
enum lorawan_channels_mask_size { LORAWAN_CHANNELS_MASK_SIZE_AS923 = 1 , LORAWAN_CHANNELS_MASK_SIZE_AU915 = 6 , LORAWAN_CHANNELS_MASK_SIZE_CN470 = 6 , LORAWAN_CHANNELS_MASK_SIZE_CN779 = 1 , LORAWAN_CHANNELS_MASK_SIZE_EU433 = 1 , LORAWAN_CHANNELS_MASK_SIZE_EU868 = 1 , LORAWAN_CHANNELS_MASK_SIZE_KR920 = 1 , LORAWAN_CHANNELS_MASK_SIZE_IN865 = 1 , LORAWAN_CHANNELS_MASK_SIZE_US915 = 6 , LORAWAN_CHANNELS_MASK_SIZE_RU864 = 1 }
```

相关声明：[lorawan_channels_mask_size](#ga0635d19612db9009775eae8e527d4897)、[LORAWAN_CHANNELS_MASK_SIZE_AS923](#gga0635d19612db9009775eae8e527d4897a577c304c4c1998916203e9ec7ae6e1be)、[LORAWAN_CHANNELS_MASK_SIZE_AU915](#gga0635d19612db9009775eae8e527d4897a1bc4cacfd02a630226f629ed61f4e1ca)、[LORAWAN_CHANNELS_MASK_SIZE_CN470](#gga0635d19612db9009775eae8e527d4897a2bdaecd6f1f853cd370ba89b465a9ee1)、[LORAWAN_CHANNELS_MASK_SIZE_CN779](#gga0635d19612db9009775eae8e527d4897a8f2f25b3ab1167f69aa594a034b27180)、[LORAWAN_CHANNELS_MASK_SIZE_EU433](#gga0635d19612db9009775eae8e527d4897a3b7968012bf2c8fa7adef454fc33124a)、[LORAWAN_CHANNELS_MASK_SIZE_EU868](#gga0635d19612db9009775eae8e527d4897a3bc215c41b7fb5652c6729756b8f979a)、[LORAWAN_CHANNELS_MASK_SIZE_KR920](#gga0635d19612db9009775eae8e527d4897a7443e6adbaaf4f7cb2037d8f3e42d86a)、[LORAWAN_CHANNELS_MASK_SIZE_IN865](#gga0635d19612db9009775eae8e527d4897a9564d246e39448f478412861a3a87b7e)、[LORAWAN_CHANNELS_MASK_SIZE_US915](#gga0635d19612db9009775eae8e527d4897a054ebab376354c8a9e6a5f4e9f6f78ee)、[LORAWAN_CHANNELS_MASK_SIZE_RU864](#gga0635d19612db9009775eae8e527d4897aaa05e08a24aded2ada511fd2d1f4cebd)。

LoRaWAN 信道掩码大小（Channels Mask Sizes）。

<a id="r_ga276e66fb8ce88f853d1987686e31fc86"></a>

```c
enum lorawan_datarate { LORAWAN_DR_0 = 0 , LORAWAN_DR_1 , LORAWAN_DR_2 , LORAWAN_DR_3 , LORAWAN_DR_4 , LORAWAN_DR_5 , LORAWAN_DR_6 , LORAWAN_DR_7 , LORAWAN_DR_8 , LORAWAN_DR_9 , LORAWAN_DR_10 , LORAWAN_DR_11 , LORAWAN_DR_12 , LORAWAN_DR_13 , LORAWAN_DR_14 , LORAWAN_DR_15 }
```

相关声明：[lorawan_datarate](#ga276e66fb8ce88f853d1987686e31fc86)、[LORAWAN_DR_0](#gga276e66fb8ce88f853d1987686e31fc86a4b60b8eb52c07b40cbaaf94a4c56e1f6)、[LORAWAN_DR_1](#gga276e66fb8ce88f853d1987686e31fc86ade4655b32ca976c317fa9f44ac8b148a)、[LORAWAN_DR_2](#gga276e66fb8ce88f853d1987686e31fc86a941f8a603aeb54560be7125a55c74159)、[LORAWAN_DR_3](#gga276e66fb8ce88f853d1987686e31fc86a4ac565dbaae0c6ad4e62dc34ca0c013a)、[LORAWAN_DR_4](#gga276e66fb8ce88f853d1987686e31fc86a6f6cd4ecd247f67cad08ede84649a939)、[LORAWAN_DR_5](#gga276e66fb8ce88f853d1987686e31fc86a08f879f1054ca54e488180b07d7ff952)、[LORAWAN_DR_6](#gga276e66fb8ce88f853d1987686e31fc86acc624ccf8a9585889c3685217f56099f)、[LORAWAN_DR_7](#gga276e66fb8ce88f853d1987686e31fc86aac8afba95d7187f0829aae7abda894d5)、[LORAWAN_DR_8](#gga276e66fb8ce88f853d1987686e31fc86a080b31031f5a2b54d84ed49b133b0a86)、[LORAWAN_DR_9](#gga276e66fb8ce88f853d1987686e31fc86afbc8d04236410a6107cccfd71ba4bace)、[LORAWAN_DR_10](#gga276e66fb8ce88f853d1987686e31fc86a0a18193e15d268d262d58897d39993b3)、[LORAWAN_DR_11](#gga276e66fb8ce88f853d1987686e31fc86a2a631e746ffc5c4378e39b7a90dd44e2)、[LORAWAN_DR_12](#gga276e66fb8ce88f853d1987686e31fc86a0df057cf1505ba94876deaeddd515548)、[LORAWAN_DR_13](#gga276e66fb8ce88f853d1987686e31fc86a18bfd63ae262f992d9d12f8d56cc217e)、[LORAWAN_DR_14](#gga276e66fb8ce88f853d1987686e31fc86a1ad3be15c2e60d0bb2f3c12faf279efa)、[LORAWAN_DR_15](#gga276e66fb8ce88f853d1987686e31fc86a4738baf87e0cb2e64d9c525e40dd6e0a)。

LoRaWAN 数据速率类型（Datarate Types）。

<a id="r_gacb8efaa0761f8761146a0e913dcb627d"></a>

```c
enum lorawan_region { LORAWAN_REGION_AS923 , LORAWAN_REGION_AU915 , LORAWAN_REGION_CN470 , LORAWAN_REGION_CN779 , LORAWAN_REGION_EU433 , LORAWAN_REGION_EU868 , LORAWAN_REGION_KR920 , LORAWAN_REGION_IN865 , LORAWAN_REGION_US915 , LORAWAN_REGION_RU864 }
```

相关声明：[lorawan_region](#gacb8efaa0761f8761146a0e913dcb627d)、[LORAWAN_REGION_AS923](#ggacb8efaa0761f8761146a0e913dcb627da6a1ba05859d575a28095437436c8e6a6)、[LORAWAN_REGION_AU915](#ggacb8efaa0761f8761146a0e913dcb627da2744fe63701f5a5f23706b6f37672c70)、[LORAWAN_REGION_CN470](#ggacb8efaa0761f8761146a0e913dcb627da52d67181588c94d2a423040b4b5a1de4)、[LORAWAN_REGION_CN779](#ggacb8efaa0761f8761146a0e913dcb627dadb106a189c4c647e5e3af89cc753e0d8)、[LORAWAN_REGION_EU433](#ggacb8efaa0761f8761146a0e913dcb627dabcb9529d8f449bcb85a893fdd20f9180)、[LORAWAN_REGION_EU868](#ggacb8efaa0761f8761146a0e913dcb627da404530e5008260260131de051283f7ba)、[LORAWAN_REGION_KR920](#ggacb8efaa0761f8761146a0e913dcb627dafae64ea9dd2c2ee7e897fc0f94484da5)、[LORAWAN_REGION_IN865](#ggacb8efaa0761f8761146a0e913dcb627da9113b34d94da40149442f432fd97e86c)、[LORAWAN_REGION_US915](#ggacb8efaa0761f8761146a0e913dcb627da70e25dd006efc115617631f64cc34c88)、[LORAWAN_REGION_RU864](#ggacb8efaa0761f8761146a0e913dcb627dad30a636d45def6889e2b5cbf60f28c0e)。

LoRaWAN 区域类型（Region Types）。

<a id="r_ga5d78efba3f8e62ccd6317aed8af4bc54"></a>

```c
enum lorawan_message_type { LORAWAN_MSG_UNCONFIRMED = 0 , LORAWAN_MSG_CONFIRMED }
```

相关声明：[lorawan_message_type](#ga5d78efba3f8e62ccd6317aed8af4bc54)、[LORAWAN_MSG_UNCONFIRMED](#gga5d78efba3f8e62ccd6317aed8af4bc54a9855d8332363a554db9dde446cc409b7)、[LORAWAN_MSG_CONFIRMED](#gga5d78efba3f8e62ccd6317aed8af4bc54a40ee76ac8d0b40d06903fc06a7ef1989)。

LoRaWAN 消息类型（Message Types）。

<a id="r_gab28a9f22482069b2246892e4ee31660d"></a>

```c
enum lorawan_dl_flags { LORAWAN_DATA_PENDING = BIT(0) , LORAWAN_TIME_UPDATED = BIT(1) }
```

相关声明：[lorawan_dl_flags](#gab28a9f22482069b2246892e4ee31660d)、[LORAWAN_DATA_PENDING](#ggab28a9f22482069b2246892e4ee31660da01aee480c4308ac7abb6bf909478cce2)、[LORAWAN_TIME_UPDATED](#ggab28a9f22482069b2246892e4ee31660dad272f787e193c2397e1b670ced4ba1b8)。

LoRaWAN 下行标志（Downlink Flags）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 10.6\_函数（Functions）

<a id="r_ga9771704a8bcab778dd30653a0fbdeb2f"></a>

```c
void lorawan_register_battery_level_callback (lorawan_battery_level_cb_t cb)
```

相关声明：[lorawan_register_battery_level_callback](#ga9771704a8bcab778dd30653a0fbdeb2f)、[lorawan_battery_level_cb_t](#ga17a7a2e1dbfa19b9f7e18a81be5514dd)。

注册电池电量回调函数（Battery Level Callback Function）。

<a id="r_gab91f31477cd44e10692ca9d56d137ae2"></a>

```c
void lorawan_register_downlink_callback (struct lorawan_downlink_cb *cb)
```

相关声明：[lorawan_register_downlink_callback](#gab91f31477cd44e10692ca9d56d137ae2)、[lorawan_downlink_cb](../modem_wireless_model_reference/P031_lorawan_downlink_cb_结构体.md)。

注册收到下行数据包（Downlink Packets）时执行的回调。

<a id="r_ga505e8d27bc7bc029feb93bbe4982d329"></a>

```c
void lorawan_register_dr_changed_callback (lorawan_dr_changed_cb_t cb)
```

相关声明：[lorawan_register_dr_changed_callback](#ga505e8d27bc7bc029feb93bbe4982d329)、[lorawan_dr_changed_cb_t](#ga87a8d911f1c825bcf8c77ada568f3ed4)。

注册数据速率（Datarate）变化时调用的回调。

<a id="r_ga7b620841f521b9addc8d1ee823ee45fd"></a>

```c
void lorawan_register_link_check_ans_callback (lorawan_link_check_ans_cb_t cb)
```

相关声明：[lorawan_register_link_check_ans_callback](#ga7b620841f521b9addc8d1ee823ee45fd)、[lorawan_link_check_ans_cb_t](#gaf9fad3b2bb93ab43751098f4b8dd31f9)。

注册收到链路检查请求应答（Link Check Answer）时调用的回调。

<a id="r_ga5b2c7543c45801c9d0d7f46546771f17"></a>

```c
int lorawan_join (const struct lorawan_join_config *config)
```

相关声明：[lorawan_join](#ga5b2c7543c45801c9d0d7f46546771f17)、[lorawan_join_config](../modem_wireless_model_reference/P033_lorawan_join_config_结构体.md)。

加入 LoRaWAN 网络（Join Network）。

<a id="r_ga640d93930e09327ee87563597f919725"></a>

```c
int lorawan_start (void)
```

相关声明：[lorawan_start](#ga640d93930e09327ee87563597f919725)。

启动 LoRaWAN 协议栈（Stack）。

<a id="r_ga23758c3225e3ebf62bbe91b7589b67d7"></a>

```c
int lorawan_send (uint8_t port, uint8_t *data, uint8_t len, enum lorawan_message_type type)
```

相关声明：[lorawan_send](#ga23758c3225e3ebf62bbe91b7589b67d7)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[lorawan_message_type](#ga5d78efba3f8e62ccd6317aed8af4bc54)。

向 LoRaWAN 网络发送数据。

<a id="r_gab9768bad8d0c18410f6b8e946e89cbbe"></a>

```c
int lorawan_set_class (enum lorawan_class dev_class)
```

相关声明：[lorawan_set_class](#gab9768bad8d0c18410f6b8e946e89cbbe)、[lorawan_class](#ga88b65799c3f1d98fbce80927218c0837)。

设置当前设备类别（Device Class）。

<a id="r_ga14f9cb6a11c585f9ac4e9986735a82c3"></a>

```c
int lorawan_set_conf_msg_tries (uint8_t tries)
```

相关声明：[lorawan_set_conf_msg_tries](#ga14f9cb6a11c585f9ac4e9986735a82c3)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置发送尝试次数（Number of Tries）。

<a id="r_ga432929bd5911e04e57ef178b65e1beaa"></a>

```c
void lorawan_enable_adr (bool enable)
```

相关声明：[lorawan_enable_adr](#ga432929bd5911e04e57ef178b65e1beaa)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用自适应数据速率（Adaptive Data Rate，ADR）。

<a id="r_ga243c3200693ae9c81dea238068afc7dd"></a>

```c
int lorawan_set_channels_mask (uint16_t *channels_mask, size_t channels_mask_size)
```

相关声明：[lorawan_set_channels_mask](#ga243c3200693ae9c81dea238068afc7dd)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置信道掩码（Channels Mask）。

<a id="r_gaaa70ba5aa545b59233bc906948a4030d"></a>

```c
int lorawan_set_datarate (enum lorawan_datarate dr)
```

相关声明：[lorawan_set_datarate](#gaaa70ba5aa545b59233bc906948a4030d)、[lorawan_datarate](#ga276e66fb8ce88f853d1987686e31fc86)。

设置默认数据速率（Default Data Rate）。

<a id="r_ga6d1b45c5543473ff4fbcef473a8e0e35"></a>

```c
enum lorawan_datarate lorawan_get_min_datarate (void)
```

相关声明：[lorawan_datarate](#ga276e66fb8ce88f853d1987686e31fc86)、[lorawan_get_min_datarate](#ga6d1b45c5543473ff4fbcef473a8e0e35)。

获取可能的最低数据速率（Minimum Possible Datarate）。

<a id="r_ga94e3c282537618efae65e8ada1f88e81"></a>

```c
void lorawan_get_payload_sizes (uint8_t *max_next_payload_size, uint8_t *max_payload_size)
```

相关声明：[lorawan_get_payload_sizes](#ga94e3c282537618efae65e8ada1f88e81)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取当前负载大小（Payload Sizes）。

<a id="r_gaaf60e8b09d6f8d3a89aa2089c137fd3f"></a>

```c
int lorawan_set_region (enum lorawan_region region)
```

相关声明：[lorawan_set_region](#gaaf60e8b09d6f8d3a89aa2089c137fd3f)、[lorawan_region](#gacb8efaa0761f8761146a0e913dcb627d)。

设置要使用的区域（Region）和频率（Frequency）。

<a id="r_ga980f1650e9cceba19da453d4937273cb"></a>

```c
int lorawan_request_device_time (bool force_request)
```

相关声明：[lorawan_request_device_time](#ga980f1650e9cceba19da453d4937273cb)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

通过 DeviceTimeReq MAC 命令请求时间。

<a id="r_ga88c22a7e83437688039c05f9c7c1e7d4"></a>

```c
int lorawan_device_time_get (uint32_t *gps_time)
```

相关声明：[lorawan_device_time_get](#ga88c22a7e83437688039c05f9c7c1e7d4)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

从 LoRaWAN 协议栈获取当前时间，该时间由 MAC 层的 DeviceTimeAns 更新。

<a id="r_gaed19bb9c528f8f21104201fd0816e3a9"></a>

```c
int lorawan_request_link_check (bool force_request)
```

相关声明：[lorawan_request_link_check](#gaed19bb9c528f8f21104201fd0816e3a9)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

通过 LinkCheckReq MAC 命令请求链路检查（Link Check）。

<a id="r_ga1f87b0b04bb5e75623d63d82f6069207"></a>

```c
int lorawan_clock_sync_run (void)
```

相关声明：[lorawan_clock_sync_run](#ga1f87b0b04bb5e75623d63d82f6069207)。

运行应用层时钟同步服务（Application Layer Clock Synchronization Service）。

<a id="r_ga12afde687fb1081bc669f844e6ab7c92"></a>

```c
int lorawan_clock_sync_get (uint32_t *gps_time)
```

相关声明：[lorawan_clock_sync_get](#ga12afde687fb1081bc669f844e6ab7c92)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取当前同步时间（Synchronized Time）。

<a id="r_gab62274848abe7cd0f23fadefd185028b"></a>

```c
void lorawan_frag_transport_register_descriptor_callback (transport_descriptor_cb cb)
```

相关声明：[lorawan_frag_transport_register_descriptor_callback](#gab62274848abe7cd0f23fadefd185028b)、[transport_descriptor_cb](#gade697fcc14a384420afc8817f72af410)。

注册处理描述符的回调函数（Handle Descriptor Callback Function）。

<a id="r_ga55b5a10df7235d51a65b40032e5f6907"></a>

```c
int lorawan_frag_transport_run (void(*transport_finished_cb)(void))
```

相关声明：[lorawan_frag_transport_run](#ga55b5a10df7235d51a65b40032e5f6907)。

运行分片数据块传输服务（Fragmented Data Block Transport Service）。

## 10.7\_详细说明（Detailed Documentation）

<a id="ga83dbf2575eaae85f1837567e9fb729a4"></a>

### `LW_RECV_PORT_ANY`

```c
#define LW_RECV_PORT_ANY UINT16_MAX
```

```c
#include <zephyr/lorawan/lorawan.h>
```

表示在任意端口接收（Receiving on Any Port）的标志。

<a id="ga17a7a2e1dbfa19b9f7e18a81be5514dd"></a>

### `lorawan_battery_level_cb_t`

```c
typedef uint8_t(* lorawan_battery_level_cb_t) (void)
```

```c
#include <zephyr/lorawan/lorawan.h>
```

定义电池电量回调处理函数签名（Battery Level Callback Handler Function Signature）。

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 节点（Node）连接到外部电源（External Power Source）时。 |
| `1..254` | 电池电量（Battery Level），`1` 为最小值，`254` 为最大值。 |
| `255` | 节点（Node）无法测量电池电量（Battery Level）时。 |

<a id="ga87a8d911f1c825bcf8c77ada568f3ed4"></a>

### `lorawan_dr_changed_cb_t`

```c
typedef void(* lorawan_dr_changed_cb_t) (enum lorawan_datarate dr)
```

```c
#include <zephyr/lorawan/lorawan.h>
```

定义数据速率变化回调处理函数签名（Datarate Changed Callback Handler Function Signature）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dr` | 更新后的数据率（Data Rate）。 |

<a id="gaf9fad3b2bb93ab43751098f4b8dd31f9"></a>

### `lorawan_link_check_ans_cb_t`

```c
typedef void(* lorawan_link_check_ans_cb_t) (uint8_t demod_margin, uint8_t nb_gateways)
```

```c
#include <zephyr/lorawan/lorawan.h>
```

定义链路检查应答处理函数签名（Link Check Answer Handler Function Signature）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `demod_margin` | 解调裕量（Demodulation Margin），单位为 dB。 |
| `nb_gateways` | 设备连接的网关（Gateway）数量。 |

<a id="gade697fcc14a384420afc8817f72af410"></a>

### `transport_descriptor_cb`

```c
typedef int(* transport_descriptor_cb) (uint32_t descriptor)
```

```c
#include <zephyr/lorawan/lorawan.h>
```

定义用户描述符回调处理函数签名（User's Descriptor Callback Handler Function Signature）。

此回调为可选。启用分片数据块传输（Fragmented Data Block Transport）时，会使用 `FragSessionSetupReq` 命令中的描述符（Descriptor）字段通知应用程序。

描述符（Descriptor）的含义由应用程序决定。使用二进制镜像（Binary Image）执行空中固件升级（FUOTA）时，它可以表示所传输固件的版本。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `descriptor` | `FragSessionSetupReq` 命令中给出的描述符值（Descriptor Value）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`。如果描述符（Descriptor）表示固件版本，返回 `0` 意味着终端设备能够接收该二进制固件。否则返回负错误码（见 `errno.h`），指出失败原因。任何负错误码都会导致向网络服务器（Network Server）发送 `FragSessionSetupAns` 时，设置错误描述符（Wrong Descriptor）状态位掩码。

<a id="ga2bf50442214ecdc717f1a24dc058a338"></a>

### `lorawan_act_type`

```c
enum lorawan_act_type
```

```c
#include <zephyr/lorawan/lorawan.h>
```

LoRaWAN 激活类型（Activation Types）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `LORAWAN_ACT_OTAA` | 空中激活（Over-the-Air Activation，OTAA）。 |
| `LORAWAN_ACT_ABP` | 个性化激活（Activation by Personalization，ABP）。 |

<a id="ga0635d19612db9009775eae8e527d4897"></a>

### `lorawan_channels_mask_size`

```c
enum lorawan_channels_mask_size
```

```c
#include <zephyr/lorawan/lorawan.h>
```

LoRaWAN 信道掩码大小（Channels Mask Sizes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `LORAWAN_CHANNELS_MASK_SIZE_AS923` | AS923 区域（Region）的掩码大小（Mask Size）。 |
| `LORAWAN_CHANNELS_MASK_SIZE_AU915` | AU915 区域（Region）的掩码大小（Mask Size）。 |
| `LORAWAN_CHANNELS_MASK_SIZE_CN470` | CN470 区域（Region）的掩码大小（Mask Size）。 |
| `LORAWAN_CHANNELS_MASK_SIZE_CN779` | CN779 区域（Region）的掩码大小（Mask Size）。 |
| `LORAWAN_CHANNELS_MASK_SIZE_EU433` | EU433 区域（Region）的掩码大小（Mask Size）。 |
| `LORAWAN_CHANNELS_MASK_SIZE_EU868` | EU868 区域（Region）的掩码大小（Mask Size）。 |
| `LORAWAN_CHANNELS_MASK_SIZE_KR920` | KR920 区域（Region）的掩码大小（Mask Size）。 |
| `LORAWAN_CHANNELS_MASK_SIZE_IN865` | IN865 区域（Region）的掩码大小（Mask Size）。 |
| `LORAWAN_CHANNELS_MASK_SIZE_US915` | US915 区域（Region）的掩码大小（Mask Size）。 |
| `LORAWAN_CHANNELS_MASK_SIZE_RU864` | RU864 区域（Region）的掩码大小（Mask Size）。 |

<a id="ga88b65799c3f1d98fbce80927218c0837"></a>

### `lorawan_class`

```c
enum lorawan_class
```

```c
#include <zephyr/lorawan/lorawan.h>
```

LoRaWAN 设备类别类型（Class Types）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `LORAWAN_CLASS_A` | A 类设备（Class A Device）。 |
| `LORAWAN_CLASS_B` | B 类设备（Class B Device）。 |
| `LORAWAN_CLASS_C` | C 类设备（Class C Device）。 |

<a id="ga276e66fb8ce88f853d1987686e31fc86"></a>

### `lorawan_datarate`

```c
enum lorawan_datarate
```

```c
#include <zephyr/lorawan/lorawan.h>
```

LoRaWAN 数据速率类型（Datarate Types）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `LORAWAN_DR_0` | DR0 数据率（Data Rate）。 |
| `LORAWAN_DR_1` | DR1 数据率（Data Rate）。 |
| `LORAWAN_DR_2` | DR2 数据率（Data Rate）。 |
| `LORAWAN_DR_3` | DR3 数据率（Data Rate）。 |
| `LORAWAN_DR_4` | DR4 数据率（Data Rate）。 |
| `LORAWAN_DR_5` | DR5 数据率（Data Rate）。 |
| `LORAWAN_DR_6` | DR6 数据率（Data Rate）。 |
| `LORAWAN_DR_7` | DR7 数据率（Data Rate）。 |
| `LORAWAN_DR_8` | DR8 数据率（Data Rate）。 |
| `LORAWAN_DR_9` | DR9 数据率（Data Rate）。 |
| `LORAWAN_DR_10` | DR10 数据率（Data Rate）。 |
| `LORAWAN_DR_11` | DR11 数据率（Data Rate）。 |
| `LORAWAN_DR_12` | DR12 数据率（Data Rate）。 |
| `LORAWAN_DR_13` | DR13 数据率（Data Rate）。 |
| `LORAWAN_DR_14` | DR14 数据率（Data Rate）。 |
| `LORAWAN_DR_15` | DR15 数据率（Data Rate）。 |

<a id="gab28a9f22482069b2246892e4ee31660d"></a>

### `lorawan_dl_flags`

```c
enum lorawan_dl_flags
```

```c
#include <zephyr/lorawan/lorawan.h>
```

LoRaWAN 下行标志（Downlink Flags）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `LORAWAN_DATA_PENDING` | 网络服务器（Network Server）还有更多下行数据（Downlink Data）排队等待发送。 |
| `LORAWAN_TIME_UPDATED` | 网络时间（Network Time）已根据网络服务器（Network Server）更新。 |

<a id="ga5d78efba3f8e62ccd6317aed8af4bc54"></a>

### `lorawan_message_type`

```c
enum lorawan_message_type
```

```c
#include <zephyr/lorawan/lorawan.h>
```

LoRaWAN 消息类型（Message Types）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `LORAWAN_MSG_UNCONFIRMED` | 非确认消息（Unconfirmed Message）。 |
| `LORAWAN_MSG_CONFIRMED` | 确认消息（Confirmed Message）。 |

<a id="gacb8efaa0761f8761146a0e913dcb627d"></a>

### `lorawan_region`

```c
enum lorawan_region
```

```c
#include <zephyr/lorawan/lorawan.h>
```

LoRaWAN 区域类型（Region Types）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `LORAWAN_REGION_AS923` | 亚洲 923 MHz 频段（Asia 923 MHz Frequency Band）。 |
| `LORAWAN_REGION_AU915` | 澳大利亚 915 MHz 频段（Australia 915 MHz Frequency Band）。 |
| `LORAWAN_REGION_CN470` | 中国 470 MHz 频段（China 470 MHz Frequency Band）。 |
| `LORAWAN_REGION_CN779` | 中国 779 MHz 频段（China 779 MHz Frequency Band）。 |
| `LORAWAN_REGION_EU433` | 欧洲 433 MHz 频段（Europe 433 MHz Frequency Band）。 |
| `LORAWAN_REGION_EU868` | 欧洲 868 MHz 频段（Europe 868 MHz Frequency Band）。 |
| `LORAWAN_REGION_KR920` | 韩国 920 MHz 频段（South Korea 920 MHz Frequency Band）。 |
| `LORAWAN_REGION_IN865` | 印度 865 MHz 频段（India 865 MHz Frequency Band）。 |
| `LORAWAN_REGION_US915` | 美国 915 MHz 频段（United States 915 MHz Frequency Band）。 |
| `LORAWAN_REGION_RU864` | 俄罗斯 864 MHz 频段（Russia 864 MHz Frequency Band）。 |

<a id="ga12afde687fb1081bc669f844e6ab7c92"></a>

### `lorawan_clock_sync_get()`

```c
int lorawan_clock_sync_get ( uint32_t * gps_time)
```

```c
#include <zephyr/lorawan/lorawan.h>
```

获取当前同步时间（Synchronized Time）。

此函数使用 GPS 纪元格式（GPS Epoch Format），与所有 LoRaWAN 服务一致。

GPS 纪元（GPS Epoch）始于 `1980-01-06T00:00:00Z`。由于不考虑闰秒（Leap Seconds）等校正，此后它已与协调世界时（UTC）产生偏差。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `gps_time` | 以 GPS 纪元格式（GPS Epoch Format）表示、截断为 32 位的同步时间（Synchronized Time）。 |

**注意（Attention）**：注意（Attention）：仅当启用以下 Kconfig 选项时可用：`CONFIG_LORAWAN_APP_CLOCK_SYNC`。

**返回（Returns）**：返回值（Returns）：成功时为 `0`；时钟尚未同步（Synchronized）时为 `-EAGAIN`。

<a id="ga1f87b0b04bb5e75623d63d82f6069207"></a>

### `lorawan_clock_sync_run()`

```c
int lorawan_clock_sync_run ( void )
```

```c
#include <zephyr/lorawan/lorawan.h>
```

运行应用层时钟同步服务（Application Layer Clock Synchronization Service）。

此服务按固定间隔发送当前时间；该间隔可通过 Kconfig 选项 `CONFIG_LORAWAN_APP_CLOCK_SYNC_PERIODICITY` 配置。如果认为时钟偏差（Clock Deviation）过大，则从应用服务器（Application Server）接收校正偏移量（Correction Offset）。

通过多播会话（Multicast Session）升级固件需要时钟同步（Clock Synchronization）；此功能也可独立于空中固件升级（FUOTA）过程使用。

**注意（Attention）**：注意（Attention）：仅当启用以下 Kconfig 选项时可用：`CONFIG_LORAWAN_APP_CLOCK_SYNC`。

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为负错误码（errno）。

<a id="ga88c22a7e83437688039c05f9c7c1e7d4"></a>

### `lorawan_device_time_get()`

```c
int lorawan_device_time_get ( uint32_t * gps_time)
```

```c
#include <zephyr/lorawan/lorawan.h>
```

从 LoRaWAN 协议栈获取当前时间，该时间由 MAC 层的 DeviceTimeAns 更新。

此函数使用 GPS 纪元格式（GPS Epoch Format），与所有 LoRaWAN 服务一致。

GPS 纪元（GPS Epoch）始于 `1980-01-06T00:00:00Z`。由于不考虑闰秒（Leap Seconds）等校正，此后它已与协调世界时（UTC）产生偏差。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `gps_time` | 以 GPS 纪元格式（GPS Epoch Format）表示、截断为 32 位的同步时间（Synchronized Time）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`；时钟尚未同步（Synchronized）时为 `-EAGAIN`。

<a id="ga432929bd5911e04e57ef178b65e1beaa"></a>

### `lorawan_enable_adr()`

```c
void lorawan_enable_adr ( bool enable)
```

```c
#include <zephyr/lorawan/lorawan.h>
```

启用自适应数据速率（Adaptive Data Rate，ADR）。

控制是否启用自适应数据率（Adaptive Data Rate，ADR）。启用 ADR 后，设定的数据率被视为默认数据率，在 ADR 算法尚未确定数据率时使用。通常仅应对射频条件（RF Conditions）稳定的设备启用 ADR，例如大部分时间处于固定位置的设备。

启用 ADR 不会重置当前数据率（Data Rate）；之前通过 `lorawan_set_datarate()` 设置的值仍会使用，直到网络通过 `LinkADRReq` 调整它。

必须在 `lorawan_start()` 之后调用此函数；启动前的调用会被忽略。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `enable` | 启用或禁用自适应数据率（Adaptive Data Rate）。 |

<a id="gab62274848abe7cd0f23fadefd185028b"></a>

### `lorawan_frag_transport_register_descriptor_callback()`

```c
void lorawan_frag_transport_register_descriptor_callback ( transport_descriptor_cb cb)
```

```c
#include <zephyr/lorawan/lorawan.h>
```

注册处理描述符的回调函数（Handle Descriptor Callback Function）。

向分片传输服务（Fragmentation Transport Service）提供一个函数：每当收到 `FragSessionSetupReq` 且需要处理描述符（Descriptor）字段时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 通知回调（Notification Callback）。 |

**注意（Attention）**：注意（Attention）：仅当启用以下 Kconfig 选项时可用：`CONFIG_LORAWAN_FRAG_TRANSPORT`。

<a id="ga55b5a10df7235d51a65b40032e5f6907"></a>

### `lorawan_frag_transport_run()`

```c
int lorawan_frag_transport_run ( void(* transport_finished_cb )(void))
```

```c
#include <zephyr/lorawan/lorawan.h>
```

运行分片数据块传输服务（Fragmented Data Block Transport Service）。

此服务接收分片数据（Fragmented Data），通常为固件镜像（Firmware Images），并将它们存储在 `image-1` 闪存分区（Flash Partition）中。

收到全部分片（Fragments）后，调用所提供的回调（Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `transport_finished_cb` | 用于通知数据传输完成（Finished Data Transfer）的回调。 |

**注意（Attention）**：注意（Attention）：仅当启用以下 Kconfig 选项时可用：`CONFIG_LORAWAN_FRAG_TRANSPORT`。

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为负错误码（errno）。

<a id="ga6d1b45c5543473ff4fbcef473a8e0e35"></a>

### `lorawan_get_min_datarate()`

```c
enum lorawan_datarate lorawan_get_min_datarate ( void )
```

```c
#include <zephyr/lorawan/lorawan.h>
```

获取可能的最低数据速率（Minimum Possible Datarate）。

网络服务器（Network Server）发送 `TxParamSetupReq` 命令后，最低可用数据率（Minimum Possible Data Rate）可能改变。

**返回（Returns）**：返回值（Returns）：最低可用数据率（Minimum Possible Data Rate）。

<a id="ga94e3c282537618efae65e8ada1f88e81"></a>

### `lorawan_get_payload_sizes()`

```c
void lorawan_get_payload_sizes ( uint8_t * max_next_payload_size, uint8_t * max_payload_size )
```

```c
#include <zephyr/lorawan/lorawan.h>
```

获取当前负载大小（Payload Sizes）。

查询当前载荷大小（Payload Sizes）。最大载荷大小随数据率（Data Rate）而变化；由于上行数据包中可能插入 MAC 层命令，当前可用载荷大小可能更小。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `max_next_payload_size` | 下一次发送的最大载荷大小（Maximum Payload Size）。 |
| `max_payload_size` | 此数据率（Data Rate）下的最大载荷大小（Maximum Payload Size）。 |

<a id="ga5b2c7543c45801c9d0d7f46546771f17"></a>

### `lorawan_join()`

```c
int lorawan_join ( const struct lorawan_join_config * config)
```

```c
#include <zephyr/lorawan/lorawan.h>
```

加入 LoRaWAN 网络（Join Network）。

使用 OTAA 或 AWB 加入 LoRaWAN 网络。译注：原文此处写作 `AWB`；本页激活方式枚举列出的是空中激活（OTAA）与个性化激活（ABP），请对照原文核实此缩写。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `config` | 要使用的配置（Configuration）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。

<a id="ga9771704a8bcab778dd30653a0fbdeb2f"></a>

### `lorawan_register_battery_level_callback()`

```c
void lorawan_register_battery_level_callback ( lorawan_battery_level_cb_t cb)
```

```c
#include <zephyr/lorawan/lorawan.h>
```

注册电池电量回调函数（Battery Level Callback Function）。

向 LoRaWAN 协议栈（Stack）提供一个函数，在需要读取电池电量（Battery Level）时调用。

如果未提供回调（Callback），LoRaWAN 后端（Backend）将报告 `255`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 指向电池电量函数（Battery Level Function）的指针。 |

<a id="gab91f31477cd44e10692ca9d56d137ae2"></a>

### `lorawan_register_downlink_callback()`

```c
void lorawan_register_downlink_callback ( struct lorawan_downlink_cb * cb)
```

```c
#include <zephyr/lorawan/lorawan.h>
```

注册收到下行数据包（Downlink Packets）时执行的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 指向包含回调参数（Callback Parameters）的结构体的指针。 |

<a id="ga505e8d27bc7bc029feb93bbe4982d329"></a>

### `lorawan_register_dr_changed_callback()`

```c
void lorawan_register_dr_changed_callback ( lorawan_dr_changed_cb_t cb)
```

```c
#include <zephyr/lorawan/lorawan.h>
```

注册数据速率（Datarate）变化时调用的回调。

成功加入网络时调用一次回调；此后每当数据率（Data Rate）因 ADR 而变化时，再次调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 指向数据率更新回调（Data Rate Update Callback）的指针。 |

<a id="ga7b620841f521b9addc8d1ee823ee45fd"></a>

### `lorawan_register_link_check_ans_callback()`

```c
void lorawan_register_link_check_ans_callback ( lorawan_link_check_ans_cb_t cb)
```

```c
#include <zephyr/lorawan/lorawan.h>
```

注册收到链路检查请求应答（Link Check Answer）时调用的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 指向链路检查应答回调（Link Check Answer Callback）的指针。 |

<a id="ga980f1650e9cceba19da453d4937273cb"></a>

### `lorawan_request_device_time()`

```c
int lorawan_request_device_time ( bool force_request)
```

```c
#include <zephyr/lorawan/lorawan.h>
```

通过 DeviceTimeReq MAC 命令请求时间。

追加 MAC `DevTimeReq` 命令。它将在下一条消息发送时处理；也可强制发送空消息（Empty Message），立即请求时间。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `force_request` | 立即发送空消息（Empty Message）以执行请求。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为负错误码（errno）。

<a id="gaed19bb9c528f8f21104201fd0816e3a9"></a>

### `lorawan_request_link_check()`

```c
int lorawan_request_link_check ( bool force_request)
```

```c
#include <zephyr/lorawan/lorawan.h>
```

通过 LinkCheckReq MAC 命令请求链路检查（Link Check）。

追加 MAC `LinkCheckReq` 命令。它将在下一条消息发送时处理；也可强制发送空消息（Empty Message），立即请求时间。译注：“请求时间”沿用原文 “request time”，此处命令名称仍为 `LinkCheckReq`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `force_request` | 立即发送空消息（Empty Message）以执行请求。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为负错误码（errno）。

<a id="ga23758c3225e3ebf62bbe91b7589b67d7"></a>

### `lorawan_send()`

```c
int lorawan_send ( uint8_t port, uint8_t * data, uint8_t len, enum lorawan_message_type type )
```

```c
#include <zephyr/lorawan/lorawan.h>
```

向 LoRaWAN 网络发送数据。

向已连接的 LoRaWAN 网络发送数据（Data）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | 发送数据所用的端口（Port）。载荷（Payload）非空时必须设置。 |
| `data` | 待发送的数据缓冲区（Data Buffer）。 |
| `len` | 待发送缓冲区（Buffer）的长度。此缓冲区最大为 `255` 字节，但实际载荷大小（Payload Size）随区域（Region）和数据率（Data Rate）变化。 |
| `type` | 指定消息是确认消息（Confirmed）还是非确认消息（Unconfirmed），必须为 `lorawan_message_type` 中的一个值。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。

<a id="ga243c3200693ae9c81dea238068afc7dd"></a>

### `lorawan_set_channels_mask()`

```c
int lorawan_set_channels_mask ( uint16_t * channels_mask, size_t channels_mask_size )
```

```c
#include <zephyr/lorawan/lorawan.h>
```

设置信道掩码（Channels Mask）。

更改默认信道掩码（Channels Mask）。不更改掩码时，所有信道均可用于数据传输。有些网络服务器（Network Servers）不会使用全部信道，这种情况下必须提供信道掩码。

必须在 `lorawan_start()` 之后、区域信道规划（Regional Channel Plan）初始化完成后调用此函数。如果在 `lorawan_join()` 之前调用，该掩码会用于入网信道选择（Join Channel Selection）。入网之后，Join-Accept 的 CFList 处理或后续 `LinkADRReq` 命令可能更新信道状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `channels_mask` | 包含要使用的信道掩码（Channels Mask）的缓冲区。 |
| `channels_mask_size` | 信道掩码缓冲区（Channels Mask Buffer）的大小。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EPERM` | LoRaWAN 协议栈（Stack）尚未启动。 |
| `-EINVAL` | 信道掩码（Channels Mask）或其大小错误。 |

<a id="gab9768bad8d0c18410f6b8e946e89cbbe"></a>

### `lorawan_set_class()`

```c
int lorawan_set_class ( enum lorawan_class dev_class)
```

```c
#include <zephyr/lorawan/lorawan.h>
```

设置当前设备类别（Device Class）。

更改当前设备类别（Device Class）。此函数可以在建立网络连接之前或之后调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev_class` | 新的设备类别（Device Class）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。

<a id="ga14f9cb6a11c585f9ac4e9986735a82c3"></a>

### `lorawan_set_conf_msg_tries()`

```c
int lorawan_set_conf_msg_tries ( uint8_t tries)
```

```c
#include <zephyr/lorawan/lorawan.h>
```

设置发送尝试次数（Number of Tries）。

必须在 `lorawan_start()` 之后调用此函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tries` | 要使用的尝试次数（Number of Tries）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EPERM` | LoRaWAN 协议栈（Stack）尚未启动。 |
| `-EINVAL` | `tries` 超出范围（Out of Range）。 |

<a id="gaaa70ba5aa545b59233bc906948a4030d"></a>

### `lorawan_set_datarate()`

```c
int lorawan_set_datarate ( enum lorawan_datarate dr)
```

```c
#include <zephyr/lorawan/lorawan.h>
```

设置默认数据速率（Default Data Rate）。

更改默认数据率（Default Data Rate）。

必须在 `lorawan_start()` 之后调用此函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dr` | 发送所用的数据率（Data Rate）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EPERM` | LoRaWAN 协议栈（Stack）尚未启动。 |
| `-EINVAL` | 数据率（Data Rate）对当前区域无效，或 ADR 已经启用。 |

<a id="gaaf60e8b09d6f8d3a89aa2089c137fd3f"></a>

### `lorawan_set_region()`

```c
int lorawan_set_region ( enum lorawan_region region)
```

```c
#include <zephyr/lorawan/lorawan.h>
```

设置要使用的区域（Region）和频率（Frequency）。

控制 LoRa 区域（Region）和频率设置（Frequency Settings）。应在 `lorawan_start()` 之前调用。如果通过 Kconfig 只选择支持一个区域，则完全不需要调用此函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `region` | 要选择的区域（Region）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则为负错误码（errno）。

<a id="ga640d93930e09327ee87563597f919725"></a>

### `lorawan_start()`

```c
int lorawan_start ( void )
```

```c
#include <zephyr/lorawan/lorawan.h>
```

启动 LoRaWAN 协议栈（Stack）。

必须在加入网络（Joining the Network）之前调用此函数。

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。


## 10.8\_原页交叉引用（Cross References）

- [emul.h](../api_file_service_interface_reference/P034_zephyr__lorawan__emul.h_文件参考.md)
- [lorawan_join_otaa](../modem_wireless_model_reference/P034_lorawan_join_otaa_结构体.md)
- [lorawan_join_abp](../modem_wireless_model_reference/P032_lorawan_join_abp_结构体.md)
- [lorawan_join_config](../modem_wireless_model_reference/P033_lorawan_join_config_结构体.md)
- [lorawan_downlink_cb](../modem_wireless_model_reference/P031_lorawan_downlink_cb_结构体.md)
- [UINT16_MAX](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3ea490c9b3617d4479bd80ef93cd5602)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [zephyr/lorawan/lorawan.h](../api_file_display_chat_reference/P017_zephyr__lorawan__lorawan.h_文件参考.md)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [CONFIG_LORAWAN_APP_CLOCK_SYNC](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LORAWAN_APP_CLOCK_SYNC)
- [CONFIG_LORAWAN_APP_CLOCK_SYNC_PERIODICITY](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LORAWAN_APP_CLOCK_SYNC_PERIODICITY)
- [CONFIG_LORAWAN_FRAG_TRANSPORT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LORAWAN_FRAG_TRANSPORT)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga2bf50442214ecdc717f1a24dc058a338a5f262e334bc46278bec491cd022b612a"></a>
<a id="gga2bf50442214ecdc717f1a24dc058a338a13bb2a28232081844e36308977ec6701"></a>
<a id="gga0635d19612db9009775eae8e527d4897a577c304c4c1998916203e9ec7ae6e1be"></a>
<a id="gga0635d19612db9009775eae8e527d4897a1bc4cacfd02a630226f629ed61f4e1ca"></a>
<a id="gga0635d19612db9009775eae8e527d4897a2bdaecd6f1f853cd370ba89b465a9ee1"></a>
<a id="gga0635d19612db9009775eae8e527d4897a8f2f25b3ab1167f69aa594a034b27180"></a>
<a id="gga0635d19612db9009775eae8e527d4897a3b7968012bf2c8fa7adef454fc33124a"></a>
<a id="gga0635d19612db9009775eae8e527d4897a3bc215c41b7fb5652c6729756b8f979a"></a>
<a id="gga0635d19612db9009775eae8e527d4897a7443e6adbaaf4f7cb2037d8f3e42d86a"></a>
<a id="gga0635d19612db9009775eae8e527d4897a9564d246e39448f478412861a3a87b7e"></a>
<a id="gga0635d19612db9009775eae8e527d4897a054ebab376354c8a9e6a5f4e9f6f78ee"></a>
<a id="gga0635d19612db9009775eae8e527d4897aaa05e08a24aded2ada511fd2d1f4cebd"></a>
<a id="gga88b65799c3f1d98fbce80927218c0837a538e56348e6d5b506e661e3af18aee6c"></a>
<a id="gga88b65799c3f1d98fbce80927218c0837a79a9c205ac583051b2e072389491c7cb"></a>
<a id="gga88b65799c3f1d98fbce80927218c0837ad158a1985688bbe54b20a8a808774547"></a>
<a id="gga276e66fb8ce88f853d1987686e31fc86a4b60b8eb52c07b40cbaaf94a4c56e1f6"></a>
<a id="gga276e66fb8ce88f853d1987686e31fc86ade4655b32ca976c317fa9f44ac8b148a"></a>
<a id="gga276e66fb8ce88f853d1987686e31fc86a941f8a603aeb54560be7125a55c74159"></a>
<a id="gga276e66fb8ce88f853d1987686e31fc86a4ac565dbaae0c6ad4e62dc34ca0c013a"></a>
<a id="gga276e66fb8ce88f853d1987686e31fc86a6f6cd4ecd247f67cad08ede84649a939"></a>
<a id="gga276e66fb8ce88f853d1987686e31fc86a08f879f1054ca54e488180b07d7ff952"></a>
<a id="gga276e66fb8ce88f853d1987686e31fc86acc624ccf8a9585889c3685217f56099f"></a>
<a id="gga276e66fb8ce88f853d1987686e31fc86aac8afba95d7187f0829aae7abda894d5"></a>
<a id="gga276e66fb8ce88f853d1987686e31fc86a080b31031f5a2b54d84ed49b133b0a86"></a>
<a id="gga276e66fb8ce88f853d1987686e31fc86afbc8d04236410a6107cccfd71ba4bace"></a>
<a id="gga276e66fb8ce88f853d1987686e31fc86a0a18193e15d268d262d58897d39993b3"></a>
<a id="gga276e66fb8ce88f853d1987686e31fc86a2a631e746ffc5c4378e39b7a90dd44e2"></a>
<a id="gga276e66fb8ce88f853d1987686e31fc86a0df057cf1505ba94876deaeddd515548"></a>
<a id="gga276e66fb8ce88f853d1987686e31fc86a18bfd63ae262f992d9d12f8d56cc217e"></a>
<a id="gga276e66fb8ce88f853d1987686e31fc86a1ad3be15c2e60d0bb2f3c12faf279efa"></a>
<a id="gga276e66fb8ce88f853d1987686e31fc86a4738baf87e0cb2e64d9c525e40dd6e0a"></a>
<a id="ggab28a9f22482069b2246892e4ee31660da01aee480c4308ac7abb6bf909478cce2"></a>
<a id="ggab28a9f22482069b2246892e4ee31660dad272f787e193c2397e1b670ced4ba1b8"></a>
<a id="gga5d78efba3f8e62ccd6317aed8af4bc54a9855d8332363a554db9dde446cc409b7"></a>
<a id="gga5d78efba3f8e62ccd6317aed8af4bc54a40ee76ac8d0b40d06903fc06a7ef1989"></a>
<a id="ggacb8efaa0761f8761146a0e913dcb627da6a1ba05859d575a28095437436c8e6a6"></a>
<a id="ggacb8efaa0761f8761146a0e913dcb627da2744fe63701f5a5f23706b6f37672c70"></a>
<a id="ggacb8efaa0761f8761146a0e913dcb627da52d67181588c94d2a423040b4b5a1de4"></a>
<a id="ggacb8efaa0761f8761146a0e913dcb627dadb106a189c4c647e5e3af89cc753e0d8"></a>
<a id="ggacb8efaa0761f8761146a0e913dcb627dabcb9529d8f449bcb85a893fdd20f9180"></a>
<a id="ggacb8efaa0761f8761146a0e913dcb627da404530e5008260260131de051283f7ba"></a>
<a id="ggacb8efaa0761f8761146a0e913dcb627dafae64ea9dd2c2ee7e897fc0f94484da5"></a>
<a id="ggacb8efaa0761f8761146a0e913dcb627da9113b34d94da40149442f432fd97e86c"></a>
<a id="ggacb8efaa0761f8761146a0e913dcb627da70e25dd006efc115617631f64cc34c88"></a>
<a id="ggacb8efaa0761f8761146a0e913dcb627dad30a636d45def6889e2b5cbf60f28c0e"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P009_LoRa API主题.md) · [返回大纲](大纲.md) · [下一章](P011_网络分组库（Network Packet Library）.md)
