---
id: learning.zephyr-docs.log-backend-helpers-reference.page-2
title: Intel_ADSP_HDA日志后端头文件参考
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/log__backend__adsp__hda_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_Intel\_ADSP\_HDA日志后端头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/log__backend__adsp__hda_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入Intel ADSP日志后端、标准辅助接口与多域辅助接口。源码跟踪译注与官方原文分开标示。

Intel ADSP HDA日志后端的头文件。

<a id="details"></a>

```c
#include <stdint.h>
```

查看此文件的源码。

Intel ADSP HDA日志后端的头文件。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 2.1\_类型定义（Typedefs）

<a id="r_ga8d50e67fece0cf916b72fcaa7c2bd11a"></a>

```c
typedef void(* adsp_hda_log_hook_t) (uint32_t written)
```

相关声明：[adsp_hda_log_hook_t](P001_Intel_ADSP_HDA日志后端接口.md#ga8d50e67fece0cf916b72fcaa7c2bd11a)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

HDA日志记录器需要一个用于进程间通信（IPC）消息的钩子（Hook）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 2.2\_函数（Functions）

<a id="r_gac9ae5b9b36f95d30643c0acf95d51e82"></a>

```c
void adsp_hda_log_init (adsp_hda_log_hook_t hook, uint32_t channel)
```

相关声明：[adsp_hda_log_init](P001_Intel_ADSP_HDA日志后端接口.md#gac9ae5b9b36f95d30643c0acf95d51e82)、[adsp_hda_log_hook_t](P001_Intel_ADSP_HDA日志后端接口.md#ga8d50e67fece0cf916b72fcaa7c2bd11a)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

初始化Intel ADSP HDA日志记录器。

## 2.3\_源码定位与版本边界

源码定位：[include/zephyr/logging/log_backend_adsp_hda.h](../../../include/zephyr/logging/log_backend_adsp_hda.h)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下译注独立于官方正文，依据来源记录中的官方头文件与可取得的实现；本地链接均为相对路径。

> 译注——源码核对：HDA接口使用指定的DMA通道（DMA Channel），钩子用于通知主机可读取日志；声明中的channel不是一般意义上的Zephyr线程或日志域编号。

> 译注——源码核对：原文明确保证每次刷新调用一次钩子，但允许多个CPU和调用上下文并发执行。需要共享计数或发送IPC消息时，串行化由钩子实现者负责，不能假定日志核心已经替它加锁。

> 译注——源码核对：本次已核对官方头文件声明；当前官方路径未取得对应HDA后端实现，因此不补造通道配置、DMA完成时序或written参数的额外语义。此项限制不影响对这三份官方页面本身的完整翻译。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 2.4\_原页交叉引用（Cross References）

- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h_source.html)
- [查看此文件的源码](P003_Intel_ADSP_HDA日志后端头文件源码.md)
- [adsp_hda_log_hook_t](P001_Intel_ADSP_HDA日志后端接口.md#ga8d50e67fece0cf916b72fcaa7c2bd11a)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [adsp_hda_log_init](P001_Intel_ADSP_HDA日志后端接口.md#gac9ae5b9b36f95d30643c0acf95d51e82)

<a id="header-details"></a>

---

[上一章](P001_Intel_ADSP_HDA日志后端接口.md) · [返回大纲](大纲.md) · [下一章](P003_Intel_ADSP_HDA日志后端头文件源码.md)
