---
id: learning.zephyr-docs.observability.obheader-2
title: MIPI_STP解码头文件
kind: reference
status: maintained
domains: [zephyr, observability]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mipi__stp__decoder_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第46章\_MIPI_STP解码头文件

原文：[mipi__stp__decoder_8h](https://docs.zephyrproject.org/latest/doxygen/html/mipi__stp__decoder_8h.html)。读取日期：2026-10-13，`latest`。

## 46.1\_用途与包含关系

`zephyr/debug/mipi_stp_decoder.h` 是MIPI系统跟踪协议第2版（MIPI System Trace Protocol v2，STPv2）解码器的头文件参考。

官方页面列出的包含项如下：

```c
#include <zephyr/kernel.h>
```

[查看官方头文件源码](../trace_interface_reference/P003_MIPI_STP解码器头文件源码.md)。

## 46.2\_数据类型、宏与回调

| 项目 | 说明 |
| --- | --- |
| [`union mipi_stp_decoder_data`](P029_MIPI_STP解码数据.md) | 与给定STP操作码（Opcode）关联的数据联合体 |
| [`struct mipi_stp_decoder_config`](P028_MIPI_STP解码配置.md) | 解码器配置 |
| `STP_DECODER_TYPE2STR(_type)` | 将类型转换为字符串字面量（String Literal）的宏 |

回调（Callback）类型签名如下：

```c
typedef bool (*mipi_stp_decoder_cb)(enum mipi_stp_decoder_ctrl_type type,
                                  union mipi_stp_decoder_data data,
                                  uint64_t *ts, bool marked);
```

## 46.3\_操作码枚举

枚举 [`mipi_stp_decoder_ctrl_type`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__stp__decoder__apis.html#ga6e1f4b66b14ab44e549292f97046a50d) 定义STPv2操作码：

```c
enum mipi_stp_decoder_ctrl_type {
    STP_DATA4 = 1,
    STP_DATA8 = 2,
    STP_DATA16 = 4,
    STP_DATA32 = 8,
    STP_DATA64 = 16,
    STP_DECODER_NULL = 128,
    STP_DECODER_MAJOR,
    STP_DECODER_MERROR,
    STP_DECODER_CHANNEL,
    STP_DECODER_VERSION,
    STP_DECODER_FREQ,
    STP_DECODER_GERROR,
    STP_DECODER_FLAG,
    STP_DECODER_ASYNC,
    STP_DECODER_NOT_SUPPORTED
};
```

## 46.4\_函数声明

以下声明与官方头文件参考页对应，完整参数和返回值见[对应接口说明](P027_MIPI_STP解码接口.md)。

| 声明 | 说明 |
| --- | --- |
| `int mipi_stp_decoder_init(const struct mipi_stp_decoder_config *config);` | 初始化解码器 |
| `int mipi_stp_decoder_decode(const uint8_t *data, size_t len);` | 解码STPv2流 |
| `void mipi_stp_decoder_sync_loss(void);` | 通知同步丢失 |

---

[上一章：CoreSight解格式头文件](P045_CoreSight解格式头文件.md) · [下一章：STMESP日志前端头文件](P047_STMESP日志前端头文件.md) · [返回大纲](大纲.md)
