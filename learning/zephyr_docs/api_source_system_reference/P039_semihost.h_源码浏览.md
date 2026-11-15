---
id: learning.zephyr-docs.api-source-system-reference.page-39
title: semihost.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/semihost_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第39章\_semihost.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/semihost_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/semihost_8h.html)。

## 39.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="foldopen00027"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00033"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00077"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="foldopen00091"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="agroup__semihost_html_ga4026806d0ea1f6d754851ef7b9f1c58c"></a>
<a id="agroup__semihost_html_ga425c53a045590978b0b3235d545780f7"></a>
<a id="agroup__semihost_html_ga497b911ba4e6b40e4e5808fa9484f5a4"></a>
<a id="agroup__semihost_html_ga4eb7ceb5ceaaded14c3dc129b7fca07b"></a>
<a id="agroup__semihost_html_ga6c340fadaa86cddee2817e96caa00edf"></a>
<a id="agroup__semihost_html_ga99f88405f4bdc9f43ab2d59b3526ebbc"></a>
<a id="agroup__semihost_html_gab8d683d2011f6683956c47a4b129faf4"></a>
<a id="agroup__semihost_html_gad8e5d671a2316901eefaf86cac43ac43"></a>
<a id="agroup__semihost_html_gadf61e00be557b7cb4457f7ea6f8da86d"></a>
<a id="agroup__semihost_html_gae7476b25d69979d488e1bbd3521d70e0"></a>
<a id="agroup__semihost_html_gaf0d429779cd2b3a06c29f93f8641e9af"></a>
<a id="agroup__semihost_html_gga425c53a045590978b0b3235d545780f7a036c2739eb8b2bd43042367d66d644c9"></a>
<a id="agroup__semihost_html_gga425c53a045590978b0b3235d545780f7a128ed24bf3519c3fa84e3fc996988708"></a>
<a id="agroup__semihost_html_gga425c53a045590978b0b3235d545780f7a14a3bbe45567c38892ede4f120c888fc"></a>
<a id="agroup__semihost_html_gga425c53a045590978b0b3235d545780f7a17270a085663f59c6104b68bf35b7c34"></a>
<a id="agroup__semihost_html_gga425c53a045590978b0b3235d545780f7a172b9e36d6fad788501e53116ab84244"></a>
<a id="agroup__semihost_html_gga425c53a045590978b0b3235d545780f7a1bc8673a95497f17cdebafdc1fe5cdde"></a>
<a id="agroup__semihost_html_gga425c53a045590978b0b3235d545780f7a300dde91715638debca2cbd6a61e508f"></a>
<a id="agroup__semihost_html_gga425c53a045590978b0b3235d545780f7a41befb06ac2fcce18e7a085b9e8911bc"></a>
<a id="agroup__semihost_html_gga425c53a045590978b0b3235d545780f7a5357da3dddbeb511d312291cbab9c466"></a>
<a id="agroup__semihost_html_gga425c53a045590978b0b3235d545780f7a99975dc411c6b501ef2f34f31a8aaa53"></a>
<a id="agroup__semihost_html_gga425c53a045590978b0b3235d545780f7ab7c309dc69b408ade19bff098818471b"></a>
<a id="agroup__semihost_html_gga425c53a045590978b0b3235d545780f7abf3d7d2b6e9a99bcacbff1c50bb1d262"></a>
<a id="agroup__semihost_html_ggadf61e00be557b7cb4457f7ea6f8da86da0e589cd7b9f53eeb303a419487e40a02"></a>
<a id="agroup__semihost_html_ggadf61e00be557b7cb4457f7ea6f8da86da32cc33a795888c73c3d1624f288fed46"></a>
<a id="agroup__semihost_html_ggadf61e00be557b7cb4457f7ea6f8da86da3db5621dbcb6c8a2a074cc69144f8367"></a>
<a id="agroup__semihost_html_ggadf61e00be557b7cb4457f7ea6f8da86da3e584069d9d8cd126bd409df9f99d627"></a>
<a id="agroup__semihost_html_ggadf61e00be557b7cb4457f7ea6f8da86da59856dd67e4079773f9ada8c3cb5ba26"></a>
<a id="agroup__semihost_html_ggadf61e00be557b7cb4457f7ea6f8da86da6d4f5801467a25613abf1d38386060ff"></a>
<a id="agroup__semihost_html_ggadf61e00be557b7cb4457f7ea6f8da86da6edbfcd0d356552569ae1cfcd78203a7"></a>
<a id="agroup__semihost_html_ggadf61e00be557b7cb4457f7ea6f8da86da78d21e53db4f44f375aefd25009dd71a"></a>
<a id="agroup__semihost_html_ggadf61e00be557b7cb4457f7ea6f8da86da7e0050f763d6c115c2b24064b4beb6ea"></a>
<a id="agroup__semihost_html_ggadf61e00be557b7cb4457f7ea6f8da86da88b03906fd14fe40d86c841de05539ce"></a>
<a id="agroup__semihost_html_ggadf61e00be557b7cb4457f7ea6f8da86da8963d2934a740ae5fd04ca84fd48f57f"></a>
<a id="agroup__semihost_html_ggadf61e00be557b7cb4457f7ea6f8da86daa800fb6638cb45941c81d41275779cac"></a>
<a id="agroup__semihost_html_ggadf61e00be557b7cb4457f7ea6f8da86daba47d649a03b0ed2bfc6fb8d3020563f"></a>
<a id="agroup__semihost_html_ggadf61e00be557b7cb4457f7ea6f8da86dac17ed558ffacf4612c234db887743ca0"></a>
<a id="agroup__semihost_html_ggadf61e00be557b7cb4457f7ea6f8da86dac1da151904c09d05b4548f1c28bb72ad"></a>
<a id="agroup__semihost_html_ggadf61e00be557b7cb4457f7ea6f8da86dad030bc2e7a63682116efb84011d40629"></a>
<a id="agroup__semihost_html_ggadf61e00be557b7cb4457f7ea6f8da86dad0ed15a780a1d9bd8583e01468f4abeb"></a>
<a id="agroup__semihost_html_ggadf61e00be557b7cb4457f7ea6f8da86dad8f17a37155fdb3c4e29c4c3ba2b4a4f"></a>
<a id="agroup__semihost_html_ggadf61e00be557b7cb4457f7ea6f8da86dad92d3362fc63d17b0f6c74f1c796ae53"></a>
<a id="agroup__semihost_html_ggadf61e00be557b7cb4457f7ea6f8da86dae3a468fafe97de23a4d0b125a438e8f6"></a>
<a id="agroup__semihost_html_ggadf61e00be557b7cb4457f7ea6f8da86daf6894316046e0cd2c07c7f55effddc8d"></a>
<a id="agroup__semihost_html_ggadf61e00be557b7cb4457f7ea6f8da86daffd89aae5102d56b677522ab2b66c438"></a>

