---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-94
title: bt_le_cs_create_config_params_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__cs__create__config__params.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第94章\_bt\_le\_cs\_create\_config\_params\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__cs__create__config__params.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

信道探测（CS）的创建配置参数。

```c
#include <zephyr/bluetooth/cs.h>
```

<a id="details"></a>

信道探测（CS）的创建配置参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 94.1\_数据成员（Data Fields）

<a id="r_a59615f8de0a39f124ae3d2e2876ecc30"></a>

```c
uint8_t id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[id](#a59615f8de0a39f124ae3d2e2876ecc30)。

信道探测配置标识符（CS configuration ID）。

<a id="r_ab4e492ad109d5b687e691786548344ea"></a>

```c
enum bt_conn_le_cs_mode mode
```

相关声明：[bt_conn_le_cs_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga2f757b15d1d5006ce2fa6a7a78082156)、[mode](#ab4e492ad109d5b687e691786548344ea)。

信道探测主模式与子模式（Main and sub CS mode）。

<a id="r_ae7ff30dcfcb4460dac48c139bdac0f75"></a>

```c
uint8_t min_main_mode_steps
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[min_main_mode_steps](#ae7ff30dcfcb4460dac48c139bdac0f75)。

执行一个子模式步骤前，要执行的信道探测主模式步骤最小数量（CS main mode steps）。

<a id="r_aa8951ab286210ab87c460ed315d091bf"></a>

```c
uint8_t max_main_mode_steps
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[max_main_mode_steps](#aa8951ab286210ab87c460ed315d091bf)。

执行一个子模式步骤前，要执行的信道探测主模式步骤最大数量（CS main mode steps）。

<a id="r_a9a7c56e1d04d634aaab4f3b81c506be3"></a>

```c
uint8_t main_mode_repetition
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[main_mode_repetition](#a9a7c56e1d04d634aaab4f3b81c506be3)。

从上一个信道探测子事件（CS subevent）末尾取出、在当前子事件开头重复执行的主模式步骤数量；这些重复步骤紧接当前事件最后一个模式 0 步骤之后执行。

<a id="r_af824b6b56fba318588ebcf707d6e7a24"></a>

```c
uint8_t mode_0_steps
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mode_0_steps](#af824b6b56fba318588ebcf707d6e7a24)。

每个信道探测子事件（CS subevent）开头包含的模式 0 步骤数量（CS mode-0 steps）。

<a id="r_a2581694b25afa7903786c7848c133c38"></a>

```c
enum bt_conn_le_cs_role role
```

相关声明：[bt_conn_le_cs_role](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga0e6f6d4fdbdfc3ed75fef4a95136076f)、[role](#a2581694b25afa7903786c7848c133c38)。

信道探测角色（CS role）。

<a id="r_a0a34afa329e88af8fcbcff1a8b0a1bcd"></a>

```c
enum bt_conn_le_cs_rtt_type rtt_type
```

相关声明：[bt_conn_le_cs_rtt_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaffd6abf9b92cc8d8463797a73b840f51)、[rtt_type](#a0a34afa329e88af8fcbcff1a8b0a1bcd)。

往返时间类型（RTT type）。

<a id="r_a4329d967361e330077ca9064bdc3fc5f"></a>

```c
enum bt_conn_le_cs_sync_phy cs_sync_phy
```

相关声明：[bt_conn_le_cs_sync_phy](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaadbf6a4dba28aec90ea07b7da634e1bb)、[cs_sync_phy](#a4329d967361e330077ca9064bdc3fc5f)。

信道探测同步物理层（CS Sync PHY）。

<a id="r_adcf6276f58bd19ec61800160979fd472"></a>

```c
uint8_t channel_map [10]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[channel_map](#adcf6276f58bd19ec61800160979fd472)。

信道探测过程（CS procedure）使用的信道映射（Channel map）。信道 n＝0、1、23、24、25、77、78 不允许使用，对应位必须设为零。

<a id="r_a6eff424679cb98ba2d749636618744ce"></a>

```c
uint8_t channel_map_repetition
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[channel_map_repetition](#a6eff424679cb98ba2d749636618744ce)。

在一个信道探测过程（CS procedure）中，非模式 0 步骤循环遍历 `Channel_Map` 字段的次数。

<a id="r_ac83ef36301b0d990cb3a7cf1e630c957"></a>

```c
enum bt_conn_le_cs_chsel_type channel_selection_type
```

相关声明：[bt_conn_le_cs_chsel_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga34e4837a77c7afd6999095985ddad4f0)、[channel_selection_type](#ac83ef36301b0d990cb3a7cf1e630c957)。

信道选择类型（Channel selection type）。

<a id="r_a14ac5115fa91bc7ed4a4aa7a0786f81f"></a>

```c
enum bt_conn_le_cs_ch3c_shape ch3c_shape
```

相关声明：[bt_conn_le_cs_ch3c_shape](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf2331ec1f1222de51fc4f30566e1c52b)、[ch3c_shape](#a14ac5115fa91bc7ed4a4aa7a0786f81f)。

用户指定的信道序列形状（Channel sequence shape）。

<a id="r_ad0ea92b48ac4e9753ee422f2286c1ded"></a>

```c
uint8_t ch3c_jump
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ch3c_jump](#ad0ea92b48ac4e9753ee422f2286c1ded)。

每个上升和下降序列中跳过的信道数量（Channels skipped）。

<a id="r_a7c804eadc92f009d82107f3ff35884ca"></a>

```c
uint8_t cs_enhancements_1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cs_enhancements_1](#a7c804eadc92f009d82107f3ff35884ca)。

信道探测增强项 1（CS Enhancements 1）。

## 94.2\_详细说明（Detailed Documentation）

<a id="ad0ea92b48ac4e9753ee422f2286c1ded"></a>

### `ch3c_jump`

```c
uint8_t bt_le_cs_create_config_params::ch3c_jump
```

每个上升和下降序列中跳过的信道数量（Channels skipped）。

<a id="a14ac5115fa91bc7ed4a4aa7a0786f81f"></a>

### `ch3c_shape`

```c
enum bt_conn_le_cs_ch3c_shape bt_le_cs_create_config_params::ch3c_shape
```

用户指定的信道序列形状（Channel sequence shape）。

<a id="adcf6276f58bd19ec61800160979fd472"></a>

### `channel_map`

```c
uint8_t bt_le_cs_create_config_params::channel_map[10]
```

信道探测过程（CS procedure）使用的信道映射（Channel map）。信道 n＝0、1、23、24、25、77、78 不允许使用，对应位必须设为零。

信道 79 保留供将来使用，必须设为零。必须至少启用 15 个信道（Channels）。

<a id="a6eff424679cb98ba2d749636618744ce"></a>

### `channel_map_repetition`

```c
uint8_t bt_le_cs_create_config_params::channel_map_repetition
```

在一个信道探测过程（CS procedure）中，非模式 0 步骤循环遍历 `Channel_Map` 字段的次数。

<a id="ac83ef36301b0d990cb3a7cf1e630c957"></a>

### `channel_selection_type`

```c
enum bt_conn_le_cs_chsel_type bt_le_cs_create_config_params::channel_selection_type
```

信道选择类型（Channel selection type）。

<a id="a7c804eadc92f009d82107f3ff35884ca"></a>

### `cs_enhancements_1`

```c
uint8_t bt_le_cs_create_config_params::cs_enhancements_1
```

信道探测增强项 1（CS Enhancements 1）。

<a id="a4329d967361e330077ca9064bdc3fc5f"></a>

### `cs_sync_phy`

```c
enum bt_conn_le_cs_sync_phy bt_le_cs_create_config_params::cs_sync_phy
```

信道探测同步物理层（CS Sync PHY）。

<a id="a59615f8de0a39f124ae3d2e2876ecc30"></a>

### `id`

```c
uint8_t bt_le_cs_create_config_params::id
```

信道探测配置标识符（CS configuration ID）。

<a id="a9a7c56e1d04d634aaab4f3b81c506be3"></a>

### `main_mode_repetition`

```c
uint8_t bt_le_cs_create_config_params::main_mode_repetition
```

从上一个信道探测子事件（CS subevent）末尾取出、在当前子事件开头重复执行的主模式步骤数量；这些重复步骤紧接当前事件最后一个模式 0 步骤之后执行。

<a id="aa8951ab286210ab87c460ed315d091bf"></a>

### `max_main_mode_steps`

```c
uint8_t bt_le_cs_create_config_params::max_main_mode_steps
```

执行一个子模式步骤前，要执行的信道探测主模式步骤最大数量（CS main mode steps）。

<a id="ae7ff30dcfcb4460dac48c139bdac0f75"></a>

### `min_main_mode_steps`

```c
uint8_t bt_le_cs_create_config_params::min_main_mode_steps
```

执行一个子模式步骤前，要执行的信道探测主模式步骤最小数量（CS main mode steps）。

<a id="ab4e492ad109d5b687e691786548344ea"></a>

### `mode`

```c
enum bt_conn_le_cs_mode bt_le_cs_create_config_params::mode
```

信道探测主模式与子模式（Main and sub CS mode）。

<a id="af824b6b56fba318588ebcf707d6e7a24"></a>

### `mode_0_steps`

```c
uint8_t bt_le_cs_create_config_params::mode_0_steps
```

每个信道探测子事件（CS subevent）开头包含的模式 0 步骤数量（CS mode-0 steps）。

<a id="a2581694b25afa7903786c7848c133c38"></a>

### `role`

```c
enum bt_conn_le_cs_role bt_le_cs_create_config_params::role
```

信道探测角色（CS role）。

<a id="a0a34afa329e88af8fcbcff1a8b0a1bcd"></a>

### `rtt_type`

```c
enum bt_conn_le_cs_rtt_type bt_le_cs_create_config_params::rtt_type
```

往返时间类型（RTT type）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/cs.h`

## 94.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/cs.h](https://docs.zephyrproject.org/latest/doxygen/html/cs_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_conn_le_cs_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga2f757b15d1d5006ce2fa6a7a78082156)
- [bt_conn_le_cs_role](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga0e6f6d4fdbdfc3ed75fef4a95136076f)
- [bt_conn_le_cs_rtt_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaffd6abf9b92cc8d8463797a73b840f51)
- [bt_conn_le_cs_sync_phy](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaadbf6a4dba28aec90ea07b7da634e1bb)
- [bt_conn_le_cs_chsel_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga34e4837a77c7afd6999095985ddad4f0)
- [bt_conn_le_cs_ch3c_shape](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf2331ec1f1222de51fc4f30566e1c52b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P093_bt_le_conn_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P095_bt_le_cs_iq_sample_结构体.md)
