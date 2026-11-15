---
id: learning.zephyr-docs.api-file-system-device-reference.page-32
title: zephyr__drivers__firmware__scmi__nxp__system.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nxp_2system_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第32章\_zephyr\_\_drivers\_\_firmware\_\_scmi\_\_nxp\_\_system.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/nxp_2system_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

NXP SCMI系统协议扩展（System Protocol Extensions）。

<a id="details"></a>

```c
#include <stdint.h>
```

查看此文件的源码。

NXP SCMI系统协议扩展（System Protocol Extensions）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 32.1\_宏定义（Macros）

<a id="define-members-0"></a>

### NXP 厂商系统电源状态（Vendor System Power States）

<a id="r_gaf5606dfb5cd46f6f997c1aaf9aacbb9b"></a>

```c
#define SCMI_NXP_SYSTEM_POWER_STATE_WAKE 0x80000000U
```

相关声明：[SCMI_NXP_SYSTEM_POWER_STATE_WAKE](../api_connection_topic_reference/P019_NXP 系统电源协议（NXP System Power Protocol）.md#gaf5606dfb5cd46f6f997c1aaf9aacbb9b)。

唤醒系统（wake the system）。

<a id="r_ga6b95b0066f23cdc5334d25bd73cdaa29"></a>

```c
#define SCMI_NXP_SYSTEM_POWER_STATE_FULL_SHUTDOWN 0x80000001U
```

相关声明：[SCMI_NXP_SYSTEM_POWER_STATE_FULL_SHUTDOWN](../api_connection_topic_reference/P019_NXP 系统电源协议（NXP System Power Protocol）.md#ga6b95b0066f23cdc5334d25bd73cdaa29)。

完整系统关闭（full system shutdown）。

<a id="r_ga38e493462a6c2ea56912d8fa86eb678b"></a>

```c
#define SCMI_NXP_SYSTEM_POWER_STATE_FULL_RESET 0x80000002U
```

相关声明：[SCMI_NXP_SYSTEM_POWER_STATE_FULL_RESET](../api_connection_topic_reference/P019_NXP 系统电源协议（NXP System Power Protocol）.md#ga38e493462a6c2ea56912d8fa86eb678b)。

完整系统复位（full system reset）。

<a id="r_ga99a3482f3ae00b1e6473dec1afd74a88"></a>

```c
#define SCMI_NXP_SYSTEM_POWER_STATE_FULL_SUSPEND 0x80000003U
```

相关声明：[SCMI_NXP_SYSTEM_POWER_STATE_FULL_SUSPEND](../api_connection_topic_reference/P019_NXP 系统电源协议（NXP System Power Protocol）.md#ga99a3482f3ae00b1e6473dec1afd74a88)。

完整系统挂起（full system suspend）。

<a id="r_gaaf610469a7b618ccbe04da6e12c282af"></a>

```c
#define SCMI_NXP_SYSTEM_POWER_STATE_FULL_WAKE 0x80000004U
```

相关声明：[SCMI_NXP_SYSTEM_POWER_STATE_FULL_WAKE](../api_connection_topic_reference/P019_NXP 系统电源协议（NXP System Power Protocol）.md#gaaf610469a7b618ccbe04da6e12c282af)。

完整系统唤醒（full system wake）。

<a id="r_ga3335f6cda08b66de30f75688d53575fc"></a>

```c
#define SCMI_NXP_SYSTEM_POWER_STATE_GRP_SHUTDOWN 0x80000005U
```

相关声明：[SCMI_NXP_SYSTEM_POWER_STATE_GRP_SHUTDOWN](../api_connection_topic_reference/P019_NXP 系统电源协议（NXP System Power Protocol）.md#ga3335f6cda08b66de30f75688d53575fc)。

组关闭（group shutdown）。

<a id="r_ga7bef35d5b4fe8681457e87cadc4da2d3"></a>

```c
#define SCMI_NXP_SYSTEM_POWER_STATE_GRP_RESET 0x80000006U
```

相关声明：[SCMI_NXP_SYSTEM_POWER_STATE_GRP_RESET](../api_connection_topic_reference/P019_NXP 系统电源协议（NXP System Power Protocol）.md#ga7bef35d5b4fe8681457e87cadc4da2d3)。

组复位（group reset）。

<a id="r_gaaaf73232a6f734f06ebf9ddc3117ac65"></a>

```c
#define SCMI_NXP_SYSTEM_POWER_STATE_SUBSYS_RESET 0x80000007U
```

相关声明：[SCMI_NXP_SYSTEM_POWER_STATE_SUBSYS_RESET](../api_connection_topic_reference/P019_NXP 系统电源协议（NXP System Power Protocol）.md#gaaaf73232a6f734f06ebf9ddc3117ac65)。

子系统复位（subsystem reset）。

<a id="r_gabae2e0660d4776f8c3bce8ecb8c77484"></a>

```c
#define SCMI_NXP_SYSTEM_POWER_STATE_MODE 0xC0000000U
```

相关声明：[SCMI_NXP_SYSTEM_POWER_STATE_MODE](../api_connection_topic_reference/P019_NXP 系统电源协议（NXP System Power Protocol）.md#gabae2e0660d4776f8c3bce8ecb8c77484)。

设置系统模式（system mode）。


## 32.2\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P615_system.h_源码浏览.md)
- [SCMI_NXP_SYSTEM_POWER_STATE_WAKE](../api_connection_topic_reference/P019_NXP 系统电源协议（NXP System Power Protocol）.md#gaf5606dfb5cd46f6f997c1aaf9aacbb9b)
- [SCMI_NXP_SYSTEM_POWER_STATE_FULL_SHUTDOWN](../api_connection_topic_reference/P019_NXP 系统电源协议（NXP System Power Protocol）.md#ga6b95b0066f23cdc5334d25bd73cdaa29)
- [SCMI_NXP_SYSTEM_POWER_STATE_FULL_RESET](../api_connection_topic_reference/P019_NXP 系统电源协议（NXP System Power Protocol）.md#ga38e493462a6c2ea56912d8fa86eb678b)
- [SCMI_NXP_SYSTEM_POWER_STATE_FULL_SUSPEND](../api_connection_topic_reference/P019_NXP 系统电源协议（NXP System Power Protocol）.md#ga99a3482f3ae00b1e6473dec1afd74a88)
- [SCMI_NXP_SYSTEM_POWER_STATE_FULL_WAKE](../api_connection_topic_reference/P019_NXP 系统电源协议（NXP System Power Protocol）.md#gaaf610469a7b618ccbe04da6e12c282af)
- [SCMI_NXP_SYSTEM_POWER_STATE_GRP_SHUTDOWN](../api_connection_topic_reference/P019_NXP 系统电源协议（NXP System Power Protocol）.md#ga3335f6cda08b66de30f75688d53575fc)
- [SCMI_NXP_SYSTEM_POWER_STATE_GRP_RESET](../api_connection_topic_reference/P019_NXP 系统电源协议（NXP System Power Protocol）.md#ga7bef35d5b4fe8681457e87cadc4da2d3)
- [SCMI_NXP_SYSTEM_POWER_STATE_SUBSYS_RESET](../api_connection_topic_reference/P019_NXP 系统电源协议（NXP System Power Protocol）.md#gaaaf73232a6f734f06ebf9ddc3117ac65)
- [SCMI_NXP_SYSTEM_POWER_STATE_MODE](../api_connection_topic_reference/P019_NXP 系统电源协议（NXP System Power Protocol）.md#gabae2e0660d4776f8c3bce8ecb8c77484)

<a id="header-details"></a>

---

[上一章](P031_zephyr__dt-bindings__pinctrl__nxp-siul2-pinctrl.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P033_zephyr__drivers__misc__nxp_flexio__nxp_flexio.h_文件参考.md)
