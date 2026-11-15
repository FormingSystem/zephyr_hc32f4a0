---
id: learning.zephyr-docs.api-file-runtime-reference.page-10
title: zephyr__drivers__otp__npm10xx.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2otp_2npm10xx_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_zephyr\_\_drivers\_\_otp\_\_npm10xx.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2otp_2npm10xx_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Nordic nPM10系列电源管理集成电路（PMIC）的OTP驱动定义。

<a id="details"></a>

```c
#include <zephyr/drivers/otp.h>
#include <zephyr/sys/util.h>
```

查看此文件的源码。

Nordic nPM10系列电源管理集成电路（PMIC）的OTP驱动定义。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 10.1\_宏定义（Macros）

<a id="r_ga7e4bb77eb3261128bef0fdb854e01c1a"></a>

```c
#define OTP_NPM10XX_UICR_BITS 104U
```

相关声明：[OTP_NPM10XX_UICR_BITS](https://docs.zephyrproject.org/latest/doxygen/html/group__otp__interface__npm10xx.html#ga7e4bb77eb3261128bef0fdb854e01c1a)。

用户可编程的用户信息配置寄存器位数（User-Programmable UICR Bits）。

<a id="r_ga1be9073f5cb879d4cff7d284a43112a1"></a>

```c
#define OTP_NPM10XX_UICR_SIZE DIV_ROUND_UP(OTP_NPM10XX_UICR_BITS, 8U)
```

相关声明：[OTP_NPM10XX_UICR_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__otp__interface__npm10xx.html#ga1be9073f5cb879d4cff7d284a43112a1)、[DIV_ROUND_UP](../util_reference/P001_通用工具公共接口.md#gae664e7492e37d324831caf2321ddda37)、[OTP_NPM10XX_UICR_BITS](https://docs.zephyrproject.org/latest/doxygen/html/group__otp__interface__npm10xx.html#ga7e4bb77eb3261128bef0fdb854e01c1a)。

容纳这些位的打包字节大小（Packed Byte Size）。

<a id="r_ga3e7fed75f9523552a136d5e7ffb4ced1"></a>

```c
#define OTP_NPM10XX_UICR_LOCK_BIT 96U
```

相关声明：[OTP_NPM10XX_UICR_LOCK_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__otp__interface__npm10xx.html#ga3e7fed75f9523552a136d5e7ffb4ced1)。

锁定位索引（Lock Bit Index）。


## 10.2\_原页交叉引用（Cross References）

- [zephyr/drivers/otp.h](../api_source_reference/P639_otp.h_源码浏览.md)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P167_npm10xx.h_源码浏览.md)
- [OTP_NPM10XX_UICR_BITS](https://docs.zephyrproject.org/latest/doxygen/html/group__otp__interface__npm10xx.html#ga7e4bb77eb3261128bef0fdb854e01c1a)
- [OTP_NPM10XX_UICR_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__otp__interface__npm10xx.html#ga1be9073f5cb879d4cff7d284a43112a1)
- [DIV_ROUND_UP](../util_reference/P001_通用工具公共接口.md#gae664e7492e37d324831caf2321ddda37)
- [OTP_NPM10XX_UICR_LOCK_BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__otp__interface__npm10xx.html#ga3e7fed75f9523552a136d5e7ffb4ced1)

<a id="header-details"></a>

---

[上一章](P009_zephyr__net__dhcpv6.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P011_zephyr__drivers__sensor__battery.h_文件参考.md)
