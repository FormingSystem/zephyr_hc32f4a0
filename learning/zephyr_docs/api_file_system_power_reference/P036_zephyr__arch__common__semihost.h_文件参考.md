---
id: learning.zephyr-docs.api-file-system-power-reference.page-36
title: zephyr__arch__common__semihost.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/semihost_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第36章\_zephyr\_\_arch\_\_common\_\_semihost.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/semihost_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

基于ARM定义的半主机机制（Semihosting）公共API。

查看此文件的源码。

<a id="details"></a>

基于ARM定义的半主机机制（Semihosting）公共API。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 36.1\_枚举（Enumerations）

<a id="r_gadf61e00be557b7cb4457f7ea6f8da86d"></a>

```c
enum semihost_instr { SEMIHOST_OPEN = 0x01 , SEMIHOST_ISTTY = 0x09 , SEMIHOST_WRITE = 0x05 , SEMIHOST_READ = 0x06 , SEMIHOST_CLOSE = 0x02 , SEMIHOST_FLEN = 0x0C , SEMIHOST_SEEK = 0x0A , SEMIHOST_TMPNAM = 0x0D , SEMIHOST_REMOVE = 0x0E , SEMIHOST_RENAME = 0x0F , SEMIHOST_WRITEC = 0x03 , SEMIHOST_WRITE0 = 0x04 , SEMIHOST_READC = 0x07 , SEMIHOST_CLOCK = 0x10 , SEMIHOST_ELAPSED = 0x30 , SEMIHOST_TICKFREQ = 0x31 , SEMIHOST_TIME = 0x11 , SEMIHOST_ERRNO = 0x13 , SEMIHOST_GET_CMDLINE = 0x15 , SEMIHOST_HEAPINFO = 0x16 , SEMIHOST_ISERROR = 0x08 , SEMIHOST_SYSTEM = 0x12 }
```

