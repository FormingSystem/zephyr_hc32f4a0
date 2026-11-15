---
id: learning.zephyr-docs.time-headers-reference.page-5
title: timespec时间结构
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structtimespec.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_timespec时间结构

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structtimespec.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入最小C库时间类型、系统时钟兼容入口和网络长超时参考，再通过接口链接进入完整说明。源码跟踪译注与官方原文分开标示。

```c
#include <zephyr/posix/posix_signal.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 5.1\_数据成员（Data Fields）

<a id="r_afc3302668d7cb5952f590da69fdd4955"></a>

```c
time_t tv_sec
```

相关声明：[time_t](P003_timespec类型头文件参考.md#aa17c461cd5eca7fc12a66daa803c7fd7)、[tv_sec](#afc3302668d7cb5952f590da69fdd4955)。

<a id="r_ae3c7510dafa8cbcaede866ed13c99683"></a>

```c
long tv_nsec
```

相关声明：[tv_nsec](#ae3c7510dafa8cbcaede866ed13c99683)。

## 5.2\_详细说明（Detailed Documentation）

<a id="ae3c7510dafa8cbcaede866ed13c99683"></a>

### `tv_nsec`

```c
long timespec::tv_nsec
```

<a id="afc3302668d7cb5952f590da69fdd4955"></a>

### `tv_sec`

```c
time_t timespec::tv_sec
```

## 5.3\_源码定位与版本边界

相对源码定位：[最小C库timespec声明](../../../lib/libc/minimal/include/sys/_timespec.h)、[时间工具接口](../../../include/zephyr/sys/timeutil.h)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下源码跟踪译注独立于官方正文，依据来源记录中保存摘要的官方main文件。译文与仓库内已有源码采用相对链接，不依赖作者机器位置；不同C库和构建配置须分别核对。

> 译注——源码核对：本次最小C库的time_t来自_TIME_T_，后者在sys/_types.h中定义为int64_t；suseconds_t来自int32_t的_SUSECONDS_T_。这些是该C库的具体类型，不应推广到所有外部C库或任意ABI。tv_nsec声明为long，不能把time_t和纳秒字段当作必然同宽。

> 译注——源码核对：结构体声明本身不会校验或规范化数值。Zephyr时间工具以0 ≤ tv_nsec < 10^9作为规范化条件（Normalization）；tv_sec为秒，tv_nsec为该秒内纳秒部分。类型不携带时钟标识（Clock ID）或纪元（Epoch），绝对时间与相对时长要由使用它的API决定。

> 译注——源码核对：_timespec.h用__time_t_defined、__suseconds_t_defined和两种timespec保护宏避免重复定义。Doxygen把同名timespec的多个来源汇到一个结构页，不意味着应用应同时手工包含不同C库的实现头文件。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 5.4\_原页交叉引用（Cross References）

- [zephyr/posix/posix_signal.h](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h_source.html)
- [time_t](P003_timespec类型头文件参考.md#aa17c461cd5eca7fc12a66daa803c7fd7)
- [posix_time.h](https://docs.zephyrproject.org/latest/doxygen/html/posix__time_8h_source.html)
- [_timespec.h](P004_timespec类型头文件源码.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P004_timespec类型头文件源码.md) · [返回大纲](大纲.md) · [下一章](P006_系统时钟兼容头文件参考.md)
