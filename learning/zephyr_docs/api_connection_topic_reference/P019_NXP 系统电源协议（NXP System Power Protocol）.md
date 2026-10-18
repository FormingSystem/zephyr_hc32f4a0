---
id: learning.zephyr-docs.api-connection-topic-reference.page-19
title: NXP 系统电源协议（NXP System Power Protocol）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__nxp__system.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_NXP 系统电源协议（NXP System Power Protocol）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__nxp__system.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

SCMI 系统电源协议的 NXP 厂商专用扩展。

<a id="details"></a>

SCMI 系统电源协议的 NXP 厂商专用扩展。

<a id="header-files"></a>
<a id="files"></a>

## 19.1\_文件（Files）

<a id="r_system_2Eh"></a>

```c
file system.h
```

相关声明：[system.h](https://docs.zephyrproject.org/latest/doxygen/html/nxp_2system_8h.html)。

NXP SCMI系统协议扩展（System Protocol Extensions）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 19.2\_NXP 厂商系统电源状态（Vendor System Power States）

<a id="r_gaf5606dfb5cd46f6f997c1aaf9aacbb9b"></a>

```c
#define SCMI_NXP_SYSTEM_POWER_STATE_WAKE 0x80000000U
```

相关声明：[SCMI_NXP_SYSTEM_POWER_STATE_WAKE](#gaf5606dfb5cd46f6f997c1aaf9aacbb9b)。

唤醒系统（wake the system）。

<a id="r_ga6b95b0066f23cdc5334d25bd73cdaa29"></a>

```c
#define SCMI_NXP_SYSTEM_POWER_STATE_FULL_SHUTDOWN 0x80000001U
```

相关声明：[SCMI_NXP_SYSTEM_POWER_STATE_FULL_SHUTDOWN](#ga6b95b0066f23cdc5334d25bd73cdaa29)。

完整系统关闭（full system shutdown）。

<a id="r_ga38e493462a6c2ea56912d8fa86eb678b"></a>

```c
#define SCMI_NXP_SYSTEM_POWER_STATE_FULL_RESET 0x80000002U
```

相关声明：[SCMI_NXP_SYSTEM_POWER_STATE_FULL_RESET](#ga38e493462a6c2ea56912d8fa86eb678b)。

完整系统复位（full system reset）。

<a id="r_ga99a3482f3ae00b1e6473dec1afd74a88"></a>

```c
#define SCMI_NXP_SYSTEM_POWER_STATE_FULL_SUSPEND 0x80000003U
```

相关声明：[SCMI_NXP_SYSTEM_POWER_STATE_FULL_SUSPEND](#ga99a3482f3ae00b1e6473dec1afd74a88)。

完整系统挂起（full system suspend）。

<a id="r_gaaf610469a7b618ccbe04da6e12c282af"></a>

```c
#define SCMI_NXP_SYSTEM_POWER_STATE_FULL_WAKE 0x80000004U
```

相关声明：[SCMI_NXP_SYSTEM_POWER_STATE_FULL_WAKE](#gaaf610469a7b618ccbe04da6e12c282af)。

完整系统唤醒（full system wake）。

<a id="r_ga3335f6cda08b66de30f75688d53575fc"></a>

```c
#define SCMI_NXP_SYSTEM_POWER_STATE_GRP_SHUTDOWN 0x80000005U
```

相关声明：[SCMI_NXP_SYSTEM_POWER_STATE_GRP_SHUTDOWN](#ga3335f6cda08b66de30f75688d53575fc)。

组关闭（group shutdown）。

<a id="r_ga7bef35d5b4fe8681457e87cadc4da2d3"></a>

```c
#define SCMI_NXP_SYSTEM_POWER_STATE_GRP_RESET 0x80000006U
```

相关声明：[SCMI_NXP_SYSTEM_POWER_STATE_GRP_RESET](#ga7bef35d5b4fe8681457e87cadc4da2d3)。

组复位（group reset）。

<a id="r_gaaaf73232a6f734f06ebf9ddc3117ac65"></a>

```c
#define SCMI_NXP_SYSTEM_POWER_STATE_SUBSYS_RESET 0x80000007U
```

相关声明：[SCMI_NXP_SYSTEM_POWER_STATE_SUBSYS_RESET](#gaaaf73232a6f734f06ebf9ddc3117ac65)。

子系统复位（subsystem reset）。

<a id="r_gabae2e0660d4776f8c3bce8ecb8c77484"></a>

```c
#define SCMI_NXP_SYSTEM_POWER_STATE_MODE 0xC0000000U
```

相关声明：[SCMI_NXP_SYSTEM_POWER_STATE_MODE](#gabae2e0660d4776f8c3bce8ecb8c77484)。

设置系统模式（system mode）。

## 19.3\_详细说明（Detailed Documentation）

<a id="ga38e493462a6c2ea56912d8fa86eb678b"></a>

### `SCMI_NXP_SYSTEM_POWER_STATE_FULL_RESET`

```c
#define SCMI_NXP_SYSTEM_POWER_STATE_FULL_RESET 0x80000002U
```

```c
#include <zephyr/drivers/firmware/scmi/nxp/system.h>
```

完整系统复位（full system reset）。

<a id="ga6b95b0066f23cdc5334d25bd73cdaa29"></a>

### `SCMI_NXP_SYSTEM_POWER_STATE_FULL_SHUTDOWN`

```c
#define SCMI_NXP_SYSTEM_POWER_STATE_FULL_SHUTDOWN 0x80000001U
```

```c
#include <zephyr/drivers/firmware/scmi/nxp/system.h>
```

完整系统关闭（full system shutdown）。

<a id="ga99a3482f3ae00b1e6473dec1afd74a88"></a>

### `SCMI_NXP_SYSTEM_POWER_STATE_FULL_SUSPEND`

```c
#define SCMI_NXP_SYSTEM_POWER_STATE_FULL_SUSPEND 0x80000003U
```

```c
#include <zephyr/drivers/firmware/scmi/nxp/system.h>
```

完整系统挂起（full system suspend）。

<a id="gaaf610469a7b618ccbe04da6e12c282af"></a>

### `SCMI_NXP_SYSTEM_POWER_STATE_FULL_WAKE`

```c
#define SCMI_NXP_SYSTEM_POWER_STATE_FULL_WAKE 0x80000004U
```

```c
#include <zephyr/drivers/firmware/scmi/nxp/system.h>
```

完整系统唤醒（full system wake）。

<a id="ga7bef35d5b4fe8681457e87cadc4da2d3"></a>

### `SCMI_NXP_SYSTEM_POWER_STATE_GRP_RESET`

```c
#define SCMI_NXP_SYSTEM_POWER_STATE_GRP_RESET 0x80000006U
```

```c
#include <zephyr/drivers/firmware/scmi/nxp/system.h>
```

组复位（group reset）。

<a id="ga3335f6cda08b66de30f75688d53575fc"></a>

### `SCMI_NXP_SYSTEM_POWER_STATE_GRP_SHUTDOWN`

```c
#define SCMI_NXP_SYSTEM_POWER_STATE_GRP_SHUTDOWN 0x80000005U
```

```c
#include <zephyr/drivers/firmware/scmi/nxp/system.h>
```

组关闭（group shutdown）。

<a id="gabae2e0660d4776f8c3bce8ecb8c77484"></a>

### `SCMI_NXP_SYSTEM_POWER_STATE_MODE`

```c
#define SCMI_NXP_SYSTEM_POWER_STATE_MODE 0xC0000000U
```

```c
#include <zephyr/drivers/firmware/scmi/nxp/system.h>
```

设置系统模式（system mode）。

<a id="gaaaf73232a6f734f06ebf9ddc3117ac65"></a>

### `SCMI_NXP_SYSTEM_POWER_STATE_SUBSYS_RESET`

```c
#define SCMI_NXP_SYSTEM_POWER_STATE_SUBSYS_RESET 0x80000007U
```

```c
#include <zephyr/drivers/firmware/scmi/nxp/system.h>
```

子系统复位（subsystem reset）。

<a id="gaf5606dfb5cd46f6f997c1aaf9aacbb9b"></a>

### `SCMI_NXP_SYSTEM_POWER_STATE_WAKE`

```c
#define SCMI_NXP_SYSTEM_POWER_STATE_WAKE 0x80000000U
```

```c
#include <zephyr/drivers/firmware/scmi/nxp/system.h>
```

唤醒系统（wake the system）。


## 19.4\_原页交叉引用（Cross References）

- [system.h](https://docs.zephyrproject.org/latest/doxygen/html/nxp_2system_8h.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P018_nRF 正交解码器（QDEC nRF）.md) · [返回大纲](大纲.md) · [下一章](P020_SHT4X API主题.md)
