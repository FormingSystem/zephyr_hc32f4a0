---
id: learning.zephyr-docs.api-file-bluetooth-media-reference.page-12
title: zephyr__bluetooth__audio__tbs.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/tbs_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_zephyr\_\_bluetooth\_\_audio\_\_tbs.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/tbs_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙电话承载服务（Telephone Bearer Service）的公共API。

<a id="details"></a>

```c
#include <stdint.h>
#include <stdbool.h>
#include <zephyr/bluetooth/assigned_numbers.h>
#include <zephyr/bluetooth/conn.h>
#include <zephyr/sys/slist.h>
#include <zephyr/sys/util_macro.h>
```

查看此文件的源码。

蓝牙电话承载服务（Bluetooth Telephone Bearer Service）的公共 API。

Copyright (c) 2020 Bose Corporation

Copyright (c) 2021-2026 Nordic Semiconductor ASA

SPDX-License-Identifier: Apache-2.0

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 12.1\_数据结构（Data Structures）

<a id="r_bt_5Ftbs_5Fcb"></a>

```c
struct bt_tbs_cb
```

相关声明：[bt_tbs_cb](../bluetooth_service_model_reference/P172_bt_tbs_cb_结构体.md)。

保存电话承载服务（Telephone Bearer Service）回调的结构。

<a id="r_bt_5Ftbs_5Fregister_5Fparam"></a>

```c
struct bt_tbs_register_param
```

相关声明：[bt_tbs_register_param](../bluetooth_service_model_reference/P177_bt_tbs_register_param_结构体.md)。

注册电话承载服务（Telephone Bearer Service）的参数。

<a id="r_bt_5Ftbs_5Fclient_5Fcall_5Fstate"></a>

```c
struct bt_tbs_client_call_state
```

相关声明：[bt_tbs_client_call_state](../bluetooth_service_model_reference/P174_bt_tbs_client_call_state_结构体.md)。

保存呼叫状态（Call State）的结构。

<a id="r_bt_5Ftbs_5Fclient_5Fcall"></a>

```c
struct bt_tbs_client_call
```

相关声明：[bt_tbs_client_call](../bluetooth_service_model_reference/P173_bt_tbs_client_call_结构体.md)。

电话承载服务客户端（Telephone Bearer Service Client）保存一次呼叫的结构。

<a id="r_bt_5Ftbs_5Fclient_5Fcb"></a>

```c
struct bt_tbs_client_cb
```

相关声明：[bt_tbs_client_cb](../bluetooth_service_model_reference/P175_bt_tbs_client_cb_结构体.md)。

保存电话承载服务（Telephone Bearer Service，TBS）客户端回调的结构体。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 12.2\_宏定义（Macros）

<a id="r_gaeb2eadb4f5559f55734797a4d700e2fe"></a>

```c
#define BT_TBS_ERR_VAL_CHANGED 0x80U
```

相关声明：[BT_TBS_ERR_VAL_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gaeb2eadb4f5559f55734797a4d700e2fe)。

读取长特征值子过程（Read Long Value Characteristic Sub-procedure）进行期间，某个特征值发生了变化。

<a id="r_ga25aa807f2e3a01d030edf4f064a4fbfd"></a>

```c
#define BT_TBS_GTBS_INDEX 0xFFU
```

相关声明：[BT_TBS_GTBS_INDEX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga25aa807f2e3a01d030edf4f064a4fbfd)。

GTBS 索引表示回调来自通用电话承载服务（Generic Telephone Bearer Service，GTBS）实例，或者表示客户端应对服务器的 GTBS 实例执行动作，而非对某个特定电话承载服务（Telephone Bearer Service）实例执行动作。

<a id="r_ga42b72d7aef36cc7ea0d5dd4ec3d7a717"></a>

```c
#define BT_TBS_MAX_UCI_SIZE 6U
```

相关声明：[BT_TBS_MAX_UCI_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga42b72d7aef36cc7ea0d5dd4ec3d7a717)。

承载统一呼叫者标识符（Bearer Uniform Caller Identifier，UCI）的最大大小。

<a id="define-members-0"></a>

### 呼叫状态（Call States）

<a id="r_ga829309945831c0e8ac36c3dd79ae26f3"></a>

```c
#define BT_TBS_CALL_STATE_INCOMING 0x00U
```

相关声明：[BT_TBS_CALL_STATE_INCOMING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga829309945831c0e8ac36c3dd79ae26f3)。

远端正在呼叫，即来电（Incoming Call）。

<a id="r_ga482f9627308cad1e56a4a5a5906c2308"></a>

```c
#define BT_TBS_CALL_STATE_DIALING 0x01U
```

相关声明：[BT_TBS_CALL_STATE_DIALING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga482f9627308cad1e56a4a5a5906c2308)。

服务器已开始呼叫远端，但尚未提醒远端，即呼出（Outgoing Call）。

<a id="r_gada61fd749f2119452429dd712d283dad"></a>

```c
#define BT_TBS_CALL_STATE_ALERTING 0x02U
```

相关声明：[BT_TBS_CALL_STATE_ALERTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gada61fd749f2119452429dd712d283dad)。

正在提醒远端，即呼出（Outgoing Call）。

<a id="r_ga3100ab7a7db823d86198847ec0df4adc"></a>

```c
#define BT_TBS_CALL_STATE_ACTIVE 0x03U
```

相关声明：[BT_TBS_CALL_STATE_ACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga3100ab7a7db823d86198847ec0df4adc)。

呼叫正在通话（Active Conversation）。

<a id="r_gac900fe331fe5b81d7ed0b21796d3e16c"></a>

```c
#define BT_TBS_CALL_STATE_LOCALLY_HELD 0x04U
```

相关声明：[BT_TBS_CALL_STATE_LOCALLY_HELD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gac900fe331fe5b81d7ed0b21796d3e16c)。

呼叫已连接，但被本地保持（Held Locally）。

<a id="r_ga76acd3539931a32361fd0deb3bbe8243"></a>

```c
#define BT_TBS_CALL_STATE_REMOTELY_HELD 0x05U
```

相关声明：[BT_TBS_CALL_STATE_REMOTELY_HELD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga76acd3539931a32361fd0deb3bbe8243)。

呼叫已连接，但被远端保持（Held Remotely）。

<a id="r_ga0d28984faadc6904f72068df6ab6c97d"></a>

```c
#define BT_TBS_CALL_STATE_LOCALLY_AND_REMOTELY_HELD 0x06U
```

相关声明：[BT_TBS_CALL_STATE_LOCALLY_AND_REMOTELY_HELD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga0d28984faadc6904f72068df6ab6c97d)。

呼叫已连接，但同时被本地和远端保持（Held Locally and Remotely）。

