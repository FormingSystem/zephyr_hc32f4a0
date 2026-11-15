---
id: learning.zephyr-docs.api-radio-permission-topic-reference.page-16
title: 半主机 API（Semihosting APIs）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_半主机 API（Semihosting APIs）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 16.1\_枚举（Enumerations）

<a id="r_gadf61e00be557b7cb4457f7ea6f8da86d"></a>

```c
enum semihost_instr { SEMIHOST_OPEN = 0x01 , SEMIHOST_ISTTY = 0x09 , SEMIHOST_WRITE = 0x05 , SEMIHOST_READ = 0x06 , SEMIHOST_CLOSE = 0x02 , SEMIHOST_FLEN = 0x0C , SEMIHOST_SEEK = 0x0A , SEMIHOST_TMPNAM = 0x0D , SEMIHOST_REMOVE = 0x0E , SEMIHOST_RENAME = 0x0F , SEMIHOST_WRITEC = 0x03 , SEMIHOST_WRITE0 = 0x04 , SEMIHOST_READC = 0x07 , SEMIHOST_CLOCK = 0x10 , SEMIHOST_ELAPSED = 0x30 , SEMIHOST_TICKFREQ = 0x31 , SEMIHOST_TIME = 0x11 , SEMIHOST_ERRNO = 0x13 , SEMIHOST_GET_CMDLINE = 0x15 , SEMIHOST_HEAPINFO = 0x16 , SEMIHOST_ISERROR = 0x08 , SEMIHOST_SYSTEM = 0x12 }
```

