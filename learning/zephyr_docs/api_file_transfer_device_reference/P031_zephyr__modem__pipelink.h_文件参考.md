---
id: learning.zephyr-docs.api-file-transfer-device-reference.page-31
title: zephyr__modem__pipelink.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pipelink_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第31章\_zephyr\_\_modem\_\_pipelink.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/pipelink_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/modem/pipe.h>
#include <zephyr/devicetree.h>
#include <zephyr/sys/util.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 31.1\_宏定义（Macros）

<a id="r_ga46d06461a5a465f4a73c135f721e3aa5"></a>

```c
#define MODEM_PIPELINK_DT_DECLARE(node_id, name)
```

相关声明：[MODEM_PIPELINK_DT_DECLARE](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipelink.html#ga46d06461a5a465f4a73c135f721e3aa5)。

根据设备树节点标识符（Devicetree Node Identifier）和名称声明管道链接（Pipelink）。

<a id="r_gac1010375931a7a5076d066e2c5ed9a14"></a>

```c
#define MODEM_PIPELINK_DT_DEFINE(node_id, name)
```

相关声明：[MODEM_PIPELINK_DT_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipelink.html#gac1010375931a7a5076d066e2c5ed9a14)。

根据设备树节点标识符（Devicetree Node Identifier）和名称定义管道链接（Pipelink）。

<a id="r_gada75e5995e78c8c8daa5a16f5e5abb4a"></a>

```c
#define MODEM_PIPELINK_DT_GET(node_id, name)
```

相关声明：[MODEM_PIPELINK_DT_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipelink.html#gada75e5995e78c8c8daa5a16f5e5abb4a)。

根据设备树节点标识符（Devicetree Node Identifier）和名称获取管道链接（Pipelink）指针。

<a id="define-members-0"></a>

### MODEM_PIPELINK_DT_INST 宏（Macros）

`MODEM_PIPELINK_DT` 宏的设备驱动实例变体（Device Driver Instance Variants）。



<a id="r_gaedc5b4665d541fe4d471a287177e6674"></a>

```c
#define MODEM_PIPELINK_DT_INST_DECLARE(inst, name)
```

相关声明：[MODEM_PIPELINK_DT_INST_DECLARE](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipelink.html#gaedc5b4665d541fe4d471a287177e6674)。

<a id="r_ga1ca071affbb19bfac4c2ef7f25bf9c65"></a>

```c
#define MODEM_PIPELINK_DT_INST_DEFINE(inst, name)
```

相关声明：[MODEM_PIPELINK_DT_INST_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipelink.html#ga1ca071affbb19bfac4c2ef7f25bf9c65)。

<a id="r_ga1c3a0ff1f1939e12fdefee85a7f5eeed"></a>

```c
#define MODEM_PIPELINK_DT_INST_GET(inst, name)
```

相关声明：[MODEM_PIPELINK_DT_INST_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipelink.html#ga1c3a0ff1f1939e12fdefee85a7f5eeed)。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 31.2\_类型定义（Typedefs）

<a id="r_ga4f93732f1df6cab41cc352526d6a849e"></a>

```c
typedef void(* modem_pipelink_callback) (struct modem_pipelink *link, enum modem_pipelink_event event, void *user_data)
```

相关声明：[modem_pipelink_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipelink.html#ga4f93732f1df6cab41cc352526d6a849e)、[modem_pipelink_event](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipelink.html#ga399168cacd287e376df68c4cf221ba00)。

管道链接（Pipelink）回调定义。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 31.3\_枚举（Enumerations）

<a id="r_ga399168cacd287e376df68c4cf221ba00"></a>

```c
enum modem_pipelink_event { MODEM_PIPELINK_EVENT_CONNECTED = 0 , MODEM_PIPELINK_EVENT_DISCONNECTED }
```

相关声明：[modem_pipelink_event](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipelink.html#ga399168cacd287e376df68c4cf221ba00)、[MODEM_PIPELINK_EVENT_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipelink.html#gga399168cacd287e376df68c4cf221ba00ab1a51a16b5dbe02ebca8fb0efe4be81f)、[MODEM_PIPELINK_EVENT_DISCONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipelink.html#gga399168cacd287e376df68c4cf221ba00ae118b022efcba2033701dfb8f2e7d38d)。

管道链接（Pipelink）事件。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 31.4\_函数（Functions）

<a id="r_ga7ee7b3454a9fe94c20855a893dd2b2a1"></a>

```c
void modem_pipelink_attach (struct modem_pipelink *link, modem_pipelink_callback callback, void *user_data)
```

相关声明：[modem_pipelink_attach](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipelink.html#ga7ee7b3454a9fe94c20855a893dd2b2a1)、[modem_pipelink_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipelink.html#ga4f93732f1df6cab41cc352526d6a849e)。

将回调（Callback）附加到管道链接（Pipelink）。

<a id="r_ga7c7638ad3f22533f374e002b787b11ce"></a>

```c
bool modem_pipelink_is_connected (struct modem_pipelink *link)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[modem_pipelink_is_connected](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipelink.html#ga7c7638ad3f22533f374e002b787b11ce)。

检查管道链接（Pipelink）的管道（Pipe）是否已连接。

<a id="r_gab09d76f7bd93a19b82a7d5e818b80d80"></a>

```c
struct modem_pipe * modem_pipelink_get_pipe (struct modem_pipelink *link)
```

相关声明：[modem_pipelink_get_pipe](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipelink.html#gab09d76f7bd93a19b82a7d5e818b80d80)。

从管道链接（Pipelink）获取管道（Pipe）。

<a id="r_ga684ff47ddb0e0487022cea62052b32e2"></a>

```c
void modem_pipelink_release (struct modem_pipelink *link)
```

相关声明：[modem_pipelink_release](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipelink.html#ga684ff47ddb0e0487022cea62052b32e2)。

清除回调（Callback）。


## 31.5\_原页交叉引用（Cross References）

- [zephyr/modem/pipe.h](../api_source_supplement_reference/P145_pipe.h_源码浏览.md)
- [zephyr/devicetree.h](../dt_main_reference/P002_设备树主头文件源码.md)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P661_pipelink.h_源码浏览.md)
- [MODEM_PIPELINK_DT_DECLARE](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipelink.html#ga46d06461a5a465f4a73c135f721e3aa5)
- [MODEM_PIPELINK_DT_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipelink.html#gac1010375931a7a5076d066e2c5ed9a14)
- [MODEM_PIPELINK_DT_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipelink.html#gada75e5995e78c8c8daa5a16f5e5abb4a)
- [MODEM_PIPELINK_DT_INST_DECLARE](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipelink.html#gaedc5b4665d541fe4d471a287177e6674)
- [MODEM_PIPELINK_DT_INST_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipelink.html#ga1ca071affbb19bfac4c2ef7f25bf9c65)
- [MODEM_PIPELINK_DT_INST_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipelink.html#ga1c3a0ff1f1939e12fdefee85a7f5eeed)
- [modem_pipelink_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipelink.html#ga4f93732f1df6cab41cc352526d6a849e)
- [modem_pipelink_event](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipelink.html#ga399168cacd287e376df68c4cf221ba00)
- [MODEM_PIPELINK_EVENT_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipelink.html#gga399168cacd287e376df68c4cf221ba00ab1a51a16b5dbe02ebca8fb0efe4be81f)
- [MODEM_PIPELINK_EVENT_DISCONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipelink.html#gga399168cacd287e376df68c4cf221ba00ae118b022efcba2033701dfb8f2e7d38d)
- [modem_pipelink_attach](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipelink.html#ga7ee7b3454a9fe94c20855a893dd2b2a1)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [modem_pipelink_is_connected](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipelink.html#ga7c7638ad3f22533f374e002b787b11ce)
- [modem_pipelink_get_pipe](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipelink.html#gab09d76f7bd93a19b82a7d5e818b80d80)
- [modem_pipelink_release](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipelink.html#ga684ff47ddb0e0487022cea62052b32e2)

<a id="MODEM_PIPELINK_DT_INST"></a>

---

[上一章](P030_zephyr__modem__pipe.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P032_zephyr__drivers__interrupt_controller__riscv_imsic.h_文件参考.md)
