---
id: learning.zephyr-docs.api-file-display-chat-reference.page-17
title: zephyr__lorawan__lorawan.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/lorawan_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_zephyr\_\_lorawan\_\_lorawan.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/lorawan_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

LoRaWAN公共API（Public APIs）。

<a id="details"></a>

```c
#include <zephyr/device.h>
#include <zephyr/sys/slist.h>
```

查看此文件的源码。

LoRaWAN公共API（Public APIs）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 17.1\_数据结构（Data Structures）

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

## 17.2\_宏定义（Macros）

<a id="r_ga83dbf2575eaae85f1837567e9fb729a4"></a>

```c
#define LW_RECV_PORT_ANY UINT16_MAX
```

相关声明：[LW_RECV_PORT_ANY](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga83dbf2575eaae85f1837567e9fb729a4)、[UINT16_MAX](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3ea490c9b3617d4479bd80ef93cd5602)。

表示在任意端口接收（Receiving on Any Port）的标志。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 17.3\_类型定义（Typedefs）

<a id="r_ga17a7a2e1dbfa19b9f7e18a81be5514dd"></a>

```c
typedef uint8_t(* lorawan_battery_level_cb_t) (void)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[lorawan_battery_level_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga17a7a2e1dbfa19b9f7e18a81be5514dd)。

定义电池电量回调处理函数签名（Battery Level Callback Handler Function Signature）。

<a id="r_ga87a8d911f1c825bcf8c77ada568f3ed4"></a>

```c
typedef void(* lorawan_dr_changed_cb_t) (enum lorawan_datarate dr)
```

相关声明：[lorawan_dr_changed_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga87a8d911f1c825bcf8c77ada568f3ed4)、[lorawan_datarate](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga276e66fb8ce88f853d1987686e31fc86)。

定义数据速率变化回调处理函数签名（Datarate Changed Callback Handler Function Signature）。

<a id="r_gaf9fad3b2bb93ab43751098f4b8dd31f9"></a>

```c
typedef void(* lorawan_link_check_ans_cb_t) (uint8_t demod_margin, uint8_t nb_gateways)
```

相关声明：[lorawan_link_check_ans_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gaf9fad3b2bb93ab43751098f4b8dd31f9)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

定义链路检查应答处理函数签名（Link Check Answer Handler Function Signature）。

<a id="r_gade697fcc14a384420afc8817f72af410"></a>

```c
typedef int(* transport_descriptor_cb) (uint32_t descriptor)
```

相关声明：[transport_descriptor_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gade697fcc14a384420afc8817f72af410)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

定义用户描述符回调处理函数签名（User's Descriptor Callback Handler Function Signature）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 17.4\_枚举（Enumerations）

<a id="r_ga88b65799c3f1d98fbce80927218c0837"></a>

```c
enum lorawan_class { LORAWAN_CLASS_A = 0x00 , LORAWAN_CLASS_B = 0x01 , LORAWAN_CLASS_C = 0x02 }
```

相关声明：[lorawan_class](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga88b65799c3f1d98fbce80927218c0837)、[LORAWAN_CLASS_A](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga88b65799c3f1d98fbce80927218c0837a538e56348e6d5b506e661e3af18aee6c)、[LORAWAN_CLASS_B](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga88b65799c3f1d98fbce80927218c0837a79a9c205ac583051b2e072389491c7cb)、[LORAWAN_CLASS_C](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga88b65799c3f1d98fbce80927218c0837ad158a1985688bbe54b20a8a808774547)。

LoRaWAN 设备类别类型（Class Types）。

<a id="r_ga2bf50442214ecdc717f1a24dc058a338"></a>

```c
enum lorawan_act_type { LORAWAN_ACT_OTAA = 0 , LORAWAN_ACT_ABP }
```

相关声明：[lorawan_act_type](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga2bf50442214ecdc717f1a24dc058a338)、[LORAWAN_ACT_OTAA](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga2bf50442214ecdc717f1a24dc058a338a5f262e334bc46278bec491cd022b612a)、[LORAWAN_ACT_ABP](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga2bf50442214ecdc717f1a24dc058a338a13bb2a28232081844e36308977ec6701)。

LoRaWAN 激活类型（Activation Types）。

<a id="r_ga0635d19612db9009775eae8e527d4897"></a>

```c
enum lorawan_channels_mask_size { LORAWAN_CHANNELS_MASK_SIZE_AS923 = 1 , LORAWAN_CHANNELS_MASK_SIZE_AU915 = 6 , LORAWAN_CHANNELS_MASK_SIZE_CN470 = 6 , LORAWAN_CHANNELS_MASK_SIZE_CN779 = 1 , LORAWAN_CHANNELS_MASK_SIZE_EU433 = 1 , LORAWAN_CHANNELS_MASK_SIZE_EU868 = 1 , LORAWAN_CHANNELS_MASK_SIZE_KR920 = 1 , LORAWAN_CHANNELS_MASK_SIZE_IN865 = 1 , LORAWAN_CHANNELS_MASK_SIZE_US915 = 6 , LORAWAN_CHANNELS_MASK_SIZE_RU864 = 1 }
```

相关声明：[lorawan_channels_mask_size](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga0635d19612db9009775eae8e527d4897)、[LORAWAN_CHANNELS_MASK_SIZE_AS923](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga0635d19612db9009775eae8e527d4897a577c304c4c1998916203e9ec7ae6e1be)、[LORAWAN_CHANNELS_MASK_SIZE_AU915](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga0635d19612db9009775eae8e527d4897a1bc4cacfd02a630226f629ed61f4e1ca)、[LORAWAN_CHANNELS_MASK_SIZE_CN470](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga0635d19612db9009775eae8e527d4897a2bdaecd6f1f853cd370ba89b465a9ee1)、[LORAWAN_CHANNELS_MASK_SIZE_CN779](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga0635d19612db9009775eae8e527d4897a8f2f25b3ab1167f69aa594a034b27180)、[LORAWAN_CHANNELS_MASK_SIZE_EU433](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga0635d19612db9009775eae8e527d4897a3b7968012bf2c8fa7adef454fc33124a)、[LORAWAN_CHANNELS_MASK_SIZE_EU868](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga0635d19612db9009775eae8e527d4897a3bc215c41b7fb5652c6729756b8f979a)、[LORAWAN_CHANNELS_MASK_SIZE_KR920](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga0635d19612db9009775eae8e527d4897a7443e6adbaaf4f7cb2037d8f3e42d86a)、[LORAWAN_CHANNELS_MASK_SIZE_IN865](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga0635d19612db9009775eae8e527d4897a9564d246e39448f478412861a3a87b7e)、[LORAWAN_CHANNELS_MASK_SIZE_US915](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga0635d19612db9009775eae8e527d4897a054ebab376354c8a9e6a5f4e9f6f78ee)、[LORAWAN_CHANNELS_MASK_SIZE_RU864](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga0635d19612db9009775eae8e527d4897aaa05e08a24aded2ada511fd2d1f4cebd)。

LoRaWAN 信道掩码大小（Channels Mask Sizes）。

<a id="r_ga276e66fb8ce88f853d1987686e31fc86"></a>

```c
enum lorawan_datarate { LORAWAN_DR_0 = 0 , LORAWAN_DR_1 , LORAWAN_DR_2 , LORAWAN_DR_3 , LORAWAN_DR_4 , LORAWAN_DR_5 , LORAWAN_DR_6 , LORAWAN_DR_7 , LORAWAN_DR_8 , LORAWAN_DR_9 , LORAWAN_DR_10 , LORAWAN_DR_11 , LORAWAN_DR_12 , LORAWAN_DR_13 , LORAWAN_DR_14 , LORAWAN_DR_15 }
```

相关声明：[lorawan_datarate](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga276e66fb8ce88f853d1987686e31fc86)、[LORAWAN_DR_0](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga276e66fb8ce88f853d1987686e31fc86a4b60b8eb52c07b40cbaaf94a4c56e1f6)、[LORAWAN_DR_1](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga276e66fb8ce88f853d1987686e31fc86ade4655b32ca976c317fa9f44ac8b148a)、[LORAWAN_DR_2](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga276e66fb8ce88f853d1987686e31fc86a941f8a603aeb54560be7125a55c74159)、[LORAWAN_DR_3](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga276e66fb8ce88f853d1987686e31fc86a4ac565dbaae0c6ad4e62dc34ca0c013a)、[LORAWAN_DR_4](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga276e66fb8ce88f853d1987686e31fc86a6f6cd4ecd247f67cad08ede84649a939)、[LORAWAN_DR_5](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga276e66fb8ce88f853d1987686e31fc86a08f879f1054ca54e488180b07d7ff952)、[LORAWAN_DR_6](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga276e66fb8ce88f853d1987686e31fc86acc624ccf8a9585889c3685217f56099f)、[LORAWAN_DR_7](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga276e66fb8ce88f853d1987686e31fc86aac8afba95d7187f0829aae7abda894d5)、[LORAWAN_DR_8](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga276e66fb8ce88f853d1987686e31fc86a080b31031f5a2b54d84ed49b133b0a86)、[LORAWAN_DR_9](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga276e66fb8ce88f853d1987686e31fc86afbc8d04236410a6107cccfd71ba4bace)、[LORAWAN_DR_10](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga276e66fb8ce88f853d1987686e31fc86a0a18193e15d268d262d58897d39993b3)、[LORAWAN_DR_11](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga276e66fb8ce88f853d1987686e31fc86a2a631e746ffc5c4378e39b7a90dd44e2)、[LORAWAN_DR_12](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga276e66fb8ce88f853d1987686e31fc86a0df057cf1505ba94876deaeddd515548)、[LORAWAN_DR_13](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga276e66fb8ce88f853d1987686e31fc86a18bfd63ae262f992d9d12f8d56cc217e)、[LORAWAN_DR_14](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga276e66fb8ce88f853d1987686e31fc86a1ad3be15c2e60d0bb2f3c12faf279efa)、[LORAWAN_DR_15](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga276e66fb8ce88f853d1987686e31fc86a4738baf87e0cb2e64d9c525e40dd6e0a)。

LoRaWAN 数据速率类型（Datarate Types）。

<a id="r_gacb8efaa0761f8761146a0e913dcb627d"></a>

```c
enum lorawan_region { LORAWAN_REGION_AS923 , LORAWAN_REGION_AU915 , LORAWAN_REGION_CN470 , LORAWAN_REGION_CN779 , LORAWAN_REGION_EU433 , LORAWAN_REGION_EU868 , LORAWAN_REGION_KR920 , LORAWAN_REGION_IN865 , LORAWAN_REGION_US915 , LORAWAN_REGION_RU864 }
```

相关声明：[lorawan_region](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gacb8efaa0761f8761146a0e913dcb627d)、[LORAWAN_REGION_AS923](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ggacb8efaa0761f8761146a0e913dcb627da6a1ba05859d575a28095437436c8e6a6)、[LORAWAN_REGION_AU915](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ggacb8efaa0761f8761146a0e913dcb627da2744fe63701f5a5f23706b6f37672c70)、[LORAWAN_REGION_CN470](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ggacb8efaa0761f8761146a0e913dcb627da52d67181588c94d2a423040b4b5a1de4)、[LORAWAN_REGION_CN779](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ggacb8efaa0761f8761146a0e913dcb627dadb106a189c4c647e5e3af89cc753e0d8)、[LORAWAN_REGION_EU433](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ggacb8efaa0761f8761146a0e913dcb627dabcb9529d8f449bcb85a893fdd20f9180)、[LORAWAN_REGION_EU868](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ggacb8efaa0761f8761146a0e913dcb627da404530e5008260260131de051283f7ba)、[LORAWAN_REGION_KR920](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ggacb8efaa0761f8761146a0e913dcb627dafae64ea9dd2c2ee7e897fc0f94484da5)、[LORAWAN_REGION_IN865](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ggacb8efaa0761f8761146a0e913dcb627da9113b34d94da40149442f432fd97e86c)、[LORAWAN_REGION_US915](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ggacb8efaa0761f8761146a0e913dcb627da70e25dd006efc115617631f64cc34c88)、[LORAWAN_REGION_RU864](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ggacb8efaa0761f8761146a0e913dcb627dad30a636d45def6889e2b5cbf60f28c0e)。

LoRaWAN 区域类型（Region Types）。

<a id="r_ga5d78efba3f8e62ccd6317aed8af4bc54"></a>

```c
enum lorawan_message_type { LORAWAN_MSG_UNCONFIRMED = 0 , LORAWAN_MSG_CONFIRMED }
```

相关声明：[lorawan_message_type](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga5d78efba3f8e62ccd6317aed8af4bc54)、[LORAWAN_MSG_UNCONFIRMED](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga5d78efba3f8e62ccd6317aed8af4bc54a9855d8332363a554db9dde446cc409b7)、[LORAWAN_MSG_CONFIRMED](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga5d78efba3f8e62ccd6317aed8af4bc54a40ee76ac8d0b40d06903fc06a7ef1989)。

LoRaWAN 消息类型（Message Types）。

<a id="r_gab28a9f22482069b2246892e4ee31660d"></a>

```c
enum lorawan_dl_flags { LORAWAN_DATA_PENDING = BIT(0) , LORAWAN_TIME_UPDATED = BIT(1) }
```

相关声明：[lorawan_dl_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gab28a9f22482069b2246892e4ee31660d)、[LORAWAN_DATA_PENDING](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ggab28a9f22482069b2246892e4ee31660da01aee480c4308ac7abb6bf909478cce2)、[LORAWAN_TIME_UPDATED](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ggab28a9f22482069b2246892e4ee31660dad272f787e193c2397e1b670ced4ba1b8)。

LoRaWAN 下行标志（Downlink Flags）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 17.5\_函数（Functions）

<a id="r_ga9771704a8bcab778dd30653a0fbdeb2f"></a>

```c
void lorawan_register_battery_level_callback (lorawan_battery_level_cb_t cb)
```

相关声明：[lorawan_register_battery_level_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga9771704a8bcab778dd30653a0fbdeb2f)、[lorawan_battery_level_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga17a7a2e1dbfa19b9f7e18a81be5514dd)。

注册电池电量回调函数（Battery Level Callback Function）。

<a id="r_gab91f31477cd44e10692ca9d56d137ae2"></a>

```c
void lorawan_register_downlink_callback (struct lorawan_downlink_cb *cb)
```

相关声明：[lorawan_register_downlink_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gab91f31477cd44e10692ca9d56d137ae2)、[lorawan_downlink_cb](../modem_wireless_model_reference/P031_lorawan_downlink_cb_结构体.md)。

注册收到下行数据包（Downlink Packets）时执行的回调。

<a id="r_ga505e8d27bc7bc029feb93bbe4982d329"></a>

```c
void lorawan_register_dr_changed_callback (lorawan_dr_changed_cb_t cb)
```

相关声明：[lorawan_register_dr_changed_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga505e8d27bc7bc029feb93bbe4982d329)、[lorawan_dr_changed_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga87a8d911f1c825bcf8c77ada568f3ed4)。

注册数据速率（Datarate）变化时调用的回调。

<a id="r_ga7b620841f521b9addc8d1ee823ee45fd"></a>

```c
void lorawan_register_link_check_ans_callback (lorawan_link_check_ans_cb_t cb)
```

相关声明：[lorawan_register_link_check_ans_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga7b620841f521b9addc8d1ee823ee45fd)、[lorawan_link_check_ans_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gaf9fad3b2bb93ab43751098f4b8dd31f9)。

注册收到链路检查请求应答（Link Check Answer）时调用的回调。

<a id="r_ga5b2c7543c45801c9d0d7f46546771f17"></a>

```c
int lorawan_join (const struct lorawan_join_config *config)
```

相关声明：[lorawan_join](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga5b2c7543c45801c9d0d7f46546771f17)、[lorawan_join_config](../modem_wireless_model_reference/P033_lorawan_join_config_结构体.md)。

加入 LoRaWAN 网络（Join Network）。

<a id="r_ga640d93930e09327ee87563597f919725"></a>

```c
int lorawan_start (void)
```

相关声明：[lorawan_start](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga640d93930e09327ee87563597f919725)。

启动 LoRaWAN 协议栈（Stack）。

<a id="r_ga23758c3225e3ebf62bbe91b7589b67d7"></a>

```c
int lorawan_send (uint8_t port, uint8_t *data, uint8_t len, enum lorawan_message_type type)
```

相关声明：[lorawan_send](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga23758c3225e3ebf62bbe91b7589b67d7)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[lorawan_message_type](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga5d78efba3f8e62ccd6317aed8af4bc54)。

向 LoRaWAN 网络发送数据。

<a id="r_gab9768bad8d0c18410f6b8e946e89cbbe"></a>

```c
int lorawan_set_class (enum lorawan_class dev_class)
```

相关声明：[lorawan_set_class](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gab9768bad8d0c18410f6b8e946e89cbbe)、[lorawan_class](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga88b65799c3f1d98fbce80927218c0837)。

设置当前设备类别（Device Class）。

<a id="r_ga14f9cb6a11c585f9ac4e9986735a82c3"></a>

```c
int lorawan_set_conf_msg_tries (uint8_t tries)
```

相关声明：[lorawan_set_conf_msg_tries](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga14f9cb6a11c585f9ac4e9986735a82c3)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置发送尝试次数（Number of Tries）。

<a id="r_ga432929bd5911e04e57ef178b65e1beaa"></a>

```c
void lorawan_enable_adr (bool enable)
```

相关声明：[lorawan_enable_adr](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga432929bd5911e04e57ef178b65e1beaa)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用自适应数据速率（Adaptive Data Rate，ADR）。

<a id="r_ga243c3200693ae9c81dea238068afc7dd"></a>

```c
int lorawan_set_channels_mask (uint16_t *channels_mask, size_t channels_mask_size)
```

相关声明：[lorawan_set_channels_mask](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga243c3200693ae9c81dea238068afc7dd)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置信道掩码（Channels Mask）。

<a id="r_gaaa70ba5aa545b59233bc906948a4030d"></a>

```c
int lorawan_set_datarate (enum lorawan_datarate dr)
```

相关声明：[lorawan_set_datarate](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gaaa70ba5aa545b59233bc906948a4030d)、[lorawan_datarate](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga276e66fb8ce88f853d1987686e31fc86)。

设置默认数据速率（Default Data Rate）。

<a id="r_ga6d1b45c5543473ff4fbcef473a8e0e35"></a>

```c
enum lorawan_datarate lorawan_get_min_datarate (void)
```

相关声明：[lorawan_datarate](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga276e66fb8ce88f853d1987686e31fc86)、[lorawan_get_min_datarate](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga6d1b45c5543473ff4fbcef473a8e0e35)。

获取可能的最低数据速率（Minimum Possible Datarate）。

<a id="r_ga94e3c282537618efae65e8ada1f88e81"></a>

```c
void lorawan_get_payload_sizes (uint8_t *max_next_payload_size, uint8_t *max_payload_size)
```

相关声明：[lorawan_get_payload_sizes](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga94e3c282537618efae65e8ada1f88e81)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取当前负载大小（Payload Sizes）。

<a id="r_gaaf60e8b09d6f8d3a89aa2089c137fd3f"></a>

```c
int lorawan_set_region (enum lorawan_region region)
```

相关声明：[lorawan_set_region](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gaaf60e8b09d6f8d3a89aa2089c137fd3f)、[lorawan_region](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gacb8efaa0761f8761146a0e913dcb627d)。

设置要使用的区域（Region）和频率（Frequency）。

<a id="r_ga980f1650e9cceba19da453d4937273cb"></a>

```c
int lorawan_request_device_time (bool force_request)
```

相关声明：[lorawan_request_device_time](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga980f1650e9cceba19da453d4937273cb)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

通过 DeviceTimeReq MAC 命令请求时间。

<a id="r_ga88c22a7e83437688039c05f9c7c1e7d4"></a>

```c
int lorawan_device_time_get (uint32_t *gps_time)
```

相关声明：[lorawan_device_time_get](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga88c22a7e83437688039c05f9c7c1e7d4)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

从 LoRaWAN 协议栈获取当前时间，该时间由 MAC 层的 DeviceTimeAns 更新。

<a id="r_gaed19bb9c528f8f21104201fd0816e3a9"></a>

```c
int lorawan_request_link_check (bool force_request)
```

相关声明：[lorawan_request_link_check](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gaed19bb9c528f8f21104201fd0816e3a9)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

通过 LinkCheckReq MAC 命令请求链路检查（Link Check）。

<a id="r_ga1f87b0b04bb5e75623d63d82f6069207"></a>

```c
int lorawan_clock_sync_run (void)
```

相关声明：[lorawan_clock_sync_run](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga1f87b0b04bb5e75623d63d82f6069207)。

运行应用层时钟同步服务（Application Layer Clock Synchronization Service）。

<a id="r_ga12afde687fb1081bc669f844e6ab7c92"></a>

```c
int lorawan_clock_sync_get (uint32_t *gps_time)
```

相关声明：[lorawan_clock_sync_get](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga12afde687fb1081bc669f844e6ab7c92)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取当前同步时间（Synchronized Time）。

<a id="r_gab62274848abe7cd0f23fadefd185028b"></a>

```c
void lorawan_frag_transport_register_descriptor_callback (transport_descriptor_cb cb)
```

相关声明：[lorawan_frag_transport_register_descriptor_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gab62274848abe7cd0f23fadefd185028b)、[transport_descriptor_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gade697fcc14a384420afc8817f72af410)。

注册处理描述符的回调函数（Handle Descriptor Callback Function）。

<a id="r_ga55b5a10df7235d51a65b40032e5f6907"></a>

```c
int lorawan_frag_transport_run (void(*transport_finished_cb)(void))
```

相关声明：[lorawan_frag_transport_run](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga55b5a10df7235d51a65b40032e5f6907)。

运行分片数据块传输服务（Fragmented Data Block Transport Service）。


## 17.6\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/sys/slist.h](../slist_reference/P003_单向链表头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P453_lorawan.h_源码浏览.md)
- [lorawan_join_otaa](../modem_wireless_model_reference/P034_lorawan_join_otaa_结构体.md)
- [lorawan_join_abp](../modem_wireless_model_reference/P032_lorawan_join_abp_结构体.md)
- [lorawan_join_config](../modem_wireless_model_reference/P033_lorawan_join_config_结构体.md)
- [lorawan_downlink_cb](../modem_wireless_model_reference/P031_lorawan_downlink_cb_结构体.md)
- [LW_RECV_PORT_ANY](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga83dbf2575eaae85f1837567e9fb729a4)
- [UINT16_MAX](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3ea490c9b3617d4479bd80ef93cd5602)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [lorawan_battery_level_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga17a7a2e1dbfa19b9f7e18a81be5514dd)
- [lorawan_dr_changed_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga87a8d911f1c825bcf8c77ada568f3ed4)
- [lorawan_datarate](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga276e66fb8ce88f853d1987686e31fc86)
- [lorawan_link_check_ans_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gaf9fad3b2bb93ab43751098f4b8dd31f9)
- [transport_descriptor_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gade697fcc14a384420afc8817f72af410)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [lorawan_class](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga88b65799c3f1d98fbce80927218c0837)
- [LORAWAN_CLASS_A](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga88b65799c3f1d98fbce80927218c0837a538e56348e6d5b506e661e3af18aee6c)
- [LORAWAN_CLASS_B](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga88b65799c3f1d98fbce80927218c0837a79a9c205ac583051b2e072389491c7cb)
- [LORAWAN_CLASS_C](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga88b65799c3f1d98fbce80927218c0837ad158a1985688bbe54b20a8a808774547)
- [lorawan_act_type](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga2bf50442214ecdc717f1a24dc058a338)
- [LORAWAN_ACT_OTAA](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga2bf50442214ecdc717f1a24dc058a338a5f262e334bc46278bec491cd022b612a)
- [LORAWAN_ACT_ABP](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga2bf50442214ecdc717f1a24dc058a338a13bb2a28232081844e36308977ec6701)
- [lorawan_channels_mask_size](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga0635d19612db9009775eae8e527d4897)
- [LORAWAN_CHANNELS_MASK_SIZE_AS923](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga0635d19612db9009775eae8e527d4897a577c304c4c1998916203e9ec7ae6e1be)
- [LORAWAN_CHANNELS_MASK_SIZE_AU915](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga0635d19612db9009775eae8e527d4897a1bc4cacfd02a630226f629ed61f4e1ca)
- [LORAWAN_CHANNELS_MASK_SIZE_CN470](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga0635d19612db9009775eae8e527d4897a2bdaecd6f1f853cd370ba89b465a9ee1)
- [LORAWAN_CHANNELS_MASK_SIZE_CN779](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga0635d19612db9009775eae8e527d4897a8f2f25b3ab1167f69aa594a034b27180)
- [LORAWAN_CHANNELS_MASK_SIZE_EU433](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga0635d19612db9009775eae8e527d4897a3b7968012bf2c8fa7adef454fc33124a)
- [LORAWAN_CHANNELS_MASK_SIZE_EU868](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga0635d19612db9009775eae8e527d4897a3bc215c41b7fb5652c6729756b8f979a)
- [LORAWAN_CHANNELS_MASK_SIZE_KR920](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga0635d19612db9009775eae8e527d4897a7443e6adbaaf4f7cb2037d8f3e42d86a)
- [LORAWAN_CHANNELS_MASK_SIZE_IN865](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga0635d19612db9009775eae8e527d4897a9564d246e39448f478412861a3a87b7e)
- [LORAWAN_CHANNELS_MASK_SIZE_US915](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga0635d19612db9009775eae8e527d4897a054ebab376354c8a9e6a5f4e9f6f78ee)
- [LORAWAN_CHANNELS_MASK_SIZE_RU864](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga0635d19612db9009775eae8e527d4897aaa05e08a24aded2ada511fd2d1f4cebd)
- [LORAWAN_DR_0](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga276e66fb8ce88f853d1987686e31fc86a4b60b8eb52c07b40cbaaf94a4c56e1f6)
- [LORAWAN_DR_1](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga276e66fb8ce88f853d1987686e31fc86ade4655b32ca976c317fa9f44ac8b148a)
- [LORAWAN_DR_2](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga276e66fb8ce88f853d1987686e31fc86a941f8a603aeb54560be7125a55c74159)
- [LORAWAN_DR_3](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga276e66fb8ce88f853d1987686e31fc86a4ac565dbaae0c6ad4e62dc34ca0c013a)
- [LORAWAN_DR_4](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga276e66fb8ce88f853d1987686e31fc86a6f6cd4ecd247f67cad08ede84649a939)
- [LORAWAN_DR_5](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga276e66fb8ce88f853d1987686e31fc86a08f879f1054ca54e488180b07d7ff952)
- [LORAWAN_DR_6](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga276e66fb8ce88f853d1987686e31fc86acc624ccf8a9585889c3685217f56099f)
- [LORAWAN_DR_7](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga276e66fb8ce88f853d1987686e31fc86aac8afba95d7187f0829aae7abda894d5)
- [LORAWAN_DR_8](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga276e66fb8ce88f853d1987686e31fc86a080b31031f5a2b54d84ed49b133b0a86)
- [LORAWAN_DR_9](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga276e66fb8ce88f853d1987686e31fc86afbc8d04236410a6107cccfd71ba4bace)
- [LORAWAN_DR_10](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga276e66fb8ce88f853d1987686e31fc86a0a18193e15d268d262d58897d39993b3)
- [LORAWAN_DR_11](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga276e66fb8ce88f853d1987686e31fc86a2a631e746ffc5c4378e39b7a90dd44e2)
- [LORAWAN_DR_12](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga276e66fb8ce88f853d1987686e31fc86a0df057cf1505ba94876deaeddd515548)
- [LORAWAN_DR_13](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga276e66fb8ce88f853d1987686e31fc86a18bfd63ae262f992d9d12f8d56cc217e)
- [LORAWAN_DR_14](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga276e66fb8ce88f853d1987686e31fc86a1ad3be15c2e60d0bb2f3c12faf279efa)
- [LORAWAN_DR_15](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga276e66fb8ce88f853d1987686e31fc86a4738baf87e0cb2e64d9c525e40dd6e0a)
- [lorawan_region](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gacb8efaa0761f8761146a0e913dcb627d)
- [LORAWAN_REGION_AS923](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ggacb8efaa0761f8761146a0e913dcb627da6a1ba05859d575a28095437436c8e6a6)
- [LORAWAN_REGION_AU915](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ggacb8efaa0761f8761146a0e913dcb627da2744fe63701f5a5f23706b6f37672c70)
- [LORAWAN_REGION_CN470](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ggacb8efaa0761f8761146a0e913dcb627da52d67181588c94d2a423040b4b5a1de4)
- [LORAWAN_REGION_CN779](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ggacb8efaa0761f8761146a0e913dcb627dadb106a189c4c647e5e3af89cc753e0d8)
- [LORAWAN_REGION_EU433](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ggacb8efaa0761f8761146a0e913dcb627dabcb9529d8f449bcb85a893fdd20f9180)
- [LORAWAN_REGION_EU868](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ggacb8efaa0761f8761146a0e913dcb627da404530e5008260260131de051283f7ba)
- [LORAWAN_REGION_KR920](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ggacb8efaa0761f8761146a0e913dcb627dafae64ea9dd2c2ee7e897fc0f94484da5)
- [LORAWAN_REGION_IN865](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ggacb8efaa0761f8761146a0e913dcb627da9113b34d94da40149442f432fd97e86c)
- [LORAWAN_REGION_US915](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ggacb8efaa0761f8761146a0e913dcb627da70e25dd006efc115617631f64cc34c88)
- [LORAWAN_REGION_RU864](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ggacb8efaa0761f8761146a0e913dcb627dad30a636d45def6889e2b5cbf60f28c0e)
- [lorawan_message_type](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga5d78efba3f8e62ccd6317aed8af4bc54)
- [LORAWAN_MSG_UNCONFIRMED](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga5d78efba3f8e62ccd6317aed8af4bc54a9855d8332363a554db9dde446cc409b7)
- [LORAWAN_MSG_CONFIRMED](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gga5d78efba3f8e62ccd6317aed8af4bc54a40ee76ac8d0b40d06903fc06a7ef1989)
- [lorawan_dl_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gab28a9f22482069b2246892e4ee31660d)
- [LORAWAN_DATA_PENDING](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ggab28a9f22482069b2246892e4ee31660da01aee480c4308ac7abb6bf909478cce2)
- [LORAWAN_TIME_UPDATED](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ggab28a9f22482069b2246892e4ee31660dad272f787e193c2397e1b670ced4ba1b8)
- [lorawan_register_battery_level_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga9771704a8bcab778dd30653a0fbdeb2f)
- [lorawan_register_downlink_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gab91f31477cd44e10692ca9d56d137ae2)
- [lorawan_register_dr_changed_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga505e8d27bc7bc029feb93bbe4982d329)
- [lorawan_register_link_check_ans_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga7b620841f521b9addc8d1ee823ee45fd)
- [lorawan_join](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga5b2c7543c45801c9d0d7f46546771f17)
- [lorawan_start](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga640d93930e09327ee87563597f919725)
- [lorawan_send](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga23758c3225e3ebf62bbe91b7589b67d7)
- [lorawan_set_class](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gab9768bad8d0c18410f6b8e946e89cbbe)
- [lorawan_set_conf_msg_tries](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga14f9cb6a11c585f9ac4e9986735a82c3)
- [lorawan_enable_adr](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga432929bd5911e04e57ef178b65e1beaa)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [lorawan_set_channels_mask](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga243c3200693ae9c81dea238068afc7dd)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [lorawan_set_datarate](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gaaa70ba5aa545b59233bc906948a4030d)
- [lorawan_get_min_datarate](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga6d1b45c5543473ff4fbcef473a8e0e35)
- [lorawan_get_payload_sizes](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga94e3c282537618efae65e8ada1f88e81)
- [lorawan_set_region](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gaaf60e8b09d6f8d3a89aa2089c137fd3f)
- [lorawan_request_device_time](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga980f1650e9cceba19da453d4937273cb)
- [lorawan_device_time_get](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga88c22a7e83437688039c05f9c7c1e7d4)
- [lorawan_request_link_check](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gaed19bb9c528f8f21104201fd0816e3a9)
- [lorawan_clock_sync_run](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga1f87b0b04bb5e75623d63d82f6069207)
- [lorawan_clock_sync_get](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga12afde687fb1081bc669f844e6ab7c92)
- [lorawan_frag_transport_register_descriptor_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#gab62274848abe7cd0f23fadefd185028b)
- [lorawan_frag_transport_run](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html#ga55b5a10df7235d51a65b40032e5f6907)

<a id="header-details"></a>

---

[上一章](P016_zephyr__canbus__isotp.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P018_zephyr__drivers__clock_control__mchp_clock_pic32ck_sg_gc.h_文件参考.md)
