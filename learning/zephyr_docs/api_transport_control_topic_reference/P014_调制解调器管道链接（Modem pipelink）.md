---
id: learning.zephyr-docs.api-transport-control-topic-reference.page-14
title: 调制解调器管道链接（Modem pipelink）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipelink.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_调制解调器管道链接（Modem pipelink）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipelink.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

调制解调器管道链接（Modem pipelink）

<a id="details"></a>

调制解调器管道链接（Modem Pipelink）。**引入版本（Since）：**3.7。**版本（Version）：**1.0.0。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 14.1\_宏定义（Macros）

<a id="r_ga46d06461a5a465f4a73c135f721e3aa5"></a>

```c
#define MODEM_PIPELINK_DT_DECLARE(node_id, name)
```

相关声明：[MODEM_PIPELINK_DT_DECLARE](#ga46d06461a5a465f4a73c135f721e3aa5)。

根据设备树节点标识符（Devicetree Node Identifier）和名称声明管道链接（Pipelink）。

<a id="r_gac1010375931a7a5076d066e2c5ed9a14"></a>

```c
#define MODEM_PIPELINK_DT_DEFINE(node_id, name)
```

相关声明：[MODEM_PIPELINK_DT_DEFINE](#gac1010375931a7a5076d066e2c5ed9a14)。

根据设备树节点标识符（Devicetree Node Identifier）和名称定义管道链接（Pipelink）。

<a id="r_gada75e5995e78c8c8daa5a16f5e5abb4a"></a>

```c
#define MODEM_PIPELINK_DT_GET(node_id, name)
```

相关声明：[MODEM_PIPELINK_DT_GET](#gada75e5995e78c8c8daa5a16f5e5abb4a)。

根据设备树节点标识符（Devicetree Node Identifier）和名称获取管道链接（Pipelink）指针。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 14.2\_类型定义（Typedefs）

<a id="r_ga4f93732f1df6cab41cc352526d6a849e"></a>

```c
typedef void(* modem_pipelink_callback) (struct modem_pipelink *link, enum modem_pipelink_event event, void *user_data)
```

相关声明：[modem_pipelink_callback](#ga4f93732f1df6cab41cc352526d6a849e)、[modem_pipelink_event](#ga399168cacd287e376df68c4cf221ba00)。

管道链接（Pipelink）回调定义。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 14.3\_枚举（Enumerations）

<a id="r_ga399168cacd287e376df68c4cf221ba00"></a>

```c
enum modem_pipelink_event { MODEM_PIPELINK_EVENT_CONNECTED = 0 , MODEM_PIPELINK_EVENT_DISCONNECTED }
```

相关声明：[modem_pipelink_event](#ga399168cacd287e376df68c4cf221ba00)、[MODEM_PIPELINK_EVENT_CONNECTED](#gga399168cacd287e376df68c4cf221ba00ab1a51a16b5dbe02ebca8fb0efe4be81f)、[MODEM_PIPELINK_EVENT_DISCONNECTED](#gga399168cacd287e376df68c4cf221ba00ae118b022efcba2033701dfb8f2e7d38d)。

管道链接（Pipelink）事件。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 14.4\_函数（Functions）

<a id="r_ga7ee7b3454a9fe94c20855a893dd2b2a1"></a>

```c
void modem_pipelink_attach (struct modem_pipelink *link, modem_pipelink_callback callback, void *user_data)
```

相关声明：[modem_pipelink_attach](#ga7ee7b3454a9fe94c20855a893dd2b2a1)、[modem_pipelink_callback](#ga4f93732f1df6cab41cc352526d6a849e)。

将回调（Callback）附加到管道链接（Pipelink）。

<a id="r_ga7c7638ad3f22533f374e002b787b11ce"></a>

```c
bool modem_pipelink_is_connected (struct modem_pipelink *link)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[modem_pipelink_is_connected](#ga7c7638ad3f22533f374e002b787b11ce)。

检查管道链接（Pipelink）的管道（Pipe）是否已连接。

<a id="r_gab09d76f7bd93a19b82a7d5e818b80d80"></a>

```c
struct modem_pipe * modem_pipelink_get_pipe (struct modem_pipelink *link)
```

相关声明：[modem_pipelink_get_pipe](#gab09d76f7bd93a19b82a7d5e818b80d80)。

从管道链接（Pipelink）获取管道（Pipe）。

<a id="r_ga684ff47ddb0e0487022cea62052b32e2"></a>

```c
void modem_pipelink_release (struct modem_pipelink *link)
```

相关声明：[modem_pipelink_release](#ga684ff47ddb0e0487022cea62052b32e2)。

清除回调（Callback）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 14.5\_MODEM_PIPELINK_DT_INST 宏（Macros）

`MODEM_PIPELINK_DT` 宏的设备驱动实例变体（Device Driver Instance Variants）。



<a id="r_gaedc5b4665d541fe4d471a287177e6674"></a>

```c
#define MODEM_PIPELINK_DT_INST_DECLARE(inst, name)
```

相关声明：[MODEM_PIPELINK_DT_INST_DECLARE](#gaedc5b4665d541fe4d471a287177e6674)。

<a id="r_ga1ca071affbb19bfac4c2ef7f25bf9c65"></a>

```c
#define MODEM_PIPELINK_DT_INST_DEFINE(inst, name)
```

相关声明：[MODEM_PIPELINK_DT_INST_DEFINE](#ga1ca071affbb19bfac4c2ef7f25bf9c65)。

<a id="r_ga1c3a0ff1f1939e12fdefee85a7f5eeed"></a>

```c
#define MODEM_PIPELINK_DT_INST_GET(inst, name)
```

相关声明：[MODEM_PIPELINK_DT_INST_GET](#ga1c3a0ff1f1939e12fdefee85a7f5eeed)。

## 14.6\_详细说明（Detailed Documentation）

<a id="ga46d06461a5a465f4a73c135f721e3aa5"></a>

### `MODEM_PIPELINK_DT_DECLARE`

```c
#define MODEM_PIPELINK_DT_DECLARE ( node_id, name )
```

```c
#include <zephyr/modem/pipelink.h>
```

展开值（Value）：

```c
extern struct modem_pipelink MODEM_PIPELINK_DT_SYM(node_id, name)
```

根据设备树节点标识符（Devicetree Node Identifier）和名称声明管道链接（Pipelink）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 设备树节点标识符（Devicetree Node Identifier）。 |
| `name` | 管道链接名称（Pipelink Name）。 |

<a id="gac1010375931a7a5076d066e2c5ed9a14"></a>

### `MODEM_PIPELINK_DT_DEFINE`

```c
#define MODEM_PIPELINK_DT_DEFINE ( node_id, name )
```

```c
#include <zephyr/modem/pipelink.h>
```

展开值（Value）：

```c
struct modem_pipelink MODEM_PIPELINK_DT_SYM(node_id, name)
```

根据设备树节点标识符（Devicetree Node Identifier）和名称定义管道链接（Pipelink）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 设备树节点标识符（Devicetree Node Identifier）。 |
| `name` | 管道链接名称（Pipelink Name）。 |

<a id="gada75e5995e78c8c8daa5a16f5e5abb4a"></a>

### `MODEM_PIPELINK_DT_GET`

```c
#define MODEM_PIPELINK_DT_GET ( node_id, name )
```

```c
#include <zephyr/modem/pipelink.h>
```

展开值（Value）：

```c
(&MODEM_PIPELINK_DT_SYM(node_id, name))
```

根据设备树节点标识符（Devicetree Node Identifier）和名称获取管道链接（Pipelink）指针。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 设备树节点标识符（Devicetree Node Identifier）。 |
| `name` | 管道链接名称（Pipelink Name）。 |

<a id="gaedc5b4665d541fe4d471a287177e6674"></a>

### `MODEM_PIPELINK_DT_INST_DECLARE`

```c
#define MODEM_PIPELINK_DT_INST_DECLARE ( inst, name )
```

```c
#include <zephyr/modem/pipelink.h>
```

展开值（Value）：

```c
MODEM_PIPELINK_DT_DECLARE(DT_DRV_INST(inst), name)
```

<a id="ga1ca071affbb19bfac4c2ef7f25bf9c65"></a>

### `MODEM_PIPELINK_DT_INST_DEFINE`

```c
#define MODEM_PIPELINK_DT_INST_DEFINE ( inst, name )
```

```c
#include <zephyr/modem/pipelink.h>
```

展开值（Value）：

```c
MODEM_PIPELINK_DT_DEFINE(DT_DRV_INST(inst), name)
```

<a id="ga1c3a0ff1f1939e12fdefee85a7f5eeed"></a>

### `MODEM_PIPELINK_DT_INST_GET`

```c
#define MODEM_PIPELINK_DT_INST_GET ( inst, name )
```

```c
#include <zephyr/modem/pipelink.h>
```

展开值（Value）：

```c
MODEM_PIPELINK_DT_GET(DT_DRV_INST(inst), name)
```

<a id="ga4f93732f1df6cab41cc352526d6a849e"></a>

### `modem_pipelink_callback`

```c
typedef void(* modem_pipelink_callback) (struct modem_pipelink *link, enum modem_pipelink_event event, void *user_data)
```

```c
#include <zephyr/modem/pipelink.h>
```

管道链接（Pipelink）回调定义。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `link` | 调制解调器管道链接实例（Modem Pipelink Instance）。 |
| `event` | 调制解调器管道链接事件（Modem Pipelink Event）。 |
| `user_data` | 传递给 `modem_pipelink_attach()` 的用户数据（User Data）。 |

<a id="ga399168cacd287e376df68c4cf221ba00"></a>

### `modem_pipelink_event`

```c
enum modem_pipelink_event
```

```c
#include <zephyr/modem/pipelink.h>
```

管道链接（Pipelink）事件。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MODEM_PIPELINK_EVENT_CONNECTED` | 调制解调器管道（Modem Pipe）已连接，可以打开。 |
| `MODEM_PIPELINK_EVENT_DISCONNECTED` | 调制解调器管道（Modem Pipe）已断开，无法打开。 |

<a id="ga7ee7b3454a9fe94c20855a893dd2b2a1"></a>

### `modem_pipelink_attach()`

```c
void modem_pipelink_attach ( struct modem_pipelink * link, modem_pipelink_callback callback, void * user_data )
```

```c
#include <zephyr/modem/pipelink.h>
```

将回调（Callback）附加到管道链接（Pipelink）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `link` | 管道链接实例（Pipelink Instance）。 |
| `callback` | 管道链接回调（Pipelink Callback）。 |
| `user_data` | 传递给管道链接回调（Pipelink Callback）的用户数据（User Data）。 |

<a id="gab09d76f7bd93a19b82a7d5e818b80d80"></a>

### `modem_pipelink_get_pipe()`

```c
struct modem_pipe * modem_pipelink_get_pipe ( struct modem_pipelink * link)
```

```c
#include <zephyr/modem/pipelink.h>
```

从管道链接（Pipelink）获取管道（Pipe）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `link` | 管道链接实例（Pipelink Instance）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `NULL` | 管道链接（Pipelink）尚未初始化时。 |

**返回（Returns）**：**返回值（Returns）：**管道链接（Pipelink）已初始化时，返回管道（Pipe）指针。

<a id="ga7c7638ad3f22533f374e002b787b11ce"></a>

### `modem_pipelink_is_connected()`

```c
bool modem_pipelink_is_connected ( struct modem_pipelink * link)
```

```c
#include <zephyr/modem/pipelink.h>
```

检查管道链接（Pipelink）的管道（Pipe）是否已连接。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `link` | 管道链接实例（Pipelink Instance）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | 管道（Pipe）已连接时。 |
| `false` | 管道（Pipe）未连接时。 |

<a id="ga684ff47ddb0e0487022cea62052b32e2"></a>

### `modem_pipelink_release()`

```c
void modem_pipelink_release ( struct modem_pipelink * link)
```

```c
#include <zephyr/modem/pipelink.h>
```

清除回调（Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `link` | 管道链接实例（Pipelink Instance）。 |


## 14.7\_原页交叉引用（Cross References）

- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [zephyr/modem/pipelink.h](../api_file_transfer_device_reference/P031_zephyr__modem__pipelink.h_文件参考.md)
- [DT_DRV_INST](../dt_instance_reference/P001_设备树驱动实例宏.md#ga219f413efba2f4c0151468b9a25a8dc1)
- [true](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7)
- [false](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a65e9886d74aaee76545e83dd09011727)

<a id="MODEM_PIPELINK_DT_INST"></a>
<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__devicetree-inst_html_ga219f413efba2f4c0151468b9a25a8dc1"></a>
<a id="agroup__modem__pipelink_html_ga46d06461a5a465f4a73c135f721e3aa5"></a>
<a id="agroup__modem__pipelink_html_gac1010375931a7a5076d066e2c5ed9a14"></a>
<a id="agroup__modem__pipelink_html_gada75e5995e78c8c8daa5a16f5e5abb4a"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga399168cacd287e376df68c4cf221ba00ab1a51a16b5dbe02ebca8fb0efe4be81f"></a>
<a id="gga399168cacd287e376df68c4cf221ba00ae118b022efcba2033701dfb8f2e7d38d"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P013_MLX90394 API主题.md) · [返回大纲](大纲.md) · [下一章](P015_调制解调器 UBX 协议（Modem Ubx）.md)
