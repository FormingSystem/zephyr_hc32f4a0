---
id: learning.zephyr-docs.shell-management-reference.page-7
title: mcumgr_Shell传输接口
kind: reference
status: maintained
domains: [zephyr, shell, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__shell.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_mcumgr\_Shell传输接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__shell.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入蓝牙Mesh Shell、mcumgr Shell管理与SMP传输接口。源码跟踪译注与官方原文分开标示。

允许通过Zephyr Shell使用MCUmgr简单管理协议（Simple Management Protocol，SMP）。

<a id="details"></a>

允许通过Zephyr Shell使用MCUmgr简单管理协议（Simple Management Protocol，SMP）。

<a id="header-files"></a>
<a id="files"></a>

## 7.1\_文件（Files）

<a id="r_smp_5Fshell_2Eh"></a>

```c
file smp_shell.h
```

相关声明：[smp_shell.h](P008_SMP_Shell头文件参考.md)。

用于mcumgr SMP协议的Shell传输（Shell Transport）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 7.2\_数据结构（Data Structures）

<a id="r_smp_5Fshell_5Fdata"></a>

```c
struct smp_shell_data
```

相关声明：[smp_shell_data](P010_SMP_Shell运行数据.md)。

SMP Shell使用的数据。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 7.3\_宏定义（Macros）

<a id="r_ga472d6f81315fea4827be0a91557832eb"></a>

```c
#define SMP_SHELL_RX_BUF_SIZE 127
```

相关声明：[SMP_SHELL_RX_BUF_SIZE](#ga472d6f81315fea4827be0a91557832eb)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 7.4\_函数（Functions）

<a id="r_ga785293b670fcc10190e6c3d480a7d6d6"></a>

```c
size_t smp_shell_rx_bytes (struct smp_shell_data *data, const uint8_t *bytes, size_t size)
```

相关声明：[smp_shell_rx_bytes](#ga785293b670fcc10190e6c3d480a7d6d6)、[smp_shell_data](P010_SMP_Shell运行数据.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

尝试将收到的字节作为SMP帧（Frame）的一部分处理。

<a id="r_ga44b90f6ba276d8d7a89d6b90c8bb0341"></a>

```c
void smp_shell_process (struct smp_shell_data *data)
```

相关声明：[smp_shell_process](#ga44b90f6ba276d8d7a89d6b90c8bb0341)、[smp_shell_data](P010_SMP_Shell运行数据.md)。

处理SMP数据；收到完整帧时执行命令。

<a id="r_ga1b71c4da07049b47269002ef6ec2b256"></a>

```c
int smp_shell_init (void)
```

相关声明：[smp_shell_init](#ga1b71c4da07049b47269002ef6ec2b256)。

初始化通过Shell承载的SMP传输（SMP Transport）。

## 7.5\_详细说明（Detailed Documentation）

<a id="ga472d6f81315fea4827be0a91557832eb"></a>

### `SMP_SHELL_RX_BUF_SIZE`

```c
#define SMP_SHELL_RX_BUF_SIZE 127
```

```c
#include <zephyr/mgmt/mcumgr/transport/smp_shell.h>
```

<a id="ga1b71c4da07049b47269002ef6ec2b256"></a>

### `smp_shell_init()`

```c
int smp_shell_init ( void )
```

```c
#include <zephyr/mgmt/mcumgr/transport/smp_shell.h>
```

初始化通过Shell承载的SMP传输（SMP Transport）。

在向SMP传输提供接收数据前，应先调用此函数。

返回（Returns）：成功为0。

<a id="ga44b90f6ba276d8d7a89d6b90c8bb0341"></a>

### `smp_shell_process()`

```c
void smp_shell_process ( struct smp_shell_data * data)
```

```c
#include <zephyr/mgmt/mcumgr/transport/smp_shell.h>
```

处理SMP数据；收到完整帧时执行命令。

应从线程上下文（Thread Context）调用此函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `data` | SMP Shell传输数据（Transfer Data）。 |

<a id="ga785293b670fcc10190e6c3d480a7d6d6"></a>

### `smp_shell_rx_bytes()`

```c
size_t smp_shell_rx_bytes ( struct smp_shell_data * data, const uint8_t * bytes, size_t size )
```

```c
#include <zephyr/mgmt/mcumgr/transport/smp_shell.h>
```

尝试将收到的字节作为SMP帧（Frame）的一部分处理。

从缓冲区开头扫描，消费属于SMP帧的所有字节，直到到达帧末尾或缓冲区末尾。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `data` | SMP Shell传输数据（Transfer Data）。 |
| `bytes` | 包含待处理字节的缓冲区。 |
| `size` | 待处理的字节数。 |

返回（Returns）：SMP消费的字节数。

## 7.6\_源码定位与版本边界

源码定位：[include/zephyr/mgmt/mcumgr/transport/smp_shell.h](../../../include/zephyr/mgmt/mcumgr/transport/smp_shell.h)、[subsys/mgmt/mcumgr/transport/src/smp_shell.c](../../../subsys/mgmt/mcumgr/transport/src/smp_shell.c)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下源码跟踪译注独立于官方正文，依据来源记录中登记的官方main文件。

> 译注——源码核对：rx_bytes的返回值是本次消费的输入字节数，不是完成的帧数，也不是命令执行结果。它扫描到帧或缓冲区末尾为止；完整帧的后续处理由process完成。

> 译注——源码核对：process应在线程上下文调用，并从就绪FIFO取出帧进行处理。活动接收缓冲和已排队帧分别由buf与buf_ready表示，不能把当前缓冲指针非NULL当作整帧已接收的证据。

> 译注——源码核对：接收前先完成smp_shell_init。此初始化与普通Shell实例初始化、具体UART硬件配置属于不同阶段，接口返回0只描述本次初始化结果。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 7.7\_原页交叉引用（Cross References）

- [smp_shell.h](P008_SMP_Shell头文件参考.md)
- [smp_shell_data](P010_SMP_Shell运行数据.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P006_Shell管理头文件源码.md) · [返回大纲](大纲.md) · [下一章](P008_SMP_Shell头文件参考.md)
