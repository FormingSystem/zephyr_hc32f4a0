---
id: learning.zephyr-docs.observability.obstruct-10
title: STMESP解复用配置
kind: reference
status: maintained
domains: [zephyr, observability]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structlog__frontend__stmesp__demux__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第43章\_STMESP解复用配置

原文：[structlog__frontend__stmesp__demux__config](https://docs.zephyrproject.org/latest/doxygen/html/structlog__frontend__stmesp__demux__config.html)。读取日期：2026-10-13，`latest`。

## 43.1\_类型与头文件

结构 [`log_frontend_stmesp_demux_config`](https://docs.zephyrproject.org/latest/doxygen/html/structlog__frontend__stmesp__demux__config.html) 保存解复用器配置（Demultiplexer Configuration）。它用于STM扩展激励端口（STM Extended Stimulus Port，STMESP）的日志解复用。

```c
#include <zephyr/logging/log_frontend_stmesp_demux.h>
```

## 43.2\_字段

位宽列为原文明确列出的位域（Bit-field）宽度；“—”表示本表未给位域宽度。

| 字段 | 类型 | 位宽 | 说明 |
| --- | --- | --- | --- |
| <a id="ada2f243b112324e99a53b831211cabce"></a>[`m_ids`](https://docs.zephyrproject.org/latest/doxygen/html/structlog__frontend__stmesp__demux__config.html#ada2f243b112324e99a53b831211cabce) | `const uint16_t *` | — | 预期主设备标识符（Major ID）的数组 |
| <a id="ad248eabec1eee58f5ef689004d5c7017"></a>[`m_ids_cnt`](https://docs.zephyrproject.org/latest/doxygen/html/structlog__frontend__stmesp__demux__config.html#ad248eabec1eee58f5ef689004d5c7017) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | — | 上述数组长度，不得大于 [`LOG_FRONTEND_STMESP_DEMUX_MAJOR_MAX`](https://docs.zephyrproject.org/latest/doxygen/html/group__log__frontend__stmesp__demux__apis.html#ga8f23994b914214a2c83d2e9aa63f0cb5) |
| <a id="aca85e1b671127e8803423f22b2d45a33"></a>[`source_id_buf`](https://docs.zephyrproject.org/latest/doxygen/html/structlog__frontend__stmesp__demux__config.html#aca85e1b671127e8803423f22b2d45a33) | `uint32_t *` | — | 保存源标识符（Source ID）的缓冲区，用于快速日志（Turbo Logging） |
| <a id="a643b5bd780342bf1944e5a63274aa305"></a>[`source_id_buf_len`](https://docs.zephyrproject.org/latest/doxygen/html/structlog__frontend__stmesp__demux__config.html#a643b5bd780342bf1944e5a63274aa305) | `size_t` | — | 缓冲区长度，必须是主设备标识符数量的整数倍 |

主设备数量上限宏及初始化函数见[STMESP日志解复用接口](P032_STMESP日志解复用接口.md)。

本文档由 `zephyr/logging/log_frontend_stmesp_demux.h` 生成。

---

[上一章：STMESP数据包联合体](P042_STMESP数据包联合体.md) · [下一章：插桩头文件](P044_插桩头文件.md) · [返回大纲](大纲.md)
