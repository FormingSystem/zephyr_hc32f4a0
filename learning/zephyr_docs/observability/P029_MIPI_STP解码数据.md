---
id: learning.zephyr-docs.observability.obapi-4
title: MIPI_STP解码数据
kind: reference
status: maintained
domains: [zephyr, observability]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/unionmipi__stp__decoder__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第29章\_MIPI_STP解码数据

原文：[unionmipi__stp__decoder__data](https://docs.zephyrproject.org/latest/doxygen/html/unionmipi__stp__decoder__data.html)。读取日期：2026-10-13，`latest`。

## 29.1\_类型与头文件

联合体（Union）[`mipi_stp_decoder_data`](https://docs.zephyrproject.org/latest/doxygen/html/unionmipi__stp__decoder__data.html) 保存与给定 **MIPI系统跟踪协议（MIPI System Trace Protocol，MIPI STP）**操作码（Opcode）关联的数据。

```c
#include <zephyr/debug/mipi_stp_decoder.h>
```

## 29.2\_字段

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| <a id="a3c7d85bc475b27f570b9059745d7d11f"></a>[`id`](https://docs.zephyrproject.org/latest/doxygen/html/unionmipi__stp__decoder__data.html#a3c7d85bc475b27f570b9059745d7d11f) | [`uint16_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e) | 标识符（Identifier，ID），用于主设备（Major）和通道（Channel） |
| <a id="a3b3cae98d63ceda950e88690da282966"></a>[`freq`](https://docs.zephyrproject.org/latest/doxygen/html/unionmipi__stp__decoder__data.html#a3b3cae98d63ceda950e88690da282966) | [`uint64_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1) | 频率（Frequency） |
| <a id="a3dc68ca2196c807965071d754c139655"></a>[`ver`](https://docs.zephyrproject.org/latest/doxygen/html/unionmipi__stp__decoder__data.html#a3dc68ca2196c807965071d754c139655) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | 版本（Version） |
| <a id="ace873d9e7d38a5f39338618b4d74cdf4"></a>[`err`](https://docs.zephyrproject.org/latest/doxygen/html/unionmipi__stp__decoder__data.html#ace873d9e7d38a5f39338618b4d74cdf4) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | 错误码（Error Code） |
| <a id="a70db937ada38cb0f97cd45fa78bd9466"></a>[`dummy`](https://docs.zephyrproject.org/latest/doxygen/html/unionmipi__stp__decoder__data.html#a70db937ada38cb0f97cd45fa78bd9466) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | 占位数据（Dummy） |
| <a id="a1cb5f92d1d0976f1ec047e7398e6d95d"></a>[`data`](https://docs.zephyrproject.org/latest/doxygen/html/unionmipi__stp__decoder__data.html#a1cb5f92d1d0976f1ec047e7398e6d95d) | [`uint64_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1) | 数据（Data） |

本文档由 `zephyr/debug/mipi_stp_decoder.h` 生成，关联[解码接口](P027_MIPI_STP解码接口.md)。

---

[上一章：MIPI_STP解码配置](P028_MIPI_STP解码配置.md) · [下一章：STMESP日志前端接口](P030_STMESP日志前端接口.md) · [返回大纲](大纲.md)
