---
id: learning.zephyr-docs.stmesp-source-reference.page-1
title: STMESP日志前端头文件源码
kind: reference
status: maintained
domains: [zephyr, kernel, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/log__frontend__stmesp_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_STMESP日志前端头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/log__frontend__stmesp_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；相关页面见[头文件参考](../observability/P047_STMESP日志前端头文件.md)和[公共接口](../observability/P030_STMESP日志前端接口.md)；访问语义和生命周期见本页译注。

## 1.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="foldopen00065"></a>
<a id="foldopen00087"></a>
<a id="foldopen00126"></a>
<a id="foldopen00145"></a>
<a id="aerrno_8h_html"></a>
<a id="agroup__iterable__section__apis_html_ga40c6ba05d5bcb848a530bdc17bbff5be"></a>
<a id="agroup__log__frontend__stmesp_html_ga68b8bdb65457ffa2c0ab7c97b8414600"></a>
<a id="agroup__log__frontend__stmesp_html_ga7b9ad98fd11cbc6c28cc6b38307d52c6"></a>
<a id="agroup__log__frontend__stmesp_html_gab2b829f38108c54490090dcd97719cec"></a>
<a id="agroup__log__frontend__stmesp_html_gacb1274db685fbd6282868b03d3c627da"></a>
<a id="agroup__log__frontend__stmesp_html_gae222ceeee8aa370e3aaeb6eb8f1e1a8f"></a>
<a id="agroup__log__frontend__stmesp_html_gaf3052fc610038ca8b3c2b9488a98d54a"></a>
<a id="agroup__log__frontend__stmesp_html_gafdfa76ad219bd073b54825ae50cf13d3"></a>
<a id="agroup__stmsp__interface_html_ga2ffcc08b7d5c32c90b5d24982c0f6349"></a>
<a id="agroup__stmsp__interface_html_ga4350f5d201e3591221a932aa9fc3e94d"></a>
<a id="agroup__stmsp__interface_html_gaa7885c5a7620e46a532dbf405bfc6034"></a>
<a id="agroup__sys-util_html_ga111fe4e9d63758262fc6810a782cb32a"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astmesp_8h_html"></a>

<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * Copyright (c) 2024 Nordic Semiconductor ASA
<a id="l00003"></a> *
<a id="l00004"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00005"></a> */
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>#ifndef ZEPHYR_INCLUDE_LOGGING_LOG_FRONTEND_STMESP_H_
<a id="l00014"></a>#define ZEPHYR_INCLUDE_LOGGING_LOG_FRONTEND_STMESP_H_
<a id="l00015"></a>
<a id="l00016"></a>#include &lt;errno.h&gt;
<a id="l00017"></a>#include &lt;zephyr/types.h&gt;
<a id="l00018"></a>#ifdef CONFIG_LOG_FRONTEND_STMESP
<a id="l00019"></a>#include &lt;zephyr/drivers/debug/stmesp.h&gt;
<a id="l00020"></a>#endif
<a id="l00021"></a>
<a id="l00022"></a>#ifdef __cplusplus
<a id="l00023"></a>extern "C" {
<a id="l00024"></a>#endif
<a id="l00025"></a>
<a id="l00032"></a>
<a id="l00043"></a>int log_frontend_stmesp_etr_ready(void);
<a id="l00044"></a>
<a id="l00050"></a>void log_frontend_stmesp_pre_sleep(void);
<a id="l00051"></a>
<a id="l00056"></a>void log_frontend_stmesp_dummy_write(void);
<a id="l00057"></a>
<a id="l00065"></a>static inline void log_frontend_stmesp_tp(uint16_t x)
<a id="l00066"></a>{
<a id="l00067"></a>#ifdef CONFIG_LOG_FRONTEND_STMESP
<a id="l00068"></a>        STMESP_Type *port;
<a id="l00069"></a>        int err = stmesp_get_port((uint32_t)x + CONFIG_LOG_FRONTEND_STMESP_TP_CHAN_BASE, &amp;port);
<a id="l00070"></a>
<a id="l00071"></a>        __ASSERT_NO_MSG(err == 0);
<a id="l00072"></a>        if (err == 0) {
<a id="l00073"></a>                stmesp_flag(port, 1, true,
<a id="l00074"></a>                            IS_ENABLED(CONFIG_LOG_FRONTEND_STMESP_GUARANTEED_ACCESS));
<a id="l00075"></a>        }
<a id="l00076"></a>#endif
<a id="l00077"></a>}
<a id="l00078"></a>
<a id="l00087"></a>static inline void log_frontend_stmesp_tp_d32(uint16_t x, uint32_t d)
<a id="l00088"></a>{
<a id="l00089"></a>#ifdef CONFIG_LOG_FRONTEND_STMESP
<a id="l00090"></a>        STMESP_Type *port;
<a id="l00091"></a>        int err = stmesp_get_port((uint32_t)x + CONFIG_LOG_FRONTEND_STMESP_TP_CHAN_BASE, &amp;port);
<a id="l00092"></a>
<a id="l00093"></a>        __ASSERT_NO_MSG(err == 0);
<a id="l00094"></a>        if (err == 0) {
<a id="l00095"></a>                stmesp_data32(port, d, true, true,
<a id="l00096"></a>                              IS_ENABLED(CONFIG_LOG_FRONTEND_STMESP_GUARANTEED_ACCESS));
<a id="l00097"></a>        }
<a id="l00098"></a>#endif
<a id="l00099"></a>}
<a id="l00100"></a>
<a id="l00106"></a>void log_frontend_stmesp_log0(const void *source, uint32_t x);
<a id="l00107"></a>
<a id="l00114"></a>void log_frontend_stmesp_log1(const void *source, uint32_t x, uint32_t arg);
<a id="l00115"></a>
<a id="l00117"></a>TYPE_SECTION_START_EXTERN(const char *, log_stmesp_ptr);
<a id="l00119"></a>
<a id="l00125"></a>
<a id="l00126"></a>#define LOG_FRONTEND_STMESP_LOG0(_source, ...)                                                     \
<a id="l00127"></a>        do {                                                                                       \
<a id="l00128"></a>                static const char _str[] __in_section(_log_stmesp_str, static, __COUNTER__)        \
<a id="l00129"></a>                        IF_ENABLED(CONFIG_LOG_FRONTEND_STMESP_DICT, (__used))                      \
<a id="l00130"></a>                        __noasan __aligned(sizeof(uint32_t)) = GET_ARG_N(1, __VA_ARGS__);          \
<a id="l00131"></a>                static const char *str_ptr __in_section(_log_stmesp_ptr, static, __COUNTER__)      \
<a id="l00132"></a>                        IF_ENABLED(CONFIG_LOG_FRONTEND_STMESP_DICT, (__used))                      \
<a id="l00133"></a>                        __noasan = _str;                                                           \
<a id="l00134"></a>                uint32_t _idx =                                                                    \
<a id="l00135"></a>                        ((uintptr_t)&amp;str_ptr - (uintptr_t)TYPE_SECTION_START(log_stmesp_ptr)) /    \
<a id="l00136"></a>                        sizeof(void *);                                                            \
<a id="l00137"></a>                log_frontend_stmesp_log0(_source, _idx);                                           \
<a id="l00138"></a>        } while (0)
<a id="l00139"></a>
<a id="l00145"></a>#define LOG_FRONTEND_STMESP_LOG1(_source, ...)                                                     \
<a id="l00146"></a>        do {                                                                                       \
<a id="l00147"></a>                static const char _str[] __in_section(_log_stmesp_str, static, __COUNTER__)        \
<a id="l00148"></a>                        IF_ENABLED(CONFIG_LOG_FRONTEND_STMESP_DICT, (__used))                      \
<a id="l00149"></a>                        __noasan __aligned(sizeof(uint32_t)) = GET_ARG_N(1, __VA_ARGS__);          \
<a id="l00150"></a>                static const char *str_ptr __in_section(_log_stmesp_ptr, static, __COUNTER__)      \
<a id="l00151"></a>                        IF_ENABLED(CONFIG_LOG_FRONTEND_STMESP_DICT, (__used))                      \
<a id="l00152"></a>                        __noasan = _str;                                                           \
<a id="l00153"></a>                uint32_t _idx =                                                                    \
<a id="l00154"></a>                        ((uintptr_t)&amp;str_ptr - (uintptr_t)TYPE_SECTION_START(log_stmesp_ptr)) /    \
<a id="l00155"></a>                        sizeof(void *);                                                            \
<a id="l00156"></a>                log_frontend_stmesp_log1(_source, _idx, (uintptr_t)(GET_ARG_N(2, __VA_ARGS__)));   \
<a id="l00157"></a>        } while (0)
<a id="l00158"></a>
<a id="l00160"></a>
<a id="l00161"></a>#ifdef __cplusplus
<a id="l00162"></a>}
<a id="l00163"></a>#endif
<a id="l00164"></a>
<a id="l00165"></a>#endif /* ZEPHYR_INCLUDE_LOGGING_LOG_FRONTEND_STMESP_H_ */
</code></pre>

## 1.2\_可见注释译文（Comments）

1. 版权与许可证：Copyright (c) 2024 Nordic Semiconductor ASA；SPDX-License-Identifier: Apache-2.0。原始法律声明保留。

2. ZEPHYR_INCLUDE_LOGGING_LOG_FRONTEND_STMESP_H_头文件包含保护结束。

## 1.3\_原页符号提示（Symbol Descriptions）

### `errno.h`

系统错误编号（System Error Numbers）。

符号定位：[errno.h](../error_reference/P004_错误号头文件参考.md)。

### `TYPE_SECTION_START_EXTERN`

```c
#define TYPE_SECTION_START_EXTERN(type, secname)
```

为通用类型声明可遍历段（Iterable Section）的起始符号。

定义位置（Definition）：iterable_sections.h:86。

符号定位：[TYPE_SECTION_START_EXTERN](../iterable_reference/P001_可遍历段公共接口.md#ga40c6ba05d5bcb848a530bdc17bbff5be)。

### `log_frontend_stmesp_tp_d32`

```c
static void log_frontend_stmesp_tp_d32(uint16_t x, uint32_t d)
```

携带32位数据的跟踪点（Trace Point）。

定义位置（Definition）：log_frontend_stmesp.h:87。

符号定位：[log_frontend_stmesp_tp_d32](../observability/P030_STMESP日志前端接口.md#ga68b8bdb65457ffa2c0ab7c97b8414600)。

### `log_frontend_stmesp_log1`

```c
void log_frontend_stmesp_log1(const void *source, uint32_t x, uint32_t arg)
```

启用Turbo日志时，为带一个参数的日志消息调用的函数。

符号定位：[log_frontend_stmesp_log1](../observability/P030_STMESP日志前端接口.md#ga7b9ad98fd11cbc6c28cc6b38307d52c6)。

### `log_frontend_stmesp_tp`

```c
static void log_frontend_stmesp_tp(uint16_t x)
```

跟踪点（Trace Point）。

定义位置（Definition）：log_frontend_stmesp.h:65。

符号定位：[log_frontend_stmesp_tp](../observability/P030_STMESP日志前端接口.md#gab2b829f38108c54490090dcd97719cec)。

### `log_frontend_stmesp_dummy_write`

```c
void log_frontend_stmesp_dummy_write(void)
```

向STMESP执行虚写（Dummy Write）。

符号定位：[log_frontend_stmesp_dummy_write](../observability/P030_STMESP日志前端接口.md#gacb1274db685fbd6282868b03d3c627da)。

### `log_frontend_stmesp_pre_sleep`

```c
void log_frontend_stmesp_pre_sleep(void)
```

进入休眠前调用的钩子（Hook）。

符号定位：[log_frontend_stmesp_pre_sleep](../observability/P030_STMESP日志前端接口.md#gae222ceeee8aa370e3aaeb6eb8f1e1a8f)。

### `log_frontend_stmesp_log0`

```c
void log_frontend_stmesp_log0(const void *source, uint32_t x)
```

启用Turbo日志时，为无参数日志消息调用的函数。

符号定位：[log_frontend_stmesp_log0](../observability/P030_STMESP日志前端接口.md#gaf3052fc610038ca8b3c2b9488a98d54a)。

### `log_frontend_stmesp_etr_ready`

```c
int log_frontend_stmesp_etr_ready(void)
```

通知前端（Frontend）ETR/STM已就绪。

符号定位：[log_frontend_stmesp_etr_ready](../observability/P030_STMESP日志前端接口.md#gafdfa76ad219bd073b54825ae50cf13d3)。

### `stmesp_flag`

```c
static void stmesp_flag(STMESP_Type *reg, uint32_t data, bool ts, bool guaranteed)
```

向STMESP写入标志（Flag）。

定义位置（Definition）：stmesp.h:99。

符号定位：[stmesp_flag](../trace_interface_reference/P002_STMESP底层接口.md#ga2ffcc08b7d5c32c90b5d24982c0f6349)。

### `stmesp_get_port`

```c
static int stmesp_get_port(uint32_t idx, STMESP_Type **port)
```

返回系统跟踪宏单元扩展激励端口（STM Extended Stimulus Port）的地址。

定义位置（Definition）：stmesp.h:169。

符号定位：[stmesp_get_port](../trace_interface_reference/P002_STMESP底层接口.md#ga4350f5d201e3591221a932aa9fc3e94d)。

### `stmesp_data32`

```c
static void stmesp_data32(STMESP_Type *reg, uint32_t data, bool ts, bool marked, bool guaranteed)
```

向STMESP写入32位数据（32-bit Data）。

定义位置（Definition）：stmesp.h:152。

符号定位：[stmesp_data32](../trace_interface_reference/P002_STMESP底层接口.md#gaa7885c5a7620e46a532dbf405bfc6034)。

### `IS_ENABLED`

```c
#define IS_ENABLED(config_macro)
```

在编译器可见的表达式中检查宏定义。

定义位置（Definition）：util_macro.h:154。

符号定位：[IS_ENABLED](../util_reference/P001_通用工具公共接口.md#ga111fe4e9d63758262fc6810a782cb32a)。

### `types.h`

符号定位：[types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)。

### `uint32_t`

```c
__UINT32_TYPE__ uint32_t
```

定义位置（Definition）：stdint.h:90。

符号定位：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

### `uint16_t`

```c
__UINT16_TYPE__ uint16_t
```

定义位置（Definition）：stdint.h:89。

符号定位：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

### `stmesp.h`

符号定位：[stmesp.h](P003_STMESP底层头文件参考.md)。

## 1.4\_源码跟踪译注

> 译注——跟踪点（Trace Point）将x加上CONFIG_LOG_FRONTEND_STMESP_TP_CHAN_BASE作为端口编号。无数据版本写带时间戳的Flag，32位版本写带标记和时间戳的32位数据；未启用CONFIG_LOG_FRONTEND_STMESP时两个内联函数为空。

> 译注——Turbo日志将格式字符串放入_log_stmesp_str段，并通过_log_stmesp_ptr段中的指针位置计算索引。该索引依赖当前固件的链接布局，解码时需使用相匹配的格式信息，不应假定跨构建稳定。

> 译注——当前ETR就绪函数在存在早期缓冲（Early Buffer）时取得端口、排出已有消息并设置就绪状态。端口获取失败转为-EIO；它接受外部已完成硬件初始化的通知，不自行配置ETR。

> 译注——休眠前钩子（Pre-sleep Hook）仅在允许使用STM且存在新数据时，执行配置次数的虚写（Dummy Write）后清零新数据标志。源码没有在此等待主机确认，因此不能把此调用当作端到端接收确认。

头文件定位：[include/zephyr/logging/log_frontend_stmesp.h](../../../include/zephyr/logging/log_frontend_stmesp.h)，关联实现／接口：[subsys/logging/frontends/log_frontend_stmesp.c](../../../subsys/logging/frontends/log_frontend_stmesp.c)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/logging/log_frontend_stmesp.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/frontends/log_frontend_stmesp.c)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 1.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](../observability/P047_STMESP日志前端头文件.md)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/drivers/debug/stmesp.h](P003_STMESP底层头文件参考.md)
- [log_frontend_stmesp_etr_ready](../observability/P030_STMESP日志前端接口.md#gafdfa76ad219bd073b54825ae50cf13d3)
- [log_frontend_stmesp_pre_sleep](../observability/P030_STMESP日志前端接口.md#gae222ceeee8aa370e3aaeb6eb8f1e1a8f)
- [log_frontend_stmesp_dummy_write](../observability/P030_STMESP日志前端接口.md#gacb1274db685fbd6282868b03d3c627da)
- [log_frontend_stmesp_tp](../observability/P030_STMESP日志前端接口.md#gab2b829f38108c54490090dcd97719cec)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [stmesp_get_port](../trace_interface_reference/P002_STMESP底层接口.md#ga4350f5d201e3591221a932aa9fc3e94d)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [stmesp_flag](../trace_interface_reference/P002_STMESP底层接口.md#ga2ffcc08b7d5c32c90b5d24982c0f6349)
- [IS_ENABLED](../util_reference/P001_通用工具公共接口.md#ga111fe4e9d63758262fc6810a782cb32a)
- [log_frontend_stmesp_tp_d32](../observability/P030_STMESP日志前端接口.md#ga68b8bdb65457ffa2c0ab7c97b8414600)
- [stmesp_data32](../trace_interface_reference/P002_STMESP底层接口.md#gaa7885c5a7620e46a532dbf405bfc6034)
- [log_frontend_stmesp_log0](../observability/P030_STMESP日志前端接口.md#gaf3052fc610038ca8b3c2b9488a98d54a)
- [log_frontend_stmesp_log1](../observability/P030_STMESP日志前端接口.md#ga7b9ad98fd11cbc6c28cc6b38307d52c6)
- [TYPE_SECTION_START_EXTERN](../iterable_reference/P001_可遍历段公共接口.md#ga40c6ba05d5bcb848a530bdc17bbff5be)

---

[返回大纲](大纲.md) · [下一章](P002_STMESP日志解复用头文件源码.md)
