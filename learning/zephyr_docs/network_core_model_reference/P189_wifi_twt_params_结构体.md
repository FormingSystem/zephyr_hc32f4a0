---
id: learning.zephyr-docs.network-core-model-reference.page-189
title: wifi_twt_params_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structwifi__twt__params.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第189章\_wifi\_twt\_params\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structwifi__twt__params.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Wi-Fi目标唤醒时间（TWT）的参数。

```c
#include <zephyr/net/wifi_mgmt.h>
```

<a id="details"></a>

Wi-Fi目标唤醒时间（TWT）的参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 189.1\_数据成员（Data Fields）

<a id="r_a6f0483861a387651c9c89ba182e064bd"></a>

```c
enum wifi_twt_operation operation
```

相关声明：[wifi_twt_operation](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gad0e998aeb1b27c4f203ca76339d323a3)、[operation](#a6f0483861a387651c9c89ba182e064bd)。

目标唤醒时间操作（TWT operation），参见枚举 `wifi_twt_operation`。

<a id="r_a5fd269328f68838b8a7e3a0b93eed894"></a>

```c
enum wifi_twt_negotiation_type negotiation_type
```

相关声明：[wifi_twt_negotiation_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga695123cd534e2499f516a07fdc5cafa8)、[negotiation_type](#a5fd269328f68838b8a7e3a0b93eed894)。

目标唤醒时间协商类型（TWT negotiation type），参见枚举 `wifi_twt_negotiation_type`。

<a id="r_a347f8cff73ee6b6ba6d15ddf6f376a2d"></a>

```c
enum wifi_twt_setup_cmd setup_cmd
```

相关声明：[wifi_twt_setup_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga31c78afc89bfdc4b54cee177843f8022)、[setup_cmd](#a347f8cff73ee6b6ba6d15ddf6f376a2d)。

目标唤醒时间建立命令（TWT setup command），参见枚举 `wifi_twt_setup_cmd`。

<a id="r_a805a23284ed4afa46b84efcd43329beb"></a>

```c
enum wifi_twt_setup_resp_status resp_status
```

相关声明：[wifi_twt_setup_resp_status](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga4d03aedac13ee4512d7717ac624f319a)、[resp_status](#a805a23284ed4afa46b84efcd43329beb)。

目标唤醒时间建立响应状态（TWT setup response status），参见枚举 `wifi_twt_setup_resp_status`。

<a id="r_a9faff59e577775b3fe53f2139462ac71"></a>

```c
enum wifi_twt_teardown_status teardown_status
```

相关声明：[wifi_twt_teardown_status](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gad3709d07aaa3ed59b48f9dd7bd181989)、[teardown_status](#a9faff59e577775b3fe53f2139462ac71)。

目标唤醒时间拆除命令状态（TWT teardown command status），参见枚举 `wifi_twt_teardown_status`。

<a id="r_adda47e302a87a766f18e28016963a561"></a>

```c
uint8_t dialog_token
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[dialog_token](#adda47e302a87a766f18e28016963a561)。

对话令牌（Dialog token），用于将请求映射到响应。

<a id="r_a95ec4b32d37309efa47256ae1ea865da"></a>

```c
uint8_t flow_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[flow_id](#a95ec4b32d37309efa47256ae1ea865da)。

流标识符（Flow ID），用于将建立操作（Setup）与拆除操作（Teardown）对应起来。

```c
union {
```

```c
struct {
```

<a id="r_ae73589711a9d51e26c2edd64f25e98f0"></a>

```c
uint64_t twt_interval
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[twt_interval](#ab92fe571559fcd5d97cdf7e6b7d86681)。

间隔（Interval）＝唤醒时间（Wake up time）＋睡眠时间（Sleeping time）。

<a id="r_aef20fca36140e406127f266208819c00"></a>

```c
bool responder
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[responder](#ae547c6fc1c7cbad15bebcfdaa43f59e7)。

请求方或响应方（Requestor or responder）。

<a id="r_a1282f44170f402897fc3d2439fc65b7b"></a>

```c
bool trigger
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[trigger](#a4e822c04b52fe6a9489e48e26b8f9382)。

启用或禁用触发（Trigger enabled or disabled）。

<a id="r_a7df67110c89bfae91fedc5026334c879"></a>

```c
bool implicit
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[implicit](#a8ea1e2501c8b69dc3fa606eb360f8678)。

隐式或显式（Implicit or explicit）。

<a id="r_a36f78d71634448994e79fd93d88da0b5"></a>

```c
bool announce
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[announce](#a02f2d822d530e5376f256503439a54f9)。

通告或不通告（Announced or unannounced）。

<a id="r_a31c675c91035d3835f276cd48f8eb43d"></a>

```c
uint32_t twt_wake_interval
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[twt_wake_interval](#a7c297459a17ed2fd232c62cca63e952f)。

唤醒时间（Wake up time）。

<a id="r_a204cbc1bda4ccc7ec2a0b3f4f30cba4b"></a>

```c
uint32_t twt_wake_ahead_duration
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[twt_wake_ahead_duration](#a6f907ca412251fdd7391f29bfa6d7713)。

提前唤醒通知（Wake ahead notification）会按照此时长，在目标唤醒时间服务周期（TWT Service Period，SP）开始之前发送。

<a id="r_a45bf3c82108f1c6f63ce673b46b294f6"></a>

```c
bool twt_info_disable
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[twt_info_disable](#ac02eab9593b1ec2c9a0453a67076df88)。

启用或禁用目标唤醒时间信息（TWT info）。

<a id="r_a1fda40d71418d89d68300ade097fe9eb"></a>

```c
uint8_t twt_exponent
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[twt_exponent](#aabb77296f007cb055f78fa1ec3d155a3)。

目标唤醒时间指数（TWT exponent）。

<a id="r_ab9c9bc6c86884924485977501fee4bd6"></a>

```c
uint16_t twt_mantissa
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[twt_mantissa](#aadad4556e2e5405b0703ebb4233a4d17)。

目标唤醒时间尾数范围（TWT Mantissa Range）：`[0-sizeof(UINT16)]`。译注：范围表达式按原文保留。

<a id="r_aff5426dfaafb352fb783b21223788d44"></a>

```c
} setup
```

相关声明：[setup](#aee57c0189b210cfcc18e213e35b9479c)。

建立操作专用参数（Setup specific parameters）。

```c
struct {
```

<a id="r_a0c3aba42ce7fdd234505303812a95165"></a>

```c
uint8_t btwt_sta_wait
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[btwt_sta_wait](#aa05e5fa6a519f700147bb99d6e69a06b)。

广播目标唤醒时间站点等待时间（Broadcast TWT station wait time）。

<a id="r_a3cc3f336e88af84593351d57eee701ca"></a>

```c
uint16_t btwt_offset
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[btwt_offset](#a4459cf19226e199d23ae0cd1d7132b73)。

广播目标唤醒时间偏移量（Broadcast TWT offset）。

<a id="r_ab74c6a124a006203393eac4b29b46d68"></a>

```c
uint8_t btwt_li
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[btwt_li](#a7e7c786c51d3bc70af135bad88ebde4f)。

以 4 个信标间隔（Beacon interval）的整数倍表示。

<a id="r_a1424d8a1f93d2f4fbb89776de9571b16"></a>

```c
uint8_t btwt_count
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[btwt_count](#afc563010a33624bf01feac1292f0871d)。

广播目标唤醒时间协定数量（Broadcast TWT agreement count）。

<a id="r_a1c9e68c2e212df896bca75f22d4f3cec"></a>

```c
struct wifi_btwt_params btwt_set_cfg [5]
```

相关声明：[wifi_btwt_params](P163_wifi_btwt_params_结构体.md)、[btwt_set_cfg](#aa11562186ea265b906861269bc8a692b)。

广播目标唤醒时间协定集合（Broadcast TWT agreement sets）。

<a id="r_ac56ff2b0b81f7321f782096e7087e099"></a>

```c
} btwt
```

相关声明：[btwt](#a72ab809144b1dd3e7e121e489ef399e2)。

建立操作专用参数（Setup specific parameters）。

```c
struct {
```

<a id="r_a97bd5e90c0ee55fa60f7c04ccaa62219"></a>

```c
bool teardown_all
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[teardown_all](#a26d6bda00452f77832f69f4465c13efb)。

拆除所有流（Teardown all flows）。

<a id="r_a49ca08fc87adc4c5760ad2f4c01535a9"></a>

```c
} teardown
```

相关声明：[teardown](#aadf62f6386359ad15491d0073c9065bf)。

拆除操作专用参数（Teardown specific parameters）。

<a id="r_ae3a691d30d5d5bd54ba9d4d0efc51923"></a>

```c
};
```

操作专用参数（Operation specific parameters）。

<a id="r_a70f58b502bb67ef3b2068ded2160b612"></a>

```c
enum wifi_twt_fail_reason fail_reason
```

相关声明：[wifi_twt_fail_reason](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga97fa304f9a1db2294a93cccd4c93bcf6)、[fail_reason](#a70f58b502bb67ef3b2068ded2160b612)。

目标唤醒时间失败原因（TWT fail reason），参见枚举 `wifi_twt_fail_reason`。

## 189.2\_详细说明（Detailed Documentation）

<a id="ae3a691d30d5d5bd54ba9d4d0efc51923"></a>

### `[union]`

```c
union { ... } wifi_twt_params
```

操作专用参数（Operation specific parameters）。

<a id="a02f2d822d530e5376f256503439a54f9"></a>

### `announce`

```c
bool wifi_twt_params::announce
```

通告或不通告（Announced or unannounced）。

<a id="a72ab809144b1dd3e7e121e489ef399e2"></a>

### `[struct]`

```c
struct { ... } wifi_twt_params::btwt
```

建立操作专用参数（Setup specific parameters）。

<a id="afc563010a33624bf01feac1292f0871d"></a>

### `btwt_count`

```c
uint8_t wifi_twt_params::btwt_count
```

广播目标唤醒时间协定数量（Broadcast TWT agreement count）。

<a id="a7e7c786c51d3bc70af135bad88ebde4f"></a>

### `btwt_li`

```c
uint8_t wifi_twt_params::btwt_li
```

以 4 个信标间隔（Beacon interval）的整数倍表示。

<a id="a4459cf19226e199d23ae0cd1d7132b73"></a>

### `btwt_offset`

```c
uint16_t wifi_twt_params::btwt_offset
```

广播目标唤醒时间偏移量（Broadcast TWT offset）。

<a id="aa11562186ea265b906861269bc8a692b"></a>

### `btwt_set_cfg`

```c
struct wifi_btwt_params wifi_twt_params::btwt_set_cfg[5]
```

广播目标唤醒时间协定集合（Broadcast TWT agreement sets）。

<a id="aa05e5fa6a519f700147bb99d6e69a06b"></a>

### `btwt_sta_wait`

```c
uint8_t wifi_twt_params::btwt_sta_wait
```

广播目标唤醒时间站点等待时间（Broadcast TWT station wait time）。

<a id="adda47e302a87a766f18e28016963a561"></a>

### `dialog_token`

```c
uint8_t wifi_twt_params::dialog_token
```

对话令牌（Dialog token），用于将请求映射到响应。

<a id="a70f58b502bb67ef3b2068ded2160b612"></a>

### `fail_reason`

```c
enum wifi_twt_fail_reason wifi_twt_params::fail_reason
```

目标唤醒时间失败原因（TWT fail reason），参见枚举 `wifi_twt_fail_reason`。

<a id="a95ec4b32d37309efa47256ae1ea865da"></a>

### `flow_id`

```c
uint8_t wifi_twt_params::flow_id
```

流标识符（Flow ID），用于将建立操作（Setup）与拆除操作（Teardown）对应起来。

<a id="a8ea1e2501c8b69dc3fa606eb360f8678"></a>

### `implicit`

```c
bool wifi_twt_params::implicit
```

隐式或显式（Implicit or explicit）。

<a id="a5fd269328f68838b8a7e3a0b93eed894"></a>

### `negotiation_type`

```c
enum wifi_twt_negotiation_type wifi_twt_params::negotiation_type
```

目标唤醒时间协商类型（TWT negotiation type），参见枚举 `wifi_twt_negotiation_type`。

<a id="a6f0483861a387651c9c89ba182e064bd"></a>

### `operation`

```c
enum wifi_twt_operation wifi_twt_params::operation
```

目标唤醒时间操作（TWT operation），参见枚举 `wifi_twt_operation`。

<a id="a805a23284ed4afa46b84efcd43329beb"></a>

### `resp_status`

```c
enum wifi_twt_setup_resp_status wifi_twt_params::resp_status
```

目标唤醒时间建立响应状态（TWT setup response status），参见枚举 `wifi_twt_setup_resp_status`。

<a id="ae547c6fc1c7cbad15bebcfdaa43f59e7"></a>

### `responder`

```c
bool wifi_twt_params::responder
```

请求方或响应方（Requestor or responder）。

<a id="aee57c0189b210cfcc18e213e35b9479c"></a>

### `[struct]`

```c
struct { ... } wifi_twt_params::setup
```

建立操作专用参数（Setup specific parameters）。

<a id="a347f8cff73ee6b6ba6d15ddf6f376a2d"></a>

### `setup_cmd`

```c
enum wifi_twt_setup_cmd wifi_twt_params::setup_cmd
```

目标唤醒时间建立命令（TWT setup command），参见枚举 `wifi_twt_setup_cmd`。

<a id="aadf62f6386359ad15491d0073c9065bf"></a>

### `[struct]`

```c
struct { ... } wifi_twt_params::teardown
```

拆除操作专用参数（Teardown specific parameters）。

<a id="a26d6bda00452f77832f69f4465c13efb"></a>

### `teardown_all`

```c
bool wifi_twt_params::teardown_all
```

拆除所有流（Teardown all flows）。

<a id="a9faff59e577775b3fe53f2139462ac71"></a>

### `teardown_status`

```c
enum wifi_twt_teardown_status wifi_twt_params::teardown_status
```

目标唤醒时间拆除命令状态（TWT teardown command status），参见枚举 `wifi_twt_teardown_status`。

<a id="a4e822c04b52fe6a9489e48e26b8f9382"></a>

### `trigger`

```c
bool wifi_twt_params::trigger
```

启用或禁用触发（Trigger enabled or disabled）。

<a id="aabb77296f007cb055f78fa1ec3d155a3"></a>

### `twt_exponent`

```c
uint8_t wifi_twt_params::twt_exponent
```

目标唤醒时间指数（TWT exponent）。

<a id="ac02eab9593b1ec2c9a0453a67076df88"></a>

### `twt_info_disable`

```c
bool wifi_twt_params::twt_info_disable
```

启用或禁用目标唤醒时间信息（TWT info）。

<a id="ab92fe571559fcd5d97cdf7e6b7d86681"></a>

### `twt_interval`

```c
uint64_t wifi_twt_params::twt_interval
```

间隔（Interval）＝唤醒时间（Wake up time）＋睡眠时间（Sleeping time）。

<a id="aadad4556e2e5405b0703ebb4233a4d17"></a>

### `twt_mantissa`

```c
uint16_t wifi_twt_params::twt_mantissa
```

目标唤醒时间尾数范围（TWT Mantissa Range）：`[0-sizeof(UINT16)]`。译注：范围表达式按原文保留。

<a id="a6f907ca412251fdd7391f29bfa6d7713"></a>

### `twt_wake_ahead_duration`

```c
uint32_t wifi_twt_params::twt_wake_ahead_duration
```

提前唤醒通知（Wake ahead notification）会按照此时长，在目标唤醒时间服务周期（TWT Service Period，SP）开始之前发送。

这应使应用在目标唤醒时间服务周期（TWT SP）开始前拥有充足时间准备数据。

<a id="a7c297459a17ed2fd232c62cca63e952f"></a>

### `twt_wake_interval`

```c
uint32_t wifi_twt_params::twt_wake_interval
```

唤醒时间（Wake up time）。

本数据类型文档由以下文件生成：

- `zephyr/net/wifi_mgmt.h`

## 189.3\_原页交叉引用（Cross References）

- [zephyr/net/wifi_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/wifi__mgmt_8h_source.html)
- [wifi_twt_operation](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gad0e998aeb1b27c4f203ca76339d323a3)
- [wifi_twt_negotiation_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga695123cd534e2499f516a07fdc5cafa8)
- [wifi_twt_setup_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga31c78afc89bfdc4b54cee177843f8022)
- [wifi_twt_setup_resp_status](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga4d03aedac13ee4512d7717ac624f319a)
- [wifi_twt_teardown_status](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gad3709d07aaa3ed59b48f9dd7bd181989)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [wifi_btwt_params](P163_wifi_btwt_params_结构体.md)
- [wifi_twt_fail_reason](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga97fa304f9a1db2294a93cccd4c93bcf6)
- [wifi_twt_params](P189_wifi_twt_params_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P188_wifi_twt_flow_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P190_wifi_version_结构体.md)
