---
id: learning.zephyr-docs.modem-wireless-model-reference.page-68
title: sim7080_ue_sys_info_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsim7080__ue__sys__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第68章\_sim7080\_ue\_sys\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsim7080__ue__sys__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Sim7080用户设备（UE）的系统信息结构。

```c
#include <zephyr/drivers/modem/simcom-sim7080.h>
```

<a id="details"></a>

Sim7080用户设备（UE）的系统信息结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 68.1\_数据成员（Data Fields）

<a id="r_a47f14459263b13749a3722107a20631c"></a>

```c
enum sim7080_ue_sys_mode sys_mode
```

相关声明：[sim7080_ue_sys_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga25a5a23ca32dbd4bc7991274d3d1ce04)、[sys_mode](#a47f14459263b13749a3722107a20631c)。

参见 `sim7080_ue_sys_mode`。

<a id="r_a77e0794049df94d1c6c106a1554fa6ea"></a>

```c
enum sim7080_ue_op_mode op_mode
```

相关声明：[sim7080_ue_op_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gaeda25db4347c7fcfbee69e8d6edace64)、[op_mode](#a77e0794049df94d1c6c106a1554fa6ea)。

参见 `sim7080_ue_op_mode`。

```c
union {
```

<a id="r_aa080fa9e4a65e5924c451d59239e1225"></a>

```c
struct sim7080_ue_sys_info_gsm gsm
```

相关声明：[sim7080_ue_sys_info_gsm](P069_sim7080_ue_sys_info_gsm_结构体.md)、[gsm](#ae2010949f786b1ee107cbfc34e207412)。

仅在 `sys_mode` 为全球移动通信系统（GSM）时设置。

<a id="r_ab52610194e269b4d821a06d348824e43"></a>

```c
struct sim7080_ue_sys_info_lte lte
```

相关声明：[sim7080_ue_sys_info_lte](P070_sim7080_ue_sys_info_lte_结构体.md)、[lte](#ace117d5d35a3b6a41b87b05315f7a19e)。

仅在系统模式为 LTE CAT-M1 或窄带物联网（NB-IoT）时设置。

<a id="r_ab42417fa5673818a5236e61a791d6c20"></a>

```c
} cell
```

相关声明：[cell](#ab42417fa5673818a5236e61a791d6c20)。

小区信息（Cell information）。

## 68.2\_详细说明（Detailed Documentation）

<a id="ab42417fa5673818a5236e61a791d6c20"></a>

### `[union]`

```c
union { ... } sim7080_ue_sys_info::cell
```

小区信息（Cell information）。

<a id="ae2010949f786b1ee107cbfc34e207412"></a>

### `gsm`

```c
struct sim7080_ue_sys_info_gsm sim7080_ue_sys_info::gsm
```

仅在 `sys_mode` 为全球移动通信系统（GSM）时设置。

<a id="ace117d5d35a3b6a41b87b05315f7a19e"></a>

### `lte`

```c
struct sim7080_ue_sys_info_lte sim7080_ue_sys_info::lte
```

仅在系统模式为 LTE CAT-M1 或窄带物联网（NB-IoT）时设置。

<a id="a77e0794049df94d1c6c106a1554fa6ea"></a>

### `op_mode`

```c
enum sim7080_ue_op_mode sim7080_ue_sys_info::op_mode
```

参见 `sim7080_ue_op_mode`。

<a id="a47f14459263b13749a3722107a20631c"></a>

### `sys_mode`

```c
enum sim7080_ue_sys_mode sim7080_ue_sys_info::sys_mode
```

参见 `sim7080_ue_sys_mode`。

本数据类型文档由以下文件生成：

- `zephyr/drivers/modem/simcom-sim7080.h`

## 68.3\_原页交叉引用（Cross References）

- [zephyr/drivers/modem/simcom-sim7080.h](https://docs.zephyrproject.org/latest/doxygen/html/simcom-sim7080_8h_source.html)
- [sim7080_ue_sys_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#ga25a5a23ca32dbd4bc7991274d3d1ce04)
- [sim7080_ue_op_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__simcom__sim7080__interface.html#gaeda25db4347c7fcfbee69e8d6edace64)
- [sim7080_ue_sys_info_gsm](P069_sim7080_ue_sys_info_gsm_结构体.md)
- [sim7080_ue_sys_info_lte](P070_sim7080_ue_sys_info_lte_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P067_sim7080_sms_buffer_结构体.md) · [返回大纲](大纲.md) · [下一章](P069_sim7080_ue_sys_info_gsm_结构体.md)