<a id="define-members-1"></a>

### 终止原因（Terminate Reason）

<a id="r_gaf7f2abd7e794806ab6b119bee47db6c6"></a>

```c
#define BT_TBS_REASON_BAD_REMOTE_URI 0x00U
```

相关声明：[BT_TBS_REASON_BAD_REMOTE_URI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gaf7f2abd7e794806ab6b119bee47db6c6)。

用于发起呼叫（Originate a Call）的 URI 值格式不正确。

<a id="r_gacd5a09f5786e01662e29d49aa5307046"></a>

```c
#define BT_TBS_REASON_CALL_FAILED 0x01U
```

相关声明：[BT_TBS_REASON_CALL_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gacd5a09f5786e01662e29d49aa5307046)。

呼叫失败（Call Failed）。

<a id="r_ga4bc073b85c6eca1f0a4b0757e1050dde"></a>

```c
#define BT_TBS_REASON_REMOTE_ENDED_CALL 0x02U
```

相关声明：[BT_TBS_REASON_REMOTE_ENDED_CALL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga4bc073b85c6eca1f0a4b0757e1050dde)。

远端结束了呼叫（Call）。

<a id="r_gaa4f89b5fa61dcc4ee7e4fb6ae0e12384"></a>

```c
#define BT_TBS_REASON_SERVER_ENDED_CALL 0x03U
```

相关声明：[BT_TBS_REASON_SERVER_ENDED_CALL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gaa4f89b5fa61dcc4ee7e4fb6ae0e12384)。

服务器端结束了呼叫（Call）。

<a id="r_ga3105e7b0b91b71eb55c1ea5c3bfd6df3"></a>

```c
#define BT_TBS_REASON_LINE_BUSY 0x04U
```

相关声明：[BT_TBS_REASON_LINE_BUSY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga3105e7b0b91b71eb55c1ea5c3bfd6df3)。

线路忙（Line Busy）。

<a id="r_gae195db56d2cd949a29d261c5473eea89"></a>

```c
#define BT_TBS_REASON_NETWORK_CONGESTED 0x05U
```

相关声明：[BT_TBS_REASON_NETWORK_CONGESTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gae195db56d2cd949a29d261c5473eea89)。

网络拥塞（Network Congestion）。

<a id="r_ga614adc266444030ac83dc6f4d2e89563"></a>

```c
#define BT_TBS_REASON_CLIENT_TERMINATED 0x06U
```

相关声明：[BT_TBS_REASON_CLIENT_TERMINATED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga614adc266444030ac83dc6f4d2e89563)。

客户端终止了呼叫（Call）。

<a id="r_ga137b813cf902c8209a624c6ae8d4a93b"></a>

```c
#define BT_TBS_REASON_NO_SERVICE 0x07U
```

相关声明：[BT_TBS_REASON_NO_SERVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga137b813cf902c8209a624c6ae8d4a93b)。

无服务（No Service）。

<a id="r_ga893d3c79ca62c5e5487d7ca7cd403ce2"></a>

```c
#define BT_TBS_REASON_NO_ANSWER 0x08U
```

相关声明：[BT_TBS_REASON_NO_ANSWER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga893d3c79ca62c5e5487d7ca7cd403ce2)。

无人应答（No Answer）。

<a id="r_gaa4dab0b5c08dcf092a125986519a7d55"></a>

```c
#define BT_TBS_REASON_UNSPECIFIED 0x09U
```

相关声明：[BT_TBS_REASON_UNSPECIFIED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gaa4dab0b5c08dcf092a125986519a7d55)。

未指定（Unspecified）。

<a id="define-members-2"></a>

### 控制点错误码（Control point error codes）

<a id="r_gaa92fdb19227ee0b268f2395f3f6a5f63"></a>

```c
#define BT_TBS_RESULT_CODE_SUCCESS 0x00U
```

相关声明：[BT_TBS_RESULT_CODE_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gaa92fdb19227ee0b268f2395f3f6a5f63)。

操作码写入（Opcode Write）成功。

<a id="r_gafac3c970b36f37c815c4370dfef89f09"></a>

```c
#define BT_TBS_RESULT_CODE_OPCODE_NOT_SUPPORTED 0x01U
```

相关声明：[BT_TBS_RESULT_CODE_OPCODE_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gafac3c970b36f37c815c4370dfef89f09)。

写入呼叫控制点（Call Control Point）时使用了无效操作码。

<a id="r_gae83a73a5a0474a62dfbcb5ced6eb3f78"></a>

```c
#define BT_TBS_RESULT_CODE_OPERATION_NOT_POSSIBLE 0x02U
```

相关声明：[BT_TBS_RESULT_CODE_OPERATION_NOT_POSSIBLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gae83a73a5a0474a62dfbcb5ced6eb3f78)。

无法完成请求的操作（Requested Operation）。

<a id="r_gadc371a3a898b3ecac56d8778109f315d"></a>

```c
#define BT_TBS_RESULT_CODE_INVALID_CALL_INDEX 0x03U
```

相关声明：[BT_TBS_RESULT_CODE_INVALID_CALL_INDEX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gadc371a3a898b3ecac56d8778109f315d)。

写入呼叫控制点（Call Control Point）时使用的呼叫索引（Call Index）无效。

<a id="r_ga3fa49179525369502018912115c1ccce"></a>

```c
#define BT_TBS_RESULT_CODE_STATE_MISMATCH 0x04U
```

相关声明：[BT_TBS_RESULT_CODE_STATE_MISMATCH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga3fa49179525369502018912115c1ccce)。

收到写入呼叫控制点（Call Control Point）的操作码时，该呼叫索引（Call Index）对应的当前呼叫状态（Call State）并非预期状态。

<a id="r_ga148585f5cfe8b1cd7f8db404dac91cdd"></a>

```c
#define BT_TBS_RESULT_CODE_OUT_OF_RESOURCES 0x05U
```

相关声明：[BT_TBS_RESULT_CODE_OUT_OF_RESOURCES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga148585f5cfe8b1cd7f8db404dac91cdd)。

内部资源不足，无法完成请求的动作（Requested Action）。

<a id="r_gaa60f75b90f461246b2f470930a60efc2"></a>

```c
#define BT_TBS_RESULT_CODE_INVALID_URI 0x06U
```

相关声明：[BT_TBS_RESULT_CODE_INVALID_URI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gaa60f75b90f461246b2f470930a60efc2)。

发送发起呼叫（Originate）操作码时，呼出 URI（Outgoing URI）不正确或无效。

<a id="define-members-3"></a>

### 可选操作码位（Optional opcodes bits）

可以支持的可选操作码（Optional Opcodes）。

有关如何从远端设备读取这些值，参见 bt_tbs_client_read_optional_opcodes()。

