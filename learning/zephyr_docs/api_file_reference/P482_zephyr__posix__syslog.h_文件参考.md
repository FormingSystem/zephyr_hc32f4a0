---
id: learning.zephyr-docs.api-file-reference.page-482
title: zephyr__posix__syslog.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/syslog_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第482章\_zephyr\_\_posix\_\_syslog.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/syslog_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <stdarg.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 482.1\_宏定义（Macros）

<a id="r_a7b264572ee428bb73548226ba5bbe88a"></a>

```c
#define LOG_PID 1
```

相关声明：[LOG_PID](#a7b264572ee428bb73548226ba5bbe88a)。

<a id="r_aeccd30c76c44f407cd9d5441318b6aba"></a>

```c
#define LOG_CONS 2
```

相关声明：[LOG_CONS](#aeccd30c76c44f407cd9d5441318b6aba)。

<a id="r_a446430791b21a34e7308046826759d25"></a>

```c
#define LOG_NDELAY 4
```

相关声明：[LOG_NDELAY](#a446430791b21a34e7308046826759d25)。

<a id="r_aed1240a0e0d7f574a09ea915d4e1af85"></a>

```c
#define LOG_ODELAY 8
```

相关声明：[LOG_ODELAY](#aed1240a0e0d7f574a09ea915d4e1af85)。

<a id="r_a9dff0ca45769bfa276ce3f0080acc397"></a>

```c
#define LOG_NOWAIT 16
```

相关声明：[LOG_NOWAIT](#a9dff0ca45769bfa276ce3f0080acc397)。

<a id="r_a542160b84335cc94dfb75604fd40d341"></a>

```c
#define LOG_PERROR 32
```

相关声明：[LOG_PERROR](#a542160b84335cc94dfb75604fd40d341)。

<a id="r_a3782c789d7d0eeab593758f80e436da4"></a>

```c
#define LOG_KERN 0
```

相关声明：[LOG_KERN](#a3782c789d7d0eeab593758f80e436da4)。

<a id="r_ac8b1ae5666bff93a5db0bb45f99f5832"></a>

```c
#define LOG_USER 1
```

相关声明：[LOG_USER](#ac8b1ae5666bff93a5db0bb45f99f5832)。

<a id="r_a135a6127cf9b508b4361594e842eefc0"></a>

```c
#define LOG_MAIL 2
```

相关声明：[LOG_MAIL](#a135a6127cf9b508b4361594e842eefc0)。

<a id="r_aeae7c4754f60a7931ce0141bac37e798"></a>

```c
#define LOG_NEWS 3
```

相关声明：[LOG_NEWS](#aeae7c4754f60a7931ce0141bac37e798)。

<a id="r_ab0db5f3df16ec19a5897b852930bca54"></a>

```c
#define LOG_UUCP 4
```

相关声明：[LOG_UUCP](#ab0db5f3df16ec19a5897b852930bca54)。

<a id="r_a9961fc94ec213d970dc7c8d9608e1d42"></a>

```c
#define LOG_DAEMON 5
```

相关声明：[LOG_DAEMON](#a9961fc94ec213d970dc7c8d9608e1d42)。

<a id="r_a22b8a93c6a27426f9a8ad4ce9407e86d"></a>

```c
#define LOG_AUTH 6
```

相关声明：[LOG_AUTH](#a22b8a93c6a27426f9a8ad4ce9407e86d)。

<a id="r_a285963d2ea1986d2f31ae7c6c0b5dc4e"></a>

```c
#define LOG_CRON 7
```

相关声明：[LOG_CRON](#a285963d2ea1986d2f31ae7c6c0b5dc4e)。

<a id="r_a3c6927ac15f5eaa92ee6d79b2837b68e"></a>

```c
#define LOG_LPR 8
```

相关声明：[LOG_LPR](#a3c6927ac15f5eaa92ee6d79b2837b68e)。

<a id="r_a25eab08bcadd790ad09db8ab1391d7b4"></a>

```c
#define LOG_LOCAL0 9
```

相关声明：[LOG_LOCAL0](#a25eab08bcadd790ad09db8ab1391d7b4)。

<a id="r_ae2702880c720b92d9b133a394536fc55"></a>

```c
#define LOG_LOCAL1 10
```

相关声明：[LOG_LOCAL1](#ae2702880c720b92d9b133a394536fc55)。

<a id="r_a3bba702c131c9a343f43cefe9dc54806"></a>

```c
#define LOG_LOCAL2 11
```

相关声明：[LOG_LOCAL2](#a3bba702c131c9a343f43cefe9dc54806)。

<a id="r_adc43741bf59af027c44c46f6c4692592"></a>

```c
#define LOG_LOCAL3 12
```

相关声明：[LOG_LOCAL3](#adc43741bf59af027c44c46f6c4692592)。

<a id="r_a7c96c20eb0501c681dea19b78c36e475"></a>

```c
#define LOG_LOCAL4 13
```

相关声明：[LOG_LOCAL4](#a7c96c20eb0501c681dea19b78c36e475)。

<a id="r_ac19bfe79880b74eb63d406c218c89350"></a>

```c
#define LOG_LOCAL5 14
```

相关声明：[LOG_LOCAL5](#ac19bfe79880b74eb63d406c218c89350)。

<a id="r_a71d48fd009db4d4e57019903d372347a"></a>

```c
#define LOG_LOCAL6 15
```

相关声明：[LOG_LOCAL6](#a71d48fd009db4d4e57019903d372347a)。

<a id="r_aea1efd5b3880503ca94c623d0517e497"></a>

```c
#define LOG_LOCAL7 16
```

相关声明：[LOG_LOCAL7](#aea1efd5b3880503ca94c623d0517e497)。

<a id="r_a5c6e8b60c2512dfc0e0224d25a61cb2c"></a>

```c
#define LOG_EMERG 0
```

相关声明：[LOG_EMERG](#a5c6e8b60c2512dfc0e0224d25a61cb2c)。

<a id="r_a12b2a3bb9e3adfeb35b4e5514e7d9043"></a>

```c
#define LOG_ALERT 1
```

相关声明：[LOG_ALERT](#a12b2a3bb9e3adfeb35b4e5514e7d9043)。

<a id="r_aaa731313f5c63e855fefb5f6519c3283"></a>

```c
#define LOG_CRIT 2
```

相关声明：[LOG_CRIT](#aaa731313f5c63e855fefb5f6519c3283)。

<a id="r_a96fad55b3f5adf08c39e4c877cf185e3"></a>

```c
#define LOG_ERR 3
```

相关声明：[LOG_ERR](#a96fad55b3f5adf08c39e4c877cf185e3)。

<a id="r_adf4476a6a4ea6c74231c826e899d7189"></a>

```c
#define LOG_WARNING 4
```

相关声明：[LOG_WARNING](#adf4476a6a4ea6c74231c826e899d7189)。

<a id="r_ad89ee324d180cdcd7defcc709ff9ca42"></a>

```c
#define LOG_NOTICE 5
```

相关声明：[LOG_NOTICE](#ad89ee324d180cdcd7defcc709ff9ca42)。

<a id="r_aeb4f36db01bd128c7afeac5889dac311"></a>

```c
#define LOG_INFO 6
```

相关声明：[LOG_INFO](#aeb4f36db01bd128c7afeac5889dac311)。

<a id="r_a6ff63e8955665c4a58b1598f2b07c51a"></a>

```c
#define LOG_DEBUG 7
```

相关声明：[LOG_DEBUG](#a6ff63e8955665c4a58b1598f2b07c51a)。

<a id="r_a8e1c2d42597b3dd0eeda52ed444b1d4a"></a>

```c
#define LOG_MASK(mask)
```

相关声明：[LOG_MASK](#a8e1c2d42597b3dd0eeda52ed444b1d4a)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 482.2\_函数（Functions）

<a id="r_ae1e4e53707d8c3fbc36bbc523fbbcda3"></a>

```c
void closelog (void)
```

相关声明：[closelog](#ae1e4e53707d8c3fbc36bbc523fbbcda3)。

<a id="r_a0dc773e0b62cd9b9e42addd25592a50e"></a>

```c
void openlog (const char *ident, int logopt, int facility)
```

相关声明：[openlog](#a0dc773e0b62cd9b9e42addd25592a50e)。

<a id="r_aca20103a73ae93ed63b2a1a94b93f53b"></a>

```c
int setlogmask (int maskpri)
```

相关声明：[setlogmask](#aca20103a73ae93ed63b2a1a94b93f53b)。

<a id="r_a7b3a37aea8e8f9fe12fe0340eaccb838"></a>

```c
void syslog (int priority, const char *message,...)
```

相关声明：[syslog](#a7b3a37aea8e8f9fe12fe0340eaccb838)。

<a id="r_a9722b4c868bed8d78283a4202a6f21d6"></a>

```c
void vsyslog (int priority, const char *format, va_list ap)
```

相关声明：[vsyslog](#a9722b4c868bed8d78283a4202a6f21d6)。

## 482.3\_详细说明（Detailed Documentation）

<a id="a12b2a3bb9e3adfeb35b4e5514e7d9043"></a>

### `LOG_ALERT`

```c
#define LOG_ALERT 1
```

<a id="a22b8a93c6a27426f9a8ad4ce9407e86d"></a>

### `LOG_AUTH`

```c
#define LOG_AUTH 6
```

<a id="aeccd30c76c44f407cd9d5441318b6aba"></a>

### `LOG_CONS`

```c
#define LOG_CONS 2
```

<a id="aaa731313f5c63e855fefb5f6519c3283"></a>

### `LOG_CRIT`

```c
#define LOG_CRIT 2
```

<a id="a285963d2ea1986d2f31ae7c6c0b5dc4e"></a>

### `LOG_CRON`

```c
#define LOG_CRON 7
```

<a id="a9961fc94ec213d970dc7c8d9608e1d42"></a>

### `LOG_DAEMON`

```c
#define LOG_DAEMON 5
```

<a id="a6ff63e8955665c4a58b1598f2b07c51a"></a>

### `LOG_DEBUG`

```c
#define LOG_DEBUG 7
```

<a id="a5c6e8b60c2512dfc0e0224d25a61cb2c"></a>

### `LOG_EMERG`

```c
#define LOG_EMERG 0
```

<a id="a96fad55b3f5adf08c39e4c877cf185e3"></a>

### `LOG_ERR`

```c
#define LOG_ERR 3
```

<a id="aeb4f36db01bd128c7afeac5889dac311"></a>

### `LOG_INFO`

```c
#define LOG_INFO 6
```

<a id="a3782c789d7d0eeab593758f80e436da4"></a>

### `LOG_KERN`

```c
#define LOG_KERN 0
```

<a id="a25eab08bcadd790ad09db8ab1391d7b4"></a>

### `LOG_LOCAL0`

```c
#define LOG_LOCAL0 9
```

<a id="ae2702880c720b92d9b133a394536fc55"></a>

### `LOG_LOCAL1`

```c
#define LOG_LOCAL1 10
```

<a id="a3bba702c131c9a343f43cefe9dc54806"></a>

### `LOG_LOCAL2`

```c
#define LOG_LOCAL2 11
```

<a id="adc43741bf59af027c44c46f6c4692592"></a>

### `LOG_LOCAL3`

```c
#define LOG_LOCAL3 12
```

<a id="a7c96c20eb0501c681dea19b78c36e475"></a>

### `LOG_LOCAL4`

```c
#define LOG_LOCAL4 13
```

<a id="ac19bfe79880b74eb63d406c218c89350"></a>

### `LOG_LOCAL5`

```c
#define LOG_LOCAL5 14
```

<a id="a71d48fd009db4d4e57019903d372347a"></a>

### `LOG_LOCAL6`

```c
#define LOG_LOCAL6 15
```

<a id="aea1efd5b3880503ca94c623d0517e497"></a>

### `LOG_LOCAL7`

```c
#define LOG_LOCAL7 16
```

<a id="a3c6927ac15f5eaa92ee6d79b2837b68e"></a>

### `LOG_LPR`

```c
#define LOG_LPR 8
```

<a id="a135a6127cf9b508b4361594e842eefc0"></a>

### `LOG_MAIL`

```c
#define LOG_MAIL 2
```

<a id="a8e1c2d42597b3dd0eeda52ed444b1d4a"></a>

### `LOG_MASK`

```c
#define LOG_MASK ( mask)
```

展开值（Value）：

```c
((mask) & BIT_MASK(LOG_DEBUG + 1))
```

<a id="a446430791b21a34e7308046826759d25"></a>

### `LOG_NDELAY`

```c
#define LOG_NDELAY 4
```

<a id="aeae7c4754f60a7931ce0141bac37e798"></a>

### `LOG_NEWS`

```c
#define LOG_NEWS 3
```

<a id="ad89ee324d180cdcd7defcc709ff9ca42"></a>

### `LOG_NOTICE`

```c
#define LOG_NOTICE 5
```

<a id="a9dff0ca45769bfa276ce3f0080acc397"></a>

### `LOG_NOWAIT`

```c
#define LOG_NOWAIT 16
```

<a id="aed1240a0e0d7f574a09ea915d4e1af85"></a>

### `LOG_ODELAY`

```c
#define LOG_ODELAY 8
```

<a id="a542160b84335cc94dfb75604fd40d341"></a>

### `LOG_PERROR`

```c
#define LOG_PERROR 32
```

<a id="a7b264572ee428bb73548226ba5bbe88a"></a>

### `LOG_PID`

```c
#define LOG_PID 1
```

<a id="ac8b1ae5666bff93a5db0bb45f99f5832"></a>

### `LOG_USER`

```c
#define LOG_USER 1
```

<a id="ab0db5f3df16ec19a5897b852930bca54"></a>

### `LOG_UUCP`

```c
#define LOG_UUCP 4
```

<a id="adf4476a6a4ea6c74231c826e899d7189"></a>

### `LOG_WARNING`

```c
#define LOG_WARNING 4
```

<a id="ae1e4e53707d8c3fbc36bbc523fbbcda3"></a>

### `closelog()`

```c
void closelog ( void )
```

<a id="a0dc773e0b62cd9b9e42addd25592a50e"></a>

### `openlog()`

```c
void openlog ( const char * ident, int logopt, int facility )
```

<a id="aca20103a73ae93ed63b2a1a94b93f53b"></a>

### `setlogmask()`

```c
int setlogmask ( int maskpri)
```

<a id="a7b3a37aea8e8f9fe12fe0340eaccb838"></a>

### `syslog()`

```c
void syslog ( int priority, const char * message, ... )
```

<a id="a9722b4c868bed8d78283a4202a6f21d6"></a>

### `vsyslog()`

```c
void vsyslog ( int priority, const char * format, va_list ap )
```


## 482.4\_原页交叉引用（Cross References）

- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/syslog_8h_source.html)
- [BIT_MASK](../util_reference/P001_通用工具公共接口.md#ga3c12c6d36ad0aa481a3436923d21f4f8)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__sys-util_html_ga3c12c6d36ad0aa481a3436923d21f4f8"></a>
<a id="asyslog_8h_html_a6ff63e8955665c4a58b1598f2b07c51a"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P481_zephyr__posix__sys__sysconf.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P483_zephyr__posix__netinet__tcp.h_文件参考.md)
