---
id: learning.zephyr-docs.modem-wireless-model-reference.page-20
title: hl78xx_cxreg_status_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structhl78xx__cxreg__status.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_hl78xx\_cxreg\_status\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structhl78xx__cxreg__status.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

缓存的+CEREG/+CREG注册详情。

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

<a id="details"></a>

缓存的+CEREG/+CREG注册详情。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 20.1\_数据成员（Data Fields）

<a id="r_a4b5acff39666484d3aa7f4920a33c195"></a>

```c
enum cellular_registration_status reg_status
```

相关声明：[cellular_registration_status](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga7309390ed507748fdb72cf078b8e08a4)、[reg_status](#a4b5acff39666484d3aa7f4920a33c195)。

从 `+CEREG/+CREG` 获得的注册状态。

<a id="r_a8674887283917c025827e2d24e07aa21"></a>

```c
bool has_tac
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[has_tac](#a8674887283917c025827e2d24e07aa21)。

存在已解析的跟踪区代码（TAC）。

<a id="r_ae28a6c477536c15740ec07615b156d37"></a>

```c
uint32_t tac
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[tac](#ae28a6c477536c15740ec07615b156d37)。

从 `+CEREG/+CREG` 获得的跟踪区代码。

<a id="r_a60f715d0323fa365590d6e6eb8f276fa"></a>

```c
bool has_cell_id
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[has_cell_id](#a60f715d0323fa365590d6e6eb8f276fa)。

存在已解析的小区 ID。

<a id="r_a6c744edb85c63395147b1b55da6dcc9d"></a>

```c
uint32_t cell_id
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[cell_id](#a6c744edb85c63395147b1b55da6dcc9d)。

从 `+CEREG/+CREG` 获得的小区 ID。

<a id="r_aa5277387244ff33df4622bcd966138d2"></a>

```c
bool has_rat_mode
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[has_rat_mode](#aa5277387244ff33df4622bcd966138d2)。

存在已解析的无线接入技术（RAT）模式。

<a id="r_ac5661b4086fb1be97cb562ac0080303c"></a>

```c
enum hl78xx_cell_rat_mode rat_mode
```

相关声明：[hl78xx_cell_rat_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga298f953be96ab47be40b5440a2573182)、[rat_mode](#ac5661b4086fb1be97cb562ac0080303c)。

从 `+CEREG/+CREG` 的 `AcT` 字段得到的 RAT 模式。

<a id="r_ab93a65b47faea7a583313bd74ea2be24"></a>

```c
bool has_cause_type
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[has_cause_type](#ab93a65b47faea7a583313bd74ea2be24)。

存在原因类型（cause type）。

<a id="r_aa79861dc75aa6db380d719bd291d6297"></a>

```c
int cause_type
```

相关声明：[cause_type](#aa79861dc75aa6db380d719bd291d6297)。

注册拒绝的原因类型。

<a id="r_ac35cd02f962b64890911b0792d7310e0"></a>

```c
bool has_reject_cause
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[has_reject_cause](#ac35cd02f962b64890911b0792d7310e0)。

存在拒绝原因（reject cause）。

<a id="r_afc07b878db1a4ebd74c1b642c5222866"></a>

```c
int reject_cause
```

相关声明：[reject_cause](#afc07b878db1a4ebd74c1b642c5222866)。

拒绝原因值。

<a id="r_a1b1616b638324a1073a81e2c51d7082a"></a>

```c
bool has_active_time
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[has_active_time](#a1b1616b638324a1073a81e2c51d7082a)。

存在活动时间（active time）字段。

<a id="r_aaec559842aa44a208c800c1056dc1960"></a>

```c
char active_time [9]
```

相关声明：[active_time](#aaec559842aa44a208c800c1056dc1960)。

原始活动时间定时器字符串。

<a id="r_aeb8daf30feb1b4c82888f5ce393b2adf"></a>

```c
bool has_tau
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[has_tau](#aeb8daf30feb1b4c82888f5ce393b2adf)。

存在跟踪区更新（TAU）字段。

<a id="r_a90f9a217168113e3b223e6fee7d3a484"></a>

```c
char tau [9]
```

相关声明：[tau](#a90f9a217168113e3b223e6fee7d3a484)。

原始 TAU 定时器字符串。

## 20.2\_详细说明（Detailed Documentation）

<a id="aaec559842aa44a208c800c1056dc1960"></a>

### `active_time`

```c
char hl78xx_cxreg_status::active_time[9]
```

原始活动时间定时器字符串。

<a id="aa79861dc75aa6db380d719bd291d6297"></a>

### `cause_type`

```c
int hl78xx_cxreg_status::cause_type
```

注册拒绝的原因类型。

<a id="a6c744edb85c63395147b1b55da6dcc9d"></a>

### `cell_id`

```c
uint32_t hl78xx_cxreg_status::cell_id
```

从 `+CEREG/+CREG` 获得的小区 ID。

<a id="a1b1616b638324a1073a81e2c51d7082a"></a>

### `has_active_time`

```c
bool hl78xx_cxreg_status::has_active_time
```

存在活动时间（active time）字段。

<a id="ab93a65b47faea7a583313bd74ea2be24"></a>

### `has_cause_type`

```c
bool hl78xx_cxreg_status::has_cause_type
```

存在原因类型（cause type）。

<a id="a60f715d0323fa365590d6e6eb8f276fa"></a>

### `has_cell_id`

```c
bool hl78xx_cxreg_status::has_cell_id
```

存在已解析的小区 ID。

<a id="aa5277387244ff33df4622bcd966138d2"></a>

### `has_rat_mode`

```c
bool hl78xx_cxreg_status::has_rat_mode
```

存在已解析的无线接入技术（RAT）模式。

<a id="ac35cd02f962b64890911b0792d7310e0"></a>

### `has_reject_cause`

```c
bool hl78xx_cxreg_status::has_reject_cause
```

存在拒绝原因（reject cause）。

<a id="a8674887283917c025827e2d24e07aa21"></a>

### `has_tac`

```c
bool hl78xx_cxreg_status::has_tac
```

存在已解析的跟踪区代码（TAC）。

<a id="aeb8daf30feb1b4c82888f5ce393b2adf"></a>

### `has_tau`

```c
bool hl78xx_cxreg_status::has_tau
```

存在跟踪区更新（TAU）字段。

<a id="ac5661b4086fb1be97cb562ac0080303c"></a>

### `rat_mode`

```c
enum hl78xx_cell_rat_mode hl78xx_cxreg_status::rat_mode
```

从 `+CEREG/+CREG` 的 `AcT` 字段得到的 RAT 模式。

<a id="a4b5acff39666484d3aa7f4920a33c195"></a>

### `reg_status`

```c
enum cellular_registration_status hl78xx_cxreg_status::reg_status
```

从 `+CEREG/+CREG` 获得的注册状态。

<a id="afc07b878db1a4ebd74c1b642c5222866"></a>

### `reject_cause`

```c
int hl78xx_cxreg_status::reject_cause
```

拒绝原因值。

<a id="ae28a6c477536c15740ec07615b156d37"></a>

### `tac`

```c
uint32_t hl78xx_cxreg_status::tac
```

从 `+CEREG/+CREG` 获得的跟踪区代码。

<a id="a90f9a217168113e3b223e6fee7d3a484"></a>

### `tau`

```c
char hl78xx_cxreg_status::tau[9]
```

原始 TAU 定时器字符串。

本数据类型文档由以下文件生成：

- `zephyr/drivers/modem/hl78xx_apis.h`

## 20.3\_原页交叉引用（Cross References）

- [zephyr/drivers/modem/hl78xx_apis.h](https://docs.zephyrproject.org/latest/doxygen/html/hl78xx__apis_8h_source.html)
- [cellular_registration_status](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga7309390ed507748fdb72cf078b8e08a4)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [hl78xx_cell_rat_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga298f953be96ab47be40b5440a2573182)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P019_hl78xx_ctzeu_update_结构体.md) · [返回大纲](大纲.md) · [下一章](P021_hl78xx_evt_结构体.md)