相关声明：[semihost_instr](#gadf61e00be557b7cb4457f7ea6f8da86d)、[SEMIHOST_OPEN](#ggadf61e00be557b7cb4457f7ea6f8da86da32cc33a795888c73c3d1624f288fed46)、[SEMIHOST_ISTTY](#ggadf61e00be557b7cb4457f7ea6f8da86dad92d3362fc63d17b0f6c74f1c796ae53)、[SEMIHOST_WRITE](#ggadf61e00be557b7cb4457f7ea6f8da86dac1da151904c09d05b4548f1c28bb72ad)、[SEMIHOST_READ](#ggadf61e00be557b7cb4457f7ea6f8da86da0e589cd7b9f53eeb303a419487e40a02)、[SEMIHOST_CLOSE](#ggadf61e00be557b7cb4457f7ea6f8da86daa800fb6638cb45941c81d41275779cac)、[SEMIHOST_FLEN](#ggadf61e00be557b7cb4457f7ea6f8da86daf6894316046e0cd2c07c7f55effddc8d)、[SEMIHOST_SEEK](#ggadf61e00be557b7cb4457f7ea6f8da86dad030bc2e7a63682116efb84011d40629)、[SEMIHOST_TMPNAM](#ggadf61e00be557b7cb4457f7ea6f8da86dad0ed15a780a1d9bd8583e01468f4abeb)、[SEMIHOST_REMOVE](#ggadf61e00be557b7cb4457f7ea6f8da86da88b03906fd14fe40d86c841de05539ce)、[SEMIHOST_RENAME](#ggadf61e00be557b7cb4457f7ea6f8da86da3e584069d9d8cd126bd409df9f99d627)、[SEMIHOST_WRITEC](#ggadf61e00be557b7cb4457f7ea6f8da86da6edbfcd0d356552569ae1cfcd78203a7)、[SEMIHOST_WRITE0](#ggadf61e00be557b7cb4457f7ea6f8da86da6d4f5801467a25613abf1d38386060ff)、[SEMIHOST_READC](#ggadf61e00be557b7cb4457f7ea6f8da86dae3a468fafe97de23a4d0b125a438e8f6)、[SEMIHOST_CLOCK](#ggadf61e00be557b7cb4457f7ea6f8da86dac17ed558ffacf4612c234db887743ca0)、[SEMIHOST_ELAPSED](#ggadf61e00be557b7cb4457f7ea6f8da86da3db5621dbcb6c8a2a074cc69144f8367)、[SEMIHOST_TICKFREQ](#ggadf61e00be557b7cb4457f7ea6f8da86da59856dd67e4079773f9ada8c3cb5ba26)、[SEMIHOST_TIME](#ggadf61e00be557b7cb4457f7ea6f8da86daffd89aae5102d56b677522ab2b66c438)、[SEMIHOST_ERRNO](#ggadf61e00be557b7cb4457f7ea6f8da86dad8f17a37155fdb3c4e29c4c3ba2b4a4f)、[SEMIHOST_GET_CMDLINE](#ggadf61e00be557b7cb4457f7ea6f8da86daba47d649a03b0ed2bfc6fb8d3020563f)、[SEMIHOST_HEAPINFO](#ggadf61e00be557b7cb4457f7ea6f8da86da8963d2934a740ae5fd04ca84fd48f57f)、[SEMIHOST_ISERROR](#ggadf61e00be557b7cb4457f7ea6f8da86da7e0050f763d6c115c2b24064b4beb6ea)、[SEMIHOST_SYSTEM](#ggadf61e00be557b7cb4457f7ea6f8da86da78d21e53db4f44f375aefd25009dd71a)。

半主机指令（Semihosting Instructions）。

<a id="r_ga425c53a045590978b0b3235d545780f7"></a>

```c
enum semihost_open_mode { SEMIHOST_OPEN_R = 0 , SEMIHOST_OPEN_RB = 1 , SEMIHOST_OPEN_R_PLUS = 2 , SEMIHOST_OPEN_RB_PLUS = 3 , SEMIHOST_OPEN_W = 4 , SEMIHOST_OPEN_WB = 5 , SEMIHOST_OPEN_W_PLUS = 6 , SEMIHOST_OPEN_WB_PLUS = 7 , SEMIHOST_OPEN_A = 8 , SEMIHOST_OPEN_AB = 9 , SEMIHOST_OPEN_A_PLUS = 10 , SEMIHOST_OPEN_AB_PLUS = 11 }
```

相关声明：[semihost_open_mode](#ga425c53a045590978b0b3235d545780f7)、[SEMIHOST_OPEN_R](#gga425c53a045590978b0b3235d545780f7ab7c309dc69b408ade19bff098818471b)、[SEMIHOST_OPEN_RB](#gga425c53a045590978b0b3235d545780f7a1bc8673a95497f17cdebafdc1fe5cdde)、[SEMIHOST_OPEN_R_PLUS](#gga425c53a045590978b0b3235d545780f7a036c2739eb8b2bd43042367d66d644c9)、[SEMIHOST_OPEN_RB_PLUS](#gga425c53a045590978b0b3235d545780f7a99975dc411c6b501ef2f34f31a8aaa53)、[SEMIHOST_OPEN_W](#gga425c53a045590978b0b3235d545780f7a14a3bbe45567c38892ede4f120c888fc)、[SEMIHOST_OPEN_WB](#gga425c53a045590978b0b3235d545780f7a41befb06ac2fcce18e7a085b9e8911bc)、[SEMIHOST_OPEN_W_PLUS](#gga425c53a045590978b0b3235d545780f7abf3d7d2b6e9a99bcacbff1c50bb1d262)、[SEMIHOST_OPEN_WB_PLUS](#gga425c53a045590978b0b3235d545780f7a172b9e36d6fad788501e53116ab84244)、[SEMIHOST_OPEN_A](#gga425c53a045590978b0b3235d545780f7a17270a085663f59c6104b68bf35b7c34)、[SEMIHOST_OPEN_AB](#gga425c53a045590978b0b3235d545780f7a128ed24bf3519c3fa84e3fc996988708)、[SEMIHOST_OPEN_A_PLUS](#gga425c53a045590978b0b3235d545780f7a300dde91715638debca2cbd6a61e508f)、[SEMIHOST_OPEN_AB_PLUS](#gga425c53a045590978b0b3235d545780f7a5357da3dddbeb511d312291cbab9c466)。

打开文件使用的模式（File Open Modes）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 16.2\_函数（Functions）

<a id="r_gab8d683d2011f6683956c47a4b129faf4"></a>

```c
long semihost_exec (enum semihost_instr instr, void *args)
```

相关声明：[semihost_exec](#gab8d683d2011f6683956c47a4b129faf4)、[semihost_instr](#gadf61e00be557b7cb4457f7ea6f8da86d)。

手动执行半主机指令（Semihosting Instruction）。

<a id="r_ga4eb7ceb5ceaaded14c3dc129b7fca07b"></a>

```c
char semihost_poll_in (void)
```

相关声明：[semihost_poll_in](#ga4eb7ceb5ceaaded14c3dc129b7fca07b)。

从控制台（Console）读取一个字节。

<a id="r_ga4026806d0ea1f6d754851ef7b9f1c58c"></a>

```c
void semihost_poll_out (char c)
```

相关声明：[semihost_poll_out](#ga4026806d0ea1f6d754851ef7b9f1c58c)。

向控制台（Console）写入一个字节。

<a id="r_ga497b911ba4e6b40e4e5808fa9484f5a4"></a>

```c
long semihost_open (const char *path, long mode)
```

相关声明：[semihost_open](#ga497b911ba4e6b40e4e5808fa9484f5a4)。

在主机系统（Host System）上打开文件。

<a id="r_gad8e5d671a2316901eefaf86cac43ac43"></a>

```c
long semihost_close (long fd)
```

相关声明：[semihost_close](#gad8e5d671a2316901eefaf86cac43ac43)。

关闭文件（File）。

<a id="r_gae7476b25d69979d488e1bbd3521d70e0"></a>

```c
long semihost_flen (long fd)
```

相关声明：[semihost_flen](#gae7476b25d69979d488e1bbd3521d70e0)。

查询文件大小（File Size）。

<a id="r_ga99f88405f4bdc9f43ab2d59b3526ebbc"></a>

```c
long semihost_seek (long fd, long offset)
```

相关声明：[semihost_seek](#ga99f88405f4bdc9f43ab2d59b3526ebbc)。

定位到文件中的绝对位置（Absolute Position）。

<a id="r_gaf0d429779cd2b3a06c29f93f8641e9af"></a>

```c
long semihost_read (long fd, void *buf, long len)
```

相关声明：[semihost_read](#gaf0d429779cd2b3a06c29f93f8641e9af)。

将文件内容（File Contents）读入缓冲区（Buffer）。

<a id="r_ga6c340fadaa86cddee2817e96caa00edf"></a>

```c
long semihost_write (long fd, const void *buf, long len)
```

相关声明：[semihost_write](#ga6c340fadaa86cddee2817e96caa00edf)。

将缓冲区内容（Buffer Contents）写入文件。

## 16.3\_详细说明（Detailed Documentation）

<a id="gadf61e00be557b7cb4457f7ea6f8da86d"></a>

### `semihost_instr`

```c
enum semihost_instr
```

```c
#include <zephyr/arch/common/semihost.h>
```

半主机指令（Semihosting Instructions）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SEMIHOST_OPEN` | 在主机系统（Host System）上打开文件或流。 |
| `SEMIHOST_ISTTY` | 检查文件是否关联到流／终端（Stream/Terminal）。 |
| `SEMIHOST_WRITE` | 写入文件或流（File or Stream）。 |
| `SEMIHOST_READ` | 从文件的当前游标位置（Cursor Position）读取。 |
| `SEMIHOST_CLOSE` | 关闭主机上由 SEMIHOST_OPEN 打开的文件。 |
| `SEMIHOST_FLEN` | 获取文件长度（File Length）。 |
| `SEMIHOST_SEEK` | 将文件游标（File Cursor）设置到文件中的指定位置。 |
| `SEMIHOST_TMPNAM` | 获取用于创建临时文件的临时绝对文件路径（Temporary Absolute File Path）。 |
| `SEMIHOST_REMOVE` | 移除主机系统（Host System）上的文件。可能不安全（Possibly Insecure）！ |
| `SEMIHOST_RENAME` | 重命名主机系统（Host System）上的文件。可能不安全（Possibly Insecure）！ |
| `SEMIHOST_WRITEC` | 向调试终端（Debug Terminal）写入一个字符。 |
| `SEMIHOST_WRITE0` | 向调试终端（Debug Terminal）写入以 NULL 终止的字符串。 |
| `SEMIHOST_READC` | 从调试终端（Debug Terminal）读取一个字符。 |
| `SEMIHOST_CLOCK` |  |
| `SEMIHOST_ELAPSED` |  |
| `SEMIHOST_TICKFREQ` |  |
| `SEMIHOST_TIME` |  |
| `SEMIHOST_ERRNO` | 获取半主机操作（Semihosting Operations）的 errno 变量。 |
| `SEMIHOST_GET_CMDLINE` | 获取应用运行时使用的命令行参数（Commandline Parameters）。 |
| `SEMIHOST_HEAPINFO` |  |
| `SEMIHOST_ISERROR` |  |
| `SEMIHOST_SYSTEM` |  |

<a id="ga425c53a045590978b0b3235d545780f7"></a>

### `semihost_open_mode`

```c
enum semihost_open_mode
```

```c
#include <zephyr/arch/common/semihost.h>
```

打开文件使用的模式（File Open Modes）。

行为对应 fopen 的等价模式字符串，例如 SEMIHOST_OPEN_RB_PLUS == "rb+"。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SEMIHOST_OPEN_R` |  |
| `SEMIHOST_OPEN_RB` |  |
| `SEMIHOST_OPEN_R_PLUS` |  |
| `SEMIHOST_OPEN_RB_PLUS` |  |
| `SEMIHOST_OPEN_W` |  |
| `SEMIHOST_OPEN_WB` |  |
| `SEMIHOST_OPEN_W_PLUS` |  |
| `SEMIHOST_OPEN_WB_PLUS` |  |
| `SEMIHOST_OPEN_A` |  |
| `SEMIHOST_OPEN_AB` |  |
| `SEMIHOST_OPEN_A_PLUS` |  |
| `SEMIHOST_OPEN_AB_PLUS` |  |

<a id="gad8e5d671a2316901eefaf86cac43ac43"></a>

### `semihost_close()`

```c
long semihost_close ( long fd)
```

```c
#include <zephyr/arch/common/semihost.h>
```

关闭文件（File）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fd` | semihost_open 返回的句柄（Handle）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-1` | 失败。 |

<a id="gab8d683d2011f6683956c47a4b129faf4"></a>

### `semihost_exec()`

```c
long semihost_exec ( enum semihost_instr instr, void * args )
```

```c
#include <zephyr/arch/common/semihost.h>
```

手动执行半主机指令（Semihosting Instruction）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `instr` | 要执行的指令代码（Instruction Code） |
| `args` | 特定指令的参数（Instruction-specific Arguments） |

**返回（Returns）**：返回值（Returns）：指令的整数返回码（Integer Return Code）。

<a id="gae7476b25d69979d488e1bbd3521d70e0"></a>

### `semihost_flen()`

```c
long semihost_flen ( long fd)
```

```c
#include <zephyr/arch/common/semihost.h>
```

查询文件大小（File Size）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fd` | semihost_open 返回的句柄（Handle）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `positive` | 成功时的文件大小。 |
| `-1` | 失败。 |

<a id="ga497b911ba4e6b40e4e5808fa9484f5a4"></a>

### `semihost_open()`

```c
long semihost_open ( const char * path, long mode )
```

```c
#include <zephyr/arch/common/semihost.h>
```

在主机系统（Host System）上打开文件。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `path` | 要打开的文件路径，可以是绝对路径，也可以相对于运行进程的当前目录。 |
| `mode` | semihost_open_mode 中的值。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `handle` | 成功时返回的正句柄（Positive Handle）。 |
| `-1` | 失败。 |

<a id="ga4eb7ceb5ceaaded14c3dc129b7fca07b"></a>

### `semihost_poll_in()`

```c
char semihost_poll_in ( void )
```

```c
#include <zephyr/arch/common/semihost.h>
```

从控制台（Console）读取一个字节。

**返回（Returns）**：返回值（Returns）：从控制台读取的字符字节（Char Byte）。

<a id="ga4026806d0ea1f6d754851ef7b9f1c58c"></a>

### `semihost_poll_out()`

```c
void semihost_poll_out ( char c)
```

```c
#include <zephyr/arch/common/semihost.h>
```

向控制台（Console）写入一个字节。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `c` | 要写入控制台的字节 |

<a id="gaf0d429779cd2b3a06c29f93f8641e9af"></a>

### `semihost_read()`

```c
long semihost_read ( long fd, void * buf, long len )
```

```c
#include <zephyr/arch/common/semihost.h>
```

将文件内容（File Contents）读入缓冲区（Buffer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fd` | semihost_open 返回的句柄（Handle）。 |
| `buf` | 用于读取数据的缓冲区。 |
| `len` | 要读取的字节数。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `read` | 成功时返回读取的字节数。 |
| `-errno` | 失败时返回负错误码。 |

<a id="ga99f88405f4bdc9f43ab2d59b3526ebbc"></a>

### `semihost_seek()`

```c
long semihost_seek ( long fd, long offset )
```

```c
#include <zephyr/arch/common/semihost.h>
```

定位到文件中的绝对位置（Absolute Position）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fd` | semihost_open 返回的句柄（Handle）。 |
| `offset` | 相对于文件开头的偏移量（Offset），单位为字节。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-errno` | 失败时返回负错误码。 |

<a id="ga6c340fadaa86cddee2817e96caa00edf"></a>

### `semihost_write()`

```c
long semihost_write ( long fd, const void * buf, long len )
```

```c
#include <zephyr/arch/common/semihost.h>
```

将缓冲区内容（Buffer Contents）写入文件。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fd` | semihost_open 返回的句柄（Handle）。 |
| `buf` | 提供待写入数据的缓冲区。 |
| `len` | 要写入的字节数。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-errno` | 失败时返回负错误码。 |


## 16.4\_原页交叉引用（Cross References）

- [zephyr/arch/common/semihost.h](../api_file_system_power_reference/P036_zephyr__arch__common__semihost.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggadf61e00be557b7cb4457f7ea6f8da86da32cc33a795888c73c3d1624f288fed46"></a>
<a id="ggadf61e00be557b7cb4457f7ea6f8da86dad92d3362fc63d17b0f6c74f1c796ae53"></a>
<a id="ggadf61e00be557b7cb4457f7ea6f8da86dac1da151904c09d05b4548f1c28bb72ad"></a>
<a id="ggadf61e00be557b7cb4457f7ea6f8da86da0e589cd7b9f53eeb303a419487e40a02"></a>
<a id="ggadf61e00be557b7cb4457f7ea6f8da86daa800fb6638cb45941c81d41275779cac"></a>
<a id="ggadf61e00be557b7cb4457f7ea6f8da86daf6894316046e0cd2c07c7f55effddc8d"></a>
<a id="ggadf61e00be557b7cb4457f7ea6f8da86dad030bc2e7a63682116efb84011d40629"></a>
<a id="ggadf61e00be557b7cb4457f7ea6f8da86dad0ed15a780a1d9bd8583e01468f4abeb"></a>
<a id="ggadf61e00be557b7cb4457f7ea6f8da86da88b03906fd14fe40d86c841de05539ce"></a>
<a id="ggadf61e00be557b7cb4457f7ea6f8da86da3e584069d9d8cd126bd409df9f99d627"></a>
<a id="ggadf61e00be557b7cb4457f7ea6f8da86da6edbfcd0d356552569ae1cfcd78203a7"></a>
<a id="ggadf61e00be557b7cb4457f7ea6f8da86da6d4f5801467a25613abf1d38386060ff"></a>
<a id="ggadf61e00be557b7cb4457f7ea6f8da86dae3a468fafe97de23a4d0b125a438e8f6"></a>
<a id="ggadf61e00be557b7cb4457f7ea6f8da86dac17ed558ffacf4612c234db887743ca0"></a>
<a id="ggadf61e00be557b7cb4457f7ea6f8da86da3db5621dbcb6c8a2a074cc69144f8367"></a>
<a id="ggadf61e00be557b7cb4457f7ea6f8da86da59856dd67e4079773f9ada8c3cb5ba26"></a>
<a id="ggadf61e00be557b7cb4457f7ea6f8da86daffd89aae5102d56b677522ab2b66c438"></a>
<a id="ggadf61e00be557b7cb4457f7ea6f8da86dad8f17a37155fdb3c4e29c4c3ba2b4a4f"></a>
<a id="ggadf61e00be557b7cb4457f7ea6f8da86daba47d649a03b0ed2bfc6fb8d3020563f"></a>
<a id="ggadf61e00be557b7cb4457f7ea6f8da86da8963d2934a740ae5fd04ca84fd48f57f"></a>
<a id="ggadf61e00be557b7cb4457f7ea6f8da86da7e0050f763d6c115c2b24064b4beb6ea"></a>
<a id="ggadf61e00be557b7cb4457f7ea6f8da86da78d21e53db4f44f375aefd25009dd71a"></a>
<a id="gga425c53a045590978b0b3235d545780f7ab7c309dc69b408ade19bff098818471b"></a>
<a id="gga425c53a045590978b0b3235d545780f7a1bc8673a95497f17cdebafdc1fe5cdde"></a>
<a id="gga425c53a045590978b0b3235d545780f7a036c2739eb8b2bd43042367d66d644c9"></a>
<a id="gga425c53a045590978b0b3235d545780f7a99975dc411c6b501ef2f34f31a8aaa53"></a>
<a id="gga425c53a045590978b0b3235d545780f7a14a3bbe45567c38892ede4f120c888fc"></a>
<a id="gga425c53a045590978b0b3235d545780f7a41befb06ac2fcce18e7a085b9e8911bc"></a>
<a id="gga425c53a045590978b0b3235d545780f7abf3d7d2b6e9a99bcacbff1c50bb1d262"></a>
<a id="gga425c53a045590978b0b3235d545780f7a172b9e36d6fad788501e53116ab84244"></a>
<a id="gga425c53a045590978b0b3235d545780f7a17270a085663f59c6104b68bf35b7c34"></a>
<a id="gga425c53a045590978b0b3235d545780f7a128ed24bf3519c3fa84e3fc996988708"></a>
<a id="gga425c53a045590978b0b3235d545780f7a300dde91715638debca2cbd6a61e508f"></a>
<a id="gga425c53a045590978b0b3235d545780f7a5357da3dddbeb511d312291cbab9c466"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P015_网络抓包（Network packet capture）.md) · [返回大纲](大纲.md) · [下一章](P017_用户模式 API（User Mode APIs）.md)
