---
id: learning.zephyr-docs.shell-util-reference.page-4
title: Shell命令历史头文件源码
kind: reference
status: maintained
domains: [zephyr, kernel, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/shell__history_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_Shell命令历史头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/shell__history_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；相关页面见[头文件参考](P003_Shell命令历史头文件参考.md)和[公共接口](P003_Shell命令历史头文件参考.md)；访问语义和生命周期见本页译注。

## 4.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="adlist_8h_html"></a>
<a id="agroup__doubly-linked-list__apis_html_ga57fdb936802a617d16c00ab08cd2ad98"></a>
<a id="agroup__doubly-linked-list__apis_html_gaa03f9557215b486fee1039dd4c07e683"></a>
<a id="akernel_8h_html"></a>
<a id="aring__buffer_8h_html"></a>
<a id="astdbool_8h_html"></a>
<a id="astdbool_8h_html_a41f9c5fb8b08eb5dc3edce4dcb37fee7"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="asys_2util_8h_html"></a>

<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * Copyright (c) 2018 Nordic Semiconductor ASA
<a id="l00003"></a> *
<a id="l00004"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00005"></a> */
<a id="l00006"></a>
<a id="l00011"></a>
<a id="l00012"></a>#ifndef ZEPHYR_INCLUDE_SHELL_SHELL_HISTORY_H_
<a id="l00013"></a>#define ZEPHYR_INCLUDE_SHELL_SHELL_HISTORY_H_
<a id="l00014"></a>
<a id="l00015"></a>#include &lt;zephyr/kernel.h&gt;
<a id="l00016"></a>#include &lt;zephyr/sys/util.h&gt;
<a id="l00017"></a>#include &lt;zephyr/sys/dlist.h&gt;
<a id="l00018"></a>#include &lt;zephyr/sys/ring_buffer.h&gt;
<a id="l00019"></a>#include &lt;stdbool.h&gt;
<a id="l00020"></a>
<a id="l00021"></a>#ifdef __cplusplus
<a id="l00022"></a>extern "C" {
<a id="l00023"></a>#endif
<a id="l00024"></a>
<a id="l00026"></a>struct shell_history {
<a id="l00027"></a>        struct k_heap *heap;
<a id="l00028"></a>        sys_dlist_t list;
<a id="l00029"></a>        sys_dnode_t *current;
<a id="l00030"></a>};
<a id="l00032"></a>
<a id="l00039"></a>#define Z_SHELL_HISTORY_DEFINE(_name, _size)                    \
<a id="l00040"></a>        K_HEAP_DEFINE(_name##_heap, _size);                     \
<a id="l00041"></a>        static struct shell_history _name = {                   \
<a id="l00042"></a>                .heap = &amp;_name##_heap,                          \
<a id="l00043"></a>                .list = SYS_DLIST_STATIC_INIT(&amp;_name.list),     \
<a id="l00044"></a>        }
<a id="l00045"></a>
<a id="l00054"></a>void z_shell_history_purge(struct shell_history *history);
<a id="l00055"></a>
<a id="l00061"></a>void z_shell_history_mode_exit(struct shell_history *history);
<a id="l00062"></a>
<a id="l00075"></a>bool z_shell_history_get(struct shell_history *history, bool up,
<a id="l00076"></a>                         uint8_t *dst, uint16_t *len);
<a id="l00077"></a>
<a id="l00088"></a>void z_shell_history_put(struct shell_history *history, uint8_t *line,
<a id="l00089"></a>                         size_t len);
<a id="l00090"></a>
<a id="l00098"></a>static inline bool z_shell_history_active(struct shell_history *history)
<a id="l00099"></a>{
<a id="l00100"></a>        return (history-&gt;current) ? true : false;
<a id="l00101"></a>}
<a id="l00102"></a>
<a id="l00103"></a>#ifdef __cplusplus
<a id="l00104"></a>}
<a id="l00105"></a>#endif
<a id="l00106"></a>
<a id="l00107"></a>#endif /* ZEPHYR_INCLUDE_SHELL_SHELL_HISTORY_H_ */
</code></pre>

## 4.2\_可见注释译文（Comments）

1. 版权与许可证：Copyright (c) 2018 Nordic Semiconductor ASA；SPDX-License-Identifier: Apache-2.0。原始法律声明保留。

2. ZEPHYR_INCLUDE_SHELL_SHELL_HISTORY_H_头文件包含保护结束。

## 4.3\_原页符号提示（Symbol Descriptions）

### `dlist.h`

双向链表（Doubly-linked List）API的头文件。

符号定位：[dlist.h](../dlist_reference/P002_双向链表头文件参考.md)。

### `sys_dnode_t`

```c
struct _dnode sys_dnode_t
```

双向链表节点结构（Node Structure）。

定义位置（Definition）：dlist.h:59。

符号定位：[sys_dnode_t](../dlist_reference/P001_双向链表公共接口.md#ga57fdb936802a617d16c00ab08cd2ad98)。

### `sys_dlist_t`

```c
struct _dnode sys_dlist_t
```

双向链表结构（List Structure）。

定义位置（Definition）：dlist.h:55。

符号定位：[sys_dlist_t](../dlist_reference/P001_双向链表公共接口.md#gaa03f9557215b486fee1039dd4c07e683)。

### `kernel.h`

公共内核 API（Public Kernel APIs）。

符号定位：[kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)。

### `ring_buffer.h`

简单的纯头文件环形缓冲区（Ring Buffer）实现。

符号定位：[ring_buffer.h](../ringbuffer_reference/P003_环形缓冲区头文件参考.md)。

### `stdbool.h`

符号定位：[stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)。

### `true`

```c
#define true
```

定义位置（Definition）：stdbool.h:14。

符号定位：[true](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#a41f9c5fb8b08eb5dc3edce4dcb37fee7)。

### `uint8_t`

```c
__UINT8_TYPE__ uint8_t
```

定义位置（Definition）：stdint.h:88。

符号定位：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

### `uint16_t`

```c
__UINT16_TYPE__ uint16_t
```

定义位置（Definition）：stdint.h:89。

符号定位：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

### `util.h`

杂项工具（Miscellaneous Utilities）。

符号定位：[util.h](../util_reference/P002_通用工具头文件参考.md)。

## 4.4\_源码跟踪译注

> 译注——历史实例使用内核堆（Kernel Heap）存储双向链表条目。当前put忽略空行和与最新条目完全相同的命令，空间不足时移除最旧条目以尝试分配；这不是按固定命令条数构造的队列。

> 译注——当前get把整条历史命令复制到dst并追加NUL，虽然原始头文件把len写作输入输出容量，该版本实现没有读取其输入值来限制复制。调用方必须保证目标空间可容纳命令和终止字符，不能把len当作已实现的截断保护。

> 译注——mode_exit仅将当前浏览指针置空；purge才删除全部条目。active表示是否处于历史浏览模式，不表示历史中是否保存了命令。

头文件定位：[include/zephyr/shell/shell_history.h](../../../include/zephyr/shell/shell_history.h)，关联实现／接口：[subsys/shell/shell_history.c](../../../subsys/shell/shell_history.c)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/shell/shell_history.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/shell_history.c)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 4.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P003_Shell命令历史头文件参考.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [zephyr/sys/dlist.h](../dlist_reference/P002_双向链表头文件参考.md)
- [zephyr/sys/ring_buffer.h](../ringbuffer_reference/P003_环形缓冲区头文件参考.md)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [sys_dlist_t](../dlist_reference/P001_双向链表公共接口.md#gaa03f9557215b486fee1039dd4c07e683)
- [sys_dnode_t](../dlist_reference/P001_双向链表公共接口.md#ga57fdb936802a617d16c00ab08cd2ad98)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [true](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#a41f9c5fb8b08eb5dc3edce4dcb37fee7)

---

[上一章](P003_Shell命令历史头文件参考.md) · [返回大纲](大纲.md) · [下一章](P005_Shell字符串转换头文件参考.md)
