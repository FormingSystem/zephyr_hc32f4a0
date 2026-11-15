---
id: learning.zephyr-docs.observability.obapi-5
title: STMESP日志前端接口
kind: reference
status: maintained
domains: [zephyr, observability]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__log__frontend__stmesp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第30章\_STMESP日志前端接口

原文：[group__log__frontend__stmesp](https://docs.zephyrproject.org/latest/doxygen/html/group__log__frontend__stmesp.html)。读取日期：2026-10-13，`latest`。

## 30.1\_用途与头文件

该日志前端（Logging Frontend）通过**系统跟踪宏单元（System Trace Macrocell，STM）**的**扩展激励端口（STM Extended Stimulus Port，STMESP）**输出日志消息和跟踪点（Trace Point）。

```c
#include <zephyr/logging/log_frontend_stmesp.h>
```

## 30.2\_快速日志宏

**快速日志（Turbo Logging）**宏处理不带格式化参数或仅带一个数值参数的日志。下方保留的实现使用 `CONFIG_LOG_FRONTEND_STMESP_DICT` 字典模式配置；`IF_ENABLED` 宏按配置选择内容，`GET_ARG_N` 宏取指定位置的参数，`TYPE_SECTION_START` 宏取得类型段起址。

宏 `LOG_FRONTEND_STMESP_LOG0(_source, ...)` 处理无参数日志；`_source` 指向日志源结构，可变参数 `...` 提供字符串。官方宏值如下：

```c
do {                                                                                       \
        static const char _str[] __in_section(_log_stmesp_str, static, __COUNTER__)        \
                IF_ENABLED(CONFIG_LOG_FRONTEND_STMESP_DICT, (__used))                      \
                __noasan __aligned(sizeof(uint32_t)) = GET_ARG_N(1, __VA_ARGS__);          \
        static const char *str_ptr __in_section(_log_stmesp_ptr, static, __COUNTER__)      \
                IF_ENABLED(CONFIG_LOG_FRONTEND_STMESP_DICT, (__used))                      \
                __noasan = _str;                                                           \
        uint32_t _idx =                                                                    \
                ((uintptr_t)&str_ptr - (uintptr_t)TYPE_SECTION_START(log_stmesp_ptr)) /    \
                sizeof(void *);                                                            \
        log_frontend_stmesp_log0(_source, _idx);                                           \
} while (0)
```

宏 `LOG_FRONTEND_STMESP_LOG1(_source, ...)` 处理单参数日志；`_source` 同样指向日志源结构，`...` 提供字符串及一个数值参数。官方宏值如下：

```c
do {                                                                                       \
        static const char _str[] __in_section(_log_stmesp_str, static, __COUNTER__)        \
                IF_ENABLED(CONFIG_LOG_FRONTEND_STMESP_DICT, (__used))                      \
                __noasan __aligned(sizeof(uint32_t)) = GET_ARG_N(1, __VA_ARGS__);          \
        static const char *str_ptr __in_section(_log_stmesp_ptr, static, __COUNTER__)      \
                IF_ENABLED(CONFIG_LOG_FRONTEND_STMESP_DICT, (__used))                      \
                __noasan = _str;                                                           \
        uint32_t _idx =                                                                    \
                ((uintptr_t)&str_ptr - (uintptr_t)TYPE_SECTION_START(log_stmesp_ptr)) /    \
                sizeof(void *);                                                            \
        log_frontend_stmesp_log1(_source, _idx, (uintptr_t)(GET_ARG_N(2, __VA_ARGS__)));   \
} while (0)
```

## 30.3\_就绪通知

<a id="gafdfa76ad219bd073b54825ae50cf13d3"></a>

```c
int log_frontend_stmesp_etr_ready(void);
```

通知前端**嵌入式跟踪路由器（Embedded Trace Router，ETR）**及 STM 已就绪。日志前端可按配置导出已有缓冲数据，然后开始写入 STM 激励端口。

**该函数只适用于负责首次配置 ETR/STM 的域（Domain）。**成功返回 `0`；内部失败返回 `-EIO`。

## 30.4\_睡眠前刷新与空写入

<a id="gae222ceeee8aa370e3aaeb6eb8f1e1a8f"></a>

<a id="gacb1274db685fbd6282868b03d3c627da"></a>

```c
void log_frontend_stmesp_pre_sleep(void);
void log_frontend_stmesp_dummy_write(void);
```

[`log_frontend_stmesp_pre_sleep()`](https://docs.zephyrproject.org/latest/doxygen/html/group__log__frontend__stmesp.html#gae222ceeee8aa370e3aaeb6eb8f1e1a8f) 是进入睡眠前应调用的钩子（Hook）。它向 STM 激励端口写入占位数据，确保全部日志数据已刷新输出。

[`log_frontend_stmesp_dummy_write()`](https://docs.zephyrproject.org/latest/doxygen/html/group__log__frontend__stmesp.html#gacb1274db685fbd6282868b03d3c627da) 对 STMESP 执行一次空写入（Dummy Write），可用于强制刷新 STM 数据。

## 30.5\_跟踪点

下列两个函数在头文件中为静态内联函数（Static Inline Function）：

<a id="gab2b829f38108c54490090dcd97719cec"></a>

<a id="ga68b8bdb65457ffa2c0ab7c97b8414600"></a>

```c
static inline void log_frontend_stmesp_tp(uint16_t x);
static inline void log_frontend_stmesp_tp_d32(uint16_t x, uint32_t d);
```

两者均使用 STM 写入跟踪点信息。`x` 是跟踪点标识符（Identifier，ID）。第二个函数额外携带参数 `d`，即一个32位数据字。

本应用程序编程接口（Application Programming Interface，API）页规定：**每个核心的不同跟踪点数量上限为 `32768 - CONFIG_LOG_FRONTEND_STMESP_TP_CHAN_BASE`**。

> 译注：[系统跟踪日志指南](P012_CoreSight系统跟踪日志.md)另将索引范围写为0～65280，与本页的数量约束并不相同。两处原值均保留；实际使用应核对所用版本头文件和 `CONFIG_LOG_FRONTEND_STMESP_TP_CHAN_BASE` 配置，不能直接把指南中的范围当成本API无条件支持的索引范围。

## 30.6\_快速日志函数

启用快速日志时，以下函数分别用于无参数日志与单参数日志：

<a id="gaf3052fc610038ca8b3c2b9488a98d54a"></a>

<a id="ga7b9ad98fd11cbc6c28cc6b38307d52c6"></a>

```c
void log_frontend_stmesp_log0(const void *source, uint32_t x);
void log_frontend_stmesp_log1(const void *source, uint32_t x, uint32_t arg);
```

| 参数 | 含义 |
| --- | --- |
| `source` | 日志源结构指针 |
| `x` | 日志消息使用的字符串索引 |
| `arg` | 单参数版本携带的参数 |

---

[上一章：MIPI_STP解码数据](P029_MIPI_STP解码数据.md) · [下一章：STMESP日志接口目录](P031_STMESP日志接口目录.md) · [返回大纲](大纲.md)