<a id="r_gaf13a663330c8d1902765c208c028ee50"></a>

```c
#define BT_TBS_OPTIONAL_OPCODE_HOLD BIT(0U)
```

相关声明：[BT_TBS_OPTIONAL_OPCODE_HOLD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gaf13a663330c8d1902765c208c028ee50)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持呼叫控制点的本地保持（Local Hold）和本地恢复（Local Retrieve）操作码。

<a id="r_ga06f41e27d2dfc92f31306938005a9058"></a>

```c
#define BT_TBS_OPTIONAL_OPCODE_JOIN BIT(1U)
```

相关声明：[BT_TBS_OPTIONAL_OPCODE_JOIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga06f41e27d2dfc92f31306938005a9058)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持呼叫控制点的合并（Join）操作码。

<a id="r_ga07a7bad80edea037cba34198c5c9c193"></a>

```c
#define BT_TBS_OPTIONAL_OPCODE_ALL (BT_TBS_OPTIONAL_OPCODE_HOLD | BT_TBS_OPTIONAL_OPCODE_JOIN)
```

相关声明：[BT_TBS_OPTIONAL_OPCODE_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga07a7bad80edea037cba34198c5c9c193)、[BT_TBS_OPTIONAL_OPCODE_HOLD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gaf13a663330c8d1902765c208c028ee50)、[BT_TBS_OPTIONAL_OPCODE_JOIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga06f41e27d2dfc92f31306938005a9058)。

支持全部控制点操作码（Control Point Opcodes）。

<a id="define-members-4"></a>

### 信号强度值界限（Signal strength value limits）

<a id="r_ga310c1cdffee350fe5235b3ad929ac715"></a>

```c
#define BT_TBS_SIGNAL_STRENGTH_NO_SERVICE 0U
```

相关声明：[BT_TBS_SIGNAL_STRENGTH_NO_SERVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga310c1cdffee350fe5235b3ad929ac715)。

无服务（No Service）。

<a id="r_gae619d9096b41690ba77ee3e7bd838be3"></a>

```c
#define BT_TBS_SIGNAL_STRENGTH_MAX 100U
```

相关声明：[BT_TBS_SIGNAL_STRENGTH_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gae619d9096b41690ba77ee3e7bd838be3)。

最大信号强度（Maximum Signal Strength）。

<a id="r_gab8a433da27a61cf1c7be2fc7b006e298"></a>

```c
#define BT_TBS_SIGNAL_STRENGTH_UNKNOWN 255U
```

相关声明：[BT_TBS_SIGNAL_STRENGTH_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gab8a433da27a61cf1c7be2fc7b006e298)。

信号强度未知（Unknown Signal Strength）。

<a id="define-members-5"></a>

### 呼叫状态标志位域（Call status flags bitfield）

<a id="r_gadc590b9f5813e190fa14644412aee25c"></a>

```c
#define BT_TBS_STATUS_FLAG_INBAND_RINGTONE BIT(0U)
```

相关声明：[BT_TBS_STATUS_FLAG_INBAND_RINGTONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gadc590b9f5813e190fa14644412aee25c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

已启用带内铃声（Inband Ringtone）。

<a id="r_ga53dfa36830f8c562711d9c6f9111929e"></a>

```c
#define BT_TBS_STATUS_FLAG_SILENT_MOD BIT(1U)
```

相关声明：[BT_TBS_STATUS_FLAG_SILENT_MOD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga53dfa36830f8c562711d9c6f9111929e)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

服务器处于静音模式（Silent Mode；原文写作 silent mod）。

<a id="define-members-6"></a>

### 呼叫标志位域（Call flags bitfield）

<a id="r_ga74344c01327304f1d2da050ddc589735"></a>

```c
#define BT_TBS_CALL_FLAG_OUTGOING BIT(0U)
```

相关声明：[BT_TBS_CALL_FLAG_OUTGOING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga74344c01327304f1d2da050ddc589735)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

设置时表示呼出（Outgoing），否则表示来电（Incoming）。

<a id="r_ga25ff3c36aaabc5e37b08acc62ac21be6"></a>

```c
#define BT_TBS_CALL_FLAG_WITHHELD BIT(1U)
```

相关声明：[BT_TBS_CALL_FLAG_WITHHELD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga25ff3c36aaabc5e37b08acc62ac21be6)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

设置时表示呼叫信息被隐藏（Withheld），否则未隐藏。

<a id="r_ga466c1c3c50e82fee9e5c8323e89be414"></a>

```c
#define BT_TBS_CALL_FLAG_WITHHELD_BY_NETWORK BIT(2U)
```

相关声明：[BT_TBS_CALL_FLAG_WITHHELD_BY_NETWORK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga466c1c3c50e82fee9e5c8323e89be414)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

设置时表示呼叫信息被网络隐藏（Withheld by Network），否则由网络提供。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 12.3\_类型定义（Typedefs）

<a id="r_ga60e9e143f247bb7e668293f0233ce300"></a>

```c
typedef bool(* bt_tbs_originate_call_cb) (struct bt_conn *conn, uint8_t call_index, const char *uri)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_tbs_originate_call_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga60e9e143f247bb7e668293f0233ce300)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

客户端发起呼叫（Originating a Call）的回调函数。

<a id="r_ga69e93b48b2a48e8a6552882660b791cc"></a>

```c
typedef void(* bt_tbs_terminate_call_cb) (struct bt_conn *conn, uint8_t call_index, uint8_t reason)
```

相关声明：[bt_tbs_terminate_call_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga69e93b48b2a48e8a6552882660b791cc)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

客户端终止呼叫（Terminating a Call）的回调函数。

<a id="r_gaa45b3f4837165d722c2df6f202a39058"></a>

```c
typedef void(* bt_tbs_join_calls_cb) (struct bt_conn *conn, uint8_t call_index_count, const uint8_t *call_indexes)
```

相关声明：[bt_tbs_join_calls_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gaa45b3f4837165d722c2df6f202a39058)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

客户端合并呼叫（Joining Calls）的回调函数。

<a id="r_ga2fa85f3cd96f25f6bb4f449fc9210fa1"></a>

```c
typedef void(* bt_tbs_call_change_cb) (struct bt_conn *conn, uint8_t call_index)
```

相关声明：[bt_tbs_call_change_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga2fa85f3cd96f25f6bb4f449fc9210fa1)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

客户端请求改变呼叫状态（Call State Change）的回调函数。

<a id="r_ga1cc9e7140531b07bf6a8dedbc17f24c0"></a>

```c
typedef bool(* bt_tbs_authorize_cb) (struct bt_conn *conn)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bt_tbs_authorize_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga1cc9e7140531b07bf6a8dedbc17f24c0)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