相关声明：[semihost_instr](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#gadf61e00be557b7cb4457f7ea6f8da86d)、[SEMIHOST_OPEN](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#ggadf61e00be557b7cb4457f7ea6f8da86da32cc33a795888c73c3d1624f288fed46)、[SEMIHOST_ISTTY](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#ggadf61e00be557b7cb4457f7ea6f8da86dad92d3362fc63d17b0f6c74f1c796ae53)、[SEMIHOST_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#ggadf61e00be557b7cb4457f7ea6f8da86dac1da151904c09d05b4548f1c28bb72ad)、[SEMIHOST_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#ggadf61e00be557b7cb4457f7ea6f8da86da0e589cd7b9f53eeb303a419487e40a02)、[SEMIHOST_CLOSE](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#ggadf61e00be557b7cb4457f7ea6f8da86daa800fb6638cb45941c81d41275779cac)、[SEMIHOST_FLEN](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#ggadf61e00be557b7cb4457f7ea6f8da86daf6894316046e0cd2c07c7f55effddc8d)、[SEMIHOST_SEEK](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#ggadf61e00be557b7cb4457f7ea6f8da86dad030bc2e7a63682116efb84011d40629)、[SEMIHOST_TMPNAM](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#ggadf61e00be557b7cb4457f7ea6f8da86dad0ed15a780a1d9bd8583e01468f4abeb)、[SEMIHOST_REMOVE](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#ggadf61e00be557b7cb4457f7ea6f8da86da88b03906fd14fe40d86c841de05539ce)、[SEMIHOST_RENAME](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#ggadf61e00be557b7cb4457f7ea6f8da86da3e584069d9d8cd126bd409df9f99d627)、[SEMIHOST_WRITEC](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#ggadf61e00be557b7cb4457f7ea6f8da86da6edbfcd0d356552569ae1cfcd78203a7)、[SEMIHOST_WRITE0](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#ggadf61e00be557b7cb4457f7ea6f8da86da6d4f5801467a25613abf1d38386060ff)、[SEMIHOST_READC](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#ggadf61e00be557b7cb4457f7ea6f8da86dae3a468fafe97de23a4d0b125a438e8f6)、[SEMIHOST_CLOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#ggadf61e00be557b7cb4457f7ea6f8da86dac17ed558ffacf4612c234db887743ca0)、[SEMIHOST_ELAPSED](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#ggadf61e00be557b7cb4457f7ea6f8da86da3db5621dbcb6c8a2a074cc69144f8367)、[SEMIHOST_TICKFREQ](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#ggadf61e00be557b7cb4457f7ea6f8da86da59856dd67e4079773f9ada8c3cb5ba26)、[SEMIHOST_TIME](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#ggadf61e00be557b7cb4457f7ea6f8da86daffd89aae5102d56b677522ab2b66c438)、[SEMIHOST_ERRNO](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#ggadf61e00be557b7cb4457f7ea6f8da86dad8f17a37155fdb3c4e29c4c3ba2b4a4f)、[SEMIHOST_GET_CMDLINE](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#ggadf61e00be557b7cb4457f7ea6f8da86daba47d649a03b0ed2bfc6fb8d3020563f)、[SEMIHOST_HEAPINFO](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#ggadf61e00be557b7cb4457f7ea6f8da86da8963d2934a740ae5fd04ca84fd48f57f)、[SEMIHOST_ISERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#ggadf61e00be557b7cb4457f7ea6f8da86da7e0050f763d6c115c2b24064b4beb6ea)、[SEMIHOST_SYSTEM](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#ggadf61e00be557b7cb4457f7ea6f8da86da78d21e53db4f44f375aefd25009dd71a)。

半主机指令（Semihosting Instructions）。

<a id="r_ga425c53a045590978b0b3235d545780f7"></a>

```c
enum semihost_open_mode { SEMIHOST_OPEN_R = 0 , SEMIHOST_OPEN_RB = 1 , SEMIHOST_OPEN_R_PLUS = 2 , SEMIHOST_OPEN_RB_PLUS = 3 , SEMIHOST_OPEN_W = 4 , SEMIHOST_OPEN_WB = 5 , SEMIHOST_OPEN_W_PLUS = 6 , SEMIHOST_OPEN_WB_PLUS = 7 , SEMIHOST_OPEN_A = 8 , SEMIHOST_OPEN_AB = 9 , SEMIHOST_OPEN_A_PLUS = 10 , SEMIHOST_OPEN_AB_PLUS = 11 }
```

相关声明：[semihost_open_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#ga425c53a045590978b0b3235d545780f7)、[SEMIHOST_OPEN_R](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#gga425c53a045590978b0b3235d545780f7ab7c309dc69b408ade19bff098818471b)、[SEMIHOST_OPEN_RB](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#gga425c53a045590978b0b3235d545780f7a1bc8673a95497f17cdebafdc1fe5cdde)、[SEMIHOST_OPEN_R_PLUS](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#gga425c53a045590978b0b3235d545780f7a036c2739eb8b2bd43042367d66d644c9)、[SEMIHOST_OPEN_RB_PLUS](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#gga425c53a045590978b0b3235d545780f7a99975dc411c6b501ef2f34f31a8aaa53)、[SEMIHOST_OPEN_W](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#gga425c53a045590978b0b3235d545780f7a14a3bbe45567c38892ede4f120c888fc)、[SEMIHOST_OPEN_WB](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#gga425c53a045590978b0b3235d545780f7a41befb06ac2fcce18e7a085b9e8911bc)、[SEMIHOST_OPEN_W_PLUS](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#gga425c53a045590978b0b3235d545780f7abf3d7d2b6e9a99bcacbff1c50bb1d262)、[SEMIHOST_OPEN_WB_PLUS](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#gga425c53a045590978b0b3235d545780f7a172b9e36d6fad788501e53116ab84244)、[SEMIHOST_OPEN_A](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#gga425c53a045590978b0b3235d545780f7a17270a085663f59c6104b68bf35b7c34)、[SEMIHOST_OPEN_AB](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#gga425c53a045590978b0b3235d545780f7a128ed24bf3519c3fa84e3fc996988708)、[SEMIHOST_OPEN_A_PLUS](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#gga425c53a045590978b0b3235d545780f7a300dde91715638debca2cbd6a61e508f)、[SEMIHOST_OPEN_AB_PLUS](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#gga425c53a045590978b0b3235d545780f7a5357da3dddbeb511d312291cbab9c466)。

打开文件使用的模式（File Open Modes）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 36.2\_函数（Functions）

<a id="r_gab8d683d2011f6683956c47a4b129faf4"></a>

```c
long semihost_exec (enum semihost_instr instr, void *args)
```

相关声明：[semihost_exec](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#gab8d683d2011f6683956c47a4b129faf4)、[semihost_instr](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#gadf61e00be557b7cb4457f7ea6f8da86d)。

手动执行半主机指令（Semihosting Instruction）。

<a id="r_ga4eb7ceb5ceaaded14c3dc129b7fca07b"></a>

```c
char semihost_poll_in (void)
```

相关声明：[semihost_poll_in](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#ga4eb7ceb5ceaaded14c3dc129b7fca07b)。

从控制台（Console）读取一个字节。

<a id="r_ga4026806d0ea1f6d754851ef7b9f1c58c"></a>

```c
void semihost_poll_out (char c)
```

相关声明：[semihost_poll_out](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#ga4026806d0ea1f6d754851ef7b9f1c58c)。

向控制台（Console）写入一个字节。

<a id="r_ga497b911ba4e6b40e4e5808fa9484f5a4"></a>

```c
long semihost_open (const char *path, long mode)
```

相关声明：[semihost_open](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#ga497b911ba4e6b40e4e5808fa9484f5a4)。

在主机系统（Host System）上打开文件。

<a id="r_gad8e5d671a2316901eefaf86cac43ac43"></a>

```c
long semihost_close (long fd)
```

相关声明：[semihost_close](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#gad8e5d671a2316901eefaf86cac43ac43)。

关闭文件（File）。

<a id="r_gae7476b25d69979d488e1bbd3521d70e0"></a>

```c
long semihost_flen (long fd)
```

相关声明：[semihost_flen](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#gae7476b25d69979d488e1bbd3521d70e0)。

查询文件大小（File Size）。

<a id="r_ga99f88405f4bdc9f43ab2d59b3526ebbc"></a>

```c
long semihost_seek (long fd, long offset)
```

相关声明：[semihost_seek](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#ga99f88405f4bdc9f43ab2d59b3526ebbc)。

定位到文件中的绝对位置（Absolute Position）。

<a id="r_gaf0d429779cd2b3a06c29f93f8641e9af"></a>

```c
long semihost_read (long fd, void *buf, long len)
```

相关声明：[semihost_read](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#gaf0d429779cd2b3a06c29f93f8641e9af)。

将文件内容（File Contents）读入缓冲区（Buffer）。

<a id="r_ga6c340fadaa86cddee2817e96caa00edf"></a>

```c
long semihost_write (long fd, const void *buf, long len)
```

相关声明：[semihost_write](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#ga6c340fadaa86cddee2817e96caa00edf)。

将缓冲区内容（Buffer Contents）写入文件。


## 36.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_system_reference/P039_semihost.h_源码浏览.md)
- [semihost_instr](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#gadf61e00be557b7cb4457f7ea6f8da86d)
- [SEMIHOST_OPEN](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#ggadf61e00be557b7cb4457f7ea6f8da86da32cc33a795888c73c3d1624f288fed46)
- [SEMIHOST_ISTTY](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#ggadf61e00be557b7cb4457f7ea6f8da86dad92d3362fc63d17b0f6c74f1c796ae53)
- [SEMIHOST_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#ggadf61e00be557b7cb4457f7ea6f8da86dac1da151904c09d05b4548f1c28bb72ad)
- [SEMIHOST_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#ggadf61e00be557b7cb4457f7ea6f8da86da0e589cd7b9f53eeb303a419487e40a02)
- [SEMIHOST_CLOSE](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#ggadf61e00be557b7cb4457f7ea6f8da86daa800fb6638cb45941c81d41275779cac)
- [SEMIHOST_FLEN](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#ggadf61e00be557b7cb4457f7ea6f8da86daf6894316046e0cd2c07c7f55effddc8d)
- [SEMIHOST_SEEK](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#ggadf61e00be557b7cb4457f7ea6f8da86dad030bc2e7a63682116efb84011d40629)
- [SEMIHOST_TMPNAM](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#ggadf61e00be557b7cb4457f7ea6f8da86dad0ed15a780a1d9bd8583e01468f4abeb)
- [SEMIHOST_REMOVE](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#ggadf61e00be557b7cb4457f7ea6f8da86da88b03906fd14fe40d86c841de05539ce)
- [SEMIHOST_RENAME](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#ggadf61e00be557b7cb4457f7ea6f8da86da3e584069d9d8cd126bd409df9f99d627)
- [SEMIHOST_WRITEC](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#ggadf61e00be557b7cb4457f7ea6f8da86da6edbfcd0d356552569ae1cfcd78203a7)
- [SEMIHOST_WRITE0](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#ggadf61e00be557b7cb4457f7ea6f8da86da6d4f5801467a25613abf1d38386060ff)
- [SEMIHOST_READC](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#ggadf61e00be557b7cb4457f7ea6f8da86dae3a468fafe97de23a4d0b125a438e8f6)
- [SEMIHOST_CLOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#ggadf61e00be557b7cb4457f7ea6f8da86dac17ed558ffacf4612c234db887743ca0)
- [SEMIHOST_ELAPSED](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#ggadf61e00be557b7cb4457f7ea6f8da86da3db5621dbcb6c8a2a074cc69144f8367)
- [SEMIHOST_TICKFREQ](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#ggadf61e00be557b7cb4457f7ea6f8da86da59856dd67e4079773f9ada8c3cb5ba26)
- [SEMIHOST_TIME](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#ggadf61e00be557b7cb4457f7ea6f8da86daffd89aae5102d56b677522ab2b66c438)
- [SEMIHOST_ERRNO](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#ggadf61e00be557b7cb4457f7ea6f8da86dad8f17a37155fdb3c4e29c4c3ba2b4a4f)
- [SEMIHOST_GET_CMDLINE](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#ggadf61e00be557b7cb4457f7ea6f8da86daba47d649a03b0ed2bfc6fb8d3020563f)
- [SEMIHOST_HEAPINFO](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#ggadf61e00be557b7cb4457f7ea6f8da86da8963d2934a740ae5fd04ca84fd48f57f)
- [SEMIHOST_ISERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#ggadf61e00be557b7cb4457f7ea6f8da86da7e0050f763d6c115c2b24064b4beb6ea)
- [SEMIHOST_SYSTEM](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#ggadf61e00be557b7cb4457f7ea6f8da86da78d21e53db4f44f375aefd25009dd71a)
- [semihost_open_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#ga425c53a045590978b0b3235d545780f7)
- [SEMIHOST_OPEN_R](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#gga425c53a045590978b0b3235d545780f7ab7c309dc69b408ade19bff098818471b)
- [SEMIHOST_OPEN_RB](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#gga425c53a045590978b0b3235d545780f7a1bc8673a95497f17cdebafdc1fe5cdde)
- [SEMIHOST_OPEN_R_PLUS](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#gga425c53a045590978b0b3235d545780f7a036c2739eb8b2bd43042367d66d644c9)
- [SEMIHOST_OPEN_RB_PLUS](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#gga425c53a045590978b0b3235d545780f7a99975dc411c6b501ef2f34f31a8aaa53)
- [SEMIHOST_OPEN_W](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#gga425c53a045590978b0b3235d545780f7a14a3bbe45567c38892ede4f120c888fc)
- [SEMIHOST_OPEN_WB](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#gga425c53a045590978b0b3235d545780f7a41befb06ac2fcce18e7a085b9e8911bc)
- [SEMIHOST_OPEN_W_PLUS](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#gga425c53a045590978b0b3235d545780f7abf3d7d2b6e9a99bcacbff1c50bb1d262)
- [SEMIHOST_OPEN_WB_PLUS](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#gga425c53a045590978b0b3235d545780f7a172b9e36d6fad788501e53116ab84244)
- [SEMIHOST_OPEN_A](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#gga425c53a045590978b0b3235d545780f7a17270a085663f59c6104b68bf35b7c34)
- [SEMIHOST_OPEN_AB](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#gga425c53a045590978b0b3235d545780f7a128ed24bf3519c3fa84e3fc996988708)
- [SEMIHOST_OPEN_A_PLUS](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#gga425c53a045590978b0b3235d545780f7a300dde91715638debca2cbd6a61e508f)
- [SEMIHOST_OPEN_AB_PLUS](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#gga425c53a045590978b0b3235d545780f7a5357da3dddbeb511d312291cbab9c466)
- [semihost_exec](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#gab8d683d2011f6683956c47a4b129faf4)
- [semihost_poll_in](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#ga4eb7ceb5ceaaded14c3dc129b7fca07b)
- [semihost_poll_out](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#ga4026806d0ea1f6d754851ef7b9f1c58c)
- [semihost_open](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#ga497b911ba4e6b40e4e5808fa9484f5a4)
- [semihost_close](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#gad8e5d671a2316901eefaf86cac43ac43)
- [semihost_flen](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#gae7476b25d69979d488e1bbd3521d70e0)
- [semihost_seek](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#ga99f88405f4bdc9f43ab2d59b3526ebbc)
- [semihost_read](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#gaf0d429779cd2b3a06c29f93f8641e9af)
- [semihost_write](https://docs.zephyrproject.org/latest/doxygen/html/group__semihost.html#ga6c340fadaa86cddee2817e96caa00edf)

<a id="header-details"></a>

---

[上一章](P035_zephyr__drivers__interrupt_controller__riscv_plic.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P037_zephyr__drivers__sensor__mcux_acmp.h_文件参考.md)
