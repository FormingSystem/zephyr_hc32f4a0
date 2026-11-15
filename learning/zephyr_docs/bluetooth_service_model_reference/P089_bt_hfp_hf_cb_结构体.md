---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-89
title: bt_hfp_hf_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hfp__hf__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第89章\_bt\_hfp\_hf\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hfp__hf__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

免提配置文件（HFP）的应用回调。

```c
#include <zephyr/bluetooth/classic/hfp_hf.h>
```

<a id="details"></a>

免提配置文件（HFP）的应用回调。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 89.1\_数据成员（Data Fields）

<a id="r_a68c09fe6aac4ff7f3b24e6a550e75d1e"></a>

```c
void(* connected )(struct bt_conn *conn, struct bt_hfp_hf *hf)
```

相关声明：[connected](#a68c09fe6aac4ff7f3b24e6a550e75d1e)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_hfp_hf](P087_bt_hfp_hf_结构体.md)。

通知应用的免提设备连接回调（HF connected callback）。

<a id="r_afdf28b8d8f9598ee2f6fa826aba4fbba"></a>

```c
void(* disconnected )(struct bt_hfp_hf *hf)
```

相关声明：[disconnected](#afdf28b8d8f9598ee2f6fa826aba4fbba)、[bt_hfp_hf](P087_bt_hfp_hf_结构体.md)。

通知应用的免提设备断开回调（HF disconnected callback）。

<a id="r_a6ea6f5a866d7e4da5e3fe894d700f6b6"></a>

```c
void(* sco_connected )(struct bt_hfp_hf *hf, struct bt_conn *sco_conn)
```

相关声明：[sco_connected](#a6ea6f5a866d7e4da5e3fe894d700f6b6)、[bt_hfp_hf](P087_bt_hfp_hf_结构体.md)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

免提同步／扩展同步面向连接链路连接回调（HF SCO/eSCO connected callback）。

<a id="r_a4586240506c876c9f58cf60a091b4044"></a>

```c
void(* sco_disconnected )(struct bt_conn *sco_conn, uint8_t reason)
```

相关声明：[sco_disconnected](#a4586240506c876c9f58cf60a091b4044)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

免提同步／扩展同步面向连接链路断开回调（HF SCO/eSCO disconnected callback）。

<a id="r_a8483c3a3ba8b0e5131bec6fce5dbc36d"></a>

```c
void(* service )(struct bt_hfp_hf *hf, uint32_t value)
```

相关声明：[service](#a8483c3a3ba8b0e5131bec6fce5dbc36d)、[bt_hfp_hf](P087_bt_hfp_hf_结构体.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

免提设备指示器回调（HF indicator callback）。

<a id="r_a46677dbfe7e73dcdc3b6cacb0aa9fa58"></a>

```c
void(* outgoing )(struct bt_hfp_hf *hf, struct bt_hfp_hf_call *call)
```

相关声明：[outgoing](#a46677dbfe7e73dcdc3b6cacb0aa9fa58)、[bt_hfp_hf](P087_bt_hfp_hf_结构体.md)、[bt_hfp_hf_call](P088_bt_hfp_hf_call_结构体.md)。

免提设备呼叫呼出回调（HF call outgoing callback）。

<a id="r_ace8989f64fea9301d6f48e5252ceb2de"></a>

```c
void(* remote_ringing )(struct bt_hfp_hf_call *call)
```

相关声明：[remote_ringing](#ace8989f64fea9301d6f48e5252ceb2de)、[bt_hfp_hf_call](P088_bt_hfp_hf_call_结构体.md)。

免提设备呼出呼叫振铃回调（HF outgoing call ringing callback）。

<a id="r_a597d2e9b20ffc2dfedd53aea2969727e"></a>

```c
void(* incoming )(struct bt_hfp_hf *hf, struct bt_hfp_hf_call *call)
```

相关声明：[incoming](#a597d2e9b20ffc2dfedd53aea2969727e)、[bt_hfp_hf](P087_bt_hfp_hf_结构体.md)、[bt_hfp_hf_call](P088_bt_hfp_hf_call_结构体.md)。

免提设备呼叫来电回调（HF call incoming callback）。

<a id="r_a71f0f50a83defe014b3b364dcc16ad9d"></a>

```c
void(* incoming_held )(struct bt_hfp_hf_call *call)
```

相关声明：[incoming_held](#a71f0f50a83defe014b3b364dcc16ad9d)、[bt_hfp_hf_call](P088_bt_hfp_hf_call_结构体.md)。

免提设备来电保持回调（HF incoming call on hold callback）。

<a id="r_a44ae68eb055f23c30dd761fd6eb1c6cd"></a>

```c
void(* accept )(struct bt_hfp_hf_call *call)
```

相关声明：[accept](#a44ae68eb055f23c30dd761fd6eb1c6cd)、[bt_hfp_hf_call](P088_bt_hfp_hf_call_结构体.md)。

免提设备接受呼叫回调（HF call accept callback）。

<a id="r_a9f248f9c7e3830c6941225bd4d2363d3"></a>

```c
void(* reject )(struct bt_hfp_hf_call *call)
```

相关声明：[reject](#a9f248f9c7e3830c6941225bd4d2363d3)、[bt_hfp_hf_call](P088_bt_hfp_hf_call_结构体.md)。

免提设备拒绝呼叫回调（HF call reject callback）。

<a id="r_a691ec076d6fba14636b873cf75262e81"></a>

```c
void(* terminate )(struct bt_hfp_hf_call *call)
```

相关声明：[terminate](#a691ec076d6fba14636b873cf75262e81)、[bt_hfp_hf_call](P088_bt_hfp_hf_call_结构体.md)。

免提设备终止呼叫回调（HF call terminate callback）。

<a id="r_af6fe24140f5a5a1aea2eff7b1e534cfd"></a>

```c
void(* held )(struct bt_hfp_hf_call *call)
```

相关声明：[held](#af6fe24140f5a5a1aea2eff7b1e534cfd)、[bt_hfp_hf_call](P088_bt_hfp_hf_call_结构体.md)。

免提设备呼叫保持回调（HF call held callback）。

<a id="r_a4977076381a5c4daf620aa6c6ab558d3"></a>

```c
void(* retrieve )(struct bt_hfp_hf_call *call)
```

相关声明：[retrieve](#a4977076381a5c4daf620aa6c6ab558d3)、[bt_hfp_hf_call](P088_bt_hfp_hf_call_结构体.md)。

免提设备恢复呼叫回调（HF call retrieve callback）。

<a id="r_add68ca4e00f7a5dbc28282ee29bea087"></a>

```c
void(* signal )(struct bt_hfp_hf *hf, uint32_t value)
```

相关声明：[signal](#add68ca4e00f7a5dbc28282ee29bea087)、[bt_hfp_hf](P087_bt_hfp_hf_结构体.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

免提设备指示器回调（HF indicator callback）。

<a id="r_a13b35eb32e4f579d853657a2ea89af42"></a>

```c
void(* roam )(struct bt_hfp_hf *hf, uint32_t value)
```

相关声明：[roam](#a13b35eb32e4f579d853657a2ea89af42)、[bt_hfp_hf](P087_bt_hfp_hf_结构体.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

免提设备指示器回调（HF indicator callback）。

<a id="r_a17faaab9a9af5dc53018fc2f94855bea"></a>

```c
void(* battery )(struct bt_hfp_hf *hf, uint32_t value)
```

相关声明：[battery](#a17faaab9a9af5dc53018fc2f94855bea)、[bt_hfp_hf](P087_bt_hfp_hf_结构体.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

免提设备指示器回调（HF indicator callback）。

<a id="r_a2712d3a5d68bdf2de6dc27f938590c0a"></a>

```c
void(* ring_indication )(struct bt_hfp_hf_call *call)
```

相关声明：[ring_indication](#a2712d3a5d68bdf2de6dc27f938590c0a)、[bt_hfp_hf_call](P088_bt_hfp_hf_call_结构体.md)。

通知应用的免提设备来电振铃指示回调（HF incoming call Ring indication callback）。

<a id="r_a80e98b5dd212158c255215b8a304d67c"></a>

```c
void(* dialing )(struct bt_hfp_hf *hf, int err)
```

相关声明：[dialing](#a80e98b5dd212158c255215b8a304d67c)、[bt_hfp_hf](P087_bt_hfp_hf_结构体.md)。

免提设备拨号回调（HF call dialing callback）。

<a id="r_ac049a95f473eb2e31ed4bba665861429"></a>

```c
void(* clip )(struct bt_hfp_hf_call *call, const char *number, uint8_t type)
```

相关声明：[clip](#ac049a95f473eb2e31ed4bba665861429)、[bt_hfp_hf_call](P088_bt_hfp_hf_call_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

通知应用的免提设备主叫线路标识回调（HF calling line identification notification callback）。

<a id="r_a512de9839559def9c2110a310f21ca03"></a>

```c
void(* vgm )(struct bt_hfp_hf *hf, uint8_t gain)
```

相关声明：[vgm](#a512de9839559def9c2110a310f21ca03)、[bt_hfp_hf](P087_bt_hfp_hf_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

通知应用的免提设备麦克风增益回调（HF microphone gain notification callback）。

<a id="r_a385cbe2c3a9c402a09b873a3ce753d8b"></a>

```c
void(* vgs )(struct bt_hfp_hf *hf, uint8_t gain)
```

相关声明：[vgs](#a385cbe2c3a9c402a09b873a3ce753d8b)、[bt_hfp_hf](P087_bt_hfp_hf_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

通知应用的免提设备扬声器增益回调（HF speaker gain notification callback）。

<a id="r_acc1ff77f98329986c2120b0c9c4f565a"></a>

```c
void(* inband_ring )(struct bt_hfp_hf *hf, bool inband)
```

相关声明：[inband_ring](#acc1ff77f98329986c2120b0c9c4f565a)、[bt_hfp_hf](P087_bt_hfp_hf_结构体.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

通知应用的免提设备带内铃声回调（HF in-band ring tone notification callback）。

<a id="r_ac58cfe5afaf2e8b8bfa9416e624275ec"></a>

```c
void(*)(struct bt_hfp_hf *hf, uint8_t id) operator) (struct bt_hfp_hf *hf, uint8_t mode, uint8_t format, const char *operator);void(*codec_negotiate
```

相关声明：[bt_hfp_hf](P087_bt_hfp_hf_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[operator)](#ac58cfe5afaf2e8b8bfa9416e624275ec)、[bt_hfp_hf](P087_bt_hfp_hf_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

通知应用的免提设备网络运营商回调（HF network operator notification callback）。

<a id="r_a0f2da8d9169658c03d2dabe2c8b1cf6f"></a>

```c
void(* ecnr_turn_off )(struct bt_hfp_hf *hf, int err)
```

相关声明：[ecnr_turn_off](#a0f2da8d9169658c03d2dabe2c8b1cf6f)、[bt_hfp_hf](P087_bt_hfp_hf_结构体.md)。

免提设备关闭回声消除与降噪回调（HF ECNR turns off callback）。

<a id="r_a5083ff06bbe2ed2611a7c67339a82588"></a>

```c
void(* call_waiting )(struct bt_hfp_hf_call *call, const char *number, uint8_t type)
```

相关声明：[call_waiting](#a5083ff06bbe2ed2611a7c67339a82588)、[bt_hfp_hf_call](P088_bt_hfp_hf_call_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

通知应用的免提设备呼叫等待回调（HF call waiting notification callback）。

<a id="r_a07da1a6c86031c42749972d5d9fb7677"></a>

```c
void(* voice_recognition )(struct bt_hfp_hf *hf, bool activate)
```

相关声明：[voice_recognition](#a07da1a6c86031c42749972d5d9fb7677)、[bt_hfp_hf](P087_bt_hfp_hf_结构体.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

语音识别激活／停用回调（Voice recognition activation/deactivation callback）。

<a id="r_a298a6d3315535331ffb779899db9f973"></a>

```c
void(* vre_state )(struct bt_hfp_hf *hf, uint8_t state)
```

相关声明：[vre_state](#a298a6d3315535331ffb779899db9f973)、[bt_hfp_hf](P087_bt_hfp_hf_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)。

语音识别引擎状态回调（Voice recognition engine state callback）。

<a id="r_ada56afdf999f5270f84fcf412916e550"></a>

```c
void(* textual_representation )(struct bt_hfp_hf *hf, char *id, uint8_t type, uint8_t operation, const char *text)
```

相关声明：[textual_representation](#ada56afdf999f5270f84fcf412916e550)、[bt_hfp_hf](P087_bt_hfp_hf_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

文本表示回调（Textual representation callback）。

<a id="r_ac1e9fb5d0446d498b6cf3705a05633e2"></a>

```c
void(* request_phone_number )(struct bt_hfp_hf *hf, const char *number)
```

相关声明：[request_phone_number](#ac1e9fb5d0446d498b6cf3705a05633e2)、[bt_hfp_hf](P087_bt_hfp_hf_结构体.md)。

请求电话号码回调（Request phone number callback）。

<a id="r_ae5682d96bdf18b148fac7ce1d9cbdb75"></a>

```c
void(* subscriber_number )(struct bt_hfp_hf *hf, const char *number, uint8_t type, uint8_t service)
```

相关声明：[subscriber_number](#ae5682d96bdf18b148fac7ce1d9cbdb75)、[bt_hfp_hf](P087_bt_hfp_hf_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[service](#a8483c3a3ba8b0e5131bec6fce5dbc36d)。

查询用户号码回调（Query subscriber number callback）。

<a id="r_a080d9149f6d0beccbcf6562e3129383a"></a>

```c
void(* query_call )(struct bt_hfp_hf *hf, struct bt_hfp_hf_current_call *call)
```

相关声明：[query_call](#a080d9149f6d0beccbcf6562e3129383a)、[bt_hfp_hf](P087_bt_hfp_hf_结构体.md)、[bt_hfp_hf_current_call](P090_bt_hfp_hf_current_call_结构体.md)。

查询当前呼叫列表回调（Query list of current calls callback）。

## 89.2\_详细说明（Detailed Documentation）

<a id="a44ae68eb055f23c30dd761fd6eb1c6cd"></a>

### `accept`

```c
void(* bt_hfp_hf_cb::accept) (struct bt_hfp_hf_call *call)
```

免提设备接受呼叫回调（HF call accept callback）。

此回调向应用提供来电／呼出的活动状态（Incoming/outgoing call active status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `call` | 免提规范免提端呼叫对象（HFP HF call object）。 |

<a id="a17faaab9a9af5dc53018fc2f94855bea"></a>

### `battery`

```c
void(* bt_hfp_hf_cb::battery) (struct bt_hfp_hf *hf, uint32_t value)
```

免提设备指示器回调（HF indicator callback）。

此回调向应用提供电池服务指示器值（Battery service indicator value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hf` | 免提规范免提端对象（HFP HF object）。 |
| `value` | 从音频网关（AG）收到的电池指示器值（Battery indicator value）。 |

<a id="a5083ff06bbe2ed2611a7c67339a82588"></a>

### `call_waiting`

```c
void(* bt_hfp_hf_cb::call_waiting) (struct bt_hfp_hf_call *call, const char *number, uint8_t type)
```

通知应用的免提设备呼叫等待回调（HF call waiting notification callback）。

提供此回调后，每当收到主动结果码（Unsolicited result code）`+CCWA` 时都会调用。可通过 `bt_hfp_hf_call_waiting_notify` 启用或禁用此通知。未启用 `CONFIG_BT_HFP_HF_3WAY_CALL` 时，将忽略 `+CCWA`，也不会通知回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `call` | 免提规范免提端呼叫对象（HFP HF call object）。 |
| `number` | 通知的电话号码（Notified phone number）。 |
| `type` | 指定电话号码格式（Phone number format）。 |

<a id="ac049a95f473eb2e31ed4bba665861429"></a>

### `clip`

```c
void(* bt_hfp_hf_cb::clip) (struct bt_hfp_hf_call *call, const char *number, uint8_t type)
```

通知应用的免提设备主叫线路标识回调（HF calling line identification notification callback）。

提供此回调后，每当收到主动结果码（Unsolicited result code）`+CLIP` 时都会调用。未启用 `CONFIG_BT_HFP_HF_CLI` 时，将忽略 `+CLIP`，也不会通知回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `call` | 免提规范免提端呼叫对象（HFP HF call object）。 |
| `number` | 通知的电话号码（Notified phone number）。 |
| `type` | 指定电话号码格式（Phone number format）。 |

<a id="a68c09fe6aac4ff7f3b24e6a550e75d1e"></a>

### `connected`

```c
void(* bt_hfp_hf_cb::connected) (struct bt_conn *conn, struct bt_hfp_hf *hf)
```

通知应用的免提设备连接回调（HF connected callback）。

提供此回调后，每次连接完成（Connection completes）都会调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `hf` | 免提规范免提端对象（HFP HF object）。 |

<a id="a80e98b5dd212158c255215b8a304d67c"></a>

### `dialing`

```c
void(* bt_hfp_hf_cb::dialing) (struct bt_hfp_hf *hf, int err)
```

免提设备拨号回调（HF call dialing callback）。

此回调向应用提供呼叫拨号结果（Call dialing result）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hf` | 免提规范免提端对象（HFP HF object）。 |
| `err` | 呼叫拨号结果（Call dialing result）。 |

<a id="afdf28b8d8f9598ee2f6fa826aba4fbba"></a>

### `disconnected`

```c
void(* bt_hfp_hf_cb::disconnected) (struct bt_hfp_hf *hf)
```

通知应用的免提设备断开回调（HF disconnected callback）。

提供此回调后，每次连接断开时都会调用，包括连接被拒绝、被取消，或建立服务级连接（SLC）过程中发生错误。已注册的 `disconnected` 回调返回后，将释放免提规范免提端对象（HFP HF object）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hf` | 免提规范免提端对象（HFP HF object）。 |

<a id="a0f2da8d9169658c03d2dabe2c8b1cf6f"></a>

### `ecnr_turn_off`

```c
void(* bt_hfp_hf_cb::ecnr_turn_off) (struct bt_hfp_hf *hf, int err)
```

免提设备关闭回声消除与降噪回调（HF ECNR turns off callback）。

提供此回调后，每当从音频网关（AG）收到关闭回声消除与降噪（ECNR）的响应时都会调用。未启用 `CONFIG_BT_HFP_HF_ECNR` 时，不通知回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hf` | 免提规范免提端对象（HFP HF object）。 |
| `err` | 请求结果（Request result）。 |

<a id="af6fe24140f5a5a1aea2eff7b1e534cfd"></a>

### `held`

```c
void(* bt_hfp_hf_cb::held) (struct bt_hfp_hf_call *call)
```

免提设备呼叫保持回调（HF call held callback）。

此回调向应用通知呼叫保持（Call held）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `call` | 免提规范免提端呼叫对象（HFP HF call object）。 |

<a id="acc1ff77f98329986c2120b0c9c4f565a"></a>

### `inband_ring`

```c
void(* bt_hfp_hf_cb::inband_ring) (struct bt_hfp_hf *hf, bool inband)
```

通知应用的免提设备带内铃声回调（HF in-band ring tone notification callback）。

提供此回调后，每当音频网关（AG）发出主动结果码（Unsolicited result code）`+BSIR` 时都会调用；此结果码向免提设备（HF）指示，AG 已在本地更改带内铃声设置（In-band ring tone setting）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hf` | 免提规范免提端对象（HFP HF object）。 |
| `inband` | 来自音频网关（AG）的带内铃声状态（In-band ring tone status）。 |

<a id="a597d2e9b20ffc2dfedd53aea2969727e"></a>

### `incoming`

```c
void(* bt_hfp_hf_cb::incoming) (struct bt_hfp_hf *hf, struct bt_hfp_hf_call *call)
```

免提设备呼叫来电回调（HF call incoming callback）。

此回调向应用提供来电状态（Incoming call status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hf` | 免提规范免提端对象（HFP HF object）。 |
| `call` | 免提规范免提端呼叫对象（HFP HF call object）。 |

<a id="a71f0f50a83defe014b3b364dcc16ad9d"></a>

### `incoming_held`

```c
void(* bt_hfp_hf_cb::incoming_held) (struct bt_hfp_hf_call *call)
```

免提设备来电保持回调（HF incoming call on hold callback）。

此回调向应用提供来电保持状态（Incoming call on hold status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `call` | 免提规范免提端呼叫对象（HFP HF call object）。 |

<a id="ac58cfe5afaf2e8b8bfa9416e624275ec"></a>

### `operator)`

```c
void(*)(struct bt_hfp_hf *hf, uint8_t id) bt_hfp_hf_cb::operator)(struct bt_hfp_hf *hf, uint8_t mode, uint8_t format, const char *operator); void(*codec_negotiate
```

通知应用的免提设备网络运营商回调（HF network operator notification callback）。

免提设备（HF）通过 `bt_hfp_hf_get_operator` 发送 `AT+COPS?` 命令后，音频网关（AG）以 `+COPS` 响应；若提供此回调，则收到该响应码时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hf` | 免提规范免提端对象（HFP HF object）。 |
| `mode` | 当前模式（Current mode）。 |
| `format` | 运营商参数字符串的格式（Operator parameter string format），应为零。 |
| `operator` | 用字母数字格式表示网络运营商名称（Network operator name）的字符串。 |

<a id="a46677dbfe7e73dcdc3b6cacb0aa9fa58"></a>

### `outgoing`

```c
void(* bt_hfp_hf_cb::outgoing) (struct bt_hfp_hf *hf, struct bt_hfp_hf_call *call)
```

免提设备呼叫呼出回调（HF call outgoing callback）。

此回调向应用提供呼出状态（Outgoing call status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hf` | 免提规范免提端对象（HFP HF object）。 |
| `call` | 免提规范免提端呼叫对象（HFP HF call object）。 |

<a id="a080d9149f6d0beccbcf6562e3129383a"></a>

### `query_call`

```c
void(* bt_hfp_hf_cb::query_call) (struct bt_hfp_hf *hf, struct bt_hfp_hf_current_call *call)
```

查询当前呼叫列表回调（Query list of current calls callback）。

提供此回调后，每当从音频网关（AG）收到结果码 `+CLCC: <idx>,<dir>,<status>,<mode>,<mprty>[,<number>,<type>]` 时都会调用。请求失败或没有活动呼叫时不调用。若 `bt_hfp_hf_current_call::number` 为 `NULL`，必须忽略 `bt_hfp_hf_current_call::type`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hf` | 免提规范免提端对象（HFP HF object）。 |
| `call` | 当前呼叫信息（Current call information）。 |

<a id="a9f248f9c7e3830c6941225bd4d2363d3"></a>

### `reject`

```c
void(* bt_hfp_hf_cb::reject) (struct bt_hfp_hf_call *call)
```

免提设备拒绝呼叫回调（HF call reject callback）。

此回调向应用提供来电／呼出被拒绝状态（Incoming/outgoing call reject status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `call` | 免提规范免提端呼叫对象（HFP HF call object）。 |

<a id="ace8989f64fea9301d6f48e5252ceb2de"></a>

### `remote_ringing`

```c
void(* bt_hfp_hf_cb::remote_ringing) (struct bt_hfp_hf_call *call)
```

免提设备呼出呼叫振铃回调（HF outgoing call ringing callback）。

此回调向应用提供呼出呼叫振铃状态（Outgoing call ringing status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `call` | 免提规范免提端呼叫对象（HFP HF call object）。 |

<a id="ac1e9fb5d0446d498b6cf3705a05633e2"></a>

### `request_phone_number`

```c
void(* bt_hfp_hf_cb::request_phone_number) (struct bt_hfp_hf *hf, const char *number)
```

请求电话号码回调（Request phone number callback）。

提供此回调后，每当从音频网关（AG）收到结果码 `+BINP: <Phone number>` 时都会调用。请求失败时，号码为 `NULL`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hf` | 免提规范免提端对象（HFP HF object）。 |
| `number` | `<Phone number>` 的值，即电话号码。 |

<a id="a4977076381a5c4daf620aa6c6ab558d3"></a>

### `retrieve`

```c
void(* bt_hfp_hf_cb::retrieve) (struct bt_hfp_hf_call *call)
```

免提设备恢复呼叫回调（HF call retrieve callback）。

此回调向应用通知呼叫恢复（Call retrieved）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `call` | 免提规范免提端呼叫对象（HFP HF call object）。 |

<a id="a2712d3a5d68bdf2de6dc27f938590c0a"></a>

### `ring_indication`

```c
void(* bt_hfp_hf_cb::ring_indication) (struct bt_hfp_hf_call *call)
```

通知应用的免提设备来电振铃指示回调（HF incoming call Ring indication callback）。

提供此回调后，每次有来电（Incoming call）时都会调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `call` | 免提规范免提端呼叫对象（HFP HF call object）。 |

<a id="a13b35eb32e4f579d853657a2ea89af42"></a>

### `roam`

```c
void(* bt_hfp_hf_cb::roam) (struct bt_hfp_hf *hf, uint32_t value)
```

免提设备指示器回调（HF indicator callback）。

此回调向应用提供漫游指示器（roaming indicator）的值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hf` | 免提规范免提端对象（HFP HF object）。 |
| `value` | 从音频网关（AG）收到的漫游指示器值。 |

<a id="a6ea6f5a866d7e4da5e3fe894d700f6b6"></a>

### `sco_connected`

```c
void(* bt_hfp_hf_cb::sco_connected) (struct bt_hfp_hf *hf, struct bt_conn *sco_conn)
```

免提同步／扩展同步面向连接链路连接回调（HF SCO/eSCO connected callback）。

提供此回调后，每次同步／扩展同步面向连接链路（SCO/eSCO）连接完成时都会调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hf` | 免提规范免提端对象（HFP HF object）。 |
| `sco_conn` | 同步／扩展同步面向连接链路连接对象（SCO/eSCO Connection object）。 |

<a id="a4586240506c876c9f58cf60a091b4044"></a>

### `sco_disconnected`

```c
void(* bt_hfp_hf_cb::sco_disconnected) (struct bt_conn *sco_conn, uint8_t reason)
```

免提同步／扩展同步面向连接链路断开回调（HF SCO/eSCO disconnected callback）。

提供此回调后，每次同步／扩展同步面向连接链路（SCO/eSCO）断开时都会调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 同步／扩展同步面向连接链路连接对象（SCO/eSCO Connection object）。 |
| `reason` | 表示断开原因的 `BT_HCI_ERR_*` 值。 |

<a id="a8483c3a3ba8b0e5131bec6fce5dbc36d"></a>

### `service`

```c
void(* bt_hfp_hf_cb::service) (struct bt_hfp_hf *hf, uint32_t value)
```

免提设备指示器回调（HF indicator callback）。

此回调向应用提供服务指示器（service indicator）的值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hf` | 免提规范免提端对象（HFP HF object）。 |
| `value` | 从音频网关（AG）收到的服务指示器值。 |

<a id="add68ca4e00f7a5dbc28282ee29bea087"></a>

### `signal`

```c
void(* bt_hfp_hf_cb::signal) (struct bt_hfp_hf *hf, uint32_t value)
```

免提设备指示器回调（HF indicator callback）。

此回调向应用提供信号指示器（signal indicator）的值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hf` | 免提规范免提端对象（HFP HF object）。 |
| `value` | 从音频网关（AG）收到的信号指示器值。 |

<a id="ae5682d96bdf18b148fac7ce1d9cbdb75"></a>

### `subscriber_number`

```c
void(* bt_hfp_hf_cb::subscriber_number) (struct bt_hfp_hf *hf, const char *number, uint8_t type, uint8_t service)
```

查询用户号码回调（Query subscriber number callback）。

如果提供了此回调，每当收到音频网关（AG）发送的结果码 `+CUNM: [<alpha>],<number>, <type>,[<speed> ,<service>]` 时都会调用它。`<alpha>`：不支持此可选字段，必须留空。`<number>`：用引号括起的电话号码字符串，其格式由 `<type>` 指定。`<type>` 字段指定所提供电话号码的格式，可以是下列值之一：

译注：此处按官方原文保留结果码拼写 `+CUNM`。

- 取值 128 至 143：电话号码可以采用国内或国际格式，并且可以包含前缀数字和/或转义数字。无需更改号码的呈现形式。
- 取值 144 至 159：电话号码采用国际格式，包含国家代码前缀。如果号码中尚未包含加号（`+`），则音频网关（AG）应按需添加。
- 取值 160 至 175：国内号码，不包含前缀数字或转义数字。`<speed>`：不支持此可选字段，必须留空。`<service>`：指示此电话号码所属的服务，必须为 4（语音）或 5（传真）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hf` | 免提规范免提端对象（HFP HF object）。 |
| `number` | 不含引号的 `<number>` 值。 |
| `type` | `<type>` 的值。 |
| `service` | `<service>` 的值。 |

<a id="a691ec076d6fba14636b873cf75262e81"></a>

### `terminate`

```c
void(* bt_hfp_hf_cb::terminate) (struct bt_hfp_hf_call *call)
```

免提设备终止呼叫回调（HF call terminate callback）。

此回调向应用提供呼入或呼出通话的终止状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `call` | 免提规范免提端呼叫对象（HFP HF call object）。 |

<a id="ada56afdf999f5270f84fcf412916e550"></a>

### `textual_representation`

```c
void(* bt_hfp_hf_cb::textual_representation) (struct bt_hfp_hf *hf, char *id, uint8_t type, uint8_t operation, const char *text)
```

文本表示回调（Textual representation callback）。

如果提供了此回调，每当收到音频网关（AG）发送的非请求结果码（unsolicited result code）`+BVRA: 1,<vrecstate>, <textualRepresentation>` 时都会调用它。`<textualRepresentation>` 的格式为 `<textID>,<textType>,<textOperation>,<string>`。`<textID>`：当前文本的唯一标识符，以十六进制字符串表示，最多 4 个字符，少于 4 个字符也有效。`<textType>`：文本类型标识符，取值如下：0——AG 从免提设备（HF）提供的音频输入中识别出的文本；1——AG 音频输出对应的文本；2——AG 音频输出对应且包含问题的文本；3——AG 音频输出对应且包含错误描述的文本。`<textOperation>`：文本操作标识符，取值如下：1——新文本（NewText），表示开始一段新文本；当 `<textID>` 变化时必须使用此操作。2——替换（Replace），替换具有相同 `<textID>` 和相同 `<textType>` 的任何已有文本。3——追加（Append），将新文本附加到已有文本，并保持相同的 `<textID>` 和 `<textType>`。`<string>`：必须是 UTF-8 文本字符串，而且始终用双引号括起。如果未启用 `CONFIG_BT_HFP_HF_VOICE_RECG_TEXT`，则忽略非请求结果码 `+BVRA`，也不会调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hf` | 免提规范免提端对象（HFP HF object）。 |
| `id` | `<textID>` 的值。 |
| `type` | `<textType>` 的值。 |
| `operation` | `<textOperation>` 的值。 |
| `text` | `<string>` 的值。 |

<a id="a512de9839559def9c2110a310f21ca03"></a>

### `vgm`

```c
void(* bt_hfp_hf_cb::vgm) (struct bt_hfp_hf *hf, uint8_t gain)
```

通知应用的免提设备麦克风增益回调（HF microphone gain notification callback）。

如果提供了此回调，每当收到非请求结果码 `+VGM` 时都会调用它。如果未启用 `CONFIG_BT_HFP_HF_VOLUME`，则忽略非请求结果码 `+VGM`，也不会调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hf` | 免提规范免提端对象（HFP HF object）。 |
| `gain` | 麦克风增益（Microphone gain）。 |

<a id="a385cbe2c3a9c402a09b873a3ce753d8b"></a>

### `vgs`

```c
void(* bt_hfp_hf_cb::vgs) (struct bt_hfp_hf *hf, uint8_t gain)
```

通知应用的免提设备扬声器增益回调（HF speaker gain notification callback）。

如果提供了此回调，每当收到非请求结果码 `+VGS` 时都会调用它。如果未启用 `CONFIG_BT_HFP_HF_VOLUME`，则忽略非请求结果码 `+VGS`，也不会调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hf` | 免提规范免提端对象（HFP HF object）。 |
| `gain` | 扬声器增益（Speaker gain）。 |

<a id="a07da1a6c86031c42749972d5d9fb7677"></a>

### `voice_recognition`

```c
void(* bt_hfp_hf_cb::voice_recognition) (struct bt_hfp_hf *hf, bool activate)
```

语音识别激活／停用回调（Voice recognition activation/deactivation callback）。

如果提供了此回调，当音频网关（AG）自主启用或停用其语音识别功能，并通过非请求结果码 `+BVRA` 通知免提设备（HF）时，就会调用它。如果未启用 `CONFIG_BT_HFP_HF_VOICE_RECG`，则忽略非请求结果码 `+BVRA`，也不会调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hf` | 免提规范免提端对象（HFP HF object）。 |
| `activate` | 语音识别激活／停用（Voice recognition activation/deactivation）。 |

<a id="a298a6d3315535331ffb779899db9f973"></a>

### `vre_state`

```c
void(* bt_hfp_hf_cb::vre_state) (struct bt_hfp_hf *hf, uint8_t state)
```

语音识别引擎状态回调（Voice recognition engine state callback）。

如果提供了此回调，每当收到音频网关（AG）发送的非请求结果码 `+BVRA: 1,<vrecstate>` 时都会调用它。`<vrecstate>`：反映 AG 上语音识别引擎当前状态的位掩码（bitmask）。位 0 为 1 表示 AG 已准备好接收音频输入；位 1 为 1 表示 AG 正在向免提设备（HF）发送音频；位 2 为 1 表示 AG 正在处理音频输入。如果未启用 `CONFIG_BT_HFP_HF_ENH_VOICE_RECG`，则忽略非请求结果码 `+BVRA`，也不会调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hf` | 免提规范免提端对象（HFP HF object）。 |
| `state` | `<vrecstate>` 的值。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/hfp_hf.h`

## 89.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/hfp_hf.h](https://docs.zephyrproject.org/latest/doxygen/html/hfp__hf_8h_source.html)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_hfp_hf](P087_bt_hfp_hf_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [bt_hfp_hf_call](P088_bt_hfp_hf_call_结构体.md)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)
- [bt_hfp_hf_current_call](P090_bt_hfp_hf_current_call_结构体.md)
- [bt_hfp_hf_call_waiting_notify](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#ga3afb0d82551708975dbeb9c903c3d1fb)
- [CONFIG_BT_HFP_HF_3WAY_CALL](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HFP_HF_3WAY_CALL)
- [CONFIG_BT_HFP_HF_CLI](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HFP_HF_CLI)
- [CONFIG_BT_HFP_HF_ECNR](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HFP_HF_ECNR)
- [bt_hfp_hf_get_operator](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html#gaaa9fbdceec140f274fc88c063a4cd4b8)
- [bt_hfp_hf_current_call::number](P090_bt_hfp_hf_current_call_结构体.md#ac384ffbde33c521f305f1283520e0c66)
- [bt_hfp_hf_current_call::type](P090_bt_hfp_hf_current_call_结构体.md#a6cefa6a215650f8380a54cda44ce5f19)
- [CONFIG_BT_HFP_HF_VOICE_RECG_TEXT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HFP_HF_VOICE_RECG_TEXT)
- [CONFIG_BT_HFP_HF_VOLUME](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HFP_HF_VOLUME)
- [CONFIG_BT_HFP_HF_VOICE_RECG](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HFP_HF_VOICE_RECG)
- [CONFIG_BT_HFP_HF_ENH_VOICE_RECG](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HFP_HF_ENH_VOICE_RECG)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P088_bt_hfp_hf_call_结构体.md) · [返回大纲](大纲.md) · [下一章](P090_bt_hfp_hf_current_call_结构体.md)
