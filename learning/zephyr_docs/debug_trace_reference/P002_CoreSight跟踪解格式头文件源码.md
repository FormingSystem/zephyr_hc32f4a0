---
id: learning.zephyr-docs.debug-trace-reference.page-2
title: CoreSight跟踪解格式头文件源码
kind: reference
status: maintained
domains: [zephyr, kernel, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/cs__trace__defmt_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_CoreSight跟踪解格式头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/cs__trace__defmt_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；相关页面见[头文件参考](../observability/P045_CoreSight解格式头文件.md)和[公共接口](../observability/P026_CoreSight解格式接口.md)；访问语义和生命周期见本页译注。

## 2.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="agroup__cs__trace__defmt_html_ga109bab752da74692779aa3eb96b771ba"></a>
<a id="agroup__cs__trace__defmt_html_gaaeaaefe2221161691144d82c932196ca"></a>
<a id="agroup__cs__trace__defmt_html_gaccc05f92bfbc04b787f6f959e954115d"></a>
<a id="akernel_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>

<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * Copyright (c) 2024 Nordic Semiconductor ASA.
<a id="l00003"></a> *
<a id="l00004"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00005"></a> */
<a id="l00006"></a>
<a id="l00007"></a>#ifndef ZEPHYR_INCLUDE_DEBUG_CORESIGHT_CS_TRACE_DEFMT_H__
<a id="l00008"></a>#define ZEPHYR_INCLUDE_DEBUG_CORESIGHT_CS_TRACE_DEFMT_H__
<a id="l00009"></a>
<a id="l00010"></a>#include &lt;zephyr/kernel.h&gt;
<a id="l00011"></a>#ifdef __cplusplus
<a id="l00012"></a>extern "C" {
<a id="l00013"></a>#endif
<a id="l00014"></a>
<a id="l00024"></a>
<a id="l00031"></a>typedef void (*cs_trace_defmt_cb)(uint32_t id, const uint8_t *data, size_t len);
<a id="l00032"></a>
<a id="l00034"></a>#define CORESIGHT_TRACE_FRAME_SIZE32 4
<a id="l00035"></a>
<a id="l00037"></a>#define CORESIGHT_TRACE_FRAME_SIZE (CORESIGHT_TRACE_FRAME_SIZE32 * sizeof(uint32_t))
<a id="l00038"></a>
<a id="l00043"></a>int cs_trace_defmt_init(cs_trace_defmt_cb cb);
<a id="l00044"></a>
<a id="l00057"></a>int cs_trace_defmt_process(const uint8_t *data, size_t len);
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00061"></a>#ifdef __cplusplus
<a id="l00062"></a>}
<a id="l00063"></a>#endif
<a id="l00064"></a>
<a id="l00065"></a>#endif /* ZEPHYR_INCLUDE_DEBUG_CORESIGHT_CS_TRACE_DEFMT_H__ */
</code></pre>

## 2.2\_可见注释译文（Comments）

1. 版权与许可证：Copyright (c) 2024 Nordic Semiconductor ASA.；SPDX-License-Identifier: Apache-2.0。原始法律声明保留。

2. ZEPHYR_INCLUDE_DEBUG_CORESIGHT_CS_TRACE_DEFMT_H__头文件包含保护结束。

## 2.3\_原页符号提示（Symbol Descriptions）

### `cs_trace_defmt_process`

```c
int cs_trace_defmt_process(const uint8_t *data, size_t len)
```

解码流（Stream）中的数据。

符号定位：[cs_trace_defmt_process](../observability/P026_CoreSight解格式接口.md#ga109bab752da74692779aa3eb96b771ba)。

### `cs_trace_defmt_init`

```c
int cs_trace_defmt_init(cs_trace_defmt_cb cb)
```

初始化CoreSight跟踪解格式器（Trace Deformatter）。

符号定位：[cs_trace_defmt_init](../observability/P026_CoreSight解格式接口.md#gaaeaaefe2221161691144d82c932196ca)。

### `cs_trace_defmt_cb`

```c
void(* cs_trace_defmt_cb)(uint32_t id, const uint8_t *data, size_t len)
```

回调函数签名（Callback Signature）。

定义位置（Definition）：cs_trace_defmt.h:31。

符号定位：[cs_trace_defmt_cb](../observability/P026_CoreSight解格式接口.md#gaccc05f92bfbc04b787f6f959e954115d)。

### `kernel.h`

公共内核 API（Public Kernel APIs）。

符号定位：[kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)。

### `uint32_t`

```c
__UINT32_TYPE__ uint32_t
```

定义位置（Definition）：stdint.h:90。

符号定位：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

### `uint8_t`

```c
__UINT8_TYPE__ uint8_t
```

定义位置（Definition）：stdint.h:88。

符号定位：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

## 2.4\_源码跟踪译注

> 译注——CoreSight跟踪解格式器（Trace Deformatter）处理格式化帧，将流编号（Stream ID）和分离后的数据交给回调。当前process要求输入恰好16字节，否则返回-EINVAL；这不是接收任意长度输入并自行拼接帧的接口。

> 译注——CORESIGHT_TRACE_FRAME_SIZE32以32位字计量，值为4；CORESIGHT_TRACE_FRAME_SIZE以字节计量，等于16。调用process的长度单位是字节。

> 译注——当前实现将输出暂存在函数栈上的15字节数组，并同步调用注册回调。回调如需在返回后继续处理数据，必须自行保存内容，不能长期持有该data指针。

> 译注——实现使用全局callback和当前流编号curr_id。init只替换回调，不重置curr_id；再次初始化不能当作清空所有流状态。调用方需按所使用的数据流和回调生命周期管理它。

头文件定位：[include/zephyr/debug/coresight/cs_trace_defmt.h](../../../include/zephyr/debug/coresight/cs_trace_defmt.h)，关联实现／接口：[subsys/debug/coresight/cs_trace_defmt.c](../../../subsys/debug/coresight/cs_trace_defmt.c)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/debug/coresight/cs_trace_defmt.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/coresight/cs_trace_defmt.c)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 2.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](../observability/P045_CoreSight解格式头文件.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [cs_trace_defmt_cb](../observability/P026_CoreSight解格式接口.md#gaccc05f92bfbc04b787f6f959e954115d)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [cs_trace_defmt_init](../observability/P026_CoreSight解格式接口.md#gaaeaaefe2221161691144d82c932196ca)
- [cs_trace_defmt_process](../observability/P026_CoreSight解格式接口.md#ga109bab752da74692779aa3eb96b771ba)

---

[上一章](P001_调试接口目录.md) · [返回大纲](大纲.md) · [下一章](P003_Nordic_ETR调试头文件参考.md)
