---
id: learning.zephyr-docs.observability.obapi-3
title: MIPI_STP解码配置
kind: reference
status: maintained
domains: [zephyr, observability]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmipi__stp__decoder__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第28章\_MIPI_STP解码配置

原文：[structmipi__stp__decoder__config](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__stp__decoder__config.html)。读取日期：2026-10-13，`latest`。

## 28.1\_类型与头文件

结构 [`mipi_stp_decoder_config`](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__stp__decoder__config.html) 保存 **MIPI系统跟踪协议（MIPI System Trace Protocol，MIPI STP）**解码器配置。

```c
#include <zephyr/debug/mipi_stp_decoder.h>
```

## 28.2\_字段

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| <a id="abf1a03280ec82f3a2db7aef25c6522ac"></a>[`start_out_of_sync`](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__stp__decoder__config.html#abf1a03280ec82f3a2db7aef25c6522ac) | [`bool`](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b) | 指示解码器以未同步（Out of Sync）状态启动 |
| <a id="a519473c106e406e453c104790045d404"></a>[`cb`](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__stp__decoder__config.html#a519473c106e406e453c104790045d404) | [`mipi_stp_decoder_cb`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__stp__decoder__apis.html#ga8c6fdc2927d954291a12e4c31ad8abe2) | 解码回调（Callback），签名见[解码接口](P027_MIPI_STP解码接口.md) |

本结构文档由 `zephyr/debug/mipi_stp_decoder.h` 生成。

---

[上一章：MIPI_STP解码接口](P027_MIPI_STP解码接口.md) · [下一章：MIPI_STP解码数据](P029_MIPI_STP解码数据.md) · [返回大纲](大纲.md)
