---
id: learning.zephyr-docs.shell-backend-reference.page-14
title: Shell日志后端头文件源码
kind: reference
status: maintained
domains: [zephyr, kernel, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/shell__log__backend_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_Shell日志后端头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/shell__log__backend_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；相关页面见[头文件参考](P013_Shell日志后端头文件参考.md)和[公共接口](P013_Shell日志后端头文件参考.md)；访问语义和生命周期见本页译注。

## 14.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="aatomic_8h_html"></a>
<a id="agroup__atomic__apis_html_ga124f07c3a788e53c3a40e4e1c06d8af8"></a>
<a id="akernel_8h_html"></a>
<a id="alog__backend_8h_html"></a>
<a id="alog__output_8h_html"></a>
<a id="ampsc__pbuf_8h_html"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructlog__backend__api_html"></a>

<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * Copyright (c) 2018 Nordic Semiconductor ASA
<a id="l00003"></a> *
<a id="l00004"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00005"></a> */
<a id="l00006"></a>
<a id="l00011"></a>
<a id="l00012"></a>#ifndef ZEPHYR_INCLUDE_SHELL_SHELL_LOG_BACKEND_H_
<a id="l00013"></a>#define ZEPHYR_INCLUDE_SHELL_SHELL_LOG_BACKEND_H_
<a id="l00014"></a>
<a id="l00015"></a>#include &lt;zephyr/kernel.h&gt;
<a id="l00016"></a>#include &lt;zephyr/logging/log_backend.h&gt;
<a id="l00017"></a>#include &lt;zephyr/logging/log_output.h&gt;
<a id="l00018"></a>#include &lt;zephyr/sys/mpsc_pbuf.h&gt;
<a id="l00019"></a>#include &lt;zephyr/sys/atomic.h&gt;
<a id="l00020"></a>#ifdef __cplusplus
<a id="l00021"></a>extern "C" {
<a id="l00022"></a>#endif
<a id="l00023"></a>
<a id="l00025"></a>extern const struct log_backend_api log_backend_shell_api;
<a id="l00026"></a>
<a id="l00028"></a>enum shell_log_backend_state {
<a id="l00029"></a>        SHELL_LOG_BACKEND_UNINIT,
<a id="l00030"></a>        SHELL_LOG_BACKEND_ENABLED,
<a id="l00031"></a>        SHELL_LOG_BACKEND_DISABLED,
<a id="l00032"></a>        SHELL_LOG_BACKEND_PANIC,
<a id="l00033"></a>};
<a id="l00034"></a>
<a id="l00036"></a>struct shell_log_backend_control_block {
<a id="l00037"></a>        atomic_t dropped_cnt;
<a id="l00038"></a>        enum shell_log_backend_state state;
<a id="l00039"></a>};
<a id="l00040"></a>
<a id="l00042"></a>struct shell_log_backend {
<a id="l00043"></a>        const struct log_backend *backend;
<a id="l00044"></a>        const struct log_output *log_output;
<a id="l00045"></a>        struct shell_log_backend_control_block *control_block;
<a id="l00046"></a>        uint32_t timeout;
<a id="l00047"></a>        const struct mpsc_pbuf_buffer_config *mpsc_buffer_config;
<a id="l00048"></a>        struct mpsc_pbuf_buffer *mpsc_buffer;
<a id="l00049"></a>};
<a id="l00050"></a>
<a id="l00052"></a>struct shell_log_backend_msg {
<a id="l00053"></a>        struct log_msg *msg;
<a id="l00054"></a>        uint32_t timestamp;
<a id="l00055"></a>};
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00060"></a>int z_shell_log_backend_output_func(uint8_t *data, size_t length, void *ctx);
<a id="l00061"></a>
<a id="l00077"></a>#ifdef CONFIG_SHELL_LOG_BACKEND
<a id="l00078"></a>#define Z_SHELL_LOG_BACKEND_DEFINE(_name, _buf, _size, _queue_size, _timeout) \
<a id="l00079"></a>        LOG_BACKEND_DEFINE(_name##_backend, log_backend_shell_api, false); \
<a id="l00080"></a>        LOG_OUTPUT_DEFINE(_name##_log_output, z_shell_log_backend_output_func,\
<a id="l00081"></a>                          _buf, _size); \
<a id="l00082"></a>        static struct shell_log_backend_control_block _name##_control_block; \
<a id="l00083"></a>        static uint32_t __aligned(Z_LOG_MSG_ALIGNMENT) \
<a id="l00084"></a>                        _name##_buf[(_queue_size) / sizeof(uint32_t)]; \
<a id="l00085"></a>        const struct mpsc_pbuf_buffer_config _name##_mpsc_buffer_config = { \
<a id="l00086"></a>                .buf = _name##_buf, \
<a id="l00087"></a>                .size = ARRAY_SIZE(_name##_buf), \
<a id="l00088"></a>                .notify_drop = NULL, \
<a id="l00089"></a>                .get_wlen = log_msg_generic_get_wlen, \
<a id="l00090"></a>                .flags = MPSC_PBUF_MODE_OVERWRITE, \
<a id="l00091"></a>        }; \
<a id="l00092"></a>        struct mpsc_pbuf_buffer _name##_mpsc_buffer; \
<a id="l00093"></a>        static const struct shell_log_backend _name##_log_backend = { \
<a id="l00094"></a>                .backend = &amp;_name##_backend, \
<a id="l00095"></a>                .log_output = &amp;_name##_log_output, \
<a id="l00096"></a>                .control_block = &amp;_name##_control_block, \
<a id="l00097"></a>                .timeout = _timeout, \
<a id="l00098"></a>                .mpsc_buffer_config = &amp;_name##_mpsc_buffer_config, \
<a id="l00099"></a>                .mpsc_buffer = &amp;_name##_mpsc_buffer, \
<a id="l00100"></a>        }
<a id="l00101"></a>
<a id="l00102"></a>#define Z_SHELL_LOG_BACKEND_PTR(_name) (&amp;_name##_log_backend)
<a id="l00103"></a>#else /* CONFIG_LOG */
<a id="l00104"></a>#define Z_SHELL_LOG_BACKEND_DEFINE(_name, _buf, _size, _queue_size, _timeout)
<a id="l00105"></a>#define Z_SHELL_LOG_BACKEND_PTR(_name) NULL
<a id="l00106"></a>#endif /* CONFIG_LOG */
<a id="l00107"></a>
<a id="l00114"></a>void z_shell_log_backend_enable(const struct shell_log_backend *backend,
<a id="l00115"></a>                                void *ctx, uint32_t init_log_level);
<a id="l00116"></a>
<a id="l00121"></a>void z_shell_log_backend_disable(const struct shell_log_backend *backend);
<a id="l00122"></a>
<a id="l00129"></a>bool z_shell_log_backend_process(const struct shell_log_backend *backend);
<a id="l00130"></a>
<a id="l00131"></a>#ifdef __cplusplus
<a id="l00132"></a>}
<a id="l00133"></a>#endif
<a id="l00134"></a>
<a id="l00135"></a>#endif /* ZEPHYR_INCLUDE_SHELL_SHELL_LOG_BACKEND_H_ */
</code></pre>

## 14.2\_可见注释译文（Comments）

1. 版权与许可证：Copyright (c) 2018 Nordic Semiconductor ASA；SPDX-License-Identifier: Apache-2.0。原始法律声明保留。

2. 原分支注释为CONFIG_LOG，实际对应CONFIG_SHELL_LOG_BACKEND条件的else分支。

3. 原结束注释为CONFIG_LOG，实际对应CONFIG_SHELL_LOG_BACKEND条件结束。

4. ZEPHYR_INCLUDE_SHELL_SHELL_LOG_BACKEND_H_头文件包含保护结束。

## 14.3\_原页符号提示（Symbol Descriptions）

### `atomic.h`

原子操作（Atomic Operations）API的头文件。

符号定位：[atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)。

### `atomic_t`

```c
long atomic_t
```

原子整型变量（Atomic Integer Variable）。

定义位置（Definition）：atomic_types.h:34。

符号定位：[atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)。

### `kernel.h`

公共内核 API（Public Kernel APIs）。

符号定位：[kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)。

### `log_backend.h`

日志后端接口（Logging Backend Interface）的头文件。

符号定位：[log_backend.h](../log_backend_reference/P002_日志后端头文件参考.md)。

### `log_output.h`

日志输出格式化器（Log Output Formatter）的头文件。

符号定位：[log_output.h](../log_output_reference/P002_日志输出头文件参考.md)。

### `mpsc_pbuf.h`

符号定位：[mpsc_pbuf.h](../intercore_reference/P170_MPSC数据包缓冲区头文件参考.md)。

### `state`

```c
state
```

定义位置（Definition）：parser_state.h:29。

符号定位：[state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)。

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

### `log_backend_api`

日志记录器后端API（Logger Backend API）。

定义位置（Definition）：log_backend.h:74。

符号定位：[log_backend_api](../log_backend_reference/P005_日志后端操作表.md)。

## 14.4\_源码跟踪译注

> 译注——此头文件参考页只公开文件说明和源码入口；源码浏览页还显示内部结构、状态枚举和z_shell_*声明。这里完整保留可见代码，但不把隐藏在Doxygen内部条件中的条目补造为公共API契约。

> 译注——日志队列宏用_queue_size除以sizeof(uint32_t)定义数组，再以数组元素个数配置MPSC缓冲。队列大小参数和MPSC字数的单位不同；实际容量受除法取整及消息对齐影响。

> 译注——条件编译实际检查CONFIG_SHELL_LOG_BACKEND。原代码两个分支注释写作CONFIG_LOG，译文保留其原名并在此区分，不能据注释反推编译开关。

头文件定位：[include/zephyr/shell/shell_log_backend.h](../../../include/zephyr/shell/shell_log_backend.h)，关联实现／接口：[subsys/shell/shell_log_backend.c](../../../subsys/shell/shell_log_backend.c)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/shell/shell_log_backend.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/shell_log_backend.c)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 14.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P013_Shell日志后端头文件参考.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/logging/log_backend.h](../log_backend_reference/P002_日志后端头文件参考.md)
- [zephyr/logging/log_output.h](../log_output_reference/P002_日志输出头文件参考.md)
- [zephyr/sys/mpsc_pbuf.h](../intercore_reference/P170_MPSC数据包缓冲区头文件参考.md)
- [zephyr/sys/atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)
- [log_backend_api](../log_backend_reference/P005_日志后端操作表.md)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

---

[上一章](P013_Shell日志后端头文件参考.md) · [返回大纲](大纲.md)
