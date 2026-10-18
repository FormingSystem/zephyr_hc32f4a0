---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-15
title: bt_conn_le_cs_config_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__le__cs__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_bt\_conn\_le\_cs\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__le__cs__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

信道探测（Channel Sounding）配置。

```c
#include <zephyr/bluetooth/conn.h>
```

<a id="details"></a>

信道探测（Channel Sounding）配置。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 15.1\_数据成员（Data Fields）

<a id="r_aaf8f1ce04fd22b4ca4728bdcfce8bd4a"></a>

```c
uint8_t id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[id](#aaf8f1ce04fd22b4ca4728bdcfce8bd4a)。

信道探测配置标识符（CS configuration ID）。

<a id="r_ab59b31730b91f843e5b8a156d98da42d"></a>

```c
enum bt_conn_le_cs_mode mode
```

相关声明：[bt_conn_le_cs_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga2f757b15d1d5006ce2fa6a7a78082156)、[mode](#ab59b31730b91f843e5b8a156d98da42d)。

信道探测主模式与子模式（CS main and sub mode）。

<a id="r_a2e59fb17cd932b7670b3e915684c2107"></a>

```c
uint8_t min_main_mode_steps
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[min_main_mode_steps](#a2e59fb17cd932b7670b3e915684c2107)。

执行一个子模式步骤前，要执行的信道探测主模式步骤最小数量（CS main mode steps）。

<a id="r_aff70b37fac8a3bd94acb25d7bd06989b"></a>

```c
uint8_t max_main_mode_steps
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[max_main_mode_steps](#aff70b37fac8a3bd94acb25d7bd06989b)。

执行一个子模式步骤前，要执行的信道探测主模式步骤最大数量（CS main mode steps）。

<a id="r_a2e904438c579870ed96b5dccff239c18"></a>

```c
uint8_t main_mode_repetition
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[main_mode_repetition](#a2e904438c579870ed96b5dccff239c18)。

从上一个信道探测子事件（CS subevent）末尾取出、在当前子事件开头重复执行的主模式步骤数量；这些重复步骤紧接当前事件最后一个模式 0 步骤之后执行。

<a id="r_a8eea68bffef759b4532b68a1ecbdd4f1"></a>

```c
uint8_t mode_0_steps
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mode_0_steps](#a8eea68bffef759b4532b68a1ecbdd4f1)。

每个信道探测子事件（CS subevent）开头包含的模式 0 步骤数量（CS mode-0 steps）。

<a id="r_ad11f8bee028ad3eb59008d46dce2d5bd"></a>

```c
enum bt_conn_le_cs_role role
```

相关声明：[bt_conn_le_cs_role](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga0e6f6d4fdbdfc3ed75fef4a95136076f)、[role](#ad11f8bee028ad3eb59008d46dce2d5bd)。

信道探测角色（CS role）。

<a id="r_a194e3844373c57e714917d03ac82666d"></a>

```c
enum bt_conn_le_cs_rtt_type rtt_type
```

相关声明：[bt_conn_le_cs_rtt_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaffd6abf9b92cc8d8463797a73b840f51)、[rtt_type](#a194e3844373c57e714917d03ac82666d)。

往返时间类型（RTT type）。

<a id="r_a2051f559b41085c4b41743aaaaecf3a1"></a>

```c
enum bt_conn_le_cs_sync_phy cs_sync_phy
```

相关声明：[bt_conn_le_cs_sync_phy](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaadbf6a4dba28aec90ea07b7da634e1bb)、[cs_sync_phy](#a2051f559b41085c4b41743aaaaecf3a1)。

信道探测同步物理层（CS Sync PHY）。

<a id="r_a971ff7ba734dd71512af7f3850de364d"></a>

```c
uint8_t channel_map_repetition
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[channel_map_repetition](#a971ff7ba734dd71512af7f3850de364d)。

在一个信道探测过程（CS procedure）中，非模式 0 步骤循环遍历 `Channel_Map` 字段的次数。

<a id="r_a63b7027929a5c3ec7fd68f35343262ee"></a>

```c
enum bt_conn_le_cs_chsel_type channel_selection_type
```

相关声明：[bt_conn_le_cs_chsel_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga34e4837a77c7afd6999095985ddad4f0)、[channel_selection_type](#a63b7027929a5c3ec7fd68f35343262ee)。

信道选择类型（Channel selection type）。

<a id="r_a9b64ecb0986e7e9995c29feaf105eeaa"></a>

```c
enum bt_conn_le_cs_ch3c_shape ch3c_shape
```

相关声明：[bt_conn_le_cs_ch3c_shape](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf2331ec1f1222de51fc4f30566e1c52b)、[ch3c_shape](#a9b64ecb0986e7e9995c29feaf105eeaa)。

用户指定的信道序列形状（Channel sequence shape）。

<a id="r_afa2846689f1a9d5b9e124b1c9095154f"></a>

```c
uint8_t ch3c_jump
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ch3c_jump](#afa2846689f1a9d5b9e124b1c9095154f)。

每个上升和下降序列中跳过的信道数量（Channels skipped）。

<a id="r_acfccd404abced1c5f5490130f2f77f23"></a>

```c
uint8_t cs_enhancements_1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cs_enhancements_1](#acfccd404abced1c5f5490130f2f77f23)。

信道探测增强 1（CS enhancements 1）的位 0：在信道探测反射方（CS reflector）中启用内联相位校正项传输（Inline PCT Transfer，IPT）。

<a id="r_aab9a1d8d09d7a439f1c4dd28b9dd05c4"></a>

```c
uint8_t t_ip1_time_us
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[t_ip1_time_us](#aab9a1d8d09d7a439f1c4dd28b9dd05c4)。

往返时间数据包（RTT packets）之间的间歇时间（Interlude time），单位为微秒。

<a id="r_a8e650b50400a45040c02a88dfb30683c"></a>

```c
uint8_t t_ip2_time_us
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[t_ip2_time_us](#a8e650b50400a45040c02a88dfb30683c)。

信道探测音调（CS tones）之间的间歇时间（Interlude time），单位为微秒。

<a id="r_a29912bd291fa4da09bb5b196d747ca6b"></a>

```c
uint8_t t_fcs_time_us
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[t_fcs_time_us](#a29912bd291fa4da09bb5b196d747ca6b)。

频率切换时间（Frequency change time），单位为微秒。

<a id="r_ae7f1cc232df00b4543fdb2b2596b9bbf"></a>

```c
uint8_t t_pm_time_us
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[t_pm_time_us](#ae7f1cc232df00b4543fdb2b2596b9bbf)。

信道探测音调（CS tones）的相位测量周期（Phase measurement period），单位为微秒。

<a id="r_a60f9d21629554d47556d0fe8d63dcae3"></a>

```c
uint8_t channel_map [10]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[channel_map](#a60f9d21629554d47556d0fe8d63dcae3)。

信道探测过程（CS procedure）使用的信道映射（Channel map）。信道 n＝0、1、23、24、25、77、78 不允许使用，对应位必须设为零。

## 15.2\_详细说明（Detailed Documentation）

<a id="afa2846689f1a9d5b9e124b1c9095154f"></a>

### `ch3c_jump`

```c
uint8_t bt_conn_le_cs_config::ch3c_jump
```

每个上升和下降序列中跳过的信道数量（Channels skipped）。

<a id="a9b64ecb0986e7e9995c29feaf105eeaa"></a>

### `ch3c_shape`

```c
enum bt_conn_le_cs_ch3c_shape bt_conn_le_cs_config::ch3c_shape
```

用户指定的信道序列形状（Channel sequence shape）。

<a id="a60f9d21629554d47556d0fe8d63dcae3"></a>

### `channel_map`

```c
uint8_t bt_conn_le_cs_config::channel_map[10]
```

信道探测过程（CS procedure）使用的信道映射（Channel map）。信道 n＝0、1、23、24、25、77、78 不允许使用，对应位必须设为零。

信道 79 保留供将来使用，必须设为零。必须至少启用 15 个信道（Channels）。

<a id="a971ff7ba734dd71512af7f3850de364d"></a>

### `channel_map_repetition`

```c
uint8_t bt_conn_le_cs_config::channel_map_repetition
```

在一个信道探测过程（CS procedure）中，非模式 0 步骤循环遍历 `Channel_Map` 字段的次数。

<a id="a63b7027929a5c3ec7fd68f35343262ee"></a>

### `channel_selection_type`

```c
enum bt_conn_le_cs_chsel_type bt_conn_le_cs_config::channel_selection_type
```

信道选择类型（Channel selection type）。

<a id="acfccd404abced1c5f5490130f2f77f23"></a>

### `cs_enhancements_1`

```c
uint8_t bt_conn_le_cs_config::cs_enhancements_1
```

信道探测增强 1（CS enhancements 1）的位 0：在信道探测反射方（CS reflector）中启用内联相位校正项传输（Inline PCT Transfer，IPT）。

其余所有位均为保留位（Reserved），必须设为 `0`。

<a id="a2051f559b41085c4b41743aaaaecf3a1"></a>

### `cs_sync_phy`

```c
enum bt_conn_le_cs_sync_phy bt_conn_le_cs_config::cs_sync_phy
```

信道探测同步物理层（CS Sync PHY）。

<a id="aaf8f1ce04fd22b4ca4728bdcfce8bd4a"></a>

### `id`

```c
uint8_t bt_conn_le_cs_config::id
```

信道探测配置标识符（CS configuration ID）。

<a id="a2e904438c579870ed96b5dccff239c18"></a>

### `main_mode_repetition`

```c
uint8_t bt_conn_le_cs_config::main_mode_repetition
```

从上一个信道探测子事件（CS subevent）末尾取出、在当前子事件开头重复执行的主模式步骤数量；这些重复步骤紧接当前事件最后一个模式 0 步骤之后执行。

<a id="aff70b37fac8a3bd94acb25d7bd06989b"></a>

### `max_main_mode_steps`

```c
uint8_t bt_conn_le_cs_config::max_main_mode_steps
```

执行一个子模式步骤前，要执行的信道探测主模式步骤最大数量（CS main mode steps）。

<a id="a2e59fb17cd932b7670b3e915684c2107"></a>

### `min_main_mode_steps`

```c
uint8_t bt_conn_le_cs_config::min_main_mode_steps
```

执行一个子模式步骤前，要执行的信道探测主模式步骤最小数量（CS main mode steps）。

<a id="ab59b31730b91f843e5b8a156d98da42d"></a>

### `mode`

```c
enum bt_conn_le_cs_mode bt_conn_le_cs_config::mode
```

信道探测主模式与子模式（CS main and sub mode）。

<a id="a8eea68bffef759b4532b68a1ecbdd4f1"></a>

### `mode_0_steps`

```c
uint8_t bt_conn_le_cs_config::mode_0_steps
```

每个信道探测子事件（CS subevent）开头包含的模式 0 步骤数量（CS mode-0 steps）。

<a id="ad11f8bee028ad3eb59008d46dce2d5bd"></a>

### `role`

```c
enum bt_conn_le_cs_role bt_conn_le_cs_config::role
```

信道探测角色（CS role）。

<a id="a194e3844373c57e714917d03ac82666d"></a>

### `rtt_type`

```c
enum bt_conn_le_cs_rtt_type bt_conn_le_cs_config::rtt_type
```

往返时间类型（RTT type）。

<a id="a29912bd291fa4da09bb5b196d747ca6b"></a>

### `t_fcs_time_us`

```c
uint8_t bt_conn_le_cs_config::t_fcs_time_us
```

频率切换时间（Frequency change time），单位为微秒。

<a id="aab9a1d8d09d7a439f1c4dd28b9dd05c4"></a>

### `t_ip1_time_us`

```c
uint8_t bt_conn_le_cs_config::t_ip1_time_us
```

往返时间数据包（RTT packets）之间的间歇时间（Interlude time），单位为微秒。

<a id="a8e650b50400a45040c02a88dfb30683c"></a>

### `t_ip2_time_us`

```c
uint8_t bt_conn_le_cs_config::t_ip2_time_us
```

信道探测音调（CS tones）之间的间歇时间（Interlude time），单位为微秒。

<a id="ae7f1cc232df00b4543fdb2b2596b9bbf"></a>

### `t_pm_time_us`

```c
uint8_t bt_conn_le_cs_config::t_pm_time_us
```

信道探测音调（CS tones）的相位测量周期（Phase measurement period），单位为微秒。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/conn.h`

## 15.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h_source.html)
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

[上一章](P014_bt_conn_le_cs_capabilities_结构体.md) · [返回大纲](大纲.md) · [下一章](P016_bt_conn_le_cs_fae_table_结构体.md)
