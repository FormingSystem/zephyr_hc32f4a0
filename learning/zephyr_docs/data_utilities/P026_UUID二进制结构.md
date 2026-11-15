---
id: learning.zephyr-docs.data-utilities.api-26
title: UUID二进制结构
kind: reference
status: maintained
domains: [zephyr, data, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structuuid.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第26章\_UUID二进制结构

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structuuid.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 26.1\_阅读说明与来源

译注：本组是 `<zephyr/sys/uuid.h>` 的通用唯一标识符（Universally Unique Identifier，UUID）接口。先读[UUID 指南](P014_UUID通用唯一标识符.md)和[生成示例](P015_UUID生成示例.md)，再查询生成、比较、解析及编码转换。蓝牙专用 UUID 类型和接口另有官方页面，不与这里的 `struct uuid` 混用。

本组：[UUID生成与转换接口](P023_UUID生成与转换接口.md) · [UUID系统头文件](P024_UUID系统头文件.md) · [UUID系统头文件源码](P025_UUID系统头文件源码.md) · [UUID二进制结构](P026_UUID二进制结构.md)。

UUID 的二进制表示（Binary Representation）。

```c
#include <zephyr/sys/uuid.h>
```

UUID 的二进制表示（Binary Representation）。

## 26.2\_相关源码与使用边界

声明来自 `<zephyr/sys/uuid.h>`。可通过本仓库[对应头文件](../../../include/zephyr/sys/uuid.h)追踪源码；本仓库版本可能与官网 `latest` 不同。译注核对依据为保存的[官方头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/sys/uuid.h)、[官方实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/lib/uuid/uuid.c)和[Kconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/lib/uuid/Kconfig)，摘要见[来源记录](../SOURCES.md)。

> 译注——结构与缓冲区：Doxygen 结构参考隐藏了 `val` 成员，当前官方头文件实际为 `uint8_t val[UUID_SIZE]`，即 16 字节。规范文本的容量为 37 字节、Base64 为 25 字节、Base64URL 为 23 字节，这些文本容量均包含末尾空字符，不能与二进制的 16 字节互换。复制、比较和转换接口需要有效的输入对象；仅检查输出指针的函数不承诺对空输入返回错误码。

<a id="details"></a>
<a id="header-details"></a>

[上一章](P025_UUID系统头文件源码.md) · [返回大纲](大纲.md)