```c
/*
 * Copyright (c) 2022, Commonwealth Scientific and Industrial Research
 * Organisation (CSIRO) ABN 41 687 119 230.
 *
 * SPDX-License-Identifier: Apache-2.0
 *
 * Based on the ARM semihosting API from:
 * https://github.com/ARM-software/abi-aa/blob/main/semihosting/semihosting.rst
 *
 * RISC-V semihosting also follows these conventions:
 * https://github.com/riscv-non-isa/riscv-semihosting/blob/main/riscv-semihosting.adoc
 */


#ifndef ZEPHYR_INCLUDE_ARCH_COMMON_SEMIHOST_H_
#define ZEPHYR_INCLUDE_ARCH_COMMON_SEMIHOST_H_

enum semihost_instr {
        /*
         * File I/O operations
         */

        SEMIHOST_OPEN   = 0x01,
        SEMIHOST_ISTTY  = 0x09,
        SEMIHOST_WRITE  = 0x05,
        SEMIHOST_READ   = 0x06,
        SEMIHOST_CLOSE  = 0x02,
        SEMIHOST_FLEN   = 0x0C,
        SEMIHOST_SEEK   = 0x0A,
        SEMIHOST_TMPNAM = 0x0D,
        SEMIHOST_REMOVE = 0x0E,
        SEMIHOST_RENAME = 0x0F,

        /*
         * Terminal I/O operations
         */

        SEMIHOST_WRITEC         = 0x03,
        SEMIHOST_WRITE0         = 0x04,
        SEMIHOST_READC          = 0x07,

        /*
         * Time operations
         */
        SEMIHOST_CLOCK          = 0x10,
        SEMIHOST_ELAPSED        = 0x30,
        SEMIHOST_TICKFREQ       = 0x31,
        SEMIHOST_TIME           = 0x11,

        /*
         * System/Misc. operations
         */

        SEMIHOST_ERRNO          = 0x13,
        SEMIHOST_GET_CMDLINE    = 0x15,
        SEMIHOST_HEAPINFO       = 0x16,
        SEMIHOST_ISERROR        = 0x08,
        SEMIHOST_SYSTEM         = 0x12
};

enum semihost_open_mode {
        SEMIHOST_OPEN_R         = 0,
        SEMIHOST_OPEN_RB        = 1,
        SEMIHOST_OPEN_R_PLUS    = 2,
        SEMIHOST_OPEN_RB_PLUS   = 3,
        SEMIHOST_OPEN_W         = 4,
        SEMIHOST_OPEN_WB        = 5,
        SEMIHOST_OPEN_W_PLUS    = 6,
        SEMIHOST_OPEN_WB_PLUS   = 7,
        SEMIHOST_OPEN_A         = 8,
        SEMIHOST_OPEN_AB        = 9,
        SEMIHOST_OPEN_A_PLUS    = 10,
        SEMIHOST_OPEN_AB_PLUS   = 11,
};

long semihost_exec(enum semihost_instr instr, void *args);

char semihost_poll_in(void);

void semihost_poll_out(char c);

long semihost_open(const char *path, long mode);

long semihost_close(long fd);

long semihost_flen(long fd);

long semihost_seek(long fd, long offset);

long semihost_read(long fd, void *buf, long len);

long semihost_write(long fd, const void *buf, long len);


#endif /* ZEPHYR_INCLUDE_ARCH_COMMON_SEMIHOST_H_ */
```

## 39.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权所有（Copyright）2022 澳大利亚联邦科学与工业研究组织（Commonwealth Scientific and Industrial Research Organisation，CSIRO），ABN 41 687 119 230。

SPDX-License-Identifier: Apache-2.0。

基于以下 ARM 半主机 API（Semihosting API）：
<https://github.com/ARM-software/abi-aa/blob/main/semihosting/semihosting.rst>

RISC-V 半主机机制（Semihosting）也遵循这些约定：
<https://github.com/riscv-non-isa/riscv-semihosting/blob/main/riscv-semihosting.adoc>

### 注释 2：原第 28 行

文件输入输出操作（File I/O Operations）。

### 注释 3：原第 53 行

终端输入输出操作（Terminal I/O Operations）。

### 注释 4：原第 64 行

时间操作（Time Operations）。

### 注释 5：原第 72 行

系统／其他操作（System / Miscellaneous Operations）。

### 注释 6：原第 201 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_ARCH_COMMON_SEMIHOST_H_`。

## 39.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/semihost_8h.html)
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

---

[上一章](P038_rv3032.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P040_sip_svc_agilex_smc.h_源码浏览.md)
