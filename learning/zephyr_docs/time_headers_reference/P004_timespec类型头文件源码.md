---
id: learning.zephyr-docs.time-headers-reference.page-4
title: timespec类型头文件源码
kind: reference
status: maintained
domains: [zephyr, kernel, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/__timespec_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_timespec类型头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/__timespec_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；完整接口说明见[头文件参考](P003_timespec类型头文件参考.md)和[公共API](P005_timespec时间结构.md)。

## 4.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="a__timespec_8h_html_aa17c461cd5eca7fc12a66daa803c7fd7"></a>
<a id="a__timespec_8h_html_ad7acf95ceafb15a1d8d86af0c4982995"></a>
<a id="a__types_8h_html"></a>
<a id="astructtimespec_html"></a>
<a id="astructtimespec_html_ae3c7510dafa8cbcaede866ed13c99683"></a>
<a id="astructtimespec_html_afc3302668d7cb5952f590da69fdd4955"></a>

<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * Copyright (c) 2019 Linaro Limited
<a id="l00003"></a> *
<a id="l00004"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00005"></a> */
<a id="l00006"></a>
<a id="l00007"></a>#ifndef ZEPHYR_LIB_LIBC_MINIMAL_INCLUDE_SYS__TIMESPEC_H_
<a id="l00008"></a>#define ZEPHYR_LIB_LIBC_MINIMAL_INCLUDE_SYS__TIMESPEC_H_
<a id="l00009"></a>
<a id="l00010"></a>#include &lt;sys/_types.h&gt;
<a id="l00011"></a>
<a id="l00012"></a>#if !defined(__time_t_defined)
<a id="l00013"></a>#define __time_t_defined
<a id="l00014"></a>typedef _TIME_T_ time_t;
<a id="l00015"></a>#endif
<a id="l00016"></a>
<a id="l00017"></a>#if !defined(__suseconds_t_defined)
<a id="l00018"></a>#define __suseconds_t_defined
<a id="l00019"></a>typedef _SUSECONDS_T_ suseconds_t;
<a id="l00020"></a>#endif
<a id="l00021"></a>
<a id="l00022"></a>#if !defined(_TIMESPEC_DECLARED) &amp;&amp; !defined(__timespec_defined)
<a id="l00023"></a>struct timespec {
<a id="l00024"></a>        time_t tv_sec;
<a id="l00025"></a>        long tv_nsec;
<a id="l00026"></a>};
<a id="l00027"></a>#define __timespec_defined
<a id="l00028"></a>#define _TIMESPEC_DECLARED
<a id="l00029"></a>#endif
<a id="l00030"></a>
<a id="l00031"></a>#endif /* ZEPHYR_LIB_LIBC_MINIMAL_INCLUDE_SYS__TIMESPEC_H_ */
</code></pre>

## 4.2\_可见注释译文（Comments）

1. 版权与许可证：Copyright (c) 2019 Linaro Limited；SPDX-License-Identifier: Apache-2.0。原始法律声明保留。

2. ZEPHYR_LIB_LIBC_MINIMAL_INCLUDE_SYS__TIMESPEC_H_头文件包含保护结束。

## 4.3\_原页符号提示（Symbol Descriptions）

### `time_t`

```c
_TIME_T_ time_t
```

定义位置（Definition）：_timespec.h:14。

符号定位：[time_t](P003_timespec类型头文件参考.md#aa17c461cd5eca7fc12a66daa803c7fd7)。

### `suseconds_t`

```c
_SUSECONDS_T_ suseconds_t
```

定义位置（Definition）：_timespec.h:19。

符号定位：[suseconds_t](P003_timespec类型头文件参考.md#ad7acf95ceafb15a1d8d86af0c4982995)。

### `_types.h`

符号定位：[_types.h](https://docs.zephyrproject.org/latest/doxygen/html/__types_8h.html)。

### `timespec`

定义位置（Definition）：posix_signal.h:53。

符号定位：[timespec](P005_timespec时间结构.md)。

### `timespec::tv_nsec`

```c
long tv_nsec
```

定义位置（Definition）：posix_signal.h:55。

符号定位：[timespec::tv_nsec](P005_timespec时间结构.md#ae3c7510dafa8cbcaede866ed13c99683)。

### `timespec::tv_sec`

```c
time_t tv_sec
```

定义位置（Definition）：posix_signal.h:54。

符号定位：[timespec::tv_sec](P005_timespec时间结构.md#afc3302668d7cb5952f590da69fdd4955)。

## 4.4\_源码跟踪译注

> 译注——本次最小C库的time_t来自_TIME_T_，后者在sys/_types.h中定义为int64_t；suseconds_t来自int32_t的_SUSECONDS_T_。这些是该C库的具体类型，不应推广到所有外部C库或任意ABI。tv_nsec声明为long，不能把time_t和纳秒字段当作必然同宽。

> 译注——结构体声明本身不会校验或规范化数值。Zephyr时间工具以0 ≤ tv_nsec < 10^9作为规范化条件（Normalization）；tv_sec为秒，tv_nsec为该秒内纳秒部分。类型不携带时钟标识（Clock ID）或纪元（Epoch），绝对时间与相对时长要由使用它的API决定。

> 译注——_timespec.h用__time_t_defined、__suseconds_t_defined和两种timespec保护宏避免重复定义。Doxygen把同名timespec的多个来源汇到一个结构页，不意味着应用应同时手工包含不同C库的实现头文件。

头文件相对定位：[lib/libc/minimal/include/sys/_timespec.h](../../../lib/libc/minimal/include/sys/_timespec.h)，关联实现／接口：[lib/libc/minimal/include/sys/_types.h](../../../lib/libc/minimal/include/sys/_types.h)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/lib/libc/minimal/include/sys/_timespec.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/lib/libc/minimal/include/sys/_types.h)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 4.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P003_timespec类型头文件参考.md)
- [sys/_types.h](https://docs.zephyrproject.org/latest/doxygen/html/__types_8h.html)
- [time_t](P003_timespec类型头文件参考.md#aa17c461cd5eca7fc12a66daa803c7fd7)
- [suseconds_t](P003_timespec类型头文件参考.md#ad7acf95ceafb15a1d8d86af0c4982995)
- [timespec](P005_timespec时间结构.md)
- [tv_sec](P005_timespec时间结构.md#afc3302668d7cb5952f590da69fdd4955)
- [tv_nsec](P005_timespec时间结构.md#ae3c7510dafa8cbcaede866ed13c99683)

---

[上一章](P003_timespec类型头文件参考.md) · [返回大纲](大纲.md) · [下一章](P005_timespec时间结构.md)
