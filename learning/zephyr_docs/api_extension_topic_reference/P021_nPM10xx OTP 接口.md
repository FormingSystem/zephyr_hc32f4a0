---
id: learning.zephyr-docs.api-extension-topic-reference.page-21
title: nPM10xx OTP 接口
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__otp__interface__npm10xx.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第21章\_nPM10xx OTP 接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__otp__interface__npm10xx.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

自 4.5 版提供（Since 4.5）；接口版本（Version）0.1.0。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 21.1\_宏定义（Macros）

<a id="r_ga7e4bb77eb3261128bef0fdb854e01c1a"></a>

```c
#define OTP_NPM10XX_UICR_BITS 104U
```

相关声明：[OTP_NPM10XX_UICR_BITS](#ga7e4bb77eb3261128bef0fdb854e01c1a)。

用户可编程的用户信息配置寄存器位数（User-Programmable UICR Bits）。

<a id="r_ga1be9073f5cb879d4cff7d284a43112a1"></a>

```c
#define OTP_NPM10XX_UICR_SIZE DIV_ROUND_UP(OTP_NPM10XX_UICR_BITS, 8U)
```

相关声明：[OTP_NPM10XX_UICR_SIZE](#ga1be9073f5cb879d4cff7d284a43112a1)、[DIV_ROUND_UP](../util_reference/P001_通用工具公共接口.md#gae664e7492e37d324831caf2321ddda37)、[OTP_NPM10XX_UICR_BITS](#ga7e4bb77eb3261128bef0fdb854e01c1a)。

容纳这些位的打包字节大小（Packed Byte Size）。

<a id="r_ga3e7fed75f9523552a136d5e7ffb4ced1"></a>

```c
#define OTP_NPM10XX_UICR_LOCK_BIT 96U
```

相关声明：[OTP_NPM10XX_UICR_LOCK_BIT](#ga3e7fed75f9523552a136d5e7ffb4ced1)。

锁定位索引（Lock Bit Index）。

## 21.2\_详细说明（Detailed Documentation）

<a id="ga7e4bb77eb3261128bef0fdb854e01c1a"></a>

### `OTP_NPM10XX_UICR_BITS`

```c
#define OTP_NPM10XX_UICR_BITS 104U
```

```c
#include <zephyr/drivers/otp/npm10xx.h>
```

用户可编程的用户信息配置寄存器位数（User-Programmable UICR Bits）。

<a id="ga3e7fed75f9523552a136d5e7ffb4ced1"></a>

### `OTP_NPM10XX_UICR_LOCK_BIT`

```c
#define OTP_NPM10XX_UICR_LOCK_BIT 96U
```

```c
#include <zephyr/drivers/otp/npm10xx.h>
```

锁定位索引（Lock Bit Index）。

驱动最后才对其编程（Programs It Last）。

**说明（Note）**：重要（Important）：如果不希望锁定用户信息配置寄存器（UICR），请确保数据缓冲区（Data Buffer）中的此位设置为 0。

<a id="ga1be9073f5cb879d4cff7d284a43112a1"></a>

### `OTP_NPM10XX_UICR_SIZE`

```c
#define OTP_NPM10XX_UICR_SIZE DIV_ROUND_UP(OTP_NPM10XX_UICR_BITS, 8U)
```

```c
#include <zephyr/drivers/otp/npm10xx.h>
```

容纳这些位的打包字节大小（Packed Byte Size）。


## 21.3\_原页交叉引用（Cross References）

- [DIV_ROUND_UP](../util_reference/P001_通用工具公共接口.md#gae664e7492e37d324831caf2321ddda37)
- [zephyr/drivers/otp/npm10xx.h](../api_file_runtime_reference/P010_zephyr__drivers__otp__npm10xx.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P020_工作队列（Workqueues）.md) · [返回大纲](大纲.md) · [下一章](P022_分组套接字的套接字选项（Socket options for packet socket）.md)
