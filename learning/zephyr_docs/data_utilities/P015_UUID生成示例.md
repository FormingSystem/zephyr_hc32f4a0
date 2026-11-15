---
id: learning.zephyr-docs.data-utilities.page-15
title: UUID生成示例
kind: reference
status: maintained
domains: [zephyr, data, development]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/uuid/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_UUID生成示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/uuid/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 15.1\_概述

本示例按照 [RFC 9562](https://datatracker.ietf.org/doc/html/rfc9562.html)，演示UUID工具的生成和处理功能：

- 生成UUIDv4。
- 根据命名空间和数据生成UUIDv5。
- 在UUID与字符串之间转换，并转换为Base64和URL安全Base64（URL-safe Base64）格式。

## 15.2\_要求

原文列出的依赖包括：

| 依赖 | 用途 |
| --- | --- |
| Mbed TLS | UUIDv5使用的哈希函数（Hash Functions） |
| Base64 | UUID的Base64编码 |
| 熵源（Entropy Source） | UUIDv4的伪随机生成（Pseudorandom Generation） |

译注：当前配套配置启用 `CONFIG_PSA_CRYPTO`、`CONFIG_PSA_WANT_ALG_SHA_1`、`CONFIG_BASE64` 和 `CONFIG_ENTROPY_GENERATOR`；v5实现通过PSA哈希接口处理SHA-1。原文把哈希依赖写作MbedTLS，实际接入应按所用版本的PSA后端及模块配置核对，而不是仅判断目录里是否有某个库。Base64转换只改变表示方式，不生成新的UUID。

## 15.3\_构建与运行

使用标准west命令构建并烧录应用。原文为 `native_sim` 给出下面的构建和运行示例；主机终端位于已准备好工具链、模块及native_sim主机依赖的Zephyr源码根目录：

```sh
west build -b native_sim samples/subsys/uuid
west build -t run
```

译注：上面的 `west build -t run` 运行主机仿真目标，不是硬件烧录命令。UUIDv4的值预期随随机输入变化；UUIDv5在命名空间与名称相同的情况下保持一致，不应把两者采用相同的输出匹配方式。


译注核对来源：[samples/subsys/uuid/src/main.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/uuid/src/main.c)、[samples/subsys/uuid/prj.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/uuid/prj.conf)。

本仓库的[对应源码](../../../samples/subsys/uuid/src/main.c)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档；UUIDv5示例值另用主机标准库交叉计算，没有执行固件构建、烧录或硬件操作。

<a id="uuid"></a>
<a id="overview"></a>
<a id="index-0"></a>
<a id="requirements"></a>
<a id="building-and-running"></a>

[上一章](P014_UUID通用唯一标识符.md) · [返回大纲](大纲.md) · [下一章](P016_二进制描述符接口总览.md)
