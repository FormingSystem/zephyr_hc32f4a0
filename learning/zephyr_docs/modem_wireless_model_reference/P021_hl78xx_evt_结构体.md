---
id: learning.zephyr-docs.modem-wireless-model-reference.page-21
title: hl78xx_evt_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structhl78xx__evt.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第21章\_hl78xx\_evt\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structhl78xx__evt.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

HL78xx的事件结构。

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

<a id="details"></a>

HL78xx 事件结构体，用于容纳 HL78xx 调制解调器的异步事件。`type` 字段指示联合体中哪个成员有效。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 21.1\_数据成员（Data Fields）

<a id="r_a0943763d4df0904b6fd6299f405dc0b4"></a>

```c
enum hl78xx_evt_type type
```

相关声明：[hl78xx_evt_type](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga8a864475f6e9673f85ec7c56028992a5)、[type](#a0943763d4df0904b6fd6299f405dc0b4)。

事件类型（Event Type）。

```c
union {
```

<a id="r_ae82e9c4cdb20e131f0e00263d3401b9a"></a>

```c
enum cellular_registration_status reg_status
```

相关声明：[cellular_registration_status](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga7309390ed507748fdb72cf078b8e08a4)、[reg_status](#af114567a2f292991f3c6de3a0b26a7ba)。

网络注册状态，用于 `HL78XX_LTE_REGISTRATION_STAT_UPDATE`。

<a id="r_a44b2619608343070ec767bf646db21b7"></a>

```c
enum hl78xx_cell_rat_mode rat_mode
```

相关声明：[hl78xx_cell_rat_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga298f953be96ab47be40b5440a2573182)、[rat_mode](#adfab3032ba9bf936a914e8ac02eed1ca)。

无线接入技术（RAT）模式，用于 `HL78XX_LTE_RAT_UPDATE`。

<a id="r_a544a2a7fadb819ee7046eed204d4baea"></a>

```c
enum wdsi_indication wdsi_indication
```

相关声明：[wdsi_indication](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga5453000edbd52c54f7193de4852aa9a8)、[wdsi_indication](#aefc1d835f3244e680a33382c0f9d61fb)。

AirVantage 设备服务指示（device service indication）。

<a id="r_ac39482fe54948bfb7819b24257f10af4"></a>

```c
enum hl78xx_event_status event_status
```

相关声明：[hl78xx_event_status](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga9b9da1841754d723cddc103800b141ae)、[event_status](#accf5c9a1709eb7181aab995267757584)。

GNSS 事件状态。

<a id="r_ac1173c4e2626062573701422422ba774"></a>

```c
enum gnss_position_events position_event
```

相关声明：[gnss_position_events](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga2a471bc1b92dba1e316b2b27e3778e1a)、[position_event](#ace5b13c268479f1e8a143e1673c4ea73)。

GNSS 位置事件类型。

<a id="r_a3687fd2a3b91392cad5e687b2decafc8"></a>

```c
enum hl78xx_psmev_event psm_event
```

相关声明：[hl78xx_psmev_event](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gae891e3155a0ebf72433dd58ae4c36512)、[psm_event](#aabfc3cb2d27cb2a1d7a473af9a6ad621)。

节能模式（PSM）事件。

<a id="r_a4f579d284ac6cb67fbd91edb2143d514"></a>

```c
enum hl78xx_edrx_event edrx_event
```

相关声明：[hl78xx_edrx_event](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga5d8a5b00f354e98abc2effa560f3bac8)、[edrx_event](#a8b207883087d39a428f02f1cc4997043)。

扩展非连续接收（eDRX）事件。

<a id="r_ae0a6bd7fc08f2abf651609bffcdc8434"></a>

```c
enum power_down_event power_down_event
```

相关声明：[power_down_event](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga6340324dcb76101c66b902bb9a14dbd3)、[power_down_event](#a83a493750d68fca89be51eddd700dae1)。

断电（Power-down）事件。

<a id="r_ac0b9817ee6b3319025c3b6e52d9889b8"></a>

```c
struct k_cellmeas_signal_info cellmeas
```

相关声明：[k_cellmeas_signal_info](../system_service_model_reference/P058_k_cellmeas_signal_info_结构体.md)、[cellmeas](#abf9091f1c192664a55b7a8a50e21ee44)。

蜂窝测量事件内容。

<a id="r_a9621a9b95ccdb80216a3d38d4844e2c4"></a>

```c
struct hl78xx_ctzeu_update ctzeu
```

相关声明：[hl78xx_ctzeu_update](P019_hl78xx_ctzeu_update_结构体.md)、[ctzeu](#ac919edeb1b552ce726527b20580303de)。

完整的 `+CTZEU` 更新载荷。

<a id="r_a8ddcc2d6bddf3463f72c6e3f76ad734a"></a>

```c
bool status
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[status](#a3dbdb39cc7be1dd57a965f7d4a86aebc)。

布尔状态值。

<a id="r_abebfedc0cfa082610c213c1f2b52daa2"></a>

```c
int value
```

相关声明：[value](#ad81a188c46465fd7d044377393d362f3)。

整数值。

<a id="r_aa142ce76ffc686074b6955437633feea"></a>

```c
} content
```

相关声明：[content](#aa142ce76ffc686074b6955437633feea)。

事件内容，具体取决于 `type`。

## 21.2\_详细说明（Detailed Documentation）

<a id="abf9091f1c192664a55b7a8a50e21ee44"></a>

### `cellmeas`

```c
struct k_cellmeas_signal_info hl78xx_evt::cellmeas
```

蜂窝测量事件内容。

<a id="aa142ce76ffc686074b6955437633feea"></a>

### `[union]`

```c
union { ... } hl78xx_evt::content
```

事件内容，具体取决于 `type`。

<a id="ac919edeb1b552ce726527b20580303de"></a>

### `ctzeu`

```c
struct hl78xx_ctzeu_update hl78xx_evt::ctzeu
```

完整的 `+CTZEU` 更新载荷。

<a id="a8b207883087d39a428f02f1cc4997043"></a>

### `edrx_event`

```c
enum hl78xx_edrx_event hl78xx_evt::edrx_event
```

扩展非连续接收（eDRX）事件。

**注意（Attention）**：注意：仅在启用以下 Kconfig 选项时可用：`CONFIG_MODEM_HL78XX_EDRX`。

<a id="accf5c9a1709eb7181aab995267757584"></a>

### `event_status`

```c
enum hl78xx_event_status hl78xx_evt::event_status
```

GNSS 事件状态。

**注意（Attention）**：注意：仅在启用以下 Kconfig 选项时可用：`CONFIG_HL78XX_GNSS`。

<a id="ace5b13c268479f1e8a143e1673c4ea73"></a>

### `position_event`

```c
enum gnss_position_events hl78xx_evt::position_event
```

GNSS 位置事件类型。

**注意（Attention）**：注意：仅在启用以下 Kconfig 选项时可用：`CONFIG_HL78XX_GNSS`。

<a id="a83a493750d68fca89be51eddd700dae1"></a>

### `power_down_event`

```c
enum power_down_event hl78xx_evt::power_down_event
```

断电（Power-down）事件。

**注意（Attention）**：注意：仅在启用以下 Kconfig 选项时可用：`CONFIG_MODEM_HL78XX_POWER_DOWN`。

<a id="aabfc3cb2d27cb2a1d7a473af9a6ad621"></a>

### `psm_event`

```c
enum hl78xx_psmev_event hl78xx_evt::psm_event
```

节能模式（PSM）事件。

**注意（Attention）**：注意：仅在启用以下 Kconfig 选项时可用：`CONFIG_MODEM_HL78XX_PSM`。

<a id="adfab3032ba9bf936a914e8ac02eed1ca"></a>

### `rat_mode`

```c
enum hl78xx_cell_rat_mode hl78xx_evt::rat_mode
```

无线接入技术（RAT）模式，用于 `HL78XX_LTE_RAT_UPDATE`。

<a id="af114567a2f292991f3c6de3a0b26a7ba"></a>

### `reg_status`

```c
enum cellular_registration_status hl78xx_evt::reg_status
```

网络注册状态，用于 `HL78XX_LTE_REGISTRATION_STAT_UPDATE`。

<a id="a3dbdb39cc7be1dd57a965f7d4a86aebc"></a>

### `status`

```c
bool hl78xx_evt::status
```

布尔状态值。

<a id="a0943763d4df0904b6fd6299f405dc0b4"></a>

### `type`

```c
enum hl78xx_evt_type hl78xx_evt::type
```

事件类型（Event Type）。

<a id="ad81a188c46465fd7d044377393d362f3"></a>

### `value`

```c
int hl78xx_evt::value
```

整数值。

<a id="aefc1d835f3244e680a33382c0f9d61fb"></a>

### `wdsi_indication`

```c
enum wdsi_indication hl78xx_evt::wdsi_indication
```

AirVantage 设备服务指示（device service indication）。

**注意（Attention）**：注意：仅在启用以下 Kconfig 选项时可用：`CONFIG_MODEM_HL78XX_AIRVANTAGE`。

本数据类型文档由以下文件生成：

- `zephyr/drivers/modem/hl78xx_apis.h`

## 21.3\_原页交叉引用（Cross References）

- [zephyr/drivers/modem/hl78xx_apis.h](https://docs.zephyrproject.org/latest/doxygen/html/hl78xx__apis_8h_source.html)
- [hl78xx_evt_type](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga8a864475f6e9673f85ec7c56028992a5)
- [cellular_registration_status](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga7309390ed507748fdb72cf078b8e08a4)
- [hl78xx_cell_rat_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga298f953be96ab47be40b5440a2573182)
- [wdsi_indication](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga5453000edbd52c54f7193de4852aa9a8)
- [hl78xx_event_status](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga9b9da1841754d723cddc103800b141ae)
- [gnss_position_events](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga2a471bc1b92dba1e316b2b27e3778e1a)
- [hl78xx_psmev_event](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#gae891e3155a0ebf72433dd58ae4c36512)
- [hl78xx_edrx_event](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga5d8a5b00f354e98abc2effa560f3bac8)
- [power_down_event](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga6340324dcb76101c66b902bb9a14dbd3)
- [k_cellmeas_signal_info](../system_service_model_reference/P058_k_cellmeas_signal_info_结构体.md)
- [hl78xx_ctzeu_update](P019_hl78xx_ctzeu_update_结构体.md)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [CONFIG_MODEM_HL78XX_EDRX](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX_EDRX)
- [CONFIG_HL78XX_GNSS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HL78XX_GNSS)
- [CONFIG_MODEM_HL78XX_POWER_DOWN](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX_POWER_DOWN)
- [CONFIG_MODEM_HL78XX_PSM](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX_PSM)
- [CONFIG_MODEM_HL78XX_AIRVANTAGE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX_AIRVANTAGE)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P020_hl78xx_cxreg_status_结构体.md) · [返回大纲](大纲.md) · [下一章](P022_hl78xx_evt_monitor_entry_结构体.md)