授权客户端（Authorizing a Client）的回调函数。

<a id="r_ga9cac11cc696be9fb387f2f7685e0d8a7"></a>

```c
typedef void(* bt_tbs_client_discover_cb) (struct bt_conn *conn, int err, uint8_t tbs_count, bool gtbs_found)
```

相关声明：[bt_tbs_client_discover_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga9cac11cc696be9fb387f2f7685e0d8a7)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

ccp_discover 的回调函数（Callback Function）。

<a id="r_gaf77231168e4444da7aef203cc9eaca95"></a>

```c
typedef void(* bt_tbs_client_write_value_cb) (struct bt_conn *conn, int err, uint8_t inst_index)
```

相关声明：[bt_tbs_client_write_value_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gaf77231168e4444da7aef203cc9eaca95)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向对端设备写入值（Writing Values）的回调函数。

<a id="r_ga40b8b3d1b318a1b5c5524877bbc2f90f"></a>

```c
typedef void(* bt_tbs_client_cp_cb) (struct bt_conn *conn, int err, uint8_t inst_index, uint8_t call_index)
```

相关声明：[bt_tbs_client_cp_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga40b8b3d1b318a1b5c5524877bbc2f90f)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

CCP 呼叫控制函数（Call Control Functions）的回调函数。

<a id="r_ga4d7632de7c2006e478880950076908a9"></a>

```c
typedef void(* bt_tbs_client_read_string_cb) (struct bt_conn *conn, int err, uint8_t inst_index, const char *value)
```

相关声明：[bt_tbs_client_read_string_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga4d7632de7c2006e478880950076908a9)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取字符串值（String Value）的函数使用的回调函数。

<a id="r_ga600051910ed538a2da823554df23dd20"></a>

```c
typedef void(* bt_tbs_client_read_value_cb) (struct bt_conn *conn, int err, uint8_t inst_index, uint32_t value)
```

相关声明：[bt_tbs_client_read_value_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga600051910ed538a2da823554df23dd20)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

读取整数值（Integer Value）的函数使用的回调函数。

<a id="r_gab881b3caaaa4425e52afd84e53adee78"></a>

```c
typedef void(* bt_tbs_client_termination_reason_cb) (struct bt_conn *conn, int err, uint8_t inst_index, uint8_t call_index, uint8_t reason)
```

相关声明：[bt_tbs_client_termination_reason_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gab881b3caaaa4425e52afd84e53adee78)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

ccp_read_termination_reason 的回调函数（Callback Function）。

<a id="r_ga7b31e1c30fa96081a3ef38e1a481b64f"></a>

```c
typedef void(* bt_tbs_client_current_calls_cb) (struct bt_conn *conn, int err, uint8_t inst_index, uint8_t call_count, const struct bt_tbs_client_call *calls)
```

相关声明：[bt_tbs_client_current_calls_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga7b31e1c30fa96081a3ef38e1a481b64f)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_tbs_client_call](../bluetooth_service_model_reference/P173_bt_tbs_client_call_结构体.md)。

ccp_read_current_calls 的回调函数（Callback Function）。

<a id="r_ga262ca74b7ae2f0c52657066549fa4f92"></a>

```c
typedef void(* bt_tbs_client_call_states_cb) (struct bt_conn *conn, int err, uint8_t inst_index, uint8_t call_count, const struct bt_tbs_client_call_state *call_states)
```

相关声明：[bt_tbs_client_call_states_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga262ca74b7ae2f0c52657066549fa4f92)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_tbs_client_call_state](../bluetooth_service_model_reference/P174_bt_tbs_client_call_state_结构体.md)。

ccp_read_call_state 的回调函数（Callback Function）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 12.4\_函数（Functions）

<a id="r_ga1b942bcf8287641f9cd53824b4d6e77b"></a>

```c
int bt_tbs_accept (uint8_t call_index)
```

相关声明：[bt_tbs_accept](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga1b942bcf8287641f9cd53824b4d6e77b)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

接听正在振铃的呼叫（Alerting Call）。

<a id="r_gab72044a1f5466114b5efb88dfcd2f097"></a>

```c
int bt_tbs_hold (uint8_t call_index)
```

相关声明：[bt_tbs_hold](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gab72044a1f5466114b5efb88dfcd2f097)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

保持呼叫（Hold a Call）。

<a id="r_gad0b45af09b82d6cd66a8481c0e67e04e"></a>

```c
int bt_tbs_retrieve (uint8_t call_index)
```

