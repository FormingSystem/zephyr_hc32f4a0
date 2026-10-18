---
id: learning.zephyr-docs.modem-wireless-model-reference.page-19
title: hl78xx_ctzeu_update_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structhl78xx__ctzeu__update.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_hl78xx\_ctzeu\_update\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structhl78xx__ctzeu__update.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

已解析的+CTZEU更新载荷。

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

<a id="details"></a>

已解析的 `+CTZEU` 更新载荷。`tz` 字段已经包含夏令时（DST）调整，与调制解调器对 `+CTZEU` 的规定一致。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 19.1\_数据成员（Data Fields）

<a id="r_a5e0f09445a9abda3c5f0b37b97473815"></a>

```c
int tz
```

相关声明：[tz](#a5e0f09445a9abda3c5f0b37b97473815)。

相对于格林尼治时间（GMT）的本地时区偏移量，以 15 分钟为单位，包含夏令时调整。

<a id="r_ae5eba83a8def3c9720797fd2f1ff46d0"></a>

```c
int dst
```

相关声明：[dst](#ae5eba83a8def3c9720797fd2f1ff46d0)。

调制解调器报告的夏令时指示值：0、1 或 2。

<a id="r_a9f0db53ae132db9a43e6a00b93807145"></a>

```c
bool has_utime
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[has_utime](#a9f0db53ae132db9a43e6a00b93807145)。

通知中包含世界时（universal time）字段。

<a id="r_a0c90dddc2087e97afd6da421a7862323"></a>

```c
int64_t date_time_ms
```

相关声明：[int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)、[date_time_ms](#a0c90dddc2087e97afd6da421a7862323)。

已解析的世界时，以 UTC Unix 纪元毫秒数表示。

<a id="r_a3b4a66b56a5632a7dc7a4964f949f7b1"></a>

```c
struct tm utc_time
```

相关声明：[tm](../posix_system_model_reference/P025_tm_结构体.md)、[utc_time](#a3b4a66b56a5632a7dc7a4964f949f7b1)。

已解析的世界时，以分解后的 UTC 日期时间结构表示。

## 19.2\_详细说明（Detailed Documentation）

<a id="a0c90dddc2087e97afd6da421a7862323"></a>

### `date_time_ms`

```c
int64_t hl78xx_ctzeu_update::date_time_ms
```

已解析的世界时，以 UTC Unix 纪元毫秒数表示。

<a id="ae5eba83a8def3c9720797fd2f1ff46d0"></a>

### `dst`

```c
int hl78xx_ctzeu_update::dst
```

调制解调器报告的夏令时指示值：0、1 或 2。

<a id="a9f0db53ae132db9a43e6a00b93807145"></a>

### `has_utime`

```c
bool hl78xx_ctzeu_update::has_utime
```

通知中包含世界时（universal time）字段。

<a id="a5e0f09445a9abda3c5f0b37b97473815"></a>

### `tz`

```c
int hl78xx_ctzeu_update::tz
```

相对于格林尼治时间（GMT）的本地时区偏移量，以 15 分钟为单位，包含夏令时调整。

<a id="a3b4a66b56a5632a7dc7a4964f949f7b1"></a>

### `utc_time`

```c
struct tm hl78xx_ctzeu_update::utc_time
```

已解析的世界时，以分解后的 UTC 日期时间结构表示。

`has_utime` 为 `true` 时有效。

本数据类型文档由以下文件生成：

- `zephyr/drivers/modem/hl78xx_apis.h`

## 19.3\_原页交叉引用（Cross References）

- [zephyr/drivers/modem/hl78xx_apis.h](https://docs.zephyrproject.org/latest/doxygen/html/hl78xx__apis_8h_source.html)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)
- [tm](../posix_system_model_reference/P025_tm_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P018_hl78xx_at_notification_结构体.md) · [返回大纲](大纲.md) · [下一章](P020_hl78xx_cxreg_status_结构体.md)
