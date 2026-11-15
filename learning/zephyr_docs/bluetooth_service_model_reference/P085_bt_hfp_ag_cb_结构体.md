---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-85
title: bt_hfp_ag_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hfp__ag__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第85章\_bt\_hfp\_ag\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hfp__ag__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

免提配置文件音频网关（HFP AG）的应用回调。

```c
#include <zephyr/bluetooth/classic/hfp_ag.h>
```

<a id="details"></a>

免提配置文件音频网关（HFP AG）的应用回调。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 85.1\_数据成员（Data Fields）

<a id="r_ab9506172c5b23bf97b5d59ddaddd7282"></a>

```c
void(* connected )(struct bt_conn *conn, struct bt_hfp_ag *ag)
```

相关声明：[connected](#ab9506172c5b23bf97b5d59ddaddd7282)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_hfp_ag](P083_bt_hfp_ag_结构体.md)。

通知应用的免提音频网关连接回调（HF AG connected callback）。

<a id="r_af9c53ab021dbbf1017d71895581960c4"></a>

```c
void(* disconnected )(struct bt_hfp_ag *ag)
```

相关声明：[disconnected](#af9c53ab021dbbf1017d71895581960c4)、[bt_hfp_ag](P083_bt_hfp_ag_结构体.md)。

通知应用的免提设备断开回调（HF disconnected callback）。

<a id="r_aac2b1ff4d80361e0e5eea2481027b4cf"></a>

```c
void(* sco_connected )(struct bt_hfp_ag *ag, struct bt_conn *sco_conn)
```

相关声明：[sco_connected](#aac2b1ff4d80361e0e5eea2481027b4cf)、[bt_hfp_ag](P083_bt_hfp_ag_结构体.md)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

免提同步／扩展同步面向连接链路连接回调（HF SCO/eSCO connected callback）。

<a id="r_a95600361e59a516f220a314e920c5858"></a>

```c
void(* sco_disconnected )(struct bt_conn *sco_conn, uint8_t reason)
```

相关声明：[sco_disconnected](#a95600361e59a516f220a314e920c5858)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

免提同步／扩展同步面向连接链路断开回调（HF SCO/eSCO disconnected callback）。

<a id="r_a1cf5786c517ecf4bf611a168e312084c"></a>

```c
int(* get_indicator_value )(struct bt_hfp_ag *ag, uint8_t *service, uint8_t *strength, uint8_t *roam, uint8_t *battery)
```

相关声明：[get_indicator_value](#a1cf5786c517ecf4bf611a168e312084c)、[bt_hfp_ag](P083_bt_hfp_ag_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取指示器值回调（Get indicator values callback）。

<a id="r_ac3771d39b8f1982514bbb23fc7773468"></a>

```c
int(* get_ongoing_call )(struct bt_hfp_ag *ag)
```

相关声明：[get_ongoing_call](#ac3771d39b8f1982514bbb23fc7773468)、[bt_hfp_ag](P083_bt_hfp_ag_结构体.md)。

获取进行中呼叫信息回调（Get ongoing call information callback）。

<a id="r_af335450c5e63139485fa5a131814d650"></a>

```c
int(* memory_dial )(struct bt_hfp_ag *ag, const char *location, char **number)
```

相关声明：[memory_dial](#af335450c5e63139485fa5a131814d650)、[bt_hfp_ag](P083_bt_hfp_ag_结构体.md)。

免提设备存储拨号请求回调（HF memory dialing request callback）。

<a id="r_a98c497e706ed5fcfe6fd308741893e91"></a>

```c
int(* number_call )(struct bt_hfp_ag *ag, const char *number)
```

相关声明：[number_call](#a98c497e706ed5fcfe6fd308741893e91)、[bt_hfp_ag](P083_bt_hfp_ag_结构体.md)。

免提设备按电话号码呼叫请求回调（HF phone number calling request callback）。

<a id="r_aa578544cd1f329a06898efcfa7db2d78"></a>

```c
int(* redial )(struct bt_hfp_ag *ag, char number[CONFIG_BT_HFP_AG_PHONE_NUMBER_MAX_LEN+1])
```

相关声明：[redial](#aa578544cd1f329a06898efcfa7db2d78)、[bt_hfp_ag](P083_bt_hfp_ag_结构体.md)。

免提设备末次号码重拨请求回调（HF last number redial request callback）。

<a id="r_a8946de63ef24bbbc69e285abe2d141c1"></a>

```c
void(* outgoing )(struct bt_hfp_ag *ag, struct bt_hfp_ag_call *call, const char *number)
```

相关声明：[outgoing](#a8946de63ef24bbbc69e285abe2d141c1)、[bt_hfp_ag](P083_bt_hfp_ag_结构体.md)、[bt_hfp_ag_call](P084_bt_hfp_ag_call_结构体.md)。

免提设备呼出回调（HF outgoing callback）。

<a id="r_aa0a4ab5aad6557a786ccf2f6861b932c"></a>

```c
void(* incoming )(struct bt_hfp_ag *ag, struct bt_hfp_ag_call *call, const char *number)
```

相关声明：[incoming](#aa0a4ab5aad6557a786ccf2f6861b932c)、[bt_hfp_ag](P083_bt_hfp_ag_结构体.md)、[bt_hfp_ag_call](P084_bt_hfp_ag_call_结构体.md)。

免提设备来电回调（HF incoming callback）。

<a id="r_a5b9f1c48e15a74b052678c491a592a5f"></a>

```c
void(* incoming_held )(struct bt_hfp_ag_call *call)
```

相关声明：[incoming_held](#a5b9f1c48e15a74b052678c491a592a5f)、[bt_hfp_ag_call](P084_bt_hfp_ag_call_结构体.md)。

免提设备来电保持回调（HF incoming call held callback）。

<a id="r_a0b8967f487d64556851420b2f4e059fe"></a>

```c
void(* ringing )(struct bt_hfp_ag_call *call, bool in_band)
```

相关声明：[ringing](#a0b8967f487d64556851420b2f4e059fe)、[bt_hfp_ag_call](P084_bt_hfp_ag_call_结构体.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

免提设备振铃回调（HF ringing callback）。

<a id="r_a7da69bf1f5b85130ce2656c4915ba6d8"></a>

```c
void(* accept )(struct bt_hfp_ag_call *call)
```

相关声明：[accept](#a7da69bf1f5b85130ce2656c4915ba6d8)、[bt_hfp_ag_call](P084_bt_hfp_ag_call_结构体.md)。

免提设备接受呼叫回调（HF call accept callback）。

<a id="r_abe78441b0f01acd72713c7658f4e0274"></a>

```c
void(* held )(struct bt_hfp_ag_call *call)
```

相关声明：[held](#abe78441b0f01acd72713c7658f4e0274)、[bt_hfp_ag_call](P084_bt_hfp_ag_call_结构体.md)。

免提设备呼叫保持回调（HF call held callback）。

<a id="r_a9d6b978f82de6ded48881a87eb90aebb"></a>

```c
void(* retrieve )(struct bt_hfp_ag_call *call)
```

相关声明：[retrieve](#a9d6b978f82de6ded48881a87eb90aebb)、[bt_hfp_ag_call](P084_bt_hfp_ag_call_结构体.md)。

免提设备恢复呼叫回调（HF call retrieve callback）。

<a id="r_abe1b5d71279c2e3292b3b90043d75224"></a>

```c
void(* reject )(struct bt_hfp_ag_call *call)
```

相关声明：[reject](#abe1b5d71279c2e3292b3b90043d75224)、[bt_hfp_ag_call](P084_bt_hfp_ag_call_结构体.md)。

免提设备拒绝呼叫回调（HF call reject callback）。

<a id="r_adf9960da8a3f4c38f7fcd60501522462"></a>

```c
void(* terminate )(struct bt_hfp_ag_call *call)
```

相关声明：[terminate](#adf9960da8a3f4c38f7fcd60501522462)、[bt_hfp_ag_call](P084_bt_hfp_ag_call_结构体.md)。

免提设备终止呼叫回调（HF call terminate callback）。

<a id="r_a2f15172060cc5d225894be5c8311610b"></a>

```c
void(* codec )(struct bt_hfp_ag *ag, uint32_t ids)
```

相关声明：[codec](#a2f15172060cc5d225894be5c8311610b)、[bt_hfp_ag](P083_bt_hfp_ag_结构体.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

支持的编解码器标识符回调（Supported codec IDs callback）。

<a id="r_a82abcad15f921fb0c99cc705e139aac1"></a>

```c
void(* codec_negotiate )(struct bt_hfp_ag *ag, int err)
```

相关声明：[codec_negotiate](#a82abcad15f921fb0c99cc705e139aac1)、[bt_hfp_ag](P083_bt_hfp_ag_结构体.md)。

编解码器协商回调（Codec negotiate callback）。

<a id="r_a390377048e8623889515f2c6b6be0874"></a>

```c
void(* audio_connect_req )(struct bt_hfp_ag *ag)
```

相关声明：[audio_connect_req](#a390377048e8623889515f2c6b6be0874)、[bt_hfp_ag](P083_bt_hfp_ag_结构体.md)。

音频连接请求回调（Audio connection request callback）。

<a id="r_aaad37582866c420ee41c3f730de16eb4"></a>

```c
void(* vgm )(struct bt_hfp_ag *ag, uint8_t gain)
```

相关声明：[vgm](#aaad37582866c420ee41c3f730de16eb4)、[bt_hfp_ag](P083_bt_hfp_ag_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

免提设备麦克风增益设置回调（HF VGM setting callback）。

<a id="r_a38adb040dee9abd794f952322bf3d615"></a>

```c
void(* vgs )(struct bt_hfp_ag *ag, uint8_t gain)
```

相关声明：[vgs](#a38adb040dee9abd794f952322bf3d615)、[bt_hfp_ag](P083_bt_hfp_ag_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

免提设备扬声器增益设置回调（HF VGS setting callback）。

<a id="r_ac3c09ffe392e167dd5aae82e740b5050"></a>

```c
void(* ecnr_turn_off )(struct bt_hfp_ag *ag)
```

相关声明：[ecnr_turn_off](#ac3c09ffe392e167dd5aae82e740b5050)、[bt_hfp_ag](P083_bt_hfp_ag_结构体.md)。

免提设备关闭回声消除与降噪回调（HF ECNR turns off callback）。

<a id="r_ac06c1ddfa5cdc4ecb81a838e32299c8a"></a>

```c
void(* explicit_call_transfer )(struct bt_hfp_ag *ag)
```

相关声明：[explicit_call_transfer](#ac06c1ddfa5cdc4ecb81a838e32299c8a)、[bt_hfp_ag](P083_bt_hfp_ag_结构体.md)。

免提设备显式呼叫转移回调（HF explicit call transfer callback）。

<a id="r_a16c528018a2e9e97320df885c049454f"></a>

```c
void(* voice_recognition )(struct bt_hfp_ag *ag, bool activate)
```

相关声明：[voice_recognition](#a16c528018a2e9e97320df885c049454f)、[bt_hfp_ag](P083_bt_hfp_ag_结构体.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

语音识别激活／停用回调（Voice recognition activation/deactivation callback）。

<a id="r_ad9925958c87b164113f607bd680ce2c3"></a>

```c
void(* ready_to_accept_audio )(struct bt_hfp_ag *ag)
```

相关声明：[ready_to_accept_audio](#ad9925958c87b164113f607bd680ce2c3)、[bt_hfp_ag](P083_bt_hfp_ag_结构体.md)。

准备接受音频回调（Ready to accept audio callback）。

<a id="r_aecc8cdaf372d93f9cb531604f9b82d65"></a>

```c
int(* request_phone_number )(struct bt_hfp_ag *ag, char **number)
```

相关声明：[request_phone_number](#aecc8cdaf372d93f9cb531604f9b82d65)、[bt_hfp_ag](P083_bt_hfp_ag_结构体.md)。

请求电话号码回调（Request phone number callback）。

<a id="r_ad690d69c9786c69ad85e005e778b316c"></a>

```c
void(* transmit_dtmf_code )(struct bt_hfp_ag *ag, char code)
```

相关声明：[transmit_dtmf_code](#ad690d69c9786c69ad85e005e778b316c)、[bt_hfp_ag](P083_bt_hfp_ag_结构体.md)。

发送双音多频代码回调（Transmit a DTMF Code callback）。

<a id="r_a976016f32e462daf38cd6d24ba18ff3d"></a>

```c
int(* subscriber_number )(struct bt_hfp_ag *ag, bt_hfp_ag_query_subscriber_func_t func)
```

相关声明：[subscriber_number](#a976016f32e462daf38cd6d24ba18ff3d)、[bt_hfp_ag](P083_bt_hfp_ag_结构体.md)、[bt_hfp_ag_query_subscriber_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga8e9b485f7ea0b9e16d96f578cdc587c3)。

获取用户号码回调（Get subscriber number callback）。

<a id="r_a965d39254b75668f968d9a2bb5cffeba"></a>

```c
void(* hf_indicator_value )(struct bt_hfp_ag *ag, enum hfp_ag_hf_indicators indicator, uint32_t value)
```

相关声明：[hf_indicator_value](#a965d39254b75668f968d9a2bb5cffeba)、[bt_hfp_ag](P083_bt_hfp_ag_结构体.md)、[hfp_ag_hf_indicators](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga030c97d703fb45a2055653c51cb1b403)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

免提设备指示器值回调（HF indicator value callback）。

## 85.2\_详细说明（Detailed Documentation）

<a id="a7da69bf1f5b85130ce2656c4915ba6d8"></a>

### `accept`

```c
void(* bt_hfp_ag_cb::accept) (struct bt_hfp_ag_call *call)
```

免提设备接受呼叫回调（HF call accept callback）。

提供此回调后，每次呼叫被接受（Accepted）时都会调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `call` | 免提规范音频网关呼叫对象（HFP AG call object）。 |

<a id="a390377048e8623889515f2c6b6be0874"></a>

### `audio_connect_req`

```c
void(* bt_hfp_ag_cb::audio_connect_req) (struct bt_hfp_ag *ag)
```

音频连接请求回调（Audio connection request callback）。

提供此回调后，每当免提设备（HF）触发音频连接请求时都会调用。收到 `AT+BCC` 命令表示音频连接建立过程由 HF 发起。如果应用提供了此回调，音频网关（AG）需要在应用层调用 `bt_hfp_ag_audio_connect`，启动编解码器连接过程（Codec connection procedure）；否则将使用默认编解码器标识符 `BT_HFP_AG_CODEC_CVSD` 启动该过程。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ag` | 免提规范音频网关对象（HFP AG object）。 |

<a id="a2f15172060cc5d225894be5c8311610b"></a>

### `codec`

```c
void(* bt_hfp_ag_cb::codec) (struct bt_hfp_ag *ag, uint32_t ids)
```

支持的编解码器标识符回调（Supported codec IDs callback）。

提供此回调后，每次支持的编解码器标识符（Codec IDs）更新时都会调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ag` | 免提规范音频网关对象（HFP AG object）。 |
| `ids` | 支持的编解码器标识符位图（Supported codec ID bitmap）。 |

<a id="a82abcad15f921fb0c99cc705e139aac1"></a>

### `codec_negotiate`

```c
void(* bt_hfp_ag_cb::codec_negotiate) (struct bt_hfp_ag *ag, int err)
```

编解码器协商回调（Codec negotiate callback）。

提供此回调后，每次编解码器协商（Codec negotiation）成功或失败时都会调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ag` | 免提规范音频网关对象（HFP AG object）。 |
| `err` | 编解码器协商结果（Codec negotiation result）。 |

<a id="ab9506172c5b23bf97b5d59ddaddd7282"></a>

### `connected`

```c
void(* bt_hfp_ag_cb::connected) (struct bt_conn *conn, struct bt_hfp_ag *ag)
```

通知应用的免提音频网关连接回调（HF AG connected callback）。

提供此回调后，每次音频网关连接（AG connection）完成时都会调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `ag` | 免提规范音频网关对象（HFP AG object）。 |

<a id="af9c53ab021dbbf1017d71895581960c4"></a>

### `disconnected`

```c
void(* bt_hfp_ag_cb::disconnected) (struct bt_hfp_ag *ag)
```

通知应用的免提设备断开回调（HF disconnected callback）。

提供此回调后，每次连接断开时都会调用，包括连接被拒绝、被取消，或建立服务级连接（SLC）过程中发生错误。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ag` | 免提规范音频网关对象（HFP AG object）。 |

<a id="ac3c09ffe392e167dd5aae82e740b5050"></a>

### `ecnr_turn_off`

```c
void(* bt_hfp_ag_cb::ecnr_turn_off) (struct bt_hfp_ag *ag)
```

免提设备关闭回声消除与降噪回调（HF ECNR turns off callback）。

提供此回调后，每当从免提设备（HF）收到关闭回声消除与降噪（ECNR）的请求时都会调用。若此回调为 `NULL`，或未启用 `CONFIG_BT_HFP_AG_ECNR`，则 AT 命令的响应结果码为 `AT ERROR`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ag` | 免提规范音频网关对象（HFP AG object）。 |

<a id="ac06c1ddfa5cdc4ecb81a838e32299c8a"></a>

### `explicit_call_transfer`

```c
void(* bt_hfp_ag_cb::explicit_call_transfer) (struct bt_hfp_ag *ag)
```

免提设备显式呼叫转移回调（HF explicit call transfer callback）。

提供此回调后，每当免提设备（HF）发送 `AT+CHLD=4` 时都会调用。收到通知后，应用应连接两个呼叫，并使用户从这两个呼叫中断开，即显式呼叫转移（Explicit Call Transfer）。回调返回后，呼叫对象失效。若回调为 `NULL`，AT 命令的响应结果码为 `AT ERROR`。未启用 `CONFIG_BT_HFP_AG_3WAY_CALL` 时，不通知此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ag` | 免提规范音频网关对象（HFP AG object）。 |

<a id="a1cf5786c517ecf4bf611a168e312084c"></a>

### `get_indicator_value`

```c
int(* bt_hfp_ag_cb::get_indicator_value) (struct bt_hfp_ag *ag, uint8_t *service, uint8_t *strength, uint8_t *roam, uint8_t *battery)
```

获取指示器值回调（Get indicator values callback）。

提供此回调后，每当音频网关（AG）需要向免提设备（HF）提供当前指示器值（Indicator values）时都会调用。典型情况是 HF 发送 `AT+CIND?`，查询 AG 指示器的当前状态。

应用应通过提供的指针填充指示器值（Indicator values）。所有值均应根据音频网关（AG）的当前状态设置。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ag` | 免提规范音频网关对象（HFP AG object）。 |
| `service` | 用于存储服务可用性指示器值（Service availability indicator）的指针。`0` 表示服务不可用，`1` 表示服务可用。 |
| `strength` | 用于存储信号强度指示器值（Signal strength indicator）的指针。范围为 0–5；`0` 表示无信号，`5` 表示最强信号。 |
| `roam` | 用于存储漫游状态指示器值（Roaming status indicator）的指针。`0` 表示未漫游，`1` 表示正在漫游。 |
| `battery` | 用于存储电池电量指示器值（Battery level indicator）的指针。范围为 0–5；`0` 表示电池耗尽，`5` 表示电池充满。 |

**说明（Note）**：注意（Note）：音频网关（AG）正处于服务级连接建立阶段（SLC establishment），此时尚未通知 AG 的 `connected()` 回调。若应用未提供此回调，或返回错误值非零，则这些指示器默认全部设为 `0`。之后可调用专用函数设置并通知具体值，例如通过 `bt_hfp_ag_service_availability()` 设置服务可用性指示器，通过 `bt_hfp_ag_signal_strength()` 设置信号强度，依此类推。

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ac3771d39b8f1982514bbb23fc7773468"></a>

### `get_ongoing_call`

```c
int(* bt_hfp_ag_cb::get_ongoing_call) (struct bt_hfp_ag *ag)
```

获取进行中呼叫信息回调（Get ongoing call information callback）。

提供此回调后，收到免提设备（HF）发送的 `AT+CIND?` 命令时会调用。收到通知后，应在 `CONFIG_BT_HFP_AG_GET_ONGOING_CALL_TIMEOUT` 指定的超时内，通过 `bt_hfp_ag_ongoing_calls()` 设置进行中的呼叫（Ongoing calls）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ag` | 免提规范音频网关对象（HFP AG object）。 |

**说明（Note）**：注意（Note）：音频网关（AG）正处于服务级连接建立阶段（SLC establishment），此时尚未通知 AG 的 `connected()` 回调。

**返回（Returns）**：返回值（Returns）：成功时为 `0`；在调用 `bt_hfp_ag_ongoing_calls()` 后，或超过 `CONFIG_BT_HFP_AG_GET_ONGOING_CALL_TIMEOUT` 后，发送 `+CIND` 响应。发生错误时返回负值，此时立即回复 `+CIND` 响应。

<a id="abe78441b0f01acd72713c7658f4e0274"></a>

### `held`

```c
void(* bt_hfp_ag_cb::held) (struct bt_hfp_ag_call *call)
```

免提设备呼叫保持回调（HF call held callback）。

提供此回调后，每次呼叫被保持（Held）时都会调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `call` | 免提规范音频网关呼叫对象（HFP AG call object）。 |

<a id="a965d39254b75668f968d9a2bb5cffeba"></a>

### `hf_indicator_value`

```c
void(* bt_hfp_ag_cb::hf_indicator_value) (struct bt_hfp_ag *ag, enum hfp_ag_hf_indicators indicator, uint32_t value)
```

免提设备指示器值回调（HF indicator value callback）。

提供此回调后，每当收到 `AT+BIEV` 命令时都会调用。未启用 `CONFIG_BT_HFP_AG_HF_INDICATORS` 时，不通知此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ag` | 免提规范音频网关对象（HFP AG object）。 |
| `indicator` | 免提设备指示器（HF indicator）。 |
| `value` | 指定指示器的值（Indicator value）。 |

<a id="aa0a4ab5aad6557a786ccf2f6861b932c"></a>

### `incoming`

```c
void(* bt_hfp_ag_cb::incoming) (struct bt_hfp_ag *ag, struct bt_hfp_ag_call *call, const char *number)
```

免提设备来电回调（HF incoming callback）。

提供此回调后，每当有新来电（Incoming call）时都会调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ag` | 免提规范音频网关对象（HFP AG object）。 |
| `call` | 免提规范音频网关呼叫对象（HFP AG call object）。 |
| `number` | 来电号码（Incoming number）。 |

<a id="a5b9f1c48e15a74b052678c491a592a5f"></a>

### `incoming_held`

```c
void(* bt_hfp_ag_cb::incoming_held) (struct bt_hfp_ag_call *call)
```

免提设备来电保持回调（HF incoming call held callback）。

提供此回调后，每当来电被保持但尚未接受（Held but not accepted）时都会调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `call` | 免提规范音频网关呼叫对象（HFP AG call object）。 |

<a id="af335450c5e63139485fa5a131814d650"></a>

### `memory_dial`

```c
int(* bt_hfp_ag_cb::memory_dial) (struct bt_hfp_ag *ag, const char *location, char **number)
```

免提设备存储拨号请求回调（HF memory dialing request callback）。

提供此回调后，每当免提设备（HF）通过存储拨号（Memory dialing）请求新呼叫时都会调用。应根据给定的音频网关存储位置（AG memory location）获取电话号码。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ag` | 免提规范音频网关对象（HFP AG object）。 |
| `location` | 音频网关存储位置（AG memory location）。 |
| `number` | 拨号号码（Dialing number）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="a98c497e706ed5fcfe6fd308741893e91"></a>

### `number_call`

```c
int(* bt_hfp_ag_cb::number_call) (struct bt_hfp_ag *ag, const char *number)
```

免提设备按电话号码呼叫请求回调（HF phone number calling request callback）。

提供此回调后，每当免提设备（HF）指定电话号码请求新呼叫时都会调用。触发后，应用需要使用传入的电话号码开始拨号。若回调无效，则不支持 HF 按电话号码拨号。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ag` | 免提规范音频网关对象（HFP AG object）。 |
| `number` | 拨号号码（Dialing number）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="a8946de63ef24bbbc69e285abe2d141c1"></a>

### `outgoing`

```c
void(* bt_hfp_ag_cb::outgoing) (struct bt_hfp_ag *ag, struct bt_hfp_ag_call *call, const char *number)
```

免提设备呼出回调（HF outgoing callback）。

提供此回调后，每当有新呼出（Outgoing call）时都会调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ag` | 免提规范音频网关对象（HFP AG object）。 |
| `call` | 免提规范音频网关呼叫对象（HFP AG call object）。 |
| `number` | 拨号号码（Dialing number）。 |

<a id="ad9925958c87b164113f607bd680ce2c3"></a>

### `ready_to_accept_audio`

```c
void(* bt_hfp_ag_cb::ready_to_accept_audio) (struct bt_hfp_ag *ag)
```

准备接受音频回调（Ready to accept audio callback）。

提供此回调后，每当免提设备（HF）准备好接受音频时都会调用。若 HF 支持增强语音识别状态特性（Enhanced Voice Recognition Status），收到 `AT+BVRA=2` 命令时会通知此回调。HF 可以在进行中的语音识别会话（VR session）里发送该值，以终止音频网关（AG）的音频输出（如有），并让 AG 准备接受新的音频输入；或者在语音识别激活后通知此回调。未启用 `CONFIG_BT_HFP_AG_ENH_VOICE_RECG` 时，不通知此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ag` | 免提规范音频网关对象（HFP AG object）。 |

<a id="aa578544cd1f329a06898efcfa7db2d78"></a>

### `redial`

```c
int(* bt_hfp_ag_cb::redial) (struct bt_hfp_ag *ag, char number[CONFIG_BT_HFP_AG_PHONE_NUMBER_MAX_LEN+1])
```

免提设备末次号码重拨请求回调（HF last number redial request callback）。

提供此回调后，每当免提设备（HF）通过 `AT+BLDN` 命令发出末次号码重拨请求（Last number redial request）时都会调用。触发后，应用需要提供上一次拨出的电话号码。若回调无效，则不支持 HF 末次号码重拨。

应用应执行以下操作：

- 从通话历史记录中取得最后拨打的电话号码。
- 将电话号码复制到提供的缓冲区。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ag` | 免提规范音频网关对象（HFP AG object）。 |
| `number` | 用于存储上一次拨出电话号码（Last dialed phone number）的缓冲区。大小为 `CONFIG_BT_HFP_AG_PHONE_NUMBER_MAX_LEN + 1`，内容应以空字符终止（Null-terminated）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，错误时为负值。成功时，音频网关（AG）继续执行呼叫建立过程（Call setup procedure）；错误时，向免提设备（HF）发送 `ERROR` 响应。

<a id="abe1b5d71279c2e3292b3b90043d75224"></a>

### `reject`

```c
void(* bt_hfp_ag_cb::reject) (struct bt_hfp_ag_call *call)
```

免提设备拒绝呼叫回调（HF call reject callback）。

提供此回调后，每次呼叫被拒绝（Rejected）时都会调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `call` | 免提规范音频网关呼叫对象（HFP AG call object）。 |

<a id="aecc8cdaf372d93f9cb531604f9b82d65"></a>

### `request_phone_number`

```c
int(* bt_hfp_ag_cb::request_phone_number) (struct bt_hfp_ag *ag, char **number)
```

请求电话号码回调（Request phone number callback）。

提供此回调后，每当收到 `AT+BINP=1` 命令时都会调用。若上层接受请求，必须取得电话号码；若拒绝请求，则必须返回错误。未启用 `CONFIG_BT_HFP_AG_VOICE_TAG` 时，不通知此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ag` | 免提规范音频网关对象（HFP AG object）。 |
| `number` | 语音标签的电话号码（Phone number of voice tag）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="a9d6b978f82de6ded48881a87eb90aebb"></a>

### `retrieve`

```c
void(* bt_hfp_ag_cb::retrieve) (struct bt_hfp_ag_call *call)
```

免提设备恢复呼叫回调（HF call retrieve callback）。

提供此回调后，每次呼叫恢复（Retrieved）时都会调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `call` | 免提规范音频网关呼叫对象（HFP AG call object）。 |

<a id="a0b8967f487d64556851420b2f4e059fe"></a>

### `ringing`

```c
void(* bt_hfp_ag_cb::ringing) (struct bt_hfp_ag_call *call, bool in_band)
```

免提设备振铃回调（HF ringing callback）。

提供此回调后，每次呼叫处于振铃状态（Ringing）时都会调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `call` | 免提规范音频网关呼叫对象（HFP AG call object）。 |
| `in_band` | `true` 表示带内振铃（In-band ringing），`false` 表示无带内振铃。 |

<a id="aac2b1ff4d80361e0e5eea2481027b4cf"></a>

### `sco_connected`

```c
void(* bt_hfp_ag_cb::sco_connected) (struct bt_hfp_ag *ag, struct bt_conn *sco_conn)
```

免提同步／扩展同步面向连接链路连接回调（HF SCO/eSCO connected callback）。

提供此回调后，每次同步／扩展同步面向连接链路（SCO/eSCO）连接完成时都会调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ag` | 免提规范音频网关对象（HFP AG object）。 |
| `sco_conn` | 同步／扩展同步面向连接链路连接对象（SCO/eSCO Connection object）。 |

<a id="a95600361e59a516f220a314e920c5858"></a>

### `sco_disconnected`

```c
void(* bt_hfp_ag_cb::sco_disconnected) (struct bt_conn *sco_conn, uint8_t reason)
```

免提同步／扩展同步面向连接链路断开回调（HF SCO/eSCO disconnected callback）。

提供此回调后，每次同步／扩展同步面向连接链路（SCO/eSCO）断开时都会调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 同步／扩展同步面向连接链路连接对象（SCO/eSCO Connection object）。 |
| `reason` | 表示断开原因的 `BT_HCI_ERR_*` 值。 |

<a id="a976016f32e462daf38cd6d24ba18ff3d"></a>

### `subscriber_number`

```c
int(* bt_hfp_ag_cb::subscriber_number) (struct bt_hfp_ag *ag, bt_hfp_ag_query_subscriber_func_t func)
```

获取用户号码回调（Get subscriber number callback）。

提供此回调后，每当收到 `AT+CNUM` 命令时都会调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ag` | 免提规范音频网关对象（HFP AG object）。 |
| `func` | 查询用户号码回调（Query subscriber number callback）。 |

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="adf9960da8a3f4c38f7fcd60501522462"></a>

### `terminate`

```c
void(* bt_hfp_ag_cb::terminate) (struct bt_hfp_ag_call *call)
```

免提设备终止呼叫回调（HF call terminate callback）。

提供此回调后，每次呼叫终止（Terminated）时都会调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `call` | 免提规范音频网关呼叫对象（HFP AG call object）。 |

<a id="ad690d69c9786c69ad85e005e778b316c"></a>

### `transmit_dtmf_code`

```c
void(* bt_hfp_ag_cb::transmit_dtmf_code) (struct bt_hfp_ag *ag, char code)
```

发送双音多频代码回调（Transmit a DTMF Code callback）。

提供此回调后，每当收到 `AT+VTS=<code>` 命令时都会调用。在进行中的呼叫里，免提设备（HF）发送 `AT+VTS`，指示音频网关（AG）向其网络连接发送指定的双音多频代码（DTMF code）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ag` | 免提规范音频网关对象（HFP AG object）。 |
| `code` | 指定的双音多频代码（DTMF code）。 |

<a id="aaad37582866c420ee41c3f730de16eb4"></a>

### `vgm`

```c
void(* bt_hfp_ag_cb::vgm) (struct bt_hfp_ag *ag, uint8_t gain)
```

免提设备麦克风增益设置回调（HF VGM setting callback）。

提供此回调后，每当免提设备（HF）通知麦克风增益设置（VGM gain setting）时都会调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ag` | 免提规范音频网关对象（HFP AG object）。 |
| `gain` | 免提设备麦克风增益值（HF microphone gain value）。 |

<a id="a38adb040dee9abd794f952322bf3d615"></a>

### `vgs`

```c
void(* bt_hfp_ag_cb::vgs) (struct bt_hfp_ag *ag, uint8_t gain)
```

免提设备扬声器增益设置回调（HF VGS setting callback）。

提供此回调后，每当免提设备（HF）通知扬声器增益设置（VGS gain setting）时都会调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ag` | 免提规范音频网关对象（HFP AG object）。 |
| `gain` | 免提设备扬声器增益值（HF speaker gain value）。 |

<a id="a16c528018a2e9e97320df885c049454f"></a>

### `voice_recognition`

```c
void(* bt_hfp_ag_cb::voice_recognition) (struct bt_hfp_ag *ag, bool activate)
```

语音识别激活／停用回调（Voice recognition activation/deactivation callback）。

提供此回调后，每次语音识别激活状态（Voice recognition activation）变化时都会调用。语音识别已激活时，上层应使用适当编解码器标识符调用 `bt_hfp_ag_audio_connect`，建立音频连接。若上层未提供此回调，将使用默认编解码器标识符 `BT_HFP_AG_CODEC_CVSD` 调用该函数。未启用 `CONFIG_BT_HFP_AG_VOICE_RECG` 时，不通知此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ag` | 免提规范音频网关对象（HFP AG object）。 |
| `activate` | 语音识别激活／停用（Voice recognition activation/deactivation）。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/hfp_ag.h`

## 85.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/hfp_ag.h](https://docs.zephyrproject.org/latest/doxygen/html/hfp__ag_8h_source.html)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_hfp_ag](P083_bt_hfp_ag_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_hfp_ag_call](P084_bt_hfp_ag_call_结构体.md)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [bt_hfp_ag_query_subscriber_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga8e9b485f7ea0b9e16d96f578cdc587c3)
- [hfp_ag_hf_indicators](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga030c97d703fb45a2055653c51cb1b403)
- [bt_hfp_ag_audio_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga542a1754a16e32a9b2651f1230aa7066)
- [BT_HFP_AG_CODEC_CVSD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gada6266f825879f39147c5d889e4192c9)
- [CONFIG_BT_HFP_AG_ECNR](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HFP_AG_ECNR)
- [CONFIG_BT_HFP_AG_3WAY_CALL](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HFP_AG_3WAY_CALL)
- [bt_hfp_ag_service_availability()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#gaf838e54046c380931f23a59919ccfa5b)
- [signal](https://docs.zephyrproject.org/latest/doxygen/html/signal_8h.html#a5d326f119f87d0facaa662520f8c322a)
- [bt_hfp_ag_signal_strength()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga20ef1240e0ff72d914405b259cc3164f)
- [bt_hfp_ag_ongoing_calls()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html#ga5614bf3f1de11959a0364f458523e06e)
- [CONFIG_BT_HFP_AG_GET_ONGOING_CALL_TIMEOUT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HFP_AG_GET_ONGOING_CALL_TIMEOUT)
- [CONFIG_BT_HFP_AG_HF_INDICATORS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HFP_AG_HF_INDICATORS)
- [CONFIG_BT_HFP_AG_ENH_VOICE_RECG](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HFP_AG_ENH_VOICE_RECG)
- [CONFIG_BT_HFP_AG_PHONE_NUMBER_MAX_LEN](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HFP_AG_PHONE_NUMBER_MAX_LEN)
- [CONFIG_BT_HFP_AG_VOICE_TAG](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HFP_AG_VOICE_TAG)
- [CONFIG_BT_HFP_AG_VOICE_RECG](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HFP_AG_VOICE_RECG)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P084_bt_hfp_ag_call_结构体.md) · [返回大纲](大纲.md) · [下一章](P086_bt_hfp_ag_ongoing_call_结构体.md)
