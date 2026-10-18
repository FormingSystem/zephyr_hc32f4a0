---
id: learning.zephyr-docs.api-file-service-reference.page-25
title: zephyr__mpipe__mpipe_message.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mpipe__message_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第25章\_zephyr\_\_mpipe\_\_mpipe\_message.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__message_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

总线消息（Bus Message）：元素向应用报告的内容。

<a id="details"></a>

```c
#include <stdint.h>
#include <zephyr/kernel.h>
#include <zephyr/sys/util_macro.h>
#include <zephyr/mpipe/mpipe_element.h>
```

查看此文件的源码。

总线消息（Bus Message）：元素向应用报告的内容。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 25.1\_数据结构（Data Structures）

<a id="r_mpipe_5Fmessage"></a>

```c
struct mpipe_message
```

相关声明：[mpipe_message](../audio_video_model_reference/P023_mpipe_message_结构体.md)。

携带消息类型和来源的消息结构（Message Structure）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 25.2\_宏定义（Macros）

<a id="r_gac446a0608709579c28f1eec01ffa3890"></a>

```c
#define MPIPE_MESSAGE_ANY UINT32_MAX
```

相关声明：[MPIPE_MESSAGE_ANY](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__message.html#gac446a0608709579c28f1eec01ffa3890)、[UINT32_MAX](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ab5eb23180f7cc12b7d6c04a8ec067fdd)。

匹配任意消息类型（Message Type）的过滤掩码（Filter Mask）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 25.3\_枚举（Enumerations）

<a id="r_ga2cbfffc03b1b703e80f73c70207cf049"></a>

```c
enum mpipe_message_type { MPIPE_MESSAGE_UNKNOWN = 0 , MPIPE_MESSAGE_EOS = BIT(0) , MPIPE_MESSAGE_ERROR = BIT(1) }
```

相关声明：[mpipe_message_type](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__message.html#ga2cbfffc03b1b703e80f73c70207cf049)、[MPIPE_MESSAGE_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__message.html#gga2cbfffc03b1b703e80f73c70207cf049a134a8207baabf7e3f75aa6a8d0d03c7f)、[MPIPE_MESSAGE_EOS](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__message.html#gga2cbfffc03b1b703e80f73c70207cf049a0cfb22ae656d98b8915937035314e32c)、[MPIPE_MESSAGE_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__message.html#gga2cbfffc03b1b703e80f73c70207cf049a0ce944a0bd05b7b9d035a1dd717726cc)。

可用作位掩码过滤器（Bitmask Filters）的消息类型（Message Types）。

<a id="r_ga686a716e86c28adfbb11dc0c1e172c22"></a>

```c
enum mpipe_error_domain { MPIPE_ERROR_FAILED = 0 , MPIPE_ERROR_CAPS , MPIPE_ERROR_BUFFER_POOL , MPIPE_ERROR_FLOW , MPIPE_ERROR_RESOURCE , MPIPE_ERROR_DOMAIN_END }
```

相关声明：[mpipe_error_domain](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__message.html#ga686a716e86c28adfbb11dc0c1e172c22)、[MPIPE_ERROR_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__message.html#gga686a716e86c28adfbb11dc0c1e172c22a3c3ba67cbdbccb5b4771b38854d384c3)、[MPIPE_ERROR_CAPS](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__message.html#gga686a716e86c28adfbb11dc0c1e172c22a1e75a9bfcc4498a13c83629832d5b121)、[MPIPE_ERROR_BUFFER_POOL](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__message.html#gga686a716e86c28adfbb11dc0c1e172c22a4319b9de20494144e9d9dc1330acbdba)、[MPIPE_ERROR_FLOW](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__message.html#gga686a716e86c28adfbb11dc0c1e172c22a0d6250f8be21799d179e0e381ac50e79)、[MPIPE_ERROR_RESOURCE](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__message.html#gga686a716e86c28adfbb11dc0c1e172c22aea01f57f830f9db7a23673aea2b02fb6)、[MPIPE_ERROR_DOMAIN_END](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__message.html#gga686a716e86c28adfbb11dc0c1e172c22a23e26086d682f178fa75ce423c8e341a)。

发生失败的领域（Domain），即元素当时正在执行的操作。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 25.4\_函数（Functions）

<a id="r_ga371e6503fe08971ce1a2606d0a034b41"></a>

```c
int mpipe_message_post (const struct mpipe_message *message)
```

相关声明：[mpipe_message_post](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__message.html#ga371e6503fe08971ce1a2606d0a034b41)、[mpipe_message](../audio_video_model_reference/P023_mpipe_message_结构体.md)。

向包含消息源元素的元素容器（Bin）之总线（Bus）发布消息（Message）。


## 25.5\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/sys/util_macro.h](../util_reference/P005_宏工具头文件源码.md)
- [zephyr/mpipe/mpipe_element.h](../api_source_reference/P550_mpipe_element.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P552_mpipe_message.h_源码浏览.md)
- [mpipe_message](../audio_video_model_reference/P023_mpipe_message_结构体.md)
- [MPIPE_MESSAGE_ANY](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__message.html#gac446a0608709579c28f1eec01ffa3890)
- [UINT32_MAX](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ab5eb23180f7cc12b7d6c04a8ec067fdd)
- [mpipe_message_type](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__message.html#ga2cbfffc03b1b703e80f73c70207cf049)
- [MPIPE_MESSAGE_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__message.html#gga2cbfffc03b1b703e80f73c70207cf049a134a8207baabf7e3f75aa6a8d0d03c7f)
- [MPIPE_MESSAGE_EOS](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__message.html#gga2cbfffc03b1b703e80f73c70207cf049a0cfb22ae656d98b8915937035314e32c)
- [MPIPE_MESSAGE_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__message.html#gga2cbfffc03b1b703e80f73c70207cf049a0ce944a0bd05b7b9d035a1dd717726cc)
- [mpipe_error_domain](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__message.html#ga686a716e86c28adfbb11dc0c1e172c22)
- [MPIPE_ERROR_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__message.html#gga686a716e86c28adfbb11dc0c1e172c22a3c3ba67cbdbccb5b4771b38854d384c3)
- [MPIPE_ERROR_CAPS](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__message.html#gga686a716e86c28adfbb11dc0c1e172c22a1e75a9bfcc4498a13c83629832d5b121)
- [MPIPE_ERROR_BUFFER_POOL](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__message.html#gga686a716e86c28adfbb11dc0c1e172c22a4319b9de20494144e9d9dc1330acbdba)
- [MPIPE_ERROR_FLOW](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__message.html#gga686a716e86c28adfbb11dc0c1e172c22a0d6250f8be21799d179e0e381ac50e79)
- [MPIPE_ERROR_RESOURCE](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__message.html#gga686a716e86c28adfbb11dc0c1e172c22aea01f57f830f9db7a23673aea2b02fb6)
- [MPIPE_ERROR_DOMAIN_END](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__message.html#gga686a716e86c28adfbb11dc0c1e172c22a23e26086d682f178fa75ce423c8e341a)
- [mpipe_message_post](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__message.html#ga371e6503fe08971ce1a2606d0a034b41)

<a id="header-details"></a>

---

[上一章](P024_zephyr__mpipe__utils__mpipe_dump.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P026_zephyr__mpipe__base__mpipe_queue.h_文件参考.md)
