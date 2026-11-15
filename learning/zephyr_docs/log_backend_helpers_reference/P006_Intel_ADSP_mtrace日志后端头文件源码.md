---
id: learning.zephyr-docs.log-backend-helpers-reference.page-6
title: Intel_ADSP_mtrace日志后端头文件源码
kind: reference
status: maintained
domains: [zephyr, kernel, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/log__backend__adsp__mtrace_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_Intel\_ADSP\_mtrace日志后端头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/log__backend__adsp__mtrace_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；完整接口说明见[头文件参考](P005_Intel_ADSP_mtrace日志后端头文件参考.md)和[公共API](P004_Intel_ADSP_mtrace日志后端接口.md)。

## 6.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="agroup__log__backend__adsp__mtrace_html_ga9bb9152344270b8257182471443caa78"></a>
<a id="agroup__log__backend__adsp__mtrace_html_gab6362dba4defcd461d24a155763b465d"></a>
<a id="agroup__log__backend__adsp__mtrace_html_gaecd49115065234a120c75f450b799269"></a>
<a id="astdint_8h_html"></a>
<a id="astructlog__backend_html"></a>

<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * Copyright (c) 2022 Intel Corporation
<a id="l00003"></a> *
<a id="l00004"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00005"></a> */
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>#ifndef ZEPHYR_INCLUDE_LOGGING_LOG_BACKEND_ADSP_MTRACE_H_
<a id="l00014"></a>#define ZEPHYR_INCLUDE_LOGGING_LOG_BACKEND_ADSP_MTRACE_H_
<a id="l00015"></a>
<a id="l00022"></a>
<a id="l00023"></a>#include &lt;stdint.h&gt;
<a id="l00024"></a>#include &lt;stddef.h&gt;
<a id="l00025"></a>
<a id="l00033"></a>typedef void(*adsp_mtrace_log_hook_t)(size_t written, size_t space_left);
<a id="l00034"></a>
<a id="l00041"></a>void adsp_mtrace_log_init(adsp_mtrace_log_hook_t hook);
<a id="l00042"></a>
<a id="l00048"></a>const struct log_backend *log_backend_adsp_mtrace_get(void);
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00052"></a>#endif /* ZEPHYR_INCLUDE_LOGGING_LOG_BACKEND_ADSP_MTRACE_H_ */
</code></pre>

## 6.2\_可见注释译文（Comments）

1. 版权与许可证：Copyright (c) 2022 Intel Corporation；SPDX-License-Identifier: Apache-2.0。原始法律声明保留。

2. ZEPHYR_INCLUDE_LOGGING_LOG_BACKEND_ADSP_MTRACE_H_头文件包含保护结束。

## 6.3\_原页符号提示（Symbol Descriptions）

### `adsp_mtrace_log_init`

```c
void adsp_mtrace_log_init(adsp_mtrace_log_hook_t hook)
```

初始化Intel ADSP mtrace日志记录器。

符号定位：[adsp_mtrace_log_init](P004_Intel_ADSP_mtrace日志后端接口.md#ga9bb9152344270b8257182471443caa78)。

### `adsp_mtrace_log_hook_t`

```c
void(* adsp_mtrace_log_hook_t)(size_t written, size_t space_left)
```

mtrace日志记录器需要一个用于IPC消息的钩子（Hook）。

定义位置（Definition）：log_backend_adsp_mtrace.h:33。

符号定位：[adsp_mtrace_log_hook_t](P004_Intel_ADSP_mtrace日志后端接口.md#gab6362dba4defcd461d24a155763b465d)。

### `log_backend_adsp_mtrace_get`

```c
const struct log_backend * log_backend_adsp_mtrace_get(void)
```

取得Intel ADSP mtrace日志后端。

符号定位：[log_backend_adsp_mtrace_get](P004_Intel_ADSP_mtrace日志后端接口.md#gaecd49115065234a120c75f450b799269)。

### `stdint.h`

符号定位：[stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)。

### `log_backend`

日志后端结构（Logger Backend Structure）。

定义位置（Definition）：log_backend.h:118。

符号定位：[log_backend](../log_backend_reference/P004_日志后端结构.md)。

## 6.4\_源码跟踪译注

> 译注——mtrace把日志写入SRAM缓冲区，再由钩子通知主机；它与HDA的DMA流接口不同，初始化参数和回调声明应分别使用。

> 译注——本次实现的adsp_mtrace_log_init初始化mtrace状态、保存钩子，并根据钩子是否非NULL设置mtrace_active。向get接口取得后端指针本身不会安装回调或替主机读取数据。

> 译注——当前输出路径把本次写入量与剩余空间传给钩子；panic模式会将传给钩子的space_left改为0以促使尽快处理，因此此时该参数不能直接作为实际剩余容量测量值。缓冲与通知并不保证主机已完成日志持久保存。

头文件定位：[include/zephyr/logging/log_backend_adsp_mtrace.h](../../../include/zephyr/logging/log_backend_adsp_mtrace.h)，关联实现／接口：[subsys/logging/backends/log_backend_adsp_mtrace.c](../../../subsys/logging/backends/log_backend_adsp_mtrace.c)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/logging/log_backend_adsp_mtrace.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/log_backend_adsp_mtrace.c)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 6.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P005_Intel_ADSP_mtrace日志后端头文件参考.md)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [adsp_mtrace_log_hook_t](P004_Intel_ADSP_mtrace日志后端接口.md#gab6362dba4defcd461d24a155763b465d)
- [adsp_mtrace_log_init](P004_Intel_ADSP_mtrace日志后端接口.md#ga9bb9152344270b8257182471443caa78)
- [log_backend](../log_backend_reference/P004_日志后端结构.md)
- [log_backend_adsp_mtrace_get](P004_Intel_ADSP_mtrace日志后端接口.md#gaecd49115065234a120c75f450b799269)

---

[上一章](P005_Intel_ADSP_mtrace日志后端头文件参考.md) · [返回大纲](大纲.md) · [下一章](P007_标准日志后端辅助接口.md)
