---
id: learning.zephyr-docs.shell-backend-reference.page-3
title: Shell后端选择头文件源码
kind: reference
status: maintained
domains: [zephyr, kernel, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/shell__backend_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_Shell后端选择头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/shell__backend_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；相关页面见[头文件参考](P002_Shell后端选择头文件参考.md)和[公共接口](P001_Shell后端目录.md)；访问语义和生命周期见本页译注。

## 3.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="foldopen00054"></a>
<a id="foldopen00068"></a>
<a id="agroup__iterable__section__apis_html_ga583e57b527884034116bf0b27a942b50"></a>
<a id="agroup__iterable__section__apis_html_ga5f3ecbd953df825cadb2d08f55bc505c"></a>
<a id="agroup__shell__backends_html_ga34edbd459f8acce386a2f953bc6c795f"></a>
<a id="agroup__shell__backends_html_gad299b24f7d116d733c3f9ccc839fdb2b"></a>
<a id="agroup__shell__backends_html_gafcf533acf3e0540c6798e58d4c1f7528"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="ashell_2shell_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructshell_html"></a>
<a id="asys_2iterable__sections_8h_html"></a>

<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * Copyright (c) 2023 Meta
<a id="l00003"></a> *
<a id="l00004"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00005"></a> */
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>#ifndef ZEPHYR_INCLUDE_SHELL_SHELL_BACKEND_H_
<a id="l00014"></a>#define ZEPHYR_INCLUDE_SHELL_SHELL_BACKEND_H_
<a id="l00015"></a>
<a id="l00016"></a>#include &lt;zephyr/types.h&gt;
<a id="l00017"></a>#include &lt;zephyr/shell/shell.h&gt;
<a id="l00018"></a>#include &lt;zephyr/sys/iterable_sections.h&gt;
<a id="l00019"></a>
<a id="l00020"></a>#ifdef __cplusplus
<a id="l00021"></a>extern "C" {
<a id="l00022"></a>#endif
<a id="l00023"></a>
<a id="l00046"></a>
<a id="l00054"></a>static inline const struct shell *shell_backend_get(uint32_t idx)
<a id="l00055"></a>{
<a id="l00056"></a>        const struct shell *backend;
<a id="l00057"></a>
<a id="l00058"></a>        STRUCT_SECTION_GET(shell, idx, &amp;backend);
<a id="l00059"></a>
<a id="l00060"></a>        return backend;
<a id="l00061"></a>}
<a id="l00062"></a>
<a id="l00068"></a>static inline int shell_backend_count_get(void)
<a id="l00069"></a>{
<a id="l00070"></a>        int cnt;
<a id="l00071"></a>
<a id="l00072"></a>        STRUCT_SECTION_COUNT(shell, &amp;cnt);
<a id="l00073"></a>
<a id="l00074"></a>        return cnt;
<a id="l00075"></a>}
<a id="l00076"></a>
<a id="l00084"></a>const struct shell *shell_backend_get_by_name(const char *backend_name);
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00088"></a>#ifdef __cplusplus
<a id="l00089"></a>}
<a id="l00090"></a>#endif
<a id="l00091"></a>
<a id="l00092"></a>#endif /* ZEPHYR_INCLUDE_SHELL_SHELL_BACKEND_H_ */
</code></pre>

## 3.2\_可见注释译文（Comments）

1. 版权与许可证：Copyright (c) 2023 Meta；SPDX-License-Identifier: Apache-2.0。原始法律声明保留。

2. ZEPHYR_INCLUDE_SHELL_SHELL_BACKEND_H_头文件包含保护结束。

## 3.3\_原页符号提示（Symbol Descriptions）

### `STRUCT_SECTION_GET`

```c
#define STRUCT_SECTION_GET(struct_type, i, dst)
```

从链接段（Section）中取得元素。

定义位置（Definition）：iterable_sections.h:339。

符号定位：[STRUCT_SECTION_GET](../iterable_reference/P001_可遍历段公共接口.md#ga583e57b527884034116bf0b27a942b50)。

### `STRUCT_SECTION_COUNT`

```c
#define STRUCT_SECTION_COUNT(struct_type, dst)
```

统计链接段（Section）中的元素数。

定义位置（Definition）：iterable_sections.h:348。

符号定位：[STRUCT_SECTION_COUNT](../iterable_reference/P001_可遍历段公共接口.md#ga5f3ecbd953df825cadb2d08f55bc505c)。

### `shell_backend_get_by_name`

```c
const struct shell * shell_backend_get_by_name(const char *backend_name)
```

按名称取得后端（Backend）。

符号定位：[shell_backend_get_by_name](P001_Shell后端目录.md#ga34edbd459f8acce386a2f953bc6c795f)。

### `shell_backend_get`

```c
static const struct shell * shell_backend_get(uint32_t idx)
```

按索引取得Shell后端（Backend）。

定义位置（Definition）：shell_backend.h:54。

符号定位：[shell_backend_get](P001_Shell后端目录.md#gad299b24f7d116d733c3f9ccc839fdb2b)。

### `shell_backend_count_get`

```c
static int shell_backend_count_get(void)
```

取得后端数量（Backend Count）。

定义位置（Definition）：shell_backend.h:68。

符号定位：[shell_backend_count_get](P001_Shell后端目录.md#gafcf533acf3e0540c6798e58d4c1f7528)。

### `types.h`

符号定位：[types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)。

### `shell.h`

Shell子系统（Shell Subsystem）的头文件。

符号定位：[shell.h](../shell_core_reference/P002_Shell核心头文件参考.md)。

### `uint32_t`

```c
__UINT32_TYPE__ uint32_t
```

定义位置（Definition）：stdint.h:90。

符号定位：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

### `shell`

Shell实例内部结构（Instance Internals）。

定义位置（Definition）：shell.h:1129。

符号定位：[shell](../shell_core_reference/P004_Shell实例结构.md)。

### `iterable_sections.h`

可遍历段（Iterable Sections）辅助工具。

符号定位：[iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)。

## 3.4\_源码跟踪译注

> 译注——后端索引（Backend Index）来自可遍历链接段（Iterable Section）。应先读取count并保证索引落在接口约定范围内；接口没有承诺越界时返回NULL。按名称查找则遍历Shell实例并用strcmp精确比较，未找到返回NULL。

> 译注——传输后端（Transport Backend）连接Shell与通信通道；日志后端（Log Backend）将日志交给Shell输出。两者职责不同，启用某种传输本身不等价于启用日志输出。

头文件定位：[include/zephyr/shell/shell_backend.h](../../../include/zephyr/shell/shell_backend.h)，关联实现／接口：[subsys/shell/shell.c](../../../subsys/shell/shell.c)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/shell/shell_backend.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/shell.c)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 3.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P002_Shell后端选择头文件参考.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/shell/shell.h](../shell_core_reference/P002_Shell核心头文件参考.md)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [shell](../shell_core_reference/P004_Shell实例结构.md)
- [shell_backend_get](P001_Shell后端目录.md#gad299b24f7d116d733c3f9ccc839fdb2b)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [STRUCT_SECTION_GET](../iterable_reference/P001_可遍历段公共接口.md#ga583e57b527884034116bf0b27a942b50)
- [shell_backend_count_get](P001_Shell后端目录.md#gafcf533acf3e0540c6798e58d4c1f7528)
- [STRUCT_SECTION_COUNT](../iterable_reference/P001_可遍历段公共接口.md#ga5f3ecbd953df825cadb2d08f55bc505c)
- [shell_backend_get_by_name](P001_Shell后端目录.md#ga34edbd459f8acce386a2f953bc6c795f)

---

[上一章](P002_Shell后端选择头文件参考.md) · [返回大纲](大纲.md) · [下一章](P004_Shell虚拟后端接口.md)