相关声明：[bt_tbs_retrieve](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gad0b45af09b82d6cd66a8481c0e67e04e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

恢复呼叫（Retrieve a Call）。

<a id="r_ga82553640882ac74f9af84bfe09ff47ee"></a>

```c
int bt_tbs_terminate (uint8_t call_index)
```

相关声明：[bt_tbs_terminate](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga82553640882ac74f9af84bfe09ff47ee)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

终止呼叫（Terminate a Call）。

<a id="r_gadeae51d7cecd80abcdcde1195bb1dfba"></a>

```c
int bt_tbs_originate (uint8_t bearer_index, char *uri, uint8_t *call_index)
```

相关声明：[bt_tbs_originate](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gadeae51d7cecd80abcdcde1195bb1dfba)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

发起呼叫（Originate a Call）。

<a id="r_ga23226d41e3b98a53ec9a9c2fa346c9ac"></a>

```c
int bt_tbs_join (uint8_t call_index_cnt, uint8_t *call_indexes)
```

相关声明：[bt_tbs_join](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga23226d41e3b98a53ec9a9c2fa346c9ac)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

合并呼叫（Join Calls）。

<a id="r_ga868b83450f7425e8a0c8cfb7c1de45d8"></a>

```c
int bt_tbs_remote_answer (uint8_t call_index)
```

相关声明：[bt_tbs_remote_answer](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga868b83450f7425e8a0c8cfb7c1de45d8)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

通知服务器远端已接听呼叫（Answered the Call）。

<a id="r_ga5ffa1a3e3b548d90a3b6a07c6bb4fc7e"></a>

```c
int bt_tbs_remote_hold (uint8_t call_index)
```

相关声明：[bt_tbs_remote_hold](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga5ffa1a3e3b548d90a3b6a07c6bb4fc7e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

通知服务器远端已保持呼叫（Held the Call）。

<a id="r_ga09a3e64040819b6b8b694b94d2f62ca0"></a>

```c
int bt_tbs_remote_retrieve (uint8_t call_index)
```

相关声明：[bt_tbs_remote_retrieve](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga09a3e64040819b6b8b694b94d2f62ca0)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

通知服务器远端已恢复呼叫（Retrieved the Call）。

<a id="r_ga52afc7b8a22b071dbac10057579f319c"></a>

```c
int bt_tbs_remote_terminate (uint8_t call_index)
```

相关声明：[bt_tbs_remote_terminate](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga52afc7b8a22b071dbac10057579f319c)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

通知服务器远端已终止呼叫（Terminated the Call）。

<a id="r_ga47939f557e4d6503af9b7b85aff9d60f"></a>

```c
int bt_tbs_remote_incoming (uint8_t bearer_index, const char *to, const char *from, const char *friendly_name)
```

相关声明：[bt_tbs_remote_incoming](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga47939f557e4d6503af9b7b85aff9d60f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向服务器通知来电（Incoming Call）。

<a id="r_ga5118db6b23b387956e75eda8aecd53d5"></a>

```c
int bt_tbs_set_bearer_provider_name (uint8_t bearer_index, const char *name)
```

相关声明：[bt_tbs_set_bearer_provider_name](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga5118db6b23b387956e75eda8aecd53d5)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置新的承载提供者（Bearer Provider）。

<a id="r_gaa77ea977fca9833d1755d5084a3f352c"></a>

```c
int bt_tbs_set_bearer_technology (uint8_t bearer_index, enum bt_bearer_tech new_technology)
```

相关声明：[bt_tbs_set_bearer_technology](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gaa77ea977fca9833d1755d5084a3f352c)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_bearer_tech](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga4bf3f820b493361a9a3b393d0282420f)。

设置新的承载技术（Bearer Technology）。

<a id="r_gac316adedf7fda441ee55feb9d24d1a94"></a>

```c
int bt_tbs_set_signal_strength (uint8_t bearer_index, uint8_t new_signal_strength)
```

相关声明：[bt_tbs_set_signal_strength](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gac316adedf7fda441ee55feb9d24d1a94)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

更新服务器报告的信号强度（Signal Strength）。

<a id="r_ga838e51a85f9833e0822090cd3df09e00"></a>

```c
int bt_tbs_set_status_flags (uint8_t bearer_index, uint16_t status_flags)
```

相关声明：[bt_tbs_set_status_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga838e51a85f9833e0822090cd3df09e00)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置特性与状态值（Feature and Status Value）。

<a id="r_gae413f94b141b6fa8233de15c36f6327a"></a>

```c
int bt_tbs_set_uri_scheme_list (uint8_t bearer_index, const char *uri_scheme_list)
```

相关声明：[bt_tbs_set_uri_scheme_list](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gae413f94b141b6fa8233de15c36f6327a)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置承载的 URI 方案列表（URI Scheme List）。

<a id="r_ga76f120dba549225a6f2c2c22be08edfc"></a>

```c
void bt_tbs_register_cb (struct bt_tbs_cb *cbs)
```

相关声明：[bt_tbs_register_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga76f120dba549225a6f2c2c22be08edfc)、[bt_tbs_cb](../bluetooth_service_model_reference/P172_bt_tbs_cb_结构体.md)。

注册电话承载服务（TBS）的回调。

<a id="r_ga970c970bedd6e94aa4c92479183554e9"></a>

```c
int bt_tbs_register_bearer (const struct bt_tbs_register_param *param)
```

相关声明：[bt_tbs_register_bearer](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga970c970bedd6e94aa4c92479183554e9)、[bt_tbs_register_param](../bluetooth_service_model_reference/P177_bt_tbs_register_param_结构体.md)。

注册电话承载（Telephone Bearer）。

<a id="r_ga8edd4d31478ed9e0aedbd1a34bdfca96"></a>

```c
int bt_tbs_unregister_bearer (uint8_t bearer_index)
```

相关声明：[bt_tbs_unregister_bearer](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga8edd4d31478ed9e0aedbd1a34bdfca96)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

注销电话承载（Telephone Bearer）。

<a id="r_ga62f5008cbfba158fe399cfaf683d1d2e"></a>

```c
void bt_tbs_dbg_print_calls (void)
```

相关声明：[bt_tbs_dbg_print_calls](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga62f5008cbfba158fe399cfaf683d1d2e)。

将所有服务的全部呼叫（Calls）打印到调试日志。

<a id="r_gac59f3dec092a14bdf234039e3dcd12eb"></a>

```c
int bt_tbs_client_discover (struct bt_conn *conn)
```

相关声明：[bt_tbs_client_discover](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gac59f3dec092a14bdf234039e3dcd12eb)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

发现某个连接上的电话承载服务（TBS）。

<a id="r_ga3a71c51d464aa19fbfbd2d60fc4901bc"></a>

```c
int bt_tbs_client_set_outgoing_uri (struct bt_conn *conn, uint8_t inst_index, const char *uri)
```

相关声明：[bt_tbs_client_set_outgoing_uri](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga3a71c51d464aa19fbfbd2d60fc4901bc)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置对端设备上 TBS 实例的呼出 URI（Outgoing URI）。

<a id="r_gaa1dcb9908057d75a54fa447639826f3c"></a>

```c
int bt_tbs_client_set_signal_strength_interval (struct bt_conn *conn, uint8_t inst_index, uint8_t interval)
```

相关声明：[bt_tbs_client_set_signal_strength_interval](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gaa1dcb9908057d75a54fa447639826f3c)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置 TBS 实例的信号强度报告间隔（Signal Strength Reporting Interval）。

<a id="r_ga0aac704008ffc92ce6609d3ffffc4523"></a>

```c
int bt_tbs_client_originate_call (struct bt_conn *conn, uint8_t inst_index, const char *uri)
```

相关声明：[bt_tbs_client_originate_call](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga0aac704008ffc92ce6609d3ffffc4523)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

请求发起呼叫（Originate a Call）。

<a id="r_ga25b803bb5cae2e1a8b0398bc48137d80"></a>

```c
int bt_tbs_client_terminate_call (struct bt_conn *conn, uint8_t inst_index, uint8_t call_index)
```

相关声明：[bt_tbs_client_terminate_call](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga25b803bb5cae2e1a8b0398bc48137d80)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

请求终止呼叫（Terminate a Call）。

<a id="r_ga23e825de6af71d4e456b63c3a621fb61"></a>

```c
int bt_tbs_client_hold_call (struct bt_conn *conn, uint8_t inst_index, uint8_t call_index)
```

相关声明：[bt_tbs_client_hold_call](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga23e825de6af71d4e456b63c3a621fb61)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

请求保持呼叫（Hold a Call）。

<a id="r_ga625fc73885c2bfd63f0f4b2d7f72eaef"></a>

```c
int bt_tbs_client_accept_call (struct bt_conn *conn, uint8_t inst_index, uint8_t call_index)
```

相关声明：[bt_tbs_client_accept_call](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga625fc73885c2bfd63f0f4b2d7f72eaef)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

接听来电（Incoming Call）。

<a id="r_gabbe194a63da0b95dc1dca0337560a585"></a>

```c
int bt_tbs_client_retrieve_call (struct bt_conn *conn, uint8_t inst_index, uint8_t call_index)
```

相关声明：[bt_tbs_client_retrieve_call](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gabbe194a63da0b95dc1dca0337560a585)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从本地保持状态恢复呼叫（Retrieve Call from Local Hold）。

<a id="r_gaae1925deb0b5865af601aa8278ffb10a"></a>

```c
int bt_tbs_client_join_calls (struct bt_conn *conn, uint8_t inst_index, const uint8_t *call_indexes, uint8_t count)
```

相关声明：[bt_tbs_client_join_calls](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gaae1925deb0b5865af601aa8278ffb10a)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

合并多个呼叫（Join Multiple Calls）。

<a id="r_ga2053a9eb7cf28f66febd365f0b682be0"></a>

```c
int bt_tbs_client_read_bearer_provider_name (struct bt_conn *conn, uint8_t inst_index)
```

相关声明：[bt_tbs_client_read_bearer_provider_name](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga2053a9eb7cf28f66febd365f0b682be0)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取 TBS 实例的承载提供者名称（Bearer Provider Name）。

<a id="r_gaba92039d3b44da9163a22400951fafa7"></a>

```c
int bt_tbs_client_read_bearer_uci (struct bt_conn *conn, uint8_t inst_index)
```

相关声明：[bt_tbs_client_read_bearer_uci](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gaba92039d3b44da9163a22400951fafa7)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取 TBS 实例的统一呼叫者标识符（UCI）。

<a id="r_ga7684dbcb78e407f7002d44fbdb805e5d"></a>

```c
int bt_tbs_client_read_technology (struct bt_conn *conn, uint8_t inst_index)
```

相关声明：[bt_tbs_client_read_technology](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga7684dbcb78e407f7002d44fbdb805e5d)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取 TBS 实例的技术类型（Technology）。

<a id="r_gad19db25591c7ae5bd0b4c2bbaefc9bed"></a>

```c
int bt_tbs_client_read_uri_list (struct bt_conn *conn, uint8_t inst_index)
```

相关声明：[bt_tbs_client_read_uri_list](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gad19db25591c7ae5bd0b4c2bbaefc9bed)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取 TBS 实例的 URI 方案列表（URI Schemes List）。

<a id="r_gaabe97df55817b8e36c79de4bf30fc83f"></a>

```c
int bt_tbs_client_read_signal_strength (struct bt_conn *conn, uint8_t inst_index)
```

相关声明：[bt_tbs_client_read_signal_strength](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gaabe97df55817b8e36c79de4bf30fc83f)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取 TBS 实例的当前信号强度（Signal Strength）。

<a id="r_ga38046c5c715d451b21a3076742268010"></a>

```c
int bt_tbs_client_read_signal_interval (struct bt_conn *conn, uint8_t inst_index)
```

相关声明：[bt_tbs_client_read_signal_interval](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga38046c5c715d451b21a3076742268010)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取 TBS 实例的信号强度报告间隔（Signal Strength Reporting Interval）。

<a id="r_ga895c7f54300e5452fb8d0c9d4b3306ae"></a>

```c
int bt_tbs_client_read_current_calls (struct bt_conn *conn, uint8_t inst_index)
```

相关声明：[bt_tbs_client_read_current_calls](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga895c7f54300e5452fb8d0c9d4b3306ae)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取 TBS 实例的当前呼叫列表（Current Calls List）。

<a id="r_gac070ec0590df5820b7721d579ceeeb15"></a>

```c
int bt_tbs_client_read_ccid (struct bt_conn *conn, uint8_t inst_index)
```

相关声明：[bt_tbs_client_read_ccid](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gac070ec0590df5820b7721d579ceeeb15)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取 TBS 实例的内容 ID（Content ID）。

<a id="r_ga4238a37b80b7d7ff611fe9b02b7cf54d"></a>

```c
int bt_tbs_client_read_call_uri (struct bt_conn *conn, uint8_t inst_index)
```

相关声明：[bt_tbs_client_read_call_uri](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga4238a37b80b7d7ff611fe9b02b7cf54d)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取 TBS 实例的呼叫目标 URI（Call Target URI）。

<a id="r_ga9fe91df1a31ce59401347fc0eac2b701"></a>

```c
int bt_tbs_client_read_status_flags (struct bt_conn *conn, uint8_t inst_index)
```

相关声明：[bt_tbs_client_read_status_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga9fe91df1a31ce59401347fc0eac2b701)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取 TBS 实例的特性与状态值（Feature and Status Value）。

<a id="r_gafeaaaefb9d4eb773dd0cbdfebe26e0b7"></a>

```c
int bt_tbs_client_read_call_state (struct bt_conn *conn, uint8_t inst_index)
```

相关声明：[bt_tbs_client_read_call_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gafeaaaefb9d4eb773dd0cbdfebe26e0b7)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取 TBS 实例当前呼叫的状态（Call States）。

<a id="r_gab04f8355c32fce501bd757b75ee9d38a"></a>

```c
int bt_tbs_client_read_remote_uri (struct bt_conn *conn, uint8_t inst_index)
```

相关声明：[bt_tbs_client_read_remote_uri](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gab04f8355c32fce501bd757b75ee9d38a)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取 TBS 实例的远端 URI（Remote URI）。

<a id="r_ga99549dd6244580e157006fb17772fd8f"></a>

```c
int bt_tbs_client_read_friendly_name (struct bt_conn *conn, uint8_t inst_index)
```

相关声明：[bt_tbs_client_read_friendly_name](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga99549dd6244580e157006fb17772fd8f)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取 TBS 实例中某个呼叫的友好名称（Friendly Name）。

<a id="r_gaf504e1a11352d77a36aa087b587e4ba8"></a>

```c
int bt_tbs_client_read_optional_opcodes (struct bt_conn *conn, uint8_t inst_index)
```

相关声明：[bt_tbs_client_read_optional_opcodes](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gaf504e1a11352d77a36aa087b587e4ba8)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取 TBS 实例支持的操作码（Supported Opcode）。

<a id="r_gabe2251d4ea88306793dc68ae683886bb"></a>

```c
int bt_tbs_client_register_cb (struct bt_tbs_client_cb *cbs)
```

相关声明：[bt_tbs_client_register_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gabe2251d4ea88306793dc68ae683886bb)、[bt_tbs_client_cb](../bluetooth_service_model_reference/P175_bt_tbs_client_cb_结构体.md)。

注册呼叫控制配置文件（CCP）的回调。

<a id="r_gaadae501fa6f7771bb9661af829805a5f"></a>

```c
struct bt_tbs_instance * bt_tbs_client_get_by_ccid (const struct bt_conn *conn, uint8_t ccid)
```

相关声明：[bt_tbs_instance](../bluetooth_service_model_reference/P176_bt_tbs_instance_结构体.md)、[bt_tbs_client_get_by_ccid](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gaadae501fa6f7771bb9661af829805a5f)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

根据 CCID 查找电话承载服务实例（Telephone Bearer Service Instance）。

<a id="r_ga20c6780a4624707a537e905e889510ca"></a>

```c
struct bt_tbs_instance * bt_tbs_client_get_by_index (const struct bt_conn *conn, uint8_t index)
```

相关声明：[bt_tbs_instance](../bluetooth_service_model_reference/P176_bt_tbs_instance_结构体.md)、[bt_tbs_client_get_by_index](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga20c6780a4624707a537e905e889510ca)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

根据索引查找电话承载服务实例（Telephone Bearer Service Instance）。


## 12.5\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [zephyr/bluetooth/assigned_numbers.h](../api_source_socket_ethernet_reference/P001_assigned_numbers.h_源码浏览.md)
- [zephyr/bluetooth/conn.h](../api_source_register_time_reference/P002_conn.h_源码浏览.md)
- [zephyr/sys/slist.h](../slist_reference/P003_单向链表头文件源码.md)
- [zephyr/sys/util_macro.h](../util_reference/P005_宏工具头文件源码.md)
- [查看此文件的源码。](../api_source_socket_ethernet_reference/P007_tbs.h_源码浏览.md)
- [bt_tbs_cb](../bluetooth_service_model_reference/P172_bt_tbs_cb_结构体.md)
- [bt_tbs_register_param](../bluetooth_service_model_reference/P177_bt_tbs_register_param_结构体.md)
- [bt_tbs_client_call_state](../bluetooth_service_model_reference/P174_bt_tbs_client_call_state_结构体.md)
- [bt_tbs_client_call](../bluetooth_service_model_reference/P173_bt_tbs_client_call_结构体.md)
- [bt_tbs_client_cb](../bluetooth_service_model_reference/P175_bt_tbs_client_cb_结构体.md)
- [BT_TBS_ERR_VAL_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gaeb2eadb4f5559f55734797a4d700e2fe)
- [BT_TBS_GTBS_INDEX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga25aa807f2e3a01d030edf4f064a4fbfd)
- [BT_TBS_MAX_UCI_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga42b72d7aef36cc7ea0d5dd4ec3d7a717)
- [BT_TBS_CALL_STATE_INCOMING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga829309945831c0e8ac36c3dd79ae26f3)
- [BT_TBS_CALL_STATE_DIALING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga482f9627308cad1e56a4a5a5906c2308)
- [BT_TBS_CALL_STATE_ALERTING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gada61fd749f2119452429dd712d283dad)
- [BT_TBS_CALL_STATE_ACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga3100ab7a7db823d86198847ec0df4adc)
- [BT_TBS_CALL_STATE_LOCALLY_HELD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gac900fe331fe5b81d7ed0b21796d3e16c)
- [BT_TBS_CALL_STATE_REMOTELY_HELD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga76acd3539931a32361fd0deb3bbe8243)
- [BT_TBS_CALL_STATE_LOCALLY_AND_REMOTELY_HELD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga0d28984faadc6904f72068df6ab6c97d)
- [BT_TBS_REASON_BAD_REMOTE_URI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gaf7f2abd7e794806ab6b119bee47db6c6)
- [BT_TBS_REASON_CALL_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gacd5a09f5786e01662e29d49aa5307046)
- [BT_TBS_REASON_REMOTE_ENDED_CALL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga4bc073b85c6eca1f0a4b0757e1050dde)
- [BT_TBS_REASON_SERVER_ENDED_CALL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gaa4f89b5fa61dcc4ee7e4fb6ae0e12384)
- [BT_TBS_REASON_LINE_BUSY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga3105e7b0b91b71eb55c1ea5c3bfd6df3)
- [BT_TBS_REASON_NETWORK_CONGESTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gae195db56d2cd949a29d261c5473eea89)
- [BT_TBS_REASON_CLIENT_TERMINATED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga614adc266444030ac83dc6f4d2e89563)
- [BT_TBS_REASON_NO_SERVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga137b813cf902c8209a624c6ae8d4a93b)
- [BT_TBS_REASON_NO_ANSWER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga893d3c79ca62c5e5487d7ca7cd403ce2)
- [BT_TBS_REASON_UNSPECIFIED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gaa4dab0b5c08dcf092a125986519a7d55)
- [BT_TBS_RESULT_CODE_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gaa92fdb19227ee0b268f2395f3f6a5f63)
- [BT_TBS_RESULT_CODE_OPCODE_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gafac3c970b36f37c815c4370dfef89f09)
- [BT_TBS_RESULT_CODE_OPERATION_NOT_POSSIBLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gae83a73a5a0474a62dfbcb5ced6eb3f78)
- [BT_TBS_RESULT_CODE_INVALID_CALL_INDEX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gadc371a3a898b3ecac56d8778109f315d)
- [BT_TBS_RESULT_CODE_STATE_MISMATCH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga3fa49179525369502018912115c1ccce)
- [BT_TBS_RESULT_CODE_OUT_OF_RESOURCES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga148585f5cfe8b1cd7f8db404dac91cdd)
- [BT_TBS_RESULT_CODE_INVALID_URI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gaa60f75b90f461246b2f470930a60efc2)
- [bt_tbs_client_read_optional_opcodes()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gaf504e1a11352d77a36aa087b587e4ba8)
- [BT_TBS_OPTIONAL_OPCODE_HOLD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gaf13a663330c8d1902765c208c028ee50)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [BT_TBS_OPTIONAL_OPCODE_JOIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga06f41e27d2dfc92f31306938005a9058)
- [BT_TBS_OPTIONAL_OPCODE_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga07a7bad80edea037cba34198c5c9c193)
- [BT_TBS_SIGNAL_STRENGTH_NO_SERVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga310c1cdffee350fe5235b3ad929ac715)
- [BT_TBS_SIGNAL_STRENGTH_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gae619d9096b41690ba77ee3e7bd838be3)
- [BT_TBS_SIGNAL_STRENGTH_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gab8a433da27a61cf1c7be2fc7b006e298)
- [BT_TBS_STATUS_FLAG_INBAND_RINGTONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gadc590b9f5813e190fa14644412aee25c)
- [BT_TBS_STATUS_FLAG_SILENT_MOD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga53dfa36830f8c562711d9c6f9111929e)
- [BT_TBS_CALL_FLAG_OUTGOING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga74344c01327304f1d2da050ddc589735)
- [BT_TBS_CALL_FLAG_WITHHELD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga25ff3c36aaabc5e37b08acc62ac21be6)
- [BT_TBS_CALL_FLAG_WITHHELD_BY_NETWORK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga466c1c3c50e82fee9e5c8323e89be414)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [bt_tbs_originate_call_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga60e9e143f247bb7e668293f0233ce300)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_tbs_terminate_call_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga69e93b48b2a48e8a6552882660b791cc)
- [bt_tbs_join_calls_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gaa45b3f4837165d722c2df6f202a39058)
- [bt_tbs_call_change_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga2fa85f3cd96f25f6bb4f449fc9210fa1)
- [bt_tbs_authorize_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga1cc9e7140531b07bf6a8dedbc17f24c0)
- [bt_tbs_client_discover_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga9cac11cc696be9fb387f2f7685e0d8a7)
- [bt_tbs_client_write_value_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gaf77231168e4444da7aef203cc9eaca95)
- [bt_tbs_client_cp_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga40b8b3d1b318a1b5c5524877bbc2f90f)
- [bt_tbs_client_read_string_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga4d7632de7c2006e478880950076908a9)
- [bt_tbs_client_read_value_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga600051910ed538a2da823554df23dd20)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [bt_tbs_client_termination_reason_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gab881b3caaaa4425e52afd84e53adee78)
- [bt_tbs_client_current_calls_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga7b31e1c30fa96081a3ef38e1a481b64f)
- [bt_tbs_client_call_states_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga262ca74b7ae2f0c52657066549fa4f92)
- [bt_tbs_accept](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga1b942bcf8287641f9cd53824b4d6e77b)
- [bt_tbs_hold](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gab72044a1f5466114b5efb88dfcd2f097)
- [bt_tbs_retrieve](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gad0b45af09b82d6cd66a8481c0e67e04e)
- [bt_tbs_terminate](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga82553640882ac74f9af84bfe09ff47ee)
- [bt_tbs_originate](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gadeae51d7cecd80abcdcde1195bb1dfba)
- [bt_tbs_join](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga23226d41e3b98a53ec9a9c2fa346c9ac)
- [bt_tbs_remote_answer](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga868b83450f7425e8a0c8cfb7c1de45d8)
- [bt_tbs_remote_hold](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga5ffa1a3e3b548d90a3b6a07c6bb4fc7e)
- [bt_tbs_remote_retrieve](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga09a3e64040819b6b8b694b94d2f62ca0)
- [bt_tbs_remote_terminate](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga52afc7b8a22b071dbac10057579f319c)
- [bt_tbs_remote_incoming](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga47939f557e4d6503af9b7b85aff9d60f)
- [bt_tbs_set_bearer_provider_name](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga5118db6b23b387956e75eda8aecd53d5)
- [bt_tbs_set_bearer_technology](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gaa77ea977fca9833d1755d5084a3f352c)
- [bt_bearer_tech](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga4bf3f820b493361a9a3b393d0282420f)
- [bt_tbs_set_signal_strength](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gac316adedf7fda441ee55feb9d24d1a94)
- [bt_tbs_set_status_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga838e51a85f9833e0822090cd3df09e00)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_tbs_set_uri_scheme_list](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gae413f94b141b6fa8233de15c36f6327a)
- [bt_tbs_register_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga76f120dba549225a6f2c2c22be08edfc)
- [bt_tbs_register_bearer](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga970c970bedd6e94aa4c92479183554e9)
- [bt_tbs_unregister_bearer](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga8edd4d31478ed9e0aedbd1a34bdfca96)
- [bt_tbs_dbg_print_calls](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga62f5008cbfba158fe399cfaf683d1d2e)
- [bt_tbs_client_discover](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gac59f3dec092a14bdf234039e3dcd12eb)
- [bt_tbs_client_set_outgoing_uri](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga3a71c51d464aa19fbfbd2d60fc4901bc)
- [bt_tbs_client_set_signal_strength_interval](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gaa1dcb9908057d75a54fa447639826f3c)
- [bt_tbs_client_originate_call](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga0aac704008ffc92ce6609d3ffffc4523)
- [bt_tbs_client_terminate_call](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga25b803bb5cae2e1a8b0398bc48137d80)
- [bt_tbs_client_hold_call](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga23e825de6af71d4e456b63c3a621fb61)
- [bt_tbs_client_accept_call](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga625fc73885c2bfd63f0f4b2d7f72eaef)
- [bt_tbs_client_retrieve_call](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gabbe194a63da0b95dc1dca0337560a585)
- [bt_tbs_client_join_calls](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gaae1925deb0b5865af601aa8278ffb10a)
- [bt_tbs_client_read_bearer_provider_name](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga2053a9eb7cf28f66febd365f0b682be0)
- [bt_tbs_client_read_bearer_uci](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gaba92039d3b44da9163a22400951fafa7)
- [bt_tbs_client_read_technology](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga7684dbcb78e407f7002d44fbdb805e5d)
- [bt_tbs_client_read_uri_list](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gad19db25591c7ae5bd0b4c2bbaefc9bed)
- [bt_tbs_client_read_signal_strength](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gaabe97df55817b8e36c79de4bf30fc83f)
- [bt_tbs_client_read_signal_interval](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga38046c5c715d451b21a3076742268010)
- [bt_tbs_client_read_current_calls](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga895c7f54300e5452fb8d0c9d4b3306ae)
- [bt_tbs_client_read_ccid](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gac070ec0590df5820b7721d579ceeeb15)
- [bt_tbs_client_read_call_uri](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga4238a37b80b7d7ff611fe9b02b7cf54d)
- [bt_tbs_client_read_status_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga9fe91df1a31ce59401347fc0eac2b701)
- [bt_tbs_client_read_call_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gafeaaaefb9d4eb773dd0cbdfebe26e0b7)
- [bt_tbs_client_read_remote_uri](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gab04f8355c32fce501bd757b75ee9d38a)
- [bt_tbs_client_read_friendly_name](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga99549dd6244580e157006fb17772fd8f)
- [bt_tbs_client_register_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gabe2251d4ea88306793dc68ae683886bb)
- [bt_tbs_instance](../bluetooth_service_model_reference/P176_bt_tbs_instance_结构体.md)
- [bt_tbs_client_get_by_ccid](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gaadae501fa6f7771bb9661af829805a5f)
- [bt_tbs_client_get_by_index](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga20c6780a4624707a537e905e889510ca)

<a id="header-details"></a>

---

[上一章](P011_zephyr__bluetooth__classic__obex.h_文件参考.md) · [返回大纲](大纲.md)
